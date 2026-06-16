# Current Local Paper RAG Fast Parallel Closeout Plan

Date: 2026-06-16

Status: `FAST_PARALLEL_CLOSEOUT_PLAN_ACTIVE`

Purpose: finish the current local paper RAG milestone tonight without reopening
old low-yield hardening loops. This is a non-final milestone closeout plan. It
does not claim paper-quality acceptance, training-effect acceptance, production
readiness, broad/general RAG readiness, whole-vault readiness, cloud/vector DB
readiness, or RuntimeAuthorization.

## Current Anchor

Parent HEAD at planning time:

- `42ea537 Add local paper RAG final review package v1.1`

Current recommended artifact:

- `integration/artifacts/paper-drafts/local-paper-rag-review-variants-v1.1-package.zip`
- SHA256:
  `2731FE77DB74BBDF29822AFEB401B25B09431FC93D942C44B1080884918AC574`

Current verifier:

```powershell
python scripts\verify_local_paper_rag_final_review_v1_1.py --root D:\devframe-system
```

Expected:

```text
PASS_LOCAL_PAPER_RAG_FINAL_REVIEW_V1_1_VERIFICATION
passed=109 failed=0
```

## Ten-Item Completion Board

### 1. Integration Superproject

Current state:

- Parent has pinned the current local paper RAG milestone evidence chain through
  test-frame and agent-acceptance.
- `CURRENT_DELIVERY.md` points to v1.1 review package.
- Parent still has unrelated dirty drift and historical report files that must
  not be mixed into closeout commits.

Still needed:

- Produce one final parent milestone report that says exactly what is current,
  what is not final, and what remains human-gated.
- Re-run parent verifiers after any v1.2 or final package update.
- Keep any pin/report commit scoped and separate from old dirty drift.

Parallel owner: Parent main thread.

Fast action:

- Create final closeout report after B/C/D lanes return.

Hard stop:

- Stop if `integration/lock/submodules.lock.yml` and gitlinks diverge for the
  current milestone modules.

### 2. Cross-Repo Contracts

Current state:

- opencode, test-frame, and agent-acceptance have established evidence package
  and non-final boundary contracts for current local RAG work.
- v1.1 package is parent-side and does not require new child runtime access.

Still needed:

- Record a final cross-repo contract summary for the current milestone:
  producer evidence, consumer evidence, governance review, parent pointer.
- Explicitly state that old Axx slices are closed unless a current P0/P1
  contradiction is rediscovered.

Parallel owner: Subagent A plus parent main thread.

Fast action:

- Summarize contracts in final parent closeout; avoid creating new schemas unless
  a verifier fails.

Hard stop:

- Stop if any child evidence hash in parent reports does not match the package on
  disk.

### 3. Opencode Adapter

Current state:

- Local paper RAG usable pipeline, quality eval, hybrid rerank, answer preview,
  Obsidian note pilot, FAISS pilot, PDF/WriteLab pilot, and manuscript package
  support have all returned as non-final evidence candidates.
- Latest currently pinned opencode in lock:
  `528f5b801082a10759df000a2315486a55a22e79`.

Still needed:

- No new opencode runtime slice is required for tonight unless a verifier or
  human review identifies a concrete blocker.
- Optional: one narrow v1.2 formatting/helper slice if target-specific output is
  requested.

Parallel owner: none by default; keep opencode quiet unless needed.

Fast action:

- Do not start broad whole-vault, cloud, external RAG, or new live-resource work
  before manuscript handoff closes.

Hard stop:

- Stop if new work would read raw private content or broaden RuntimeAuthorization
  without a fresh explicit TaskSpec.

### 4. Test-Frame Adapter / TestRunSpec

Current state:

- test-frame current closed-loop consumption is pinned in parent:
  `72c3150e89c6542054547bc5f092f38388be153c`.
- It covers usable pipeline, quality eval, hybrid rerank, and answer preview as
  verification evidence only.

Still needed:

- If v1.2 changes only parent-side manuscript packaging, no new test-frame slice
  is required.
- If v1.2 changes package/verifier semantics, add one focused parent-side
  verifier first; only dispatch test-frame if fail-closed cross-repo coverage is
  materially changed.

Parallel owner: Subagent D for governance check only.

Fast action:

- Keep test-frame idle unless a new runtime/evidence contract appears.

Hard stop:

- Stop if a new package allows final/paper-quality/production/RAG-ready claims.

### 5. Control-Plane State Machine Conformance

Current state:

- The parent lock includes `devframe-control-plane` at
  `09167bc656f8625c97bfae5c52dae5a0280b116c`.
- Current local paper RAG work did not require control-plane mutation.

Still needed:

- Record that current milestone does not expand the control-plane state machine.
- Defer deeper conformance unless the final parent closeout needs a formal state
  transition artifact.

Parallel owner: Subagent D.

Fast action:

- Treat as documentation closeout, not implementation.

Hard stop:

- Stop if a final report claims a state transition that the control-plane lock
  does not support.

### 6. Artifact Registry / Evidence Store

Current state:

- Evidence ZIPs exist for opencode, test-frame, and agent-acceptance current
  milestone slices.
- v1.1 final-review package is verified and has a stable SHA256.

Still needed:

- Make one final evidence index for tonight's current deliverables:
  v1.1 package, current verifier outputs, child evidence hashes, and known gaps.
- Do not include raw runtime artifacts or private content.

Parallel owner: Subagent A/C plus parent main thread.

Fast action:

- Append or create final evidence index only after subagent results return.

Hard stop:

