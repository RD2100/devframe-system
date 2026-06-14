# Phase 0.5-1B Checkpoint Report

Date: 2026-06-15
Branch: `codex/rdinit-phase-0-5`
Status: checkpoint only, not final acceptance

## Summary

The superproject governance bootstrap and Phase 0.5 inventory are in place.
Four submodule agents completed contract-focused branches. The parent
superproject has advanced submodule gitlinks to committed branch tips.

## Submodule Branches

| Module | Branch | Status | Review focus |
|---|---|---|---|
| `agent-acceptance` | `codex/devframe-system-path-gate0-contract` | Pinned at `88dd581` | Path drift, expired authorization, HUMAN_REQUIRED preservation |
| `devframe-control-plane` | `codex/lease-source-lock-contracts` | Pinned at `49c6be8` | DispatchAssignment, WorkerLease, runtime SourceLock, stale completion |
| `dev-frame-opencode` | `codex/paper-user-visible-mojibake-cleanup` | Pinned at `4ab02c8` | RuntimeAuthorization, EvidenceManifest, paper schema/fixture readability, runtime/API privacy gate, WriteLab handoff fixture coverage, audit sensitive scan, live WriteLab authorization guard, CLI status boundary, redacted reviewer pack boundary, finalizer acceptance boundary, and focused mojibake cleanup |
| `test-frame` | `codex/adapter-negative-matrix` | Pinned at `71caa1c` | Adapter mapping, required/optional profile semantics, fake-green canaries |

## Paper Focus

Completed in the `dev-frame-opencode` submodule branch:

- Fixed user-visible text in `ai-workflow-hub/src/ai_workflow_hub/domains/paper/contracts/paper_task_spec.schema.json`.
- Fixed user-visible text in `ai-workflow-hub/src/ai_workflow_hub/domains/paper/fixtures/paper_task_spec.sample.yaml`.
- Added runtime/evidence boundary contracts for controlled execution review.
- Added `ai-workflow-hub/tests/test_paper_task_spec_contract.py`, a pure static guardrail for schema shape, fixture shape, mojibake regression, and sensitive field redaction contract references.
- Added a runtime/API paper privacy gate that fails raw `paragraph_text` or
  `writelab_token` closed to `human_required` unless explicit
  `RuntimeAuthorization.data_policy` allows the supplied fields.
- Redacted sensitive fields from runtime API return state and human-gate issue
  summaries.
- Restored tracked `mock_handoff.zip` coverage for WriteLab handoff conversion.
- Added a regression test that asserts ZIP `manifest.json` matches the tracked
  `mock_manifest.json`.
- Added an audit ZIP preflight scan that fails closed when candidate text
  artifacts contain unredacted paper sensitive fields, Bearer tokens, WriteLab
  paragraph payloads, or matched-text payloads.
- Added a live WriteLab client authorization guard that fails direct expression
  and paragraph diagnosis calls closed before HTTP dispatch unless
  `RuntimeAuthorization.data_policy` explicitly allows `paragraph_text`.
- Added CLI final-acceptance boundary output and
  `docs/paper/PAPER_CLI_STATUS_MATRIX.md` so workflow status, schema validity,
  and artifact verdicts are not promoted to final paper acceptance.
- Added a redacted `reviewer_pack` boundary to `paper report`, including
  privacy/redaction status, sanitized RuntimeAuthorization metadata,
  artifact/hash pointers, and explicit non-authoritative verdict fields.
- Expanded `schemas/paper_redacted_evidence_pack.schema.json` to validate the
  reviewer pack boundary and prevent treating reviewer-pack output as final
  acceptance.
- Extended report redaction to WriteLab live payload fragments and Bearer
  tokens before closeout/reviewer-pack output is emitted.
- Added production-path `final_acceptance` output in the paper finalizer.
  It is true only for accepted, completed, unblocked runs and ignores
  reviewer-pack, closeout, validation, and artifact-verification claims.
- Cleaned remaining focused mojibake hits in goal-runner review comments and
  reran the Unicode scan across `ai-workflow-hub` source/tests/paper
  docs/schemas; only legitimate BibTeX Latin mappings remain.

