# PARENT_LOCAL_PAPER_RAG_DOCX_EXPORT_A1

## Status

`DISPATCHED_PARENT_DOCX_EXPORT`

## Goal

Export the standalone local paper RAG reviewer draft Markdown artifact to a
DOCX file for human review and annotation.

## Inputs

- Markdown artifact:
  `integration/artifacts/paper-drafts/local-paper-rag-reviewer-draft-v0.1.md`

## Allowed Scope

- Parent artifact/report only.
- Use local tooling only.
- Generate DOCX from the existing Markdown draft.

## Forbidden Scope

- Do not install packages.
- Do not call external services.
- Do not read Zotero keys, original PDFs, raw runtime stores, FAISS binaries, or
  private payloads.
- Do not update submodule pins, lock files, or runtime registry.
- Do not claim paper-quality acceptance or final governance acceptance.

## Expected Deliverables

- `integration/artifacts/paper-drafts/local-paper-rag-reviewer-draft-v0.1.docx`
- `integration/reports/parent-local-paper-rag-docx-export-a1-2026-06-16.md`

## Verification

- Verify DOCX ZIP/OpenXML entry list.
- Verify selected text markers in `word/document.xml`.
- Compute SHA256.
- Run `git diff --check` on the report/TaskSpec and confirm artifact is staged.

