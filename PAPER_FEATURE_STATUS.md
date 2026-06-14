# Paper Feature Status

Date: 2026-06-15
Primary module: `dev-frame-opencode/ai-workflow-hub`
Status: Active development focus; Security Preflight P1 fix candidate ready; runtime/API privacy gate, WriteLab handoff fixture coverage, audit sensitive scan, live WriteLab authorization guard, CLI status boundary, redacted reviewer pack boundary, finalizer acceptance boundary, paper audit privacy hard gate, Security Preflight P1 gates, and cross-module final-verdict boundaries pinned

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
- The paper finalizer now emits `final_acceptance` from the production graph
  path. It is true only for accepted, completed, unblocked runs and ignores
  reviewer-pack/report/artifact validation claims.
- Paper audit/report privacy hard gates now reject or redact direct
  `paragraph`, `matched_text`, and `text_span` payload keys before they can
  enter closeout/reviewer-pack/audit outputs.
- Security Preflight P1 fix candidates now add deny-by-default TaskSpec
  verification command allowlisting, structured review-recovery verdict
  requirements, and daemon-side write authorization/risk gating.
- `test-frame` now carries paper/WriteLab reviewer-pack negative fixtures for
  no-tests-run, fake green, summary-as-final-verdict, artifact outside root,
  token leakage, raw paragraph leakage, `human_required` promotion, and missing
  hash/manifest boundaries.
- `agent-acceptance` now rejects dispatch/test-frame/control-plane evidence and
  expired RuntimeAuthorization when those artifacts try to claim final
  governance acceptance.

## Priority Gaps

| ID | Severity | Gap | Evidence | Desired outcome |
|---|---|---|---|---|
| PAPER-001 | P1 | User-visible schema/fixture text is mojibake in at least `paper_task_spec.schema.json` and `paper_task_spec.sample.yaml` | Fixed and pinned in `dev-frame-opencode` commit `08c76bb`; JSON/YAML parse and static pytest passed | Preserve field names, required fields, enums, and schema structure in future edits |
| PAPER-002 | P1 | Paper full-text privacy boundary needs a project-level gate | Runtime/API gate pinned in `145fc05`; audit bundle sensitive scan pinned in `cb34be3`; live WriteLab authorization guard pinned in `ea0758a`; reviewer-pack boundary pinned in `51215f1`; finalizer acceptance boundary pinned through `4ab02c8`; archive SD-04/SD-05 boundary pinned in `b505bf7`; paper audit privacy hard gate pinned in `8119c85`; Security Preflight P1 gate candidate pinned in `4558ab8`; unauthorized raw `paragraph_text`/`writelab_token` becomes `human_required`, audit ZIP candidates fail closed on unredacted sensitive artifacts, direct live WriteLab calls block before HTTP dispatch without explicit `paragraph_text` authorization, closeout reports carry non-authoritative redacted reviewer-pack metadata, graph finalization cannot be promoted by report/artifact pass fields, closure validation rejects reviewer-pack/report/test/zip/dispatch/test-frame/control-plane final-verdict promotion, and daemon/CLI paths have fix-candidate security gates | Keep real paper content blocked until fresh RuntimeAuthorization is issued and Security Preflight independent review passes |
| PAPER-003 | P1 | CLI command completeness is broad but not summarized for users | Fixed and pinned in `3395033`: `docs/paper/PAPER_CLI_STATUS_MATRIX.md` maps paper commands and three status layers | Keep the matrix current as commands evolve |
| PAPER-004 | P1 | Runtime success, human_required, blocked, and final acceptance boundaries need integration-level assertions | Fixed at CLI boundary in `3395033`, graph finalizer boundary in `ee08dd1`, and archive SD-04 boundary in `1b1fad5`: non-JSON output, JSON/report fields, production finalizer state, and closure validation distinguish workflow status from final acceptance; tests cover accepted, accepted_with_limitation, blocked, needs_more_evidence, fake reviewer-pack/artifact pass fields, and reviewer-pack/report/test/zip promotion attempts | Extend equivalent boundary probes to future dispatch/test-frame runtime artifacts |
| PAPER-005 | P2 | WriteLab/offline handoff path needs current compatibility proof | Fixed and pinned in `dev-frame-opencode` commit `72d1dbd`; tracked `mock_handoff.zip` restored, manifest SHA/size values match ZIP entries, and `test_writelab_adapter.py` now asserts ZIP manifest consistency | Keep the fixture in CI and add future negative fixtures for privacy-attestation and integrity failures |
| PAPER-006 | P2 | Paper evidence reports need redacted reviewer pack shape | Fixed and pinned in `51215f1`: `paper report` includes `reviewer_pack`, `schemas/paper_redacted_evidence_pack.schema.json` validates its boundary fields, and tests prove raw payload/token strings are omitted while summary text cannot override structured acceptance | Keep reviewer-pack schema current as governance-level EvidenceManifest contracts mature |
| PAPER-007 | P2 | Additional user-facing paper adapter/client evidence strings may still contain mojibake | Focused cleanup pinned in `4ab02c8`; Unicode scan of `ai-workflow-hub` source/tests/paper docs/schemas found no remaining target mojibake after cleanup, except legitimate BibTeX Latin character mappings | Keep the scan pattern available for future text/report edits |

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

