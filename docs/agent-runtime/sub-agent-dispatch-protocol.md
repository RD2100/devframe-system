# Sub-Agent Dispatch Protocol (SADP) v1.0

> RD2100 Agent Runtime v2 | 2026-05-28
> Canonical root: `D:\devframe-system`
> Default development workflow for Codex + Claude Code collaboration

---

## 0. Overview

SADP defines the default pattern for multi-agent development:

```
[Codex Goal Agent]                      [Claude Code Agent]
     |                                         |
     |  1. Decompose goal 锟斤拷 TaskSpec            |
     |  2. Dispatch TaskSpec to sub-agent       |
     |---------------------------------------->|
     |                                         | 3. Execute task with full context
     |                                         | 4. Collect evidence (test results, diffs)
     |                                         | 5. Produce ExecutionReport
     |  6. Receive ExecutionReport             |
     |<----------------------------------------|
     |  7. Evaluate against acceptance gates    |
     |  8. Issue next TaskSpec or mark complete |
```

**Roles:**
- **Codex Goal Agent** (planning tier): Decomposes goals, dispatches tasks, evaluates reports, maintains plan state. Uses `update_plan` and `create_goal` tools.
- **Claude Code Agent** (execution tier): Receives TaskSpec, executes implementation, collects evidence, returns ExecutionReport. Uses filesystem, git, test runners.
- **Human Reviewer** (oversight tier): Reviews ExecutionReports for P0/P1 tasks, approves gate decisions, signs off on capability registrations.

**Key Principle**: TaskSpec is a self-contained contract. The sub-agent receives ALL context it needs in the dispatch 锟斤拷 it does not re-derive the goal.

---

## 0.R Mandatory Reviewer Node

SADP separates execution from approval. The executor/fixer may implement code and report evidence, but it must not approve its own work or close P0/P1 findings. Every `@go` run that changes files MUST pass through this state machine:

```text
human_gate
  -> executor/fixer
  -> tester
  -> reviewer
  -> finalizer
```

### 0.R.1 Role Boundaries

| Role | May Produce | Must Not Produce |
|------|-------------|------------------|
| executor/fixer | code changes, execution log, `diff.patch` | `review.md`, `review.yaml`, final pass verdict |
| tester | `test-output.md`, command exit-code evidence | code-quality approval |
| reviewer | `review.md`, `review.yaml`, P0/P1 findings | implementation changes |
| finalizer | `final-report.md`, deterministic artifact summary | reviewer judgment, code-quality approval |

The reviewer MUST run as a separate role/session/model identity from the executor/fixer. Executor reports are claims, not facts.

### 0.R.2 Required Evidence Package

Each `@go` run MUST produce a run evidence directory containing:

```text
diff.patch
test-output.md
safety-report.json
chain-evidence.json
review.md
review.yaml
final-report.md
```

`review.yaml` is machine-readable reviewer evidence. It MUST include:

```yaml
reviewer_role: reviewer
reviewer_id: "<reviewer-session-or-agent-id>"
executor_id: "<executor-session-or-agent-id>"
verdict: pass | blocked | fail | escalate
reviewed_inputs:
  - diff.patch
  - test-output.md
  - safety-report.json
  - chain-evidence.json
findings:
  - id: finding-001
    severity: P0 | P1 | P2 | P3
    status: open | resolved | false_positive
    title: "short finding"
```

### 0.R.3 Finalizer Gate

The finalizer MUST run:

```powershell
python tools/go_evidence.py finalize <run-evidence-dir>
```

If reviewer artifacts are missing, reviewer role is `executor`/`fixer`/`coder`, reviewed inputs are incomplete, or any P0/P1 finding remains unresolved, the final status MUST be `blocked`.

The finalizer may summarize deterministic evidence, but it MUST NOT substitute for reviewer judgment.

---



### 0. Gate 0: Resource Sufficiency Check (BEFORE any TaskSpec)

Before creating any TaskSpec that adds, creates, or introduces something new, the plan agent MUST run the Resource Sufficiency Check per core-008:

```
1. Existence    锟斤拷 Does something already cover this need?
2. Coverage     锟斤拷 Can minimal change to existing cover it?
3. Composition  锟斤拷 Can existing resources be combined?
4. Protocol     锟斤拷 Does existing workflow already handle this?
5. Precedent    锟斤拷 Have lessons learned recorded this pattern?
```

