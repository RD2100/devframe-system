# Parent Pin Review: test-frame Zotero Web API Metadata-Only Verification

Date: 2026-06-16
Parent repo: `D:\devframe-system`
Decision: `ACCEPTED_AND_PARENT_PINNED`

## Pin Update

Previous parent gitlink:

`test-frame = a30758a3b309dd5f0e33e57cce5a15a90b725c82`

New parent gitlink:

`test-frame = b1925fc39d5393402fee0fcc664edbc83eaf3a27`

Other intended module pins:

- `agent-acceptance = 6b9a83c1dca0ea650dbc7e97f13977ac02e3e3ee`
- `dev-frame-opencode = bd31f7feb4353412d2ac70cf614f4db3b70c3770`
- `devframe-control-plane = 09167bc656f8625c97bfae5c52dae5a0280b116c`

Note: `dev-frame-opencode` had separate unpinned local drift at parent review
time and was not staged for this pin. This report only pins `test-frame`.

Updated files:

- `BASELINE_LOCK.json`
- `integration/lock/submodules.lock.yml`
- `integration/reports/README.md`
- `integration/PROJECT_COMPLETENESS_PLAN.md`
- `integration/reports/test-frame-zotero-web-api-metadata-only-verification-return-review-2026-06-16.md`
- `integration/reports/parent-pin-review-test-frame-zotero-web-api-metadata-only-verification-2026-06-16.md`
- `test-frame` gitlink

## Boundary

This pin records synthetic/offline verification contracts for Zotero Web API
metadata-only evidence.

It does not authorize:

- reading Zotero API keys;
- calling Zotero Web API;
- reading Zotero notes, attachments, PDFs, or full text;
- Obsidian, RAG, WriteLab, browser/CDP, cloud, or MiniApp;
- final governance acceptance.
