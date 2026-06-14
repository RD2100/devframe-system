# TaskSpecs

Date: 2026-06-15

This directory records active and completed sub-agent assignments for
`devframe-system`.

Every TaskSpec must preserve these boundaries:

- No runtime execution unless a fresh RuntimeAuthorization explicitly allows it.
- No final acceptance claims from executor, runtime, or test summaries.
- No mutation of historical evidence archives.
- Every sub-agent report must include a Reviewer Index.

## Recent Assignments

| TaskSpec | Owner thread | Module | Status |
|---|---|---|---|
| `TS-PAPER-BUSINESS-REPORT-ARTIFACT.md` | `019ec6c5-7d65-76e2-b9a6-9316c75aeae8` | `dev-frame-opencode` | completed in `08ac4f5` |
| `TS-TEST-FRAME-BUSINESS-REPORT-NEGATIVES.md` | `019ec6c6-5238-74b3-8870-c973bee56131` | `test-frame` | completed in `891b106` |
| `TS-AGENT-ACCEPTANCE-SD07-AUTH-GATE.md` | `019ec6c5-0855-7b11-812a-a099010b9b18` | `agent-acceptance` | completed-readonly; `SD07_TASKSPEC_REQUIRED` |
| `TS-CONTROL-PLANE-DRY-RUN-STATE-MACHINE.md` | `019ec6c4-a05c-7053-966e-a260f5b51aa1` | `devframe-control-plane` | completed in `b001cea` |

## Next Required Assignment

`agent-acceptance` needs an implementation TaskSpec for SD-07 real-content/live
WriteLab RuntimeAuthorization boundary before any real-content pilot can be
authorized.
