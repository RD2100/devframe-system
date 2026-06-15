# TaskSpec: AGENT_ACCEPTANCE_A11_CROSS_MODULE_SMOKE

task_id: `agent-acceptance-a11-cross-module-smoke`

owner_module: `agent-acceptance`

source_parent_commit: `24ee242`

## Goal

Perform a read-only governance smoke review for the current `devframe-system`
A11 parent state.

Confirm that the parent gitlinks, lock files, and intake evidence do not allow
offline/local candidate evidence to be mistaken for final acceptance.

## Scope

Read-only inputs:

- parent repo: `D:\devframe-system`
- parent commit: `24ee242 Record A11 post-pin status`
- `BASELINE_LOCK.json`
- `integration/lock/submodules.lock.yml`
- `integration/reports/post-pin-status-a11-2026-06-15.md`
- `integration/reports/grouped-parent-pin-a11-2026-06-15.md`
- `integration/reports/opencode-zotero-evidence-manifest-schema-return-review-2026-06-15.md`
- `integration/reports/grouped-parent-pin-a10-2026-06-15.md`

Expected pinned heads:

- `agent-acceptance`: `b9bb53a72bbd7b4c4e4402aca11b4cc67f9506f5`
- `dev-frame-opencode`: `f9d381c0f8e974f1dd36642e1e412dfb2581ad5a`
- `devframe-control-plane`: `79399541b8426cff0f362b665bad09e3c23e974b`
- `test-frame`: `c3353fb34900aa24f56df5b9c9230f3249d6c01a`

## Allowed Actions

- Read files.
- Run local read-only git/status/diff commands.
- Run existing local validators if they do not mutate files.
- Produce module-local evidence and report artifacts under an approved
  module-local evidence path.

## Forbidden Actions

- Do not modify parent files.
- Do not update submodule pins.
- Do not push.
- Do not reset, clean, stash, or remove untracked evidence.
- Do not start real Zotero, Obsidian, RAG, WriteLab, MiniApp, browser/CDP,
  cloud, Android, H5, MeterSphere, or other live runtime.
- Do not claim final acceptance.

## Checks Required

1. Parent gitlink check:
   - `git ls-tree HEAD agent-acceptance dev-frame-opencode devframe-control-plane test-frame`
   - Expected: matches the four A11 pinned heads above.

2. Lock file check:
   - `BASELINE_LOCK.json`
   - `integration/lock/submodules.lock.yml`
   - Expected: both reference the same four A11 pinned heads.

3. Boundary check:
   - A11 reports must state local/offline/synthetic candidate scope.
   - A11 reports must not state live-ready or final-ready.
   - `final acceptance` must remain gated by acceptance governance, not by
     test-frame, ZIP evidence, parent pin, or opencode report.

4. Dirty-state interpretation:
   - Parent status may show `? agent-acceptance` due older untracked evidence
     inside the submodule.
   - Expected: report this as untracked evidence note, not parent gitlink drift.

## Expected Output

Return a concise final report with:

- status;
- branch;
- commit/hash reviewed;
- commands run;
- files/reports reviewed;
- Reviewer Index;
- findings;
- known gaps;
- dirty state;
- final verdict limited to local read-only smoke.

## Acceptance Criteria

- PASS only if all A11 pin/lock references match.
- PASS only if no report promotes offline/local evidence to final acceptance.
- BLOCKED if parent files are missing or unreadable.
- FAILED if pin/lock mismatch is found.
- FAILED if final acceptance is claimed from local/offline evidence.

## Boundary

This TaskSpec is read-only and local. It does not authorize real runtime or
private data access.
