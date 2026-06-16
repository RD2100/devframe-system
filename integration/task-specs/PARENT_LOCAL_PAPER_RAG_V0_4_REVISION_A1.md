# PARENT_LOCAL_PAPER_RAG_V0_4_REVISION_A1

## Status

`DISPATCHED_PARENT_V0_4_PAPER_REVISION`

## Goal

Use the v0.3 review packet to produce a targeted v0.4 paper revision that is
more suitable for human review.

## Inputs

- v0.3 Markdown draft:
  `integration/artifacts/paper-drafts/local-paper-rag-reviewer-draft-v0.3.md`
- v0.3 review prompt:
  `integration/artifacts/paper-drafts/local-paper-rag-v0.3-review-prompt.md`
- v0.3 reference closeout report:
  `integration/reports/parent-current-local-paper-rag-reference-v0-3-closeout-2026-06-16.md`

## Allowed Scope

- Parent paper draft artifacts only.
- Create review findings, v0.4 Markdown, v0.4 DOCX, and a parent report.
- Preserve source IDs `[S1]` through `[S6]`.
- Preserve non-final boundaries.

## Forbidden Scope

- Do not call Zotero APIs or read Zotero keys.
- Do not call external bibliography services.
- Do not call WriteLab, cloud LLMs, browser/CDP, MiniApp, external RAG, or
  private runtime services.
- Do not update submodule pins, lock files, or runtime registry.
- Do not claim paper-quality acceptance, final governance acceptance,
  production readiness, broad/general RAG readiness, or RuntimeAuthorization.

## Expected Deliverables

- `integration/artifacts/paper-drafts/local-paper-rag-v0.3-review-findings.md`
- `integration/artifacts/paper-drafts/local-paper-rag-reviewer-draft-v0.4.md`
- `integration/artifacts/paper-drafts/local-paper-rag-reviewer-draft-v0.4.docx`
- `integration/reports/parent-local-paper-rag-v0-4-revision-a1-2026-06-16.md`

## Verification

- Confirm v0.4 Markdown and DOCX include `reviewer draft v0.4`.
- Confirm v0.4 includes the technical-core section and evaluation-boundary
  section.
- Confirm references `[S1]` through `[S6]` remain present.
- Confirm DOCX OpenXML is readable.
- Run `git diff --check`.
