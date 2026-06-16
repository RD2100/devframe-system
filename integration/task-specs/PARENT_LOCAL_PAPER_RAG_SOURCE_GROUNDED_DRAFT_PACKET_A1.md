# TaskSpec: PARENT_LOCAL_PAPER_RAG_SOURCE_GROUNDED_DRAFT_PACKET_A1

## Status

`TASKSPEC_AUTHORIZED`

## Goal

Create a parent-level source-grounded draft packet from the minimized local
paper RAG answer-preview evidence.

The packet should help the user decide whether the current local RAG workflow
is useful for paper drafting, while preserving strict non-final boundaries.

## Source Evidence

- Human review packet:
  `integration/reports/parent-local-paper-rag-human-review-packet-a1-2026-06-16.md`
- Answer-preview closeout:
  `integration/reports/parent-current-local-paper-rag-answer-preview-milestone-closeout-2026-06-16.md`
- Opencode answer-preview evidence ZIP:
  `D:\devframe-system\.agent\evidence\evidence-opencode-local-paper-rag-answer-preview-a1-528f5b8.zip`
- Opencode evidence ZIP SHA256:
  `F1AB005DBE53429E825E2ACBF58750635744DE7D8A94F978878C9EEABA4F5FB9`
- Test-frame answer-preview consumption ZIP:
  `D:\devframe-system\test-frame\reports\evidence-opencode-local-paper-rag-answer-preview-consumption-a1.zip`
- Test-frame evidence ZIP SHA256:
  `B091B9C9BFEE25E46515A2C4561A69CBD1A3527BE7E8FEFBA932A6509F9B769E`

## Allowed Scope

- Work only in the parent repo `D:\devframe-system`.
- Create parent-level report(s) under `integration/reports/`.
- Use minimized evidence only:
  - question IDs.
  - deterministic answer theme bullets.
  - source/title fingerprints.
  - counts.
  - issue/warning booleans.
  - known gaps.
- No submodule code changes.
- No parent lock/gitlink update.

## Forbidden

- Do not read or expose raw PDF text.
- Do not read or expose raw Markdown bodies.
- Do not read or expose chunks, raw query text, raw source paths, vectors, FAISS
  binary, WriteLab payload/response, Zotero key/API, attachments, notes, full
  text, `paragraph_text`, browser/CDP/cloud, MiniApp payloads, or
  external/private RAG runtime payloads.
- Do not call live Zotero, cloud LLM, cloud vector DB, external/private RAG,
  browser/CDP/cloud, MiniApp, or WriteLab.
- Do not grant RuntimeAuthorization.
- Do not claim final governance acceptance, paper-quality acceptance,
  production readiness, broad/general RAG readiness, whole-vault readiness,
  external/private RAG readiness, cloud readiness, or cloud vector DB readiness.
- Do not push/reset/clean/stash.

## Expected Output

- `integration/reports/parent-local-paper-rag-source-grounded-draft-packet-a1-2026-06-16.md`
- The packet should include:
  - five draft sections mapped to the five preview IDs.
  - a clear distinction between preview themes and unverified source-grounded
    claims.
  - source fingerprint references only.
  - reviewer questions for each section.
  - hard boundary statement.
  - recommended next step.

## Expected Verification

- `git diff --check` for the new report and this TaskSpec.
- Search the generated packet for final/paper-quality/production/RAG-ready
  overclaim language and verify it remains explicitly non-final.
- Commit only the TaskSpec and report.

## Success Criteria

- The user can read the packet and understand what a paper draft might look
  like, without exposing raw private content.
- The packet does not pretend to be a final paper, final answer, or
  paper-quality acceptance.
