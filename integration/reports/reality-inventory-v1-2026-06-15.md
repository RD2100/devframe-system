# devframe-system Reality Inventory v1

Date: 2026-06-15
Scope: parent repository and checked-out submodule paths
Runtime: not executed
Command class: read-only inspection

## 1. Purpose

This report records the current verified and observed state of
`D:\devframe-system` so later parent work can separate facts from assumptions.

It does not approve submodule pins, does not execute tests, does not run real
external runtime, and does not claim final readiness.

## 2. Evidence Vocabulary

| Term | Meaning |
|---|---|
| `verified` | checked from command output or exact file path in this parent repo |
| `observed` | visible in the current worktree but not independently accepted |
| `drift` | observed worktree commit differs from parent lock |
| `clean` | module-local `git status --short --branch` shows no file changes |
| `dirty` | module-local or parent status shows modified or untracked files |
| `human_required` | needs explicit human/main-coordinator decision |
| `waiting_for_submodule_report` | parent has not yet received accepted module-local evidence |

## 3. Commands Used

Read-only commands used:

```text
git status --short --branch
git rev-parse --show-toplevel
git rev-parse --abbrev-ref HEAD
git rev-parse HEAD
git remote -v
git branch -vv
git submodule status --recursive
git rev-parse --abbrev-ref --symbolic-full-name @{u}
Get-ChildItem
Get-Content
Test-Path
```

Commands not used:

- tests;
- project scripts;
- package install;
- external runtime;
- GitLab runner execution;
- submodule pin mutation.

## 4. Parent Repository

| Field | Value | Status |
|---|---|---|
| Repo | `devframe-system` | `verified` |
| Path | `D:\devframe-system` | `verified` |
| Exists | yes | `verified` |
| Git root | `D:/devframe-system` | `verified` |
| Branch | `codex/rdinit-phase-0-5` | `verified` |
| HEAD | `0ab49dc77c458d75d4996d8a585361c984c74643` | `verified` |
| Upstream | none configured for active branch | `verified` |
| Remote | `origin git@github.com:RD2100/devframe-system.git` | `verified` |
| Dirty state | dirty | `verified` |
| Submodules | four configured submodules | `verified` |

Parent dirty entries observed:

```text
 M agent-acceptance
 M dev-frame-opencode
 M integration/reports/README.md
 M integration/task-specs/README.md
 M test-frame
?? integration/PROJECT_COMPLETENESS_PLAN.md
?? integration/reports/devframe-master-plan-v0-2026-06-15.md
?? integration/task-specs/TS-AGENT-ACCEPTANCE-SD07-READINESS-REVIEW.md
?? integration/task-specs/TS-CONTROL-PLANE-RUNTIME-AUTH-SCHEMA-ALIGNMENT.md
?? integration/task-specs/TS-OPENCODE-SECURITY-PREFLIGHT-FOCUSED-REFRESH.md
?? integration/task-specs/TS-TEST-FRAME-SD07-CANARY-ALIGNMENT.md
```

Interpretation:

- Parent docs/task specs are actively changing.
- Three submodule pointers have observed drift.
- This is not a pin approval.

## 5. Submodule Inventory

| Module | Path | Exists | Branch | HEAD | Module dirty | Upstream | Remote | Lock commit | Lock match | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| `agent-acceptance` | `D:\devframe-system\agent-acceptance` | yes | `codex/paper-archive-final-verdict-boundary` | `1ae113875dd87b49322c12b708129b71c13d6882` | dirty: untracked evidence | none | `https://github.com/RD2100/agent-acceptance.git` | `3cf2c9be9f33ddabdc029a652dca512d8193a5e5` | no | observed minimal rule center head; needs review before pin |
| `dev-frame-opencode` | `D:\devframe-system\dev-frame-opencode` | yes | `codex/paper-audit-privacy-hard-gate` | `e3f628b3f5ff23aeb8ded675bae4b109b31576eb` | clean | none | `https://github.com/RD2100/dev-frame-opencode.git` | `0c24204fd99e6cab1d853ecadb12200244119fe1` | no | offline paper MVP candidate; not live ready |
| `devframe-control-plane` | `D:\devframe-system\devframe-control-plane` | yes | `codex/lease-source-lock-contracts` | `79399541b8426cff0f362b665bad09e3c23e974b` | clean | none | `https://github.com/RD2100/devframe-control-plane.git` | `79399541b8426cff0f362b665bad09e3c23e974b` | yes | frozen; keep interface observation only |
| `test-frame` | `D:\devframe-system\test-frame` | yes | `codex/adapter-negative-matrix` | `941819b8d251b4363777d7f2d90c10f46fa59da6` | dirty: untracked `.codex/` | none | `https://github.com/RD2100/test-frame.git` | `bdd7b67a4bb9cfee2c6601c2f755abfd68164da7` | no | observed positive pilot prereq gate; needs review before pin |

Submodule status output:

```text
+1ae113875dd87b49322c12b708129b71c13d6882 agent-acceptance (v0.3.0-rc1a-210-g1ae1138)
+e3f628b3f5ff23aeb8ded675bae4b109b31576eb dev-frame-opencode (heads/codex/paper-audit-privacy-hard-gate)
 79399541b8426cff0f362b665bad09e3c23e974b devframe-control-plane (v0.1.0-rc-44-g7939954)
+941819b8d251b4363777d7f2d90c10f46fa59da6 test-frame (heads/codex/adapter-negative-matrix)
```

