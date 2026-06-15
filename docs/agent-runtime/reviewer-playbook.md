# Reviewer Playbook -- RD2100 Agent Runtime v2

> Batch D4, 2026-05-27
> Purpose: give reviewers a deterministic process for judging execution reports, batch outputs, and phase gates.
> Scope: Phase 0-5 bootstrap assets plus Phase 6 Source Lock review planning.

## 1. Reviewer Role

The reviewer is the gate owner. The executor may submit evidence, summaries, and recommendations, but the executor must not self-approve a GateResult.

Primary reviewer duties:

1. Confirm the report matches the batch scope.
2. Confirm changed files are inside approved outputs.
3. Confirm pre/post git status supports the claimed delta.
4. Detect fake green reports.
5. Enforce P0 hard stops from `runtime-invariants.md`.
6. Decide `pass_to_review`, `needs_revision`, `blocked`, or `human_required`.

## 2. Required Reference Order

Review in this order:

1. `AGENTS.md`
2. `docs/agent-runtime/source-of-truth-decision.md`
3. `docs/agent-runtime/verification-gates.md`
4. `docs/agent-runtime/runtime-invariants.md`
5. `docs/agent-runtime/negative-acceptance-tests.md`
6. `docs/agent-runtime/tool-policy.md`
7. `docs/agent-runtime/integration-contracts.md`
8. `schemas/agent-runtime/README.md`

For Phase 6 review, also read:

1. `docs/agent-runtime/phase-6-source-lock-quarantine.md`
2. `schemas/agent-runtime/source-lock-record.schema.json`
3. `skills-inbox/quarantine/README.md`
4. `skills-inbox/allowlist.example.json`

## 3. Ten-Step Review Flow

### Step 1: Identify the Batch

Record:

- Batch ID: Batch A / Batch B / Batch C / Batch D / Phase 6
- Claimed status
- Claimed approved output paths
- Claimed changed files
- Claimed skipped or blocked validations

If the report mixes outputs from multiple batches without approval, decision is `needs_revision` or `blocked` depending on changed files.

### Step 2: Verify Source of Truth

Expected canonical root:

```text
D:\devframe-system
```

Rules:

- Batch A may propose source of truth.
- Batch B/C/D require the approved canonical root.
- Phase 6 requires the approved canonical root plus allowlist approval.

Decision:

- Wrong canonical root: `blocked`
- Missing source_of_truth_ref in a modifying batch: `needs_revision`
- Multiple roots with no decision: `human_required`

### Step 3: Verify Pre-Batch Git Status

The report must include:

- Command: `git status --short`
- CWD: `D:\devframe-system`
- Existing dirty files
- Existing untracked files

Decision:

- Missing pre-status before writes: `blocked`
- Pre-status after writes only: `human_required`
- Pre-status present but no CWD: `needs_revision`

### Step 4: Verify Post-Batch Git Status

For modifying batches, the report must include post-status.

Check:

- Modified baseline files are unchanged unless explicitly authorized.
- New files are only under approved output paths.
- No unexpected directories appeared.
- No generated logs, caches, lockfiles, temp files, or downloaded source appeared.

Decision:

- Missing post-status: `blocked`
- Unexpected changed files: `blocked`
- Ambiguous dirty attribution: `human_required`

### Step 5: Compare Approved Outputs

For every changed file, classify:

```text
approved_output
existing_dirty_unchanged
unexpected_changed_file
forbidden_path
```

Forbidden paths in Phase 0-5 include:

- `scripts/`
- `agent-workqueue/`
- `.claude/`
- `.codegraph/`
- global or project memory
- MCP configuration
- `.git/hooks`
- external source clones
- package lockfiles

Decision:

- Any `forbidden_path`: `blocked`
- Any `unexpected_changed_file`: `blocked` or `human_required`
- Approved outputs only: continue

### Step 6: Audit Commands

Each command must include:

- command
- CWD
- result
- exit code or clear result classification
- short output summary

Forbidden command classes:

- `git clone`, `git pull`, `git fetch`, submodule update
- `npm install`, `npm ci`, `pip install`, `yarn add`, `pnpm install`
- remote script execution
- unauthorized hook registration (pre-edit is authorized; other 4 require human gate)
- MCP config mutation
- UI-TARS or real desktop automation
- dangerous git mutation
- secret file reads

Decision:

- Forbidden command executed: `blocked`
- Unknown command omitted from audit: `needs_revision`
- Script missing but reported pass: `blocked`

### Step 7: Validate Artifacts

For every artifact:

- Confirm the path exists.
- Confirm it is in approved output paths.
- Confirm the purpose matches the batch.
- Confirm schema or JSON fixtures are valid JSON when applicable.
- Confirm Markdown assets do not contradict active Phase 0-5 policy.

Decision:

- Missing required artifact: `needs_revision`
- Artifact outside approved output paths: `blocked`
- Artifact contradicts P0 policy: `blocked`

### Step 8: Run Domain Checks

Use these checks by batch:

