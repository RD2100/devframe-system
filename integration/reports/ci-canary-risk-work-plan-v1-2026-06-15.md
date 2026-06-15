# devframe-system CI Canary Risk Work Plan v1

Date: 2026-06-15
Scope: parent-level S08 plan
Runtime: not executed
Sources:

- `.gitlab-ci.yml`
- `integration/runbooks/gitlab-ci-readonly-policy.md`
- `RISK_REGISTER.md`
- `integration/reports/reality-inventory-v1-2026-06-15.md`
- `integration/reports/phase-negative-matrix-v1-2026-06-15.md`

## 1. Purpose

This report defines the S08 parent plan for read-only GitLab CI, canary policy,
risk handling, parallel/serial execution, and promotion conditions.

No CI file was changed by this report.

## 2. Current GitLab CI Boundary

Allowed now:

- inspect git status;
- inspect submodule status;
- run whitespace/diff checks;
- run read-only inventory checks after script-safety review;
- publish read-only evidence.

Forbidden now:

- install packages;
- run build tools without approval;
- run tests that execute runtime;
- run MiniApp/browser/CDP/cloud;
- run live Zotero/Obsidian/RAG/WriteLab;
- mutate submodule pins;
- produce final acceptance.

## 3. Required CI Guardrails

| Guardrail | Required behavior |
|---|---|
| CI command allowlist | only read-only commands unless explicitly approved |
| Runtime ban | no external runtime in Phase 0.5/0.6 parent CI |
| Artifact boundary | CI artifacts must be reports/logs only, no private data |
| Submodule pin ban | CI must not update lock files or commit pointers |
| Failure semantics | unavailable check is `blocked`, failed check is `failed`, never pass |
| Review boundary | CI pass is not final acceptance |

## 4. Canary Policy

Canary goal:

- test parent contracts and negative fixtures against synthetic local inputs;
- never require private paper content or live services;
- never require control-plane worker expansion;
- never update submodule pins.

Canary must fail on:

- offline candidate promoted to final;
- dry-run promoted to live;
- missing EvidenceManifest;
- reviewer/executor collision;
- drifted commit marked pin-ready;
- read-only CI expanded to runtime command.

## 5. Top Risk Controls

| Risk | Current control | S08 next action |
|---|---|---|
| fake green | existing NEG tests plus S07 parent matrix | add parent fixture plan before automation |
| dispatch success as task success | contract alignment matrix | keep dispatch/execute/review/final separate |
| reviewer/executor collision | SADP reviewer node | require reviewer identity in report checks |
| out-of-scope writes | write-set gates in submodules | parent records allowed files in TaskSpecs only |
| ZIP overreach | A120 boundary report | expand ZIP inventory before global claims |
| live runtime over-promotion | RuntimeAuthorization requirement | keep all live pilots human-gated |
| private paper data leakage | privacy gates and redaction requirements | no real data in parent reports |
| submodule drift | reality inventory and pin matrix | no pin until independent review |
| stale `.gitmodules` advisory branch | S01 inventory | cleanup only after coordinator approval |
| CI expansion | read-only policy | require policy diff review |

## 6. Parallel Work Allowed Now

Parent can continue in parallel on:

- S02 Phase 0.5 state review;
- S03 boundary assessment;
- S04 ZIP evidence discovery;
- S05 architecture/DAG refinement;
- S08 CI/canary/risk plan maintenance;
- TaskSpec suggestions for later main-coordinator dispatch.

Submodules can continue self-iteration in parallel, but parent must classify
their new heads as `observed` until reviewed.

## 7. Serial Work Required Later

These must remain serial:

1. Receive submodule final reports.
2. Review evidence paths and changed files.
3. Run or inspect allowed verification only.
4. Update pin readiness matrix.
5. Main coordinator decides whether to update lock files.
6. Only then update pins.
7. Only after human approval run real pilots.
8. Only after reviewer/governance evidence claim final readiness.

## 8. Phase Conditions

| Phase | Entry condition | Exit condition |
|---|---|---|
| Phase 0.5 | current parent bootstrap exists | S00-S09 parent reports complete with no fake-green gaps |
| Phase 0.6 | parent contract/negative matrix accepted | read-only CI proof and canary fixture plan accepted |
| Phase 1 | offline MVP candidate evidence accepted | no live/private claims; no pin drift unresolved |
| Phase 1A | RuntimeAuthorization schema accepted | denied live cases fail closed |
| Phase 1B | test-frame positive pilot spec accepted | no real runtime until human gate |
| Phase 2-pre | redaction/EvidenceManifest/human gate ready | synthetic canary passes and live plan approved |
| Phase 2 | authorized positive pilot | pilot evidence reviewed independently |
| Phase 3 | CI expansion proposal accepted | still no automatic final acceptance |
| Phase 4 | control-plane scope explicitly approved | worker/lease/source-lock semantics reviewed |
| Phase 5 | all evidence/review/final verdict contracts accepted | final readiness can be considered |

## 9. Immediate Parent Tasks

```text
SUGGESTED_TASK_FOR_DEVFRAME_SYSTEM:
- task_id: DFS-S02-PHASE-05-STATE-REVIEW-V1
- goal: classify parent Phase 0.5 status as complete/partial/missing/unknown.
- allowed files: integration/reports/**, COMPLETION_MATRIX.md, INTEGRATION_STATUS.md
- expected tests: read-only file and markdown consistency checks.
- acceptance criteria: every Phase 0.5 required asset has path, status, and gap.
- risk: high
```

```text
SUGGESTED_TASK_FOR_DEVFRAME_SYSTEM:
- task_id: DFS-S04-ZIP-EVIDENCE-DISCOVERY-V1
- goal: inventory A101-A120 evidence/reviewer/manifest coverage without running scripts.
- allowed files: integration/reports/**, integration/contracts/**
- expected tests: read-only artifact existence checks.
- acceptance criteria: each pack is verified/partial/missing/unknown with exact path.
- risk: high
```

```text
SUGGESTED_TASK_FOR_DEVFRAME_SYSTEM:
- task_id: DFS-S08-CANARY-FIXTURE-PLAN-V1
- goal: design synthetic parent canary fixtures for S07 negative cases.
- allowed files: integration/reports/**, docs/agent-runtime/**
- expected tests: no runtime; fixture design review only.
- acceptance criteria: every parent negative case has fixture type, expected result, and owner.
- risk: medium
```

## 10. Parent Conclusion

S08 is plan-ready.

The parent should keep CI read-only, avoid runtime expansion, and continue
S02/S03/S04/S05 while waiting for submodule reports. The next best parent report
is S02 Phase 0.5 State Review v1.