`+` means the checked-out submodule commit differs from the parent index.

## 6. Lock Files

| Lock file | Exists | Source | Status |
|---|---|---|---|
| `BASELINE_LOCK.json` | yes | parent root | `verified` |
| `integration/lock/submodules.lock.yml` | yes | generated from baseline lock | `verified` |

Locked modules:

| Module | Locked branch | Locked commit | Observed branch | Observed commit | Parent conclusion |
|---|---|---|---|---|---|
| `agent-acceptance` | `codex/paper-archive-final-verdict-boundary` | `3cf2c9b` | `codex/paper-archive-final-verdict-boundary` | `1ae1138` | drift; review required |
| `dev-frame-opencode` | `codex/paper-audit-privacy-hard-gate` | `0c24204` | `codex/paper-audit-privacy-hard-gate` | `e3f628b` | drift; review required |
| `devframe-control-plane` | `codex/lease-source-lock-contracts` | `7939954` | `codex/lease-source-lock-contracts` | `7939954` | aligned |
| `test-frame` | `codex/adapter-negative-matrix` | `bdd7b67` | `codex/adapter-negative-matrix` | `941819b` | drift; review required |

## 7. `.gitmodules` Advisory Branches

`.gitmodules` exists and records four submodules.

| Module | `.gitmodules` branch | Observed branch | Match | Parent conclusion |
|---|---|---|---|---|
| `agent-acceptance` | `master` | `codex/paper-archive-final-verdict-boundary` | no | stale advisory metadata |
| `dev-frame-opencode` | `master` | `codex/paper-audit-privacy-hard-gate` | no | stale advisory metadata |
| `devframe-control-plane` | `codex/route-a-baseline-candidate` | `codex/lease-source-lock-contracts` | no | stale advisory metadata |
| `test-frame` | `codex/harden-baseline` | `codex/adapter-negative-matrix` | no | stale advisory metadata |

This is not automatically a failure because lock files are the current source
of pin truth. It is a parent cleanup/review item before future onboarding.

## 8. Alias And Non-Submodule Paths

| Path | Exists | Git identity | Status | Notes |
|---|---|---|---|---|
| `D:\devframe-system\ai-workflow-hub` | yes | resolves to parent repo | `observed` | contains `tests/`; not a locked submodule |

Parent conclusion:

- Treat `dev-frame-opencode` as the canonical locked submodule.
- Treat `ai-workflow-hub` as an alias or local helper path until separately
  documented.

## 9. Integration Paths

| Path | Exists | Status | Notes |
|---|---|---|---|
| `integration/` | yes | `verified` | parent integration workspace |
| `integration/contracts/` | yes | `verified` | contract area |
| `integration/lock/` | yes | `verified` | submodule lock area |
| `integration/reports/` | yes | `verified` | report area |
| `integration/runbooks/` | yes | `verified` | runbook area |
| `integration/task-specs/` | yes | `verified` | delegated task spec area |
| `docs/agent-runtime/` | yes | `verified` | runtime governance docs |

## 10. A120 Evidence Paths

| Path | Exists | Size | Status |
|---|---:|---:|---|
| `integration/reports/a120/a120-evidence-zip-review.md` | yes | 1873 | `verified` |
| `integration/reports/a120/a120-evidence-zip-review.json` | yes | 6775 | `verified` |

Parent conclusion:

- A120 evidence review exists.
- Its status remains bounded to that report.
- It is not evidence that all A101-A120 artifacts are accepted.

## 11. Known Reports

Reports directory currently includes:

- `phase-0.5-1b-checkpoint.md`
- `security-preflight-2026-06-15.md`
- `paper-business-validation-2026-06-15.md`
- `sd07-runtime-authorization-boundary-2026-06-15.md`
- `sd07-readiness-slices-2026-06-15.md`
- `devframe-master-plan-v0-2026-06-15.md`
- `a120/a120-evidence-zip-review.md`
- `a120/a120-evidence-zip-review.json`

## 12. Known TaskSpecs

TaskSpec directory currently includes historical and new parent-visible specs,
including:

- `TS-AGENT-ACCEPTANCE-SD07-READINESS-REVIEW.md`
- `TS-CONTROL-PLANE-RUNTIME-AUTH-SCHEMA-ALIGNMENT.md`
- `TS-OPENCODE-SECURITY-PREFLIGHT-FOCUSED-REFRESH.md`
- `TS-TEST-FRAME-SD07-CANARY-ALIGNMENT.md`

These four are untracked in the parent status at the time of this inventory.

## 13. Verified Facts

- Parent root and branch are known.
- Four locked submodule paths exist.
- Three submodule worktree commits differ from lock.
- `devframe-control-plane` is aligned with lock.
- Active branches have no upstream configured.
- `ai-workflow-hub` is not a Git submodule in this checkout.
- A120 review files exist.
- Read-only CI and GitLab policy files exist.

## 14. Gaps

- No independent parent review yet for `agent-acceptance@1ae1138`.
- No independent parent review yet for `dev-frame-opencode@e3f628b`.
- No independent parent review yet for `test-frame@941819b`.
- No GitLab runner proof artifact observed in this inventory.
- No full A101-A120 verifier inventory yet.
- `.gitmodules` advisory branches are stale relative to active branches.

## 15. Parent Conclusion

S01 is complete enough for parent planning v1.

Pin readiness is not established. The parent should next build a pin readiness
matrix that maps each observed submodule head to required review evidence,
allowed claims, forbidden claims, and final coordinator decision.
