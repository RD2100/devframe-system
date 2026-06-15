# Zotero Web API Metadata-Only Preflight Pass

Date: 2026-06-16
Parent repo: `D:\devframe-system`
Task: `ZOTERO_WEB_API_METADATA_ONLY_PREFLIGHT_A2`
Status: `PASS_METADATA_ONLY`

## Decision

The authorized Zotero Web API metadata-only preflight passed after the user
enabled/finished Zotero sync.

This proves the parent can reach the user's personal Zotero cloud library and
read metadata-only records while excluding `note` and `attachment` item types.

This is not final acceptance and does not authorize Zotero attachments, PDF,
full text, private notes, Obsidian, RAG, WriteLab, browser/CDP, cloud, MiniApp,
or production/live citation verification.

## Authorization

User authorized:

- reading `C:\Users\RD\key\zotero.txt`;
- using the contained Zotero user id and API key locally;
- accessing Zotero Web API for the personal library;
- reading the whole library metadata.

Boundary preserved:

- API key was not printed in chat output;
- API key was not written to parent reports;
- API key was not staged or committed;
- raw Zotero item JSON was not persisted;
- raw titles were not persisted;
- raw abstracts were not persisted;
- notes were not read;
- attachments were not read;
- PDFs and full text were not read.

## Result

Observed API host:

`api.zotero.org`

Summary:

| Check | Result |
|---|---:|
| all-items count probe | 25 |
| top-items count probe | 23 |
| metadata records read after excluding note/attachment item types | 23 |
| metadata API calls | 1 |
| returned forbidden item types | 0 |
| item types read | `journalArticle=23` |
| notes read | false |
| attachments read | false |
| PDF read | false |
| full text read | false |
| final acceptance claimed | false |

Generated local evidence summary:

`D:\devframe-system\.agent\evidence\zotero-web-api-metadata-only-preflight-a2\ZOTERO_WEB_API_METADATA_ONLY_PREFLIGHT_SUMMARY.json`

The summary contains only counts, booleans, field presence counts, version
ranges, and fingerprints. It does not contain raw item payloads, raw titles,
raw abstracts, the API key, or the raw user id.

## Verification

Commands/probes run:

- key file parse probe without printing secrets;
- Zotero Web API all-items `format=versions` count probe;
- Zotero Web API top-items `format=versions` count probe;
- Zotero Web API metadata query with `note` and `attachment` excluded through
  item type filtering;
- `python -m json.tool` over the generated summary;
- Python safety assertion over the generated summary.

Safety assertion result:

- `status=PASS_METADATA_ONLY`
- `records_seen=23`
- `returned_forbidden_item_type_counts={}`
- `notes_read=false`
- `attachments_read=false`
- `pdf_read=false`
- `full_text_read=false`
- `raw_items_persisted=false`
- `raw_titles_persisted=false`
- `raw_abstracts_persisted=false`
- `final_acceptance_claimed=false`
- `live_ready_claimed=false`

## Known Gaps

- This is a parent-side preflight script, not yet integrated into
  `dev-frame-opencode` as a reusable product command.
- No evidence ZIP was produced for this parent-side preflight.
- This does not validate downstream citation lookup, Obsidian import, RAG
  indexing, or WriteLab output.
- This does not read or validate Zotero notes, attachments, PDFs, or full text.
- Zotero API credentials still need a formal RuntimeAuthorization/EvidenceManifest
  path before this becomes a repeatable product workflow.

## Next Safe Step

Recommended next task:

`OPENCODE_ZOTERO_WEB_API_METADATA_ONLY_ADAPTER_A1`

Goal:

- implement a local/offline-safe Zotero Web API metadata-only adapter in
  `dev-frame-opencode`;
- keep notes/attachments/PDF/full-text blocked;
- persist only minimized evidence: counts, fingerprints, item type counts,
  field presence counts, and redaction counts;
- add regression coverage for empty remote library, forbidden item type return,
  secret redaction, and no raw title/abstract persistence.

## Boundary

Accepted scope:

- Zotero Web API metadata-only preflight;
- personal library only;
- `journalArticle` metadata count and minimized evidence only.

Rejected promotions:

- not Zotero PDF/full-text readiness;
- not Obsidian/RAG/WriteLab/browser/cloud readiness;
- not final governance acceptance;
- not a full production integration.
