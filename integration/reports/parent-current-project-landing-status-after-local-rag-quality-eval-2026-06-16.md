# Parent Current Project Landing Status After Local RAG Quality Eval

Date: 2026-06-16

## Executive Status

Status: `PRACTICAL_LOCAL_PAPER_RAG_MILESTONE_CANDIDATE`

The parent superproject now pins a complete local paper RAG evidence chain through quality evaluation:

- `dev-frame-opencode`: `44188cdb627e571bed55b20fe4f8d71d2d0828c1`
- `test-frame`: lock target `9d91a7f7ae1dcfca0c8b6be362ebb3691e3e8528`
- `agent-acceptance`: `41258e8fc041eda1063eb65ecb300f80f2298534`
- `devframe-control-plane`: `09167bc656f8625c97bfae5c52dae5a0280b116c`

The current local paper workflow has progressed from isolated pilots into a usable local loop:

1. convert local PDFs into Markdown notes;
2. build/reuse a local FAISS index;
3. run retrieval probes;
4. produce minimized quality-eval signals;
5. verify evidence shape and fail-closed cases in test-frame;
6. review the chain in agent-acceptance;
7. close the milestone in the parent.

This is still not final governance acceptance, paper-quality acceptance, production readiness, broad live readiness, whole-vault readiness, general RAG readiness, external/private RAG readiness, cloud readiness, or RuntimeAuthorization.

## Evidence Chain

| Layer | Parent Evidence | Result |
|---|---|---|
| opencode local RAG closed loop | `b7cb4e8`, `81e3a60` | scoped PDF-to-Markdown-to-FAISS-to-retrieval pilot closed |
| opencode usable RAG pipeline | `ffc571c`, `4e1fac8` | repeatable first-run build plus second-run index reuse closed |
| opencode quality eval | `ca9d270`, `fd74422` | deterministic quality gate closed as non-final milestone |
| test-frame consumption | `0becd6b`, `9873363`, `03fa31d` | fail-closed verification for closed loop, usable pipeline, and quality eval |
| agent-acceptance review | `6668f12`, `6d3bc8c`, `1cea349` | governance review accepted each as non-final milestone candidate |

Latest closeout report:

- `integration/reports/parent-current-local-paper-rag-quality-eval-milestone-closeout-2026-06-16.md`

## Ten-Part Landing Standard

### 1. Integration Superproject

Status: `MOSTLY_DONE_WITH_DIRTY_WORKTREE_CAVEAT`

What is done:

- Parent pins the current RAG quality-eval chain in `BASELINE_LOCK.json` and `integration/lock/submodules.lock.yml`.
- Parent has explicit intake reports and closeout reports for opencode, test-frame, and agent-acceptance.

Remaining:

- Parent worktree still contains unrelated historical drift, including `.agent/PROJECT_REGISTRY.json`, `test-frame` checkout drift, and older report/index changes. These are not part of the current RAG quality-eval closeout.
- Parent branch is ahead of origin and has not been pushed in this workflow.

### 2. Cross-Repo Contracts

Status: `DONE_FOR_CURRENT_LOCAL_RAG_SCOPE`

What is done:

- Evidence remains separated by producer: opencode implementation, test-frame verification, agent-acceptance governance, parent pin/closeout.
- Reports preserve the boundary that no child module can self-promote to final acceptance.
- The current quality-eval chain has source hashes, report paths, and parent pins.

Remaining:

- Cross-repo contracts for broader whole-vault RAG, private/external RAG, cloud vector DB, and production release remain out of scope.

### 3. Opencode Adapter

Status: `DONE_FOR_LOCAL_PAPER_RAG_MVP`

What is done:

- Zotero metadata-only evidence, PDF/WriteLab scoped pilot, Obsidian allowlisted-note pilot, local FAISS pilot, local closed-loop RAG, usable local RAG pipeline, and deterministic quality eval all have opencode evidence.
- Latest quality eval facts include 6 documents, 47 chunks, 3 queries, 3 retrieval successes, coverage ratio 1.0, 9 top-k mappings, and zero empty/duplicate/low-confidence/unknown-source/warning signals.

Remaining:

- No paper-quality acceptance.
- No whole-vault indexing.
- No external/private RAG service.
- No cloud vector DB.
- No production runtime claim.

### 4. Test-Frame Adapter / TestRunSpec

Status: `DONE_FOR_CURRENT_LOCAL_RAG_SCOPE`

What is done:

- test-frame verifies minimized evidence consumption for local RAG closed loop, usable pipeline, and quality eval.
- Negative cases cover raw-sensitive markers, provenance drift, runtime expansion, final/live/production/RAG-ready overclaims, and quality-signal degradation.

Remaining:

- The visible `test-frame` checkout is ahead of the locked commit. Current parent lock intentionally points to `9d91a7f7ae1dcfca0c8b6be362ebb3691e3e8528`; later local drift should be reviewed separately or reset only with explicit approval.

