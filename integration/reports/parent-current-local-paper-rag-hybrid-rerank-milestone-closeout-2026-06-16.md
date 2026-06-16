# Parent Current Local Paper RAG Hybrid Rerank Milestone Closeout

Date: 2026-06-16

## Verdict

LOCAL_PAPER_RAG_HYBRID_RERANK_CLOSED_AS_NON_FINAL_MILESTONE_CANDIDATE

The parent superproject now has a complete non-final evidence chain for the local paper RAG hybrid rerank milestone:

1. parent human spot-check identified the Q4 source-routing limitation.
2. opencode implemented deterministic local hybrid rerank evidence.
3. test-frame consumed the minimized evidence and verified fail-closed boundaries.
4. agent-acceptance reviewed the chain as non-final governance evidence.
5. parent lock/gitlink pins and parent intake reports are aligned.

This closes the current hybrid rerank milestone only as scoped local paper RAG usability evidence. It is not final governance acceptance, paper-quality acceptance, production readiness, broad live readiness, whole-vault readiness, general RAG readiness, external/private RAG readiness, cloud readiness, cloud vector DB readiness, or RuntimeAuthorization.

## Pinned Chain

### Human Spot Check

- parent commit: `27b037d`
- report: `integration/reports/parent-local-paper-rag-human-spot-check-a1-2026-06-16.md`
- verdict: `PASS_WITH_LIMITATIONS`
- key finding: Q4 broad virtual-scene question needed title/keyword/source-count assist because semantic-only ranking put the earthquake-rescue paper first.

### Opencode

- parent pin commit: `4f29a77`
- module: `dev-frame-opencode`
- pinned commit: `209ac0e0417338c332af59a342fcf5c8a19b51af`
- task: `OPENCODE_LOCAL_PAPER_RAG_HYBRID_RERANK_A1`
- evidence ZIP: `D:\devframe-system\.agent\evidence\evidence-opencode-local-paper-rag-hybrid-rerank-a1-209ac0e.zip`
- SHA256: `BE65898E071DDC351B6B600A97242774190B62D5D9529630706739C0980A0443`

### Test-Frame

- parent pin commit: `1d4fdb6`
- module: `test-frame`
- pinned commit: `1cd659f7f5b8f7edfda81fffa994a188fda8bf5d`
- task: `TESTFRAME_OPENCODE_LOCAL_PAPER_RAG_HYBRID_RERANK_CONSUMPTION_A1`
- evidence ZIP: `D:\devframe-system\test-frame\reports\evidence-opencode-local-paper-rag-hybrid-rerank-consumption-a1.zip`
- SHA256: `B554D2D6FA681233E26ED1324EAA3C86705C8D01A79D8B17251C749BBEA21426`

### Agent-Acceptance

- parent pin commit: `d24d818`
- module: `agent-acceptance`
- pinned commit: `aac98913ff8df3caf486fe766d0c8920ae5d7ce8`
- task: `AGENT_ACCEPTANCE_LOCAL_PAPER_RAG_HYBRID_RERANK_GOVERNANCE_REVIEW_A1`
- evidence ZIP: `D:\devframe-system\.agent\evidence\evidence-agent-acceptance-local-paper-rag-hybrid-rerank-governance-review-a1-aac9891.zip`
- SHA256: `BE96983D4E54C4D60CD6351B87EBB102CB382A43BAFB6D59A5F99496EDCBC77D`

## What Is Now Proven

The local paper RAG chain now has scoped evidence that the previously observed Q4 routing weakness has been addressed by a deterministic local hybrid rerank:

- `hybrid_rerank_enabled=true`
- `rerank_strategy=embedding_plus_title_keyword_source_count`
- `rerank_spot_check_passed=true`
- `rerank_query_count=1`
- `rerank_expected_source_match_count=1`
- `rerank_issue_count=0`
- `rerank_warning_count=0`
- core retrieval remained stable:
  - document count: 6
  - chunk count: 47
  - retrieval query count: 3
  - retrieval success count: 3
  - top-k total count: 9
- hybrid report remained compatible with quality eval:
  - `quality_eval_status=PASS_LOCAL_RAG_QUALITY_EVAL`

The test-frame consumption slice verifies the minimized evidence shape and fails closed when:

- hybrid rerank is disabled.
- rerank strategy drifts.
- expected source match count is zero.
- rerank issues or warnings appear while the report claims PASS.
- retrieval counts regress.
- quality-eval compatibility fails.
- raw/private markers appear.
- runtime scope expands.
- final, paper-quality, production, general-RAG, whole-vault, external/private-RAG, cloud, or RuntimeAuthorization claims are made.

The agent-acceptance review confirms that this is governance-acceptable only as non-final milestone evidence.

## What Is Not Proven

This closeout does not prove:

- final governance acceptance
- paper-quality acceptance
- human paper-quality acceptance
- full citation-grounded answer verification
- broad ranking quality
- broader corpus coverage
- whole-vault indexing
- broad live readiness
- private/external RAG readiness
- cloud vector DB integration
- cloud readiness
- production readiness
- RuntimeAuthorization

## Boundary

The parent closeout did not inspect raw PDF text, Markdown bodies, chunks, query text, source paths, vectors, FAISS binaries, API keys, WriteLab payloads/responses, private runtime artifacts, Zotero key/API, live RAG, PDF conversion, Obsidian runtime, browser/CDP/cloud, MiniApp, cloud LLM, cloud vector DB, external/private RAG, embeddings API, or vector DB service.

The parent closeout does not update runtime authorization scope and does not authorize new live resource access.

## Current Practical Meaning

The project now has a local paper RAG path that is usable enough for the current scoped milestone:

- PDF-to-Markdown local corpus exists for the authorized paper folder.
- local FAISS-backed pipeline can build and reuse an index.
- minimized quality-eval passes.
- human spot-check identified a real ranking weakness.
- hybrid rerank produces evidence closing that weakness for the recorded Q4 spot-check.
- test-frame and agent-acceptance have both independently consumed/reviewed the minimized evidence.
- parent pins all relevant module commits.

This is the strongest current non-final RAG milestone so far. The next meaningful work should be product-facing or acceptance-facing, not more low-yield schema hardening by default:

- generate a small answer preview/report from the local RAG results for human review;
- run a human paper-quality review over selected questions and retrieved sources;
- package a repeatable command/workflow for day-to-day local use;
- only expand to whole-vault, external/private RAG, cloud vector DB, or production under fresh scoped authorization.

## Reviewer Index

- changed files:
  - `integration/reports/parent-current-local-paper-rag-hybrid-rerank-milestone-closeout-2026-06-16.md`
- critical code paths: none; parent closeout report only.
- tests/probes run:
  - inherited verified opencode/test-frame/agent-acceptance ZIP hashes
  - parent pin review checks from `4f29a77`, `1d4fdb6`, and `d24d818`
  - parent lock JSON parse before the final governance pin
- generated artifacts:
  - this closeout report
- known gaps:
  - non-final milestone closeout only
  - no runtime reproduction by parent
  - no raw/private content inspection by parent
- suggested review focus:
  - confirm the closeout preserves non-final boundary
  - confirm Q4 scoped closure is not treated as broad ranking quality proof
  - confirm all module pins are represented accurately
