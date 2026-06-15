# Integration Reports

Date: 2026-06-15

This directory is reserved for future generated or manually reviewed integration
reports.

Current reports:

- `parent-pin-review-a22-2026-06-15.md` records a no-go pin review after
  `dev-frame-opencode` moved past `7ffc609...` to a dirty `f5b0c80...` state.
- `opencode-capability-map-evidence-matrix-return-review-2026-06-15.md`
  records parent intake of the latest local/offline opencode capability-map
  and business validation evidence-matrix chain.
- `zotero-metadata-only-pilot-blocked-2026-06-15.md` records the first real
  Zotero metadata-only pilot attempt. The run was correctly blocked because the
  user-provided BibTeX export contained `abstract`, `file`, and `note` fields.
- `bound-gpt-consultation-review-2026-06-15.md` records the consultation with
  the bound ChatGPT conversation and the review verdict that its output was not
  usable as a plan.
- `constraint-evidence-vocabulary-v1-2026-06-15.md` records S00 allowed and
  forbidden actions, evidence vocabulary, non-equivalence rules, and report
  directory policy.
- `governance-boundary-assessment-v1-2026-06-15.md` records S03 parent and
  module boundaries: who may produce which claim and which promotions are
  blocked.
- `zip-evidence-discovery-v1-2026-06-15.md` records S04 ZIP evidence discovery:
  A120 review is bounded and verified locally; global A101-A120 acceptance is
  unknown.
- `target-architecture-dag-v1-2026-06-15.md` records S05 target architecture,
  evidence flow DAG, planning slice DAG, and non-equivalent success states.
- `devframe-master-plan-v1-go-no-go-2026-06-15.md` records S09 final parent
  completeness plan and Go/No-Go decision for this cycle.
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
- `devframe-master-plan-v0-2026-06-15.md` records the parent-only integrated
  S00-S09 plan, current reality inventory, Go/No-Go boundary, and next
  devframe-system task suggestions.
- `reality-inventory-v1-2026-06-15.md` records the S01 parent reality
  inventory: parent repo, submodules, lock drift, advisory branch mismatch,
  alias paths, reports, task specs, and A120 evidence paths.
- `pin-readiness-matrix-v1-2026-06-15.md` records the parent pin-readiness
  judgement: observed drift is not pin-ready; `devframe-control-plane` remains
  aligned and frozen.
- `pin-readiness-matrix-v2-2026-06-15.md` records updated pin readiness after
  parent canary intake: `agent-acceptance` and `test-frame` returns accepted
  for intake, but pin remains no-go.
- `parent-pin-review-a1-2026-06-15.md` records the explicit parent pin review
  after current drift inspection: no pin, no lock mutation, next step is
  module summaries/returns before any pin proposal.
- `opencode-dirty-state-observation-2026-06-15.md` records parent observation
  of active `dev-frame-opencode` dirty metadata-only Zotero hardening work and
  why parent pin remains no-go.
- `opencode-zotero-metadata-export-hardening-return-review-2026-06-15.md`
  records parent intake review of `dev-frame-opencode` commit `9d4c2f6`.
- `parent-pin-review-a2-2026-06-15.md` records the updated pin review:
  candidate pins are identifiable, but human/coordinator approval is required
  before any pin mutation.
- `parent-pin-review-a3-2026-06-15.md` records the post-A2 drift review:
  `dev-frame-opencode` and `test-frame` are dirty again, so parent pin is
  currently no-go.
- `parent-pin-review-a4-2026-06-15.md` records active module self-iteration:
  `dev-frame-opencode` is dirty in a RIS parser slice and `test-frame` is
  awaiting closeout GPT verdict, so parent pin remains no-go.
- `test-frame-readiness-closeout-return-review-2026-06-15.md` records parent
  intake of `test-frame` closeout milestone head `c3353fb...`.
- `parent-pin-review-a5-2026-06-15.md` records the updated parent pin review:
  `test-frame` is now a pin candidate, but grouped parent pin remains no-go
  because `dev-frame-opencode` is still active/dirty.
- `opencode-zotero-ris-metadata-parser-return-review-2026-06-15.md` records
  parent intake of `dev-frame-opencode` RIS metadata parser head `cb4997a...`.
- `parent-pin-review-a6-2026-06-15.md` records the grouped parent pin candidate
  set after opencode RIS and test-frame closeout returns; mutation still needs
  explicit approval.
- `opencode-zotero-metadata-scope-limits-return-review-2026-06-15.md` records
  parent intake of `dev-frame-opencode` metadata-only pilot scope-limit head
  `6bd9809...`; A6 opencode pin choice is superseded.
- `parent-pin-review-a7-2026-06-15.md` records the current grouped parent pin
  candidate set after opencode scope limits, test-frame closeout, and
  agent-acceptance parent canary return.
- `opencode-zotero-export-file-type-guard-return-review-2026-06-15.md`
  records parent intake of `dev-frame-opencode` metadata-only export file type
  guard head `3a72213...`; A7 opencode pin choice is superseded.
