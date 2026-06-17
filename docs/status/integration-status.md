# Integration Status

Date: 2026-06-15
Status: Phase 0.5 complete; SD-07 readiness slices pinned across paper report UX, negative fixtures, RuntimeAuthorization governance, and dry-run control-plane guard; real paper content remains gated
Route: ROUTE_A_STRICT_CLEAN_BASELINE

## Current State

`devframe-system` is a Git superproject that pins four source repositories as
submodules. Source code remains owned by each submodule repository.

The `/rdinit` governance bootstrap has been applied to this superproject. The
generated SADP rules, schemas, and agent-runtime documents are present under
`rules/`, `schemas/`, `docs/agent-runtime/`, and `templates/runtime-bootstrap/`.

## Verified Baseline

| Module | Role | Pinned commit | Status |
|---|---|---:|---|
| `agent-acceptance` | Governance and acceptance framework | `3cf2c9be9f33ddabdc029a652dca512d8193a5e5` | SD-04 through SD-07 boundaries retained, and minimal rule-center TaskSpec `agent-acceptance-minimal-rule-center-a1` added and write_set parsing fixed for the next autonomous iteration |
| `devframe-control-plane` | Control-plane runtime candidate | `79399541b8426cff0f362b665bad09e3c23e974b` | Lease/source-lock contract, in-memory dry-run runtime state machine, and paper real-content/live WriteLab RuntimeAuthorization dry-run guard branch pinned |
| `dev-frame-opencode` | Controlled coding runtime candidate | `0c24204fd99e6cab1d853ecadb12200244119fe1` | Runtime/paper privacy gate, WriteLab handoff fixture, audit sensitive scan, live WriteLab authorization guard, CLI/status/reviewer-pack/finalizer boundaries, Security Preflight P1 gates, machine-readable paper business validation report, and visible SD-07 report gate branch pinned |
| `test-frame` | Controlled verification runtime candidate | `bdd7b67a4bb9cfee2c6601c2f755abfd68164da7` | Adapter/negative matrix retained, and time-goal-manager MiniApp smoke dry-run contract is pinned with missing-environment BLOCKED/FAILED semantics recorded in parent reports |

## Current Gaps

| Gap | Severity | Status | Notes |
|---|---|---|---|
| `agent-acceptance` active binding path drift | P1 | Contracted and pinned | Commit `88dd581` documents the integration path, legacy path, and HUMAN_REQUIRED preservation; current pin `3cf2c9b` preserves SD-04/SD-05/SD-06/SD-07 boundaries and adds the minimal rule-center TaskSpec and write_set parsing fix. Active rebinding is still human-gated. |
| A120 evidence location split | P1 | Open | A120 generated evidence exists in `D:\dev-frame-opencode\ai-workflow-hub`, not the submodule path. |
| Independent A120 ZIP verifier | P1 | Implemented | `scripts/review_a120_evidence_zip.py` produced `PASS_WITH_BOUNDARY`; reports are stored under `integration/reports/a120`. This is evidence review, not final acceptance. |
| `control-plane` lease/heartbeat/cancellation runtime | P0/P1 | Contracted, dry-run state-machine pinned, and paper authorization guard pinned | Commit `b001cea` adds a pure in-memory dry-run runtime state machine for dispatch, lease acquire, heartbeat, source lock, completion, cancellation, failure, retry, and dispatch-success promotion boundaries. Commit `7939954` blocks paper real-content/live WriteLab dry-run dispatch without fresh scoped RuntimeAuthorization. Runtime enforcement remains future work. |
| `test-frame` adapter/failure semantics | P1 | Contracted and dry-run pinned | Commit `bdd7b67` carries the time-goal-manager MiniApp smoke profile and dry-run contract. Parent reports record both dry-run readiness and missing WeChat DevTools BLOCKED/FAILED semantics. It remains a verification runtime candidate, not a final verdict source. |
| Paper feature usability and privacy boundary | P1 | Machine-readable business validation report artifact candidate pinned with visible SD-07 gate and dry-run authorization guard | Commit `0c24204` exposes `sd07_governance_gate` in `paper business-validate` JSON, schema, tests, and docs. Commit `7940891` adds a negative canary for `synthetic_offline` report output authorizing live execution. Commit `7939954` blocks dry-run paper real-content/live dispatch without fresh scoped RuntimeAuthorization. Commit `38d7b2e` keeps business-validation artifacts non-final and adds SD-07 so real-content/live WriteLab evidence fails closed without fresh scoped RuntimeAuthorization and human gate evidence. |
| Security Preflight | P1 | Review pass with boundary | `integration/reports/security-preflight-2026-06-15.md` records canonical clean baseline, SkillSpector `TOOL_NOT_AVAILABLE`, focused security findings, P1 fix candidate commits `4558ab8` and `40ee21b`, main-thread regression verification, test-frame negative-matrix review pass, and agent-acceptance independent review pass. |
| Final verdict authority | P0 | Expanded, not live-runtime complete | Dispatch, execution, test, review, governance, and business-validation results must remain distinct. Paper reviewer-pack/report/test/zip promotion is rejected by SD-04, dispatch/test-frame/control-plane promotion is rejected by SD-05, business-validation promotion is rejected by SD-06, and real-content/live WriteLab evidence without fresh scoped RuntimeAuthorization is rejected by SD-07. Live runtime final verdict authority is still blocked until fresh authorization, pilot TaskSpec, and independent review. |

## Allowed Next Work

- Maintain read-only baseline checks.
- Add contracts, plans, risk register, runbooks, and readonly CI.
- Implement independent evidence verifier design before live runtime use.
- Add dry-run-only adapters before any real dispatch.
- Review the machine-readable Paper Business Validation report candidate under synthetic/offline evidence.
- Review the SD-07 real-content/live WriteLab RuntimeAuthorization boundary before any real-content pilot.
- Review the newly pinned SD-07 readiness slices as a cross-module set before any real-content pilot.
- Prepare the next TaskSpec for a human-authorized real-content pilot only after fresh RuntimeAuthorization exists.

## Not Yet Allowed

- OpenCode runtime execution.
- Control-plane worker dispatch.
- Test-frame runtime execution against real H5, MiniApp, MeterSphere, cloud device, or Android targets.
- Treating any generated summary, dispatch result, or internal verdict as final acceptance.
- Promoting Paper Business Capability Validation candidate evidence to final acceptance.
- Running Paper Business Capability Validation with real paper content before fresh RuntimeAuthorization.
