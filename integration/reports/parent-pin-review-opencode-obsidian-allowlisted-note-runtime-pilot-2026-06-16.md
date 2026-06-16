# Parent Pin Review: opencode Obsidian Allowlisted Note Runtime Pilot

Date: 2026-06-16

## Decision

ACCEPTED_AND_PARENT_PINNED.

The parent repository now records `dev-frame-opencode` at `7f9496310547ceef09e3a6d1e40758d321995fdc` for the scoped Obsidian allowlisted single-note runtime pilot.

## Pin Delta

- Previous parent-pinned opencode commit: `052b6620a52ac2a525ca5e911e4f090d38f0f9a1`
- New parent-pinned opencode commit: `7f9496310547ceef09e3a6d1e40758d321995fdc`
- Updated files:
  - `BASELINE_LOCK.json`
  - `integration/lock/submodules.lock.yml`
  - `dev-frame-opencode` gitlink

## Evidence

- Evidence ZIP: `D:\devframe-system\.agent\evidence\evidence-opencode-obsidian-allowlisted-note-runtime-pilot-a1-7f94963.zip`
- SHA256: `6474305DF16CF249918E9FD249B2C085484383A7C2496E551EAC40EBAFA8190C`

## Parent Verification Summary

- Evidence hash: PASS.
- Evidence entry list: PASS.
- Focused tests: PASS, 11 passed.
- Related regression: PASS, 59 passed.
- Schema parse: PASS.
- ZIP report schema validation: PASS.
- ZIP raw-sensitive scan: PASS.
- Submodule diff whitespace check: PASS.
- Parent staged whitespace check: required before commit.

## Governance Boundary

This pin records a scoped single-note Obsidian pilot only. It does not authorize whole-vault scans, attachment reads, PDF/full-text processing, RAG/private retrieval, WriteLab calls, browser/CDP/cloud/MiniApp access, production readiness, or final governance acceptance.

The next expansion step should be a separate RAG/private retrieval or Obsidian follow-up TaskSpec with a fresh evidence manifest and explicit human authorization.