- `parent-pin-review-a8-2026-06-15.md` records the current grouped parent pin
  candidate set after opencode file type guard, test-frame closeout, and
  agent-acceptance parent canary return.
- `opencode-zotero-empty-metadata-failclosed-return-review-2026-06-15.md`
  records parent intake of `dev-frame-opencode` empty/unrecognized metadata
  fail-closed head `58b79e2...`; A8 opencode pin choice is superseded.
- `parent-pin-review-a9-2026-06-15.md` records the current grouped parent pin
  candidate set after opencode empty metadata fail-closed, test-frame closeout,
  and agent-acceptance parent canary return.
- `opencode-zotero-evidence-manifest-boundary-return-review-2026-06-15.md`
  records parent intake of `dev-frame-opencode` evidence-manifest boundary head
  `a2cedaa...`; A9 opencode pin choice is superseded.
- `parent-pin-review-a10-2026-06-15.md` records the current grouped parent pin
  candidate set after opencode evidence-manifest boundary, test-frame closeout,
  and agent-acceptance parent canary return.
- `grouped-parent-pin-a10-2026-06-15.md` records the grouped parent gitlink
  and lock update to the A10 candidate set.
- `opencode-zotero-evidence-manifest-schema-return-review-2026-06-15.md`
  records parent intake of `dev-frame-opencode` schema-gated evidence manifest
  head `f9d381c...`.
- `parent-pin-review-a11-2026-06-15.md` records the A11 opencode-only pin
  review after the A10 grouped baseline.
- `grouped-parent-pin-a11-2026-06-15.md` records the opencode-only parent
  gitlink and lock update to `f9d381c...`.
- `post-pin-status-a11-2026-06-15.md` records the current A11 post-pin state,
  including the `agent-acceptance` untracked evidence note and verification
  boundary.
- `agent-acceptance-a11-cross-module-smoke-return-review-2026-06-15.md`
  records parent intake of the read-only A11 cross-module lock/evidence smoke
  return from `agent-acceptance`.
- `stage-closeout-a11-2026-06-15.md` records the A11 stage closeout, current
  usable baseline, remaining human decisions, and no-real-runtime boundary.
- `agent-acceptance-evidence-ignore-a12-2026-06-15.md` records the narrow
  `agent-acceptance` local evidence ignore cleanup, parent gitlink/lock update,
  and the explicit decision not to pin concurrent `dev-frame-opencode` work.
- `opencode-zotero-manifest-record-shape-schema-return-review-2026-06-15.md`
  records parent intake of `dev-frame-opencode` A12 local/offline Zotero
  manifest record-shape schema hardening at `3c08f3a...`.
- `parent-pin-review-a12-2026-06-15.md` records the parent decision to pin
  `dev-frame-opencode` to `3c08f3a...` while preserving the no-real-runtime and
  no-final-acceptance boundary.
- `opencode-zotero-manifest-closed-shape-return-review-2026-06-15.md` records
  parent intake of `dev-frame-opencode` A13 local/offline Zotero manifest
  closed-shape schema hardening at `4d8c575...`.
- `parent-pin-review-a13-2026-06-15.md` records the parent decision to pin
  `dev-frame-opencode` to `4d8c575...` while preserving the no-real-runtime and
  no-final-acceptance boundary.
- `opencode-zotero-report-closed-shape-return-review-2026-06-15.md` records
  parent intake of `dev-frame-opencode` A14 local/offline Zotero report
  closed-shape schema hardening at `739082b...`.
- `parent-pin-review-a14-2026-06-15.md` records the parent decision to pin
  `dev-frame-opencode` to `739082b...` while preserving the no-real-runtime and
  no-final-acceptance boundary.
- `real-resource-positive-pilot-authorization-checklist-2026-06-15.md`
  records the required human RuntimeAuthorization packet and single-track
  selection gate before any real positive pilot.
- `positive-pilot-authorization-packet-validator-2026-06-15.md` records the
  local validator, wrapper schema, and synthetic fixtures for
  RuntimeAuthorization/TestRunSpec positive-pilot authorization packets.
- `opencode-zotero-summary-sample-closed-shape-return-review-2026-06-15.md`
  records parent intake of `dev-frame-opencode` A15 local/offline Zotero
  summary sample closed-shape schema hardening at `128cbf8...`.
- `parent-pin-review-a15-2026-06-15.md` records the parent decision to pin
  `dev-frame-opencode` to `128cbf8...` while preserving the no-real-runtime and
  no-final-acceptance boundary.
- `opencode-zotero-authorization-result-closed-shape-return-review-2026-06-15.md`
  records parent intake of `dev-frame-opencode` A16 local/offline Zotero
  authorization result closed-shape schema hardening at `d19d9ac...`.
- `parent-pin-review-a16-2026-06-15.md` records the parent decision to pin
  `dev-frame-opencode` to `d19d9ac...` while preserving the no-real-runtime and
  no-final-acceptance boundary.
- `opencode-human-runtime-authorization-decision-closed-shape-return-review-2026-06-15.md`
  records parent intake of `dev-frame-opencode` A17 local/offline human
  RuntimeAuthorization decision closed-shape schema hardening at `f8de961...`.
