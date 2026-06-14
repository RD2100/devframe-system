# Core Rules -- RD2100 Agent Runtime v2

> Domain: runtime core
> Phase 0-5: P0/P1 active; P2-P4 within approved task scope

---

## RULE core-001: No Destructive Git Without Approval

- **Priority**: P0 (Hard Stop)
- **Trigger**: Any git command that mutates history or discards work
- **Scope**: All phases
- **Rule**: Do not execute `git reset --hard`, `git clean -fd`, `git push --force`, `git checkout --`, `git stash drop`, `git branch -D` without explicit human approval.
- **Verification**: `git reflog` shows no unapproved destructive entries since session start.
- **Conflict Handling**: Even if a task plan says "reset to clean state", stop and ask.

---

## RULE core-002: No Secret Exposure

- **Priority**: P0 (Hard Stop)
- **Trigger**: Reading or writing any file
- **Scope**: All phases
- **Rule**: Do not read `.env`, `*.key`, `*.pem`, `*token*`, `*credential*`, SSH private keys, or any file that appears to contain secrets. Do not include secrets in output, logs, or reports.
- **Verification**: Grep output/logs for secret patterns (`BEGIN PRIVATE KEY`, `api_key=`, `token:`, `password=`).
- **Conflict Handling**: If a task requires reading a file that might contain secrets, stop and ask.

---

## RULE core-003: Phase Boundary Enforcement

- **Priority**: P0 (Hard Stop)
- **Trigger**: Any action
- **Scope**: Phase 0-5 bootstrap
- **Verification**: Cross-reference action list with Phase 0-5 forbidden list.
- **Conflict Handling**: If a batch plan requests a forbidden action, flag in ExecutionReport, do not execute.

---

## RULE core-004: Exit Code Contract

- **Priority**: P1 (Scope Control)
- **Trigger**: Any task completion
- **Scope**: All agent-acceptance runner tasks
- **Rule**: Exit 0 = PASS, Exit 1 = BLOCKED, Exit 2 = FAILED. Never report FAILED or BLOCKED as PASS ("no fake green").
- **Verification**: Exit code matches reported status.
- **Conflict Handling**: If a check fails but is a known flaky test, report as BLOCKED with known-issue reference, not PASS.

---

## RULE core-005: Dirty Baseline Protection

- **Priority**: P1 (Scope Control)
- **Trigger**: Any file modification
- **Scope**: Phase 0-5
- **Rule**: Do not modify existing dirty files (currently 13 modified + 6 untracked at baseline) unless explicitly approved in batch plan. New work must only touch approved scope.
- **Verification**: `git status --short` before and after each batch. Diff must only show approved changes.
- **Conflict Handling**: If a task accidentally touches a dirty baseline file, report immediately, do not continue.

---

## RULE core-006: Evidence Before Claim

- **Priority**: P2 (Evidence)
- **Trigger**: Making any claim about system state or task completion
- **Scope**: All phases
- **Rule**: Every claim must be backed by evidence. "X works" requires a test result, file listing, or command output. "Y exists" requires `test -f` or equivalent.
- **Verification**: Each claim in ExecutionReport has a corresponding evidence reference.
- **Conflict Handling**: If evidence cannot be collected (e.g., tool unavailable), note the limitation, downgrade claim confidence.

---

## RULE core-007: No Capability Without Inventory Registration

- **Priority**: P0 (Hard Stop)
- **Trigger**: Installing a plugin, registering a hook, enabling MCP, loading a skill, authorizing script execution -- any action that introduces or activates a new capability
- **Scope**: All phases, both platforms (Claude Code + Codex)
- **Rule**: Any capability must be registered in `docs/agent-runtime/capability-inventory.md` and receive reviewer approval BEFORE it is enabled. The `Platform` field in the inventory entry determines which platform(s) the capability is available on. A capability that does not appear in the inventory does not exist -- it must not be used, even if technically callable.
- **Registration Procedure**:
  1. Propose the capability in `capability-inventory.md` with `Status: proposed`
  2. Reviewer approves �?change to `Status: approved`
  3. Enable the capability on the target platform
  4. Verify via `codex plugin list` (Codex) or `settings.json` (Claude)
  5. Report the registration in the batch ExecutionReport
