# devframe-system Constraint And Evidence Vocabulary v1

Date: 2026-06-15
Scope: parent repository safety and evidence language
Runtime: not executed
Slice: S00

## 1. Purpose

This report locks the parent-level constraints and evidence vocabulary used by
the rest of the devframe-system completeness plan.

It exists so later reports do not silently promote observations into readiness
claims.

## 2. Allowed Now

| Action | Boundary |
|---|---|
| read parent files | allowed within `D:\devframe-system` |
| read submodule status | allowed through read-only git inspection |
| inspect lock files | allowed |
| inspect docs/reports/task specs | allowed |
| write parent planning reports | allowed under `integration/reports/` |
| update parent plan/index docs | allowed for `integration/PROJECT_COMPLETENESS_PLAN.md` and report indexes |
| run whitespace checks | allowed with `git diff --check` |
| propose tasks | allowed as suggestions only |

## 3. Forbidden Now

| Action | Status |
|---|---|
| update submodule pins | forbidden |
| commit, push, reset, clean, stash | forbidden |
| modify submodule business code | forbidden |
| dispatch child-module agents | outside this role |
| run real MiniApp E2E | forbidden without RuntimeAuthorization |
| run live Zotero, Obsidian, RAG, or WriteLab | forbidden without RuntimeAuthorization |
| read or store private paper content | forbidden |
| install packages | forbidden |
| mutate MCP, hooks, CI runtime, or credentials | forbidden |
| claim final acceptance | forbidden without independent review and governance approval |

## 4. Commands Not Run Policy

Every report must state when these were not run:

- real external runtime;
- package install;
- tests or build tools;
- project scripts that require script-safety review;
- submodule pin updates;
- GitLab runner jobs;
- live data adapters.

If a command cannot run due to missing authorization or environment, the status
is `blocked`, not `pass`.

## 5. Evidence Vocabulary

| Term | Meaning |
|---|---|
| `verified` | checked from local command output or exact file path |
| `observed` | visible in the current checkout but not independently accepted |
| `candidate` | useful offline/dry-run result, not final readiness |
| `partial` | some assets or evidence exist but coverage is incomplete |
| `missing` | expected asset was not found |
| `unknown` | not checked or cannot be known from current local evidence |
| `blocked` | cannot proceed without prerequisite or approval |
| `failed` | a check ran and failed |
| `human_required` | needs human or main-coordinator decision |
| `waiting_for_submodule_report` | parent awaits accepted submodule evidence |
| `final_ready` | only after independent review and governance approval |

## 6. Non-Equivalence Rules

These states are never equivalent:

| Lower-layer event | Must not be called |
|---|---|
| dispatch created | task success |
| worker report submitted | reviewer approval |
| test-frame pass | final acceptance |
| dry-run pass | live environment pass |
| offline candidate | production ready |
| ZIP review pass | global evidence acceptance |
| RuntimeAuthorization exists | quality verdict |
| observed submodule HEAD | pin-ready commit |

## 7. Final Report Directory

Parent planning reports go under:

```text
integration/reports/
```

Subdirectories are allowed for bounded evidence families, such as:

```text
integration/reports/a120/
```

Live runtime reports must not be stored until a TaskSpec and
RuntimeAuthorization explicitly allow the run.

## 8. Parent Conclusion

S00 is complete for the current planning cycle.

All later parent reports should use this vocabulary and must keep candidate,
blocked, observed, verified, and final-ready states separate.