If the check finds existing coverage 锟斤拷 **Do not create TaskSpec. Return reuse plan.**

Execute agent MUST reject any additive TaskSpec that lacks documented sufficiency check.



### 0.0 When SADP Activates

SADP is triggered **explicitly by the user** saying `@go`. In normal conversation (without `@go`), the agent responds directly without the full SADP workflow.

| Trigger | Behavior |
|---------|----------|
| User says `@go` | Full SADP: Gate 0 -> TaskSpec -> dispatch -> review -> regression |
| Normal conversation (no `@go`) | Direct response. No TaskSpec, no dispatch. Keep changes minimal. |

**Why**: Previous auto-trigger rules (3+ files, governance files, task-like instructions) caused SADP to activate during normal collaboration, creating friction. The `@go` signal restores user control over when formal governance applies.

**Exception**: Even without `@go`, agents must still obey P0 hard stops (core-001~008). Gate 0 (core-008) thinking still applies -- don't build unnecessarily -- but without the formal TaskSpec/ExecutionReport/Audit overhead.

### 0.0b Post-Completion Review (Non-@go Mode)

After completing **any non-trivial work** in normal conversation mode (file modifications beyond trivial text fixes), the agent MUST:

1. **Write a summary report** to `reports/auto-review-<topic>-<date>.md` covering: what changed, why, key decisions, files touched.
2. **Dispatch to coding agent** (`deepseek/deepseek-v4-pro`) for regression testing and quality audit at the highest review standard.
3. **Read and apply** the review findings before considering work complete.

This ensures quality assurance without burdening normal conversation with pre-execution formalities.

**Minimum report contents:**
```yaml
- Summary: [one-line description]
- Changed files: [list with paths]
- Key decisions: [why each change was made]
- Verification performed: [what was checked]
- Known gaps: [what was NOT checked]
```

### 0.0a Cumulative Trigger Window (Advisory in @go-Only Mode)

> **@go-only mode**: This section is advisory. Cumulative thresholds inform human judgment but do NOT force SADP activation. SADP activates only via explicit `@go` signal (§0.0).


Governance triggers are evaluated **cumulatively** across the session and objective,
not only per TaskSpec. Splitting a task into smaller parts does not reduce the required governance level.

```yaml
cumulative_trigger_window:
  scope:
    - session_id
    - objective_id
  track:
    - cumulative_write_set        # All files written this session/objective
    - cumulative_new_artifacts    # All new files or modules created
    - cumulative_protected_touches # Count of protected file modifications
    - cumulative_task_count       # Total tasks under same objective
  trigger_sadp_when:
    cumulative_write_set_count_gte: 3
    new_artifacts_count_gte: 1
    protected_touches_gte: 1
    same_objective_task_count_gte: 3
  rule: task_splitting_does_not_reduce_governance_level
  escalation:
    if_cumulative_threshold_crossed: require_plan_review
```

**Advisory rule:** If 3 consecutive tasks under the same objective each modify 1 file,
the cumulative write_set = 3, crossing the advisory threshold.
The agent should not attempt to avoid SADP review by splitting a 3-file change into three 1-file changes.


### 0.1 Gate 0 Ledger (Mandatory TaskSpec Field)

Every TaskSpec that adds, creates, or introduces something new MUST include a `gate_0` YAML block.
This is an **evidence contract**, not a self-attestation.
Boolean fields alone (e.g. `inventory_checked: true`) are **invalid** without accompanying evidence references.

```yaml
gate_0:
  triggered: true
  trigger_reason: [why Gate 0 was triggered]

  # Evidence block — replaces boolean self-attestation.
  # A gate_0 without inventory_evidence is INVALID.
  inventory_evidence:
    queried_sources:           # Which files/registries were actually consulted
      - capability-inventory.md
      - sub-agent-dispatch-protocol.md
    matched_capabilities:      # Which capability IDs were found as relevant
      - CAP-011
      - CAP-018
    compared_against_request:  # What user need was checked against inventory
      - "resource routing"
      - "dispatch protocol"

  rules_checked: [list of rule IDs consulted]
  lessons_checked: [list of lesson IDs checked]

  sufficiency_decision: existing_sufficient | existing_partial | new_delta_required | escalate_uncertain
  decision: reuse | build_delta | escalate
  delta_justification: [required if sufficiency_decision is new_delta_required]

  # INVALID gate_0 conditions:
  invalid_if:
    - inventory_evidence.queried_sources is empty
    - inventory_evidence.matched_capabilities is empty and sufficiency_decision is not escalate_uncertain
    - sufficiency_decision is new_delta_required and delta_justification is empty
```

