# Devframe-System Bootstrap Report

## Verdict

`BOOTSTRAPPED_LOCAL_SUPERPROJECT`

The physical superproject exists at `D:\devframe-system` and pins the four
source repositories as submodules. This is not a source-code merge.

## Source Baselines

- `agent-acceptance`: `285d5c906a074ce7c689c8f656caabbdb32af8dc`
- `devframe-control-plane`: `311847818927d3c7ec8c8718949b38c74605fc83`
- `dev-frame-opencode`: `3a3aa5722bd6015bec30a8e9190140148b45167c`
- `test-frame`: `aeb4a31f770e35e7f698e5c3169406ddba231a4d`

## Notable Decisions

- `test-frame` is treated as a controlled verification runtime candidate, not
  as a plugin.
- `dev-frame-opencode` was cleaned and verified before pinning.
- `agent-acceptance` was pushed to the GitHub remote `https-origin/master`
  because the GitLab `origin/master` push path timed out.
- No external runtime, paper workflow, package install, cleanup, reset, or stash
  command was used during bootstrap.

## Evidence

- `dev-frame-opencode`: `python -m pytest tests -q` -> `2451 passed, 2 skipped, 3 warnings`.
- Route A source preflight before bootstrap: all four source repositories were
  clean and had HEAD equal to their selected upstream.
- Superproject submodule pins are recorded in `BASELINE_LOCK.json`.
