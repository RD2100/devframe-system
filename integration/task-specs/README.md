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
| `TS-AGENT-ACCEPTANCE-SD07-READINESS-REVIEW.md` | `019ec6c5-0855-7b11-812a-a099010b9b18` | `agent-acceptance` | dispatched |
| `TS-OPENCODE-SECURITY-PREFLIGHT-FOCUSED-REFRESH.md` | `019ec6c5-7d65-76e2-b9a6-9316c75aeae8` | `dev-frame-opencode` | dispatched |
| `TS-TEST-FRAME-SD07-CANARY-ALIGNMENT.md` | `019ec6c6-5238-74b3-8870-c973bee56131` | `test-frame` | dispatched |
| `TS-CONTROL-PLANE-RUNTIME-AUTH-SCHEMA-ALIGNMENT.md` | `019ec6c4-a05c-7053-966e-a260f5b51aa1` | `devframe-control-plane` | dispatched |
| `TS-AGENT-ACCEPTANCE-PARENT-CANARY-GATE-A1.md` | `019ec6c5-0855-7b11-812a-a099010b9b18` | `agent-acceptance` | returned `PARENT_CANARY_GATE_GAP_FIXED` in `b9bb53a`; parent intake accepted |
| `TS-TEST-FRAME-PARENT-CANARY-REPORT-A1.md` | `019ec6c6-5238-74b3-8870-c973bee56131` | `test-frame` | returned `PARENT_CANARY_REPORT_GAP_FIXED` in `eed8d88`; parent intake accepted |

## Next Required Assignment

Review `integration/reports/parent-pin-review-a10-2026-06-15.md` before
preparing any pin proposal.

The current next work is to fresh re-check and, if stable, update parent
gitlinks and lock files to the A10 candidate set.

Current `dev-frame-opencode` note:

- The existing module thread returned metadata-only Zotero export hardening at
  `9d4c2f62c636d91641c5843c43eaa896fbba5243`.
- Parent intake accepted the return.
- Fresh parent observation found the module advanced to `3b2e4ae...` and is
  dirty again in a RIS metadata-only parser slice.
- The module then returned RIS metadata parser support at
  `cb4997ae91daed53d6a52193011ebc6701e94a01`.
- Parent intake accepted the RIS return.
- The module then returned metadata-only pilot scope limits at
  `6bd9809cc635e58e066cb0b3d1f38c2534b03d7a`.
- Parent intake accepted the scope-limit return; this supersedes the A6
  opencode pin choice.
- The module then returned export file type and encoding guard at
  `3a722134ca5f693f93796a6e63bc573109d2e48f`.
- Parent intake accepted the file-type guard return; this supersedes the A7
  opencode pin choice.
- The module then returned empty/unrecognized metadata fail-closed at
  `58b79e292bcf3ab4dbf66cb656f9827093f48dd0`.
- Parent intake accepted the empty metadata return; this supersedes the A8
  opencode pin choice.
- The module then returned evidence-manifest boundary at
  `a2cedaa280f12f717d4bf0a64c1c12ece6f5fefe`.
- Parent intake accepted the manifest boundary return; this supersedes the A9
  opencode pin choice. A HOLD was sent before parent pin.

Current `test-frame` note:

- The prior parent canary intake accepted `eed8d88...`.
- Fresh parent observation found `test-frame` at `c3353fb...`, worktree clean,
  with closeout evidence accepted by module GPT as
  `MILESTONE_READY_FOR_MAIN_CONTROL_PIN`.
- Parent intake accepted `c3353fb...` as a `test-frame` pin candidate.

Current parent decision:

- A10 grouped candidate heads are verified for parent pin review.
- Re-check module heads immediately before any lock/gitlink mutation.

None of this authorizes real paper content, live WriteLab, external runtime,
submodule pin updates, or final acceptance.
