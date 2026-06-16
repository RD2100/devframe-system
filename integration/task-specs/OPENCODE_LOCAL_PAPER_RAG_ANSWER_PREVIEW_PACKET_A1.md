# OPENCODE_LOCAL_PAPER_RAG_ANSWER_PREVIEW_PACKET_A1

## Goal

Add a practical, human-reviewable local paper RAG answer preview packet.

This moves the current local RAG chain from retrieval/eval evidence to a small deterministic answer-preview report for reviewer inspection. It remains preview evidence only, not final answer quality, paper-quality acceptance, production readiness, broad/general RAG readiness, or RuntimeAuthorization.

## Context

The parent has closed the local paper RAG hybrid rerank milestone:

- parent closeout: `f0d1e57 Close local paper RAG hybrid rerank milestone`
- parent-pinned `dev-frame-opencode`: `209ac0e0417338c332af59a342fcf5c8a19b51af`
- parent-pinned `test-frame`: `1cd659f7f5b8f7edfda81fffa994a188fda8bf5d`
- parent-pinned `agent-acceptance`: `aac98913ff8df3caf486fe766d0c8920ae5d7ce8`

Current proven state:

- local paper RAG pipeline builds and reuses a FAISS index.
- deterministic local quality eval passes.
- hybrid rerank closes the recorded Q4 source-routing limitation for the scoped spot-check.
- all evidence remains minimized and non-final.

## Allowed

- Work inside `D:\devframe-system\dev-frame-opencode`.
- Add CLI, adapter, schema, tests, and minimized evidence output.
- Reuse existing local paper RAG pipeline/runtime artifacts where possible.
- Use local/offline deterministic/rules-only answer theme generation.
- Read the authorized local paper/Markdown-derived corpus through existing pipeline/runtime paths if needed.
- Use installed local `faiss-cpu` / `sentence-transformers` if needed.
- Generate minimized report, manifest, schema, tests, and evidence ZIP.

## Forbidden

- Do not call Zotero API/key.
- Do not call cloud LLM, cloud vector DB, external/private RAG service, browser/CDP/cloud, or MiniApp.
- Do not persist raw PDF text, raw Markdown bodies, raw chunks, raw query text, raw source paths, vectors, secrets, API keys, or raw WriteLab payload/response in report/evidence ZIP.
- Do not claim final governance acceptance, paper-quality acceptance, production readiness, broad/general RAG readiness, whole-vault readiness, external/private RAG readiness, cloud readiness, or RuntimeAuthorization.
- Do not update parent pin/lock.
- Do not push/reset/clean/stash.

## Expected Implementation

- Add a CLI such as `paper local-rag-answer-preview`.
- Add a closed JSON schema for the answer preview report.
- Emit a minimized report with fields such as:
  - `preview_status=PASS_LOCAL_RAG_ANSWER_PREVIEW`
  - `validation_kind=local_deterministic_answer_preview`
  - `document_count`
  - `chunk_count`
  - `query_count`
  - `retrieval_success_count`
  - `answer_preview_count`
  - five stable question IDs
  - deterministic answer themes or compact paraphrase rows
  - top source fingerprints/title fingerprints only
  - citation/source consistency booleans
  - warning and issue counts
  - boundary booleans for no cloud LLM, no external RAG, no raw persistence, and no final/production/general-RAG claims

The report may include deterministic answer-theme bullets if they are generated summaries and do not quote raw paper text.

## Question Set

Represent these as stable IDs, not raw full question text:

- Q1: earthquake rescue virtual training system purpose
- Q2: foreign military virtual training system characteristics
- Q3: VR fire/rescue training advantages
- Q4: virtual scene construction factors
- Q5: military vocational education application value

Q4 must use the hybrid rerank source-routing result.

## Expected Negative Cases

- Missing, duplicate, or extra question ID fails closed.
- Q4 source fingerprint/title fingerprint drift fails closed.
- Raw text/path/query/vector fields in minimized report fail closed.
- Cloud LLM, external RAG, cloud vector DB, or broadened runtime flags fail closed.
- Any final governance, paper-quality, production, whole-vault, general-RAG, cloud, or RuntimeAuthorization overclaim fails closed.

## Expected Verification

- Focused pytest for the answer preview report.
- Relevant local RAG regression tests.
- Schema JSON parse.
- CLI smoke on current local runtime/corpus.
- Raw-sensitive scan over generated report/manifest/evidence staging.
- `git diff --check`.

## Return

- Status: `READY_FOR_PARENT_INTAKE` or `BLOCKED_WITH_REASON`.
- Commit hash and message.
- Changed files.
- Evidence ZIP path and SHA256.
- Verification commands and results.
- Live/local smoke summary if run.
- Reviewer Index: changed files, critical paths, tests, generated artifacts, known gaps, and review focus.
