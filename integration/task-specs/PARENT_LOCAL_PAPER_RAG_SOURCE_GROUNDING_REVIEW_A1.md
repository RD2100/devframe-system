# PARENT_LOCAL_PAPER_RAG_SOURCE_GROUNDING_REVIEW_A1

## Status

`DISPATCHED_PARENT_LOCAL_REVIEW`

## Goal

Review the current local paper RAG bounded outline against the explicitly
authorized Obsidian Markdown corpus and decide whether each of the five draft
sections is grounded enough to proceed to section drafting.

## Inputs

- Parent bounded outline:
  `integration/reports/parent-local-paper-rag-bounded-expanded-outline-a1-2026-06-16.md`
- Parent source-grounded draft packet:
  `integration/reports/parent-local-paper-rag-source-grounded-draft-packet-a1-2026-06-16.md`
- Authorized Obsidian corpus root:
  `D:\Obsidian\paper-pilot\papers\virtual-training`
- Source files in scope:
  - `00-virtual-training-paper-index.md`
  - `01-*.md`
  - `02-*.md`
  - `03-*.md`
  - `04-*.md`
  - `05-*.md`
  - `06-*.md`

## Allowed Scope

- Parent repo documentation/report only.
- Read the authorized Markdown files listed above.
- Use short paraphrases and file/line references.
- Record support strength, claim limits, and next drafting decisions.

## Forbidden Scope

- Do not read Zotero keys or call Zotero APIs.
- Do not read original PDFs directly.
- Do not call WriteLab, cloud LLMs, browser/CDP, MiniApp, or external RAG.
- Do not inspect FAISS binaries, vectors, raw chunks, or private runtime stores.
- Do not update submodule pins, lock files, or parent runtime registry.
- Do not claim final governance acceptance, paper-quality acceptance,
  production readiness, broad/general RAG readiness, whole-vault readiness, or
  RuntimeAuthorization.

## Expected Deliverable

- `integration/reports/parent-local-paper-rag-source-grounding-review-a1-2026-06-16.md`

The report should answer:

- Which source files support each of the five draft sections?
- Which claims can be used as cautious draft claims?
- Which claims must stay limited or be removed?
- Whether the next step should be section drafting, retrieval refinement, or
  human paper-quality review.

## Verification

- Run `git diff --check` against the new TaskSpec/report.
- Check that the report preserves non-final boundaries.
- Check that no long source excerpts, secrets, raw PDF text, vectors, or runtime
  payloads are introduced.

