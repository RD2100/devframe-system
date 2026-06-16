# Parent Current Paper Plugin Milestone Closeout After FAISS

Date: 2026-06-16

Status: `NON_FINAL_MILESTONE_ACCEPTED_CANDIDATE_AT_LOCAL_FAISS_BOUNDARY`

Parent repo: `D:\devframe-system`
Parent HEAD basis: `e53e74f Pin agent-acceptance FAISS Obsidian governance review`

## Decision

The current project state is suitable to describe as a non-final Paper MVP plus
plugin-pilot milestone candidate at the local FAISS boundary.

This is stronger than the earlier single-note RAG closeout because the project
now has a scoped local FAISS allowlisted-folder pilot, test-frame consumption
validation, and agent-acceptance governance review all parent-pinned.

This closeout does not claim final governance acceptance, paper-quality
acceptance, production readiness, broad live readiness, whole-vault readiness,
general RAG readiness, external/private RAG readiness, cloud vector DB
readiness, cloud/payment readiness, or RuntimeAuthorization.

## Current Parent Pins

- `agent-acceptance = 77f080875561010d3eaa1bf5e90b6e9ade9d0084`
- `dev-frame-opencode = 3b4397655a68712077c042f17f2e1a17f37ba0ba`
- `devframe-control-plane = 09167bc656f8625c97bfae5c52dae5a0280b116c`
- `test-frame = 98564a402337ce9f4b8b2b789f64952d82586bb8`

## What Is Done

1. Integration superproject
   - Parent now records current accepted gitlinks and lock entries for opencode,
     test-frame, and agent-acceptance at the FAISS milestone.
   - Relevant parent commits:
     - `40f49f2` pinned opencode Paper MVP closeout.
     - `c04386e` pinned Obsidian allowlisted note pilot.
     - `f7bcb3d` pinned RAG single-note pilot.
     - `8ee589e` pinned opencode FAISS Obsidian local pilot.
     - `66851dc` pinned test-frame FAISS Obsidian consumption.
     - `e53e74f` pinned agent-acceptance FAISS Obsidian governance review.

2. Cross-repo contracts
   - opencode produced minimized schemas/reports for Zotero metadata, PDF/WriteLab,
     Obsidian note, local single-note retrieval, and local FAISS allowlisted-folder
     RAG smoke.
   - test-frame has synthetic/offline consumption checks for the FAISS evidence
     shape and overclaim guards.
   - agent-acceptance reviewed FAISS governance boundaries and accepted only a
     non-final milestone candidate.

3. opencode adapter
   - Current pin includes a scoped local FAISS pilot over an allowlisted Obsidian
     Markdown folder.
   - Evidence records `faiss-cpu 1.14.3`, `sentence-transformers 5.5.1`, model
     `sentence-transformers/all-MiniLM-L6-v2`, 7 Markdown documents, 316 chunks,
     384-dimensional embeddings, `IndexFlatIP`, and top-3 retrieval.
   - Evidence excludes raw note text, raw chunks, raw query, raw paths, vectors,
     secrets, and FAISS index binary.

4. test-frame adapter / TestRunSpec
   - Current pin consumes FAISS minimized evidence as verification evidence only.
   - Fail-closed coverage includes provenance/hash/package drift, count/model/version
     drift, remote token use, scope expansion, raw-sensitive markers, and
     final/live/production/general-RAG/whole-vault overclaims.

5. control-plane state machine conformance
   - Control-plane remains pinned at the previously accepted fail-closed/security
     closeout state.
   - No new control-plane runtime expansion was required for this milestone.

6. Artifact registry / evidence store
   - `.agent\evidence` and test-frame report ZIPs contain the current FAISS
     milestone evidence.
   - Parent reports record hashes, boundaries, and pin decisions.

7. RuntimeAuthorization signer / validator
   - RuntimeAuthorization remains scoped and non-broad.
   - The FAISS milestone does not grant a new broad authorization.

8. Source-level safety review
   - Existing runtime pilot safety review found no P0/P1 source-level blocker for
     scoped Obsidian/RAG paths.
   - FAISS governance review also found no P0/P1 blocker for the local FAISS
     milestone candidate.

9. Dry-run / E2E harness
   - Paper pipeline has local/offline closeout evidence.
   - order-dish has real local MiniApp E2E evidence from the earlier runtime path.
   - FAISS itself is represented as scoped local smoke plus test-frame consumption.

10. Canary repo / rollback drill
   - External project verification exists via `D:\order-dish`.
   - A polished release tag would still benefit from explicit rollback rehearsal,
     but it is not required for this non-final milestone candidate.

## Evidence Summary

### Paper MVP Closeout Governance

- opencode closeout pinned: `b7716c8b60998d822e52e078ee003487a4dbf236`
- agent-acceptance governance pinned: `0769485321f3ab733f7315e5f2ff5e44b82d731c`
- Verdict: `PAPER_MVP_CLOSEOUT_ACCEPTED_AS_NON_FINAL_MILESTONE_CANDIDATE`

### Obsidian Allowlisted Note Runtime Pilot