Still open:

- Post-run `changed_files subset of write_set` hard gate.
- Real WriteLab paragraph-text flow requires fresh RuntimeAuthorization.
- Archive-side agent-acceptance integration must still reject any promotion
  from report/reviewer-pack output to final acceptance.

## Verification Run

Allowed local verification only:

- `powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\readonly-inventory.ps1` -> passed.
- `python .\scripts\review_a120_evidence_zip.py` -> `PASS_WITH_BOUNDARY`.
- `git diff --check` at superproject root -> passed.
- UTF-8/UTF-8-SIG JSON parse for `integration\` and `schemas\` -> passed, 51 files.
- Submodule `git diff --check` for all four modules -> passed with CRLF warnings only.
- Target JSON/YAML parse in changed submodule contracts -> passed.
- `dev-frame-opencode\ai-workflow-hub`: `python -m pytest -p no:cacheprovider tests\test_paper_task_spec_contract.py -q` -> `5 passed in 0.09s`.
- `dev-frame-opencode\ai-workflow-hub`: `python -m pytest -p no:cacheprovider tests\test_paper_runtime.py -q` -> `80 passed in 13.70s`.
- `dev-frame-opencode\ai-workflow-hub`: `python -m pytest -p no:cacheprovider tests\test_paper_task_spec_contract.py tests\test_paper_cli_a18b.py -q` -> `23 passed in 0.72s`.
- `dev-frame-opencode`: RuntimeAuthorization schema JSON parse -> passed.
- `dev-frame-opencode\ai-workflow-hub`: `python -m pytest -p no:cacheprovider tests\test_writelab_adapter.py -q` -> `63 passed in 0.19s`.
- Wider related paper/WriteLab group:
  `python -m pytest -p no:cacheprovider tests\test_writelab_adapter.py tests\test_writelab_client.py tests\test_paper_acceptance_gate.py tests\test_paper_graph.py -q`
  -> `221 passed in 5.32s`.
- `dev-frame-opencode\ai-workflow-hub`: `python -m pytest -p no:cacheprovider tests\test_paper_a26_audit_hardening.py -q` -> `17 passed in 1.14s`.
- `dev-frame-opencode\ai-workflow-hub`: `python -m pytest -p no:cacheprovider tests\test_paper_a25_audit_package.py tests\test_paper_a26_audit_hardening.py tests\test_paper_cli_a18b.py -q` -> `62 passed in 2.06s`.
- `dev-frame-opencode\ai-workflow-hub`: `python -m pytest -p no:cacheprovider tests\test_paper_runtime.py tests\test_writelab_adapter.py -q` -> `143 passed in 13.20s`.
- `dev-frame-opencode\ai-workflow-hub`: `python -m ruff check src/ai_workflow_hub/context_layer/adapters/writelab_client.py tests/test_writelab_client.py` -> passed.
- `dev-frame-opencode\ai-workflow-hub`: `python -m pytest tests/test_writelab_client.py tests/test_paper_runtime.py tests/test_paper_graph.py tests/test_paper_evidence_pipeline.py tests/test_writelab_adapter.py -q` -> `276 passed in 17.56s`.
- `dev-frame-opencode\ai-workflow-hub`: `python -m pytest tests/test_paper_a19_safe_e2e.py tests/test_paper_a20_real_e2e.py tests/test_paper_a25_audit_package.py tests/test_paper_a26_audit_hardening.py tests/test_paper_a27_audit_polish.py tests/test_paper_a28_verify_command.py -q` -> `115 passed in 4.26s`.
- `dev-frame-opencode\ai-workflow-hub`: `python -m py_compile src/ai_workflow_hub/cli.py` -> passed.
- `dev-frame-opencode\ai-workflow-hub`: `python -m pytest tests/test_paper_cli.py tests/test_paper_a19_safe_e2e.py tests/test_paper_a20_real_e2e.py tests/test_paper_a23_closeout_report.py tests/test_paper_a23b_closeout_hardening.py tests/test_paper_a25_audit_package.py tests/test_paper_a26_audit_hardening.py -q` -> `151 passed in 4.94s`.
- `dev-frame-opencode\ai-workflow-hub`: `python -m pytest tests/test_writelab_client.py tests/test_paper_runtime.py tests/test_paper_graph.py tests/test_paper_evidence_pipeline.py tests/test_writelab_adapter.py -q` -> `276 passed in 15.83s`.
- `dev-frame-opencode\ai-workflow-hub`: `python -m py_compile src/ai_workflow_hub/cli.py` -> passed.
- `dev-frame-opencode\ai-workflow-hub`: `python -m pytest tests/test_paper_a23b_closeout_hardening.py -q` -> `14 passed in 1.12s`.
- `dev-frame-opencode\ai-workflow-hub`: `python -m pytest tests/test_paper_cli.py tests/test_paper_cli_a18b.py tests/test_paper_a19_safe_e2e.py tests/test_paper_a23_closeout_report.py tests/test_paper_a23b_closeout_hardening.py tests/test_paper_a24_artifact_binding.py tests/test_paper_a25_audit_package.py tests/test_paper_a26_audit_hardening.py -q` -> `173 passed in 5.04s`.
- `dev-frame-opencode\ai-workflow-hub`: `python -m pytest tests/test_writelab_client.py tests/test_paper_runtime.py tests/test_paper_graph.py tests/test_paper_evidence_pipeline.py tests/test_writelab_adapter.py -q` -> `276 passed in 16.12s`.
- `dev-frame-opencode\ai-workflow-hub`: `python -m pytest tests/test_paper_a19_safe_e2e.py tests/test_paper_a20_real_e2e.py tests/test_paper_a25_audit_package.py tests/test_paper_a26_audit_hardening.py tests/test_paper_a27_audit_polish.py tests/test_paper_a28_verify_command.py -q` -> `115 passed in 3.84s`.
- `dev-frame-opencode\ai-workflow-hub`: `python -m py_compile src/ai_workflow_hub/workflows/paper_graph.py src/ai_workflow_hub/workflows/paper_workflow_state.py` -> passed.
- `dev-frame-opencode\ai-workflow-hub`: `python -m pytest tests/test_paper_graph.py -q` -> `100 passed in 0.67s`.
- `dev-frame-opencode\ai-workflow-hub`: `python -m pytest tests/test_paper_runtime.py tests/test_paper_cli.py -q` -> `130 passed in 11.97s`.
- `dev-frame-opencode\ai-workflow-hub`: `python -m pytest tests/test_paper_cli.py tests/test_paper_cli_a18b.py tests/test_paper_a19_safe_e2e.py tests/test_paper_a23_closeout_report.py tests/test_paper_a23b_closeout_hardening.py tests/test_paper_a24_artifact_binding.py tests/test_paper_a25_audit_package.py tests/test_paper_a26_audit_hardening.py -q` -> `173 passed in 5.38s`.
- `dev-frame-opencode\ai-workflow-hub`: `python -m pytest tests/test_writelab_client.py tests/test_paper_runtime.py tests/test_paper_graph.py tests/test_paper_evidence_pipeline.py tests/test_writelab_adapter.py -q` -> `278 passed in 16.16s`.
- `dev-frame-opencode\ai-workflow-hub`: `python -m pytest tests/test_paper_a19_safe_e2e.py tests/test_paper_a20_real_e2e.py tests/test_paper_a25_audit_package.py tests/test_paper_a26_audit_hardening.py tests/test_paper_a27_audit_polish.py tests/test_paper_a28_verify_command.py -q` -> `115 passed in 4.01s`.

## Known Boundary

`scripts\check-submodules.ps1` should pass after the parent lock files are
updated and all submodule gitlinks are staged.

No package install, npm suite, OpenCode execution, control-plane worker
dispatch, test-frame external capability, real paper-content run, pack, or
validate script was run in this checkpoint. The Python execution added for the
paper gates was local ruff/pytest/schema verification inside
`dev-frame-opencode`.
