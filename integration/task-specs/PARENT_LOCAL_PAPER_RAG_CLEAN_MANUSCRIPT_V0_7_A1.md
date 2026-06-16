# PARENT_LOCAL_PAPER_RAG_CLEAN_MANUSCRIPT_V0_7_A1

## Status

`DISPATCHED_PARENT_CLEAN_MANUSCRIPT_V0_7`

## Goal

Create a reviewer-facing clean manuscript v0.7 by converting internal source
labels from `[S1]` style markers to conventional numeric references `[1]`
through `[6]`, then package it as the current recommended paper artifact.

## Inputs

- v0.6 clean manuscript:
  `integration/artifacts/paper-drafts/local-paper-rag-clean-manuscript-v0.6.md`
- artifact index:
  `integration/artifacts/paper-drafts/README.md`

## Expected Deliverables

- `integration/artifacts/paper-drafts/local-paper-rag-clean-manuscript-v0.7.md`
- `integration/artifacts/paper-drafts/local-paper-rag-clean-manuscript-v0.7.docx`
- `integration/artifacts/paper-drafts/local-paper-rag-clean-manuscript-v0.7-package.zip`
- `integration/reports/parent-local-paper-rag-clean-manuscript-v0-7-a1-2026-06-16.md`

## Boundary

Parent paper artifacts only. Do not invoke live runtime, Zotero, WriteLab,
Obsidian, RAG, browser/CDP, MiniApp, cloud services, external bibliography
services, private runtime services, or submodule pin updates. Do not claim final
paper-quality acceptance, final citation acceptance, or final governance
acceptance.

## Verification

- Confirm v0.7 Markdown/DOCX/package exist.
- Confirm no `[S1]` style internal labels remain.
- Confirm numeric references `[1]` through `[6]` and exactly six bibliography
  entries are present.
- Confirm v0.7 has no internal governance scaffolding.
- Confirm DOI signals are preserved.
- Confirm package ZIP contains only review artifacts.
- Run `git diff --check` on the current-slice files.
