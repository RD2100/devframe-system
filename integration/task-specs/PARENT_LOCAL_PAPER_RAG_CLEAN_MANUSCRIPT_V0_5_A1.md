# PARENT_LOCAL_PAPER_RAG_CLEAN_MANUSCRIPT_V0_5_A1

## Status

`DISPATCHED_PARENT_CLEAN_MANUSCRIPT_V0_5`

## Goal

Create a clean manuscript candidate from v0.4 by removing internal governance
review scaffolding while preserving the paper body and references.

## Inputs

- v0.4 reviewer draft:
  `integration/artifacts/paper-drafts/local-paper-rag-reviewer-draft-v0.4.md`
- v0.4 revision report:
  `integration/reports/parent-local-paper-rag-v0-4-revision-a1-2026-06-16.md`

## Allowed Scope

- Parent paper artifacts only.
- Create clean Markdown and DOCX manuscript candidate artifacts.
- Verify that internal governance sections are removed from the clean
  manuscript.

## Forbidden Scope

- Do not invoke live runtime, Zotero, WriteLab, Obsidian, RAG, browser/CDP,
  MiniApp, cloud services, external bibliography services, or private runtime
  services.
- Do not update submodule pins, lock files, or runtime registry.
- Do not claim final paper-quality acceptance, final governance acceptance,
  production readiness, broad/general RAG readiness, or RuntimeAuthorization.

## Expected Deliverables

- `integration/artifacts/paper-drafts/local-paper-rag-clean-manuscript-v0.5.md`
- `integration/artifacts/paper-drafts/local-paper-rag-clean-manuscript-v0.5.docx`
- `integration/reports/parent-local-paper-rag-clean-manuscript-v0-5-a1-2026-06-16.md`

## Verification

- Confirm clean Markdown has no `Status:` block.
- Confirm clean Markdown has no `Source-Claim Matrix`.
- Confirm clean Markdown has no `人工审阅清单`.
- Confirm clean DOCX OpenXML is readable and contains references/DOI signals.
- Run `git diff --check`.
