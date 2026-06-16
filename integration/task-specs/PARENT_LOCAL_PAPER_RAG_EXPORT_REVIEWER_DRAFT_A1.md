# PARENT_LOCAL_PAPER_RAG_EXPORT_REVIEWER_DRAFT_A1

## Status

`DISPATCHED_PARENT_ARTIFACT_EXPORT`

## Goal

Export the reviewer-ready local paper RAG draft into a standalone Markdown
artifact outside the integration report stream.

## Inputs

- Reviewer-ready draft report:
  `integration/reports/parent-local-paper-rag-reviewer-ready-draft-a1-2026-06-16.md`

## Allowed Scope

- Parent documentation/artifact only.
- Create a standalone Markdown draft artifact under
  `integration/artifacts/paper-drafts/`.
- Include citation placeholders, source table, claim matrix, and human review
  checklist.

## Forbidden Scope

- Do not read Zotero keys or call Zotero APIs.
- Do not read original PDFs directly.
- Do not call WriteLab, cloud LLMs, browser/CDP, MiniApp, external RAG, or
  private runtime services.
- Do not update submodule pins, lock files, or runtime registry.
- Do not claim final governance acceptance, paper-quality acceptance,
  production readiness, broad/general RAG readiness, whole-vault readiness, or
  RuntimeAuthorization.

## Expected Deliverables

- `integration/artifacts/paper-drafts/local-paper-rag-reviewer-draft-v0.1.md`
- `integration/reports/parent-local-paper-rag-export-reviewer-draft-a1-2026-06-16.md`

## Verification

- Run `git diff --check` against the new TaskSpec/report/artifact.
- Confirm the standalone artifact has all five sections, `[S1]` through `[S6]`,
  and non-final boundaries.