- **Platform Synchronization**:
  - Platform: Both �?enable on both platforms (if applicable)
  - Platform: Claude �?enable on Claude Code only
  - Platform: Codex �?enable on Codex only
  - Cross-platform capabilities (Both) registered once, enabled per-platform as needed
- **Verification**: Compare `codex plugin list` enabled entries and Claude `settings.json` hooks/MCP against `capability-inventory.md`. Every enabled capability must have a matching approved inventory entry.
- **Conflict Handling**: If a task requires a capability not in the inventory, stop and propose registration. Do not use it first and register later.

---

## RULE core-008: Resource Sufficiency �� Prove Gap Before Any Action

- **Priority**: P0 (Hard Stop)
- **Trigger**: ANY agent action that proposes creating, adding, modifying, or introducing something new. This includes code, documents, rules, frameworks, abstractions, processes, configurations, and protocols.
- **Scope**: All phases, all platforms, all task types.

**Principle**: The agent's default answer to "should I create X?" is "what already exists that makes X unnecessary?" The burden of proof is on the NEW action.

**Resource Sufficiency Check (mandatory before any additive action):**

| Check | Question |
|-------|----------|
| **Existence** | Does something already exist that covers this need? |
| **Coverage** | Does an existing resource partially cover it �� and can the gap be filled with a minimal change? |
| **Composition** | Can multiple existing resources be combined to satisfy the need? |
| **Protocol** | Does an existing workflow, dispatch rule, or governance mechanism already handle this? |
| **Precedent** | Has this situation occurred before? What did the lesson log say? |

**Decision Matrix (universal):**

| Finding | Action |
|---------|--------|
| Exact match exists | **Stop.** Point to existing. Do nothing new. |
| Partial coverage + gap is ��20% | **Minimal patch.** Edit existing, don't create new. |
| Composition of 2+ existing covers need | **Compose.** Write glue only if necessary. |
| Truly novel need confirmed | **Proceed.** Document which resources were checked. |

**False Positives (model must recognize these as NOT sufficient justification):**
- "The existing resource is in a different format" �� format conversion is not a reason to recreate
- "The existing resource is not organized how I would" �� preference is not a gap
- "It would be cleaner as a new thing" �� aesthetics is not a gap
- "This is a common pattern so we should have it" �� commonality is not a gap
- "User asked for it" �� user request is a hypothesis, not proof of need

### Execute Agent Veto Contract

1. **Veto validity**: A veto is valid only if it cites specific capability IDs, rule IDs, and proposes an alternative execution path. A veto without executable alternative is invalid unless the task is unsafe or irreversible.

2. **Veto decision types**:
   - `accept` �?task is necessary, proceed
   - `reject_redundant` �?existing capabilities cover this; must provide reuse plan
   - `reject_unsafe` �?task poses security/irreversibility risk; cannot be appealed
   - `request_revision` �?task needs clarification or scope reduction
   - `escalate` �?cannot decide, defer to human reviewer

3. **Appeal mechanism**: Plan agent can appeal `reject_redundant` to human reviewer. `reject_unsafe` cannot be appealed.

4. **Risk-based escalation**: Low-risk + reversible tasks �?execute agent veto can be final. High-risk + irreversible tasks �?must escalate to human if either agent disagrees.

5. **Anti-abuse constraint**: Execute agent must not systematically reject all new construction. If >50% of TaskSpecs in a batch are rejected, the veto authority is suspended pending human review.

**Verification**: Every ExecutionReport for a construction task must include a `gate_0_reuse_check` section proving that inventory was checked, existing capabilities were evaluated, and delta was justified.

**Conflict Handling**: If Gate 0 is skipped or incomplete, the execute agent MUST reject the TaskSpec. Plan agent must re-submit with Gate 0 completed.


---

## Knowledge Metabolism Rule

P0 rules are capped at 7. If a new P0 rule is proposed, an existing P0 must be downgraded to P1, merged into another P0, or deprecated with justification. This prevents rule inflation where too many mandatory checks cause agent attention dilution.

Current P0 count (core.md internal): core-001, core-002, core-003, core-005, core-007, core-008 = 6. Cap of 7 not reached. (core-004 is P1 and is not counted in P0 cap.)
