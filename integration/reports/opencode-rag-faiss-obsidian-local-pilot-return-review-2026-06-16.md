# opencode RAG FAISS Obsidian Local Pilot Return Review

Date: 2026-06-16

## Verdict

ACCEPTED_FOR_PARENT_PIN as a scoped local FAISS allowlisted-folder RAG smoke.

This is not final governance acceptance, paper-quality acceptance, production readiness, broad live readiness, whole-vault readiness, external/private RAG readiness, cloud vector DB readiness, or authorization to broaden source scope.

## Reviewed Return

- Module: `dev-frame-opencode`
- Branch: `codex/paper-audit-privacy-hard-gate`
- Commit: `3b4397655a68712077c042f17f2e1a17f37ba0ba`
- Message: `Add FAISS Obsidian local index pilot`
- Evidence ZIP: `D:\devframe-system\.agent\evidence\evidence-opencode-rag-faiss-obsidian-local-pilot-a1-3b43976.zip`
- Expected SHA256: `69805A82974B7114548557BF13D4181635D588D3E4882BE59791A2FAE34E94C0`
- Observed SHA256: `69805A82974B7114548557BF13D4181635D588D3E4882BE59791A2FAE34E94C0`

## Scope Accepted

- Adds `paper rag-faiss-obsidian-local-pilot`.
- Adds local FAISS Obsidian pilot adapter.
- Adds closed schema `schemas/paper_rag_faiss_obsidian_local_pilot_report.schema.json`.
- Adds focused tests `tests\test_paper_rag_faiss_obsidian_local_pilot.py`.
- Installs and uses `faiss-cpu` and `sentence-transformers` for this scoped pilot.
- Builds a local FAISS index from the explicitly allowlisted Obsidian Markdown folder only.
- Stores runtime index artifacts under `D:\devframe-system\.agent\runtime\rag-faiss-obsidian-local-index-a1`.
- Keeps evidence minimized and excludes raw note text, raw chunks, raw query, raw local paths, vectors, secrets, and the index binary.

## Live Local Smoke Summary

- `pilot_status=PASS_FAISS_LOCAL_INDEX_SMOKE`
- `faiss-cpu=1.14.3`
- `sentence-transformers=5.5.1`
- embedding model: `sentence-transformers/all-MiniLM-L6-v2`
- model download/cache performed: `true`
- remote token used: `false`
- document count: `7`
- chunk count: `316`
- embedding dimension: `384`
- FAISS index kind: `IndexFlatIP`
- retrieved count: `3`
- whole vault scanned: `false`
- external RAG called: `false`
- embeddings API called: `false`
- vector DB service called: `false`
- PDF/full text read: `false`
- WriteLab called: `false`

## Parent Verification

- Evidence hash matched expected SHA256.
- Evidence entry list was limited to changed-files, command logs, minimized reports, schema snapshot, `EXECUTION_REPORT.md`, and `REVIEWER_INDEX.md`.
- `python -m pytest tests\test_paper_rag_faiss_obsidian_local_pilot.py -q` -> 4 passed.
- `python -m pytest tests\test_paper_rag_faiss_obsidian_local_pilot.py tests\test_paper_rag_faiss_obsidian_prep.py tests\test_paper_rag_single_note_retrieval_pilot.py tests\test_obsidian_note_adapter.py -q` -> 26 passed.
- `python -m json.tool schemas\paper_rag_faiss_obsidian_local_pilot_report.schema.json` -> PASS.
- `git diff --check 0617e3e9831002cfbcc3c8125d85ef6e76e0655a 3b4397655a68712077c042f17f2e1a17f37ba0ba` -> PASS.
- ZIP report inspection confirmed minimized report values and non-final boundary booleans.

## Privacy Boundary

- Evidence/report contain minimized facts only.
- `raw_note_persisted_in_report_or_evidence=false`
- `raw_chunks_persisted_in_report_or_evidence=false`
- `raw_query_persisted=false`
- `raw_paths_persisted=false`
- `embedding_vectors_persisted_in_evidence=false`
- `api_key_persisted=false`
- `zotero_key_persisted=false`

## Runtime Boundary

- The accepted slice reads only the explicitly allowlisted Obsidian Markdown folder.
- It does not scan the whole vault.
- It does not read PDFs, attachments, `.obsidian` config, Zotero key/API, WriteLab, browser/CDP/cloud, MiniApp, external/private RAG, embeddings API, or cloud vector DB.
- It does not claim final acceptance, paper-quality acceptance, production readiness, broad live readiness, whole-vault readiness, or general RAG readiness.

## Known Gaps

- This proves one scoped local FAISS index smoke, not a production RAG service.
- It does not prove whole-vault indexing, refresh/incremental indexing, ranking quality, multi-query evaluation, private RAG service integration, cloud vector DB integration, or paper-quality acceptance.
- Any expansion beyond the allowlisted folder requires a fresh scoped TaskSpec and explicit authorization.