- opencode pinned: `7f9496310547ceef09e3a6d1e40758d321995fdc`
- Evidence ZIP SHA256: `6474305DF16CF249918E9FD249B2C085484383A7C2496E551EAC40EBAFA8190C`
- Result: one allowlisted Markdown note read, metadata/counts only.
- Not claimed: whole-vault scan, attachment/PDF/full-text readiness, RAG readiness,
  broad live readiness.

### RAG Single Obsidian Note Local Retrieval Pilot

- opencode pinned: `d4d8a85a54d17c3d787e2e90903776dcf809150e`
- Evidence ZIP SHA256: `D4683D043B1917ED1F38D116A1E0D6BBE4763C342A3374122CD8C5E253620D71`
- Result: deterministic local single-note retrieval manifest with chunk fingerprints.
- Not claimed: external/private RAG, embeddings API, vector DB, whole-vault RAG,
  general RAG readiness, raw note/chunk/query persistence.

### Local FAISS Obsidian Allowlisted-Folder Pilot

- opencode pinned: `3b4397655a68712077c042f17f2e1a17f37ba0ba`
- Parent pin commit: `8ee589e6f10eae9d5d1f58617eaa1bc4adf3797b`
- Evidence ZIP SHA256: `69805A82974B7114548557BF13D4181635D588D3E4882BE59791A2FAE34E94C0`
- Result: local FAISS smoke over allowlisted Obsidian Markdown folder.
- Recorded facts: 7 documents, 316 chunks, 384-dimensional embeddings,
  `IndexFlatIP`, top-3 retrieval, model download/cache performed, no token used.
- Not claimed: whole-vault readiness, general RAG readiness, external/private RAG,
  cloud vector DB readiness, paper-quality acceptance.

### test-frame FAISS Consumption

- test-frame pinned: `98564a402337ce9f4b8b2b789f64952d82586bb8`
- Parent pin commit: `66851dcd196f3daabcb0d58c3b6256348e7fea0c`
- Evidence ZIP SHA256: `C3D1175EEE4F364BD9CEEFDCDC1AE3355A9876CDA52A81A94743EE39A1C3D916`
- Result: synthetic/offline consumption validation of minimized FAISS evidence.
- Not claimed: final acceptance, production readiness, broad live readiness,
  general RAG readiness, whole-vault readiness.

### Agent Acceptance FAISS Governance Review

- agent-acceptance pinned: `77f080875561010d3eaa1bf5e90b6e9ade9d0084`
- Parent pin commit: `e53e74f`
- Verdict: `RAG_FAISS_OBSIDIAN_LOCAL_PILOT_ACCEPTED_AS_NON_FINAL_MILESTONE_CANDIDATE`
- Evidence ZIP SHA256: `702CBB9D19020B4566B4E7C2DBD2FAF3F3A36ED7C2F2BC9584A2F1BA2EACDE8C`
- Known warning: runner finish reported `ExecutionReport may be missing gate results`;
  parent-side verification still confirmed py_compile, pytest, diff check, ZIP hash,
  and ZIP entry list.

## What Is Not Done

- No final governance acceptance.
- No paper-quality acceptance.
- No production readiness claim.
- No broad live readiness claim.
- No whole-vault Obsidian scan.
- No unrestricted attachment/PDF/full-text expansion.
- No external/private RAG service integration.
- No cloud vector DB integration.
- No cloud/payment production verification.
- No polished release tag or push.
- No final user-facing product acceptance.

## Current Stop Point

The plan should stop at the local FAISS boundary unless the user explicitly
authorizes a fresh next slice.

The meaningful current status is:

`LOCAL_FAISS_RAG_SMOKE_PARENT_PINNED_AND_GOVERNANCE_REVIEWED_NON_FINAL`

This means the project can demonstrate:

- real Zotero metadata-only was already handled earlier;
- PDF/WriteLab scoped live smoke was handled earlier;
- Obsidian allowlisted note access works;
- local single-note retrieval manifest works;
- local FAISS allowlisted-folder index smoke works;
- test-frame validates FAISS evidence as non-final;
- agent-acceptance confirms the boundary.

It does not mean the system is production-ready or generally RAG-ready.

## Residual Risk

- Parent worktree still contains older pre-existing report/registry drift outside
  this closeout.
- `agent-acceptance\.agent\PROJECT_REGISTRY.json` remains local runtime/workspace
  registry drift and is intentionally excluded from parent pins.
- The FAISS pilot performed a local model download/cache and local index smoke,
  but ranking quality, refresh behavior, and larger corpus behavior remain
  unproven.
- The current FAISS evidence excludes raw content by design; that is good for
  governance, but it means content quality still needs a separate human/reviewer
  evaluation path.

## Recommended Next Human Decision

Choose one:

1. Stop here for tonight as
   `NON_FINAL_MILESTONE_ACCEPTED_CANDIDATE_AT_LOCAL_FAISS_BOUNDARY`.
2. Run a small FAISS quality evaluation slice over minimized query/result facts.
3. Prepare whole-vault Obsidian preauthorization.
4. Prepare external/private RAG or cloud vector DB preauthorization.
5. Start a release-polish pass to classify parent drift and create a final
   evidence index without expanding runtime scope.
