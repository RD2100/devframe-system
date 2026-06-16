# Return Review: test-frame Local Paper RAG Usable Pipeline Consumption

Date: 2026-06-16

## Reviewed Return

- TaskSpec: `TESTFRAME_OPENCODE_LOCAL_PAPER_RAG_USABLE_PIPELINE_CONSUMPTION_A1`
- Submodule: `D:\devframe-system\test-frame`
- Commit: `210e47d9353736347e2fbafedc0d67312789b0bb`
- Message: `Add local paper RAG usable pipeline consumption`
- Evidence ZIP: `D:\devframe-system\test-frame\reports\evidence-opencode-local-paper-rag-usable-pipeline-consumption-a1.zip`
- ZIP SHA256: `7ADA51DC43E213022A935730E96CD947940278CA5D4E275FA9CD10A39C119372`

## Intake Decision

ACCEPTED_FOR_PARENT_PIN.

This slice validates parent-pinned opencode usable local paper RAG pipeline
evidence as synthetic/offline test-frame verification evidence only. It checks
both the first-run local index build and the second-run incremental reuse proof.

## Source Evidence

- Producer commit: `7c13ff0de6de8c50706b77efb58b132bce27dce0`
- Parent pin commit: `ffc571caefc0013c2188cfc5ee95b1a8f83af694`
- Source ZIP SHA256: `BA8AD8D6E9E012D17A2CE0EA71FDB478232907D6806470801DC6B4A8C1159B9A`

## Verification

- Fixture JSON parse: PASS.
- Focused pytest: PASS, `12 passed`.
- Adjacent local RAG/closed-loop/FAISS consumption regression: PASS, `35 passed`.
- Evidence manifest JSON parse: PASS.
- Submodule diff whitespace check: PASS.
- Evidence ZIP entry list: PASS.
- Evidence ZIP SHA256: PASS.

## Coverage

- First-run evidence requires `PASS_LOCAL_RAG_PIPELINE`, 6 PDFs, 13 Markdown notes, 6 documents, 47 chunks, 19 source fingerprints, 19 new sources, refresh completed, and index rebuilt.
- Rerun evidence requires 0 new, 0 changed, 19 unchanged, 0 deleted, refresh not required, refresh completed, and index reused.
- Retrieval quality spot-check requires 3 successful queries, 9 total top-k results, coverage count 3, and zero empty, duplicate, low-confidence, or warning signals.
- Fail-closed tests cover missing/drifted provenance, package hash, package entries, command evidence, first-run/rerun values, raw/sensitive markers, external runtime expansion, and final/live/production/general-RAG overclaims.

## Boundary

The test-frame slice did not read raw ZIP payloads, PDFs, Markdown bodies,
chunks, queries, source paths, vectors, FAISS binaries, Zotero key/API, WriteLab
payloads/responses, Obsidian runtime, live RAG, browser/CDP/cloud, MiniApp,
external RAG, embeddings API, vector DB service, or external runtime.

This is not final governance acceptance, paper-quality acceptance, production
readiness, broad live readiness, whole-vault readiness, general RAG readiness,
external/private RAG readiness, cloud readiness, or RuntimeAuthorization.

## Coordination Note

The visible `test-frame` checkout had unrelated later local drift at
`8ae4f71 config: add fitness manager miniapp profile`. To avoid mixing that
unrelated work into this RAG milestone, the reviewed commit was created from a
temporary worktree rooted at the previous parent-pinned `2efaa342...` commit.
The parent pin records only `210e47d9353736347e2fbafedc0d67312789b0bb`.
