# Integration Reports

Date: 2026-06-15

This directory is reserved for future generated or manually reviewed integration
reports.

Current reports:

- `phase-0.5-1b-checkpoint.md` records the `/rdinit`, Phase 0.5,
  four-submodule contract branches, paper focus, and static verification
  checkpoint.
- `security-preflight-2026-06-15.md` records the canonical clean baseline,
  SkillSpector availability, focused security findings, P1 fix commits
  `4558ab8` and `40ee21b`, and independent-review pass boundary before Paper
  Function Business Capability Validation.
- `paper-business-validation-2026-06-15.md` records the synthetic/offline
  machine-readable Paper Business Validation report artifact candidate,
  sub-agent outputs, main-thread verification, and non-final-acceptance
  boundary.
- `sd07-runtime-authorization-boundary-2026-06-15.md` records the
  `agent-acceptance` SD-07 real-content/live WriteLab RuntimeAuthorization
  boundary implementation and main-thread verification.
- `sd07-readiness-slices-2026-06-15.md` records the cross-module SD-07
  readiness slices in `dev-frame-opencode`, `test-frame`, and
  `devframe-control-plane`, plus main-thread verification.
- `a120/a120-evidence-zip-review.json` and
  `a120/a120-evidence-zip-review.md` record the independent A120 evidence ZIP
  review boundary.

Current policy:

- Do not store live runtime reports here until a TaskSpec authorizes the run.
- Do not store final acceptance here unless the report includes independent
  reviewer evidence and governance approval.
- Historical reports must state their source path, command, timestamp, and
  whether external runtime was executed.
