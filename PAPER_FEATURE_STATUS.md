# Paper Feature Status

Date: 2026-06-15
Primary module: `dev-frame-opencode/ai-workflow-hub`
Status: Active development focus; runtime/API privacy gate, WriteLab handoff fixture coverage, audit sensitive scan, live WriteLab authorization guard, CLI status boundary, and redacted reviewer pack boundary pinned

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
- Raw `paragraph_text` and `writelab_token` now fail closed to
  `human_required` unless explicit `RuntimeAuthorization.data_policy` allows
  the supplied fields.
- Runtime API return state and human-gate issue summaries are redacted before
  leaving the adapter boundary.
- Run ID sanitization exists.
- There are extensive paper tests and cumulative A66-A120 evidence.
- A120 ZIP evidence now has an independent `PASS_WITH_BOUNDARY` reviewer-side
  verifier in this superproject.
- WriteLab handoff ZIP fixture coverage is restored with a tracked
  `mock_handoff.zip` and manifest/ZIP consistency test.
- `paper audit` now fails closed before ZIP creation if candidate text artifacts
  contain unredacted paper-sensitive fields or WriteLab payload markers.
- Direct live WriteLab expression and paragraph diagnosis calls now fail closed
  before HTTP dispatch unless `RuntimeAuthorization.data_policy` explicitly
  allows `paragraph_text`.
- Paper CLI now displays final-acceptance boundaries for `paper run`, `go`,
  `resume`, `status`, `validate`, and `report`, and documents the command
  status matrix in `docs/paper/PAPER_CLI_STATUS_MATRIX.md`.
- `paper report` now includes a redacted `reviewer_pack` boundary that records
  privacy/redaction status, RuntimeAuthorization metadata without raw field
  names, artifact/hash pointers, and explicit non-authoritative verdict rules.
- Report redaction now covers WriteLab live payload fragments such as
  `"paragraph"`, `"matched_text"`, `"text_span"`, and `Authorization: Bearer`
  values before they can appear in closeout/reviewer-pack output.

## Priority Gaps

| ID | Severity | Gap | Evidence | Desired outcome |
|---|---|---|---|---|
| PAPER-001 | P1 | User-visible schema/fixture text is mojibake in at least `paper_task_spec.schema.json` and `paper_task_spec.sample.yaml` | Fixed and pinned in `dev-frame-opencode` commit `08c76bb`; JSON/YAML parse and static pytest passed | Preserve field names, required fields, enums, and schema structure in future edits |
| PAPER-002 | P1 | Paper full-text privacy boundary needs a project-level gate | Runtime/API gate pinned in `145fc05`; audit bundle sensitive scan pinned in `cb34be3`; live WriteLab authorization guard pinned in `ea0758a`; reviewer-pack boundary pinned in `51215f1`; unauthorized raw `paragraph_text`/`writelab_token` becomes `human_required`, audit ZIP candidates fail closed on unredacted sensitive artifacts, direct live WriteLab calls block before HTTP dispatch without explicit `paragraph_text` authorization, and closeout reports carry non-authoritative redacted reviewer-pack metadata | Add governance-level finalizer tests before any real paper content run |
| PAPER-003 | P1 | CLI command completeness is broad but not summarized for users | Fixed and pinned in `3395033`: `docs/paper/PAPER_CLI_STATUS_MATRIX.md` maps paper commands and three status layers | Keep the matrix current as commands evolve |
| PAPER-004 | P1 | Runtime success, human_required, blocked, and final acceptance boundaries need integration-level assertions | Fixed at CLI boundary in `3395033`: non-JSON output and JSON/report fields distinguish workflow status from final acceptance; focused CLI tests cover accepted, accepted_with_limitation, blocked, and needs_more_evidence cases | Add remaining governance-level finalizer tests |
| PAPER-005 | P2 | WriteLab/offline handoff path needs current compatibility proof | Fixed and pinned in `dev-frame-opencode` commit `72d1dbd`; tracked `mock_handoff.zip` restored, manifest SHA/size values match ZIP entries, and `test_writelab_adapter.py` now asserts ZIP manifest consistency | Keep the fixture in CI and add future negative fixtures for privacy-attestation and integrity failures |
| PAPER-006 | P2 | Paper evidence reports need redacted reviewer pack shape | Fixed and pinned in `51215f1`: `paper report` includes `reviewer_pack`, `schemas/paper_redacted_evidence_pack.schema.json` validates its boundary fields, and tests prove raw payload/token strings are omitted while summary text cannot override structured acceptance | Keep reviewer-pack schema current as governance-level EvidenceManifest contracts mature |
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

