# TS-OPENCODE-PAPER-SD07-REPORT-UX

Owner thread: `019ec6c5-7d65-76e2-b9a6-9316c75aeae8`
Module: `dev-frame-opencode`
Expected base: `08ac4f593006d62bf5b096133dfe9212cce8e49f`
Priority: P1

## Goal

Review and, if needed, minimally improve the paper business-validation CLI,
schema, and docs so the newly pinned SD-07 governance gate is visible in the
machine-readable report and user-facing documentation.

## Scope

- Inspect `paper business-validate`, `schemas/paper_business_validation_report.schema.json`,
  and `ai-workflow-hub/docs/paper/PAPER_BUSINESS_CAPABILITY_VALIDATION.md`.
- Confirm synthetic/offline output clearly says it is candidate evidence only.
- Confirm real paper content and live WriteLab remain blocked until fresh
  RuntimeAuthorization and a dedicated pilot TaskSpec exist.
- If the current artifact lacks an explicit SD-07/gate field or wording, add the
  smallest compatible field/doc/test update.

## Forbidden

- No real paper content.
- No live WriteLab, daemon worker, OpenCode dispatch, browser/CDP, ChatGPT, cloud,
  or external runtime.
- No broad CLI refactor, package install, push, reset, clean, stash, or MCP
  config mutation.

## Expected Verification

- Focused paper business-validation tests.
- Affected paper CLI tests.
- JSON schema parse/validation.
- `git diff --check`.

## Output

Return `SD07_REPORT_UX_READY`, `NO_CHANGE_NEEDED`, or `BLOCKED`, with branch,
commit hash if changed, tests run, Reviewer Index, known gaps, and review focus.
