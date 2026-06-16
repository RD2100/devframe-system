# S15 Execution State Machine Lock

Date: 2026-06-16
Parent repo: `D:\devframe-system`
Status: `STATE_MACHINE_BOUNDARY_LOCKED`

## State Set

| State | Meaning |
|---|---|
| `BLOCKED` | Work cannot proceed because a required condition failed or is missing. |
| `HUMAN_REQUIRED` | A human must authorize or decide before the next state. |
| `NO_GO` | The action is outside the current phase and cannot be opened by automation. |
| `PARENT_PLANNING_READY` | Parent may write plans, reports, and TaskSpecs only. |
| `CHILD_REPORT_REQUIRED` | A child module result is needed before parent review. |
| `DESIGN_ONLY` | Contract/design documentation is allowed; runtime is not. |
| `NOT_IMPLEMENTED` | The capability is not built or not wired at parent level. |
| `METADATA_ONLY_VERIFIED` | Metadata-only evidence was accepted within its limited scope. |
| `METADATA_ONLY_REJECTED` | Metadata-only evidence failed or overclaimed. |
| `FINAL_VERDICT_NOT_AVAILABLE` | Final governance acceptance cannot be issued. |

## Decision Rules

| Condition | Result |
|---|---|
| Any unresolved `NO_GO` | `BLOCKED` |
| Any unresolved `HUMAN_REQUIRED` | `HUMAN_REQUIRED` |
| Runtime execution detected without matching authorization | `INVALID_STATE` |
| Metadata-only evidence passes with correct boundaries | `METADATA_ONLY_VERIFIED` |
| Metadata-only evidence leaks raw/private data or overclaims | `METADATA_ONLY_REJECTED` |
| Child module reports pass but parent review is missing | `CHILD_REPORT_REQUIRED` |
| Parent has only design contracts | `DESIGN_ONLY` |
| Final verdict requested without final gate evidence | `FINAL_VERDICT_NOT_AVAILABLE` |

## Forbidden Promotions

These transitions are invalid in S15:

| From | To | Why invalid |
|---|---|---|
| `ExecutionReport: PASS` | `FinalVerdict: accepted` | Execution is not governance. |
| `Evidence ZIP hash matches` | `System verified` | ZIP evidence is not autonomous. |
| `Test-frame pass` | `Production ready` | Test-frame evidence is not production proof. |
| `Metadata-only pass` | `PDF/full-text ready` | Resource class changed. |
| `Dry-run pass` | `Live runtime ready` | Dry-run is not live execution. |
| `Child commit clean` | `Parent pin accepted` | Parent review is required. |
| `RuntimeAuthorization request shape valid` | `Runtime authorized` | Human decision is required. |
| `Control-plane schema exists` | `Control-plane active` | Runtime dispatch remains frozen. |

## Allowed Promotions

These transitions are allowed when evidence is present:

| From | To | Required evidence |
|---|---|---|
| Child `READY_FOR_PARENT_INTAKE` | Parent review report | commit, ZIP path, SHA256, tests, boundaries |
| Parent review accepted | Parent pin update | clean target commit, lock update, pin report |
| Metadata-only report pass | `METADATA_ONLY_VERIFIED` | minimized report, no raw/private leakage, no final claim |
| Design brief accepted | `DESIGN_ONLY` | docs/contracts only, no runtime side effects |

## Irreversibility Rules

1. `NO_GO` cannot be upgraded by child evidence.
2. `HUMAN_REQUIRED` cannot be bypassed by schema validity.
3. `METADATA_ONLY_VERIFIED` cannot imply any broader resource class.
4. `FINAL_VERDICT_NOT_AVAILABLE` remains until the final-verdict gate has
   independent reviewer provenance and parent governance evidence.

## Current S15 Parent State

Current parent status: `METADATA_ONLY_MVP_WITH_RUNTIME_BOUNDARY_LOCK`.

This means:

- metadata-only candidate evidence can be reviewed and pinned;
- runtime expansion remains closed;
- final governance acceptance is not available;
- control-plane activation, CI/CD, canary drills, and new live resources remain
  outside S15 execution scope.
