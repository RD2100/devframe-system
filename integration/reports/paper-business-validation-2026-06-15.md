# Paper Business Capability Validation Report

Date: 2026-06-15
Status: `PAPER_BUSINESS_VALIDATION_REPORT_ARTIFACT_CANDIDATE`
Boundary: synthetic/offline evidence only; not final paper acceptance

## Summary

The paper feature has advanced from Security Preflight review into a
machine-readable business-capability validation candidate. The candidate is
intentionally scoped to synthetic/offline evidence: it verifies the current
command surface, evidence/reviewer-pack shape, status versus final-acceptance
separation, redaction boundary, and JSON report contract without running real
paper content or live WriteLab flows.

## Sub-Agent Outputs

| Module | Commit | Result | Evidence |
|---|---:|---|---|
| `dev-frame-opencode` | `08ac4f593006d62bf5b096133dfe9212cce8e49f` | Machine-readable business report artifact implemented | `paper business-validate`; `schemas/paper_business_validation_report.schema.json`; `ai-workflow-hub/tests/test_paper_business_capability_validation.py`; `ai-workflow-hub/docs/paper/PAPER_BUSINESS_CAPABILITY_VALIDATION.md` |
| `test-frame` | `891b10658c69356cd5a587c3f120fdfdc2b9cb8d` | Negative matrix extended for report shape | `docs/agent-runtime/negative-test-fixtures/NEG-039` through `NEG-048`; `tests/test_paper_negative_fixtures.py` |
| `agent-acceptance` | `38d7b2e0aad226cce5732cb4d56e45ae2d065ec7` | Governance boundary extended through SD-07 | `scripts/validate_workflow_closure.py`; `tests/test_workflow_closure_validation.py`; `_evidence/paper-business-validation-governance-a1/`; `_evidence/paper-real-content-runtime-authorization-boundary-a1/` |
| `devframe-control-plane` | `b001cea174e3a4224bea68786adbb10cd82ce84f` | Related dry-run state-machine candidate advanced | `control_plane/runtime_contract_probe.py`; `tests/test_runtime_contract_probe.py` |

## Main-Thread Verification

- `dev-frame-opencode`: `python -m pytest ai-workflow-hub\tests\test_paper_business_capability_validation.py -q` -> `7 passed in 0.60s`.
- `dev-frame-opencode`: `python -m pytest ai-workflow-hub\tests\test_paper_cli.py ai-workflow-hub\tests\test_paper_cli_a18.py ai-workflow-hub\tests\test_paper_cli_a18b.py -q` -> `97 passed in 3.59s`.
- `dev-frame-opencode`: `git diff --check HEAD~1 HEAD` -> passed.
- `dev-frame-opencode`: `python -m ai_workflow_hub.cli paper business-validate --output <temp-json>` -> generated JSON with `profile=paper_business_validation_report`, `validation_mode=synthetic_offline`, `candidate_status=BUSINESS_CAPABILITY_VALIDATION_CANDIDATE`, `runtime_authorization_required_for_real_content=true`, and 14 command-chain entries.
- `test-frame`: `python -m pytest tests\test_paper_negative_fixtures.py tests\contracts\test_contracts.py tests\schema\test_canonical.py -q` -> `19 passed in 0.31s`.
- `test-frame`: `git diff --check` -> passed.
- `agent-acceptance`: `python -m pytest tests\test_workflow_closure_validation.py -q` -> `27 passed in 0.26s`.
- `agent-acceptance`: `python -m py_compile scripts\validate_workflow_closure.py tests\test_workflow_closure_validation.py` -> passed.
- `agent-acceptance`: NEG-044/NEG-045/NEG-046 JSON parse probe -> passed.
- `agent-acceptance`: `powershell -ExecutionPolicy Bypass -File scripts\sadp-audit.ps1` -> `[SADP-AUDIT] No staged changes. PASS.`
- `agent-acceptance`: `git diff --check HEAD~1 HEAD` -> passed.
- `devframe-control-plane`: `python -m pytest tests\test_runtime_contract_probe.py -q` -> `14 passed in 0.07s`.
- `devframe-control-plane`: `git diff --check` -> passed.

