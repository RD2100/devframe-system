# Paper Integration

Date: 2026-06-15

This directory tracks the devframe-system integration plan for paper workflow
development. The source implementation currently lives in
`dev-frame-opencode/ai-workflow-hub`.

## Boundary

- `dev-frame-opencode` owns paper CLI/runtime/source implementation.
- `devframe-system` owns integration gates, privacy expectations, reviewer
  evidence boundaries, and cross-module readiness.
- Real paper full text is sensitive by default.
- No paper runtime or external WriteLab operation may run without explicit
  RuntimeAuthorization.

## Active Focus

1. Keep paper privacy/redaction gates fail-closed for reports, audit ZIPs, and
   reviewer packs.
2. Keep paper CLI status, artifact verification, and final acceptance as
   separate user-visible meanings.
3. Use test-frame negative fixtures for paper/WriteLab reviewer-pack privacy
   and fake-green canaries.
4. Keep real paper content and live WriteLab flows blocked until fresh
   RuntimeAuthorization exists.
5. Review the machine-readable Paper Function Business Validation report
   candidate with synthetic/offline evidence; keep real content gated by the
   pinned SD-07 boundary and fresh RuntimeAuthorization.
6. Treat the SD-07 report UX, negative canary, and control-plane dry-run guard
   as a cross-module readiness slice that still requires independent review.

## Current Gate

`PAPER_SD07_READINESS_SLICES_PINNED`

Next target:

Independent review of the SD-07 readiness slices, then a separate pilot
TaskSpec only after fresh RuntimeAuthorization exists. SD-07 is pinned in
`agent-acceptance` commit `38d7b2e`; `dev-frame-opencode` commit `0c24204`
exposes it in the report artifact; `test-frame` commit `7940891` adds the
synthetic-live canary; `devframe-control-plane` commit `7939954` adds the
dry-run dispatch guard. This is a gate, not authorization to run real paper
content.
