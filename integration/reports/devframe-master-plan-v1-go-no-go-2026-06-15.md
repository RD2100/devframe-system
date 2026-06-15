# devframe-system Master Plan v1 Go/No-Go

Date: 2026-06-15
Scope: parent repository completeness plan
Runtime: not executed
Slice: S09

## 1. Executive Summary

Parent-level devframe-system completeness planning is now complete enough for
the current cycle.

The parent repo now has:

- S00 constraint and evidence vocabulary;
- S01 reality inventory;
- S02 Phase 0.5 state review;
- S03 governance boundary assessment;
- S04 ZIP evidence discovery;
- S05 target architecture and DAG;
- S06 contract alignment matrix;
- S07 parent negative matrix;
- S08 CI/canary/risk work plan;
- S09 Go/No-Go summary.

Main conclusion:

```text
PARENT_PLANNING_READY
PIN_UPDATE_NO_GO
REAL_RUNTIME_NO_GO
FINAL_READY_NO_GO
SUBMODULE_REPORT_REVIEW_REQUIRED
```

## 2. Reality Inventory

Current parent state:

| Item | Status |
|---|---|
| parent root | `D:\devframe-system` verified |
| parent branch | `codex/rdinit-phase-0-5` |
| parent worktree | dirty with parent docs/task specs and submodule drift |
| active upstream | none configured |
| four submodule paths | exist |
| A120 review files | exist |

Submodule lock state:

| Module | Lock vs observed | Decision |
|---|---|---|
| `agent-acceptance` | drift | no pin |
| `dev-frame-opencode` | drift | no pin |
| `devframe-control-plane` | aligned | keep frozen |
| `test-frame` | drift | no pin |

## 3. Current Integration Status

Phase 0.5 bootstrap assets are present.

Current baseline is not clean-final because:

- three submodules are ahead of lock;
- parent planning docs are newly created;
- some existing task-spec files are untracked;
- GitLab runner proof is not observed.

This is not a blocker for parent planning. It is a blocker for pin/final claims.

## 4. Boundary Assessment

The architecture boundary is now explicit:

- workers produce artifacts and ExecutionReports;
- test-frame produces TestRunSpec/TestExecutionReport;
- reviewers and ZIP tools produce bounded review evidence;
- agent-acceptance/governance produces gate/final-verdict boundaries;
- parent collects, classifies, aligns, and recommends.

No lower layer may self-promote to final acceptance.

## 5. ZIP Assessment

A120 evidence review exists and is bounded.

Global A101-A120 acceptance is unknown.

Current conclusion:

| Question | Answer |
|---|---|
| Is A120 review output present? | yes |
| Was the reviewer script rerun in this cycle? | no |
| Is A120 final acceptance? | no |
| Are all A101-A120 packs inventoried? | no |
| Can ZIP review replace governance final verdict? | no |

## 6. Architecture

The target architecture is a four-layer evidence chain:

1. worker layer;
2. verification layer;
3. review layer;
4. governance layer.

Parent repo stays above these as the ledger and Go/No-Go layer.

`devframe-control-plane` remains frozen and optional for MVP.

## 7. DAG

Current parent slice DAG:

```text
S00 -> S01
S01 -> S02, S03, S04
S02/S03/S04 -> S05
S05 -> S06
S06 -> S07
S05/S07 -> S08
S08 -> S09
```

Current evidence DAG:

```text
TaskSpec
  -> ExecutionReport / TestExecutionReport
  -> EvidenceManifest
  -> ReviewerEvidencePack
  -> EvidenceZipReviewReport / ReviewVerdict
  -> GateResult
  -> FinalVerdict boundary
  -> Pin readiness matrix
  -> Main coordinator pin decision
```

## 8. Contracts

S06 aligned these core contracts:

- TaskSpec;
- DispatchAssignment;
- RuntimeAuthorization;
- WorkerLease;
- SourceLock;
- RunSpec;
- ExecutionReport;
- TestRunSpec;
- TestExecutionReport;
- EvidenceIndex;
- EvidenceManifest;
- ReviewerEvidencePack;
- EvidenceZipReviewReport;
- ReviewVerdict;
- GateResult;
- FailureRecord;
- AuditEvent;
- FinalVerdict.

Missing centralized parent schemas remain for:

- RuntimeAuthorization;
- TestRunSpec;
- TestExecutionReport;
- FailureRecord;
- AuditEvent;
- FinalVerdict mapping.

These are next-phase documentation/schema tasks, not blockers for this parent
planning cycle.

## 9. Testing Strategy

Allowed now:

- read-only file inspection;
- read-only git inspection;
- markdown consistency checks;
- `git diff --check`;
- report-level negative case design.

Not allowed now:

- real MiniApp E2E;
- live Zotero/Obsidian/RAG/WriteLab;
- private paper data;
- package install;
- build/runtime tests;
- submodule pin updates.

## 10. Negative Matrix

S07 adds 16 parent-specific negative cases covering:

