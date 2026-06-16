# Test-Frame Local Paper RAG Hybrid Rerank Consumption Return Review

## Intake Verdict

`ACCEPTED_FOR_PARENT_PIN`

This intake records test-frame synthetic/offline consumption validation for the parent-pinned opencode local paper RAG hybrid-rerank evidence.

## Reviewed Source

- Module: `test-frame`
- Source baseline: `9d91a7f7ae1dcfca0c8b6be362ebb3691e3e8528`
- Scoped commit: `1cd659f7f5b8f7edfda81fffa994a188fda8bf5d`
- Commit message: `Add local paper RAG hybrid rerank consumption`
- Temporary worktree: `D:\devframe-system\.agent\worktrees\test-frame-hybrid-rerank`

The visible `D:\devframe-system\test-frame` checkout had unrelated drift, so the scoped commit was produced in a clean temporary worktree.

## Changed Files

- `docs/test-frame/paper-pipeline-metadata-only/README.md`
- `docs/test-frame/paper-pipeline-metadata-only/opencode-local-paper-rag-hybrid-rerank-consumption.fixture.json`
- `tests/test_opencode_local_paper_rag_hybrid_rerank_consumption.py`

## Evidence

- Evidence ZIP: `D:\devframe-system\test-frame\reports\evidence-opencode-local-paper-rag-hybrid-rerank-consumption-a1.zip`
- SHA256: `B554D2D6FA681233E26ED1324EAA3C86705C8D01A79D8B17251C749BBEA21426`
- ZIP entries:
  - `commands/preflight.txt`
  - `commands/verification-summary.txt`
  - `manifests/evidence-manifest.json`
  - `EXECUTION_REPORT.md`
  - `REVIEWER_INDEX.md`
  - `STATUS_SUMMARY.md`

## Parent-Pinned Source Consumed

- opencode commit: `209ac0e0417338c332af59a342fcf5c8a19b51af`
- opencode parent pin: `4f29a7776c76a1db83da0a06119486bf22cbc7f5`
- opencode evidence ZIP SHA256: `BE65898E071DDC351B6B600A97242774190B62D5D9529630706739C0980A0443`

## Verification

- `python -m json.tool docs\test-frame\paper-pipeline-metadata-only\opencode-local-paper-rag-hybrid-rerank-consumption.fixture.json > $null`: PASS
- `python -m pytest tests\test_opencode_local_paper_rag_hybrid_rerank_consumption.py -q`: 11 passed
- Local RAG consumption regression:
  - `python -m pytest tests\test_opencode_local_paper_rag_usable_pipeline_consumption.py tests\test_opencode_local_paper_rag_quality_eval_consumption.py tests\test_opencode_local_paper_rag_hybrid_rerank_consumption.py -q`: 34 passed
- Evidence collector/manifest plus local RAG consumption regression:
  - `python -m pytest tests\test_evidence_pack_manifest.py tests\test_evidence_collector.py tests\test_opencode_local_paper_rag_usable_pipeline_consumption.py tests\test_opencode_local_paper_rag_quality_eval_consumption.py tests\test_opencode_local_paper_rag_hybrid_rerank_consumption.py -q`: 59 passed
- `python -m json.tool ...\evidence-manifest.json`: PASS
- `git diff --check`: PASS, CRLF warning only
- `git diff --cached --check`: PASS, CRLF warning only

## Coverage Summary

- Positive minimized fixture consumes opencode hybrid rerank as test-frame verification evidence only.
- Requires hybrid rerank enabled, strategy `embedding_plus_title_keyword_source_count`, rerank spot-check passed, one rerank query, one expected source match, and zero rerank issues/warnings.
- Requires pipeline status `PASS_LOCAL_RAG_PIPELINE`, 6 documents, 47 chunks, 3 retrieval queries, 3 retrieval successes, and 9 top-k results.
- Requires hybrid quality-eval compatibility status `PASS_LOCAL_RAG_QUALITY_EVAL`.
- Fails closed on provenance/package/schema drift, missing or false rerank flags, wrong rerank strategy, zero expected source matches, rerank warnings/issues while PASS, retrieval regressions, quality-eval compatibility failure, raw/sensitive markers, runtime expansion, and final/paper-quality/production/RAG-ready/RuntimeAuthorization overclaims.

## Boundary

This is synthetic/offline consumption only. It does not inspect raw opencode ZIP payloads, raw PDF text, Markdown bodies, chunks, query text, source paths, vectors, FAISS binaries, Zotero key/API material, WriteLab payloads/responses, attachments, notes, full text, paragraph text, browser/CDP/cloud, MiniApp, whole-vault Obsidian, external/private RAG, embeddings API, or vector DB service.

It does not claim final governance acceptance, paper-quality acceptance, production readiness, broad/general RAG readiness, whole-vault readiness, external/private RAG readiness, cloud readiness, or RuntimeAuthorization.

## Known Gaps

- Consumption validates minimized evidence shape only; it does not rerun opencode runtime.
- Hybrid rerank remains deterministic local rerank evidence, not paper-quality acceptance.
- Broader corpus, whole-vault, external/private RAG, cloud vector DB, and production readiness remain out of scope.