- Contract assets: compare against `integration-contracts.md` and `schemas/agent-runtime/*.schema.json`.
- Runtime rules: compare against `rules/README.md` priority model.
- Hooks: confirm `*.audit.draft.ps1`, audit-only header, no mutation, no registration, `exit 0`.
- Skill intake: confirm `reference_only`, `candidate`, `defer`, or `reject`; never install/absorb/approved in Phase 0-5.
- Memory: confirm proposals only; no write or solidify.
- Phase 6: confirm SourceLock and quarantine only; no install/run/enable.

### Step 8a: Verify Capability Registration

For every capability used in the batch, verify:

1. Does it appear in `capability-inventory.md`?
2. Is its Status `approved`?
3. Is its Platform field compatible with the executing platform?
4. Is its Phase 0-5 constraint being respected?

Decision:

- Capability used but not in inventory: `blocked`
- Capability in inventory but Status is `proposed`: `blocked`
- Capability in inventory, approved, but Platform mismatch: `needs_revision`
- Capability in inventory, approved, correct platform, Phase constraint violated: `blocked`
- All capabilities registered and approved: continue

### Step 9: Apply Invariants and Negative Tests

Cross-check:

- P0 invariants in `runtime-invariants.md`
- Negative fixtures in `docs/agent-runtime/negative-test-fixtures/`
- Gate semantics in `verification-gates.md`

If the report resembles a negative test fixture, the expected Gate Decision from that fixture is the minimum severity.

### Step 10: Issue Reviewer Decision

Allowed decisions:

```text
pass_to_review
needs_revision
blocked
human_required
```

The decision must include:

- blocking findings
- nonblocking findings
- required fixes
- approved next batch, if any
- residual risk

## 4. Changed Files Attribution

Use this classification table.

| Class | Meaning | Reviewer Decision |
|---|---|---|
| `existing_dirty_unchanged` | Dirty before and after, no evidence of content change | continue |
| `approved_new_file` | New file under approved output path | continue |
| `approved_edit` | Existing file explicitly approved for this batch | continue |
| `unexpected_changed_file` | New or modified path not in approved outputs | blocked / human_required |
| `forbidden_path` | Path in protected area | blocked |
| `unattributed_change` | Cannot tell whether executor touched it | human_required |

For dirty baseline files, do not rely on status letters alone. If the file is already dirty and the task claims it was untouched, the executor must provide enough evidence to compare pre/post content or state that the batch did not inspect content hashes.

## 5. Fake Green Detection

Fake green means the report claims success while evidence is missing, failed, blocked, or contradictory.

Immediate fake green indicators:

- `blocked_by_env` later summarized as pass.
- Script missing but reported as ran.
- Command failed but listed under successful validations.
- Skipped validation omitted from report.
- Post-status missing after file writes.
- Unknown source of truth treated as approved.
- GateResult signed by executor.
- Hard stop marked yes but overall status pass.

Decision:

- Fake green on a P0 or validation claim: `blocked`
- Incomplete but honest evidence: `needs_revision` or `human_required`

## 6. Dirty Worktree Review

The reviewer must preserve the known dirty baseline unless a batch explicitly authorizes a specific dirty file edit.

Current known baseline includes 13 modified files and 6 original untracked entries recorded in Batch A.

Review process:

1. Compare the report's pre-status to known baseline.
2. Identify new untracked batch assets.
3. Confirm no protected dirty file changed content.
4. If a dirty file must be edited, require a separate batch.

Decision:

- Dirty file edited without explicit batch approval: `blocked`
- Dirty attribution unclear: `human_required`
- Dirty baseline unchanged: continue

## 7. Batch Checklists

### Batch A Checklist

Purpose: inventory, source-of-truth proposal, path drift.

Pass requirements:

- Read-only for A1.
- `source_of_truth_decision` is proposed, not silently approved.
- Path drift register includes `D:\devFrame` vs `D:\dev-frame`.
- Duplicate clone relationship is documented.
- CodeGraph status is documented without reindex.
- No files written unless A2 was approved.

Blockers:

- Source of truth unknown after write.
- Multiple candidate roots and no reviewer decision.
- External clone or package install.
- Secret access.

### Batch B Checklist

Purpose: runtime docs, contracts, tool/memory/skill policy.

Pass requirements:

- 8 core contracts are present.
- SkillIntakeRecord dispositions are limited to `reference_only`, `candidate`, `defer`, `reject`.
- Tool policy forbids package installs, MCP config mutation, UI-TARS, external scripts in Phase 0-5.
- Memory architecture freezes memory writes in Phase 0-5.
- Verification gates do not mark missing checks as pass.

Blockers:

- Any current-phase install/approved language for external skills.
- Memory write or solidify allowed in Phase 0-5.
- MCP config changes allowed in Phase 0-5.

### Batch C Checklist

Purpose: rules, audit-only hooks, AGENTS navigation.

Pass requirements:

