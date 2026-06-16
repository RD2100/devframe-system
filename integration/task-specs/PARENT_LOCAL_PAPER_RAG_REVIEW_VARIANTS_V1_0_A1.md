# PARENT_LOCAL_PAPER_RAG_REVIEW_VARIANTS_V1_0_A1

## Goal

Create reviewer-facing v1.0 manuscript variants so the same evidence-backed paper draft can be reviewed as:

- a short paper;
- a technical note;
- an internal research brief.

## Scope

Parent-superproject artifacts only:

- build variant Markdown and DOCX files under `integration/artifacts/paper-drafts`;
- build one review-variants handoff ZIP;
- add a verifier for variant uniqueness, package shape, DOCX readability, and non-final boundary;
- update current delivery pointers.

## Boundary

This task does not inspect raw PDFs, raw Markdown source bodies, raw chunks, retrieval queries, source paths, vectors, FAISS binaries, WriteLab payloads, Zotero keys, browser/CDP/cloud/MiniApp runtime content, external RAG services, or cloud vector DB artifacts.

This task does not grant final paper-quality acceptance, training-effect acceptance, production readiness, broad RAG readiness, whole-vault readiness, or RuntimeAuthorization.

## Required Verification

Run from `D:\devframe-system`:

```powershell
python scripts\build_local_paper_rag_review_variants_v1_0.py --root D:\devframe-system
python scripts\verify_local_paper_rag_review_variants_v1_0.py --root D:\devframe-system
```

Expected verifier result:

```text
PASS_LOCAL_PAPER_RAG_REVIEW_VARIANTS_V1_0_VERIFICATION
passed=79 failed=0
```