**Rule: missing `gate_0` OR `gate_0` missing `inventory_evidence` => execute agent MUST reject.**


### 0.2 Conflict Registry (Mandatory TaskSpec Fields)

Every TaskSpec MUST declare its file access scope to enable safe parallel dispatch:

```yaml
conflict_registry:
  read_set: [files this task will read]
  write_set: [files this task will modify]
  protected_files_touched: true | false
  conflict_level: none | low | high
```

**Rules:**

1. **Write-set serialization**: If a task's `write_set` overlaps with another active task's `write_set`, tasks MUST be serialized (wait, do not parallel-execute).
2. **Protected files require exclusive lock**: The following files are protected and require an exclusive lock (no other task may read or write them concurrently):
   - `AGENTS.md`, `CLAUDE.md`, `capability-inventory.md`
   - The SADP protocol file (`sub-agent-dispatch-protocol.md`)
   - Core rules (`rules/core.md`)
   - Lessons log (`docs/agent-runtime/lessons-learned.md`)
3. **No git merge as primary resolution**: Agents MUST NOT rely on git merge as the primary conflict resolution mechanism. Serialization and exclusive locks are the mandatory approach.

## 1. TaskSpec Format

Every task dispatched from Codex Goal Agent to Claude Code Agent uses this format:

```markdown
## Task: [title]

- **ID**: task-[8-char-uuid]
- **Batch**: batch-[name]
- **Risk**: low | medium | high | critical
- **Priority**: P0 | P1 | P2 | P3
- **Goal**: [1-3 sentence concrete objective]
- **Context**: [what happened before this task, relevant state]
- **Allowed Files**: [explicit paths, never "any" or "all"]
- **Forbidden**: [explicit constraints: no edits to X, no package install, etc.]
- **Gate 0 Ledger**:
  ```yaml
  gate_0:
    triggered: true
    trigger_reason: [why Gate 0 was triggered]
    inventory_evidence:
      queried_sources: [files checked]
      matched_capabilities: [capability IDs found relevant]
      compared_against_request: [need checked]
    rules_checked: [list of rule IDs consulted]
    lessons_checked: [list of lesson IDs checked]
    sufficiency_decision: existing_sufficient | existing_partial | new_delta_required | escalate_uncertain
    decision: reuse | build_delta | escalate
    delta_justification: [required if sufficiency_decision is new_delta_required]
  ```
- **Conflict Registry**:
  ```yaml
  conflict_registry:
    read_set: [files this task will read]
    write_set: [files this task will modify]
    protected_files_touched: true | false
    conflict_level: none | low | high
  ```
- **Acceptance Gates**:
  1. [gate-1: e.g., `cargo build` exits 0]
  2. [gate-2: e.g., test X passes]
  3. ...
- **Expected Output**: [files created/modified, artifacts produced]
- **Rollback**: [command to undo if blocked]
- **Report To**: [where to return ExecutionReport 锟斤拷 default: calling agent session]
```

### Example

