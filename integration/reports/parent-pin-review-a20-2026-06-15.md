# Parent Pin Review A20

Date: 2026-06-15

## Status

`A20_OPENCODE_PREAUTH_REVIEWER_VERDICT_TEMPLATE_CLOSED_SHAPE_PIN_REVIEW_PASS`

Parent pin review accepts the latest `dev-frame-opencode` local/offline preauth
reviewer verdict template closed-shape schema slice for parent pin.

## Candidate Pins

- `agent-acceptance`:
  `75f8eb329778d4a8cffb28f6ba79b137038d4fed`
- `dev-frame-opencode`:
  `3f6d64a534a29ffe256346b8758cdb87fd864b02`
- `devframe-control-plane`:
  `79399541b8426cff0f362b665bad09e3c23e974b`
- `test-frame`:
  `c3353fb34900aa24f56df5b9c9230f3249d6c01a`

## Decision

Pin `dev-frame-opencode` from
`86262b49abcf05cb3507aad575fe521c70d8cd51` to
`3f6d64a534a29ffe256346b8758cdb87fd864b02`.

Keep the other module pins unchanged from the current parent baseline.

## Evidence Inputs

- A20 return review:
  `integration/reports/opencode-preauth-reviewer-verdict-template-closed-shape-return-review-2026-06-15.md`
- Evidence ZIP:
  `D:\devframe-system\.agent\evidence\evidence-opencode-preauth-reviewer-verdict-template-closed-shape-a1-3f6d64a.zip`
- Evidence ZIP SHA256:
  `FF62578464EA88AFB21DA240B1372C69B2ED6925C0CCD0174D2FFA63F60987BD`
- Direct parent verification:
  - preauth packet pytest: 8 passed
  - adjacent real-pilot local/offline pytest group: 74 passed
  - preauth packet schema parse: PASS
  - diff check: PASS

## Boundary

This pin records a local/offline contract hardening step only.

It does not authorize or claim:

- real Zotero, Obsidian, RAG, WriteLab, MiniApp, browser/CDP, cloud, H5,
  MeterSphere, Android, PDF, attachment, full text, or private paper runtime
  execution;
- approved real-resource pilot verdict;
- production/live readiness;
- final acceptance.

## Reviewer Index

- Changed parent files:
  - `D:\devframe-system\BASELINE_LOCK.json`
  - `D:\devframe-system\integration\lock\submodules.lock.yml`
  - `D:\devframe-system\integration\reports\opencode-preauth-reviewer-verdict-template-closed-shape-return-review-2026-06-15.md`
  - `D:\devframe-system\integration\reports\parent-pin-review-a20-2026-06-15.md`
  - `D:\devframe-system\integration\reports\README.md`
  - `D:\devframe-system\integration\PROJECT_COMPLETENESS_PLAN.md`
  - `D:\devframe-system\dev-frame-opencode` gitlink
- Required parent checks:
  - `git diff --cached --check`
  - `python -m json.tool BASELINE_LOCK.json`
  - lock text contains all four candidate commits
  - `git submodule status --recursive`
- Known gaps:
  - No real runtime executed.
  - No independent live pilot review.
  - No push performed by this review.
