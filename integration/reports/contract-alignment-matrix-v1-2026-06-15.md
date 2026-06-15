# devframe-system Contract Alignment Matrix v1

Date: 2026-06-15
Scope: parent repository contract alignment
Runtime: not executed
Sources:

- `docs/agent-runtime/integration-contracts.md`
- `docs/agent-runtime/sub-agent-dispatch-protocol.md`
- `docs/agent-runtime/verification-gates.md`
- `integration/contracts/README.md`
- `integration/contracts/evidence-zip-review.md`
- `schemas/agent-runtime/`

## 1. Purpose

This report aligns the contract names currently used across parent planning,
runtime governance, evidence review, and submodule integration.

It does not change schemas. It defines the parent-level producer, consumer,
required fields, and invalid cases that future schema updates or submodule
reports must satisfy.

## 2. Alignment Rule

No contract may promote its own success to a later layer.

Required non-equivalence:

- `DispatchAssignment` success is not `ExecutionReport` success.
- `ExecutionReport` success is not `ReviewVerdict` success.
- `TestExecutionReport` pass is not `FinalVerdict`.
- `EvidenceZipReviewReport` pass is not global evidence acceptance.
- `RuntimeAuthorization` allows a bounded run; it is not a quality verdict.

## 3. Contract Matrix

| Contract | Current source | Producer | Consumer | Required fields | Invalid cases |
|---|---|---|---|---|---|
| `TaskSpec` | `schemas/agent-runtime/task-spec.schema.json`; SADP | planner or human operator | executor, reviewer, parent ledger | `task_id`, `title`, `priority`, `status`, `description`, write/read scope when delegated | duplicate `task_id`; missing scope; markdown-only fields copied as undeclared JSON; task asks for forbidden runtime |
| `DispatchAssignment` | integration target; related to multi-agent dispatch plan | main coordinator or control-plane layer | worker, parent ledger | assignment id, `task_id`, target worker, allowed repo/path, expected report path, lease/source-lock references | treated as task success; missing target; overlapping write scope; dispatch outside approved module |
| `RuntimeAuthorization` | integration target; paper/live gates | human approver plus parent/main coordinator | worker, test-frame, opencode, reviewer | authorization id, runtime type, data class, allowed commands, time window, redaction rules, evidence path | live/private run without approval; broad wildcard authorization; missing redaction; reused authorization outside scope |
| `WorkerLease` | control-plane target | control-plane layer | worker, finalizer, parent ledger | lease id, worker id, task id, acquired/expires timestamps, heartbeat state | stale worker completes task; overlapping active lease; dispatch success called execution success |
| `SourceLock` | `schemas/agent-runtime/source-lock-record.schema.json`; control-plane target | control-plane or parent lock manager | workers, reviewer, parent ledger | source id/path, locked commit, branch, owner, acquired/expires, write scope | source changes mid-review; missing commit; overlapping write lock; branch-only lock without commit |
| `RunSpec` | `schemas/agent-runtime/run-spec.schema.json`; core contract | runner or agent | evidence collector, gate runner | `run_id`, `task_id`, `started_at`, `status`, `exit_code` | exit code outside 0/1/2; no TaskSpec reference; `blocked` reported as pass |
| `ExecutionReport` | `schemas/agent-runtime/execution-report.schema.json`; core contract | executor or runtime provider | parent, reviewer, acceptance layer | report id, batch/task id, status, summary, changed files, commands, evidence references, known gaps | self-approved pass; missing reviewer artifacts for pass; changed files omitted; generated artifacts claimed without paths |
| `TestRunSpec` | integration target; test-frame contract | planner/test-frame requestor | test-frame | test id, target module, fixture/profile, runtime allowed flag, expected result, artifact/report path | real runtime hidden under dry-run; missing expected result; no blocked-by-env path |
| `TestExecutionReport` | integration target; test-frame output | test-frame | parent, reviewer, agent-acceptance | test id, run id, status, exit code, artifacts, blocked/failed reason, environment profile | test pass promoted to final acceptance; blocked/failed collapsed into pass; missing artifact path |
| `EvidenceIndex` | `schemas/agent-runtime/evidence-index.schema.json`; core contract | executor/evidence collector | reviewer, audit trail | evidence id, run id, artifact path/type, collected time, status, freshness | artifact outside root; stale evidence marked current; missing checksum when required |
| `EvidenceManifest` | `schemas/agent-runtime/evidence-manifest.schema.json` | runtime provider plus reviewer | ZIP reviewer, parent, acceptance layer | manifest id, acceptance id, schema version, artifact list, hashes, provenance, freshness | path traversal; hash mismatch; missing acceptance id; external manifest differs from ZIP manifest |
| `ReviewerEvidencePack` | SADP reviewer package target | finalizer or evidence packer | independent reviewer | diff, test output, safety report, chain evidence, reviewed inputs, executor id | executor reviews own work; missing reviewed inputs; pack includes private data without redaction |
| `EvidenceZipReviewReport` | `integration/contracts/evidence-zip-review.md` | independent ZIP reviewer | parent, reviewer, acceptance layer | zip path, manifest path, required checks, hash recompute result, verdict boundary | ZIP review treated as final verdict; absolute/path traversal entries accepted; hashes not recomputed |
| `ReviewVerdict` | `schemas/agent-runtime/review.schema.json`; SADP reviewer node | independent reviewer | finalizer, parent, agent-acceptance | reviewer id, executor id, verdict, findings, reviewed inputs | reviewer id equals executor id; P0/P1 open but pass; template `ACCEPTED` without evidence |
| `GateResult` | `schemas/agent-runtime/gate-result.schema.json`; verification gates | gate runner or agent-acceptance | parent, finalizer, release gate | gate id, run id, level, name, result, checked time, evidence ids | P0 fail not blocking; skipped gate reported pass; no evidence for pass |
| `FailureRecord` | integration target | executor, tester, reviewer, or parent | parent ledger, risk register | failure id, source contract, severity, status, blocking reason, next owner | failure swallowed; blocked marked pass; no owner for human-required gap |
| `AuditEvent` | integration target | parent, runner, reviewer, finalizer | audit trail, human reviewer | event id, timestamp, actor, action, subject id, before/after or reason | mutable history; missing actor; event claims unverified state change |
| `FinalVerdict` | integration target; governance layer | agent-acceptance or human governance | parent, release/readiness decision | verdict id, accepted inputs, gate summary, reviewer summary, limitations, final state | generated by executor; missing reviewer evidence; candidate promoted to final-ready |