```markdown
## Task: Add rate-limiting middleware

- **ID**: task-a1b2c3d4
- **Batch**: batch-api-hardening
- **Risk**: medium
- **Priority**: P1
- **Goal**: Add a rate-limiting middleware to the Express API that limits requests to 100/min per IP using express-rate-limit.
- **Context**: Previous task added helmet middleware. API entry is `src/app.ts:42`.
- **Allowed Files**:
  - `src/middleware/rateLimiter.ts` (new)
  - `src/app.ts` (add middleware registration only)
  - `tests/middleware/rateLimiter.test.ts` (new)
- **Forbidden**:
   - Do not modify any other middleware
   - Do not change the Express app structure
   - Do not add npm packages other than express-rate-limit
- **Gate 0 Ledger**:
  ```yaml
  gate_0:
    triggered: true
    trigger_reason: "New middleware introduced; Gate 0 required per core-008"
    inventory_evidence:
      queried_sources:
        - capability-inventory.md
        - sub-agent-dispatch-protocol.md
      matched_capabilities:
        - rate-limiting (partial coverage via proxy, no in-app middleware)
        - express-middleware (existing helmet middleware)
      compared_against_request:
        - "in-app rate limiting per route"
    rules_checked:
      - core-008
      - coding-005
    lessons_checked:
      - LL-003
    sufficiency_decision: new_delta_required
    decision: build_delta
    delta_justification: "No in-app rate-limiting exists; proxy config does not cover per-route limits"
  ```
- **Conflict Registry**:
  ```yaml
  conflict_registry:
    read_set:
      - src/app.ts
      - src/middleware/ (existing patterns)
    write_set:
      - src/middleware/rateLimiter.ts
      - src/app.ts
      - tests/middleware/rateLimiter.test.ts
    protected_files_touched: false
    conflict_level: low
  ```
- **Acceptance Gates**:
   1. `npm test -- tests/middleware/rateLimiter.test.ts` passes
   2. `npm run build` succeeds
   3. No regression in existing tests (`npm test`)
- **Expected Output**: rateLimiter.ts, updated app.ts, rateLimiter.test.ts
- **Rollback**: `git checkout -- src/app.ts && rm src/middleware/rateLimiter.ts tests/middleware/rateLimiter.test.ts`
- **Report To**: return ExecutionReport to this session
```

---

## 2. ExecutionReport Format

Every task completion returns this format:

```markdown
## ExecutionReport: [task-id]

- **Status**: pass | fail | blocked | escalate
- **Review Status**: draft | submitted | reviewed | accepted | rejected
- **Summary**: [1-3 sentences: what was done, what was found]
- **Changed Files**:
  - `path/to/file.ts` (+N lines, -M lines) 锟斤拷 [what changed]
  - ...
- **Unchanged But Inspected**:
  - `path/to/file.ts` 锟斤拷 [why inspected, why not changed]
- **Evidence**:
  - Test results: [command + output summary]
  - Build: [pass/fail]
  - Lint: [pass/fail + any new warnings]
- **Risks**:
  - [anything the next agent or reviewer should watch for]
- **Reviewer Index**:
  - `path/to/critical-change.ts` 锟斤拷 [why review recommended]
  - ...
- **Next Steps Suggested**:
  - [optional: what logically follows]
- **Capabilities Used**:
  - [capability name] 锟斤拷 [Status: approved]
```

### Example

```markdown
## ExecutionReport: task-a1b2c3d4

- **Status**: pass
- **Review Status**: accepted
- **Summary**: Added rate-limiting middleware (100 req/min per IP). All tests pass, no regression.
- **Changed Files**:
  - `src/middleware/rateLimiter.ts` (+45 lines) 锟斤拷 new middleware
  - `src/app.ts` (+3 lines, -0 lines) 锟斤拷 registered middleware at line 48
  - `tests/middleware/rateLimiter.test.ts` (+62 lines) 锟斤拷 6 test cases
- **Evidence**:
  - `npm test -- tests/middleware/rateLimiter.test.ts`: 6/6 PASS
  - `npm test`: 47/47 PASS (no regression)
  - `npm run build`: success
- **Risks**: None. Rate limit window (1 min) may need tuning under real load.
- **Reviewer Index**:
  - `src/middleware/rateLimiter.ts:30-35` 锟斤拷 sliding window logic, verify correctness
- **Capabilities Used**:
  - rg/Grep/Read 锟斤拷 Status: approved
  - Shell (read-only) 锟斤拷 Status: approved
```

---

## 3. Dispatch Flow

### 3.1 Codex Goal Agent (Plan 锟斤拷 Dispatch)

1. **Goal agent** enters goal mode (`<goal_context>` active)
2. **Decomposes** goal into batch(es) of tasks using `update_plan`
3. **Dispatches** each task as a self-contained TaskSpec block
4. The sub-agent session receives the TaskSpec as its primary instruction
5. TaskSpec includes ALL context 锟斤拷 sub-agent does not re-derive

### 3.2 Claude Code Agent (Execute 锟斤拷 Report)

1. **Receives** TaskSpec as session instruction
2. **Reads** allowed files, notes forbidden constraints
3. **Executes** the task: reads, edits, tests
4. **Collects evidence**: test output, build results, git diff stats
5. **Returns** ExecutionReport to the goal agent session

### 3.3 Goal Agent (Evaluate 锟斤拷 Next)



### 3.3a Plan Auditor (Independent Compliance Check)

