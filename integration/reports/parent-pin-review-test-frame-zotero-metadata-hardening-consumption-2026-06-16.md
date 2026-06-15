# Parent Pin Review: test-frame Zotero Metadata Hardening Consumption

Date: 2026-06-16
Parent repo: `D:\devframe-system`
Decision: `ACCEPTED_AND_PARENT_PINNED`

## Pin Update

Previous parent gitlink:

`test-frame = f8bce53333f9087af06b1842716f73777794be27`

New parent gitlink:

`test-frame = fc22a3ba891b342e24d384888b2b707d66f3c81a`

Other intended module pins remain:

- `agent-acceptance = 6b9a83c1dca0ea650dbc7e97f13977ac02e3e3ee`
- `dev-frame-opencode = b097217c9ad3b53d4c28a03a7fb1510d2606bf71`
- `devframe-control-plane = 09167bc656f8625c97bfae5c52dae5a0280b116c`

Updated files:

- `BASELINE_LOCK.json`
- `integration/lock/submodules.lock.yml`
- `integration/reports/test-frame-zotero-metadata-hardening-consumption-return-review-2026-06-16.md`
- `integration/reports/parent-pin-review-test-frame-zotero-metadata-hardening-consumption-2026-06-16.md`
- `test-frame` gitlink

Note: existing parent governance report/index edits were left unstaged for
their owning thread. This pin commit only covers the test-frame hardening
consumption intake.

## Boundary

This pin records synthetic/offline evidence consumption verification for
opencode Zotero Web API metadata-only hardening evidence.

It does not authorize:

- reading Zotero API keys;
- calling Zotero Web API;
- reading Zotero notes, attachments, PDFs, or full text;
- Obsidian, RAG, WriteLab, browser/CDP, cloud, or MiniApp;
- final governance acceptance.