- offline candidate overclaim;
- dry-run/live confusion;
- test pass promoted to final acceptance;
- dispatch success promoted to task success;
- ZIP review overreach;
- pin drift overclaim;
- missing RuntimeAuthorization;
- private content leakage;
- missing EvidenceManifest;
- reviewer/executor collision;
- CI runtime expansion.

These are design/report checks for now. No real runtime is required.

## 11. GitLab Plan

GitLab CI should remain read-only.

Allowed CI classes:

- git status;
- submodule status;
- diff/whitespace checks;
- read-only inventory after script-safety approval.

Forbidden CI classes:

- install;
- runtime;
- live adapters;
- pin mutation;
- final acceptance.

GitLab runner proof remains `human_required`.

## 12. ZIP Verifier Plan

Near-term plan:

- keep A120 bounded;
- inventory A101-A120 evidence paths before any global claim;
- separate ZIP structure review from reviewer identity and governance verdict;
- reject copy-forward/template acceptance without evidence.

## 13. Roadmap

Next parent work after this cycle:

1. Create centralized contract docs/schemas for missing contracts.
2. Create parent canary fixture plan for NEG-PARENT cases.
3. Inventory A101-A120 packs if main coordinator provides paths.
4. Review submodule reports when returned.
5. Update pin readiness matrix after review.
6. Only then consider lock updates.

## 14. Risk Register

Top active risks:

| Risk | Current control |
|---|---|
| fake green | S00 vocabulary, S07 negative matrix |
| offline candidate promoted too early | S03 boundary, S07 negatives |
| pin drift accidentally accepted | S01 inventory, pin matrix |
| ZIP review over-scoped | S04 discovery |
| live/private data leak | RuntimeAuthorization and redaction required |
| CI runtime expansion | S08 read-only plan |
| control-plane scope creep | frozen status |

## 15. Parallel And Serial Plan

Parallel can continue:

- submodules self-iterate;
- parent maintains reports and matrices;
- main coordinator collects reports.

Serial must wait:

- independent submodule review;
- pin readiness update;
- coordinator pin decision;
- human authorization for live runtime;
- final governance verdict.

## 16. Go/No-Go

| Area | Decision |
|---|---|
| parent completeness planning | `GO` |
| use reports as review standard | `GO` |
| continue submodule self-iteration | `GO` |
| update submodule pins | `NO-GO` |
| run real runtime | `NO-GO` |
| connect real Zotero/Obsidian/RAG/WriteLab | `NO-GO` |
| call paper offline MVP production ready | `NO-GO` |
| call test-frame dry-run live pass | `NO-GO` |
| call A120 ZIP review final acceptance | `NO-GO` |
| claim full project final-ready | `NO-GO` |

## 17. Immediate TaskSpecs

Suggested parent tasks:

```text
SUGGESTED_TASK_FOR_DEVFRAME_SYSTEM:
- task_id: DFS-CONTRACT-SCHEMA-GAPS-V1
- goal: document or draft parent schemas for RuntimeAuthorization, TestRunSpec, TestExecutionReport, FailureRecord, AuditEvent, and FinalVerdict mapping.
- allowed files: integration/contracts/**, schemas/agent-runtime/**, integration/reports/**
- expected tests: schema/doc consistency review only.
- acceptance criteria: each missing contract has owner, required fields, invalid cases, and phase boundary.
- risk: high
```

```text
SUGGESTED_TASK_FOR_DEVFRAME_SYSTEM:
- task_id: DFS-PARENT-CANARY-FIXTURE-PLAN-V1
- goal: design synthetic fixture files for NEG-PARENT-001 through NEG-PARENT-016 without executing runtime.
- allowed files: integration/reports/**, docs/agent-runtime/**
- expected tests: no runtime; fixture design review only.
- acceptance criteria: every negative case has fixture type, expected result, and future owner.
- risk: medium
```

```text
SUGGESTED_TASK_FOR_DEVFRAME_SYSTEM:
- task_id: DFS-PIN-READINESS-UPDATE-AFTER-REPORTS
- goal: update pin readiness only after accepted submodule reports return.
- allowed files: integration/reports/**
- expected tests: read-only evidence review.
- acceptance criteria: every observed head has review status, allowed claims, forbidden claims, and coordinator decision field.
- risk: high
```

## 18. Commands Not Run

This cycle did not run:

- project scripts;
- tests;
- build tools;
- package installers;
- GitLab runner jobs;
- external runtime;
- live adapters;
- MiniApp real E2E;
- submodule pin updates;
- commits or pushes.

## 19. Human Required Items

Human or main-coordinator action is required for:

- approving real runtime;
- approving private paper data use;
- accepting GitLab runner proof;
- approving submodule pin changes;
- deciding whether to clean stale `.gitmodules` advisory branches;
- approving any final-ready claim.

## 20. Final Recommendation

Use this v1 report as the parent review standard.

The devframe-system parent task for this cycle is complete enough: the project
now has a coherent completeness plan, reality inventory, boundary model,
contract matrix, negative matrix, CI/canary/risk plan, and Go/No-Go result.

The next stop condition is external to this planning role: accepted submodule
reports, human runtime authorization, or main-coordinator pin decisions.
