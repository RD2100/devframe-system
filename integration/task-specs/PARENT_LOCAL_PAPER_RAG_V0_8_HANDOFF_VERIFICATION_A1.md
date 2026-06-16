# PARENT_LOCAL_PAPER_RAG_V0_8_HANDOFF_VERIFICATION_A1

## Status

`DISPATCHED_PARENT_LOCAL_PAPER_RAG_V0_8_HANDOFF_VERIFICATION`

## Goal

Add a read-only parent verifier for the current v0.8 local paper RAG handoff.
The verifier should let a reviewer confirm the handoff package without manually
walking every report.

## Inputs

- v0.8 readiness packet:
  `integration/reports/parent-current-local-paper-rag-final-readiness-packet-v0-8-2026-06-16.md`
- v0.8 manuscript artifacts under:
  `integration/artifacts/paper-drafts/`
- `BASELINE_LOCK.json`
- opencode answer-preview evidence ZIP:
  `D:\devframe-system\.agent\evidence\evidence-opencode-local-paper-rag-answer-preview-a1-528f5b8.zip`

## Expected Deliverables

- `scripts/verify_local_paper_rag_v0_8_handoff.py`
- `integration/reports/local-paper-rag-v0-8-handoff-verification/local-paper-rag-v0-8-handoff-verification.json`
- `integration/reports/local-paper-rag-v0-8-handoff-verification/local-paper-rag-v0-8-handoff-verification.md`
- `integration/reports/parent-local-paper-rag-v0-8-handoff-verification-a1-2026-06-16.md`

## Boundary

Read-only parent verification only. Do not invoke live runtime, Zotero,
WriteLab, Obsidian, RAG, browser/CDP, MiniApp, cloud services, external
bibliography services, private runtime services, or submodule pin updates. Do
not inspect raw PDFs, raw Obsidian notes, raw chunks, vectors, FAISS binaries,
WriteLab payloads, Zotero keys, or private runtime artifacts. Do not claim final
paper-quality acceptance, training-effect acceptance, final governance
acceptance, or RuntimeAuthorization.

## Verification

- Run the handoff verifier from `D:\devframe-system`.
- Confirm it exits 0.
- Confirm generated JSON and Markdown reports exist.
- Confirm `git diff --check` passes for current-slice files.