- Stop if evidence package contains raw PDF text, raw Markdown body, raw chunks,
  raw query text, source paths, vectors, FAISS binaries, WriteLab payloads, API
  keys, Zotero credentials, browser/cloud payloads, or MiniApp runtime content.

### 7. RuntimeAuthorization Signer / Validator

Current state:

- RuntimeAuthorization boundaries exist for scoped pilots.
- Current v1.1 manuscript package does not request new runtime access.

Still needed:

- Record that no new RuntimeAuthorization is granted by v1.1 or final closeout.
- Defer signer/validator expansion unless a new live-resource step is requested.

Parallel owner: Subagent D.

Fast action:

- Keep runtime gate closed.

Hard stop:

- Stop if any report treats a pilot authorization as reusable broad access.

### 8. Source-Level Safety Review

Current state:

- v1.1 scripts and verifiers were added in parent and verified.
- Child governance reviews checked ZIP entry lists and boundaries without opening
  raw private content.

Still needed:

- Run a final safety grep over current delivery docs/scripts for forbidden
  overclaims and private/raw markers.
- Keep review scoped to current delivery files, not the whole dirty worktree.

Parallel owner: Subagent D plus parent main thread.

Fast action:

- Run current verifiers and targeted `rg` checks before final closeout commit.

Hard stop:

- Stop if final docs contain final acceptance, production-ready, broad RAG-ready,
  whole-vault-ready, or paper-quality acceptance claims.

### 9. Dry-Run End-to-End Harness

Current state:

- Local RAG pipeline has already proven first-run build and second-run reuse in
  opencode evidence.
- v1.1 parent package is verified by parent-side verifier.

Still needed:

- For tonight, one final parent dry-run should be:
  current delivery verifier + v1.0 compatibility verifier + submission prep
  verifier + review variants verifier.
- Do not rerun expensive live pilots unless a current artifact contradicts the
  verified state.

Parallel owner: Parent main thread.

Fast action:

```powershell
python scripts\verify_local_paper_rag_final_review_v1_1.py --root D:\devframe-system
python scripts\verify_local_paper_rag_v1_0_handoff.py --root D:\devframe-system
python scripts\verify_local_paper_rag_submission_prep_v1_0.py --root D:\devframe-system
python scripts\verify_local_paper_rag_review_variants_v1_0.py --root D:\devframe-system
```

Hard stop:

- Stop on any verifier failure; do not downgrade checks to make them pass.

### 10. Canary Repo + Rollback Drill

Current state:

- `order-dish` rdtest work exists as separate evidence, not part of the current
  local paper RAG closeout.
- No production deploy or canary rollout is required for the paper RAG manuscript
  handoff.

Still needed:

- Record canary/rollback as out of scope for tonight's paper RAG closeout unless
  the user switches to `/rdtest` or MiniApp delivery.
- For paper RAG, rollback is git-level: revert the final parent closeout commit
  and continue using v1.1 package as previous known-good artifact.

Parallel owner: none.

Fast action:

- Do not mix MiniApp canary into paper RAG closeout.

Hard stop:

- Stop if a report combines unrelated MiniApp runtime acceptance with paper RAG
  acceptance.

## Parallel Execution Map

### Lane A: Parent Closeout / Contract Index

Owner: parent main thread + Subagent A.

Deliverables:

- final parent closeout report;
- final evidence index;
- contract summary across opencode, test-frame, agent-acceptance.

Acceptance:

- exact commit/hash paths listed;
- old dirty drift isolated;
- no unrelated runtime-pilot artifacts staged.

### Lane B: Manuscript / Submission Candidate

Owner: Subagent B, then parent main thread if automation is needed.

Deliverables:

- decision-ready manuscript route summary;
- optional v1.2 GB/T-style candidate package if no target venue is provided;
- reference metadata human-check list.

Acceptance:

- no internal workflow terms in article body;
- cautious evidence boundary preserved;
- reference formatting marked as candidate unless metadata is manually checked.

### Lane C: Local RAG Usability

Owner: Subagent C.

Deliverables:

- one-page user operation flow:
  PDF folder -> Markdown -> FAISS -> retrieval -> answer preview -> quality eval;
- list of commands or wrappers that already exist;
- list of only the missing ergonomic items.

Acceptance:

- no raw/private content opened;
- no production or general-RAG claim;
- repeat-run reuse remains documented.

### Lane D: Governance / Safety Gate

Owner: Subagent D.

Deliverables:

- P0/P1 hard-stop checklist for final closeout;
- targeted safety scan recommendation;
- RuntimeAuthorization non-expansion statement.

Acceptance:

- final closeout cannot imply final governance acceptance, paper-quality
  acceptance, production readiness, broad/general RAG readiness, whole-vault
  readiness, cloud/vector DB readiness, or RuntimeAuthorization.

## Immediate Critical Path

1. Subagents A-D run read-only audits in parallel.
2. Parent main thread creates this fast closeout plan.
3. Parent main thread runs current verifiers.
4. Incorporate only high-signal subagent findings.
5. Produce final parent closeout report.
6. Commit scoped parent files only.

## What Must Be Human-Decided

These cannot be honestly automated into completion:

- whether the manuscript is a short paper, technical note, internal brief, or
  target-specific submission;
- whether the paper's academic quality is sufficient;
- whether reference metadata is fully correct for a real venue;
- whether training-effect claims should be strengthened by new empirical data.

## Practical Tonight Target

Recommended target:

`CURRENT_LOCAL_PAPER_RAG_HANDOFF_READY_FOR_HUMAN_REVIEW`

Meaning:

- workflow evidence is closed enough for a milestone;
- v1.1 paper package is ready for human review;
- no final acceptance is claimed;
- next work is either human manuscript review or target-venue formatting.
