# Parent Final Stage Evidence Index After FAISS

Date: 2026-06-16

Status: `NON_FINAL_LOCAL_FAISS_MILESTONE_INDEXED`

Parent basis:
- parent HEAD before this index: `05e57ea Record FAISS paper plugin milestone closeout`
- parent branch: `codex/rdinit-phase-0-5`

## Purpose

This report is a practical final-stage index for the current work session. It
does not introduce new runtime behavior, new authorization, or new evidence. It
collects the parent-pinned state after the FAISS Obsidian local pilot and marks
the current project stop line.

This is not final governance acceptance, production readiness, broad live
readiness, paper-quality acceptance, whole-vault readiness, general RAG
readiness, external/private RAG readiness, cloud vector DB readiness, cloud or
payment readiness, or RuntimeAuthorization.

## Current Stop Line

`NON_FINAL_MILESTONE_ACCEPTED_CANDIDATE_AT_LOCAL_FAISS_BOUNDARY`

Plain meaning:

- The project has a parent-pinned, governance-reviewed local FAISS RAG smoke.
- The smoke is scoped to an allowlisted Obsidian Markdown folder.
- The smoke has test-frame consumption checks and agent-acceptance governance
  review.
- It is enough for tonight's non-final milestone.
- It is not enough to call the system production-ready or generally RAG-ready.

## Current Parent Pins

| Module | Pinned commit | Meaning |
|---|---:|---|
| `agent-acceptance` | `77f080875561010d3eaa1bf5e90b6e9ade9d0084` | FAISS governance review accepted as non-final milestone candidate |
| `dev-frame-opencode` | `3b4397655a68712077c042f17f2e1a17f37ba0ba` | FAISS Obsidian local pilot implementation/evidence |
| `test-frame` | `98564a402337ce9f4b8b2b789f64952d82586bb8` | FAISS evidence consumption validation |
| `devframe-control-plane` | `09167bc656f8625c97bfae5c52dae5a0280b116c` | Existing fail-closed/security closeout pin |

## Main Evidence Chain

### 1. Paper MVP Closeout

- parent commit: `40f49f2 Pin opencode paper MVP closeout`
- opencode commit: `b7716c8b60998d822e52e078ee003487a4dbf236`
- evidence: compact Paper MVP closeout candidate
- boundary: non-final; no live resource rerun

### 2. Paper MVP Governance Review

- parent commit: `84f17df Pin agent-acceptance paper MVP governance review`
- agent-acceptance commit: `0769485321f3ab733f7315e5f2ff5e44b82d731c`
- verdict: `PAPER_MVP_CLOSEOUT_ACCEPTED_AS_NON_FINAL_MILESTONE_CANDIDATE`
- boundary: not paper-quality acceptance, not production-ready

### 3. PDF Excerpt To Local WriteLab Smoke

- parent commit: `b93099f Pin opencode PDF WriteLab live pilot`
- opencode commit: `fc15f7b829ff1701b6e7e78778cd549608b8a577`
- result: scoped local PDF excerpt to local WriteLab live smoke
- boundary: no broad PDF/full-text processing, no production-ready claim

### 4. PDF WriteLab Bindings

- parent commit: `cde2a1d Pin opencode PDF WriteLab live bindings`
- opencode commit: `a8b5a0143bff87f8aaaed3d50b9b6ad9225f7843`
- result: business validation and plugin closeout include scoped live-smoke
  evidence
- boundary: binding only; no additional live call

### 5. Obsidian Allowlisted Note Pilot

- parent commit: `c04386e Pin opencode Obsidian allowlisted note pilot`
- opencode commit: `7f9496310547ceef09e3a6d1e40758d321995fdc`
- result: one allowlisted Markdown note metadata/count evidence
- boundary: no whole-vault scan, no attachments, no RAG readiness

### 6. RAG Single Note Retrieval Pilot

- parent commit: `f7bcb3d Pin opencode RAG single note pilot`
- opencode commit: `d4d8a85a54d17c3d787e2e90903776dcf809150e`
- result: deterministic local single-note retrieval manifest
- boundary: no external/private RAG, no embeddings API, no vector DB, no
  general RAG readiness

### 7. FAISS Obsidian Local Pilot

- parent commit: `8ee589e Pin opencode FAISS Obsidian local pilot`
- opencode commit: `3b4397655a68712077c042f17f2e1a17f37ba0ba`
- evidence ZIP SHA256:
  `69805A82974B7114548557BF13D4181635D588D3E4882BE59791A2FAE34E94C0`
- result:
  - 7 allowlisted Markdown documents
  - 316 chunks
  - 384-dimensional embeddings
  - FAISS `IndexFlatIP`
  - top-3 retrieval
  - `faiss-cpu 1.14.3`
  - `sentence-transformers 5.5.1`
  - model `sentence-transformers/all-MiniLM-L6-v2`
- boundary:
  - evidence excludes raw note text, raw chunks, raw query, raw paths, vectors,
    secrets, and FAISS index binary
  - not whole-vault-ready, not general-RAG-ready, not cloud-vector-ready

### 8. test-frame FAISS Consumption

