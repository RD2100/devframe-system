# Integration Contracts -- RD2100 Agent Runtime v2

> **Phase 2 Update (2026-05-30)**: BoundaryEnvelope schema defined for future cross-project data flows (Phase 6).
> See `schemas/draft/boundary-envelope.schema.draft.json` (inactive, Phase 6 candidate).


> Batch B1R, 2026-05-27
> Defines 8 core data contracts for the agent runtime.
> Phase 0-5: contracts are defined but not enforced by automated validation.

## Core Contracts (8)

Every agent execution within the runtime produces and consumes these contract types.
Each contract defines: purpose, producer, consumer, required/optional fields, status enum, minimal JSON example, and validation rules.

---

## Contract 1: TaskSpec

| Field | Value |
|-------|-------|
| **Purpose** | Describe a unit of work before execution begins |
| **Producer** | Planner agent or human operator |
| **Consumer** | Executor agent |
| **Status enum** | `draft`, `ready`, `in_progress`, `completed`, `closed`, `deferred`, `rejected`, `accepted_with_limitation`, `pending_human_decision` |
| **Formats** | JSON schema (`task-spec.schema.json`) for machine validation; markdown (SADP protocol section 1) for human-readable dispatch |

### Dual-Format Contract

TaskSpec has one canonical machine contract and one authoring representation:

- **JSON schema** (`schemas/agent-runtime/task-spec.schema.json`): canonical closed machine contract. Used by dispatch plan validators and automated consumers. Unknown or misspelled fields are rejected.
- **Markdown** (SADP protocol section 1): human-readable authoring representation used for agent-to-agent instructions. It must be normalized into the canonical JSON fields before machine validation.

Markdown-only fields are operational instructions, not undeclared JSON extensions. A consumer must map them through the table below; it must not copy arbitrary markdown labels into canonical JSON.

### Field Mapping (JSON ↔ Markdown)

| JSON Schema Field | Markdown Field | Present In | Notes |
|---|---|---|---|
| `task_id` | ID | Both | |
| `title` | (in heading `## Task: [title]`) | Both | |
| `priority` | Priority | Both | |
| `status` | (implicit from workflow) | JSON only | Markdown uses workflow position |
| `description` | Goal + Context | Both | Markdown splits into two fields |
| `depends_on` | (workflow ordering) | JSON only | Markdown uses implicit ordering |
| `assumptions` | Context (partial) | Both | |
| `risk_notes` | Risk | Both | JSON: string; Markdown: enum label |
| `estimated_tools` | (not in markdown) | JSON only | |
| `gate_0` | Gate 0 Ledger | Both | YAML embedded in markdown |
| `conflict_registry` | Conflict Registry | Both | YAML embedded in markdown |
| `security_report` | (not in markdown) | JSON only | Checklist for task completion |
| — | Batch | Markdown only | Organizational grouping |
| — | Allowed Files | Markdown only | Covered by `conflict_registry.write_set` in JSON |
| — | Forbidden | Markdown only | Covered by `deny_paths` in TaskSpec YAML |
| — | Acceptance Gates | Markdown only | Evaluated by the task runner and external review; not copied into TaskSpec JSON |
| — | Expected Output | Markdown only | Covered by `conflict_registry.write_set` in JSON |
| — | Rollback | Markdown only | Operational instruction |
| — | Report To | Markdown only | Session routing |

### Required fields (JSON schema)
| Field | Type | Description |
|-------|------|-------------|
| `task_id` | string | Unique identifier |
| `title` | string | Short description |
| `priority` | enum | `P0`, `P1`, `P2`, `P3` |
| `status` | enum | From 9-value status enum above |
| `description` | string | What to do and why |

### Optional fields (JSON schema)
| Field | Type | Description |
|-------|------|-------------|
| `depends_on` | string[] | Task IDs that must complete first |
| `assumptions` | string[] | Assumptions made when creating this task |
| `risk_notes` | string | Known risks or concerns |
| `estimated_tools` | string[] | Tools likely needed |
| `gate_0` | object | Gate 0 Reuse-before-Build evidence contract |
| `conflict_registry` | object | File access scope for parallel dispatch safety |
| `security_report` | object | Security checklist with explicit `scan_status`; planning begins at `not_run` |

### Minimal JSON
```json
{
  "task_id": "t-001",
  "title": "Inventory agent-acceptance directory",
  "priority": "P1",
  "status": "ready",
  "description": "Run read-only checks on D:\\agent-acceptance and report findings."
}
```

