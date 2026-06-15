# dev-frame-opencode Zotero Web API Metadata-Only Adapter Parent Intake

Date: 2026-06-16
Parent repo: `D:\devframe-system`
Submodule: `dev-frame-opencode`
TaskSpec: `OPENCODE_ZOTERO_WEB_API_METADATA_ONLY_ADAPTER_A1`
Status: `READY_FOR_PARENT_INTAKE`

## Decision

Parent intake accepts `dev-frame-opencode` commit
`bd31f7feb4353412d2ac70cf614f4db3b70c3770` as a focused Zotero Web API
metadata-only adapter milestone.

This is not final governance acceptance and does not authorize Zotero notes,
attachments, PDF, full text, Obsidian, RAG, WriteLab, browser/CDP, cloud,
MiniApp, or production/live citation verification.

## Evidence

Evidence ZIP:

`D:\devframe-system\.agent\evidence\evidence-opencode-zotero-web-api-metadata-only-adapter-a1-bd31f7f.zip`

Expected SHA256:

`8799B7DB7D815954269FA01BB0BF15AAF507882494DE1180707E55F068143B47`

Observed SHA256:

`8799B7DB7D815954269FA01BB0BF15AAF507882494DE1180707E55F068143B47`

Evidence directory:

`D:\devframe-system\.agent\evidence\opencode-zotero-web-api-metadata-only-adapter-a1`

## Implementation Summary

Changed files in the submodule commit:

- `ai-workflow-hub/src/ai_workflow_hub/cli.py`
- `ai-workflow-hub/src/ai_workflow_hub/context_layer/adapters/zotero_web_metadata_pilot.py`
- `ai-workflow-hub/tests/test_zotero_web_metadata_pilot.py`
- `schemas/paper_zotero_web_api_metadata_only_pilot_report.schema.json`

Implemented behavior:

- reusable Zotero Web API metadata-only adapter;
- CLI command: `paper zotero-web-metadata-pilot`;
- closed report schema;
- personal-library metadata read from `https://api.zotero.org`;
- key file values read only in memory;
- API key and raw user id are not persisted;
- minimized evidence only: counts, item type counts, field presence counts,
  redaction counts, fingerprints, version range, and booleans;
- raw item JSON, raw titles, raw abstracts, notes, attachments, PDFs, and full
  text are not persisted;
- empty remote library returns non-PASS;
- returned `note` or `attachment` item types fail closed.

## Verification

Parent-side commands run:

- `git -C dev-frame-opencode status --short --branch`
- `git -C dev-frame-opencode rev-parse HEAD`
- `Get-FileHash .agent\evidence\evidence-opencode-zotero-web-api-metadata-only-adapter-a1-bd31f7f.zip -Algorithm SHA256`
- `$env:PYTHONPATH='src'; python -m pytest tests\test_zotero_web_metadata_pilot.py -q`
- `python -m json.tool schemas\paper_zotero_web_api_metadata_only_pilot_report.schema.json`
- `git diff --check HEAD~1 HEAD`

Observed:

- submodule worktree clean at `bd31f7f...`;
- evidence ZIP hash matched;
- focused tests: `7 passed`;
- schema JSON parse: PASS;
- submodule diff check: PASS;
- evidence ExecutionReport states targeted paper suite: `63 passed`;
- evidence live report validation and raw-sensitive scan: PASS.

## Live Smoke Summary

Minimized live smoke fields reported by submodule:

- API host: `api.zotero.org`;
- `pilot_status=PASS_METADATA_ONLY`;
- `metadata_records_read=23`;
- `item_type_counts=journalArticle=23`;
- `redaction_counts`: `abstractNote=23`, `accessDate=23`, `title=23`, `url=23`;
- `raw_items_persisted=false`;
- `raw_titles_persisted=false`;
- `raw_abstracts_persisted=false`;
- `final_acceptance_claimed=false`.

The evidence ZIP excludes raw API responses and credential files.

## Known Gaps

- Pagination beyond the first metadata page is not expanded in this minimal
  slice; the current authorized personal library returns 23 top metadata
  records.
- This is not PDF/attachment/full-text processing.
- This is not Obsidian/RAG/WriteLab/browser/CDP/cloud/MiniApp integration.
- This is not final governance acceptance.

## Reviewer Index

Critical code paths:

- `paper zotero-web-metadata-pilot` CLI command;
- `build_zotero_web_metadata_pilot_report(...)`;
- key-file parser for authorized local Zotero credential file;
- requester restricted to `https://api.zotero.org`;
- note/attachment fail-closed guard;
- minimized evidence manifest generation;
- closed JSON schema validation.

Review focus:

- confirm no API key, raw user id, raw item JSON, raw title, or raw abstract is
  persisted;
- confirm `note` and `attachment` fail closed;
- confirm empty remote library is not promoted to PASS;
- confirm metadata-only result is not promoted to final acceptance.
