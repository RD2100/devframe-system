# Parent Pin Review: opencode RAG FAISS Obsidian Prep

Date: 2026-06-16

## Decision

ACCEPTED_AND_PARENT_PINNED.

The parent repository now records `dev-frame-opencode` at `0617e3e9831002cfbcc3c8125d85ef6e76e0655a` for the scoped FAISS/Obsidian allowlisted-folder prep preflight.

## Pin Delta

- Previous parent-pinned opencode commit: `d4d8a85a54d17c3d787e2e90903776dcf809150e`
- New parent-pinned opencode commit: `0617e3e9831002cfbcc3c8125d85ef6e76e0655a`
- Updated files:
  - `BASELINE_LOCK.json`
  - `integration/lock/submodules.lock.yml`
  - `dev-frame-opencode` gitlink

## Evidence

- Evidence ZIP: `D:\devframe-system\.agent\evidence\evidence-opencode-rag-faiss-obsidian-prep-a1-0617e3e.zip`
- SHA256: `8BAC3BC0D20E48B6C846B32685C85781DE68DB9A7338CEEAA105549973E44DC6`

## Parent Verification Summary

- Evidence hash: PASS.
- Evidence entry list: PASS.
- Focused tests: PASS, 5 passed.
- Adjacent Obsidian/RAG regression: PASS, 22 passed.
- Schema parse: PASS.
- Submodule diff whitespace check: PASS.
- Parent staged whitespace check: required before commit.

## Governance Boundary

This pin records prep/preflight evidence only. It does not authorize package install, model download, FAISS index build, whole-vault scans, attachment reads, PDF/full-text processing, external/private RAG services, embeddings APIs, vector databases, WriteLab calls, browser/CDP/cloud/MiniApp access, production readiness, general RAG readiness, or final governance acceptance.

The next expansion step should be a separate FAISS dependency installation and local pilot TaskSpec with fresh authorization, explicit source allowlist, local index artifact rules, and evidence minimization constraints.
