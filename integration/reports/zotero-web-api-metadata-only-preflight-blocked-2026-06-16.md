# Zotero Web API Metadata-Only Preflight Blocked

Date: 2026-06-16
Parent repo: `D:\devframe-system`
Task: `ZOTERO_WEB_API_METADATA_ONLY_PREFLIGHT_A1`
Status: `BLOCKED_EMPTY_REMOTE_LIBRARY`

## Decision

The Zotero Web API credential file was readable and the API call authenticated,
but the remote personal Zotero library returned zero items.

This is not a usable metadata-only pilot result. It is a blocked preflight.

## Authorization

User authorized:

- reading `C:\Users\RD\key\zotero.txt`;
- using the contained Zotero user id and API key locally;
- accessing Zotero Web API for a personal library;
- reading the whole library metadata.

Boundary:

- no API key printed in parent report;
- no API key committed;
- no raw Zotero item JSON persisted;
- no titles, abstracts, notes, PDF content, attachments, or full text persisted;
- no Obsidian, RAG, WriteLab, browser/CDP, cloud workflow, or MiniApp used.

## Verification

Commands/probes run:

- key file existence and non-empty-line count probe;
- Zotero Web API item type catalog probe;
- Zotero Web API metadata-only item query with `note` and `attachment`
  excluded by item type filter;
- Zotero Web API `format=versions` count probe for all items;
- Zotero Web API `format=versions` count probe for top items.

Observed:

- API host: `api.zotero.org`
- library type: personal user library
- authentication: succeeded
- all items `Total-Results`: `0`
- top items `Total-Results`: `0`
- metadata records fetched: `0`
- forbidden item types returned: none
- notes read: false
- attachments read: false
- PDF read: false
- full text read: false
- final acceptance claimed: false

Generated local evidence summary:

`D:\devframe-system\.agent\evidence\zotero-web-api-metadata-only-preflight-a1\ZOTERO_WEB_API_METADATA_ONLY_PREFLIGHT_SUMMARY.json`

The summary status was corrected to `BLOCKED_EMPTY_REMOTE_LIBRARY` so that a
zero-item API response cannot be mistaken for a successful real metadata pilot.

## Likely Cause

The local Zotero desktop library has entries, but the Zotero Web API account
currently sees an empty cloud library.

Most likely causes:

- Zotero desktop sync is not enabled;
- Zotero desktop is logged into a different account than the provided API key;
- items are local-only and have not synced to zotero.org yet;
- the API key belongs to another Zotero user id/account.

## Required Human Action

Before rerun:

1. Open Zotero desktop.
2. Go to `编辑` -> `设置` -> `同步`.
3. Log into the same Zotero account that owns the API key.
4. Enable data sync for the library.
5. Click sync and wait until it finishes.
6. Open zotero.org in a browser and confirm the library contains the expected
   items online.
7. Keep file/attachment syncing disabled if you do not want PDF/attachment
   cloud sync.

After that, rerun only the Zotero Web API metadata-only preflight.

## Boundary

This blocked result does not authorize:

- Zotero app local database access;
- Zotero attachments, PDF, full text, or notes;
- Obsidian vault access;
- RAG or vector store execution;
- WriteLab calls;
- browser/CDP/cloud workflows;
- final governance acceptance.
