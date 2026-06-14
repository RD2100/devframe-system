# SD-07 RuntimeAuthorization Boundary Report

Date: 2026-06-15
Status: `SD07_RUNTIME_AUTHORIZATION_BOUNDARY_PINNED`
Boundary: governance closure validation only; not runtime authorization

## Summary

`agent-acceptance` now carries SD-07 workflow closure validation for real paper
content, live WriteLab, and real-content pilot evidence. The gate fails closed
when evidence claims real-content or live execution without fresh scoped
RuntimeAuthorization, non-empty `human_gate_ref`, required sensitive-field
authorization, and `redaction_required=true`.

This does not authorize real paper text, live WriteLab, OpenCode dispatch,
control-plane workers, browser/CDP, ChatGPT, cloud services, or any external
runtime.

## Submodule Output

| Module | Commit | Result | Evidence |
|---|---:|---|---|
| `agent-acceptance` | `38d7b2e0aad226cce5732cb4d56e45ae2d065ec7` | SD-07 implemented and self-verified | `scripts/validate_workflow_closure.py`; `tests/test_workflow_closure_validation.py`; `docs/agent-runtime/negative-test-fixtures/NEG-044` through `NEG-046`; `_evidence/paper-real-content-runtime-authorization-boundary-a1/` |

## Main-Thread Verification

- `python -m py_compile scripts\validate_workflow_closure.py tests\test_workflow_closure_validation.py` -> passed.
- `python -m pytest tests\test_workflow_closure_validation.py -q` -> `27 passed in 0.26s`.
- NEG-044/NEG-045/NEG-046 JSON parse probe -> all parsed with `expected_gate_decision=blocked` and `hard_stop=True`.
- `git diff --check HEAD~1 HEAD` -> passed.
- `git show --name-only --format= --no-renames HEAD | Select-String -Pattern '^_archive/'` -> no matches.
- `powershell -ExecutionPolicy Bypass -File scripts\sadp-audit.ps1` -> `[SADP-AUDIT] No staged changes. PASS.`

## Reviewer Index

Changed files and artifacts to inspect:

- `agent-acceptance/scripts/validate_workflow_closure.py`
- `agent-acceptance/tests/test_workflow_closure_validation.py`
- `agent-acceptance/docs/agent-runtime/negative-acceptance-tests.md`
- `agent-acceptance/docs/agent-runtime/negative-test-fixtures/README.md`
- `agent-acceptance/docs/agent-runtime/negative-test-fixtures/NEG-044-real-content-pilot-without-runtime-authorization.json`
- `agent-acceptance/docs/agent-runtime/negative-test-fixtures/NEG-045-live-writelab-without-human-gate.json`
- `agent-acceptance/docs/agent-runtime/negative-test-fixtures/NEG-046-synthetic-offline-authorizes-live-execution.json`
- `agent-acceptance/_evidence/paper-real-content-runtime-authorization-boundary-a1/EXECUTION_REPORT.md`
- `agent-acceptance/_evidence/paper-real-content-runtime-authorization-boundary-a1/REVIEWER_INDEX.md`
- `agent-acceptance/_evidence/paper-real-content-runtime-authorization-boundary-a1/verification.md`
- `agent-acceptance/_reports/paper-real-content-runtime-authorization-boundary-a1/execution-report.md`

Critical review focus:

- Confirm SD-07 scans JSON evidence recursively and catches real-content/live
  evidence outside happy-path filenames.
- Confirm missing, expired, malformed, or scope-incomplete RuntimeAuthorization
  fails closed.
- Confirm synthetic/offline evidence cannot authorize live execution.
- Confirm authorized real-content pilot evidence remains candidate evidence and
  cannot claim final governance acceptance.

## Known Gaps

- No real paper content was processed.
- No live WriteLab flow was executed.
- No external runtime, OpenCode dispatch, control-plane worker, browser/CDP,
  ChatGPT, cloud service, or test-frame runtime was used.
- A real-content pilot still requires fresh RuntimeAuthorization, a dedicated
  TaskSpec, and independent review.