### 5. Control-Plane State Machine Conformance

Status: `STABLE_BUT_NOT_RETESTED_IN_THIS_RAG_SLICE`

What is done:

- Parent pins `devframe-control-plane` at `09167bc656f8625c97bfae5c52dae5a0280b116c`, previously accepted as verifier-failure fail-closed evidence.

Remaining:

- The RAG quality-eval path did not exercise a live control-plane dispatch or worker state machine.
- If final product acceptance requires control-plane runtime orchestration, run a scoped conformance smoke later.

### 6. Artifact Registry / Evidence Store

Status: `DONE_FOR_CURRENT_EVIDENCE_CHAIN`

What is done:

- Evidence ZIPs exist under `.agent/evidence` or module report directories.
- Parent reports record ZIP paths and SHA256 hashes.
- Runtime artifacts are intentionally excluded from evidence ZIPs when they may contain raw content, vectors, or local paths.

Remaining:

- `.agent/PROJECT_REGISTRY.json` is still local runtime/workspace drift and was intentionally not committed.
- A cleaner final index page could still be generated for human navigation, but the core evidence chain is present.

### 7. RuntimeAuthorization Signer / Validator

Status: `PARTIAL_AND_SCOPE_BOUND`

What is done:

- RuntimeAuthorization boundaries exist in prior pilots and reports.
- Current RAG quality eval does not require or grant new RuntimeAuthorization.

Remaining:

- No broad runtime authorization exists for whole-vault, external/private RAG, cloud services, production, or unrestricted PDF/full-text access.
- Final acceptance must not infer authorization from local quality-eval success.

### 8. Source-Level Safety Review

Status: `DONE_FOR_CURRENT_CHAIN_AS_GOVERNANCE_REVIEW`

What is done:

- agent-acceptance reviewed the chain and accepted it only as a non-final milestone candidate.
- Parent verified hashes and entry lists without inspecting raw/private content.
- Reports preserve raw-content, final-acceptance, and runtime-expansion boundaries.

Remaining:

- No independent full code security audit of every opencode/test-frame change in the whole day is claimed by this closeout.

### 9. Dry-Run End-to-End Harness

Status: `DONE_FOR_LOCAL_PAPER_RAG_MVP`

What is done:

- The local RAG pipeline has first-run and rerun evidence.
- First run builds the index; second run reuses it.
- Quality eval consumes minimized pipeline facts and passes deterministic gates.

Remaining:

- No broad user-facing UI or production service harness is claimed.
- No whole-vault or cloud RAG E2E is claimed.

### 10. Canary Repo + Rollback Drill

Status: `PARTIAL`

What is done:

- There is separate rdtest/order-dish dry-run evidence for external project intake.
- Parent has repeated pin-only commits that provide straightforward Git rollback points.

Remaining:

- No dedicated rollback drill for the local paper RAG milestone has been executed.
- No production canary deployment exists.

## Practical Go / No-Go

### Go

It is reasonable to use the current system as a local, scoped paper RAG milestone candidate for:

- local PDF corpus ingestion into Markdown;
- local FAISS indexing and reuse;
- retrieval probes;
- deterministic quality-signal checks;
- evidence-backed parent review;
- human spot-check preparation.

### No-Go

Do not claim:

- final governance acceptance;
- paper-quality acceptance;
- production readiness;
- whole-vault readiness;
- external/private RAG readiness;
- cloud/vector DB readiness;
- broad live runtime authorization;
- RuntimeAuthorization.

## Recommended Next Moves For Tonight

Priority 1: human-facing usability check.

- Select 3 to 5 concrete questions over the current PDF corpus.
- Run or inspect the local RAG output through the existing pipeline.
- Record whether the answer is useful, whether sources are plausible, and whether retrieval misses anything obvious.
- This should be a spot-check, not another schema-hardening pass.

Priority 2: parent final readiness packet.

- Produce one concise parent packet that links:
  - current lock commits;
  - RAG closeout;
  - quality-eval closeout;
  - known non-final gaps;
  - commands for a human to reproduce the local pipeline.

Priority 3: optional rollback drill.

- Record exact rollback command targets for the last three parent milestones.
- Do not execute destructive rollback unless explicitly approved.

## Reviewer Index

- changed files:
  - `integration/reports/parent-current-project-landing-status-after-local-rag-quality-eval-2026-06-16.md`
- critical code paths: none; parent status/report only.
- tests/probes run:
  - `git submodule status --recursive`
  - parent log and lock inspection
  - local RAG report inventory inspection
- generated artifacts:
  - this current landing status report
- known gaps:
  - no runtime reproduction in this report
  - no raw/private content inspection
  - existing unrelated parent worktree drift remains
- suggested review focus:
  - confirm the ten-part landing standard is accurate
  - confirm non-final boundary remains explicit
  - use this report to choose the next real execution task instead of more low-yield schema hardening
