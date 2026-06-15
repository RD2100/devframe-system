# TS-AGENT-ACCEPTANCE-PARENT-CANARY-GATE-A1

Owner thread: `019ec6c5-0855-7b11-812a-a099010b9b18`
Module: `agent-acceptance`
Expected base: observed current checkout `1ae113875dd87b49322c12b708129b71c13d6882`
Priority: P1
Status: dispatched

## Goal

Consume selected devframe-system parent canary fixtures and ensure
`agent-acceptance` rejects final-ready, pin-ready, runtime-authorization,
reviewer-collision, and evidence-manifest overclaims.

## Scope

Input fixtures:

- `D:\devframe-system\integration\fixtures\parent-canary\NEG-PARENT-001-offline-candidate-final-ready.json`
- `D:\devframe-system\integration\fixtures\parent-canary\NEG-PARENT-003-test-pass-as-final-acceptance.json`
- `D:\devframe-system\integration\fixtures\parent-canary\NEG-PARENT-004-dispatch-as-task-success.json`
- `D:\devframe-system\integration\fixtures\parent-canary\NEG-PARENT-005-a120-zip-global-acceptance.json`
- `D:\devframe-system\integration\fixtures\parent-canary\NEG-PARENT-007-live-run-missing-runtime-authorization.json`
- `D:\devframe-system\integration\fixtures\parent-canary\NEG-PARENT-009-missing-evidence-manifest.json`
- `D:\devframe-system\integration\fixtures\parent-canary\NEG-PARENT-010-reviewer-executor-collision.json`
- `D:\devframe-system\integration\fixtures\parent-canary\NEG-PARENT-012-runtime-authorization-reused-out-of-scope.json`
- `D:\devframe-system\integration\fixtures\parent-canary\NEG-PARENT-016-executor-produced-final-verdict.json`

Parent schemas to inspect:

- `D:\devframe-system\schemas\agent-runtime\runtime-authorization.schema.json`
- `D:\devframe-system\schemas\agent-runtime\failure-record.schema.json`
- `D:\devframe-system\schemas\agent-runtime\final-verdict.schema.json`

Allowed module work:

- add minimal fixture copies or references under existing `agent-acceptance`
  negative fixture/test locations;
- add minimal validator/test coverage for selected parent canary cases;
- produce an ExecutionReport with Reviewer Index.

## Forbidden

- No real paper content.
- No live Zotero, Obsidian, RAG, WriteLab, MiniApp, browser/CDP, cloud, or
  external runtime.
- No submodule pin update.
- No parent lock file mutation.
- No package install, push, reset, clean, stash, or MCP config mutation.
- Do not claim final readiness.

## Expected Verification

Use the narrowest existing `agent-acceptance` negative/gate tests that cover the
new fixtures. If adding tests, run only the relevant test file(s).

Also run:

```powershell
git diff --check
```

If tests cannot run, return `BLOCKED` with exact reason. Do not report blocked
or failed checks as pass.

## Acceptance Criteria

- Every selected fixture returns the expected `blocked` or `failed` result.
- Reviewer/executor collision is rejected.
- Missing RuntimeAuthorization is rejected.
- Executor-produced FinalVerdict is rejected.
- A120 ZIP review cannot become global/final acceptance.
- Report includes changed files, tests run, artifacts, known gaps, and review
  focus.

## Output

Return one of:

- `PARENT_CANARY_GATE_PASS`
- `PARENT_CANARY_GATE_GAP_FIXED`
- `BLOCKED`

Include branch, commit hash if changed, tests run, Reviewer Index, known gaps,
and exact files touched.
