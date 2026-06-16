# Parent Pin Review: opencode Local Paper RAG Usable Pipeline

Date: 2026-06-16

## Decision

ACCEPTED_AND_PARENT_PINNED.

The parent repository now records `dev-frame-opencode` at `7c13ff0de6de8c50706b77efb58b132bce27dce0` for the scoped repeatable local paper RAG pipeline.

## Pin Delta

- Previous parent-pinned opencode commit: `22ad943bca273edcd77115926fad539b102c0fb6`
- New parent-pinned opencode commit: `7c13ff0de6de8c50706b77efb58b132bce27dce0`
- Updated files:
  - `BASELINE_LOCK.json`
  - `integration/lock/submodules.lock.yml`
  - `dev-frame-opencode` gitlink

## Evidence

- Evidence ZIP: `D:\devframe-system\.agent\evidence\evidence-opencode-local-paper-rag-usable-pipeline-a1-7c13ff0.zip`
- SHA256: `BA8AD8D6E9E012D17A2CE0EA71FDB478232907D6806470801DC6B4A8C1159B9A`

## Parent Verification Summary

- Evidence hash: PASS.
- Evidence entry list: PASS.
- Focused tests: PASS, 5 passed.
- Adjacent RAG/Obsidian/closed-loop regression: PASS, 37 passed.
- Schema parse: PASS.
- First-run and rerun report schema validation: PASS.
- Minimized report inspection: PASS.
- Raw value/path marker scan: PASS.
- Submodule diff whitespace check: PASS.
- Parent staged whitespace check: required before commit.

## Runtime Summary

- First run: 6 PDFs, 13 Markdown notes, 6 FAISS documents, 47 chunks, 19 new source fingerprints, index rebuilt, 3 retrieval queries succeeded, 9 total top-k results.
- Second run: 0 new, 0 changed, 19 unchanged, 0 deleted, refresh not required, index reused.
- Quality spot-check: deterministic local rules, no empty results, no duplicate results, no low-confidence warnings.

## Governance Boundary

This pin records a scoped local pipeline milestone only. It does not authorize whole-vault scans, broader Obsidian access, Zotero key/API access, external/private RAG services, cloud vector databases, browser/CDP/cloud/MiniApp access, production readiness, general RAG readiness, whole-vault readiness, paper-quality acceptance, or final governance acceptance.

Recommended next step: test-frame consumption of this minimized usable-pipeline evidence, followed by agent-acceptance governance review if that consumption passes.
