# Test-Frame Local Paper RAG Answer Preview Consumption Return Review

## Intake Verdict

`ACCEPTED_FOR_PARENT_PIN`

This intake records test-frame synthetic/offline consumption validation for the parent-pinned opencode local paper RAG answer-preview evidence.

## Reviewed Source

- Module: `test-frame`
- Previous parent-pinned baseline: `1cd659f7f5b8f7edfda81fffa994a188fda8bf5d`
- Scoped commit: `18c19898c599eca5452f2e10fcaa23f2d151339d`
- Commit message: `Add local paper RAG answer preview consumption`
- Visible checkout: `D:\devframe-system\test-frame`

The visible checkout contains unrelated old local drift in files outside this slice. This review scope is limited to the scoped answer-preview consumption commit and its evidence package.

## Changed Files

- `docs/test-frame/paper-pipeline-metadata-only/local-paper-rag-answer-preview-consumption.md`
- `docs/test-frame/paper-pipeline-metadata-only/opencode-local-paper-rag-answer-preview-consumption.fixture.json`
- `tests/test_opencode_local_paper_rag_answer_preview_consumption.py`

## Evidence

- Evidence ZIP: `D:\devframe-system\test-frame\reports\evidence-opencode-local-paper-rag-answer-preview-consumption-a1.zip`
- SHA256: `B091B9C9BFEE25E46515A2C4561A69CBD1A3527BE7E8FEFBA932A6509F9B769E`
- ZIP entries:
  - `commands/preflight.txt`
  - `commands/verification-summary.txt`
  - `manifests/evidence-manifest.json`
  - `EXECUTION_REPORT.md`
  - `REVIEWER_INDEX.md`
  - `STATUS_SUMMARY.md`

## Parent-Pinned Source Consumed

- opencode commit: `528f5b801082a10759df000a2315486a55a22e79`
- opencode parent pin: `3879e6ec25f563cde395abe0cba6a84198a6cbef`
- opencode evidence ZIP SHA256: `F1AB005DBE53429E825E2ACBF58750635744DE7D8A94F978878C9EEABA4F5FB9`

## Verification

- `Get-FileHash -Algorithm SHA256 D:\devframe-system\test-frame\reports\evidence-opencode-local-paper-rag-answer-preview-consumption-a1.zip`: matched declared SHA256.
- `tar -tf D:\devframe-system\test-frame\reports\evidence-opencode-local-paper-rag-answer-preview-consumption-a1.zip`: expected command/report/manifest entries only.
- `python -m json.tool docs\test-frame\paper-pipeline-metadata-only\opencode-local-paper-rag-answer-preview-consumption.fixture.json > $null`: PASS.
- `python -m pytest tests\test_opencode_local_paper_rag_answer_preview_consumption.py -q`: 11 passed.
- `python -m json.tool reports\opencode-local-paper-rag-answer-preview-consumption-a1\manifests\evidence-manifest.json > $null`: PASS.

## Coverage Summary

- Positive minimized fixture consumes opencode answer-preview evidence as test-frame verification evidence only.
- Requires `PASS_LOCAL_RAG_ANSWER_PREVIEW`, five answer previews, six documents, 47 chunks, five queries, Q4 hybrid expected source match, and zero issues/warnings.
- Fails closed on provenance, package hash, package entry, schema, source commit, parent pin, scope, count, Q4 routing, warning/issue, raw-sensitive marker, runtime expansion, and final/paper-quality/production/RAG-ready/RuntimeAuthorization overclaim drift.

## Boundary

This is synthetic/offline consumption only. It does not inspect raw opencode ZIP payloads, raw PDF text, Markdown bodies, chunks, query text, source paths, vectors, FAISS binaries, Zotero key/API material, WriteLab payloads/responses, attachments, notes, full text, paragraph text, browser/CDP/cloud, MiniApp, whole-vault Obsidian, external/private RAG, embeddings API, or vector DB service.

It does not claim final governance acceptance, paper-quality acceptance, production readiness, broad/general RAG readiness, whole-vault readiness, external/private RAG readiness, cloud readiness, or RuntimeAuthorization.

## Known Gaps

- Consumption validates minimized evidence shape only; it does not rerun opencode runtime.
- Answer previews are deterministic/rules-only human-review aids, not paper-quality acceptance.
- Broader corpus, whole-vault, external/private RAG, cloud vector DB, and production readiness remain out of scope.
