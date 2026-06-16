# PARENT_LOCAL_PAPER_RAG_REFERENCE_V0_3_A1

## Status

`DISPATCHED_PARENT_REFERENCE_V0_3_AND_DOCX`

## Goal

Upgrade the local paper RAG reviewer draft from v0.2 citation placeholders to a
near-final human-review reference draft, and export the same v0.3 draft to DOCX.

## Inputs

- v0.2 Markdown draft:
  `integration/artifacts/paper-drafts/local-paper-rag-reviewer-draft-v0.2.md`
- Authorized PDF folder:
  `E:\厂里\虚拟训练`
- Local PDF first/last-page metadata extracted with PyMuPDF.

## Allowed Scope

- Parent documentation/artifact only.
- Read local authorized PDFs for bibliographic signals only.
- Create Markdown and DOCX reviewer artifacts.
- Record verification and non-final boundary in a parent report.

## Forbidden Scope

- Do not call Zotero APIs or read Zotero keys.
- Do not call external bibliography services.
- Do not call WriteLab, cloud LLMs, browser/CDP, MiniApp, external RAG, or
  private runtime services.
- Do not update submodule pins, lock files, or runtime registry.
- Do not claim final citation acceptance, paper-quality acceptance, production
  readiness, or RuntimeAuthorization.

## Expected Deliverables

- `integration/artifacts/paper-drafts/local-paper-rag-reviewer-draft-v0.3.md`
- `integration/artifacts/paper-drafts/local-paper-rag-reviewer-draft-v0.3.docx`
- `integration/reports/parent-local-paper-rag-reference-v0-3-a1-2026-06-16.md`

## Verification

- Confirm `[S1]` through `[S6]` still appear.
- Confirm v0.3 includes page ranges and DOI signals observed from local PDFs
  where available.
- Confirm DOCX OpenXML is readable and contains the upgraded references.
- Run `git diff --check`.
