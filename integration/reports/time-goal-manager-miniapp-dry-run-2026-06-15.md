# Time Goal Manager MiniApp Dry-Run Contract Report

Date: 2026-06-15
Status: `TESTFRAME_TGM_MINIAPP_DRY_RUN_READY`
Boundary: dry-run contract only; not real MiniApp E2E readiness

## Summary

`test-frame` now has a first-stage orchestration contract for the
`time-goal-manager` MiniApp E2E surface. The integration uses the existing
`time-goal-manager` Jest E2E runner through a thin bridge and exposes a
`miniapp-smoke` profile through the TestFrame CLI.

This is accepted only as dry-run contract readiness. It proves project/profile
loading, stage planning, bridge argument compatibility, structured
`MINIAPP_RESULTS` output, and missing-environment non-fake-green behavior. It
does not prove real WeChat DevTools, miniprogram-automator, Jest E2E, cloud
backend, or release readiness.

## Pinned Inputs

| Module | Commit | Result | Notes |
|---|---:|---|---|
| `test-frame` | `bdd7b67a4bb9cfee2c6601c2f755abfd68164da7` | `TESTFRAME_TGM_MINIAPP_DRY_RUN_READY` | Adds `time-goal-manager` project config, `miniapp-smoke` profile, and local contract tests. |
| `time-goal-manager` | `1f8585e9228f62d1ad91a7d7ccae0391ba67ed00` | Bridge commit recorded | Adds `scripts/testframe-miniapp-bridge.js`; this repo is external to the parent submodule lock and had pre-existing dirty/staged work. |

## Main-Thread Verification

- `python -m cli.main --help` in `test-frame` -> exit 0.
- `python -m cli.main check --project=time-goal-manager` -> `[OK] Config check passed`.
- `python -m cli.main run --project=time-goal-manager --profile=miniapp-smoke --dry-run` -> prints `Stage 0: [miniapp-smoke] -> tools: ['miniprogram-automator']`.
- `python -m pytest tests\test_time_goal_manager_miniapp_config.py -q` -> `5 passed`.
- `python -m pytest tests\test_miniapp_integration.py tests\test_miniapp_probe.py -q` -> `40 passed`.
- `node scripts\testframe-miniapp-bridge.js --files connection,home --dry-run --port 19501` in `D:\time-goal-manager` -> emits `MINIAPP_RESULTS` for `connection` and `home` with `dry_run=true`.
- `git diff --check` in `test-frame` -> passed.
- `git diff --check -- scripts/testframe-miniapp-bridge.js` in `time-goal-manager` -> passed.

## Generated Artifacts

Generated but not committed:

- `D:\time-goal-manager\artifacts\testframe\miniapp-smoke-results.json`

## Decision

`TESTFRAME_TGM_MINIAPP_DRY_RUN_READY` is accepted as a dry-run contract. The
existing `time-goal-manager` Jest E2E was not rewritten, no real MiniApp E2E was
run, no environment secrets were written, no artifacts were committed, and
TestFrame remains an orchestration/evidence layer only.

The next recommended slice is real-environment failure semantics, not broader
profile expansion.

## Reviewer Index

Changed files and artifacts to inspect:

- `test-frame/config/projects/time-goal-manager.yaml`
- `test-frame/config/profiles/miniapp-smoke.yaml`
- `test-frame/tests/test_time_goal_manager_miniapp_config.py`
- `D:\time-goal-manager\scripts\testframe-miniapp-bridge.js`
- `integration/lock/submodules.lock.yml`
- `integration/reports/time-goal-manager-miniapp-dry-run-2026-06-15.md`

Critical review focus:

- Confirm `miniapp-smoke` remains dry-run contract readiness only.
- Confirm the bridge does not rewrite or bypass existing Jest E2E logic.
- Confirm missing DevTools environment returns non-zero and does not create fake green.
- Confirm generated artifacts remain untracked and outside parent commits.
- Confirm `time-goal-manager` dirty worktree is not treated as clean or release-ready.

Known gaps:

- Real WeChat DevTools was not launched.
- Real miniprogram-automator was not connected.
- Real Jest E2E was not run through TestFrame.
- `miniapp-core` and `miniapp-release` profiles are intentionally deferred.
- `D:\time-goal-manager` remains broadly dirty from pre-existing unrelated work.

Suggested next TaskSpec:

`TS-TEST-FRAME-TGM-MINIAPP-BLOCKED-FAILED-SEMANTICS`

- Verify non-dry-run behavior without `WECHAT_DEVTOOL_PATH` / `WECHAT_DEVTOOLS_CLI`.
- Verify missing environment exits non-zero and maps to BLOCKED/FAILED honestly.
- Verify `MINIAPP_RESULTS` schema and artifact shape remain stable.
- Verify bridge exit code and TestFrame verdict mapping are consistent.
- Do not run real MiniApp E2E unless separately authorized with a configured DevTools environment.
