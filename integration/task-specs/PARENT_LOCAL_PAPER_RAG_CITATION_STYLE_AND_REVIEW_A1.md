# PARENT_LOCAL_PAPER_RAG_CITATION_STYLE_AND_REVIEW_A1

## Status

`DISPATCHED_PARENT_LOCAL_REVIEW_PACKET`

## Goal

Turn the section draft into a reviewer-facing draft packet with citation
placeholders, a source table, and human review gates.

## Inputs

- Section draft:
  `integration/reports/parent-local-paper-rag-section-draft-a1-2026-06-16.md`
- Source grounding review:
  `integration/reports/parent-local-paper-rag-source-grounding-review-a1-2026-06-16.md`
- Authorized local Markdown corpus:
  `D:\Obsidian\paper-pilot\papers\virtual-training`

## Allowed Scope

- Parent documentation/report only.
- Reuse known source file names, source hashes, and source line ranges.
- Add citation placeholders and a reviewer decision table.
- Mark formal citation metadata as requiring human cleanup where conversion text
  is noisy.

## Forbidden Scope

- Do not read Zotero keys or call Zotero APIs.
- Do not read original PDFs directly.
- Do not call WriteLab, cloud LLMs, browser/CDP, MiniApp, external RAG, or
  private runtime services.
- Do not update submodule pins, lock files, or runtime registry.
- Do not claim final governance acceptance, paper-quality acceptance,
  production readiness, broad/general RAG readiness, whole-vault readiness, or
  RuntimeAuthorization.

## Expected Deliverable

- `integration/reports/parent-local-paper-rag-citation-style-and-review-a1-2026-06-16.md`

## Verification

- Run `git diff --check` against the new TaskSpec/report.
- Confirm all five sections have citation placeholders.
- Confirm the report preserves non-final and human-review boundaries.

