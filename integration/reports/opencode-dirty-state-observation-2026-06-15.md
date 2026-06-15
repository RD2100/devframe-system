# devframe-system Observation: dev-frame-opencode Dirty State

Date: 2026-06-15
Scope: parent observation only
Runtime: not executed
Verdict: `OPENCODE_RETURN_ACCEPTED_BUT_CURRENT_DIRTY_AGAIN`

## 1. Current Observed State

Module:

- `dev-frame-opencode`

Branch:

- `codex/paper-audit-privacy-hard-gate`

Initial observed HEAD:

- `77f558dcc5d17a974cb835b5715204ef38386eb1`
- Recent commit: `77f558d Add real Zotero metadata-only pilot entrypoint`

Tracked dirty files:

- `ai-workflow-hub/src/ai_workflow_hub/context_layer/adapters/zotero_metadata_real_pilot.py`
- `ai-workflow-hub/tests/test_paper_real_zotero_metadata_only_pilot.py`
- `schemas/paper_real_zotero_metadata_only_pilot_report.schema.json`

## 2. Parent Diff Observation

The parent inspected the current diff summary.

Observed direction:

- Add `metadata_format_detected` to the report schema.
- Detect and support metadata-only JSON variants:
  - Better BibTeX JSON;
  - CSL JSON;
  - Zotero API JSON;
  - generic Zotero metadata JSON.
- Detect but fail closed on unsupported text formats:
  - BibTeX;
  - RDF/XML.
- Expand forbidden metadata fields to include common private or full-text leak
  vectors such as notes, annotations, abstract, attachment path, local library
  path, storage, URI, file path, and full text fields.

Parent interpretation:

- This appears aligned with local metadata-only hardening.
- It is still uncommitted tracked dirty state.
- It is not parent-ready until the module returns tests, evidence, and boundary
  confirmation.

## 3. Thread Observation

The parent inspected the existing `dev-frame-opencode` thread:

- Thread: `019ec6c5-7d65-76e2-b9a6-9316c75aeae8`
- Status: in progress.
- The child thread stated it is continuing a no-plugin, no-real-data local
  slice for Zotero metadata export compatibility and sensitive-field
  fail-closed hardening.
- The child thread later reported that `metadata_format_detected` was tightened
  to a known enum in the schema.
- The child thread was last observed preparing documentation for the supported
  JSON / unsupported BibTeX-RDF boundary.
- The child thread then updated
  `ai-workflow-hub/docs/paper/PAPER_REAL_ZOTERO_METADATA_ONLY_PILOT.md`.
- The child thread reported the core metadata-only pilot tests passed:
  `13 passed`.
- After the parent closure reminder, the child confirmed it would finish
  checks, commit locally, confirm dirty state, and return a pin-review report.
- The child reported `git diff --check` exit 0 with Windows line-ending
  warnings only.
- The child reported the diff was limited to 4 hardening files, staged them,
  and was last observed starting the local commit.
- The child then reported a successful commit and a clean worktree at
  `9d4c2f6...`.
- Parent independently verified:
  - HEAD: `9d4c2f62c636d91641c5843c43eaa896fbba5243`;
  - worktree clean;
  - commit title: `Harden Zotero metadata export pilot parsing`;
  - changed files: 4.
- The child was last observed generating a local ZIP evidence pack for parent
  pin review.
- Final return was received with status
  `PASS_LOCAL_OFFLINE / PARENT_PIN_REVIEW_READY`.
- Parent verified evidence ZIP, ExecutionReport, Reviewer Index, clean
  submodule worktree, and commit `9d4c2f62c636d91641c5843c43eaa896fbba5243`.
- Parent intake review:
  `integration/reports/opencode-zotero-metadata-export-hardening-return-review-2026-06-15.md`.
- The child thread explicitly framed real Zotero export execution as a TODO for
  later human availability.

## 4. Parent Boundary

This observation does not authorize:

- real Zotero plugin installation;
- real Zotero API access;
- real Obsidian/RAG/WriteLab/private paper content;
- browser/CDP/cloud runtime;
- parent pin or lock mutation;
- final readiness claim.

## 5. Parent Decision

Parent decision:

- Do not dispatch a duplicate task.
- Accept the return for intake.
- Do not pin without explicit approval.
- Keep pin decision as `NO-GO_FOR_PIN`.
- Parent sent a closure reminder asking the active thread to return status, commit,
  tests, changed files, artifacts, Reviewer Index, known gaps, and dirty-state
  status before any real Zotero/plugin/API work.

Required return before parent pin review can continue:

- final commit or explicit BLOCKED status;
- tests run;
- schema validation evidence;
- privacy/redaction evidence;
- no real resource execution confirmation;
- Reviewer Index and known gaps.

## 6. Post-A2 Update

After `parent-pin-review-a2-2026-06-15.md`, the parent performed a fresh
read-only status check.

Observed current state:

- HEAD remains `9d4c2f62c636d91641c5843c43eaa896fbba5243`.
- Worktree is dirty again.
- Dirty tracked files:
  - `ai-workflow-hub/docs/paper/PAPER_REAL_ZOTERO_METADATA_ONLY_PILOT.md`
  - `ai-workflow-hub/src/ai_workflow_hub/context_layer/adapters/zotero_metadata_real_pilot.py`
  - `ai-workflow-hub/tests/test_paper_real_zotero_metadata_only_pilot.py`
- Diff summary: 225 insertions and 22 deletions.

Parent interpretation:

- The prior return remains accepted for intake.
- The current dirty state is new active drift.
- Parent pin readiness is suspended until the new drift is closed by a final
  module return or explicit coordinator/human instruction.

Latest parent pin review:

- `integration/reports/parent-pin-review-a3-2026-06-15.md`

## 7. Post-A4 Update

After A3, `dev-frame-opencode` advanced to:

- HEAD: `3b2e4ae Support safe BibTeX metadata pilot exports`

The module then started a new local-only RIS metadata export parser slice and
became dirty again.

Current observed dirty files:

- `ai-workflow-hub/docs/paper/PAPER_REAL_ZOTERO_METADATA_ONLY_PILOT.md`
- `ai-workflow-hub/src/ai_workflow_hub/context_layer/adapters/zotero_metadata_real_pilot.py`
- `ai-workflow-hub/tests/test_paper_real_zotero_metadata_only_pilot.py`
- `schemas/paper_real_zotero_metadata_only_pilot_report.schema.json`

Parent interpretation:

- `3b2e4ae...` is observed, not parent-intake accepted.
- RIS slice is active self-iteration.
- Parent pin readiness remains no-go.

Latest parent pin review:

- `integration/reports/parent-pin-review-a4-2026-06-15.md`
