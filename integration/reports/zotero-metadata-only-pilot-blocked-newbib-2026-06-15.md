# Zotero Metadata-Only Pilot Blocked: Second BibTeX Export

Date: 2026-06-15
Reviewer: parent devframe-system coordinator
Scope: metadata-only pilot from user-provided export file

## Verdict

Status: `BLOCKED_EXPECTED_FAIL_CLOSED`

The latest user-provided BibTeX export was rejected before the metadata pilot
could pass. This is the correct result because the export still contains
forbidden fields.

## Input

- Export file:
  `D:\devframe-system\.agent\manual-input\导出的条目2.bib`
- Evidence directory:
  `D:\devframe-system\.agent\evidence\zotero-metadata-only-pilot-20260615-newbib-20260615-2034`
- Authorization decision:
  `D:\devframe-system\.agent\evidence\zotero-metadata-only-pilot-20260615-newbib-20260615-2034\human-runtime-authorization-decision.json`
- Pilot report:
  `D:\devframe-system\.agent\evidence\zotero-metadata-only-pilot-20260615-newbib-20260615-2034\zotero-metadata-only-pilot-report.json`

## Commands Run

From `D:\devframe-system\dev-frame-opencode\ai-workflow-hub` with
`PYTHONPATH=src`:

- `python -m ai_workflow_hub.cli paper real-pilot-authorize-metadata --authorized-by user_chat_authorization --output <evidence>\human-runtime-authorization-decision.json`
- `python -m ai_workflow_hub.cli paper real-zotero-metadata-pilot --authorization-decision <evidence>\human-runtime-authorization-decision.json --source-mode export_file --export-path <manual-input>\导出的条目2.bib --output <evidence>\zotero-metadata-only-pilot-report.json`
- `python -m json.tool <evidence>\zotero-metadata-only-pilot-report.json`

## Result

The generated pilot report returned:

- `pilot_status`: `BLOCKED`
- `source_available`: `false`
- `human_required`: `true`
- `reasons`: `forbidden_metadata_export_fields_present`
- `forbidden_fields`: `abstract`, `file`, `note`

Pre-scan counts on the export file also found:

- `abstract =`: 23 occurrences
- `file =`: 2 occurrences
- `note =`: 23 occurrences

## Boundary

No Zotero application, Obsidian vault, RAG/vector store, WriteLab, MiniApp,
browser/CDP, cloud, PDF, attachment, full text, or private paper runtime was
started.

The only input read was the user-provided BibTeX export file. No raw paper
titles, abstracts, file paths, notes, or private content are reproduced in this
report.

## Required User Action

Export BibTeX again with metadata only:

- do not export notes;
- do not export files or attachments;
- do not include abstracts;
- do not include PDFs, annotations, full text, or file paths.

The next acceptable file should have zero matches for `abstract =`, `file =`,
and `note =`.
