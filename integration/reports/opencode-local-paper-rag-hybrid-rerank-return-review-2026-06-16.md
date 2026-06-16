# Opencode Local Paper RAG Hybrid Rerank Return Review

## Intake Verdict

`ACCEPTED_FOR_PARENT_PIN`

This intake records the opencode local paper RAG hybrid rerank slice. It accepts the slice as scoped local/offline candidate evidence only.

## Reviewed Source

- Module: `dev-frame-opencode`
- Branch: `codex/paper-audit-privacy-hard-gate`
- Commit: `209ac0e0417338c332af59a342fcf5c8a19b51af`
- Commit message: `Add local paper RAG hybrid rerank`

## Changed Files

- `ai-workflow-hub/src/ai_workflow_hub/context_layer/adapters/local_paper_rag_pipeline.py`
- `ai-workflow-hub/tests/test_paper_local_rag_pipeline.py`
- `schemas/paper_local_rag_pipeline_report.schema.json`

## Evidence

- Evidence ZIP: `D:\devframe-system\.agent\evidence\evidence-opencode-local-paper-rag-hybrid-rerank-a1-209ac0e.zip`
- Declared SHA256: `BE65898E071DDC351B6B600A97242774190B62D5D9529630706739C0980A0443`
- Observed SHA256: `BE65898E071DDC351B6B600A97242774190B62D5D9529630706739C0980A0443`
- ZIP entry list: expected hybrid pipeline report/manifest, hybrid quality eval report/manifest, schema, command logs, ExecutionReport, Reviewer Index, and changed-files list only.

## Live/Local Smoke Summary

- `pipeline_status`: `PASS_LOCAL_RAG_PIPELINE`
- `hybrid_rerank_enabled`: true
- `rerank_strategy`: `embedding_plus_title_keyword_source_count`
- `rerank_spot_check_passed`: true
- `rerank_query_count`: 1
- `rerank_expected_source_match_count`: 1
- `rerank_issue_count`: 0
- `rerank_warning_count`: 0
- document count: 6
- chunk count: 47
- retrieval query count: 3
- retrieval success count: 3
- top-k total count: 9
- hybrid report quality eval status: `PASS_LOCAL_RAG_QUALITY_EVAL`

## Parent Verification

- `Get-FileHash ... -Algorithm SHA256`: PASS
- `tar -tf ...`: PASS
- `PYTHONPATH=src; python -m pytest tests\test_paper_local_rag_pipeline.py -q`: 6 passed
- `python -m json.tool schemas\paper_local_rag_pipeline_report.schema.json`: PASS
- `git diff --check 44188cdb627e571bed55b20fe4f8d71d2d0828c1 209ac0e0417338c332af59a342fcf5c8a19b51af`: PASS
- ZIP report field inspection: `rerank_spot_check_passed=true`, final/paper-quality/production/RAG-ready claims remained false.

## Boundary

The slice improves deterministic local source routing for the scoped paper RAG pipeline. It does not persist raw PDF text, raw Markdown bodies, raw chunks, raw query text, raw source paths, vectors, FAISS binaries, secrets, API keys, or raw WriteLab payloads/responses in the evidence ZIP.

It does not call Zotero API/key, cloud LLM, cloud vector DB, external/private RAG service, browser/CDP/cloud, MiniApp, or perform a whole-vault scan.

It does not claim final governance acceptance, paper-quality acceptance, production readiness, broad/general RAG readiness, whole-vault readiness, external/private RAG readiness, cloud readiness, or RuntimeAuthorization.

## Known Gaps

- Hybrid rerank is deterministic local title-keyword/source-count evidence, not a full answer-quality evaluator.
- Evidence stores minimized fingerprints/counts only; raw source reasoning stays outside evidence by design.
- Broader corpus, whole-vault, external/private RAG, and production readiness remain out of scope.
