# devframe-system Target Architecture And DAG v1

Date: 2026-06-15
Scope: parent-level architecture and execution DAG
Runtime: not executed
Slice: S05

## 1. Purpose

This report defines the target architecture for a practical devframe-system
toolchain.

The goal is not a perfect platform. The goal is a usable, evidence-backed
workflow where offline candidates, tests, reviews, and final acceptance remain
separate.

## 2. Four-Layer Architecture

| Layer | Owner | Produces | Does not produce |
|---|---|---|---|
| worker layer | `dev-frame-opencode` and other executors | artifacts, diffs, ExecutionReport, candidate outputs | reviewer approval or final acceptance |
| verification layer | `test-frame` | TestRunSpec, TestExecutionReport, dry-run/live blocked semantics | final acceptance |
| review layer | independent reviewer and ZIP verifier | ReviewVerdict, EvidenceZipReviewReport, reviewer pack checks | worker implementation or final governance |
| governance layer | `agent-acceptance` plus human/main coordinator | GateResult, FinalVerdict boundary, fake-green prevention | runtime execution or submodule implementation |

Parent role:

- maintain the ledger and standards;
- compare evidence against contracts;
- recommend Go/No-Go;
- never collapse the layers.

## 3. Control-Plane Position

`devframe-control-plane` stays frozen.

It may provide vocabulary or future contracts for:

- DispatchAssignment;
- WorkerLease;
- SourceLock;
- heartbeat/worker state.

It must not be required for the current offline MVP path.

## 4. Runtime/Data Boundary

Real external data and services require all of:

- RuntimeAuthorization;
- redaction rules;
- EvidenceManifest;
- human gate;
- blocked/failed semantics;
- independent review.

Until those exist, real Zotero, Obsidian, RAG, WriteLab, MiniApp real E2E,
browser/CDP, cloud, and private paper content remain blocked.

## 5. Evidence Flow DAG

```mermaid
flowchart TD
  A["TaskSpec or parent plan"]
  B["RuntimeAuthorization if live or private"]
  C["Worker execution or offline candidate"]
  D["ExecutionReport"]
  E["TestRunSpec"]
  F["TestExecutionReport"]
  G["EvidenceManifest"]
  H["ReviewerEvidencePack"]
  I["EvidenceZipReviewReport"]
  J["ReviewVerdict"]
  K["GateResult"]
  L["FinalVerdict boundary"]
  M["Parent pin readiness matrix"]
  N["Main coordinator pin decision"]

  A --> C
  A --> E
  B --> C
  C --> D
  E --> F
  D --> G
  F --> G
  G --> H
  H --> I
  H --> J
  I --> K
  J --> K
  K --> L
  L --> M
  M --> N
```

## 6. Planning Slice DAG

```mermaid
flowchart TD
  S00["S00 Constraint And Evidence Vocabulary"]
  S01["S01 Reality Inventory"]
  S02["S02 Phase 0.5 State Review"]
  S03["S03 Boundary Assessment"]
  S04["S04 ZIP Evidence Discovery"]
  S05["S05 Architecture And DAG"]
  S06["S06 Contract Alignment"]
  S07["S07 Negative Matrix"]
  S08["S08 CI Canary Risk Plan"]
  S09["S09 Master Plan v1 Go/No-Go"]

  S00 --> S01
  S01 --> S02
  S01 --> S03
  S01 --> S04
  S02 --> S05
  S03 --> S05
  S04 --> S05
  S05 --> S06
  S06 --> S07
  S05 --> S08
  S07 --> S08
  S08 --> S09
```

## 7. Non-Equivalent Success States

| State | Not equivalent to |
|---|---|
| TaskSpec exists | task executed |
| DispatchAssignment exists | task succeeded |
| ExecutionReport pass | reviewer accepted |
| TestExecutionReport pass | final acceptance |
| EvidenceZipReviewReport pass | global evidence accepted |
| ReviewVerdict pass | lock pin approved |
| RuntimeAuthorization exists | run succeeded |
| aligned lock | production ready |

## 8. Practical MVP Shape

The practical usable toolchain needs:

1. offline paper MVP can run on synthetic fixtures;
2. fake-green gates reject candidate/final confusion;
3. test-frame can distinguish dry-run, blocked, failed, and later live pass;
4. parent can see inventory, contract alignment, negative matrix, and pin status;
5. real data/runtime remains human-gated.

## 9. Parent Conclusion

S05 is complete enough for Master Plan v1.

The architecture supports continuing parent planning while submodules
self-iterate. It also prevents a common failure mode: treating a lower-layer
success as final readiness.
