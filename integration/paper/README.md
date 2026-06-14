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

1. Fix user-visible mojibake in paper schema and fixtures.
2. Define paper privacy/redaction gates at integration level.
3. Map paper CLI commands to status meanings and evidence outputs.
4. Add paper negative cases: real full text without authorization, memory write
   with paper content, unredacted evidence pack, human_required promoted to pass.
