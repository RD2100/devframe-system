# Runtime Invariants -- RD2100 Agent Runtime v2

> Batch D2, 2026-05-27
> Defines 35 runtime invariants that must hold for every agent execution.
> P0 invariants are non-downgradeable hard stops.
> Phase 0-5: all invariants active as specified.

---

## Priority Legend

| Priority | Meaning | Violation Consequence |
|----------|---------|----------------------|
| **P0** | Hard Stop | Delivery blocked. Must resolve before any further action. |
| **P1** | Scope Control | FAILED status. Must fix before batch completion. |
| **P2** | Evidence / Quality | WARNING. Should fix; may proceed with documented justification. |

P0 invariants cannot be downgraded by P1-P4 considerations. No exception path exists for P0 violations.

---

## Category 1: Source of Truth

### INV-001: Canonical Root Reference

| Field | Value |
|-------|-------|
| **ID** | INV-001 |
| **Priority** | P0 (Hard Stop) |
| **Scope** | All phases, all agents |
| **Rule** | The canonical project root is `D:\agent-acceptance`. All path references in execution reports, evidence chains, and contract records must resolve to absolute paths rooted at this directory. Relative paths are resolved from this root. |
| **Violation Example** | An agent writes a report referencing `..\other-project\config.json` without resolving the absolute path. A task spec references `~/Documents/project` instead of the canonical root. |
| **Detection** | Grep all output files for relative path references (not starting with `D:\agent-acceptance\`). Verify `git rev-parse --show-toplevel` equals the canonical root. |
| **Gate Decision on Violation** | BLOCKED. All paths must be corrected to absolute canonical form. |

### INV-002: No Path Drift

| Field | Value |
|-------|-------|
| **ID** | INV-002 |
| **Priority** | P0 (Hard Stop) |
| **Scope** | All phases, all agents |
| **Rule** | No file written by an agent may reference a non-existent or drifted path in its content. Paths mentioned in documentation, contracts, and rules must resolve on-disk at the time of writing. Drifted paths (e.g., `D:\devFrame` when actual is `D:\dev-frame`) are invalid. |
| **Violation Example** | A contract document references `D:\devFrame\ai-workflow-hub` when the actual path is `D:\dev-frame\ai-workflow-hub`. An invariant references `C:\Users\OtherUser` when the actual home is `C:\Users\RD`. |
| **Detection** | For each path mentioned in a newly written file, run `test -d` or `test -f`. Rejected if the path does not exist. |
| **Gate Decision on Violation** | BLOCKED. Path must be corrected or documented as a known drift with resolution plan. |

---

## Category 2: Approved Outputs (Write Scope Boundary)

### INV-003: Write Scope Containment

| Field | Value |
|-------|-------|
| **ID** | INV-003 |
| **Priority** | P0 (Hard Stop) |
| **Scope** | Phase 0-5, all agents |
| **Rule** | Agents may only write to paths explicitly approved in the batch plan's "Approved Output Path" section. No write to any other path is permitted. The approved scope for Batch D2 is: `D:\agent-acceptance\docs\agent-runtime\runtime-invariants.md`. |
| **Violation Example** | An agent writes `D:\agent-acceptance\docs\FLOW_CATALOG.md` (a dirty baseline file not in approved scope). An agent creates `D:\agent-acceptance\new-file.log` without batch plan approval. |
| **Detection** | `git status --short` diff between pre and post. Any new or modified file not in the approved paths list is a violation. |
| **Gate Decision on Violation** | BLOCKED. Unapproved writes must be reverted or escalated for review. |

### INV-004: No Dirty Baseline File Modification

| Field | Value |
|-------|-------|
| **ID** | INV-004 |
| **Priority** | P0 (Hard Stop) |
| **Scope** | Phase 0-5 |
| **Rule** | The 13 modified and 6 untracked files present at baseline must not be altered. This includes: README.md, scripts/*, agent-workqueue/*, docs/FLOW_CATALOG.md, docs/NEXT_STAGE_BACKLOG.md, docs/RUNBOOK.md. New work must only touch batch-approved output paths. |
| **Violation Example** | An agent edits `README.md` to add a new section. An agent modifies `scripts/Run-WorkQueue.ps1` to fix a bug. |
| **Detection** | `git diff --name-only` must not include any file from the dirty baseline list. `git status --short` must show those files unchanged. |
| **Gate Decision on Violation** | BLOCKED. Report immediately. Do not continue the batch. |

### INV-005: New Files Only Under Approved Directories

| Field | Value |
|-------|-------|
| **ID** | INV-005 |
| **Priority** | P0 (Hard Stop) |
| **Scope** | Phase 0-5 |
| **Rule** | Any new file created must be under a directory path explicitly approved in the batch plan. For Batch D2, only `D:\agent-acceptance\docs\agent-runtime\` is approved for new file creation. No files may be created at the repository root or in unapproved subdirectories. |
| **Violation Example** | An agent creates `D:\agent-acceptance\templates\new-template.md` without approval. An agent creates `D:\agent-acceptance\invariants-backup.md` at the repo root. |
| **Detection** | `git status --short` shows untracked files. Each must be verified against the approved directories list. |
| **Gate Decision on Violation** | BLOCKED. Unapproved new files must be deleted or formally added to the batch-approved output paths. |

---

## Category 3: Pre/Post Git Status

### INV-006: Pre-Batch Git Status Required

| Field | Value |
|-------|-------|
| **ID** | INV-006 |
| **Priority** | P0 (Hard Stop) |
| **Scope** | Phase 0-5, every batch |
| **Rule** | Before any file-modifying batch begins, `git status --short` must be captured and recorded in the ExecutionReport as the pre-batch baseline. This snapshot is the reference against which all batch changes are measured. |
| **Violation Example** | A batch starts writing files without first capturing `git status --short`. The pre-batch state is unknown, making post-batch verification impossible. |
| **Detection** | ExecutionReport missing a "Pre-Batch Git Status" section with `git status --short` output. |
| **Gate Decision on Violation** | BLOCKED. Run `git status --short` immediately. If files were already modified, escalate for manual review. |

### INV-007: Post-Batch Git Status Required

| Field | Value |
|-------|-------|
| **ID** | INV-007 |
| **Priority** | P0 (Hard Stop) |
| **Scope** | Phase 0-5, every batch |
| **Rule** | After the batch completes (or is blocked), `git status --short` must be captured and compared against the pre-batch baseline. The diff must contain ONLY changes to the approved output paths listed in the batch plan. |
| **Violation Example** | A batch finishes and the report omits the post-batch git status. The pre/post diff cannot be verified. |
| **Detection** | ExecutionReport missing a "Post-Batch Git Status" section. Diff between pre and post `git status --short` shows unexpected changes. |
| **Gate Decision on Violation** | BLOCKED. If missing, capture immediately. If diff shows unapproved changes, escalate. |

### INV-008: Pre/Post Diff Must Be Clean

| Field | Value |
|-------|-------|
| **ID** | INV-008 |
| **Priority** | P0 (Hard Stop) |
| **Scope** | Phase 0-5, every batch |
| **Rule** | The diff between pre-batch and post-batch `git status --short` must show zero unexpected changes. Dirty baseline files must appear unchanged in both snapshots. Only files in the batch-approved output paths may appear as new. |
| **Violation Example** | Pre-batch shows `M README.md`. Post-batch also shows `M README.md` but the content hash differs -- it was silently edited. A new untracked file `D:\agent-acceptance\test.log` appears that is not in the batch-approved output paths. |
| **Detection** | Compare pre and post `git status --short` line by line. Check content hashes (`git diff`) for files that appear `M` in both snapshots. |
| **Gate Decision on Violation** | BLOCKED. Report the specific unexpected change immediately. |

---

## Category 4: Fake Green (FAILED/BLOCKED != PASS)

### INV-009: No Fake Green

| Field | Value |
|-------|-------|
| **ID** | INV-009 |
| **Priority** | P0 (Hard Stop) |
| **Scope** | All phases, all agents |
| **Rule** | A task or gate that fails or is blocked MUST be reported as FAILED or BLOCKED respectively. It must NOT be reported as PASS. This is unconditional. A check that cannot execute is BLOCKED, not PASS. A check that executes and fails is FAILED, not PASS. |
| **Violation Example** | A security gate check cannot run because the tool is unavailable. The agent reports the gate as PASS with a note "assumed safe". A test exits with code 2 but the report says "all good, PASS". |
| **Detection** | Cross-reference exit codes with reported statuses. Cross-reference gate execution evidence with reported gate results. |
| **Gate Decision on Violation** | BLOCKED. This is a P0 hard stop with no bypass. The report must be corrected. |

### INV-010: Exit Code Contract Enforcement

| Field | Value |
|-------|-------|
| **ID** | INV-010 |
| **Priority** | P0 (Hard Stop) |
| **Scope** | All agent-acceptance runner tasks |
| **Rule** | Exit code 0 = PASS. Exit code 1 = BLOCKED. Exit code 2 = FAILED. No other exit codes are valid. The exit code must match the reported task status. A task that returns exit code 1 cannot be reported as PASS. |
| **Violation Example** | A script returns exit code 1 (BLOCKED) due to a missing prerequisite. The agent reports the task as PASS because "the script itself ran fine." A task returns exit code 2 (FAILED) but is reported as PASS with a note "failure was minor." |
| **Detection** | For each RunSpec, verify that `exit_code` and `status` are consistent: 0 -> completed (PASS), 1 -> blocked (BLOCKED), 2 -> failed (FAILED). |
| **Gate Decision on Violation** | BLOCKED. Reconcile exit code with status. |

### INV-011: Flaky Test Is BLOCKED Not PASS

| Field | Value |
|-------|-------|
| **ID** | INV-011 |
| **Priority** | P1 (Scope Control) |
| **Scope** | All phases |
| **Rule** | A known flaky test that fails must be reported as BLOCKED with a reference to the flaky-test issue. It must not be reported as PASS. Only consistently passing tests can earn a PASS status. |
| **Violation Example** | A flaky integration test fails on this run but passed last time. The agent reports the task as PASS because "it's known flaky." |
| **Detection** | For any FAIL result that gets reported as PASS, check if there is a documented flaky-test issue referenced. If not, it is a fake green. |
| **Gate Decision on Violation** | FAILED. Task must be re-reported with correct BLOCKED status and flaky-test reference. |

---

## Category 5: External Clone (Forbidden in Phase 0-5)

### INV-012: No External Repository Clone

| Field | Value |
|-------|-------|
| **ID** | INV-012 |
| **Priority** | P0 (Hard Stop) |
| **Scope** | Phase 0-5 |
| **Rule** | Agents must not clone, fetch, or pull any external repository during Phase 0-5. This includes `git clone`, `gh repo clone`, `git submodule update`, and any equivalent operation. Supply chain risk is unacceptable before Phase 6 Source Lock &amp; Quarantine. |
| **Violation Example** | An agent runs `git clone https://github.com/example/skill-repo.git` to fetch a skill definition. An agent runs `git submodule update --init` to pull in dependencies. |
| **Detection** | Audit bash command history. Grep for `git clone`, `git submodule`, `gh repo clone`. Monitor for new directories containing `.git`. |
| **Gate Decision on Violation** | BLOCKED. Cloned repository must be removed. Security review required. |

---

## Category 6: Package Install (Forbidden in Phase 0-5)

### INV-013: No Package Manager Execution

| Field | Value |
|-------|-------|
| **ID** | INV-013 |
| **Priority** | P0 (Hard Stop) |
| **Scope** | Phase 0-5 |
| **Rule** | Agents must not execute any package manager command that installs or modifies dependencies. This includes `npm install`, `npm ci`, `pip install`, `pip install -e .`, `yarn add`, `pnpm install`, `cargo install`, `go get`, `gem install`, `nuget install`, and equivalents. |
| **Violation Example** | An agent runs `pip install requests` to use an HTTP library. An agent runs `npm install` to regenerate node_modules. |
| **Detection** | Audit bash command history for package manager commands. Check for new/modified `node_modules/`, `package-lock.json`, `yarn.lock`, `requirements.txt` changes, `__pycache__/`. |
| **Gate Decision on Violation** | BLOCKED. Installed packages must be removed. Dependency modifications must be reverted. |

### INV-014: No Build Tool Execution

| Field | Value |
|-------|-------|
| **ID** | INV-014 |
| **Priority** | P1 (Scope Control) |
| **Scope** | Phase 0-5 |
| **Rule** | Agents must not execute build tools or compilers unless the command is explicitly listed in the reviewer-approved validation commands list. This includes `npm run build`, `npx tsc`, `python -m compileall`, `make`, `cmake`, `dotnet build`, `go build`, `cargo build`. |
| **Violation Example** | An agent runs `npx tsc --noEmit` to check for type errors without reviewer approval. An agent runs `python -m compileall .` to verify syntax. |
| **Detection** | Audit bash command history for build tool invocations. Check for build artifact directories (`dist/`, `build/`, `out/`, `target/`). |
| **Gate Decision on Violation** | FAILED. Build artifacts must be removed. Execution must be documented and escalated. |

---

## Category 7: Hook Registration (Forbidden in Phase 0-5)

### INV-015: No Git Hook Registration

| Field | Value |
|-------|-------|
| **ID** | INV-015 |
| **Priority** | P0 (Hard Stop) |
| **Scope** | Phase 0-5 |
| **Rule** | Agents must not register, modify, or configure git hooks. This includes `git config core.hooksPath`, installing husky/lint-staged, writing to `.git/hooks/`, modifying `.husky/`, or any equivalent hook mechanism. |
| **Violation Example** | An agent runs `git config core.hooksPath .githooks` to set up hooks. An agent creates `.git/hooks/pre-commit` with a lint script. |
| **Detection** | Check `.git/hooks/` for new files. Check `git config --list` for `core.hookspath`. Check for `.husky/` directory changes. |
| **Gate Decision on Violation** | BLOCKED. Hooks must be removed. `git config` changes must be reverted. |

### INV-016: No System Hook Registration

| Field | Value |
|-------|-------|
| **ID** | INV-016 |
| **Priority** | P0 (Hard Stop) |
| **Scope** | Phase 0-5 |
| **Rule** | Agents must not register any form of system-level or IDE hook. This includes Visual Studio Code extensions, Windows Task Scheduler tasks, cron jobs, systemd timers, file system watchers, or any auto-trigger mechanism. |
| **Violation Example** | An agent creates a file watcher script that auto-runs on save. An agent installs a VS Code extension to enable auto-formatting. |
| **Detection** | Check for new system-level configurations. Check VS Code `.vscode/extensions.json` modifications. |
| **Gate Decision on Violation** | BLOCKED. Registered hooks must be removed. |

---

## Category 8: MCP Config Modification (Forbidden in Phase 0-5)

### INV-017: No MCP Configuration Mutation

| Field | Value |
|-------|-------|
| **ID** | INV-017 |
| **Priority** | P0 (Hard Stop) |
| **Scope** | Phase 0-5 |
| **Rule** | Agents must not modify any MCP server configuration file. This includes Claude Code `mcp_servers` settings, `.claude/mcp.json`, or any MCP configuration. Adding, removing, or altering MCP server entries is a configuration freeze violation. |
| **Violation Example** | An agent adds a new MCP server entry to `.claude/mcp.json` to enable a new tool. An agent changes the `codegraph` MCP server URL to a different instance. |
| **Detection** | Check MCP configuration files for modification timestamps. Compare pre/post content hashes of `.claude/mcp.json` and related files. |
| **Gate Decision on Violation** | BLOCKED. MCP configuration must be restored to pre-batch state. |

---

## Category 9: Memory Write (Forbidden in Phase 0-5)

### INV-018: No Memory File Write

| Field | Value |
|-------|-------|
| **ID** | INV-018 |
| **Priority** | P0 (Hard Stop) |
| **Scope** | Phase 0-5 |
| **Rule** | Agents must not write to any memory file. This includes `memory/*.md`, `MEMORY.md` index, `ACTIVE.md`, `agent-state.db`, or any file within `C:\Users\RD\.claude\`. Memory reads are permitted. Memory writes require `MemoryUpdateRecord` with status `proposed` only. |
| **Violation Example** | An agent writes a new entry to `memory/decisions.md`. An agent modifies `MEMORY.md` to add a new index entry. An agent writes to `agent-state.db` directly. |
| **Detection** | Pre/post `git status --short` comparison for `memory/` directory. Check modification timestamps of `MEMORY.md`, `ACTIVE.md`, `agent-state.db`. |
| **Gate Decision on Violation** | BLOCKED. Written memory must be identified and reported. |

### INV-019: Memory Proposals Only (No Solidify)

| Field | Value |
|-------|-------|
| **ID** | INV-019 |
| **Priority** | P0 (Hard Stop) |
| **Scope** | Phase 0-5 |
| **Violation Example** | An agent calls  to persist a bug pattern. An agent calls  to publish a new finding. |
| **Gate Decision on Violation** | BLOCKED. Solidified knowledge must be flagged for human review. |

### INV-020: MemoryUpdateRecord Status Constraint

| Field | Value |
|-------|-------|
| **ID** | INV-020 |
| **Priority** | P1 (Scope Control) |
| **Scope** | Phase 0-5 |
| **Rule** | All `MemoryUpdateRecord` entries created in Phase 0-5 must have `status: "proposed"`. The statuses `approved`, `rejected`, and `superseded` are only set by a human reviewer or in Phase 6+. |
| **Violation Example** | An agent creates a MemoryUpdateRecord with `status: "approved"` without human review. An agent writes `status: "superseded"` on an existing record. |
| **Detection** | Validate all MemoryUpdateRecord entries in the ExecutionReport. Any non-`proposed` status is a violation. |
| **Gate Decision on Violation** | FAILED. Record must be corrected to `proposed` status. |

---

## Category 10: Secrets Exposure

### INV-021: No Secrets in Output

| Field | Value |
|-------|-------|
| **ID** | INV-021 |
| **Priority** | P0 (Hard Stop) |
| **Scope** | All phases, all agents, all output |
| **Rule** | Secrets must never appear in any agent output: reports, logs, console output, commit messages, or written files. This includes API keys, tokens, passwords, private keys, connection strings with embedded credentials, and OAuth client secrets. Use `REPLACE_ME` or `<YOUR_KEY_HERE>` placeholders if documentation examples are needed. |
| **Violation Example** | An execution log contains `api_key=sk-abc123def456`. A report includes an AWS access key. A config example includes a real JWT signing secret. |
| **Detection** | Grep all output for patterns: `BEGIN.*PRIVATE KEY`, `api_key\s*=\s*[A-Za-z0-9]`, `token\s*:\s*[A-Za-z0-9]`, `password\s*=\s*[^\s]`, `secret\s*=\s*[^\s]`. |

### INV-022: No Secret File Access

| Field | Value |
|-------|-------|
| **ID** | INV-022 |
| **Priority** | P0 (Hard Stop) |
| **Scope** | All phases, all agents |
| **Rule** | Agents must not read files that are likely to contain secrets. This includes `.env`, `*.key`, `*.pem`, `*token*`, `*credential*`, `*secret*`, SSH private keys, and any file with restricted permissions. If a task requires accessing such a file, stop and ask for human guidance. |
| **Violation Example** | An agent runs `Read` on `D:\agent-acceptance\.env` to check configuration. An agent greps for `*.pem` files and reads their contents. |
| **Detection** | Audit file access logs for secret-pattern paths. Grep Read tool calls for `.env`, `.key`, `.pem`, `token`, `credential`, `secret`. |
| **Gate Decision on Violation** | BLOCKED. Report the access. If secrets were read into context, escalate for context-clearing protocol. |

### INV-023: No Hardcoded Credentials in Written Files

| Field | Value |
|-------|-------|
| **ID** | INV-023 |
| **Priority** | P0 (Hard Stop) |
| **Scope** | All phases, all agents |
| **Rule** | Any file written by an agent must not contain hardcoded credentials. This applies to configuration examples, documentation, code snippets, and test fixtures. Test fixture placeholders must use `test_` prefix with reviewer approval. |
| **Violation Example** | A written Markdown file contains `password = "admin123"` in a configuration example. A test fixture file contains a real database connection string. |
| **Detection** | Grep all newly written files for credential patterns: `password\s*=\s*"[^"]*"`, `secret\s*=\s*"[^"]*"`, `api_key\s*=\s*"[^"]*"`, `token\s*=\s*"[^"]*"`. |
| **Gate Decision on Violation** | BLOCKED. File must be rewritten with placeholders. |

---

## Category 11: Dangerous Git

### INV-024: No Force Push to Main/Master

| Field | Value |
|-------|-------|
| **ID** | INV-024 |
| **Priority** | P0 (Hard Stop) |
| **Scope** | All phases |
| **Rule** | `git push --force` or `git push -f` to `main` or `master` is unconditionally forbidden. This is an irreversible destructive operation. No exception exists. If force push to main appears necessary, escalate to human. |
| **Violation Example** | An agent force-pushes to origin/master to "clean up" after a bad rebase. |
| **Detection** | Pre-execution check: if a bash command includes `git push` and `--force` or `-f`, verify target branch is not main/master. `git reflog` audit. |
| **Gate Decision on Violation** | BLOCKED (pre-execution if detected). If already executed, CRITICAL escalation -- contact human immediately. |

### INV-025: No Destructive Git Without Approval

| Field | Value |
|-------|-------|
| **ID** | INV-025 |
| **Priority** | P0 (Hard Stop) |
| **Scope** | All phases |
| **Rule** | Destructive git commands require explicit human approval before execution. This includes: `git reset --hard`, `git clean -fd`, `git checkout -- <file>`, `git stash drop`, `git branch -D`, `git rebase --abort` with lost commits. Even if a batch plan mentions "reset to clean state," the agent must stop and confirm. |
| **Violation Example** | An agent runs `git reset --hard HEAD~3` to undo recent commits. An agent runs `git clean -fd` to remove untracked files. |
| **Detection** | Pre-execution check for destructive git patterns. `git reflog` audit post-execution. |
| **Gate Decision on Violation** | BLOCKED (pre-execution). If executed without approval, escalate for data recovery. |

### INV-026: No Skip Hooks

| Field | Value |
|-------|-------|
| **ID** | INV-026 |
| **Priority** | P1 (Scope Control) |
| **Scope** | All phases |
| **Rule** | Git hooks must not be skipped (`--no-verify`, `--no-gpg-sign`) unless the human reviewer explicitly requests it. If a hook fails, investigate and fix the underlying issue rather than bypassing. |
| **Violation Example** | An agent uses `git commit --no-verify` because the lint hook fails. An agent uses `git push --no-verify` to bypass branch protection checks. |
| **Detection** | Check git log/reflog for `--no-verify` flags. Audit hook bypass patterns. |
| **Gate Decision on Violation** | FAILED. Document the bypass, report the hook failure, and create a task to fix the hook. |

### INV-027: Phase 0-5 Commit Freeze

| Field | Value |
|-------|-------|
| **ID** | INV-027 |
| **Priority** | P1 (Scope Control) |
| **Scope** | Phase 0-5 |
| **Rule** | No git commits, stashes, resets, cleans, or other git state mutations are permitted in Phase 0-5. The existing dirty baseline (13 modified + 6 untracked) must be preserved exactly as-is. All batch work is tracked as untracked new files. |
| **Violation Example** | An agent commits a finished batch file. An agent stashes changes to "clean up." |
| **Detection** | `git log` shows no new commits since baseline. `git stash list` unchanged. `git status --short` shows dirty baseline files unchanged. |
| **Gate Decision on Violation** | FAILED. Any git mutation must be reported and escalated. |

---

## Category 12: Executor Self-Approval

### INV-028: Executor Cannot Approve Own Work

| Field | Value |
|-------|-------|
| **ID** | INV-028 |
| **Priority** | P0 (Hard Stop) |
| **Scope** | All phases |
| **Rule** | The executor agent (the agent performing a task) must not approve its own work. Approval requires a separate reviewer agent or a human. The executor may report results and claim completion, but the gate decision of "approved" or "accepted" must come from a different entity. |
| **Violation Example** | An agent completes a batch and marks the ExecutionReport `status: "accepted"` without human or reviewer agent sign-off. An agent sets `reviewer_decision: "approved"` on its own report. |
| **Detection** | Check ExecutionReport `status` field. If value is `accepted` or `reviewed` and no separate reviewer entity is documented, it is self-approval. Check `reviewer_decision` field for executor-set values. |
| **Gate Decision on Violation** | BLOCKED. Status must be downgraded to `submitted` or `draft`. |

### INV-029: Gate Result Must Be Explicit

| Field | Value |
|-------|-------|
| **ID** | INV-029 |
| **Priority** | P1 (Scope Control) |
| **Scope** | All phases |
| **Rule** | Every gate check must produce an explicit result: PASS, FAIL, WARNING, BLOCKED, or SKIPPED. Implicit or assumed gate results are not acceptable. Skipped gates must include a documented reason. Unavailable gates must be BLOCKED, not SKIPPED. |
| **Violation Example** | An agent skips the P2 quality gate without documenting why. An agent assumes the security gate passed because "the code looks safe." |
| **Detection** | For each required gate in the batch plan, verify a GateResult record exists with an explicit `result` field value. |
| **Gate Decision on Violation** | FAILED. Missing gate results must be produced or documented as BLOCKED with reason. |

---

## Category 13: Skill Installation (Forbidden in Phase 0-5)

### INV-030: No Skill Installation

| Field | Value |
|-------|-------|
| **ID** | INV-030 |
| **Priority** | P0 (Hard Stop) |
| **Scope** | Phase 0-5 |
| **Rule** | Agents must not install, enable, activate, or register any skill. This includes `skill-installer install`, writing to `~/.claude/skills/`, modifying skill registrations, or invoking skill activation commands. Skills from `skills-inbox/external/` must not be executed. |
| **Violation Example** | An agent runs `skill-installer install example-skill`. An agent copies a skill definition into `~/.claude/skills/`. |
| **Detection** | Check for new files in `~/.claude/skills/`. Check for skill registration changes. Audit for skill-installer tool invocations. |
| **Gate Decision on Violation** | BLOCKED. Installed skill must be removed. Registration must be reverted. |

### INV-031: External Skill Intake -- Record Only

| Field | Value |
|-------|-------|
| **ID** | INV-031 |
| **Priority** | P1 (Scope Control) |
| **Scope** | Phase 0-5 |
| **Rule** | When an external skill is encountered during Phase 0-5, the only permitted action is to create a `SkillIntakeRecord` (Contract 6) and/or `ToolRiskRecord` (Contract 7) with appropriate disposition. Defer, reject, or reference-only are the only valid dispositions. No execution, no installation, no cloning of the skill source. |
| **Violation Example** | An agent clones a skill repository to inspect its code. An agent evaluates a skill by running a test invocation. |
| **Detection** | Audit for `git clone` of skill repos. Check for new directories under `skills-inbox/`. Verify skill evaluation does not involve code execution. |
| **Gate Decision on Violation** | FAILED. Unapproved skill actions must be reported. |

---

## Category 14: Evidence Before Claim

### INV-032: Every Claim Must Have Evidence

| Field | Value |
|-------|-------|
| **ID** | INV-032 |
| **Priority** | P2 (Evidence) |
| **Scope** | All phases |
| **Rule** | Every substantive claim in an ExecutionReport must be backed by observable evidence. "X is configured" requires file content showing X. "Y works" requires a test result or command output. "Z exists" requires `test -f` or equivalent. Evidence must be traceable: claim -> artifact -> file read or command output. |
| **Violation Example** | An agent claims "all contracts validate correctly" without showing validation output. An agent claims "no secrets in output" without showing the grep results. |
| **Detection** | For each claim in the ExecutionReport, verify a corresponding evidence reference exists. Evidence must be a real file path reachable via `test -f` or `test -d`. |
| **Gate Decision on Violation** | WARNING. Downgrade unbacked claims to stated assumptions. |

### INV-033: Evidence Chain Traceability

| Field | Value |
|-------|-------|
| **ID** | INV-033 |
| **Priority** | P2 (Evidence) |
| **Scope** | All phases |
| **Rule** | Each piece of evidence must be traceable to the claim it supports. The chain is: claim in report -> evidence reference (EvidenceIndex entry) -> artifact at a filesystem path. The artifact must be accessible via Read or Bash at the referenced path. |
| **Violation Example** | A claim references an evidence ID that does not exist in the EvidenceIndex. An EvidenceIndex entry references `runs/result.log` but the file does not exist on disk. |
| **Detection** | For each EvidenceIndex entry, verify `test -f <artifact_path>` returns true. For each claim, verify the evidence reference is valid. |
| **Gate Decision on Violation** | WARNING. Broken evidence chains must be repaired or claims downgraded. |

---

## Category 15: Phase Boundary Enforcement

### INV-034: Phase 0-5 Action Allowlist

| Field | Value |
|-------|-------|
| **ID** | INV-034 |
| **Priority** | P0 (Hard Stop) |
| **Scope** | Phase 0-5 |
| **Violation Example** | An agent runs `pip install`. An agent modifies MCP config. An agent writes to a memory file. An agent executes an external script. |
| **Detection** | Cross-reference every tool invocation with the Phase 0-5 permitted list in `tool-policy.md`. |
| **Gate Decision on Violation** | BLOCKED. Phase boundary violation must be reported. Action must be undone if possible. |

### INV-035: Phase 0-5 Bash Allowlist

| Field | Value |
|-------|-------|
| **ID** | INV-035 |
| **Priority** | P0 (Hard Stop) |
| **Scope** | Phase 0-5 |
| **Rule** | Bash commands in Phase 0-5 must fit one of these patterns: path existence checks (`test -d`, `test -f`), directory listing (`ls`, `wc`), read-only git (`git status`, `git diff`, `git log`, `git rev-parse`, `git branch`, `git remote -v`), `mkdir -p` under reviewer-approved write scope, `echo` to new files under reviewer-approved write scope, and reviewer-approved validation commands. All other bash patterns are forbidden. |
| **Violation Example** | An agent runs `npx tsc --noEmit` (build tool, not in allowlist). An agent runs `npm list` (package manager, not in allowlist). An agent runs `rm -rf node_modules` (destructive, not in allowlist). |
| **Detection** | Audit every bash invocation against the Phase 0-5 Bash allowlist in `tool-policy.md`. |
| **Gate Decision on Violation** | BLOCKED. Unapproved bash command must be reported. Effects must be assessed. |

---

## Category 16: Command Injection

### INV-036: No Shell Command Injection

| Field | Value |
|-------|-------|
| **ID** | INV-036 |
| **Priority** | P0 (Hard Stop) |
| **Scope** | All phases, all agents |
| **Rule** | Shell commands must never be constructed by concatenating user or external input into command strings. Use argument arrays or parameterized interfaces where available. If a bash tool requires argument substitution, validate the input against a strict allowlist before substitution. |
| **Violation Example** | An agent constructs `bash "ls ${userInput}"` where userInput comes from a task description. An agent builds a PowerShell command string with unvalidated path input. |
| **Detection** | Grep for string interpolation patterns in tool invocations where the interpolated variable comes from task input, user input, or external data. |
| **Gate Decision on Violation** | BLOCKED. Refactor command construction to use safe argument passing. |

---

## Category 17: Path Traversal

### INV-037: No Path Traversal

| Field | Value |
|-------|-------|
| **ID** | INV-037 |
| **Priority** | P0 (Hard Stop) |
| **Scope** | All phases, all agents |
| **Rule** | File paths constructed with user or external input must be validated to stay within the intended directory or project root. Reject paths containing `..` segments that would escape the root. Resolve and verify the canonical path is within the allowed boundary. Absolute paths outside the batch-approved output paths are rejected. |
| **Violation Example** | A task spec includes a relative path `../../etc/config` which an agent uses without validation. An agent constructs a path `D:\outside\file.txt` from user input and writes to it. |
| **Detection** | For any user-supplied path, resolve the canonical path and verify it starts with `D:\agent-acceptance\` or the explicitly approved output directory. |
| **Gate Decision on Violation** | BLOCKED. Path must be rejected. Escalation if path traversal was attempted. |

---

## Category 18: Input Validation

### INV-038: Task Input Validation at Boundary

| Field | Value |
|-------|-------|
| **ID** | INV-038 |
| **Priority** | P0 (Hard Stop) |
| **Scope** | All phases |
| **Rule** | All fields received in a TaskSpec must be validated before the executor acts on them. `task_id` must be non-empty and unique. `priority` must be one of P0/P1/P2/P3. `status` must be one of draft/ready/deferred/rejected. `description` must be non-empty. Reject invalid input rather than silently proceeding. |
| **Violation Example** | An agent receives a task with `priority: "urgent"` (not a valid value) and executes it anyway. An agent receives a task with an empty `task_id` and proceeds. |
| **Detection** | Validate all TaskSpec fields against the Contract 1 validation rules before task execution. |
| **Gate Decision on Violation** | BLOCKED. Task must be rejected with validation error details. |

### INV-039: RunSpec Field Validation

| Field | Value |
|-------|-------|
| **ID** | INV-039 |
| **Priority** | P1 (Scope Control) |
| **Scope** | All phases |
| **Rule** | RunSpec records produced by an agent must pass Contract 2 validation: `task_id` references an existing TaskSpec, `status` is one of pending/running/completed/blocked/failed, `exit_code` is 0/1/2, and `started_at` precedes `finished_at` if both are present. |
| **Violation Example** | A RunSpec has `exit_code: 5` (invalid). A RunSpec has `status: "success"` (not in enum). A RunSpec has `finished_at` before `started_at`. |
| **Detection** | Validate every RunSpec produced against Contract 2 rules. |
| **Gate Decision on Violation** | FAILED. RunSpec must be corrected. |

### INV-040: EvidenceIndex Path Validation

| Field | Value |
|-------|-------|
| **ID** | INV-040 |
| **Priority** | P1 (Scope Control) |
| **Scope** | All phases |
| **Rule** | All `artifact_path` values in EvidenceIndex records must be within the project root (`D:\agent-acceptance\`). Path traversal outside the project root is a P0 violation (see INV-037). Even internal paths must be validated to prevent drift. |
| **Violation Example** | An EvidenceIndex entry references `D:\other-project\output.log`. An entry references a path that does not exist on disk. |
| **Detection** | For each EvidenceIndex entry, verify `artifact_path` starts with the project root and `test -f <path>` returns true. |
| **Gate Decision on Violation** | FAILED. Invalid evidence paths must be corrected or removed. |

---

## Invariant Summary

| ID | Category | Priority | Short Name |
|----|----------|----------|------------|
| INV-001 | Source of Truth | P0 | Canonical Root Reference |
| INV-002 | Source of Truth | P0 | No Path Drift |
| INV-003 | Approved Outputs | P0 | Write Scope Containment |
| INV-004 | Approved Outputs | P0 | No Dirty Baseline File Modification |
| INV-005 | Approved Outputs | P0 | New Files Only Under Approved Directories |
| INV-006 | Pre/Post Git Status | P0 | Pre-Batch Git Status Required |
| INV-007 | Pre/Post Git Status | P0 | Post-Batch Git Status Required |
| INV-008 | Pre/Post Git Status | P0 | Pre/Post Diff Must Be Clean |
| INV-009 | Fake Green | P0 | No Fake Green |
| INV-010 | Fake Green | P0 | Exit Code Contract Enforcement |
| INV-011 | Fake Green | P1 | Flaky Test Is BLOCKED Not PASS |
| INV-012 | External Clone | P0 | No External Repository Clone |
| INV-013 | Package Install | P0 | No Package Manager Execution |
| INV-014 | Package Install | P1 | No Build Tool Execution |
| INV-015 | Hook Registration | P0 | No Git Hook Registration |
| INV-016 | Hook Registration | P0 | No System Hook Registration |
| INV-017 | MCP Config | P0 | No MCP Configuration Mutation |
| INV-018 | Memory Write | P0 | No Memory File Write |
| INV-019 | Memory Write | P0 | Memory Proposals Only (No Solidify) |
| INV-020 | Memory Write | P1 | MemoryUpdateRecord Status Constraint |
| INV-021 | Secrets Exposure | P0 | No Secrets in Output |
| INV-022 | Secrets Exposure | P0 | No Secret File Access |
| INV-023 | Secrets Exposure | P0 | No Hardcoded Credentials in Written Files |
| INV-024 | Dangerous Git | P0 | No Force Push to Main/Master |
| INV-025 | Dangerous Git | P0 | No Destructive Git Without Approval |
| INV-026 | Dangerous Git | P1 | No Skip Hooks |
| INV-027 | Dangerous Git | P1 | Phase 0-5 Commit Freeze |
| INV-028 | Executor Self-Approval | P0 | Executor Cannot Approve Own Work |
| INV-029 | Executor Self-Approval | P1 | Gate Result Must Be Explicit |
| INV-030 | Skill Installation | P0 | No Skill Installation |
| INV-031 | Skill Installation | P1 | External Skill Intake -- Record Only |
| INV-032 | Evidence Before Claim | P2 | Every Claim Must Have Evidence |
| INV-033 | Evidence Before Claim | P2 | Evidence Chain Traceability |
| INV-034 | Phase Boundary | P0 | Phase 0-5 Action Allowlist |
| INV-035 | Phase Boundary | P0 | Phase 0-5 Bash Allowlist |
| INV-036 | Command Injection | P0 | No Shell Command Injection |
| INV-037 | Path Traversal | P0 | No Path Traversal |
| INV-038 | Input Validation | P0 | Task Input Validation at Boundary |
| INV-039 | Input Validation | P1 | RunSpec Field Validation |
| INV-040 | Input Validation | P1 | EvidenceIndex Path Validation |

---

## P0 Non-Downgradeability Clause

No P0 invariant may be downgraded by a P1, P2, P3, or P4 consideration. P0 violations are unconditional hard stops. The following scenarios are explicitly NOT valid justifications for downgrading a P0:

- "The violation was minor" (P0 severity is not graduated)
- "Fixing it would delay the batch" (schedule does not override P0)
- "The risk is theoretical" (P0 gates on potential, not realized, harm)
- "The tool automatically did it" (agents are responsible for their tool invocations)
- "It was in the batch plan" (P0 overrides batch plan instructions)

---

## Coverage Matrix

| Required Category | Covered By |
|-------------------|------------|
| Source of truth (canonical_root, path drift) | INV-001, INV-002 |
| Approved outputs (write scope boundary) | INV-003, INV-004, INV-005 |
| Pre/post git status | INV-006, INV-007, INV-008 |
| Fake green (FAILED/BLOCKED != PASS) | INV-009, INV-010, INV-011 |
| External clone (forbidden Phase 0-5) | INV-012 |
| Package install (forbidden Phase 0-5) | INV-013, INV-014 |
| Hook registration (forbidden Phase 0-5) | INV-015, INV-016 |
| MCP config modification (forbidden Phase 0-5) | INV-017 |
| Memory write (forbidden Phase 0-5, proposed records only) | INV-018, INV-019, INV-020 |
| Secrets exposure (P0 hard stop) | INV-021, INV-022, INV-023 |
| Dangerous git (reset --hard, clean -fd, push --force) | INV-024, INV-025, INV-026, INV-027 |
| Executor self-approval | INV-028, INV-029 |
| Skill installation (forbidden Phase 0-5) | INV-030, INV-031 |
| Evidence before claim | INV-032, INV-033 |
| Phase boundary enforcement | INV-034, INV-035 |
| Command injection | INV-036 |
| Path traversal | INV-037 |
| Input validation | INV-038, INV-039, INV-040 |
| Exit code contract | INV-010 |
| Dirty baseline protection | INV-004 |

---

## References

- `integration-contracts.md` -- Contracts 1-8 (TaskSpec, RunSpec, EvidenceIndex, GateResult, ExecutionReport, SkillIntakeRecord, ToolRiskRecord, MemoryUpdateRecord)
- `tool-policy.md` -- Phase 0-5 permitted and forbidden tools
- `verification-gates.md` -- P0-P3 gate hierarchy and gate execution order
- `memory-architecture.md` -- Phase 0-5 memory freeze, three-layer model
- `external-skill-intake.md` -- Phase 0-5 intake pipeline (record/classify/defer)
- `rules/core.md` -- Core rules: destructive git, secrets, phase boundary, exit code, dirty baseline, evidence
- `rules/security.md` -- Security rules: secrets, command injection, path traversal, input validation, credentials, thread safety, encryption, error messages
- `rules/review.md` -- Review rules: no fake green, report template, reviewer index, evidence chain, gate results, pre/post status
- `rules/git.md` -- Git rules: force push, destructive commands, skip hooks, clean commits, amend, phase 0-5 commit freeze
