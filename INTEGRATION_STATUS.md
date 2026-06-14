# Integration Status

Date: 2026-06-15
Status: Phase 0.5 complete; Paper Business Capability Validation candidate recorded with synthetic/offline evidence, negative fixtures, and governance boundary; real paper content remains gated
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
| `devframe-control-plane` | Control-plane runtime candidate | `c3edf8528cb853c023929c2c26fef208177e2198` | Lease/source-lock contract plus in-memory runtime contract probe branch pinned |
| `dev-frame-opencode` | Controlled coding runtime candidate | `b805658a2c9111ab839749ed81a210305127d42d` | Runtime/paper privacy gate, WriteLab handoff fixture, audit sensitive scan, live WriteLab authorization guard, CLI/status/reviewer-pack/finalizer boundaries, Security Preflight P1 gates, and paper business capability validation candidate branch pinned |
| `test-frame` | Controlled verification runtime candidate | `93b95b98e59dbf0ca0bc060c949eb7fa53f3b3ef` | Adapter contract plus paper reviewer-pack and paper business validation negative matrix branch pinned |

## Current Gaps

| Gap | Severity | Status | Notes |
|---|---|---|---|
| `agent-acceptance` active binding path drift | P1 | Contracted and pinned | Commit `88dd581` documents the integration path, legacy path, and HUMAN_REQUIRED preservation; current pin `f3abb20` preserves that boundary and adds SD-04/SD-05/SD-06 verdict-promotion rejection. Active rebinding is still human-gated. |
| A120 evidence location split | P1 | Open | A120 generated evidence exists in `D:\dev-frame-opencode\ai-workflow-hub`, not the submodule path. |
| Independent A120 ZIP verifier | P1 | Implemented | `scripts/review_a120_evidence_zip.py` produced `PASS_WITH_BOUNDARY`; reports are stored under `integration/reports/a120`. This is evidence review, not final acceptance. |
| `control-plane` lease/heartbeat/cancellation runtime | P0/P1 | Contracted and probe-pinned | Commit `c3edf85` adds a pure in-memory runtime contract probe for duplicate dispatch, stale lease completion, overlap SourceLock, cancellation after completion, retry non-retryable failure, and dispatch-success promotion. Runtime enforcement remains future work. |
| `test-frame` adapter/failure semantics | P1 | Contracted and fixture-pinned | Commit `93b95b9` adds paper business validation negative fixtures `NEG-039` through `NEG-043` on top of reviewer-pack fixtures `NEG-031` through `NEG-038`. It remains a verification runtime candidate, not a final verdict source. |
| Paper feature usability and privacy boundary | P1 | Business capability validation candidate pinned with synthetic/offline evidence | Commit `b805658` documents and tests the current paper command chain, reviewer-pack non-final boundary, status/final-acceptance separation, and redaction boundary. Commit `93b95b9` adds negative canaries for missing command-chain evidence, summary-only production path, audit ZIP promotion, offline handoff integrity, and incomplete business manifests. Commit `f3abb20` adds SD-06 so business-validation artifacts cannot be promoted to final governance verdict. |
| Security Preflight | P1 | Review pass with boundary | `integration/reports/security-preflight-2026-06-15.md` records canonical clean baseline, SkillSpector `TOOL_NOT_AVAILABLE`, focused security findings, P1 fix candidate commits `4558ab8` and `40ee21b`, main-thread regression verification, test-frame negative-matrix review pass, and agent-acceptance independent review pass. |
| Final verdict authority | P0 | Expanded, not live-runtime complete | Dispatch, execution, test, review, governance, and business-validation results must remain distinct. Paper reviewer-pack/report/test/zip promotion is rejected by SD-04, dispatch/test-frame/control-plane promotion is rejected by SD-05, and business-validation promotion is rejected by SD-06. Live runtime final verdict authority is still blocked until fresh authorization. |

## Allowed Next Work

- Maintain read-only baseline checks.
- Add contracts, plans, risk register, runbooks, and readonly CI.
- Implement independent evidence verifier design before live runtime use.
- Add dry-run-only adapters before any real dispatch.
- Review the Paper Business Capability Validation candidate under synthetic/offline evidence.
- Prepare the next TaskSpec for a human-authorized real-content pilot only after fresh RuntimeAuthorization exists.

## Not Yet Allowed

- OpenCode runtime execution.
- Control-plane worker dispatch.
- Test-frame runtime execution against real H5, MiniApp, MeterSphere, cloud device, or Android targets.
- Treating any generated summary, dispatch result, or internal verdict as final acceptance.
- Promoting Paper Business Capability Validation candidate evidence to final acceptance.
- Running Paper Business Capability Validation with real paper content before fresh RuntimeAuthorization.