- `dev-frame-opencode` branch: `codex/paper-redacted-reviewer-pack`
- Pinned commit: `51215f1b060fe760ebd0da192f03cb28694411d8`
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
- Paper privacy gate files added or updated in the pinned branch:
  - `ai-workflow-hub/src/ai_workflow_hub/context_layer/adapters/paper_runtime.py`
  - `ai-workflow-hub/tests/test_paper_runtime.py`
  - `schemas/agent-runtime/runtime-authorization.schema.json`
  - `docs/agent-runtime/integration-contracts.md`
- Narrow verification observed by the main thread for commit `145fc05`:
  - `python -m pytest -p no:cacheprovider tests\test_paper_runtime.py -q` -> `80 passed in 13.70s`.
  - `python -m pytest -p no:cacheprovider tests\test_paper_task_spec_contract.py tests\test_paper_cli_a18b.py -q` -> `23 passed in 0.72s`.
  - RuntimeAuthorization schema JSON parses successfully.
  - `git diff --check` passed with CRLF warnings only.
- Handoff fixture coverage added in commit `72d1dbd`:
  - `ai-workflow-hub/src/ai_workflow_hub/context_layer/adapters/writelab_fixtures/mock_handoff.zip`
  - `ai-workflow-hub/src/ai_workflow_hub/context_layer/adapters/writelab_fixtures/mock_manifest.json`
  - `ai-workflow-hub/tests/test_writelab_adapter.py`
- Verification observed by the main thread for commit `72d1dbd`:
  - `python -m pytest -p no:cacheprovider tests\test_writelab_adapter.py -q` -> `63 passed in 0.19s`.
  - `python -m pytest -p no:cacheprovider tests\test_writelab_adapter.py tests\test_writelab_client.py tests\test_paper_acceptance_gate.py tests\test_paper_graph.py -q` -> `221 passed in 5.32s`.
  - `python -m pytest -p no:cacheprovider tests\test_paper_runtime.py -q` -> `80 passed in 13.05s`.
  - `python -m pytest -p no:cacheprovider tests\test_paper_task_spec_contract.py tests\test_paper_cli_a18b.py -q` -> `23 passed in 0.72s`.
- Audit sensitive scan added in commit `cb34be3`:
  - `ai-workflow-hub/src/ai_workflow_hub/cli.py`
  - `ai-workflow-hub/tests/test_paper_a26_audit_hardening.py`
- Verification observed by the main thread for commit `cb34be3`:
  - `python -m pytest -p no:cacheprovider tests\test_paper_a26_audit_hardening.py -q` -> `17 passed in 1.14s`.
  - `python -m pytest -p no:cacheprovider tests\test_paper_a25_audit_package.py tests\test_paper_a26_audit_hardening.py tests\test_paper_cli_a18b.py -q` -> `62 passed in 2.06s`.
  - `python -m pytest -p no:cacheprovider tests\test_paper_runtime.py tests\test_writelab_adapter.py -q` -> `143 passed in 13.20s`.
- Live WriteLab authorization guard added in commit `ea0758a`:
  - `ai-workflow-hub/src/ai_workflow_hub/context_layer/adapters/writelab_client.py`
  - `ai-workflow-hub/tests/test_writelab_client.py`
