# Integration Status

Date: 2026-06-15
Status: Phase 0.5 complete; Phase 1B paper privacy gate advanced with runtime boundaries
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
| `agent-acceptance` | Governance and acceptance framework | `88dd58183e705f1df07c32b690ab56766c643642` | Contract branch pinned |
| `devframe-control-plane` | Control-plane runtime candidate | `49c6be859dd726092fc433cc18cb7ea9537498da` | Contract branch pinned |
| `dev-frame-opencode` | Controlled coding runtime candidate | `145fc0500d8fc03e5a11c5909ca615300e48cbc3` | Runtime/paper privacy gate branch pinned |
| `test-frame` | Controlled verification runtime candidate | `71caa1c242d9a85d185c4e29ee24eb078183ffd5` | Adapter contract branch pinned |

## Current Gaps

| Gap | Severity | Status | Notes |
|---|---|---|---|
| `agent-acceptance` active binding path drift | P1 | Contracted and pinned | Commit `88dd581` documents the integration path, legacy path, and HUMAN_REQUIRED preservation. Active rebinding is still human-gated. |
| A120 evidence location split | P1 | Open | A120 generated evidence exists in `D:\dev-frame-opencode\ai-workflow-hub`, not the submodule path. |
| Independent A120 ZIP verifier | P1 | Implemented | `scripts/review_a120_evidence_zip.py` produced `PASS_WITH_BOUNDARY`; reports are stored under `integration/reports/a120`. This is evidence review, not final acceptance. |
| `control-plane` lease/heartbeat/cancellation runtime | P0/P1 | Contracted and pinned | Commit `49c6be8` adds DispatchAssignment, WorkerLease, runtime SourceLock, AuditEvent, FailureRecord contracts. Runtime enforcement remains future work. |
| `test-frame` adapter/failure semantics | P1 | Contracted and pinned | Commit `71caa1c` maps RunSpec/EvidenceManifest/ExecutionReport and adds canary guidance. It remains a verification runtime candidate, not a final verdict source. |
| Paper feature usability and privacy boundary | P1 | Runtime/API privacy gate pinned; broader evidence pack work pending | Commit `145fc05` fail-closes raw `paragraph_text`/`writelab_token` to `human_required` unless explicit `RuntimeAuthorization.data_policy` allows the supplied fields. It also redacts runtime API return state and human-gate issue text. Narrow verification passed 80 paper runtime tests, 23 paper CLI/spec tests, schema parse, and diff check. Live WriteLab use, old evidence audit scans, and reviewer-pack shape still need follow-up probes. |
| Final verdict authority | P0 | Open | Dispatch, execution, test, review, and governance results must remain distinct. |

## Allowed Next Work

- Maintain read-only baseline checks.
- Add contracts, plans, risk register, runbooks, and readonly CI.
- Implement independent evidence verifier design before live runtime use.
- Add dry-run-only adapters before any real dispatch.

## Not Yet Allowed

- OpenCode runtime execution.
- Control-plane worker dispatch.
- Test-frame runtime execution against real H5, MiniApp, MeterSphere, cloud device, or Android targets.
- Treating any generated summary, dispatch result, or internal verdict as final acceptance.
