# PARENT_LOCAL_PAPER_RAG_REVIEWER_READY_DRAFT_A1

## Status

`DISPATCHED_PARENT_REVIEWER_READY_DRAFT`

## Goal

Produce a single reviewer-ready Markdown draft packet from the local paper RAG
section draft and citation review packet.

This is the first consolidated paper-facing artifact in the parent repo. It
must remain non-final and require human paper-quality acceptance before any
final claim.

## Inputs

- Section draft:
  `integration/reports/parent-local-paper-rag-section-draft-a1-2026-06-16.md`
- Citation review packet:
  `integration/reports/parent-local-paper-rag-citation-style-and-review-a1-2026-06-16.md`
- Source grounding review:
  `integration/reports/parent-local-paper-rag-source-grounding-review-a1-2026-06-16.md`

## Allowed Scope

- Parent documentation/report only.
- Consolidate existing draft material.
- Include citation placeholders, source-claim matrix, and human review gates.

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

- `integration/reports/parent-local-paper-rag-reviewer-ready-draft-a1-2026-06-16.md`

## Verification

- Run `git diff --check` against the new TaskSpec/report.
- Confirm the single draft includes all five sections and `[S1]` through `[S6]`.
- Confirm the non-final/human-review boundary remains explicit.