- Verification observed by the main thread for commit `ea0758a`:
  - `python -m ruff check src/ai_workflow_hub/context_layer/adapters/writelab_client.py tests/test_writelab_client.py` -> passed.
  - `python -m pytest tests/test_writelab_client.py tests/test_paper_runtime.py tests/test_paper_graph.py tests/test_paper_evidence_pipeline.py tests/test_writelab_adapter.py -q` -> `276 passed in 17.56s`.
  - `python -m pytest tests/test_paper_a19_safe_e2e.py tests/test_paper_a20_real_e2e.py tests/test_paper_a25_audit_package.py tests/test_paper_a26_audit_hardening.py tests/test_paper_a27_audit_polish.py tests/test_paper_a28_verify_command.py -q` -> `115 passed in 4.26s`.
- CLI status boundary added in commit `3395033`:
  - `ai-workflow-hub/src/ai_workflow_hub/cli.py`
  - `ai-workflow-hub/tests/test_paper_cli.py`
  - `docs/paper/PAPER_CLI_STATUS_MATRIX.md`
- Verification observed by the main thread for commit `3395033`:
  - `python -m py_compile src/ai_workflow_hub/cli.py` -> passed.
  - `python -m pytest tests/test_paper_cli.py tests/test_paper_a19_safe_e2e.py tests/test_paper_a20_real_e2e.py tests/test_paper_a23_closeout_report.py tests/test_paper_a23b_closeout_hardening.py tests/test_paper_a25_audit_package.py tests/test_paper_a26_audit_hardening.py -q` -> `151 passed in 4.94s`.
  - `python -m pytest tests/test_writelab_client.py tests/test_paper_runtime.py tests/test_paper_graph.py tests/test_paper_evidence_pipeline.py tests/test_writelab_adapter.py -q` -> `276 passed in 15.83s`.
- Redacted reviewer pack boundary added in commit `51215f1`:
  - `ai-workflow-hub/src/ai_workflow_hub/cli.py`
  - `ai-workflow-hub/tests/test_paper_a23b_closeout_hardening.py`
  - `docs/paper/PAPER_CLI_STATUS_MATRIX.md`
  - `schemas/paper_redacted_evidence_pack.schema.json`
- Verification observed by the main thread for commit `51215f1`:
  - `python -m py_compile src/ai_workflow_hub/cli.py` -> passed.
  - `python -m pytest tests/test_paper_a23b_closeout_hardening.py -q` -> `14 passed in 1.12s`.
  - `python -m pytest tests/test_paper_cli.py tests/test_paper_cli_a18b.py tests/test_paper_a19_safe_e2e.py tests/test_paper_a23_closeout_report.py tests/test_paper_a23b_closeout_hardening.py tests/test_paper_a24_artifact_binding.py tests/test_paper_a25_audit_package.py tests/test_paper_a26_audit_hardening.py -q` -> `173 passed in 5.04s`.
  - `python -m pytest tests/test_writelab_client.py tests/test_paper_runtime.py tests/test_paper_graph.py tests/test_paper_evidence_pipeline.py tests/test_writelab_adapter.py -q` -> `276 passed in 16.12s`.
  - `python -m pytest tests/test_paper_a19_safe_e2e.py tests/test_paper_a20_real_e2e.py tests/test_paper_a25_audit_package.py tests/test_paper_a26_audit_hardening.py tests/test_paper_a27_audit_polish.py tests/test_paper_a28_verify_command.py -q` -> `115 passed in 3.84s`.

Remaining hard boundary: real paper content remains blocked unless a fresh
RuntimeAuthorization with `data_policy.paper_sensitive_input=explicit_allow`,
`redaction_required=true`, `human_gate_ref`, and matching
`allowed_sensitive_fields` explicitly allows that flow. Reviewer-pack output is
redacted evidence for independent review; it is not final acceptance.
