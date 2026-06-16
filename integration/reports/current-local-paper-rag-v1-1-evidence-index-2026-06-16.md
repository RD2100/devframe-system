# Current Local Paper RAG v1.1 Evidence Index

Date: 2026-06-16

Status: `CURRENT_EVIDENCE_INDEX_FOR_V1_1_HUMAN_REVIEW_HANDOFF`

This index lists minimized evidence for the current non-final local paper RAG
handoff. It intentionally does not expand raw PDFs, Markdown bodies, chunks,
queries, source paths, vectors, FAISS binaries, WriteLab payloads, Zotero
credentials, browser/cloud payloads, MiniApp runtime content, or other private
runtime data.

## Parent Delivery

| Artifact | Path | SHA256 / Result |
|---|---|---|
| v1.1 review package | `integration/artifacts/paper-drafts/local-paper-rag-review-variants-v1.1-package.zip` | `2731FE77DB74BBDF29822AFEB401B25B09431FC93D942C44B1080884918AC574` |
| v1.1 verifier | `scripts/verify_local_paper_rag_final_review_v1_1.py` | `PASS_LOCAL_PAPER_RAG_FINAL_REVIEW_V1_1_VERIFICATION`, `109 passed`, `0 failed` |
| v1.0 handoff verifier | `scripts/verify_local_paper_rag_v1_0_handoff.py` | `PASS_LOCAL_PAPER_RAG_V1_0_HANDOFF_VERIFICATION`, `36 passed`, `0 failed` |
| submission prep verifier | `scripts/verify_local_paper_rag_submission_prep_v1_0.py` | `PASS_LOCAL_PAPER_RAG_SUBMISSION_PREP_V1_0_VERIFICATION`, `10 passed`, `0 failed` |
| review variants verifier | `scripts/verify_local_paper_rag_review_variants_v1_0.py` | `PASS_LOCAL_PAPER_RAG_REVIEW_VARIANTS_V1_0_VERIFICATION`, `79 passed`, `0 failed` |

## Opencode Producer Evidence

| Slice | Evidence ZIP | SHA256 |
|---|---|---|
| local paper RAG usable pipeline | `.agent/evidence/evidence-opencode-local-paper-rag-usable-pipeline-a1-7c13ff0.zip` | `BA8AD8D6E9E012D17A2CE0EA71FDB478232907D6806470801DC6B4A8C1159B9A` |
| local paper RAG quality eval | `.agent/evidence/evidence-opencode-local-paper-rag-quality-eval-a1-44188cd.zip` | `8C5296FCE736BC8D9AD0F9218EC2B6C598CB85D2FA6897DEF2350E461FF4EDC5` |
| local paper RAG hybrid rerank | `.agent/evidence/evidence-opencode-local-paper-rag-hybrid-rerank-a1-209ac0e.zip` | `BE65898E071DDC351B6B600A97242774190B62D5D9529630706739C0980A0443` |
| local paper RAG answer preview | `.agent/evidence/evidence-opencode-local-paper-rag-answer-preview-a1-528f5b8.zip` | `F1AB005DBE53429E825E2ACBF58750635744DE7D8A94F978878C9EEABA4F5FB9` |

Current pinned opencode commit:

- `528f5b801082a10759df000a2315486a55a22e79`

## Test-Frame Consumer Evidence

| Artifact | Path | SHA256 |
|---|---|---|
| current closed-loop consumption evidence | `test-frame/reports/evidence-opencode-current-local-paper-rag-closed-loop-consumption-a1.zip` | `BFBBA75F9EA9C2675FE565C135D07D423E5C474A146726404B9E73CCC9A14E10` |

Current pinned test-frame commit:

- `72c3150e89c6542054547bc5f092f38388be153c`

Test-frame scope:

- synthetic/offline consumption evidence only;
- no raw PDF, raw Markdown, raw chunks, raw query, source paths, vectors, FAISS
  binary, WriteLab payload, Zotero key/API, browser/cloud payload, or MiniApp
  runtime content;
- no final acceptance, paper-quality acceptance, production readiness,
  broad/general RAG readiness, or RuntimeAuthorization.

## Agent-Acceptance Governance Evidence

| Artifact | Path | SHA256 |
|---|---|---|
| current milestone governance review | `agent-acceptance/_evidence/AGENT_ACCEPTANCE_CURRENT_LOCAL_PAPER_RAG_MILESTONE_GOVERNANCE_REVIEW_A1/evidence-agent-acceptance-current-local-paper-rag-milestone-governance-review-a1.zip` | `06E3ABC40EEB137CBFFFC562714CAA6DC7881DBE4103E6A9107D0D6EA9CE45B7` |

Current pinned agent-acceptance commit:

- `2e0bd5633eaca20bd0124dd22b7dd6d8702325b1`

Governance scope:

- accepted only as non-final milestone evidence;
- no final governance acceptance;
- no paper-quality acceptance;
- no production readiness;
- no broad/general RAG readiness;
- no whole-vault/cloud/vector DB readiness;
- no RuntimeAuthorization.

## Current Parent Pins

| Module | Commit |
|---|---|
| `agent-acceptance` | `2e0bd5633eaca20bd0124dd22b7dd6d8702325b1` |
| `dev-frame-opencode` | `528f5b801082a10759df000a2315486a55a22e79` |
| `devframe-control-plane` | `09167bc656f8625c97bfae5c52dae5a0280b116c` |
| `test-frame` | `72c3150e89c6542054547bc5f092f38388be153c` |

## Superseded / Historical Evidence

The following remain useful for history but are not the current recommended
human-review package:

- v1.0 handoff package;
- v1.0 submission-prep package;
- v1.0 review variants package;
- earlier Axx schema-hardening evidence packages;
- runtime-pilots working files.

Current human-review artifact is v1.1 only.

## Boundary

This evidence index proves only the current handoff package and supporting
minimized evidence chain. It does not prove:

- paper quality;
- empirical training effect;
- target-venue submission readiness;
- production readiness;
- whole-vault readiness;
- broad/general RAG readiness;
- external/private RAG readiness;
- cloud vector DB readiness;
- RuntimeAuthorization.
