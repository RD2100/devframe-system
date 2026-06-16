# Parent Pin Review: opencode Local Paper RAG Closed Loop

Date: 2026-06-16

## Decision

ACCEPTED_AND_PARENT_PINNED.

The parent repository now records `dev-frame-opencode` at `22ad943bca273edcd77115926fad539b102c0fb6` for the scoped local paper RAG closed-loop pilot.

## Pin Delta

- Previous parent-pinned opencode commit: `3b4397655a68712077c042f17f2e1a17f37ba0ba`
- New parent-pinned opencode commit: `22ad943bca273edcd77115926fad539b102c0fb6`
- Updated files:
  - `BASELINE_LOCK.json`
  - `integration/lock/submodules.lock.yml`
  - `dev-frame-opencode` gitlink

## Evidence

- Evidence ZIP: `D:\devframe-system\.agent\evidence\evidence-opencode-local-paper-rag-closed-loop-a1-22ad943.zip`
- SHA256: `E1EC86F5A87BF02527E23FD582139B3CE7A4F5B969A859DD724C59FC21596B69`

## Parent Verification Summary

- Evidence hash: PASS.
- Evidence entry list: PASS.
- Focused tests: PASS, 6 passed.
- Adjacent PDF/Obsidian/RAG/WriteLab regression: PASS, 36 passed.
- Schema parse: PASS.
- Report schema validation: PASS.
- Minimized report inspection: PASS.
- Submodule diff whitespace check: PASS.
- Parent staged whitespace check: required before commit.

## Runtime Summary

- Source scope: authorized local PDF folder `E:\厂里\虚拟训练`.
- Target scope: authorized Obsidian vault folder `D:\Obsidian\paper-pilot\papers\virtual-training`.
- Smoke result: 3 PDFs converted into 3 Markdown notes, FAISS index built over 3 documents and 27 chunks, 3 retrieval queries returned 9 total top-k results.
- Diagnosis path: `rules_fallback`, issue count 0.

## Governance Boundary

This pin records a scoped local pilot only. It does not authorize whole-vault scans, broader Obsidian access, Zotero key/API access, external/private RAG services, cloud vector databases, browser/CDP/cloud/MiniApp access, production readiness, general RAG readiness, whole-vault readiness, paper-quality acceptance, or final governance acceptance.

Recommended next step: test-frame consumption of this minimized closed-loop evidence, followed by agent-acceptance governance review if that consumption passes.
