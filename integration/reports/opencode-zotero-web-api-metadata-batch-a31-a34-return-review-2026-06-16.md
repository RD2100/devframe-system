# dev-frame-opencode Zotero Web API Metadata Batch A31-A34 Parent Intake

Date: 2026-06-16
Parent repo: `D:\devframe-system`
Submodule: `dev-frame-opencode`
Status: `READY_FOR_BATCH_PARENT_INTAKE`

## Decision

Parent intake accepts the `dev-frame-opencode` Zotero Web API metadata-only
hardening batch from `bd31f7f...` through
`b097217c9ad3b53d4c28a03a7fb1510d2606bf71`.

This is a metadata-only hardening batch. It is not final governance acceptance,
not PDF/full-text readiness, and not Obsidian/RAG/WriteLab/browser/cloud/MiniApp
readiness.

## Batch Commits

1. `cdb45bbeaa169b3270b89f30b0073d7f1d39b575`
   - `Add Zotero Web metadata pagination evidence`
   - Evidence ZIP:
     `D:\devframe-system\.agent\evidence\evidence-opencode-zotero-web-api-pagination-a1-cdb45bb.zip`
   - SHA256:
     `2BE59E6C0A1D6B3EBB28FC9CB241AAD55333113ADAF7ED9F1744DEA838EA6FF0`

2. `494679aa4d302f1af31d1f49441a61bb4da36feb`
   - `Expose Zotero Web metadata page limit`
   - Evidence ZIP:
     `D:\devframe-system\.agent\evidence\evidence-opencode-zotero-web-api-cli-page-limit-a1-494679a.zip`
   - SHA256:
     `7377D154DF298C2DD5A6B0B3EADDD3DC71A65614E8B30E3E698DF83AADF2DC79`

3. `689071516b5b411e45060656d154c6b8762fa1ec`
   - `Minimize Zotero Web API failure evidence`
   - Evidence ZIP:
     `D:\devframe-system\.agent\evidence\evidence-opencode-zotero-web-api-failure-minimization-a1-6890715.zip`
   - SHA256:
     `45322B548D5C48A02B282BEFEAFDB82F50034598B3B14CEA0E4627CCE35941DF`

4. `b097217c9ad3b53d4c28a03a7fb1510d2606bf71`
   - `Document Zotero Web metadata pilot boundary`
   - Evidence ZIP:
     `D:\devframe-system\.agent\evidence\evidence-opencode-zotero-web-api-doc-boundary-a1-b097217.zip`
   - SHA256:
     `EEA8729B18894DA7CB160C9A0D12EA9DFE3DA84A4257B3541E595E1AB0C970A3`

## Implementation Summary

Changed files across batch:

- `ai-workflow-hub/src/ai_workflow_hub/context_layer/adapters/zotero_web_metadata_pilot.py`
- `ai-workflow-hub/src/ai_workflow_hub/cli.py`
- `ai-workflow-hub/tests/test_zotero_web_metadata_pilot.py`
- `schemas/paper_zotero_web_api_metadata_only_pilot_report.schema.json`
- `ai-workflow-hub/docs/paper/PAPER_REAL_ZOTERO_METADATA_ONLY_PILOT.md`

Batch behavior:

- bounded pagination for top-item metadata reads;
- report/schema fields: `metadata_page_limit`, `metadata_pages_read`,
  `metadata_pagination_complete`;
- over-limit remote libraries fail closed;
- CLI option: `paper zotero-web-metadata-pilot --page-limit`;
- minimized `failure_summary` for HTTP, non-JSON, and network failures;
- remote response bodies and low-level exception messages are not persisted;
- documentation of CLI, schema, pagination, failure summary, and non-final
  boundary.

## Parent Verification

Commands run:

- `git -C dev-frame-opencode status --short --branch`
- `git -C dev-frame-opencode rev-parse HEAD`
- SHA256 verification for all four evidence ZIPs
- `$env:PYTHONPATH='src'; python -m pytest tests\test_zotero_web_metadata_pilot.py -q`
- `python -m json.tool schemas\paper_zotero_web_api_metadata_only_pilot_report.schema.json`
- `git diff --check bd31f7feb4353412d2ac70cf614f4db3b70c3770 b097217c9ad3b53d4c28a03a7fb1510d2606bf71`

Observed:

- submodule worktree clean at `b097217...`;
- all four evidence ZIP hashes matched;
- adapter/CLI tests: `12 passed`;
- schema JSON parse: PASS;
- batch diff check: PASS.

## Live Metadata-Only Smoke Summary

Delegated live smoke summary:

- API host: `api.zotero.org`;
- key file read in memory; values not printed or persisted;
- default page limit: `PASS_METADATA_ONLY`, 23 `journalArticle` metadata
  records, 1 metadata page;
- `--page-limit 10`: `PASS_METADATA_ONLY`, 23 `journalArticle` metadata
  records, 3 metadata pages;
- `notes_read=false`;
- `attachments_read=false`;
- `pdf_read=false`;
- `full_text_read=false`;
- `raw_items_persisted=false`;
- `raw_titles_persisted=false`;
- `raw_abstracts_persisted=false`;
- API key, raw user id, raw item JSON, raw title, and raw abstract were not
  persisted.

## Known Gaps

- Zotero Web API metadata-only, personal library only.
- No notes, attachments, PDF, full text, Obsidian, RAG, WriteLab, browser/CDP,
  cloud, or MiniApp.
- Not production ready and not final acceptance.

## Reviewer Index

Critical review paths:

- `zotero_web_metadata_pilot.py` pagination and failure minimization;
- CLI `--page-limit`;
- closed report schema;
- evidence minimization and redaction checks;
- documentation boundary wording.

Review focus:

- over-limit libraries must fail closed;
- failure summaries must not persist raw response bodies or exception details;
- pagination evidence must not be promoted to final readiness;
- metadata-only must remain separate from notes/attachments/PDF/full text.
