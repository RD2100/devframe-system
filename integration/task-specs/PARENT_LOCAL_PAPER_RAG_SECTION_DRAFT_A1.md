# PARENT_LOCAL_PAPER_RAG_SECTION_DRAFT_A1

## Status

`DISPATCHED_PARENT_LOCAL_DRAFT`

## Goal

Produce a bounded, source-grounded Chinese section draft from the source
grounding review.

The draft should be useful as a human-review paper artifact, while preserving
the boundary that it is not final paper-quality acceptance.

## Inputs

- Source grounding review:
  `integration/reports/parent-local-paper-rag-source-grounding-review-a1-2026-06-16.md`
- Bounded outline:
  `integration/reports/parent-local-paper-rag-bounded-expanded-outline-a1-2026-06-16.md`
- Authorized local Markdown corpus:
  `D:\Obsidian\paper-pilot\papers\virtual-training`

## Allowed Scope

- Parent documentation/report only.
- Use the source file and line references already recorded in the source
  grounding review.
- Draft cautious Chinese prose and keep claims traceable.
- Include a reviewer checklist and residual limitations.

## Forbidden Scope

- Do not read Zotero keys or call Zotero APIs.
- Do not read original PDFs directly.
- Do not call WriteLab, cloud LLMs, browser/CDP, MiniApp, or external RAG.
- Do not update submodule pins, lock files, or runtime registry.
- Do not claim final governance acceptance, paper-quality acceptance,
  production readiness, broad/general RAG readiness, whole-vault readiness, or
  RuntimeAuthorization.

## Expected Deliverable

- `integration/reports/parent-local-paper-rag-section-draft-a1-2026-06-16.md`

## Verification

- Run `git diff --check` against the new TaskSpec/report.
- Confirm the draft preserves source references and non-final boundaries.
- Confirm no long source excerpts, secrets, raw PDF text, vectors, or runtime
  payloads are introduced.