### Validation rules
- `task_id` must be unique within the session
- `priority` must be one of P0/P1/P2/P3
- `status` must be one of the 9-value enum: draft/ready/in_progress/completed/closed/deferred/rejected/accepted_with_limitation/pending_human_decision
- `description` must be non-empty
- `gate_0.inventory_evidence` must include `queried_sources` and `matched_capabilities` when `gate_0.triggered` is true (boolean self-attestation alone is INVALID per LL-007)
- `conflict_registry` must declare `read_set` and `write_set` before execution
- JSON schema sets `additionalProperties: false`; only declared properties are permitted

---

## Contract 2: RunSpec

| Field | Value |
|-------|-------|
| **Purpose** | Record how a task was executed |
| **Producer** | Runner (PowerShell script or agent) |
| **Consumer** | Reviewer agent, verification gates |
| **Status enum** | `pending`, `running`, `completed`, `blocked`, `failed` |

### Required fields
| Field | Type | Description |
|-------|------|-------------|
| `run_id` | string | Unique run identifier |
| `task_id` | string | Reference to TaskSpec |
| `started_at` | ISO8601 | Execution start timestamp |
| `status` | enum | From status enum above |
| `exit_code` | int | 0=PASS, 1=BLOCKED, 2=FAILED |

### Optional fields
| Field | Type | Description |
|-------|------|-------------|
| `finished_at` | ISO8601 | Execution end timestamp |
| `command` | string | Exact command executed |
| `cwd` | string | Working directory |
| `tier` | int | Execution tier (0/1/2) |
| `dry_run` | bool | Whether this was a dry run |
| `error_output` | string | Captured error output |

### Minimal JSON
```json
{
  "run_id": "r-001",
  "task_id": "t-001",
  "started_at": "2026-05-27T10:00:00Z",
  "status": "completed",
  "exit_code": 0
}
```

### Validation rules
- `task_id` must reference an existing TaskSpec
- `status` must be one of pending/running/completed/blocked/failed
- `exit_code` must be 0, 1, or 2
- `started_at` must be before `finished_at` if both present

---

## Contract 3: EvidenceIndex

| Field | Value |
|-------|-------|
| **Purpose** | Index of evidence artifacts produced during a run |
| **Producer** | Executor agent |
| **Consumer** | Reviewer agent, audit trail |
| **Status enum** | `collected`, `verified`, `disputed` |

### Required fields
| Field | Type | Description |
|-------|------|-------------|
| `evidence_id` | string | Unique identifier |
| `run_id` | string | Reference to RunSpec |
| `artifact_path` | string | Path to evidence artifact |
| `artifact_type` | enum | `log`, `screenshot`, `diff`, `report`, `output` |
| `collected_at` | ISO8601 | When evidence was collected |
| `status` | enum | From status enum above |

### Optional fields
| Field | Type | Description |
|-------|------|-------------|
| `checksum` | string | SHA256 of artifact |
| `size_bytes` | int | Artifact file size |
| `notes` | string | Collector notes |

### Minimal JSON
```json
{
  "evidence_id": "ev-001",
  "run_id": "r-001",
  "artifact_path": "runs/powershell-acceptance/smoke-20260527.log",
  "artifact_type": "log",
  "collected_at": "2026-05-27T10:01:00Z",
  "status": "collected"
}
```

### Freshness fields (Phase 2 extension)
| Field | Type | Description |
|-------|------|-------------|
| `freshness` | enum | `historical`, `current`, `stale_or_unknown` |
| `currency_basis` | enum | `approved_run`, `existing_artifact`, `manual_inspection`, `unknown` |
| `approved_run_id` | string | Only if currency_basis=approved_run |

**Freshness policy**:
- `historical` evidence CANNOT be used as current evidence in GateResult
- `current` requires either an `approved_run_id` or reviewer attestation
- Default for pre-existing artifacts: `stale_or_unknown`
- `status=verified` without `freshness=current` is INVALID

### Validation rules
- `run_id` must reference an existing RunSpec
- `artifact_type` must be one of log/screenshot/diff/report/output
- `artifact_path` must be within the project root
- `freshness=current` requires `currency_basis=approved_run` with valid `approved_run_id` (unless reviewer-attested)
- `status=verified` requires `freshness=current`

---

## Contract 4: GateResult

| Field | Value |
|-------|-------|
| **Purpose** | Result of a single verification gate check |
| **Producer** | Verification gate runner |
| **Consumer** | Reviewer agent, release pipeline |
| **Status enum** | `pass`, `fail`, `warning`, `blocked`, `skipped` |

