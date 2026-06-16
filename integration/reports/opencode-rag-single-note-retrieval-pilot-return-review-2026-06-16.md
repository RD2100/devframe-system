# opencode RAG Single Note Retrieval Pilot Return Review

Date: 2026-06-16

## Verdict

ACCEPTED_FOR_PARENT_PIN as a scoped local/offline single Obsidian note retrieval-manifest pilot.

This is not final governance acceptance, paper-quality acceptance, production readiness, broad live readiness, whole-vault RAG readiness, or authorization for external/private RAG services.

## Reviewed Return

- Module: `dev-frame-opencode`
- Branch: `codex/paper-audit-privacy-hard-gate`
- Commit: `d4d8a85a54d17c3d787e2e90903776dcf809150e`
- Message: `Add RAG single note retrieval pilot`
- Evidence ZIP: `D:\devframe-system\.agent\evidence\evidence-opencode-rag-single-note-retrieval-pilot-a1-d4d8a85.zip`
- Expected SHA256: `D4683D043B1917ED1F38D116A1E0D6BBE4763C342A3374122CD8C5E253620D71`
- Observed SHA256: `D4683D043B1917ED1F38D116A1E0D6BBE4763C342A3374122CD8C5E253620D71`

## Scope Accepted

- Adds `paper rag-single-note-pilot`.
- Adds deterministic local/offline retrieval manifest generation over exactly one allowlisted Obsidian Markdown note.
- Stores minimized facts only: counts, fingerprints, boundary booleans, and retrieval mode.
- Adds closed schema `schemas/paper_rag_single_note_retrieval_pilot_report.schema.json`.

## Live Scoped Smoke Summary

- Vault root: `D:\Obsidian\paper-pilot`
- One allowlisted Markdown note was read.
- `pilot_status=PASS_SINGLE_NOTE_RETRIEVAL_MANIFEST`
- `validation_kind=local_single_note_retrieval_manifest`
- `source_kind=obsidian_allowlisted_note`
- `note_size_bytes=19316`
- `chunk_count=17`
- `chunk_fingerprint_count=17`
- `top_k_count=3`
- `retrieval_index_kind=deterministic_local`
- `whole_vault_scanned=false`
- `external_rag_called=false`
- `embeddings_api_called=false`
- `vector_db_called=false`
- `raw_note_persisted=false`
- `raw_chunks_persisted=false`
- `raw_query_persisted=false`
- `rag_ready_claimed=false`

## Parent Verification

- Evidence hash matched expected SHA256.
- Evidence entry list was limited to changed-files, command logs, minimized reports, schema snapshot, `EXECUTION_REPORT.md`, and `REVIEWER_INDEX.md`.
- `python -m pytest tests\test_paper_rag_single_note_retrieval_pilot.py -q` -> 6 passed.
- `python -m json.tool schemas\paper_rag_single_note_retrieval_pilot_report.schema.json` -> PASS.
- `git diff --check 7f9496310547ceef09e3a6d1e40758d321995fdc d4d8a85a54d17c3d787e2e90903776dcf809150e` -> PASS.

## Privacy Boundary

- Evidence/report contain minimized facts only.
- No raw note body, raw chunks, raw query, raw note path, raw paper text, or vault listing is accepted as parent evidence.
- The accepted slice did not call external/private RAG, embeddings APIs, vector DBs, browser/CDP/cloud, WriteLab, Zotero, PDFs, attachments, or whole-vault scan.

## Known Gaps

- This is a local single-note retrieval manifest only, not private/external RAG service integration.
- Whole-vault RAG, attachments, PDF/full-text, WriteLab, Zotero, embeddings APIs, and vector DBs remain out of scope.
- Paper quality acceptance remains a separate human/reviewer decision.
