# opencode RAG FAISS Obsidian Prep Return Review

Date: 2026-06-16

## Verdict

ACCEPTED_FOR_PARENT_PIN as a scoped FAISS/Obsidian allowlisted-folder prep preflight.

This is not final governance acceptance, paper-quality acceptance, production readiness, broad live readiness, general RAG readiness, whole-vault readiness, or authorization to install dependencies, download models, or build a FAISS index.

## Reviewed Return

- Module: `dev-frame-opencode`
- Branch: `codex/paper-audit-privacy-hard-gate`
- Commit: `0617e3e9831002cfbcc3c8125d85ef6e76e0655a`
- Message: `Add FAISS Obsidian RAG prep preflight`
- Evidence ZIP: `D:\devframe-system\.agent\evidence\evidence-opencode-rag-faiss-obsidian-prep-a1-0617e3e.zip`
- Expected SHA256: `8BAC3BC0D20E48B6C846B32685C85781DE68DB9A7338CEEAA105549973E44DC6`
- Observed SHA256: `8BAC3BC0D20E48B6C846B32685C85781DE68DB9A7338CEEAA105549973E44DC6`

## Scope Accepted

- Adds `paper rag-faiss-obsidian-prep`.
- Adds FAISS/Obsidian allowlisted-folder prep adapter.
- Adds closed schema `schemas/paper_rag_faiss_obsidian_prep_report.schema.json`.
- Adds focused tests `tests\test_paper_rag_faiss_obsidian_prep.py`.
- Reports dependency availability, allowlist scope, planned artifacts, privacy boundaries, runtime boundaries, and install preflight guidance.
- Fails closed when FAISS or sentence-transformers dependencies are missing.

## Preflight Summary

- `faiss_present=false`
- `sentence_transformers_present=false`
- CLI smoke status: `DEPENDENCY_INSTALL_REQUIRED`
- Package install performed: `false`
- Model download performed: `false`
- FAISS index build performed: `false`
- Whole-vault scan performed: `false`

## Parent Verification

- Evidence hash matched expected SHA256.
- Evidence entry list was limited to changed-files, command logs, minimized reports, schema snapshot, `EXECUTION_REPORT.md`, and `REVIEWER_INDEX.md`.
- `python -m pytest tests\test_paper_rag_faiss_obsidian_prep.py -q` -> 5 passed.
- `python -m pytest tests\test_paper_rag_single_note_retrieval_pilot.py tests\test_obsidian_note_adapter.py tests\test_paper_rag_faiss_obsidian_prep.py -q` -> 22 passed.
- `python -m json.tool schemas\paper_rag_faiss_obsidian_prep_report.schema.json` -> PASS.
- `git diff --check d4d8a85a54d17c3d787e2e90903776dcf809150e 0617e3e` -> PASS.

## Privacy Boundary

- Evidence/report contain minimized facts only.
- No raw note body, raw chunks, raw query, raw local paths, API keys, or embedding vectors are accepted as parent evidence.
- The accepted slice did not install packages, download embedding models, build a FAISS index, scan the Obsidian vault, call external/private RAG, call embeddings APIs, call vector DB services, call browser/CDP/cloud, call WriteLab, call Zotero, read PDFs, or read attachments.

## Known Gaps

- `faiss-cpu` and `sentence-transformers` are not installed in the current environment.
- This is prep/preflight only; it does not prove FAISS indexing, query retrieval, model download, or performance.
- Any real FAISS pilot requires a fresh scoped TaskSpec and explicit authorization for package install, model download, allowlisted source scope, local index artifacts, and raw-content minimization.
