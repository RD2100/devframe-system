# Parent Pin Review: opencode RAG FAISS Obsidian Local Pilot

Date: 2026-06-16

## Decision

ACCEPTED_AND_PARENT_PINNED.

The parent repository now records `dev-frame-opencode` at `3b4397655a68712077c042f17f2e1a17f37ba0ba` for the scoped local FAISS allowlisted-folder RAG smoke.

## Pin Delta

- Previous parent-pinned opencode commit: `0617e3e9831002cfbcc3c8125d85ef6e76e0655a`
- New parent-pinned opencode commit: `3b4397655a68712077c042f17f2e1a17f37ba0ba`
- Updated files:
  - `BASELINE_LOCK.json`
  - `integration/lock/submodules.lock.yml`
  - `dev-frame-opencode` gitlink

## Evidence

- Evidence ZIP: `D:\devframe-system\.agent\evidence\evidence-opencode-rag-faiss-obsidian-local-pilot-a1-3b43976.zip`
- SHA256: `69805A82974B7114548557BF13D4181635D588D3E4882BE59791A2FAE34E94C0`

## Parent Verification Summary

- Evidence hash: PASS.
- Evidence entry list: PASS.
- Focused tests: PASS, 4 passed.
- Adjacent Obsidian/RAG regression: PASS, 26 passed.
- Schema parse: PASS.
- Submodule diff whitespace check: PASS.
- Minimized report inspection: PASS.
- Parent staged whitespace check: required before commit.

## Runtime Summary

- Dependencies installed for scoped pilot: `faiss-cpu 1.14.3`, `sentence-transformers 5.5.1`.
- Embedding model used: `sentence-transformers/all-MiniLM-L6-v2`.
- Model download/cache occurred; no HuggingFace token or API token was used or recorded.
- Local index artifact directory: `D:\devframe-system\.agent\runtime\rag-faiss-obsidian-local-index-a1`.
- Smoke result: 7 allowlisted Markdown documents, 316 chunks, 384-dimensional embeddings, top-3 retrieval returned.

## Governance Boundary

This pin records a scoped local FAISS pilot only. It does not authorize whole-vault scans, broader Obsidian access, attachment reads, PDF/full-text processing, external/private RAG services, embeddings APIs, cloud vector databases, WriteLab calls, browser/CDP/cloud/MiniApp access, production readiness, general RAG readiness, whole-vault readiness, paper-quality acceptance, or final governance acceptance.

Recommended next step: test-frame consumption of this minimized FAISS local pilot evidence, followed by agent-acceptance governance review if that consumption passes.
