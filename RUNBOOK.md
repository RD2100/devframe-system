# Integration Runbook

Date: 2026-06-15

## Routine Read-only Health Check

Run from `D:\devframe-system`:

```powershell
git status --short --branch
git submodule status --recursive
git diff --check
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\check-submodules.ps1
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\readonly-inventory.ps1
python .\scripts\review_a120_evidence_zip.py
```

Expected result:

- Superproject worktree is clean or only expected local branch changes exist.
- Each submodule HEAD matches `BASELINE_LOCK.json`.
- No submodule reports unexpected dirty state.
- No runtime, test framework, package install, external service, or deployment is
  invoked by the health check.
- `readonly-inventory.ps1` also parses JSON files under `schemas\` and
  `integration\` as UTF-8 or UTF-8 with BOM.
- The A120 ZIP verifier may write reviewer-side reports under
  `integration\reports\a120`; it does not execute pack scripts, validation
  scripts, tests, or runtime.

## Phase Gates

| Phase | Entry condition | Exit evidence |
|---|---|---|
| 0.5 | Clean submodule baseline and `/rdinit` bootstrap present | Integration docs, lock file, readonly scripts, readonly CI policy |
| 1A | Phase 0.5 accepted | Independent A120 ZIP verifier spec and negative fixtures |
| 1B | ZIP verifier plan stable | opencode and test-frame adapter contracts |
| 2-pre | Adapter contracts accepted | control-plane dry-run dispatch contract |
| 3 | Dry-run stable | Canary negative matrix passes |
| 4 | Canary stable | Multi-worker lease/source-lock contract verified |
| 5 | Human authorization refreshed | Live runtime pilot evidence and independent review |

## Human Gate Triggers

Pause before:

- Rebinding live conversation or project registry paths.
- Running OpenCode, control-plane worker, test-frame runtime, or any external
  H5/MiniApp/MeterSphere/cloud/Android capability.
- Promoting an internal verdict to final acceptance.
- Updating submodule commits.
- Pushing, merging, deploying, resetting, cleaning, or stashing.

## Active TaskSpecs

See `integration\task-specs\` for active sub-agent assignments. Each completed
sub-agent task must return a Reviewer Index before its phase can move from
`Delegated` to `Complete`.

Current submodule branch outputs:

| Module | Branch | Main-thread status |
|---|---|---|
| `agent-acceptance` | `codex/paper-archive-final-verdict-boundary` | Pinned at `f3abb20`; SD-04, SD-05, and SD-06 final-verdict boundaries active |
| `devframe-control-plane` | `codex/lease-source-lock-contracts` | Pinned at `b001cea`; runtime contract probe plus dry-run state machine active, runtime enforcement remains future work |
| `test-frame` | `codex/adapter-negative-matrix` | Pinned at `891b106`; paper reviewer-pack, business-validation, and business report negative matrix active, canary implementation remains future work |
| `dev-frame-opencode` | `codex/paper-audit-privacy-hard-gate` | Pinned at `08ac4f5`; paper runtime/privacy/write-scope/audit privacy boundaries, Security Preflight P1 reviewed gates, and machine-readable synthetic/offline business validation report active |

Current delegated next-slice assignments:

| TaskSpec | Module | Expected output |
|---|---|---|
| `TS-PAPER-BUSINESS-REPORT-ARTIFACT.md` | `dev-frame-opencode` | Completed in `08ac4f5`: machine-readable synthetic/offline paper business validation report |
| `TS-TEST-FRAME-BUSINESS-REPORT-NEGATIVES.md` | `test-frame` | Completed in `891b106`: negative fixtures/tests for business validation report shape |
| `TS-AGENT-ACCEPTANCE-SD07-AUTH-GATE.md` | `agent-acceptance` | Completed read-only: returned `SD07_TASKSPEC_REQUIRED` |
| `TS-CONTROL-PLANE-DRY-RUN-STATE-MACHINE.md` | `devframe-control-plane` | Completed in `b001cea`: pure in-memory dry-run state machine/validator candidate |

## Paper Focus

Paper functionality is tracked in `PAPER_FEATURE_STATUS.md` and
`integration\paper\README.md`. Treat real paper text as sensitive by default:
paper reports and evidence must use summaries, hashes, or redacted excerpts
unless a fresh RuntimeAuthorization explicitly allows broader handling.

Security preflight is tracked in
`integration\reports\security-preflight-2026-06-15.md`. Security Preflight P1
review has passed with boundary; real paper content and live WriteLab flows
still require fresh RuntimeAuthorization before execution.

Paper Business Validation report artifact candidate evidence is tracked in
`integration\reports\paper-business-validation-2026-06-15.md`. Treat that
candidate as review input only: it validates the synthetic/offline command,
schema, JSON artifact, and evidence shape, not final user acceptance.
