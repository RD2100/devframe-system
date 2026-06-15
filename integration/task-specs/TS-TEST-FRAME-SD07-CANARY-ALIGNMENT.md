# TS-TEST-FRAME-SD07-CANARY-ALIGNMENT

Owner thread: `019ec6c6-5238-74b3-8870-c973bee56131`
Module: `test-frame`
Expected base: `7940891cf5643f59fb50709c6ac77137d861b4c1`
Priority: P1

## Goal

Review the SD-07 negative matrix against the newly visible
`sd07_governance_gate` report fields and the existing `agent-acceptance` SD-07
fixtures. Add a minimal canary only if there is a clear report-shape or
authorization overclaim gap.

## Scope

- Inspect `NEG-044` through `NEG-049`.
- Compare `NEG-049` to `agent-acceptance` SD-07 synthetic/offline live
  authorization rejection.
- Compare expected report fields against `dev-frame-opencode`
  `schemas/paper_business_validation_report.schema.json` at commit `0c24204`.
- Confirm test-frame remains verification evidence only and cannot claim final
  paper acceptance.

## Forbidden

- No external verification runtime, H5, MiniApp, MeterSphere, cloud device,
  Android, browser/CDP, ChatGPT, WriteLab, or real paper text.
- No broad renumbering, package install, push, reset, clean, stash, or MCP
  config mutation.

## Expected Verification

- `python -m pytest tests\test_paper_negative_fixtures.py -q`
- If fixtures change:
  `python -m pytest tests\test_paper_negative_fixtures.py tests\contracts\test_contracts.py tests\schema\test_canonical.py -q`
- `git diff --check`

## Output

Return `SD07_CANARY_ALIGNMENT_PASS`, `SD07_CANARY_GAP_FIXED`, or `BLOCKED`,
with branch, commit hash if changed, tests run, Reviewer Index, known gaps, and
review focus.
