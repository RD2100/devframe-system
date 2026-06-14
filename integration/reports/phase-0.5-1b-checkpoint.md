# Phase 0.5-1B Checkpoint Report

Date: 2026-06-15
Branch: `codex/rdinit-phase-0-5`
Status: checkpoint only, not final acceptance; machine-readable Paper Business Validation report artifact candidate recorded with boundary

## Summary

The superproject governance bootstrap and Phase 0.5 inventory are in place.
Four submodule agents completed contract-focused branches. The parent
superproject has advanced submodule gitlinks to committed branch tips.

## Submodule Branches

| Module | Branch | Status | Review focus |
|---|---|---|---|
| `agent-acceptance` | `codex/paper-archive-final-verdict-boundary` | Pinned at `f3abb20` | Path drift, expired authorization, HUMAN_REQUIRED preservation, paper archive SD-04, dispatch/test-frame/control-plane SD-05, and paper business-validation SD-06 final-verdict boundary |
| `devframe-control-plane` | `codex/lease-source-lock-contracts` | Pinned at `b001cea` | DispatchAssignment, WorkerLease, runtime SourceLock, stale completion, in-memory runtime contract probe, and dry-run state machine |
| `dev-frame-opencode` | `codex/paper-audit-privacy-hard-gate` | Pinned at `08ac4f5` | RuntimeAuthorization, EvidenceManifest, paper schema/fixture readability, runtime/API privacy gate, WriteLab handoff fixture coverage, audit sensitive scan, live WriteLab authorization guard, CLI status boundary, redacted reviewer pack boundary, finalizer acceptance boundary, focused mojibake cleanup, post-run write-set hard gate, paper audit privacy hard gate, Security Preflight P1 reviewed gates, and machine-readable synthetic/offline paper business validation report |
| `test-frame` | `codex/adapter-negative-matrix` | Pinned at `891b106` | Adapter mapping, required/optional profile semantics, fake-green canaries, paper reviewer-pack negative fixtures, business-validation negative fixtures, and business report shape negative fixtures |

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
- Added `agent-acceptance` closure validator SD-04 checks so paper
  reviewer-pack/report/test/zip artifacts cannot claim final verdict authority
  or promote `needs_more_evidence` to final acceptance.
- Added OpenCode goal-runner post-run write-set enforcement. It checks
  `state.json.changed_files` against `allowed_files`, `write_set`, or
  `conflict_registry.write_set`, and fails forbidden/out-of-scope files with
  `diff_scope_ok=false`.
- Expanded paper audit/report hard gates for raw paragraph payloads, WriteLab
  `matched_text`, `text_span`, and payload markers before closeout,
  reviewer-pack, or audit outputs can be considered safe.
- Added Security Preflight P1 fix candidates in OpenCode for deny-by-default
  TaskSpec verification command allowlisting, structured review-recovery
  verdict requirements, and daemon-side queued write authorization/risk gating.
- Followed independent governance review on `4558ab8`, which blocked the naked
  `daemon_write_authorized=True` self-authorization path, then pinned
  `40ee21b` to require structured daemon authorization bound to task, project,
  workflow, source, and expiry.
- Added `test-frame` paper reviewer-pack negative fixtures `NEG-031` through
  `NEG-038` for privacy and fake-green canaries.
- Added `agent-acceptance` SD-05 closure validation so dispatch/test-frame/
  control-plane artifacts and expired authorization cannot claim final
  governance verdict.
- Added `devframe-control-plane` in-memory runtime contract probe for duplicate
  dispatch, stale lease completion, overlapping SourceLock, cancellation after
  completion, retry non-retryable failure, and dispatch-success promotion.
- Added `devframe-control-plane` in-memory dry-run state machine in commit
  `b001cea`, covering dispatch, lease acquire, heartbeat, source lock,
  completion, cancellation, failure, retry, and mechanical-success boundaries.
- Added a machine-readable synthetic/offline Paper Business Validation report
  artifact in `dev-frame-opencode` commit `08ac4f5`, covering `paper
  business-validate`, JSON schema validation, paper command-chain evidence,
  reviewer-pack non-finality, status/final-acceptance separation, redaction
  boundaries, and the current business capability matrix.
- Added `test-frame` paper business-validation and business report negative
  fixtures `NEG-039` through `NEG-048` in commit `891b106`.
- Added `agent-acceptance` SD-06 closure validation in commit `f3abb20` so
  paper business-validation artifacts cannot claim final governance verdict.
- Added `agent-acceptance` SD-07 read-only assessment:
  `SD07_TASKSPEC_REQUIRED` before real-content or live WriteLab pilots.

Security Preflight status:

- Canonical `D:\dev-frame-opencode` master is clean at `3a3aa57`.
- SkillSpector is not available in the current environment; result recorded as
  `TOOL_NOT_AVAILABLE`.
- Focused security review found no P0. P1 findings now have independent review
  pass with boundary after `dev-frame-opencode` commits `4558ab8` and
  `40ee21b`.
- `test-frame` returned `NEGATIVE_MATRIX_REVIEW_PASS`; `agent-acceptance`
  returned `SECURITY_PREFLIGHT_REVIEW_PASS`.
- See `integration/reports/security-preflight-2026-06-15.md`.

Still open:

- Control-plane runtime SourceLock/WorkerLease enforcement.
- Real WriteLab paragraph-text flow requires fresh RuntimeAuthorization.
- SD-07 real-content/live WriteLab RuntimeAuthorization boundary implementation.
- Live daemon worker use should add signed or out-of-band authorization storage
  beyond the current structured task authorization contract.

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
- `dev-frame-opencode\ai-workflow-hub`: with `PYTHONPATH` set to the submodule
  source path, `python -m pytest tests\test_paper_cli_a18b.py tests\test_paper_a23b_closeout_hardening.py tests\test_paper_a26_audit_hardening.py -q` -> `54 passed`.
