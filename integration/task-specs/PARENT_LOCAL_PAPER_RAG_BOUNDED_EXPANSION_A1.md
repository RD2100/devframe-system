# TaskSpec: PARENT_LOCAL_PAPER_RAG_BOUNDED_EXPANSION_A1

## Status

`TASKSPEC_AUTHORIZED`

## Goal

Produce a bounded, non-final expanded outline from the local paper RAG
source-grounded draft packet.

The output should be useful for human paper planning while keeping every claim
clearly marked as a draft hypothesis until source-grounded review is complete.

## Inputs

- `integration/reports/parent-local-paper-rag-source-grounded-draft-packet-a1-2026-06-16.md`
- `integration/reports/parent-local-paper-rag-human-review-packet-a1-2026-06-16.md`
- `integration/reports/parent-current-local-paper-rag-answer-preview-milestone-closeout-2026-06-16.md`

## Allowed

- Parent repo only.
- Create `integration/reports/parent-local-paper-rag-bounded-expanded-outline-a1-2026-06-16.md`.
- Use minimized preview themes, source fingerprints, counts, and known gaps.

## Forbidden

- Do not read raw PDF text, raw Markdown bodies, raw chunks, raw query text,
  source paths, vectors, FAISS binaries, WriteLab payloads/responses, Zotero
  key/API, attachments, notes, full text, `paragraph_text`, browser/CDP/cloud,
  MiniApp payloads, or external/private RAG runtime payloads.
- Do not call cloud LLM, external/private RAG, cloud vector DB, browser/CDP,
  MiniApp, Zotero, or WriteLab.
- Do not update parent lock/gitlink.
- Do not claim final governance acceptance, paper-quality acceptance,
  production readiness, broad/general RAG readiness, whole-vault readiness,
  external/private RAG readiness, cloud readiness, or RuntimeAuthorization.

## Expected Output

- Expanded outline with:
  - candidate paper title.
  - abstract skeleton.
  - five section plan mapped to the five preview IDs.
  - per-section draft hypotheses.
  - per-section source fingerprint references.
  - per-section reviewer risks.
  - next source-grounding checklist.

## Verification

- `git diff --check` over this TaskSpec and the report.
- Search report for boundary language proving it remains non-final.
- Commit only this TaskSpec and report.
