# Current Local Paper RAG Remaining Work Concurrent Plan

Date: 2026-06-16

Status: `R1_R2_R3_PINNED_WAITING_HUMAN_REVIEW`

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

Closeout pins completed after this plan was opened:

- agent-acceptance governance review pinned in parent commit
  `6356fd1 Pin agent-acceptance current local paper RAG governance`.
- test-frame current closed-loop consumption pinned in parent commit
  `fbe26a4 Pin test-frame current local paper RAG closeout consumption`.
- parent lock now records:
  - `agent-acceptance` commit
    `2e0bd5633eaca20bd0124dd22b7dd6d8702325b1`;
  - `test-frame` commit
    `72c3150e89c6542054547bc5f092f38388be153c`;
  - `dev-frame-opencode` commit
    `528f5b801082a10759df000a2315486a55a22e79`.

Final-review package completed after the closeout pins:

- v1.1 final-review package:
  `integration/artifacts/paper-drafts/local-paper-rag-review-variants-v1.1-package.zip`
- SHA256:
  `2731FE77DB74BBDF29822AFEB401B25B09431FC93D942C44B1080884918AC574`
- Verification:
  `PASS_LOCAL_PAPER_RAG_FINAL_REVIEW_V1_1_VERIFICATION`, 109 passed, 0 failed.

## Remaining Work

### R1. Test-Frame Current Closed-Loop Consumption

Owner: test-frame worker

Status: `DONE_AND_PARENT_PINNED`

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

Status: `DONE_AND_PARENT_PINNED`

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

Status: `DONE`

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

Status: `NEXT_REQUIRED_DECISION_AFTER_V1_1_HANDOFF`

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

Status: `OPTIONAL_AFTER_R4`

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

1. Treat old Axx tasks as closed for the current local-paper-RAG milestone unless
   a specific blocker is rediscovered.
2. Do not start new runtime expansion before the manuscript decision.
3. User picks manuscript form and review direction.
4. If a target venue is chosen, run a focused formatting/reference pass.
5. If no target venue is chosen, preserve the three generated variants as the
   current handoff package.

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

Treat the current state as good enough for a human-review handoff. Open
`local-paper-rag-short-paper-v1.1.docx` first unless a technical-note or internal
brief route is already preferred. The only required next decision is which
manuscript form to use:

- short paper;
- technical note;
- internal research brief;
- or target-specific submission candidate.