- `parent-pin-review-a17-2026-06-15.md` records the parent decision to pin
  `dev-frame-opencode` to `f8de961...` while preserving the no-real-runtime and
  no-final-acceptance boundary.
- `opencode-agent-acceptance-rules-closed-shape-return-review-2026-06-15.md`
  records parent intake of `dev-frame-opencode` A18 local/offline
  `agent_acceptance_rules` closed-shape schema hardening at `8ae6cb7...`.
- `parent-pin-review-a18-2026-06-15.md` records the parent decision to pin
  `dev-frame-opencode` to `8ae6cb7...` while preserving the no-real-runtime and
  no-final-acceptance boundary.
- `opencode-preauth-authorization-template-closed-shape-return-review-2026-06-15.md`
  records parent intake of `dev-frame-opencode` A19 local/offline preauth
  authorization template closed-shape schema hardening at `86262b4...`.
- `parent-pin-review-a19-2026-06-15.md` records the parent decision to pin
  `dev-frame-opencode` to `86262b4...` while preserving the no-real-runtime and
  no-final-acceptance boundary.
- `opencode-preauth-reviewer-verdict-template-closed-shape-return-review-2026-06-15.md`
  records parent intake of `dev-frame-opencode` A20 local/offline preauth
  reviewer verdict template closed-shape schema hardening at `3f6d64a...`.
- `parent-pin-review-a20-2026-06-15.md` records the parent decision to pin
  `dev-frame-opencode` to `3f6d64a...` while preserving the no-real-runtime and
  no-final-acceptance boundary.
- `opencode-preauth-pilot-scenario-matrix-closed-shape-return-review-2026-06-15.md`
  records parent intake of `dev-frame-opencode` A21 local/offline preauth pilot
  scenario matrix closed-shape schema hardening at `a1ed82b...`.
- `parent-pin-review-a21-2026-06-15.md` records the parent decision to pin
  `dev-frame-opencode` to `a1ed82b...` while preserving the no-real-runtime and
  no-final-acceptance boundary.
- `contract-alignment-matrix-v1-2026-06-15.md` records S06 contract alignment:
  producers, consumers, required fields, invalid cases, schema coverage, and
  non-equivalence rules.
- `contract-schema-gaps-v1-2026-06-15.md` records missing or partial parent
  schemas and the recommended schema creation order.
- `contract-schema-creation-v1-2026-06-15.md` records the created parent draft
  schemas for runtime authorization, test specs/reports, failures, audit
  events, and final verdicts.
- `phase-negative-matrix-v1-2026-06-15.md` records S07 parent negative cases
  for candidate overclaim, dry-run/live confusion, pin drift, ZIP overreach,
  missing authorization, and final verdict provenance.
- `parent-canary-fixture-plan-v1-2026-06-15.md` records synthetic canary
  fixture needs for NEG-PARENT-001 through NEG-PARENT-016.
- `parent-canary-fixtures-a1-2026-06-15.md` records the created synthetic
  parent canary fixtures under `integration/fixtures/parent-canary/`.
- `parent-canary-validation-a1-2026-06-15.md` records read-only validation of
  the parent canary fixtures: 16/16 present, unique, synthetic, and
  `runtime_allowed=false`.
- `parent-canary-dispatch-a1-2026-06-15.md` records dispatch of parent canary
  consumption TaskSpecs to `agent-acceptance` and `test-frame`.
- `parent-canary-dispatch-status-2026-06-15.md` records the current dispatch
  monitoring status: `agent-acceptance` and `test-frame` are in progress, no
  final parent canary returns have been observed, and parent pin readiness
  remains no-go.
- `parent-canary-return-intake-checklist-2026-06-15.md` records the checklist
  the parent should use when `agent-acceptance` and `test-frame` return parent
  canary reports.
- `parent-canary-agent-acceptance-return-review-2026-06-15.md` records parent
  intake review of `agent-acceptance` return
  `PARENT_CANARY_GATE_GAP_FIXED` at `b9bb53a...`.
- `parent-canary-test-frame-return-review-2026-06-15.md` records parent intake
  review of `test-frame` return `PARENT_CANARY_REPORT_GAP_FIXED` at
  `eed8d88...`.
- `parent-canary-combined-intake-review-2026-06-15.md` records combined parent
  intake: both parent canary returns accepted for intake, pin still no-go.
- `ci-canary-risk-work-plan-v1-2026-06-15.md` records S08 read-only CI,
  canary, risk, parallel/serial execution, and phase-condition planning.
- `phase-0.5-state-review-v1-2026-06-15.md` records S02 parent Phase 0.5
  state: bootstrap assets present, current baseline not clean-final, CI runner
  proof unknown, and pin/runtime still no-go.

Current policy:

- Do not store live runtime reports here until a TaskSpec authorizes the run.
- Do not store final acceptance here unless the report includes independent
  reviewer evidence and governance approval.
- Historical reports must state their source path, command, timestamp, and
  whether external runtime was executed.