- `rules/*` use IDs, priorities, triggers, actions, verification, conflict handling.
- P0 > P1 > P2 > P3 > P4 is explicit.
- pre-edit hook: named `*.audit.draft.ps1` (known naming gap), is ACTIVE + REGISTERED + BLOCKING (exit 1 on hard violations). Other hooks: named `*.audit.draft.ps1`, audit-only draft, exit 0 always.
- Active hook blocks: memory writes, sealed file edits, secret file edits. Permits: approved-scope writes, dirty baseline warnings (exit 0).
- Hooks never call network.
- `AGENTS.md` is navigation-only.

Blockers:

- Draft hook (not pre-edit) registered without human gate.
- Hook placed in `.git/hooks`.
- pre-edit hook modified to allow memory/sealed/secrets edits without reviewer approval.
- AGENTS.md copies full rules and becomes a rule dump.
- README edited without separate approval.

### Batch D Checklist

Purpose: hard assets: schemas, invariants, negative tests, risk models, Phase 6 design, reviewer playbook.

Pass requirements:

- Schemas are valid JSON and use strict enums.
- Invariants cover P0 hard stops.
- Negative tests map to invariants.
- FMEA and STRIDE identify controls and gate decisions.
- Phase 6 remains review-only and quarantine-only.
- Reviewer Playbook references the produced assets.

Blockers:

- Schema allows install/absorb/approved for Phase 0-5 skill intake.
- Schema allows executor-signed GateResult.
- Invariants downgrade P0 hard stops.
- Phase 6 design allows install/run/enable.

### Batch E Checklist

Purpose: README path drift fix.

Pass requirements:

- Only `README.md` is edited.
- Only path drift is changed: `D:\devFrame` to `D:\dev-frame`.
- No structure or unrelated wording change.
- Pre/post diff shows exact lines changed.

Blockers:

- README rewrite beyond path drift.
- Any other dirty baseline file touched.
- Git mutation or commit.

### Phase 6 Checklist

Purpose: external source lock and quarantine.

Pass requirements:

- Source is on approved allowlist.
- Human approval exists before clone.
- Clone target is quarantine only.
- Commit SHA is locked.
- SourceLockRecord exists.
- Static review notes exist.
- No install, execute, enable MCP, register hook, or UI-TARS real desktop.

Blockers:

- Clone before allowlist or human approval.
- Missing commit SHA.
- Quarantine is runtime-loadable.
- Any external code executed.

## 8. Gate Decision Tree

```text
1. Was any P0 hard stop violated?
   yes -> blocked
   no  -> continue

2. Is source_of_truth valid for this batch?
   no -> blocked or human_required
   yes -> continue

3. Are pre/post git status records complete?
   missing pre -> blocked
   missing post after writes -> blocked
   complete -> continue

4. Are changed files inside approved outputs?
   no -> blocked / human_required
   yes -> continue

5. Did any forbidden command run?
   yes -> blocked
   no -> continue

5a. Were all used capabilities registered and approved in capability-inventory.md?
   no -> blocked or needs_revision
   yes -> continue

6. Are validations honest?
   fake green -> blocked
   blocked_by_env reported honestly -> needs_revision / human_required
   complete -> continue

7. Are required artifacts present and consistent?
   missing critical artifact -> needs_revision
   contradictory artifact -> blocked
   complete -> continue

8. Is a human decision needed?
   yes -> human_required
   no -> pass_to_review
```

## 9. Report Review Template

Use this when replying to an Execution Report.

```markdown
# Reviewer Decision

Decision: pass_to_review / needs_revision / blocked / human_required

## Findings

| Severity | Finding | File/Path | Required Fix |
|---|---|---|---|

## Evidence Checked

- Git status:
- Changed files:
- Artifact paths:
- Command audit:
- Forbidden action check:
- Invariant checks:
- Negative test similarity:

## Scope Result

- Approved outputs only: yes/no
- Dirty baseline untouched: yes/no/unknown
- High-risk actions avoided: yes/no
- Fake green detected: yes/no

## Next Step

- Allow next batch:
- Required fixes:
- Human decisions:
```

## 10. Useful Cross-References

| Need | Reference |
|---|---|
| Active bootstrap boundary | `AGENTS.md`, `tool-policy.md` |
| Source of truth | `source-of-truth-decision.md` |
| P0/P1/P2/P3 gates | `verification-gates.md` |
| Invariants | `runtime-invariants.md` |
| Negative tests | `negative-acceptance-tests.md`, `negative-test-fixtures/` |
| Contracts | `integration-contracts.md`, `schemas/agent-runtime/` |
| External skill intake | `external-skill-intake.md`, `skills-inbox/` |
| Phase 6 | `phase-6-source-lock-quarantine.md`, `source-lock-record.schema.json` |
| Risk models | `fmea-risk-analysis.md`, `stride-threat-model.md` |

## 11. Known Review Notes

These items are known low-severity follow-ups from D7-R/D8-R and should not block this playbook:

1. `skills-inbox/external/README.md` may still contain sandbox wording that should be softened in a later doc cleanup.
2.  terminology is not yet normalized in the permitted tool table.
3. Some documents use "approved scope" wording that should be backed by schema references in a later consistency pass.

Do not promote these notes to blockers unless a new batch changes their context or makes them permissive.
