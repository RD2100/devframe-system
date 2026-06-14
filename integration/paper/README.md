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
5. Resolve Security Preflight P1 findings before Paper Function Business
   Capability Validation.

## Current Gate

`SECURITY_PREFLIGHT_IN_PROGRESS`

Next target after P1 security triage:

`Paper Function Business Capability Validation`
