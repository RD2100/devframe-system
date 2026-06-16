# test-frame RAG FAISS Obsidian Local Index Consumption Return Review

Date: 2026-06-16

## Verdict

ACCEPTED_FOR_PARENT_PIN as synthetic/offline consumption validation for the parent-pinned opencode FAISS Obsidian local index pilot.

This is not final governance acceptance, paper-quality acceptance, production readiness, broad live readiness, whole-vault readiness, general RAG readiness, external/private RAG readiness, or RuntimeAuthorization.

## Reviewed Return

- Module: `test-frame`
- Branch: `codex/adapter-negative-matrix`
- Commit: `98564a402337ce9f4b8b2b789f64952d82586bb8`
- Message: `Add FAISS Obsidian local index consumption`
- Evidence ZIP: `D:\devframe-system\test-frame\reports\evidence-opencode-rag-faiss-obsidian-local-index-consumption-a1.zip`
- Expected SHA256: `C3D1175EEE4F364BD9CEEFDCDC1AE3355A9876CDA52A81A94743EE39A1C3D916`
- Observed SHA256: `C3D1175EEE4F364BD9CEEFDCDC1AE3355A9876CDA52A81A94743EE39A1C3D916`

## Source Context Consumed

- Parent opencode pin commit: `8ee589e6f10eae9d5d1f58617eaa1bc4adf3797b`
- Parent-pinned opencode commit: `3b4397655a68712077c042f17f2e1a17f37ba0ba`
- Source opencode evidence ZIP: `D:\devframe-system\.agent\evidence\evidence-opencode-rag-faiss-obsidian-local-pilot-a1-3b43976.zip`
- Source opencode evidence ZIP SHA256: `69805A82974B7114548557BF13D4181635D588D3E4882BE59791A2FAE34E94C0`

## Scope Accepted

- Adds minimized fixture `docs\test-frame\paper-pipeline-metadata-only\opencode-rag-faiss-obsidian-local-index-consumption.fixture.json`.
- Adds focused fail-closed tests `tests\test_opencode_rag_faiss_obsidian_local_index_consumption.py`.
- Updates paper-pipeline metadata-only documentation with FAISS local index consumption semantics.
- Consumes parent-pinned minimized facts only.
- Does not read Obsidian note bodies, raw chunks, raw queries, raw local paths, runtime FAISS vectors, index binaries, PDFs, attachments, Zotero credentials, WriteLab payloads, external/private RAG, embeddings APIs, vector DB services, browser/CDP, cloud, or MiniApp.

## Parent Verification

- Evidence hash matched expected SHA256.
- Evidence entry list contains command/report/manifest/patch artifacts only.
- `python -m json.tool docs\test-frame\paper-pipeline-metadata-only\opencode-rag-faiss-obsidian-local-index-consumption.fixture.json` -> PASS.
- `python -m pytest tests\test_opencode_rag_faiss_obsidian_local_index_consumption.py -q` -> 11 passed.
- `python -m pytest tests\test_opencode_rag_faiss_obsidian_local_index_consumption.py tests\test_opencode_a63_a64_zotero_manifest_uniqueness_consumption.py tests\test_opencode_pdf_writelab_live_real_pilot_consumption.py tests\test_paper_pipeline_metadata_only_orchestration.py -q` -> 37 passed.
- `python -m pytest tests\test_evidence_pack_manifest.py tests\test_evidence_collector.py tests\test_opencode_rag_faiss_obsidian_local_index_consumption.py -q` -> 36 passed.
- `python -m json.tool reports\opencode-rag-faiss-obsidian-local-index-consumption-a1\evidence\evidence-pack-manifest.json` -> PASS.
- `git diff --check 22b9220cd3620805fe13b28898636cace8d9b158 98564a402337ce9f4b8b2b789f64952d82586bb8` -> PASS.

## Coverage Accepted

- Positive fixture consumes `PASS_FAISS_LOCAL_INDEX_SMOKE` as verification evidence only.
- Provenance, parent pin, ZIP hash, package entries, schema refs, dependency/model facts, and counts are pinned.
- Fail-closed checks cover:
  - producer/parent/hash/schema/package drift;
  - zero or drifted document/chunk/retrieval counts;
  - dependency/model/index-kind drift;
  - model download with token use;
  - whole-vault scan or external runtime expansion;
  - raw note/chunk/query/path/vector markers and token-like values;
  - final/live/production/paper-quality/general-RAG/whole-vault overclaims.

## Known Gaps

- Synthetic/offline consumption only.
- Does not prove whole-vault indexing, ranking quality, incremental refresh, private/external RAG service readiness, cloud vector DB readiness, or paper-quality acceptance.
- Does not inspect raw Obsidian notes, raw chunks, paths, runtime index binaries, or FAISS vectors by design.