### Required fields
| Field | Type | Description |
|-------|------|-------------|
| `gate_id` | string | Unique gate result identifier |
| `run_id` | string | Reference to RunSpec |
| `gate_level` | enum | `P0`, `P1`, `P2`, `P3` |
| `gate_name` | string | Human-readable gate name |
| `result` | enum | From status enum above |
| `checked_at` | ISO8601 | When check was performed |

### Optional fields
| Field | Type | Description |
|-------|------|-------------|
| `details` | string | Explanation of result |
| `evidence_ids` | string[] | Referenced evidence |
| `recommendation` | string | Suggested action if not pass |

### Minimal JSON
```json
{
  "gate_id": "g-001",
  "run_id": "r-001",
  "gate_level": "P0",
  "gate_name": "Security: No secrets in output",
  "result": "pass",
  "checked_at": "2026-05-27T10:02:00Z"
}
```

### Validation rules
- `gate_level` must be one of P0/P1/P2/P3
- `result` must be one of pass/fail/warning/blocked/skipped
- P0 gate with `fail` result must block delivery (BLOCKED)
- P0 gate with `blocked` result must block delivery (BLOCKED)

---

## Contract 5: ExecutionReport

| Field | Value |
|-------|-------|
| **Purpose** | Final structured report of a batch execution |
| **Producer** | Report generator (Write-Report.ps1 or agent) |
| **Consumer** | Human reviewer, planning agent |
| **Status enum** | `pass`, `fail`, `blocked`, `escalate` |

### Required fields
| Field | Type | Description |
|-------|------|-------------|
| `report_id` | string | Unique report identifier |
| `batch_id` | string | Batch identifier (e.g., "A1", "B1") |
| `generated_at` | ISO8601 | Report generation timestamp |
| `status` | enum | From status enum above |
| `summary` | string | Executive summary |
| `executor_id` | string | Required when `status=pass`; identifies the execution session/agent |

### Optional fields
| Field | Type | Description |
|-------|------|-------------|
| `run_ids` | string[] | Referenced RunSpecs |
| `gate_results` | GateResult[] | Inline gate results |
| `blocking_issues` | string[] | Issues blocking progress |
| `recommendations` | string[] | Suggested next actions |
| `reviewer_decision` | string | Reviewer's gate decision |
| `reviewer_artifacts` | object | Required when `status=pass`; includes review paths, role, verdict, and `reviewer_id` |

### Minimal JSON
```json
{
  "report_id": "rep-001",
  "batch_id": "A1",
  "generated_at": "2026-05-27T10:05:00Z",
  "status": "blocked",
  "summary": "Batch A1 awaits independent review evidence."
}
```

### Validation rules
- `batch_id` must not be empty
- `summary` must not be empty
- If `status` is `pass`, `executor_id` and `reviewer_artifacts` are required
- `reviewer_artifacts.reviewer_id` must differ from `executor_id`; enforce with `scripts/validate_execution_report.py`

---

## Contract 6: SkillIntakeRecord

| Field | Value |
|-------|-------|
| **Purpose** | Record the intake evaluation of an external skill |
| **Producer** | Skill evaluator (agent or human) |
| **Consumer** | Reviewer, future Phase 6+ quarantine pipeline |
| **Status enum** | `reference_only`, `candidate`, `defer`, `reject` |

### Required fields
| Field | Type | Description |
|-------|------|-------------|
| `record_id` | string | Unique record identifier |
| `skill_name` | string | Name of the skill being evaluated |
| `source` | string | Where the skill came from (URL, path, user) |
| `evaluated_at` | ISO8601 | Evaluation timestamp |
| `disposition` | enum | From status enum above |
| `rationale` | string | Why this disposition was chosen |

### Optional fields
| Field | Type | Description |
|-------|------|-------------|
| `risk_level` | enum | `low`, `medium`, `high`, `critical` |
| `declared_tools` | string[] | Tools the skill claims to use |
| `gate_results` | GateResult[] | Gate check results |
| `reviewer_notes` | string | Human reviewer notes |
| `target_phase` | string | Phase when this skill could be reconsidered |

### Minimal JSON
```json
{
  "record_id": "sr-001",
  "skill_name": "example-skill",
  "source": "user request 2026-05-27",
  "evaluated_at": "2026-05-27T10:10:00Z",
  "disposition": "defer",
  "rationale": "Phase 0-5 does not permit skill installation. Re-evaluate in Phase 6."
}
```

### Validation rules
- `disposition` must be one of reference_only/candidate/defer/reject
- `rationale` must be non-empty
- `defer` and `reject` dispositions must include `target_phase` or reason permanently blocked

---

## Contract 7: ToolRiskRecord