- `dev-frame-opencode` branch: `codex/paper-audit-privacy-hard-gate`
- Pinned commit: `4558ab819ceacd8998c5b295f51f790c21e55857`
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
- Finalizer acceptance boundary added in commit `ee08dd1`:
  - `ai-workflow-hub/src/ai_workflow_hub/workflows/paper_graph.py`
  - `ai-workflow-hub/src/ai_workflow_hub/workflows/paper_workflow_state.py`
  - `ai-workflow-hub/tests/test_paper_graph.py`
- Verification observed by the main thread for commit `ee08dd1`:
  - `python -m py_compile src/ai_workflow_hub/workflows/paper_graph.py src/ai_workflow_hub/workflows/paper_workflow_state.py` -> passed.
  - `python -m pytest tests/test_paper_graph.py -q` -> `100 passed in 0.67s`.
  - `python -m pytest tests/test_paper_runtime.py tests/test_paper_cli.py -q` -> `130 passed in 11.97s`.
  - `python -m pytest tests/test_paper_cli.py tests/test_paper_cli_a18b.py tests/test_paper_a19_safe_e2e.py tests/test_paper_a23_closeout_report.py tests/test_paper_a23b_closeout_hardening.py tests/test_paper_a24_artifact_binding.py tests/test_paper_a25_audit_package.py tests/test_paper_a26_audit_hardening.py -q` -> `173 passed in 5.38s`.
  - `python -m pytest tests/test_writelab_client.py tests/test_paper_runtime.py tests/test_paper_graph.py tests/test_paper_evidence_pipeline.py tests/test_writelab_adapter.py -q` -> `278 passed in 16.16s`.
  - `python -m pytest tests/test_paper_a19_safe_e2e.py tests/test_paper_a20_real_e2e.py tests/test_paper_a25_audit_package.py tests/test_paper_a26_audit_hardening.py tests/test_paper_a27_audit_polish.py tests/test_paper_a28_verify_command.py -q` -> `115 passed in 4.01s`.
- Focused mojibake cleanup added in commit `4ab02c8`:
  - `ai-workflow-hub/src/ai_workflow_hub/goal_runner.py`
- Verification observed by the main thread for commit `4ab02c8`:
  - Unicode scan across `ai-workflow-hub/src`, `tests`, `docs/paper`, and `schemas` -> `invalid_utf8 0`; no target mojibake findings remain except legitimate BibTeX Latin character mappings.
  - `python -m py_compile src/ai_workflow_hub/goal_runner.py` -> passed.
  - `pytest tests/test_batch_retry.py tests/test_stage3b_idempotency.py -q` -> `11 passed in 0.50s`.
  - `git diff --check` passed with CRLF warnings only.
- Archive-side final verdict boundary added in `agent-acceptance` commit `1b1fad5`:
  - `scripts/validate_workflow_closure.py`
  - `tests/test_workflow_closure_validation.py`
- Verification observed by the main thread for commit `1b1fad5`:
  - `python -m py_compile scripts\validate_workflow_closure.py tests\test_workflow_closure_validation.py` -> passed.
  - `pytest tests\test_workflow_closure_validation.py -q` -> `18 passed in 0.10s`.
  - `pytest tests\test_workflow_closure_validation.py tests\test_paper_acceptance_contracts.py tests\test_paper_privacy_boundaries.py tests\test_paper_go_nogo.py -q` -> `48 passed in 0.20s` with existing tuple-return warnings in `tests/test_paper_acceptance_contracts.py`.
  - Real CLI probe with a synthetic bad `reviewer_pack.json` ZIP -> `WORKFLOW_CLOSURE_VALIDATION.result=fail` and SD-04 blocking issues for final-verdict promotion.
