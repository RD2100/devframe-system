# PARENT_LOCAL_PAPER_RAG_REFERENCE_CLEANUP_A1

## Status

`DISPATCHED_PARENT_REFERENCE_CLEANUP`

## Goal

Upgrade the local paper RAG reviewer draft from raw citation placeholders to a
human-reviewable reference draft.

## Inputs

- Standalone draft v0.1:
  `integration/artifacts/paper-drafts/local-paper-rag-reviewer-draft-v0.1.md`
- Authorized PDF folder:
  `E:\厂里\虚拟训练`
- Authorized Markdown folder:
  `D:\Obsidian\paper-pilot\papers\virtual-training`

## Allowed Scope

- Parent documentation/artifact only.
- Read local PDF first-page metadata/text from the already authorized local
  folder.
- Create a v0.2 draft artifact with a reference section and confidence notes.

## Forbidden Scope

- Do not call Zotero APIs or read Zotero keys.
- Do not use external bibliography services.
- Do not call WriteLab, cloud LLMs, browser/CDP, MiniApp, external RAG, or
  private runtime services.
- Do not update submodule pins, lock files, or runtime registry.
- Do not claim that citation metadata is final.

## Expected Deliverables

- `integration/artifacts/paper-drafts/local-paper-rag-reviewer-draft-v0.2.md`
- `integration/reports/parent-local-paper-rag-reference-cleanup-a1-2026-06-16.md`

## Verification

- Confirm `[S1]` through `[S6]` still appear.
- Confirm a `参考文献草案` section exists.
- Confirm low-confidence citation fields are marked for human review.
- Run `git diff --check`.

