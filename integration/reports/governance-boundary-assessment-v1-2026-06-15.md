# devframe-system Governance Boundary Assessment v1

Date: 2026-06-15
Scope: parent-level module boundary assessment
Runtime: not executed
Slice: S03

## 1. Purpose

This report defines which layer may produce which claim in the current
devframe-system architecture.

It prevents four common mistakes:

- worker output treated as reviewer approval;
- test output treated as final acceptance;
- ZIP review treated as global evidence acceptance;
- observed submodule drift treated as pin readiness.

## 2. Parent Layer

`devframe-system` owns:

- reality inventory;
- lock and observed-head comparison;
- parent planning reports;
- integration contract alignment;
- negative matrix planning;
- CI/canary/risk planning;
- Go/No-Go recommendations.

`devframe-system` does not own:

- child-module implementation;
- child-module dispatch;
- submodule pin updates without coordinator decision;
- live runtime execution;
- final governance approval.

## 3. Module Boundaries

| Module | May produce | Must not produce | Current parent status |
|---|---|---|---|
| `agent-acceptance` | GateResult, ReviewVerdict, FinalVerdict boundary, fake-green gates, RuntimeAuthorization checks | worker implementation success, test-frame pass, opencode live readiness | `observed`; current head ahead of lock and needs review |
| `dev-frame-opencode` | paper workflow artifacts, offline MVP candidate reports, adapter boundaries, ExecutionReport | final acceptance, live readiness without authorization, private-data approval | `candidate`; offline only |
| `test-frame` | TestRunSpec, TestExecutionReport, dry-run and blocked/failed semantics, pilot prereq checks | final acceptance, governance approval, plugin identity | `observed`; current head ahead of lock and needs review |
| `devframe-control-plane` | DispatchAssignment, WorkerLease, SourceLock observation, dispatch state | task success, quality verdict, MVP blocker | `frozen`; aligned with lock |

## 4. Cross-Layer Claim Rules

| Claim | Required source | Parent status if missing |
|---|---|---|
| task executed | ExecutionReport plus evidence paths | `blocked` |
| tests passed | TestExecutionReport plus artifacts | `blocked` |
| reviewer accepted | ReviewVerdict from independent reviewer | `blocked` |
| evidence pack valid | EvidenceManifest plus bounded review report | `blocked` |
| live runtime authorized | RuntimeAuthorization with scope and redaction | `blocked` |
| final ready | FinalVerdict plus reviewed inputs and limitations | `blocked` |
| pin ready | independent review plus pin readiness matrix update | `blocked` |

## 5. Current Boundary Findings

| Finding | Severity | Status | Parent action |
|---|---|---|---|
| `agent-acceptance` current head has untracked evidence | high | `observed` | require accepted report before pin |
| `dev-frame-opencode` paper MVP is offline candidate | high | `candidate` | block live/final claims |
| `test-frame` current head adds positive pilot prereq gate | high | `observed` | require review before pin or pilot |
| `devframe-control-plane` is aligned but frozen | medium | `frozen` | keep out of MVP critical path |
| `.gitmodules` branches are stale advisory metadata | medium | `partial` | cleanup only after coordinator approval |

## 6. Governance Decision Table

| Input state | Parent decision |
|---|---|
| offline candidate with complete synthetic fixtures | useful, not final |
| dry-run pass with no real environment | useful, not live pass |
| environment missing and check cannot run | `blocked` |
| check ran and failed | `failed` |
| review report missing | `blocked` for acceptance |
| reviewer equals executor | `blocked` |
| submodule commit differs from lock | `observed drift` |
| aligned frozen module | keep frozen unless explicitly reopened |

## 7. Parent Conclusion

S03 is complete enough for parent planning v1.

The boundary is clear: parent can continue planning and evidence alignment, but
cannot turn submodule observations into pins, runtime approval, or final
acceptance.
