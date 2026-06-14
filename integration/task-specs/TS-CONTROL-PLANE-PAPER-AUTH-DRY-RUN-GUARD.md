# TS-CONTROL-PLANE-PAPER-AUTH-DRY-RUN-GUARD

Owner thread: `019ec6c4-a05c-7053-966e-a260f5b51aa1`
Module: `devframe-control-plane`
Expected base: `b001cea174e3a4224bea68786adbb10cd82ce84f`
Priority: P1

## Goal

Extend the pure in-memory control-plane dry-run probe so future paper
real-content/live WriteLab dispatch cannot be represented as dispatchable
without a fresh scoped RuntimeAuthorization marker.

## Scope

- Reuse `control_plane/runtime_contract_probe.py` and
  `tests/test_runtime_contract_probe.py` unless a smaller adjacent helper is
  clearly better.
- Add dry-run-only validation for paper real-content/live task metadata, if not
  already present.
- Confirm dispatch mechanical success still cannot claim `task_success` or
  final verdict.
- Keep the implementation in-memory only.

## Forbidden

- No control-plane worker, doctor, run, queue daemon, external runtime, browser,
  cloud, paper workflow, real paper text, WriteLab, OpenCode dispatch, push,
  reset, clean, stash, package install, or MCP config mutation.

## Expected Verification

- `python -m pytest tests\test_runtime_contract_probe.py -q`
- `git diff --check`

## Output

Return `PAPER_AUTH_DRY_RUN_GUARD_READY`, `NO_CHANGE_NEEDED`, or `BLOCKED`, with
branch, commit hash if changed, tests run, Reviewer Index, known gaps, and
review focus.