## Decision

`PAPER_BUSINESS_VALIDATION_REPORT_ARTIFACT_CANDIDATE` is ready for human
review. This means the paper feature has a reviewable and machine-checkable
offline evidence package for its current business surface. It does not
authorize final acceptance, real paper content, live WriteLab execution, or
runtime worker dispatch.

## Reviewer Index

Changed files and artifacts to inspect:

- `dev-frame-opencode/ai-workflow-hub/tests/test_paper_business_capability_validation.py`
- `dev-frame-opencode/ai-workflow-hub/docs/paper/PAPER_BUSINESS_CAPABILITY_VALIDATION.md`
- `dev-frame-opencode/schemas/paper_business_validation_report.schema.json`
- `dev-frame-opencode/ai-workflow-hub/src/ai_workflow_hub/cli.py`
- `test-frame/docs/agent-runtime/negative-test-fixtures/NEG-039-paper-missing-command-chain-evidence.json`
- `test-frame/docs/agent-runtime/negative-test-fixtures/NEG-040-paper-summary-only-production-path-skipped.json`
- `test-frame/docs/agent-runtime/negative-test-fixtures/NEG-041-paper-audit-zip-as-final-acceptance.json`
- `test-frame/docs/agent-runtime/negative-test-fixtures/NEG-042-paper-offline-handoff-integrity-missing.json`
- `test-frame/docs/agent-runtime/negative-test-fixtures/NEG-043-paper-business-manifest-incomplete.json`
- `test-frame/docs/agent-runtime/negative-test-fixtures/NEG-044-paper-business-report-invalid-validation-mode.json`
- `test-frame/docs/agent-runtime/negative-test-fixtures/NEG-045-paper-business-report-final-acceptance-true.json`
- `test-frame/docs/agent-runtime/negative-test-fixtures/NEG-046-paper-business-report-missing-fresh-authorization-gate.json`
- `test-frame/docs/agent-runtime/negative-test-fixtures/NEG-047-paper-business-report-incomplete-command-chain.json`
- `test-frame/docs/agent-runtime/negative-test-fixtures/NEG-048-paper-business-report-privacy-boundary-leak.json`
- `agent-acceptance/scripts/validate_workflow_closure.py`
- `agent-acceptance/tests/test_workflow_closure_validation.py`
- `agent-acceptance/_evidence/paper-business-validation-governance-a1/`
- `devframe-control-plane/control_plane/runtime_contract_probe.py`
- `devframe-control-plane/tests/test_runtime_contract_probe.py`

Critical review focus:

- Confirm the validation matrix is business-relevant and not only test-count
  driven.
- Confirm `reviewer_pack`, audit ZIP, reports, tests, and business-validation
  artifacts cannot claim final acceptance.
- Confirm real paper content and live WriteLab paths remain blocked without
  fresh RuntimeAuthorization.
- Confirm generated evidence paths and hashes are inspectable by reviewers.
- Confirm the JSON report schema fields match the `test-frame` NEG-044 through
  NEG-048 report-shape canaries.
- Confirm SD-07 real-content/live WriteLab RuntimeAuthorization boundary blocks
  unauthorized real-content/live evidence before any real-content pilot.

Known gaps:

- No real paper text was processed.
- No live WriteLab flow was executed.
- No OpenCode runtime, control-plane worker, or test-frame external runtime was
  run.
- Final product acceptance still requires human review, fresh
  RuntimeAuthorization, a dedicated pilot TaskSpec, and an independently
  reviewed real-content pilot.
- SD-07 is implemented as a governance gate in `agent-acceptance` commit
  `38d7b2e`; it is not authorization to run real paper content or live
  WriteLab.
