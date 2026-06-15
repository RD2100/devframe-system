# devframe-system Phase 0.5 State Review v1

Date: 2026-06-15
Scope: parent repository Phase 0.5 state
Runtime: not executed
Verdict: `phase-0.5-partial-current`

## 1. Purpose

This report reviews whether the parent repo has the Phase 0.5 bootstrap assets
needed for practical integration work.

It distinguishes two states:

- bootstrap assets exist;
- current worktree is not a clean accepted baseline.

## 2. Summary

Phase 0.5 is structurally present but not currently clean/final.

| Area | Status | Reason |
|---|---|---|
| physical superproject | `complete` | four submodule paths exist |
| baseline lock files | `complete` | `BASELINE_LOCK.json` and `integration/lock/submodules.lock.yml` exist |
| runtime governance docs | `complete` | `docs/agent-runtime/` is populated |
| integration contracts area | `complete` | `integration/contracts/` exists |
| reports area | `complete` | `integration/reports/` exists and now includes S00-S08 parent reports |
| runbooks area | `complete` | read-only GitLab runbook exists |
| scripts area | `partial` | scripts exist, but were not run in this review |
| CI declaration | `partial` | `.gitlab-ci.yml` exists; runner proof not observed |
| README bootstrap status | `stale` | README still lists original bootstrap pins, not current lock |
| `.gitmodules` branch metadata | `stale` | advisory branches differ from current locked/observed branches |
| current baseline cleanliness | `partial` | submodule drift and parent doc/task-spec changes exist |

## 3. Asset Review

| Asset | Path | Exists | Status |
|---|---|---|---|
| root instructions | `AGENTS.md` | yes | `complete` |
| bootstrap report | `BOOTSTRAP_REPORT.md` | yes | `complete` |
| baseline lock | `BASELINE_LOCK.json` | yes | `complete` |
| submodule lock | `integration/lock/submodules.lock.yml` | yes | `complete` |
| gitmodules | `.gitmodules` | yes | `complete_with_stale_branch_metadata` |
| README | `README.md` | yes | `stale_bootstrap_snapshot` |
| completion matrix | `COMPLETION_MATRIX.md` | yes | `complete` |
| integration status | `INTEGRATION_STATUS.md` | yes | `complete` |
| risk register | `RISK_REGISTER.md` | yes | `complete` |
| runbook | `RUNBOOK.md` | yes | `complete` |
| GitLab CI | `.gitlab-ci.yml` | yes | `partial_runner_unknown` |

## 4. Runtime Governance Docs

`docs/agent-runtime/` includes:

- `operating-model.md`;
- `integration-contracts.md`;
- `verification-gates.md`;
- `tool-policy.md`;
- `capability-inventory.md`;
- `runtime-invariants.md`;
- `project-local-skill-bindings.md`;
- `reviewer-playbook.md`;
- `negative-acceptance-tests.md`;
- `negative-test-fixtures/`;
- `sub-agent-dispatch-protocol.md`;
- `dispatch-model-profiles.md`;
- `lessons-learned.md`;
- `governance-manifest.md`.

Parent conclusion: governance documentation is sufficient for continued Phase
0.5 planning.

## 5. Scripts

Scripts present:

- `scripts/check-submodules.ps1`;
- `scripts/readonly-inventory.ps1`;
- `scripts/review_a120_evidence_zip.py`.

This review did not run these scripts. Under the current safety boundary,
script execution should require script-safety review or explicit coordinator
approval.

## 6. CI

`.gitlab-ci.yml` exists and is aligned with read-only intent.

Current status:

- CI design: `present`;
- runner proof: `unknown`;
- runtime expansion: `not allowed`;
- final acceptance in CI: `not allowed`.

## 7. Local-Only Status

Current Phase 0.5 operating mode remains local-only/read-only for integration
planning.

Not authorized:

- live runtime;
- real paper data;
- live WriteLab;
- real Zotero/Obsidian/RAG;
- MiniApp real E2E;
- package install;
- submodule pin updates.

## 8. Current Gaps

| Gap | Severity | Next action |
|---|---|---|
| current submodule drift | high | wait for review, then update pin readiness matrix |
| README lists bootstrap-era pins | medium | update only after coordinator decides canonical status wording |
| `.gitmodules` advisory branch metadata is stale | medium | cleanup only after coordinator approval |
| GitLab runner proof absent | medium | collect runner artifact later; do not infer pass |
| scripts not run | low | keep as not-run unless script-safety approval exists |

## 9. Decision

Phase 0.5 should be treated as:

```text
BOOTSTRAP_ASSETS_PRESENT
CURRENT_BASELINE_NOT_CLEAN_FINAL
PARENT_PLANNING_CAN_CONTINUE
PIN_AND_RUNTIME_NO_GO
```

## 10. Parent Conclusion

S02 is complete enough for parent planning v1.

The next useful parent artifact is S03/S05 boundary and architecture refinement,
using the already produced inventory, pin matrix, contract matrix, negative
matrix, and CI/canary plan.