> **Session type matters**: For `@go` sessions, full SADP compliance is required. For non-`@go` sessions, compliance is governed by §0.0b (post-completion review), not by full SADP requirements. The Plan Auditor must distinguish session types before applying audit rules.


Before accepting any session that produces file changes, an independent Plan Auditor must verify SADP compliance.

**Principle**: Plan Agent must not audit its own compliance. Independent Evidence Before Acceptance.

**Auditor Role**:
- Verifies SADP trigger conditions were correctly identified
- Verifies TaskSpec exists when required (anti-LL-009)
- Verifies Gate 0 contains inventory_evidence, not just boolean fields
- Verifies ExecutionReport exists and covers actual changed files
- Verifies read_set/write_set matches git diff
- Verifies protected file access was reported
- Verifies cumulative trigger window was not bypassed by task splitting
- Does NOT re-judge implementation quality or architecture decisions

**Audit Inputs** ([Session Ledger](session-ledger.schema.md)):
- session_id, objective, changed_files list
- taskspecs_created, execution_reports_created
- protected_files_touched, cumulative_write_set
- sadp_required flag, audit_status

**Audit Outputs** ([Audit Record](audit-record.schema.md)):
- findings: structured pass/fail for each compliance check
- issues: list of violations with severity (block/warn)
- decision: pass | block | escalate
- rationale: evidence-based explanation

**Decision Rules**:

| Condition | Decision |
|-----------|----------|
| All findings pass, no issues | **pass** |
| Missing TaskSpec when SADP required | **block** |
| Gate 0 without inventory_evidence | **block** |
| ExecutionReport missing after execution | **block** |
| Changed files not covered by any ExecutionReport | **block** |
| Protected files touched but not reported | **block** |
| Cumulative trigger bypass detected | **block** |
| Auditor uncertain, governance files touched | **escalate** |
| Auditor uncertain, low-risk non-governance | **pass** (with warn) |

**Hard Rule**: Any session that produces file changes must produce an Audit Record before finalization, commit, merge, or handoff. Plan Agent cannot audit or approve its own compliance.

**Anti-Bypass**: Audit trigger is based on session diff and changed_files, not Plan Agent self-report. If changed_files is non-empty and no Audit Record exists, the session is blocked by default.

**Anti-Recursion**: Plan Auditor only checks structured evidence consistency. It does not create new governance rules. Uncertainty → escalate to Human, not to another auditor. No Audit-Auditor.

**Cost Model**: Low-risk non-governance sessions pass on static ledger check (0 LLM calls). High-risk or governance-touching sessions trigger 1 LLM audit call (max 1 per session).

### 3.3b Plan Agent Review Procedure (Mandatory After Every ExecutionReport)

Before accepting an ExecutionReport and dispatching the next task, the plan agent MUST run this review checklist:

```yaml
plan_agent_review:
  gate_evaluation:
    - gate_id: [each acceptance gate from TaskSpec]
      status: pass | fail
      evidence: [actual output matching gate condition]

  regression_tests:
    audit_type: full | targeted
    checks:
      - R1: core_rules_integrity       # All existing rule IDs still present
      - R2: capability_inventory_count  # No capability entries lost
      - R3: lessons_integrity           # All lesson IDs still present
      - R4: file_size_sanity            # No file exploded beyond expected bounds
      - R5: markdown_structure          # All code blocks closed, no broken YAML
      - R6: task_template_intact        # TaskSpec format still valid after modifications
    result: pass | fail | false_positive

  changed_files_audit:
    - file: [path]
      expected_change: [what should have changed]
      actual_change: [what actually changed]
      unexpected_modifications: [files changed but not in TaskSpec allowed_files]

  decision: accept | reject | request_revision
```

**Regression Test Triggers:**
- `full` — after any task that modifies governance files (rules, protocols, inventory, lessons, AGENTS.md)
- `targeted` — after tasks that modify only application code (check only affected modules)

**Decision Rules:**
- All gates PASS + regression PASS → `accept`, dispatch next task
- Gate FAIL → `request_revision` back to execute agent with specific gate failure
- Regression FAIL → `reject`, halt batch, flag for human review
- Unexpected file modifications → `reject`, potential scope violation


1. **Receives** ExecutionReport
2. **Evaluates** against acceptance gates:
   - All gates PASS 锟斤拷 mark task complete, dispatch next if any remain
   - Any gate FAIL 锟斤拷 analyze, possibly revise TaskSpec and re-dispatch
   - BLOCKED 锟斤拷 escalate to human reviewer