- `dev-frame-opencode`: with `PYTHONPATH` set to
  `D:\devframe-system\dev-frame-opencode\ai-workflow-hub\src`,
  `python -m pytest ai-workflow-hub\tests\test_security_preflight_p1.py ai-workflow-hub\tests\test_paper_a21_daemon_queue_e2e.py ai-workflow-hub\tests\test_paper_a22_daemon_soak_hardening.py ai-workflow-hub\tests\test_paper_runtime.py -q` -> `144 passed in 13.95s`.
- `dev-frame-opencode`: with `PYTHONPATH` set to
  `D:\devframe-system\dev-frame-opencode\ai-workflow-hub\src`,
  `python -m pytest ai-workflow-hub\tests\test_batch_retry.py ai-workflow-hub\tests\test_stage3b_idempotency.py -q` -> `14 passed in 0.59s`.
- `dev-frame-opencode`: `python -m compileall -q ai-workflow-hub\src` -> passed.
- `dev-frame-opencode`: `git diff --check` -> passed.
- `dev-frame-opencode`: after commit `40ee21b`, with `PYTHONPATH` set to
  `D:\devframe-system\dev-frame-opencode\ai-workflow-hub\src`,
  `python -m pytest ai-workflow-hub\tests\test_security_preflight_p1.py ai-workflow-hub\tests\test_paper_a21_daemon_queue_e2e.py ai-workflow-hub\tests\test_paper_a22_daemon_soak_hardening.py ai-workflow-hub\tests\test_paper_runtime.py -q` -> `146 passed in 12.91s`.
- `dev-frame-opencode`: after commit `40ee21b`, with `PYTHONPATH` set to
  `D:\devframe-system\dev-frame-opencode\ai-workflow-hub\src`,
  `python -m pytest ai-workflow-hub\tests\test_batch_retry.py ai-workflow-hub\tests\test_stage3b_idempotency.py -q` -> `14 passed in 0.60s`.
- `dev-frame-opencode`: after commit `40ee21b`,
  `python -m compileall -q ai-workflow-hub\src` -> passed.
- `dev-frame-opencode`: after commit `40ee21b`, `git diff --check` -> passed.
- `test-frame`: `python -m pytest tests\test_paper_negative_fixtures.py tests\test_gate_semantics.py -q` -> `31 passed`.
- `test-frame`: `python tools\ai_guard.py full` -> `PASS`.
- `devframe-control-plane`: `python -m pytest tests\test_runtime_contract_probe.py -q` -> `8 passed`.
- `devframe-control-plane`: after commit `b001cea`,
  `python -m pytest tests\test_runtime_contract_probe.py -q` -> `14 passed in 0.07s`.
- `agent-acceptance`: `python tests\test_workflow_closure_validation.py` -> `22/22 passed`.
- `agent-acceptance`: `python scripts\qoderwork_task_runner.py finish --task-id devframe-final-verdict-boundary-a1` -> `PASS`.
- `dev-frame-opencode`: with `PYTHONPATH` set to
  `D:\devframe-system\dev-frame-opencode\ai-workflow-hub\src`,
  `python -m pytest ai-workflow-hub\tests\test_paper_business_capability_validation.py -q`
  -> `4 passed in 0.27s`.
- `dev-frame-opencode`: after commit `08ac4f5`, with `PYTHONPATH` set to
  `D:\devframe-system\dev-frame-opencode\ai-workflow-hub\src`,
  `python -m pytest ai-workflow-hub\tests\test_paper_business_capability_validation.py -q`
  -> `7 passed in 0.60s`.
- `dev-frame-opencode`: after commit `08ac4f5`, with `PYTHONPATH` set to the
  submodule source path,
  `python -m pytest ai-workflow-hub\tests\test_paper_cli.py ai-workflow-hub\tests\test_paper_cli_a18.py ai-workflow-hub\tests\test_paper_cli_a18b.py -q`
  -> `97 passed in 3.59s`.
- `dev-frame-opencode`: after commit `08ac4f5`,
  `python -m ai_workflow_hub.cli paper business-validate --output <temp-json>`
  -> generated `profile=paper_business_validation_report`,
  `validation_mode=synthetic_offline`, `candidate_status=BUSINESS_CAPABILITY_VALIDATION_CANDIDATE`,
  `runtime_authorization_required_for_real_content=true`, and 14 command-chain entries.
- `dev-frame-opencode`: with `PYTHONPATH` set to the submodule source path,
  the current paper regression group -> `435 passed in 13.62s`.
- `test-frame`: `python -m pytest tests\test_paper_negative_fixtures.py tests\contracts\test_contracts.py tests\schema\test_canonical.py -q`
  -> `19 passed in 0.17s`.
- `test-frame`: after commit `891b106`,
  `python -m pytest tests\test_paper_negative_fixtures.py tests\contracts\test_contracts.py tests\schema\test_canonical.py -q`
  -> `19 passed in 0.31s`.
- `agent-acceptance`: `python -m pytest tests\test_workflow_closure_validation.py -q`
  -> `23 passed in 0.11s`.
- `agent-acceptance`: `python -m compileall -q scripts\validate_workflow_closure.py` -> passed.

## Known Boundary

`scripts\check-submodules.ps1` should pass after the parent lock files are
updated and all submodule gitlinks are staged.

No package install, npm suite, OpenCode execution, control-plane worker
dispatch, test-frame external capability, real paper-content run, pack, or
validate script was run in this checkpoint. The Python execution added for the
paper gates was local ruff/pytest/schema verification inside
`dev-frame-opencode`. The Paper Business Capability Validation candidate is
synthetic/offline review evidence only; it is not final paper acceptance.
