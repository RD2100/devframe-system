# TS-TEST-FRAME-PARENT-CANARY-REPORT-A1

Owner thread: `019ec6c6-5238-74b3-8870-c973bee56131`
Module: `test-frame`
Expected base: observed current checkout `941819b8d251b4363777d7f2d90c10f46fa59da6`
Priority: P1
Status: dispatched

## Goal

Consume devframe-system parent canary fixtures that target test-report
semantics. Ensure `test-frame` preserves dry-run/live separation and
blocked/failed/pass semantics.

## Scope

Input fixtures:

- `D:\devframe-system\integration\fixtures\parent-canary\NEG-PARENT-002-dry-run-live-e2e-pass.json`
- `D:\devframe-system\integration\fixtures\parent-canary\NEG-PARENT-013-missing-env-reported-pass.json`

Parent schemas to inspect:

- `D:\devframe-system\schemas\agent-runtime\test-run-spec.schema.json`
- `D:\devframe-system\schemas\agent-runtime\test-execution-report.schema.json`
- `D:\devframe-system\schemas\agent-runtime\failure-record.schema.json`

Allowed module work:

- add minimal fixture copies or references under existing `test-frame`
  negative fixture/test locations;
- add minimal validator/test coverage for selected parent canary cases;
- produce an ExecutionReport with Reviewer Index.

## Forbidden

- No real MiniApp E2E.
- No H5, MeterSphere, cloud device, Android, browser/CDP, ChatGPT, WriteLab, or
  real paper text.
- No submodule pin update.
- No parent lock file mutation.
- No package install, push, reset, clean, stash, or MCP config mutation.
- Do not claim final acceptance.

## Expected Verification

Use the narrowest existing `test-frame` negative/report validation tests that
cover dry-run/live and missing environment semantics. If adding tests, run only
the relevant test file(s).

Also run:

```powershell
git diff --check
```

If tests cannot run, return `BLOCKED` with exact reason. Do not report blocked
or failed checks as pass.

## Acceptance Criteria

- Dry-run evidence cannot be reported as real environment E2E pass.
- Missing environment cannot be reported as pass.
- `blocked` and `failed` semantics remain distinct.
- `TestExecutionReport` remains evidence only and cannot claim final
  acceptance.
- Report includes changed files, tests run, artifacts, known gaps, and review
  focus.

## Output

Return one of:

- `PARENT_CANARY_REPORT_PASS`
- `PARENT_CANARY_REPORT_GAP_FIXED`
- `BLOCKED`

Include branch, commit hash if changed, tests run, Reviewer Index, known gaps,
and exact files touched.
