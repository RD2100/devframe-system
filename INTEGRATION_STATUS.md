# Integration Status

Date: 2026-06-15
Status: Phase 0.5 complete; Security Preflight P1 fix candidate ready; paper privacy, reviewer-pack, dispatch verdict, test-frame, and control-plane guardrails advanced
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
| `agent-acceptance` | Governance and acceptance framework | `b505bf716c55c804302db35f33375afc9524c826` | Path/Gate0, paper archive SD-04, and dispatch/test-frame/control-plane SD-05 final-verdict boundary branch pinned |
| `devframe-control-plane` | Control-plane runtime candidate | `c3edf8528cb853c023929c2c26fef208177e2198` | Lease/source-lock contract plus in-memory runtime contract probe branch pinned |
| `dev-frame-opencode` | Controlled coding runtime candidate | `4558ab819ceacd8998c5b295f51f790c21e55857` | Runtime/paper privacy gate, WriteLab handoff fixture, audit sensitive scan, live WriteLab authorization guard, CLI status boundary, redacted reviewer pack boundary, finalizer acceptance boundary, focused mojibake cleanup, post-run write-set hard gate, paper audit privacy hard gate, and Security Preflight P1 gate branch pinned |
| `test-frame` | Controlled verification runtime candidate | `be27de01950a05d743764fd394a3ab9c9336b818` | Adapter contract plus paper reviewer-pack negative matrix branch pinned |

## Current Gaps

| Gap | Severity | Status | Notes |
|---|---|---|---|
| `agent-acceptance` active binding path drift | P1 | Contracted and pinned | Commit `88dd581` documents the integration path, legacy path, and HUMAN_REQUIRED preservation; current pin `b505bf7` preserves that boundary and adds SD-04/SD-05 verdict-promotion rejection. Active rebinding is still human-gated. |
| A120 evidence location split | P1 | Open | A120 generated evidence exists in `D:\dev-frame-opencode\ai-workflow-hub`, not the submodule path. |
| Independent A120 ZIP verifier | P1 | Implemented | `scripts/review_a120_evidence_zip.py` produced `PASS_WITH_BOUNDARY`; reports are stored under `integration/reports/a120`. This is evidence review, not final acceptance. |
| `control-plane` lease/heartbeat/cancellation runtime | P0/P1 | Contracted and probe-pinned | Commit `c3edf85` adds a pure in-memory runtime contract probe for duplicate dispatch, stale lease completion, overlap SourceLock, cancellation after completion, retry non-retryable failure, and dispatch-success promotion. Runtime enforcement remains future work. |
| `test-frame` adapter/failure semantics | P1 | Contracted and fixture-pinned | Commit `be27de0` adds paper/WriteLab reviewer-pack negative fixtures `NEG-031` through `NEG-038`. It remains a verification runtime candidate, not a final verdict source. |
| Paper feature usability and privacy boundary | P1 | Runtime/API privacy gate, WriteLab handoff fixture coverage, audit bundle sensitive scan, live WriteLab authorization guard, CLI status boundary, redacted reviewer pack boundary, finalizer acceptance boundary, focused mojibake cleanup, archive-side SD-04/SD-05 boundaries, post-run write-set hard gate, paper audit privacy hard gate, and Security Preflight P1 fix candidate pinned | Commit `8119c85` expands audit/report hard gates for raw paragraph payloads, WriteLab `matched_text`, `text_span`, and payload markers. Commit `4558ab8` adds P1 gates for TaskSpec verification command allowlisting, structured review recovery verdicts, and daemon-side write authorization/risk gating. Commit `b505bf7` adds SD-05 so dispatch/test-frame/control-plane evidence and expired authorization cannot claim final governance verdict. Commit `be27de0` adds paper reviewer-pack negative fixtures. |
| Security Preflight | P1 | Fix candidate ready; independent review pending | `integration/reports/security-preflight-2026-06-15.md` records canonical clean baseline, SkillSpector `TOOL_NOT_AVAILABLE`, focused security findings, P1 fix candidate commit `4558ab8`, and main-thread regression verification. |
| Final verdict authority | P0 | Expanded, not live-runtime complete | Dispatch, execution, test, review, and governance results must remain distinct. Paper reviewer-pack/report/test/zip promotion is rejected by SD-04, and dispatch/test-frame/control-plane promotion is rejected by SD-05. Live runtime final verdict authority is still blocked until security preflight and fresh authorization. |

## Allowed Next Work

- Maintain read-only baseline checks.
- Add contracts, plans, risk register, runbooks, and readonly CI.
- Implement independent evidence verifier design before live runtime use.
- Add dry-run-only adapters before any real dispatch.
- Complete independent Security Preflight review before paper business acceptance.

## Not Yet Allowed

- OpenCode runtime execution.
- Control-plane worker dispatch.
- Test-frame runtime execution against real H5, MiniApp, MeterSphere, cloud device, or Android targets.
- Treating any generated summary, dispatch result, or internal verdict as final acceptance.
- Paper Business Capability Validation with real paper content before fresh RuntimeAuthorization and independent Security Preflight review.
