# Current Local Paper RAG Remaining Work Concurrent Plan

Date: 2026-06-16

Status: `ACTIVE_FAST_CLOSEOUT_PLAN`

## Objective

Finish the current local paper RAG milestone fast, without reopening every old
Axx slice. The target is a usable, reviewable, locally verified paper-support
workflow:

PDF corpus -> Markdown/Obsidian material -> local FAISS RAG -> quality checks ->
hybrid rerank -> answer preview -> manuscript/variants -> parent closeout.

This plan is explicitly non-final. It does not grant paper-quality acceptance,
training-effect acceptance, production readiness, broad/general RAG readiness,
whole-vault readiness, cloud/vector DB readiness, or RuntimeAuthorization.

## Already Done

Parent-superproject current artifacts:

- v1.0 main manuscript handoff is available.
- submission-prep supplement is available.
- short-paper, technical-note, and internal-brief variants are generated.
- review-variants package is verified:
  `PASS_LOCAL_PAPER_RAG_REVIEW_VARIANTS_V1_0_VERIFICATION`, 79 passed, 0 failed.
- current parent closeout report exists:
  `integration/reports/parent-current-local-paper-rag-milestone-closeout-a1-2026-06-16.md`.
- current evidence index exists:
  `integration/reports/current-local-paper-rag-evidence-index-draft-2026-06-16.md`.

Latest local RAG evidence already available from opencode:

- usable pipeline;
- quality eval;
- hybrid rerank;
- answer preview.

## Remaining Work

### R1. Test-Frame Current Closed-Loop Consumption

Owner: test-frame worker

Goal:

- consume the latest current closed-loop evidence as minimized verification
  evidence;
- verify usable pipeline, quality eval, hybrid rerank, and answer preview as one
  current milestone;
- reject raw/private leakage and final/live/production/RAG-ready overclaims.

Expected output:

- test-frame commit;
- evidence ZIP path and SHA256;
- focused tests and regression summary;
- boundary confirmation.

Human blocker:

- none expected unless fixture/source facts contradict current parent evidence.

### R2. Agent-Acceptance Current Milestone Governance

Owner: agent-acceptance worker

Goal:

- review current milestone as non-final candidate;
- verify hashes and ZIP entry lists only;
- confirm no promotion to final governance acceptance, paper-quality acceptance,
  production readiness, broad RAG readiness, whole-vault readiness, cloud/vector
  DB readiness, or RuntimeAuthorization.

Expected output:

- agent-acceptance commit;
- governance review;
- ExecutionReport;
- Reviewer Index;
- evidence ZIP and SHA256.

Human blocker:

- none expected unless governance finds P0/P1 boundary violation.

### R3. Parent Intake / Pin

Owner: parent thread

Goal:

- after R1 and R2 commits exist, review and pin them separately;
- keep test-frame and agent-acceptance pin commits separate;
- avoid mixing unrelated dirty drift into those commits.

Expected output:

- one parent pin commit for test-frame, if accepted;
- one parent pin commit for agent-acceptance, if accepted;
- updated parent report(s) with exact commit hashes and evidence hashes.

Human blocker:

- only if a submodule return is missing evidence, has a hash mismatch, or crosses
  scope boundary.

### R4. Human Paper Review

Owner: user / human reviewer

Goal:

- choose the intended form:
  - short paper;
  - technical note;
  - internal research brief;
  - formal submission candidate after additional formatting.
- inspect the selected DOCX;
- decide whether the cautious training-effect boundary is acceptable.

Expected output:

- selected target form;
- required edits, if any;
- decision whether reference formatting needs a target-venue pass.

Human blocker:

- unavoidable. Paper quality and target use case cannot be honestly automated
  into final acceptance.

### R5. Optional Target-Venue Formatting Pass

Owner: parent/opencode later task, only after R4 decision

Goal:

- convert the chosen manuscript into target-specific style, likely GB/T 7714 or
  target journal format;
- manually confirm reference metadata that automation cannot infer.

Expected output:

- target-formatted DOCX/MD;
- format audit;
- updated package.

Human blocker:

- target venue and reference metadata.

## Fast Sequencing

1. Do not wait on old Axx tasks unless they affect current closed-loop evidence.
2. Finish R1 and R2 in parallel.
3. Parent pins R1/R2 separately if accepted.
4. Parent emits final current-milestone status.
5. User picks manuscript form and review direction.

## Hard Stops

Stop and return findings if any worker observes:

- raw PDF text, raw Markdown body, raw chunks, raw query, source paths, vectors,
  FAISS binaries, WriteLab payloads, API keys, Zotero credentials, browser/cloud
  payloads, or MiniApp runtime content inside evidence packages;
- final acceptance, paper-quality acceptance, production-ready, broad RAG-ready,
  whole-vault-ready, or RuntimeAuthorization claims;
- evidence ZIP hash mismatch;
- missing task-specific evidence;
- submodule worktree changes outside the scoped task.

## Current Practical Recommendation

Treat the current state as good enough for a human-review handoff once R1 and R2
are pinned or recorded as non-blocking. The only required human decision after
that is which manuscript form to use.