- Post-run write-set hard gate added in commit `7a1278b`:
  - `ai-workflow-hub/src/ai_workflow_hub/goal_runner.py`
  - `ai-workflow-hub/tests/test_batch_retry.py`
- Verification observed by the main thread for commit `7a1278b`:
  - `python -m py_compile src\ai_workflow_hub\goal_runner.py tests\test_batch_retry.py` -> passed.
  - `pytest tests\test_batch_retry.py tests\test_stage3b_idempotency.py tests\test_workflow_nodes.py -q` -> `14 passed, 1 skipped in 0.60s`.
  - `pytest tests\test_paper_runtime.py tests\test_paper_cli.py -q` -> `130 passed in 13.37s`.
  - `git diff --check` passed with CRLF warnings only.
- Paper audit privacy hard gate added in commit `8119c85`:
  - `ai-workflow-hub/src/ai_workflow_hub/cli.py`
  - `ai-workflow-hub/tests/test_paper_cli_a18b.py`
  - `ai-workflow-hub/tests/test_paper_a26_audit_hardening.py`
- Main-thread verification for commit `8119c85`:
  - `PYTHONPATH=D:\devframe-system\dev-frame-opencode\ai-workflow-hub\src; python -m pytest tests\test_paper_cli_a18b.py tests\test_paper_a23b_closeout_hardening.py tests\test_paper_a26_audit_hardening.py -q` -> `54 passed`.
  - `git diff --check` passed.
- Security Preflight P1 gate fix candidate added in commit `4558ab8`:
  - `ai-workflow-hub/src/ai_workflow_hub/cli.py`
  - `ai-workflow-hub/src/ai_workflow_hub/daemon.py`
  - `ai-workflow-hub/tests/test_paper_a21_daemon_queue_e2e.py`
  - `ai-workflow-hub/tests/test_security_preflight_p1.py`
- Main-thread verification for commit `4558ab8`:
  - `PYTHONPATH=D:\devframe-system\dev-frame-opencode\ai-workflow-hub\src; python -m pytest ai-workflow-hub\tests\test_security_preflight_p1.py ai-workflow-hub\tests\test_paper_a21_daemon_queue_e2e.py ai-workflow-hub\tests\test_paper_a22_daemon_soak_hardening.py ai-workflow-hub\tests\test_paper_runtime.py -q` -> `144 passed in 13.95s`.
  - `PYTHONPATH=D:\devframe-system\dev-frame-opencode\ai-workflow-hub\src; python -m pytest ai-workflow-hub\tests\test_batch_retry.py ai-workflow-hub\tests\test_stage3b_idempotency.py -q` -> `14 passed in 0.59s`.
  - `python -m compileall -q ai-workflow-hub\src` -> passed.
  - `git diff --check` passed.
- Paper reviewer-pack negative fixtures added in `test-frame` commit
  `be27de0`:
  - `docs/agent-runtime/negative-test-fixtures/NEG-031` through `NEG-038`
  - `tests/test_paper_negative_fixtures.py`
- Main-thread verification for commit `be27de0`:
  - `python -m pytest tests\test_paper_negative_fixtures.py tests\test_gate_semantics.py -q` -> `31 passed`.
  - `python tools\ai_guard.py full` -> `PASS`.
- Dispatch/test-frame/control-plane final verdict boundary added in
  `agent-acceptance` commit `b505bf7`:
  - `scripts/validate_workflow_closure.py`
  - `tests/test_workflow_closure_validation.py`
  - `docs/agent-runtime/negative-test-fixtures/NEG-039` through `NEG-042`
- Main-thread verification for commit `b505bf7`:
  - `python tests\test_workflow_closure_validation.py` -> `22/22 passed`.
  - `python scripts\qoderwork_task_runner.py finish --task-id devframe-final-verdict-boundary-a1` -> `PASS`.

Current security gate:

- `integration/reports/security-preflight-2026-06-15.md`
- `PROJECT_STAGE: SECURITY_PREFLIGHT_FIX_CANDIDATE_READY`
- P1 security findings have fix candidates pinned in `dev-frame-opencode`
  commit `4558ab8` for TaskSpec command execution boundary, exit-code based
  review recovery, and daemon queued write authorization.
- Independent Security Preflight review is still required before Paper Function
  Business Capability Validation.

Remaining hard boundary: real paper content remains blocked unless a fresh
RuntimeAuthorization with `data_policy.paper_sensitive_input=explicit_allow`,
`redaction_required=true`, `human_gate_ref`, and matching
`allowed_sensitive_fields` explicitly allows that flow. Reviewer-pack output is
redacted evidence for independent review; it is not final acceptance.
