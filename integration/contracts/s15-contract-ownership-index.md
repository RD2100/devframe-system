# S15 Contract Ownership Index

Date: 2026-06-16
Parent repo: `D:\devframe-system`
Status: `S15_CONTRACT_OWNERSHIP_DEFINED`

## Purpose

This index defines which layer owns each cross-repo contract and what that
contract can and cannot prove in S15.

No contract below can self-promote to final governance acceptance.

## Ownership Table

| Contract | Primary owner | S15 state | Can prove | Cannot prove |
|---|---|---|---|---|
| `TaskSpec` | `agent-acceptance` / parent coordinator | `CANDIDATE` | scoped work intent, allowed files, boundaries | implementation success |
| `Gate0Preflight` | `agent-acceptance` | `CANDIDATE` | preflight shape and blocked conditions | runtime authorization |
| `RuntimeAuthorization` | parent + human approver | `HUMAN_REQUIRED` | explicit bounded permission when approved | success, final acceptance, broader resource access |
| `HumanRuntimeAuthorizationDecision` | human approver + parent record | `HUMAN_REQUIRED` | one scoped human decision | reusable or wildcard authorization |
| `TestRunSpec` | `test-frame` + parent | `CANDIDATE` | intended verification run shape | real-world correctness |
| `TestExecutionReport` | runtime/test provider | `READ_ONLY_EVIDENCE` | observed test execution evidence | final governance acceptance |
| `ExecutionReport` | executing child module | `READ_ONLY_EVIDENCE` | commands, changed files, tests, artifacts | independent review |
| `EvidenceManifest` | evidence producer + reviewer | `READ_ONLY_EVIDENCE` | artifact paths, hashes, provenance | approval or runtime success |
| `ReviewVerdict` | independent reviewer / GPT-bound review | `REVIEW_INPUT_ONLY` | reviewed scope, limitations, rework status | final governance acceptance |
| `FinalVerdict` | parent governance layer | `NOT_AVAILABLE` | final decision after all gates | anything unless explicitly issued |
| `SubmoduleLock` | parent superproject | `PARENT_ACTION_ONLY` | parent-selected commit baseline | child runtime correctness |
| `CapabilityMap` | opencode candidate + parent review | `CANDIDATE` | declared capability status and gaps | production readiness |
| `BusinessValidationReport` | opencode candidate + test-frame checks | `CANDIDATE` | metadata MVP evidence matrix shape | final paper acceptance |
| `ParentCanaryFixture` | parent/test-frame | `DESIGN_ONLY` | negative overclaim cases | live canary execution |
| `RollbackDrillSpec` | parent | `DESIGN_ONLY` | intended rollback procedure | executed rollback proof |

## Cross-track Mapping

| Completion track | Required contracts | S15 status |
|---|---|---|
| Integration superproject | `SubmoduleLock`, `ExecutionReport`, `ReviewVerdict` | metadata MVP usable |
| Cross-repo contracts | all contracts in this index | candidate-defined |
| Opencode adapter | `ExecutionReport`, `EvidenceManifest`, `BusinessValidationReport` | metadata-only candidate |
| Test-frame adapter / TestRunSpec | `TestRunSpec`, `TestExecutionReport`, fixtures | synthetic/offline candidate |
| Control-plane state machine | `DispatchAssignment`, `WorkerLease`, `SourceLock`, `ExecutionReport` | frozen/design-only |
| Artifact registry / evidence store | `EvidenceManifest`, parent report index | candidate |
| RuntimeAuthorization signer / validator | `RuntimeAuthorization`, human decision, audit event | human-required |
| Source-level safety review | reviewer report, targeted tests, negative probes | candidate/incomplete |
| Dry-run end-to-end harness | `TestRunSpec`, `ExecutionReport`, `EvidenceManifest` | design/candidate |
| Canary repo + rollback drill | canary fixtures, rollback drill spec | design-only |

## Promotion Rules

Allowed:

- `ExecutionReport` plus parent review can support parent pin.
- `EvidenceManifest` plus hash verification can support evidence intake.
- `ReviewVerdict` plus parent review can support accepted-with-limitations.
- Metadata-only reports can support `METADATA_ONLY_VERIFIED`.

Forbidden:

- `ExecutionReport` cannot issue `FinalVerdict`.
- `TestExecutionReport` cannot issue `FinalVerdict`.
- `EvidenceManifest` cannot issue `FinalVerdict`.
- `RuntimeAuthorization` cannot be inferred from schema validity.
- `ReviewVerdict` cannot authorize a broader resource class than reviewed.
- `SubmoduleLock` cannot prove production readiness.
- `CapabilityMap` cannot prove runtime availability.

## Final Governance Boundary

`FinalVerdict` remains `NOT_AVAILABLE` in S15.

Before `FinalVerdict` can become available, the parent must have:

1. a final-verdict rule center result;
2. independent reviewer provenance;
3. explicit resource-class accounting;
4. no unresolved `HUMAN_REQUIRED` or `NO_GO` blockers;
5. no raw/private evidence leakage;
6. a parent decision that is not produced by any child executor.

## S15 Conclusion

The parent now has contract ownership clarity for a metadata-only governance
MVP. Runtime activation and final acceptance remain outside the S15 contract
state.
