# Time Goal Manager MiniApp Blocked/Failed Semantics Report

Date: 2026-06-15
Status: `TGM_MINIAPP_BLOCKED_FAILED_SEMANTICS_VERIFIED`
Boundary: missing-environment semantics only; no real MiniApp E2E execution

## Summary

After accepting `TESTFRAME_TGM_MINIAPP_DRY_RUN_READY`, the next slice verified
that non-dry-run paths do not fake green when the WeChat DevTools environment is
missing. This check intentionally did not run real WeChat DevTools,
miniprogram-automator, Jest E2E, browser/CDP, cloud services, or any external
runtime.

## Inputs

| Component | Commit | Scope |
|---|---:|---|
| `test-frame` | `bdd7b67a4bb9cfee2c6601c2f755abfd68164da7` | TestFrame project/profile and wrapper verdict mapping |
| `time-goal-manager` | `1f8585e9228f62d1ad91a7d7ccae0391ba67ed00` | Thin TestFrame bridge script |

## Verification Commands

### TestFrame non-dry-run with missing DevTools

Command:

```powershell
$env:WECHAT_DEVTOOL_PATH=$null
$env:WECHAT_DEVTOOLS_CLI=$null
python -m cli.main run --project=time-goal-manager --profile=miniapp-smoke
```

Result:

```text
exit code: 1
[miniprogram-automator] [BLOCKED] WeChat DevTools CLI not found
[FAIL] Stage miniapp-smoke failed, pipeline abort
[FAIL] Test pipeline failed
```

Interpretation: TestFrame maps the missing runtime environment to a blocked
tool result and a failing pipeline exit. It does not claim pass.

### Bridge non-dry-run with missing DevTools env

Command:

```powershell
$env:WECHAT_DEVTOOL_PATH=$null
$env:WECHAT_DEVTOOLS_CLI=$null
node scripts\testframe-miniapp-bridge.js --files connection,home --port 19501
```

Result:

```text
exit code: 1
MINIAPP_RESULTS:[{"name":"fatal","status":"failed","error":"WECHAT_DEVTOOL_PATH not set"}]
TESTFRAME_ARTIFACT:D:\time-goal-manager\artifacts\testframe\miniapp-smoke-results.json
```

Generated artifact content:

```json
{
  "schema_version": "testframe.time-goal-manager-miniapp.v1",
  "results": [
    {
      "name": "fatal",
      "status": "failed",
      "error": "WECHAT_DEVTOOL_PATH not set"
    }
  ],
  "dry_run": false,
  "port": 19501
}
```

Interpretation: the bridge emits structured `MINIAPP_RESULTS`, writes a local
artifact, and exits non-zero. It does not convert missing environment into
`passed`.

## Decision

`TGM_MINIAPP_BLOCKED_FAILED_SEMANTICS_VERIFIED` is accepted for missing
environment semantics. This is still not real MiniApp E2E readiness.

## Reviewer Index

Changed files and artifacts to inspect:

- `integration/reports/time-goal-manager-miniapp-blocked-failed-semantics-2026-06-15.md`
- `D:\time-goal-manager\artifacts\testframe\miniapp-smoke-results.json` (generated, not committed)
- `test-frame/config/projects/time-goal-manager.yaml`
- `D:\time-goal-manager\scripts\testframe-miniapp-bridge.js`

Critical review focus:

- Confirm missing runtime prerequisites remain BLOCKED/FAILED, not passed.
- Confirm bridge exit code and `MINIAPP_RESULTS` agree.
- Confirm generated artifact is not committed.
- Confirm real E2E was not executed.

Known gaps:

- No real WeChat DevTools was launched.
- No real miniprogram-automator connection was attempted.
- No Jest E2E file was run through TestFrame.
- Positive real-environment execution still requires explicit authorization and
  a configured local DevTools environment.
