# devframe-system Parent Canary Fixtures A1

Date: 2026-06-15
Scope: synthetic parent canary fixtures
Runtime: not executed
Task: `DFS-PARENT-CANARY-FIXTURES-A1`
Verdict: `SYNTHETIC_FIXTURES_CREATED`

## 1. Created Path

```text
integration/fixtures/parent-canary/
```

## 2. Created Fixtures

| Fixture | Negative case |
|---|---|
| `NEG-PARENT-001-offline-candidate-final-ready.json` | offline candidate overclaim |
| `NEG-PARENT-002-dry-run-live-e2e-pass.json` | dry-run/live confusion |
| `NEG-PARENT-003-test-pass-as-final-acceptance.json` | test pass promoted to final |
| `NEG-PARENT-004-dispatch-as-task-success.json` | dispatch promoted to task success |
| `NEG-PARENT-005-a120-zip-global-acceptance.json` | A120 ZIP review overreach |
| `NEG-PARENT-006-drift-marked-pin-ready.json` | drifted submodule marked pin-ready |
| `NEG-PARENT-007-live-run-missing-runtime-authorization.json` | live run without authorization |
| `NEG-PARENT-008-private-content-leak.json` | private content leak |
| `NEG-PARENT-009-missing-evidence-manifest.json` | missing EvidenceManifest |
| `NEG-PARENT-010-reviewer-executor-collision.json` | reviewer/executor collision |
| `NEG-PARENT-011-gitmodules-as-pin-source.json` | `.gitmodules` used as pin source |
| `NEG-PARENT-012-runtime-authorization-reused-out-of-scope.json` | authorization reused out of scope |
| `NEG-PARENT-013-missing-env-reported-pass.json` | missing environment reported pass |
| `NEG-PARENT-014-ci-adds-runtime-command.json` | CI runtime/install expansion |
| `NEG-PARENT-015-control-plane-mvp-blocker.json` | frozen control-plane made MVP blocker |
| `NEG-PARENT-016-executor-produced-final-verdict.json` | executor-produced final verdict |

## 3. Boundary

All fixtures are synthetic and include:

```text
runtime_allowed=false
```

They do not contain:

- private paper content;
- credentials;
- live resource data;
- MiniApp real environment data;
- browser/CDP runtime output.

## 4. Verification

JSON parse check passed for all 16 fixture files.

No tests, scripts, package installs, external runtime, or submodule changes were
executed.

## 5. Next Action

Main coordinator can dispatch follow-up work:

- parent read-only fixture consistency checker;
- `agent-acceptance` gate consumption for final-ready/pin-ready/runtime
  overclaim cases;
- `test-frame` validator consumption for dry-run/live and missing-env cases.