- parent commit: `66851dc Pin test-frame FAISS Obsidian consumption`
- test-frame commit: `98564a402337ce9f4b8b2b789f64952d82586bb8`
- evidence ZIP SHA256:
  `C3D1175EEE4F364BD9CEEFDCDC1AE3355A9876CDA52A81A94743EE39A1C3D916`
- result: synthetic/offline consumption validation for minimized FAISS evidence
- boundary: cannot promote smoke to final, production, general RAG, or
  whole-vault readiness

### 9. Agent Acceptance FAISS Governance Review

- parent commit: `e53e74f Pin agent-acceptance FAISS Obsidian governance review`
- agent-acceptance commit: `77f080875561010d3eaa1bf5e90b6e9ade9d0084`
- evidence ZIP SHA256:
  `702CBB9D19020B4566B4E7C2DBD2FAF3F3A36ED7C2F2BC9584A2F1BA2EACDE8C`
- verdict:
  `RAG_FAISS_OBSIDIAN_LOCAL_PILOT_ACCEPTED_AS_NON_FINAL_MILESTONE_CANDIDATE`
- boundary: non-final milestone candidate only

### 10. FAISS Closeout

- parent commit: `05e57ea Record FAISS paper plugin milestone closeout`
- report:
  `integration/reports/parent-current-paper-plugin-milestone-closeout-after-faiss-2026-06-16.md`
- result: current project stop line recorded at local FAISS boundary

## Ten-Track Status

| # | Track | Current status | Practical meaning |
|---:|---|---|---|
| 1 | Integration superproject | `DONE_FOR_LOCAL_FAISS_MILESTONE` | Parent can pin, lock, and report current modules. |
| 2 | Cross-repo contracts | `DONE_FOR_LOCAL_FAISS_MILESTONE` | opencode/test-frame/agent-acceptance contracts align on minimized evidence and non-final boundaries. |
| 3 | opencode adapter | `DONE_FOR_LOCAL_FAISS_MILESTONE` | Zotero metadata, PDF/WriteLab smoke, Obsidian note, single-note RAG, and FAISS local pilot are represented. |
| 4 | test-frame adapter / TestRunSpec | `DONE_FOR_LOCAL_FAISS_MILESTONE` | FAISS evidence consumption and overclaim guards exist. |
| 5 | control-plane state machine conformance | `STABLE_FROZEN_FOR_THIS_MILESTONE` | Existing fail-closed/security pin remains enough; no new expansion. |
| 6 | artifact registry / evidence store | `DONE_FOR_LOCAL_FAISS_MILESTONE` | Evidence ZIP hashes and parent reports are indexed. |
| 7 | RuntimeAuthorization signer / validator | `SCOPED_ONLY` | Runtime authorization remains narrow; no broad grant. |
| 8 | source-level safety review | `DONE_FOR_SCOPED_RUNTIME_PATHS` | No P0/P1 blocker found for current scoped paths; not a full historical audit. |
| 9 | dry-run end-to-end harness | `PARTIAL_BUT_USEFUL` | Paper pipeline and MiniApp evidence exist; not full production E2E. |
| 10 | canary repo + rollback drill | `PARTIAL` | order-dish canary evidence exists; explicit rollback rehearsal remains undone. |

## What Is Not Done

- Final governance acceptance.
- Paper-quality acceptance.
- Production readiness.
- Broad live readiness.
- Whole-vault Obsidian indexing.
- Attachments/PDF/full-text unrestricted processing.
- General RAG readiness.
- External/private RAG service integration.
- Cloud vector DB integration.
- Ranking quality evaluation over real research questions.
- Incremental index refresh or delete/update behavior.
- Release tag, push, or deployment.
- Parent dirty/report drift cleanup.

## Current Risk Notes

- Parent worktree contains older local report/runtime drift. This report does not
  classify or clean that drift.
- `agent-acceptance\.agent\PROJECT_REGISTRY.json` remains local runtime/workspace
  registry drift and is intentionally excluded from pins.
- FAISS model download/cache happened during the pilot, but model cache lifecycle,
  refresh behavior, and larger-corpus performance are not closed.
- Minimized evidence protects private content, but it also means paper-content
  quality must be evaluated separately.

## Recommended Stop/Next Decision

Recommended stop for tonight:

`STOP_AT_LOCAL_FAISS_NON_FINAL_MILESTONE`

If more time is available, the next useful step should be one of:

1. `PARENT_DRIFT_CLASSIFICATION_AND_FINAL_EVIDENCE_LEDGER_A1`
   - no runtime expansion; classify current parent dirty/untracked reports and
     produce a clean reviewer ledger.
2. `RAG_FAISS_QUALITY_EVAL_MINIMIZED_A1`
   - ask a few fixed queries, store only minimized scores/fingerprints, and do
     not persist raw chunks/query text.
3. `OBSIDIAN_WHOLE_VAULT_PREAUTH_A1`
   - prepare authorization and minimization rules before scanning wider vault
     content.

Do not proceed directly to broad whole-vault RAG, cloud vector DB, production
readiness, or final acceptance without a fresh scoped TaskSpec.
