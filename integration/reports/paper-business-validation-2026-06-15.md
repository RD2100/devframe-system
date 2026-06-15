# Paper Business Capability Validation Report

Date: 2026-06-15
Status: `PAPER_BUSINESS_VALIDATION_REPORT_ARTIFACT_CANDIDATE_WITH_SD07_READINESS`
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
| `dev-frame-opencode` | `0c24204fd99e6cab1d853ecadb12200244119fe1` | Machine-readable business report artifact implemented with visible SD-07 gate | `paper business-validate`; `schemas/paper_business_validation_report.schema.json`; `ai-workflow-hub/tests/test_paper_business_capability_validation.py`; `ai-workflow-hub/docs/paper/PAPER_BUSINESS_CAPABILITY_VALIDATION.md` |
| `test-frame` | `7940891cf5643f59fb50709c6ac77137d861b4c1` | Negative matrix extended for report shape and SD-07 synthetic-live overclaim | `docs/agent-runtime/negative-test-fixtures/NEG-039` through `NEG-049`; `tests/test_paper_negative_fixtures.py` |
| `agent-acceptance` | `38d7b2e0aad226cce5732cb4d56e45ae2d065ec7` | Governance boundary extended through SD-07 | `scripts/validate_workflow_closure.py`; `tests/test_workflow_closure_validation.py`; `_evidence/paper-business-validation-governance-a1/`; `_evidence/paper-real-content-runtime-authorization-boundary-a1/` |
| `devframe-control-plane` | `79399541b8426cff0f362b665bad09e3c23e974b` | Related dry-run state-machine advanced with paper RuntimeAuthorization guard | `control_plane/runtime_contract_probe.py`; `tests/test_runtime_contract_probe.py` |

## Main-Thread Verification

- `dev-frame-opencode`: `python -m pytest ai-workflow-hub\tests\test_paper_business_capability_validation.py -q` -> `7 passed in 0.69s`.
- `dev-frame-opencode`: `python -m pytest ai-workflow-hub\tests\test_paper_business_capability_validation.py ai-workflow-hub\tests\test_paper_cli.py ai-workflow-hub\tests\test_paper_cli_a18.py ai-workflow-hub\tests\test_paper_cli_a18b.py -q` -> `104 passed in 3.01s`.
- `dev-frame-opencode`: `git diff --check HEAD~1 HEAD` -> passed.
- `dev-frame-opencode`: `python -m ai_workflow_hub.cli paper business-validate` JSON probe -> generated `profile=paper_business_validation_report`, `validation_mode=synthetic_offline`, `gate=SD-07`, `candidate=True`, `real=blocked_until_fresh_runtime_authorization`, and `live=blocked_until_dedicated_pilot_taskspec`.
- `test-frame`: `python -m pytest tests\test_paper_negative_fixtures.py tests\contracts\test_contracts.py tests\schema\test_canonical.py -q` -> `19 passed in 0.21s`.
- `test-frame`: `git diff --check HEAD~1 HEAD` -> passed.
- `agent-acceptance`: `python -m pytest tests\test_workflow_closure_validation.py -q` -> `27 passed in 0.26s`.
- `agent-acceptance`: `python -m py_compile scripts\validate_workflow_closure.py tests\test_workflow_closure_validation.py` -> passed.
- `agent-acceptance`: NEG-044/NEG-045/NEG-046 JSON parse probe -> passed.
- `agent-acceptance`: `powershell -ExecutionPolicy Bypass -File scripts\sadp-audit.ps1` -> `[SADP-AUDIT] No staged changes. PASS.`
- `agent-acceptance`: `git diff --check HEAD~1 HEAD` -> passed.
- `devframe-control-plane`: `python -m pytest tests\test_runtime_contract_probe.py -q` -> `21 passed in 0.06s`.
- `devframe-control-plane`: unauthorized paper live dispatch probe -> `allowed=False`, `code=RUNTIME_AUTHORIZATION_REQUIRED`, `assignments=0`, `failures=1`.
- `devframe-control-plane`: `git diff --check HEAD~1 HEAD` -> passed.

## Decision

`PAPER_BUSINESS_VALIDATION_REPORT_ARTIFACT_CANDIDATE_WITH_SD07_READINESS` is ready for human
review. This means the paper feature has a reviewable and machine-checkable
offline evidence package for its current business surface, plus cross-module
SD-07 visibility, negative canary, and dry-run guard evidence. It does not
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
- `test-frame/docs/agent-runtime/negative-test-fixtures/NEG-049-paper-business-report-synthetic-authorizes-live.json`
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
  NEG-049 report-shape and SD-07 canaries.
- Confirm control-plane blocks paper real-content/live dry-run dispatch without
  fresh scoped RuntimeAuthorization and creates no active assignment.
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
