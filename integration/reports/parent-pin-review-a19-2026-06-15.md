# Parent Pin Review A19

Date: 2026-06-15

## Status

`A19_OPENCODE_PREAUTH_AUTHORIZATION_TEMPLATE_CLOSED_SHAPE_PIN_REVIEW_PASS`

Parent pin review accepts the latest `dev-frame-opencode` local/offline preauth
authorization template closed-shape schema slice for parent pin.

## Candidate Pins

- `agent-acceptance`:
  `75f8eb329778d4a8cffb28f6ba79b137038d4fed`
- `dev-frame-opencode`:
  `86262b49abcf05cb3507aad575fe521c70d8cd51`
- `devframe-control-plane`:
  `79399541b8426cff0f362b665bad09e3c23e974b`
- `test-frame`:
  `c3353fb34900aa24f56df5b9c9230f3249d6c01a`

## Decision

Pin `dev-frame-opencode` from
`8ae6cb77ac977a602dd834efd14405a523c0cb5a` to
`86262b49abcf05cb3507aad575fe521c70d8cd51`.

Keep the other module pins unchanged from the current parent baseline.

## Evidence Inputs

- A19 return review:
  `integration/reports/opencode-preauth-authorization-template-closed-shape-return-review-2026-06-15.md`
- Evidence ZIP:
  `D:\devframe-system\.agent\evidence\evidence-opencode-preauth-authorization-template-closed-shape-a1-86262b4.zip`
- Evidence ZIP SHA256:
  `345F97BB7AB6C766E71AEDA04A1813668D59536EEB9EA68153070CA08BBF3351`
- Direct parent verification:
  - preauth packet pytest: 8 passed
  - adjacent real-pilot local/offline pytest group: 67 passed
  - business capability validation: 7 passed
  - preauth packet schema parse: PASS
  - diff check: PASS

## Boundary

This pin records a local/offline contract hardening step only.

It does not authorize or claim:

- real Zotero, Obsidian, RAG, WriteLab, MiniApp, browser/CDP, cloud, H5,
  MeterSphere, Android, PDF, attachment, full text, or private paper runtime
  execution;
- production/live readiness;
- final acceptance.

## Reviewer Index

- Changed parent files:
  - `D:\devframe-system\BASELINE_LOCK.json`
  - `D:\devframe-system\integration\lock\submodules.lock.yml`
  - `D:\devframe-system\integration\reports\opencode-preauth-authorization-template-closed-shape-return-review-2026-06-15.md`
  - `D:\devframe-system\integration\reports\parent-pin-review-a19-2026-06-15.md`
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
