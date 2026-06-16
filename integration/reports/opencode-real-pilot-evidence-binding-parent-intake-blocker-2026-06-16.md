# Opencode Real Pilot Evidence Binding Parent Intake Blocker

Date: 2026-06-16
Parent repo: `D:\devframe-system`
Status: `BLOCKED_FOR_PARENT_PIN`

## Reviewed Return

Module:

- `dev-frame-opencode`

Candidate commit:

- `13403c3ddac5b70d6d1cdddb965b4c4e1cc1e476`
- message: `Bind paper real pilot evidence in business validation`

Parent baseline before candidate:

- `a914e5da642b0aa9484e877cabf5de553d5a7379`

Evidence ZIP:

- `D:\devframe-system\.agent\evidence\evidence-opencode-business-validation-real-pilot-evidence-binding-a1.zip`
- SHA256 observed: `2B1F0D71B77B0E568E7132770E33038C98BEFEFE3865DD6E1399843B1769BF2A`

## Parent-side Checks

Checks run:

- `git -C dev-frame-opencode log --oneline a914e5d..13403c3`
- `git -C dev-frame-opencode diff --name-status a914e5d..13403c3`
- `git -C dev-frame-opencode status --short --branch`
- `Get-FileHash ...evidence-opencode-business-validation-real-pilot-evidence-binding-a1.zip -Algorithm SHA256`
- `python -m zipfile -l ...evidence-opencode-business-validation-real-pilot-evidence-binding-a1.zip`

Observed:

- candidate commit exists;
- evidence ZIP exists;
- evidence ZIP SHA256 matches the declared value;
- ZIP contains expected report/command/reviewer artifacts;
- submodule working tree is not clean.

## Blocker

Parent pin is blocked because the opencode submodule has an untracked file:

`ai-workflow-hub/src/ai_workflow_hub/context_layer/adapters/paper_pdf_writelab_live_pilot.py`

This file is not part of commit `13403c3ddac5b70d6d1cdddb965b4c4e1cc1e476`.

The parent cannot safely pin the submodule while uncommitted child drift is
present, because the checkout state may not match the reviewed commit.

## Required Rework

Opencode must do one of:

1. commit the file in a new scoped TaskSpec and return evidence; or
2. remove/ignore it under module policy and return a clean worktree; or
3. explain why the untracked file is unrelated and provide a clean canonical
   checkout for parent review.

The parent will not clean, reset, stash, delete, or stage this child file.

## Boundary

This blocker report does not:

- parent-pin opencode;
- modify submodule lock;
- accept PDF/WriteLab/Obsidian/RAG/plugin runtime evidence;
- claim final governance acceptance;
- claim production-ready or live-ready status.

## Current Verdict

`BLOCKED_FOR_PARENT_PIN_PENDING_OPENCODE_CLEAN_WORKTREE`