## 4. Existing Schema Coverage

| Contract | Existing schema status | Parent action |
|---|---|---|
| `TaskSpec` | present | use as canonical task contract |
| `RunSpec` | present | use for command/test run records |
| `EvidenceIndex` | present | align with EvidenceManifest freshness |
| `GateResult` | present | enforce P0 blocked semantics |
| `ExecutionReport` | present | require reviewer index and known gaps |
| `EvidenceManifest` | present | use for artifact hash/provenance |
| `ReviewVerdict` | partial via `review.schema.json` | map to reviewer independence requirements |
| `SourceLock` | present as source-lock record | use before source-sensitive pin or runtime claims |
| `RuntimeAuthorization` | not centralized in parent schema | define or map before live adapter work |
| `TestRunSpec` | not centralized in parent schema | define with test-frame before positive pilot |
| `TestExecutionReport` | not centralized in parent schema | define with test-frame before positive pilot |
| `FailureRecord` | not centralized in parent schema | define before final readiness |
| `AuditEvent` | not centralized in parent schema | define before automated finalization |
| `FinalVerdict` | integration target | keep governance-owned |

## 5. Producer And Consumer Boundaries

Parent ledger may collect and classify evidence. It must not impersonate:

- executor;
- tester;
- independent reviewer;
- final governance verdict.

Submodules may produce their own reports, but parent acceptance requires:

- exact path references;
- command summaries;
- changed files;
- generated artifacts;
- known gaps;
- reviewer identity where applicable;
- explicit blocked/failed distinction.

## 6. Invalid Promotion Cases

These cases must fail future negative checks:

| Case | Must become |
|---|---|
| `ExecutionReport.status=pass` with no reviewer evidence | `blocked` |
| `TestExecutionReport.status=pass` used as final acceptance | `failed` |
| `EvidenceZipReviewReport=pass` for one pack used for all packs | `failed` |
| `RuntimeAuthorization` missing but live adapter ran | `blocked` |
| `DispatchAssignment` exists but no worker report | `blocked` |
| observed submodule HEAD differs from lock but is marked pin-ready | `failed` |
| reviewer id equals executor id | `failed` |
| dry-run evidence marked live positive pilot | `failed` |

## 7. Next Schema Work

Parent should next create or update schema/docs for:

- `RuntimeAuthorization`;
- `TestRunSpec`;
- `TestExecutionReport`;
- `FailureRecord`;
- `AuditEvent`;
- `FinalVerdict` mapping.

This should be done as parent contract documentation first. Submodule schema
changes should be dispatched only by the main coordinator.

## 8. Parent Conclusion

S06 has enough parent-level alignment for planning v1.

The next useful parent artifact is S07: a phase-tagged negative matrix that
turns the invalid promotion cases into concrete expected failures or blocked
states.