3. **Updates** `update_plan` with new status
4. **Dispatches** next task or marks goal complete

---

## 4. Integration Points

### 4.1 dev-frame (Task State Machine)

AI Workflow Hub (`D:\dev-frame\ai-workflow-hub`) is inside the governance boundary as the future/reference control-plane task state machine:
- `tasks.yaml`: Task definitions with status, risk, dependencies
- `projects.yaml`: Project registry with enabled/disabled state
- SADP TaskSpec maps to ai-workflow-hub task format:
  - `TaskSpec.ID` 锟斤拷 `tasks.yaml: id`
  - `TaskSpec.Risk` 锟斤拷 `tasks.yaml: risk`
  - `TaskSpec.Goal` 锟斤拷 `tasks.yaml: description`
  - `ExecutionReport.Status` 锟斤拷 `tasks.yaml: status`

Phase 0-5 boundary: this mapping is reference-only unless a separate human-gated task authorizes dev-frame writes or execution. Agents MUST NOT update `D:\dev-frame\ai-workflow-hub\tasks.yaml`, run ai-workflow-hub, or generate GateResult from dev-frame by default.

Future authorized control-plane updates use this shape:
```yaml
- id: task-a1b2c3d4
  status: completed    # or failed, blocked
  last_run_id: run-[uuid]
```

### 4.2 test-frame (Evidence Collection)

TestFrame (`D:\test-frame`) provides evidence patterns:
- ExecutionReport.Evidence follows test-frame evidence provider contract
- Historical evidence (pre-existing test results) marked as `historical`
- Current evidence (this session) marked as `current, collected YYYY-MM-DD`
- GateResult: NEVER produced by sub-agent 锟斤拷 reviewer decides

### 4.3 Capability Inventory

Every capability used in a task must appear in `capability-inventory.md` with `Status: approved`. The ExecutionReport.CapabilitiesUsed field enables automated capability audit (reviewer-playbook Step 8a).

---




### 4.4 Dispatch Model Selection (Decision Tree)

Before dispatching, consult [Dispatch Model Profiles](dispatch-model-profiles.md):

```
Task involves code files (.ps1/.py)?
  锟斤拷锟斤拷 Yes 锟斤拷 Use deepseek-chat or execute directly (Codex)
  锟斤拷锟斤拷 No 锟斤拷 Task involves .md files?
            锟斤拷锟斤拷 锟斤拷2 files 锟斤拷 deepseek-v4-pro (fast, cheap)
            锟斤拷锟斤拷 3-5 files 锟斤拷 deepseek-chat (capable)
            锟斤拷锟斤拷 6+ files 锟斤拷 Codex direct (no tool timeout)
```

**Operational checks before dispatch:**
1. Close opencode desktop app (process conflict)
2. Keep prompt <500 chars
3. Target files <5KB each
4. Confirm `dev-frame-opencode Dispatch` is approved in `capability-inventory.md`
5. Confirm `tool-policy.md` allows the exact `opencode run` command class
6. Verify `opencode run "say ok"` only when the current task has a human gate for opencode execution

**Failure fallback:** If dispatch times out twice, execute task directly as Codex goal agent and note in ExecutionReport.

### 4.4b CDP Write Adapter (Multi-GPT Dispatch)

For real multi-GPT execution where workers must run in **independent ChatGPT sessions**, use the CDP Write Adapter:

```
scripts/cdp_write_adapter.py   — low-level CDP WebSocket client
scripts/cdp_dispatch_runner.py — orchestration: plan → adapter → evidence
```

**Dispatch flow:**
1. `cdp_dispatch_runner.py status` — verify plan READY, binding active, CDP live
2. `cdp_dispatch_runner.py dry-run` — validate all connections without sending
3. `cdp_dispatch_runner.py run --wave parallel` — inject TaskSpecs into ChatGPT tabs

**Requirements:**
- Chrome with `--remote-debugging-port=9222` (see `multi_cdp_launcher.py`)
- Python `websockets` library ≥ 13 (Chrome 149+ rejects synchronous `websocket-client`)
- At least one open `chatgpt.com/c/<conversation-id>` tab per worker
- CAP-030 registered in capability-inventory.md

