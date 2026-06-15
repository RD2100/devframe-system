# TS-CONTROL-PLANE-RUNTIME-AUTH-SCHEMA-ALIGNMENT

Owner thread: `019ec6c4-a05c-7053-966e-a260f5b51aa1`
Module: `devframe-control-plane`
Expected base: `79399541b8426cff0f362b665bad09e3c23e974b`
Priority: P1

## Goal

Review the pure in-memory paper RuntimeAuthorization dry-run guard against the
SD-07 governance boundary and the paper business report fields. Add only narrow
tests or helper adjustments if the marker shape is misaligned.

## Scope

- Inspect `control_plane/runtime_contract_probe.py` and
  `tests/test_runtime_contract_probe.py`.
- Compare required scopes with SD-07 and report fields:
  `paper_real_content`, `writelab_live_dispatch`,
  `blocked_until_fresh_runtime_authorization`, and
  `blocked_until_dedicated_pilot_taskspec`.
- Confirm blocked unauthorized paper real-content/live dispatch creates no
  active `DispatchAssignment`.
- Confirm dispatch mechanical success still cannot claim `task_success` or
  `final_verdict`.

## Forbidden

- No control-plane worker, doctor, run, queue daemon, external runtime,
  browser/CDP, cloud, paper workflow, real paper text, WriteLab, OpenCode
  dispatch, package install, push, reset, clean, stash, or MCP config mutation.

## Expected Verification

- `python -m pytest tests\test_runtime_contract_probe.py -q`
- `git diff --check`

## Output

Return `RUNTIME_AUTH_SCHEMA_ALIGNMENT_PASS`, `RUNTIME_AUTH_SCHEMA_GAP_FIXED`,
or `BLOCKED`, with branch, commit hash if changed, tests run, Reviewer Index,
known gaps, and review focus.