| Field | Value |
|-------|-------|
| **Purpose** | Record risk assessment of a tool available to agents |
| **Producer** | Tool policy evaluator |
| **Consumer** | Agent runtime, verification gates |
| **Status enum** | `permitted`, `restricted`, `forbidden_in_phase`, `needs_review` |

### Required fields
| Field | Type | Description |
|-------|------|-------------|
| `record_id` | string | Unique record identifier |
| `tool_name` | string | Tool identifier |
| `risk_level` | enum | `low`, `medium`, `high`, `critical` |
| `phase_policy` | string | Phase range where policy applies (e.g., "Phase 0-5") |
| `classification` | enum | From status enum above |
| `rationale` | string | Why this classification |

### Optional fields
| Field | Type | Description |
|-------|------|-------------|
| `conditions` | string | Conditions under which classification could change |
| `review_date` | ISO8601 | When to re-evaluate |

### Minimal JSON
```json
{
  "record_id": "tr-001",
  "tool_name": "skill-installer",
  "risk_level": "critical",
  "phase_policy": "Phase 0-5",
  "classification": "forbidden_in_phase",
  "rationale": "Skill installation is deferred to Phase 6+ Source Lock & Quarantine."
}
```

### Validation rules
- `risk_level` must be one of low/medium/high/critical
- `classification` must be one of permitted/restricted/forbidden_in_phase/needs_review
- `phase_policy` must specify applicable phase range

---

## Contract 8: MemoryUpdateRecord

| Field | Value |
|-------|-------|
| **Purpose** | Proposed memory update, subject to human approval |
| **Producer** | Agent (proposed only, not written) |
| **Consumer** | Human reviewer (approves/rejects), future Phase writer |
| **Status enum** | `proposed`, `approved`, `rejected`, `superseded` |

### Required fields
| Field | Type | Description |
|-------|------|-------------|
| `record_id` | string | Unique record identifier |
| `proposed_at` | ISO8601 | When proposed |
| `memory_type` | enum | `user`, `feedback`, `project`, `reference` |
| `target_location` | string | Where this would be written |
| `summary` | string | One-line summary of the proposed memory |
| `status` | enum | From status enum above |

### Optional fields
| Field | Type | Description |
|-------|------|-------------|
| `full_content` | string | Full proposed memory content |
| `trigger_event` | string | What triggered this proposal |
| `reviewer` | string | Who should review |
| `approved_at` | ISO8601 | When approved |
| `written_at` | ISO8601 | When actually written (future phase) |

### Minimal JSON
```json
{
  "record_id": "mu-001",
  "proposed_at": "2026-05-27T10:15:00Z",
  "memory_type": "project",
  "target_location": "C:\\Users\\RD\\.claude\\projects\\D--agent-acceptance\\memory\\",
  "summary": "Batch A1 inventory discovered path drift D:\\devFrame vs D:\\dev-frame",
  "status": "proposed"
}
```

### Validation rules
- `memory_type` must be one of user/feedback/project/reference
- `status` must be one of proposed/approved/rejected/superseded
- `target_location` must be a valid path
- Phase 0-5: only `proposed` status allowed for new records

---

## Contract Dependency Graph

```
TaskSpec --> RunSpec --> EvidenceIndex
                  |--> GateResult
                  |--> ExecutionReport

SkillIntakeRecord (independent)
ToolRiskRecord (independent)
MemoryUpdateRecord (independent, proposed-only in Phase 0-5)
```

---

## Appendix: System Integration Notes

These are notes on external system interfaces. They are NOT core contracts.
Core contracts are the 8 defined above.

### A1: ai-workflow-hub (Upstream CLI)
- **Status**: FIXED (Batch E) -- README.md references corrected to `D:\dev-frame`. Claude memory alias `D--devFrame` remains as P3 cosmetic issue.
- **Interface**: CLI via `$env:AI_WORKFLOW_HUB`
- **Direction**: agent-acceptance calls ai-workflow-hub CLI

### A2: CodeGraph (Code Intelligence)
- **Status**: ACTIVE -- dev-frame: 410 files, test-frame: 102 files, agent-acceptance: 0 files
- **Interface**: MCP (codegraph_* tools)
- **Direction**: Agent queries CodeGraph

- **Interface**: MCP (* tools)
- **Direction**: Bidirectional (read: search/recent knowledge; write: register, share_decision, report_bug_pattern)

### A4: test-frame (Future Downstream)
- **Status**: PLANNED

### A5: Memory System (Internal)
- **Status**: PARTIAL -- Phase 0-5 read-only, MemoryUpdateRecord proposals only
