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
| `TS-AGENT-ACCEPTANCE-SD07-AUTH-GATE.md` | `019ec6c5-0855-7b11-812a-a099010b9b18` | `agent-acceptance` | readonly completed; implementation completed in `38d7b2e` |
| `TS-CONTROL-PLANE-DRY-RUN-STATE-MACHINE.md` | `019ec6c4-a05c-7053-966e-a260f5b51aa1` | `devframe-control-plane` | completed in `b001cea` |
| `TS-OPENCODE-PAPER-SD07-REPORT-UX.md` | `019ec6c5-7d65-76e2-b9a6-9316c75aeae8` | `dev-frame-opencode` | completed in `0c24204` |
| `TS-TEST-FRAME-SD07-NEGATIVE-REVIEW.md` | `019ec6c6-5238-74b3-8870-c973bee56131` | `test-frame` | completed in `7940891` |
| `TS-CONTROL-PLANE-PAPER-AUTH-DRY-RUN-GUARD.md` | `019ec6c4-a05c-7053-966e-a260f5b51aa1` | `devframe-control-plane` | completed in `7939954` |

## Next Required Assignment

Review the cross-module SD-07 readiness slices pinned in
`integration/reports/sd07-readiness-slices-2026-06-15.md`, then run the next
targeted Security Preflight slice before preparing any real-content pilot
TaskSpec.

The current next slices are independent guardrail/readiness tasks. None of them
authorize real paper content, live WriteLab, external runtime, or final
acceptance.
