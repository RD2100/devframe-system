# Parent Local Paper RAG Human Review Packet A1

## Purpose

This packet turns the current minimized local paper RAG answer-preview evidence
into a human-review checklist.

It is intended to answer one practical question:

> Are the current local RAG answer-preview themes and source-routing signals
> useful enough to guide the next paper-quality review step?

This packet is not final governance acceptance, paper-quality acceptance,
production readiness, broad/general RAG readiness, whole-vault readiness,
external/private RAG readiness, cloud readiness, or RuntimeAuthorization.

## Source Evidence

- Parent milestone closeout:
  `integration/reports/parent-current-local-paper-rag-answer-preview-milestone-closeout-2026-06-16.md`
- Opencode answer-preview evidence ZIP:
  `D:\devframe-system\.agent\evidence\evidence-opencode-local-paper-rag-answer-preview-a1-528f5b8.zip`
- Opencode ZIP SHA256:
  `F1AB005DBE53429E825E2ACBF58750635744DE7D8A94F978878C9EEABA4F5FB9`
- Test-frame consumption ZIP:
  `D:\devframe-system\test-frame\reports\evidence-opencode-local-paper-rag-answer-preview-consumption-a1.zip`
- Test-frame ZIP SHA256:
  `B091B9C9BFEE25E46515A2C4561A69CBD1A3527BE7E8FEFBA932A6509F9B769E`
- Agent-acceptance governance ZIP:
  `D:\devframe-system\.agent\evidence\evidence-agent-acceptance-local-paper-rag-answer-preview-governance-review-a1-aa0fcd5.zip`
- Agent-acceptance ZIP SHA256:
  `F9D9B06D220D983B02234D7CA470CE0CDA990A5F2339E2603F169581DEFE1FC1`

## Current Minimized Status

- `preview_status`: `PASS_LOCAL_RAG_ANSWER_PREVIEW`
- `validation_kind`: `local_deterministic_answer_preview`
- `answer_preview_kind`: `deterministic_local_rules`
- `document_count`: 6
- `chunk_count`: 47
- `query_count`: 5
- `retrieval_success_count`: 3
- `answer_preview_count`: 5
- `hybrid_rerank_enabled`: true
- `rerank_strategy`: `embedding_plus_title_keyword_source_count`
- `q4_hybrid_expected_source_matched`: true
- `citation_source_consistency_passed`: true
- `issue_count`: 0
- `warnings_count`: 0

## Preview Rows For Human Review

The rows below are minimized. They do not include raw query text, raw paper
text, raw Markdown bodies, source paths, chunks, vectors, or FAISS binaries.

### Q1_EARTHQUAKE_RESCUE_PURPOSE

Answer theme bullets:

- training objective framing
- rescue procedure rehearsal
- risk-reduced scenario practice

Signals:

- expected source matched: true
- citation source consistency passed: true
- top source fingerprints:
  - `sha256:771bd90bae9e97a19ef08a3d50dfecbfa5c2c0c87e963c8abfb97b87d09cc0ae`
  - `sha256:22c432f35ccffd6723a28130d22ff317fdab2b3b14854663bfd05dec0623b44b`
  - `sha256:8f4146baa4b3d6f1c69ae9c1ca4403ea8f89f2c7c9c0db40eb3986f33894014f`

Manual review prompt:

- Does this preview stay focused on why earthquake rescue training uses virtual/immersive practice?
- Does it avoid claiming final answer quality from minimized fingerprints alone?

### Q2_FOREIGN_MILITARY_CHARACTERISTICS

Answer theme bullets:

- simulation-based readiness
- repeatable scenario design
- technology-supported training control

Signals:

- expected source matched: true
- citation source consistency passed: true
- top source fingerprints:
  - `sha256:8f4146baa4b3d6f1c69ae9c1ca4403ea8f89f2c7c9c0db40eb3986f33894014f`
  - `sha256:ef4be5bcc0f3f828c417cdf4c7353b71d2662693eaebb3e74c979af46cf288d3`
  - `sha256:22c432f35ccffd6723a28130d22ff317fdab2b3b14854663bfd05dec0623b44b`

Manual review prompt:

- Does this preview identify useful training-system characteristics rather than drifting into generic military commentary?
- Is the result actionable enough to justify a deeper source-grounded review?

### Q3_VR_FIRE_RESCUE_ADVANTAGES

Answer theme bullets:

- safer practice environment
- repeatable emergency drills
- immersive decision rehearsal

Signals:

- expected source matched: true
- citation source consistency passed: true
- top source fingerprints:
  - `sha256:f78911a3127834f1a1aa6d7cd1f3f2ba4961c606f00ced9156f77b1d9696e031`
  - `sha256:771bd90bae9e97a19ef08a3d50dfecbfa5c2c0c87e963c8abfb97b87d09cc0ae`
  - `sha256:22c432f35ccffd6723a28130d22ff317fdab2b3b14854663bfd05dec0623b44b`

Manual review prompt:

- Does this preview capture practical VR/fire-rescue benefits without overclaiming operational effectiveness?
- Would a reviewer know which direction to inspect next in the source corpus?

### Q4_VIRTUAL_SCENE_CONSTRUCTION_FACTORS

Answer theme bullets:

- scene fidelity and training objective alignment
- environment modeling and interaction design
- scenario coverage for operational tasks

Signals:

- expected source matched: true
- citation source consistency passed: true
- Q4 hybrid expected source matched: true
- top source fingerprints:
  - `sha256:22c432f35ccffd6723a28130d22ff317fdab2b3b14854663bfd05dec0623b44b`
  - `sha256:771bd90bae9e97a19ef08a3d50dfecbfa5c2c0c87e963c8abfb97b87d09cc0ae`
  - `sha256:8f4146baa4b3d6f1c69ae9c1ca4403ea8f89f2c7c9c0db40eb3986f33894014f`

Manual review prompt:

- This was the prior weak spot. Does the hybrid rerank now route the preview toward virtual-scene construction instead of a broader adjacent topic?
- Are the three themes sufficient as a paper-outline seed, or do they need source-grounded expansion?

### Q5_MILITARY_VOCATIONAL_EDUCATION_VALUE

Answer theme bullets:

- job-oriented skill transfer
- standardized local practice evidence
- repeatable competence evaluation support

Signals:

- expected source matched: true
- citation source consistency passed: true
- top source fingerprints:
  - `sha256:ef4be5bcc0f3f828c417cdf4c7353b71d2662693eaebb3e74c979af46cf288d3`
  - `sha256:22c432f35ccffd6723a28130d22ff317fdab2b3b14854663bfd05dec0623b44b`
  - `sha256:771bd90bae9e97a19ef08a3d50dfecbfa5c2c0c87e963c8abfb97b87d09cc0ae`

Manual review prompt:

- Does this preview connect local RAG evidence to vocational education value without making institutional or outcome claims not proven by the evidence?
- Is it a useful bridge toward a paper section or reviewer note?

## Human Review Checklist

Use this as the next manual gate:

- [ ] The five preview IDs cover the intended review questions.
- [ ] Each answer theme is understandable without raw private content.
- [ ] Q4 routing is acceptable after hybrid rerank.
- [ ] Source fingerprints are enough to verify provenance without exposing raw paths.
- [ ] No row is treated as a final answer.
- [ ] No row is treated as paper-quality acceptance.
- [ ] Any row needing expansion is marked for source-grounded follow-up.
- [ ] Any row that looks too generic is sent back to local rerank/query refinement.
- [ ] Reviewer agrees whether the next step should be paper-outline drafting,
      source-grounded answer generation, or another retrieval-quality pass.

## Decision Options

Choose one:

1. `PROCEED_TO_SOURCE_GROUNDED_DRAFT_PACKET`
   - Use the five preview rows as outline seeds.
   - Still minimized and local unless fresh authorization expands scope.
2. `REFINE_RETRIEVAL_OR_RERANK`
   - Keep improving local RAG ranking/query coverage before drafting.
3. `HOLD_FOR_HUMAN_PAPER_QUALITY_REVIEW`
   - Stop technical expansion and let a human reviewer judge usefulness.

## Boundary

This packet is derived from minimized evidence only. It does not read or expose
raw PDF text, raw Markdown bodies, raw chunks, raw query text, source paths,
vectors, FAISS binaries, WriteLab payloads/responses, Zotero key/API material,
attachments, notes, full text, `paragraph_text`, browser/CDP/cloud, MiniApp
payloads, or external/private RAG runtime payloads.

It does not claim final governance acceptance, paper-quality acceptance,
production readiness, broad/general RAG readiness, whole-vault readiness,
external/private RAG readiness, cloud readiness, cloud vector DB readiness, or
RuntimeAuthorization.

## Recommended Next TaskSpec

`PARENT_LOCAL_PAPER_RAG_SOURCE_GROUNDED_DRAFT_PACKET_A1`

Goal: generate a local, minimized draft packet from the five preview rows and
source fingerprints. The packet should remain non-final and should clearly mark
which statements are preview themes versus source-grounded claims.
