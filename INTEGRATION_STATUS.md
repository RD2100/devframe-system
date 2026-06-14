# Integration Status

Date: 2026-06-15
Status: Phase 0.5 complete; machine-readable Paper Business Validation report artifact candidate recorded with synthetic/offline evidence, negative fixtures, governance boundary, and dry-run control-plane progress; real paper content remains gated
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
| `agent-acceptance` | Governance and acceptance framework | `f3abb202a9d58044718d3e5b9b920bef8e4000e8` | Path/Gate0, paper archive SD-04, dispatch/test-frame/control-plane SD-05, and paper business validation SD-06 final-verdict boundary branch pinned |
| `devframe-control-plane` | Control-plane runtime candidate | `b001cea174e3a4224bea68786adbb10cd82ce84f` | Lease/source-lock contract plus in-memory dry-run runtime state machine branch pinned |
| `dev-frame-opencode` | Controlled coding runtime candidate | `08ac4f593006d62bf5b096133dfe9212cce8e49f` | Runtime/paper privacy gate, WriteLab handoff fixture, audit sensitive scan, live WriteLab authorization guard, CLI/status/reviewer-pack/finalizer boundaries, Security Preflight P1 gates, and machine-readable paper business validation report branch pinned |
| `test-frame` | Controlled verification runtime candidate | `891b10658c69356cd5a587c3f120fdfdc2b9cb8d` | Adapter contract plus paper reviewer-pack, business validation, and business report negative matrix branch pinned |

## Current Gaps

| Gap | Severity | Status | Notes |
|---|---|---|---|
| `agent-acceptance` active binding path drift | P1 | Contracted and pinned | Commit `88dd581` documents the integration path, legacy path, and HUMAN_REQUIRED preservation; current pin `f3abb20` preserves that boundary and adds SD-04/SD-05/SD-06 verdict-promotion rejection. Active rebinding is still human-gated. |
| A120 evidence location split | P1 | Open | A120 generated evidence exists in `D:\dev-frame-opencode\ai-workflow-hub`, not the submodule path. |
| Independent A120 ZIP verifier | P1 | Implemented | `scripts/review_a120_evidence_zip.py` produced `PASS_WITH_BOUNDARY`; reports are stored under `integration/reports/a120`. This is evidence review, not final acceptance. |
| `control-plane` lease/heartbeat/cancellation runtime | P0/P1 | Contracted and dry-run state-machine pinned | Commit `b001cea` adds a pure in-memory dry-run runtime state machine for dispatch, lease acquire, heartbeat, source lock, completion, cancellation, failure, retry, and dispatch-success promotion boundaries. Runtime enforcement remains future work. |
| `test-frame` adapter/failure semantics | P1 | Contracted and fixture-pinned | Commit `891b106` adds machine-readable paper business report negative fixtures `NEG-044` through `NEG-048` on top of reviewer-pack fixtures `NEG-031` through `NEG-038` and business validation fixtures `NEG-039` through `NEG-043`. It remains a verification runtime candidate, not a final verdict source. |
| Paper feature usability and privacy boundary | P1 | Machine-readable business validation report artifact candidate pinned with synthetic/offline evidence | Commit `08ac4f5` adds `paper business-validate`, `schemas/paper_business_validation_report.schema.json`, tests, and docs for a synthetic/offline JSON business validation report. Commit `891b106` adds negative canaries for invalid validation mode, final-acceptance promotion, missing fresh authorization gate, incomplete command chain, and raw privacy field leakage. Commit `f3abb20` adds SD-06 so business-validation artifacts cannot be promoted to final governance verdict. |
| Security Preflight | P1 | Review pass with boundary | `integration/reports/security-preflight-2026-06-15.md` records canonical clean baseline, SkillSpector `TOOL_NOT_AVAILABLE`, focused security findings, P1 fix candidate commits `4558ab8` and `40ee21b`, main-thread regression verification, test-frame negative-matrix review pass, and agent-acceptance independent review pass. |
| Final verdict authority | P0 | Expanded, not live-runtime complete | Dispatch, execution, test, review, governance, and business-validation results must remain distinct. Paper reviewer-pack/report/test/zip promotion is rejected by SD-04, dispatch/test-frame/control-plane promotion is rejected by SD-05, and business-validation promotion is rejected by SD-06. `agent-acceptance` returned `SD07_TASKSPEC_REQUIRED` for real-content/live WriteLab RuntimeAuthorization boundary work. Live runtime final verdict authority is still blocked until fresh authorization and SD-07 implementation. |

## Allowed Next Work

- Maintain read-only baseline checks.
- Add contracts, plans, risk register, runbooks, and readonly CI.
- Implement independent evidence verifier design before live runtime use.
- Add dry-run-only adapters before any real dispatch.
- Review the machine-readable Paper Business Validation report candidate under synthetic/offline evidence.
- Implement SD-07 real-content/live WriteLab RuntimeAuthorization boundary before any real-content pilot.
- Prepare the next TaskSpec for a human-authorized real-content pilot only after fresh RuntimeAuthorization exists.

## Not Yet Allowed

- OpenCode runtime execution.
- Control-plane worker dispatch.
- Test-frame runtime execution against real H5, MiniApp, MeterSphere, cloud device, or Android targets.
- Treating any generated summary, dispatch result, or internal verdict as final acceptance.
- Promoting Paper Business Capability Validation candidate evidence to final acceptance.
- Running Paper Business Capability Validation with real paper content before fresh RuntimeAuthorization.
