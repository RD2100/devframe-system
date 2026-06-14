# Paper Feature Status

Date: 2026-06-15
Primary module: `dev-frame-opencode/ai-workflow-hub`
Status: Active development focus; first static privacy/usability contract pinned

## Current Surface

Observed paper functionality includes:

- `aihub paper create`
- `aihub paper run`
- `aihub paper resume`
- `aihub paper status`
- `aihub paper list`
- `aihub paper go`
- `aihub paper ledger`
- `aihub paper audit`
- `aihub paper verify`
- `aihub paper validate`
- `aihub paper evidence`
- `aihub paper checkpoint`
- `aihub paper verify-chain`

Core implementation areas:

- `src/ai_workflow_hub/cli.py`
- `src/ai_workflow_hub/context_layer/adapters/paper_runtime.py`
- `src/ai_workflow_hub/context_layer/adapters/paper_evidence_pipeline.py`
- `src/ai_workflow_hub/context_layer/adapters/paper_acceptance_gate.py`
- `src/ai_workflow_hub/context_layer/adapters/paper_decision_audit.py`
- `src/ai_workflow_hub/context_layer/adapters/paper_issue_ledger.py`
- `src/ai_workflow_hub/context_layer/adapters/writelab_adapter.py`
- `src/ai_workflow_hub/context_layer/adapters/writelab_client.py`
- `src/ai_workflow_hub/workflows/paper_graph.py`
- `src/ai_workflow_hub/workflows/paper_workflow_state.py`
- `src/ai_workflow_hub/domains/paper/contracts/`
- `src/ai_workflow_hub/domains/paper/fixtures/`

## Current Strengths

- Paper workflow has CLI, runtime, graph, ledger, audit, evidence, and human
  gate concepts.
- Privacy redaction exists for sensitive fields such as `paragraph_text` and
  `writelab_token`.
- Run ID sanitization exists.
- There are extensive paper tests and cumulative A66-A120 evidence.
- A120 ZIP evidence now has an independent `PASS_WITH_BOUNDARY` reviewer-side
  verifier in this superproject.

## Priority Gaps

| ID | Severity | Gap | Evidence | Desired outcome |
|---|---|---|---|---|
| PAPER-001 | P1 | User-visible schema/fixture text is mojibake in at least `paper_task_spec.schema.json` and `paper_task_spec.sample.yaml` | Fixed and pinned in `dev-frame-opencode` commit `08c76bb`; JSON/YAML parse and static pytest passed | Preserve field names, required fields, enums, and schema structure in future edits |
| PAPER-002 | P1 | Paper full-text privacy boundary needs a project-level gate | `paper_task_input` and redaction schemas exist, but final integration gate is not yet in this superproject | No real paper full text can enter evidence, memory, or reports without explicit authorization |
| PAPER-003 | P1 | CLI command completeness is broad but not summarized for users | CLI has many commands; no superproject UX matrix yet | One user-facing paper command map and readiness state |
| PAPER-004 | P1 | Runtime success, human_required, blocked, and final acceptance boundaries need integration-level assertions | Paper runtime can pause for human gate | Paper command output cannot become final governance acceptance |
| PAPER-005 | P2 | WriteLab/offline handoff path needs current compatibility proof | WriteLab adapters and schemas exist | Static contract check plus fixture validation |
| PAPER-006 | P2 | Paper evidence reports need redacted reviewer pack shape | Paper evidence schemas exist | Reviewer pack contains summaries/hashes, not private full text |
| PAPER-007 | P2 | Additional user-facing paper adapter/client evidence strings may still contain mojibake | Static sub-agent read on 2026-06-15 | Fix remaining user-visible output strings in a focused follow-up with snapshot checks |

## Paper Completion Criteria

Paper functionality is not complete until all of the following are true:

- User-facing schema and fixture text is readable.
- Paper input classification blocks unsafe full-text use by default.
- Redaction checks prove private paper text is not written to reports, memory,
  logs, or evidence packs.
- Paper CLI commands have a documented command map and expected status meaning.
- `human_required`, `blocked`, and `failed` cannot be reported as accepted.
- Offline handoff and WriteLab adapter paths have static or unit-level evidence.
- A reviewer can inspect paper evidence without seeing raw private paper text.

## Current Paper Branch Evidence

- `dev-frame-opencode` branch: `codex/runtime-authorization-contract`
- Pinned commit: `08c76bbeb743a68b35c33c0357aff057bb69bd49`
- Paper text fix files:
  - `ai-workflow-hub/src/ai_workflow_hub/domains/paper/contracts/paper_task_spec.schema.json`
  - `ai-workflow-hub/src/ai_workflow_hub/domains/paper/fixtures/paper_task_spec.sample.yaml`
- Narrow verification observed by the main thread:
  - Current schema JSON parses successfully.
  - Fixture YAML parses successfully.
  - Mojibake token search in the two files has no matches.
  - `python -m pytest -p no:cacheprovider tests\test_paper_task_spec_contract.py -q` -> `5 passed in 0.09s`.
- Diff shows user-visible description/comment/sample text changes, not field or enum changes.
- Runtime/evidence contracts added in the same branch:
  - `schemas/agent-runtime/runtime-authorization.schema.json`
  - `schemas/agent-runtime/evidence-manifest.schema.json`
  - optional `ExecutionReport` references for runtime authorization, runtime observations, and evidence manifest

Remaining hard boundary: `writelab_client` may send paragraph text to a local
WriteLab API in live paths. Real paper content remains blocked until a fresh
RuntimeAuthorization and privacy attestation explicitly allow that flow.
