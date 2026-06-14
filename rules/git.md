# Git Rules -- RD2100 Agent Runtime v2

> Domain: git safety
> Phase 0-5: P0/P1 active; P2-P4 within approved task scope

---

## RULE git-001: No Force Push to Main/Master

- **Priority**: P0 (Hard Stop)
- **Trigger**: `git push --force` or `git push -f` to main or master
- **Scope**: All phases
- **Rule**: Never force-push to the main/master branch. This is an irreversible destructive action that can destroy team work.
- **Verification**: If push is needed, verify target branch is not main/master before pushing.
- **Conflict Handling**: No exceptions. If force-push to main appears necessary, stop and escalate to human.

---

## RULE git-002: No Destructive Commands Without Approval

- **Priority**: P0 (Hard Stop)
- **Trigger**: `git reset --hard`, `git clean -fd`, `git checkout -- <file>`, `git stash drop`, `git branch -D`
- **Scope**: All phases
- **Rule**: Destructive git commands that irreversibly discard work require explicit human approval. State what would be lost and why it must be discarded.
- **Verification**: Git reflog shows no unapproved destructive operations.
- **Conflict Handling**: If a destructive command is in a batch plan, flag it, do not execute without separate confirmation.

---

## RULE git-003: No Skip Hooks

- **Priority**: P1 (Scope Control)
- **Trigger**: `git commit --no-verify`, `git push --no-verify`, `--no-gpg-sign`
- **Scope**: All phases
- **Rule**: Do not skip git hooks unless the user explicitly requests it. If a hook fails, investigate and fix the underlying issue rather than bypassing the hook.
- **Verification**: Git log shows no `--no-verify` flags without documented approval.
- **Conflict Handling**: If a hook is broken and blocking legitimate work, report the hook failure, get approval to bypass, and create a task to fix the hook.

---

## RULE git-004: Clean Commits

- **Priority**: P2 (Evidence)
- **Trigger**: Creating a commit
- **Scope**: All phases
- **Rule**: Each commit should be a logical unit of change. Do not mix unrelated changes in one commit. Do not commit secrets, large binaries, or generated files without explicit approval. Commit messages should explain why, not what.
- **Verification**: `git diff --stat` shows focused changes; `git log --oneline` messages are meaningful.
- **Conflict Handling**: If a change naturally spans multiple concerns, document in the commit body.

---

## RULE git-005: Never Amend Published Commits

- **Priority**: P1 (Scope Control)
- **Trigger**: `git commit --amend` on a commit that has been pushed
- **Scope**: All phases
- **Rule**: Never amend a commit that has been pushed to a shared branch. Amending published history causes divergence and lost work for teammates.
- **Verification**: Before amending, check `git status` and `git log --oneline origin/<branch>..HEAD`.
- **Conflict Handling**: If a published commit must be changed, use `git revert` (for undo) or create a new commit (for fixes).

---

## RULE git-006: Phase 0-5 Commit Freeze

- **Priority**: P1 (Scope Control)
- **Trigger**: Any git commit
- **Scope**: Phase 0-5 bootstrap
- **Rule**: Do not commit, stash, reset, clean, or otherwise mutate git state during Phase 0-5. The existing dirty baseline (13 modified + 6 untracked) must be preserved exactly as-is. All new work is untracked.
- **Verification**: `git status --short` shows unchanged modified files; no new commits.
- **Conflict Handling**: If a batch plan requires a git mutation, flag it, do not execute.
