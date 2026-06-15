# Parent Pin Review: test-frame Zotero Metadata Manifest Consumption

Date: 2026-06-16
Parent repo: `D:\devframe-system`
Decision: `ACCEPTED_AND_PARENT_PINNED`

## Pin Update

Previous parent gitlink:

`test-frame = fc22a3ba891b342e24d384888b2b707d66f3c81a`

New parent gitlink:

`test-frame = d62356481e24c3c0118fa5b7f705fe576b307fb1`

Other intended module pins remain:

- `agent-acceptance = 6b9a83c1dca0ea650dbc7e97f13977ac02e3e3ee`
- `dev-frame-opencode = bd1bbb5920dfd714ff053a10d8657f95d4449bfe`
- `devframe-control-plane = 09167bc656f8625c97bfae5c52dae5a0280b116c`

Updated files:

- `BASELINE_LOCK.json`
- `integration/lock/submodules.lock.yml`
- `integration/reports/test-frame-zotero-metadata-manifest-consumption-return-review-2026-06-16.md`
- `integration/reports/parent-pin-review-test-frame-zotero-metadata-manifest-consumption-2026-06-16.md`
- `test-frame` gitlink

Note: existing parent governance report/index edits were left unstaged for
their owning thread. This pin commit only covers the test-frame standalone
manifest consumption intake.

## Boundary

This pin records synthetic/offline standalone EvidenceManifest consumption
verification for Zotero Web API metadata-only evidence.

It does not authorize:

- reading Zotero API keys;
- calling Zotero Web API;
- reading Zotero notes, attachments, PDFs, or full text;
- Obsidian, RAG, WriteLab, browser/CDP, cloud, or MiniApp;
- final governance acceptance.