**Honesty rule:** When using sub-agent dispatch (QoderWork Task tool) instead of CDP Write, the dispatch report must honestly declare that workers share a single session. The CDP adapter provides real independent multi-GPT execution.

### 4.5 WorkQueue (Task Dispatch Queue)

Agent WorkQueue (`D:\devframe-system\agent-acceptance\agent-workqueue`) provides tier-graded task management:
- Tasks flow: WorkQueue.create 锟斤拷 SADP dispatch 锟斤拷 Claude Code execute 锟斤拷 ExecutionReport 锟斤拷 WorkQueue.complete
- Priority tiers: P0 (critical) 锟斤拷 P1 (high) 锟斤拷 P2 (normal) 锟斤拷 P3 (low)
- Each task gets a WorkQueue ID that maps to TaskSpec.ID
- Dry-run mode: inspect queue without dispatch (Phase 0-5 authorized)

### 4.6 Scripts (Verification Runners)

PowerShell runners (`D:\devframe-system\agent-acceptance\scripts`) provide automated verification:
- Source inspection authorized (read script contents, understand what it does)
- Execution requires ScriptSafetyRecord + separate human gate
- Script paths documented in capability-inventory.md

## 5. Bootstrap Integration

When a project is bootstrapped with `bootstrap.ps1`, the generated AGENTS.md includes:

```markdown
## Default Development Process: Sub-Agent Dispatch

This project uses the [Sub-Agent Dispatch Protocol](docs/agent-runtime/sub-agent-dispatch-protocol.md).
The Codex goal agent plans and dispatches; the Claude Code agent executes and reports.

- All tasks dispatched via TaskSpec format (self-contained contract)
- All results returned via ExecutionReport format (evidence-backed)
- Capability usage tracked against capability-inventory.md
- Acceptance gates must pass before next dispatch
```

---

## 6. Phase 0-5 Constraints

- TaskSpec dispatch does NOT violate Phase 0-5 boundaries:
  - No package install unless explicitly authorized in Forbidden section (default: forbidden)
  - No git mutations unless explicitly authorized (default: no commit without human gate)
  - No capability use without inventory registration (core-007)
- ExecutionReport preserves audit trail for human review
- All evidence is verifiable: test commands with output, file paths with line counts

---

## 7. E2E Acceptance Test

To verify the protocol works end-to-end:

1. Codex goal agent creates a TaskSpec for a trivial task (e.g., "add a comment to README.md")
2. Claude Code agent receives, executes, returns ExecutionReport
3. Goal agent evaluates, marks complete

Expected: full cycle completes within one goal turn, all gates PASS.

---

>
## 8. Phase Exit Authorization (2026-05-28)

Reviewer: RD. The following Phase 0-5 constraints are lifted for SADP operation:

| Capability | Previous | Now | Scope |
|------------|----------|-----|-------|
| dev-frame | design_only | adapter_dry_run | Read-only command inspection |
| test-frame | historical_only | current_evidence | Read evidence/reports/test-results |
| WorkQueue | read_only | dry_run_dispatch | Inspect tasks, no execution |
| Scripts | not_run | source_inspection | Read source, no execution |
| SADP | protocol_only | full_dispatch | TaskSpec 锟斤拷 ExecutionReport cycle |

Test execution, package install, git mutations, and MCP changes remain forbidden without separate human gate.


**Version**: 1.0 | **Status**: approved | **Replaces**: ad-hoc goal-mode handoffs


### 4.7 Fallback Matrix

When SADP dispatch fails, agent must classify and route per risk level:

```yaml
fallback_policy:
  low_risk_docs:
    allowed_fallback: codex_direct
    require_audit: true
  medium_risk_code:
    allowed_fallback: backup_model_dry_run
    forbid: direct_write_without_review
    require_audit: true
  high_risk_architecture:
    allowed_fallback: pause_and_escalate
    forbid: auto_fallback, silent_fallback
    require_audit: true
  governance_modification:
    allowed_fallback: none
    forbid: any_auto_fallback
    require_audit: true
```

**Rules:**
1. Classify failure type (api_key_expired, cli_changed, model_unavailable, timeout, unknown) before choosing fallback.
2. Silent fallback is forbidden at all risk levels. Every fallback must be recorded in ExecutionReport.
3. Governance modification tasks (rules, protocols, AGENTS.md, CLAUDE.md) have zero allowed fallback — must escalate to human.
