# Parent Pin Review: opencode RAG Single Note Retrieval Pilot

Date: 2026-06-16

## Decision

ACCEPTED_AND_PARENT_PINNED.

The parent repository now records `dev-frame-opencode` at `d4d8a85a54d17c3d787e2e90903776dcf809150e` for the scoped local/offline single Obsidian note retrieval-manifest pilot.

## Pin Delta

- Previous parent-pinned opencode commit: `7f9496310547ceef09e3a6d1e40758d321995fdc`
- New parent-pinned opencode commit: `d4d8a85a54d17c3d787e2e90903776dcf809150e`
- Updated files:
  - `BASELINE_LOCK.json`
  - `integration/lock/submodules.lock.yml`
  - `dev-frame-opencode` gitlink

## Evidence

- Evidence ZIP: `D:\devframe-system\.agent\evidence\evidence-opencode-rag-single-note-retrieval-pilot-a1-d4d8a85.zip`
- SHA256: `D4683D043B1917ED1F38D116A1E0D6BBE4763C342A3374122CD8C5E253620D71`

## Parent Verification Summary

- Evidence hash: PASS.
- Evidence entry list: PASS.
- Focused tests: PASS, 6 passed.
- Schema parse: PASS.
- Submodule diff whitespace check: PASS.
- Parent staged whitespace check: required before commit.

## Governance Boundary

This pin records a scoped local/offline single-note retrieval manifest only. It does not authorize whole-vault scans, attachment reads, PDF/full-text processing, external/private RAG services, embeddings APIs, vector databases, WriteLab calls, browser/CDP/cloud/MiniApp access, production readiness, general RAG readiness, or final governance acceptance.

The next expansion step should be a separate private/local RAG service or whole-vault retrieval TaskSpec with fresh RuntimeAuthorization, evidence minimization rules, and explicit human authorization.
