# Opencode Grouped Command Policy Return Review

Date: 2026-06-16
Reviewer: parent devframe-system coordinator
Scope: parent intake review only

## Verdict

Status: `ACCEPTED_FOR_PARENT_INTAKE_WITH_LIMITATIONS`

The latest `dev-frame-opencode` local/security hardening batch is accepted for
parent intake. This is focused command-execution hardening, not a full
repository security audit and not final governance acceptance.

## Reviewed Batch

Submodule:

- Path: `D:\devframe-system\dev-frame-opencode`
- Branch: `codex/paper-audit-privacy-hard-gate`
- Current commit for grouped intake:
  `f9ab656fb602b648639d9e27ea3ab54df4f22bad`

### OPENCODE_PROJECT_COMMAND_EXECUTION_POLICY_A1

- Commit: `1b08ebca36b7b730bcdf5137b9f7953a43b03736`
- Message: `Harden project command execution policy`
- Evidence ZIP:
  `D:\devframe-system\.agent\evidence\evidence-opencode-project-command-execution-policy-a1-1b08ebc.zip`
- Evidence ZIP SHA256:
  `B7C37067779B4FD779C5352DA2EA4941957947734A9896E57AF3AA044DC614E7`
- GPT verdict: `accepted_with_limitations`
- Accepted status: `OPENCODE_PROJECT_COMMAND_EXECUTION_POLICY_READY`
- Rework required: `false`

Verification from return:

- `test_security_preflight_p1.py`: `18 passed`
- e2e/m3/business suite: `22 passed`
- py_compile: `PASS`
- `git diff --check`: `PASS`

### OPENCODE_COMMAND_POLICY_MATRIX_AND_NEGATIVE_CASES_A1

- Commit: `f9ab656fb602b648639d9e27ea3ab54df4f22bad`
- Message: `Add command policy matrix coverage`
- Evidence ZIP:
  `D:\devframe-system\.agent\evidence\evidence-opencode-command-policy-matrix-and-negative-cases-a1-f9ab656.zip`
- Evidence ZIP SHA256:
  `2E70F127A25DDDFCC37881ED74ED485A433D0178CED69FE0F0E1EA31C455345D`
- GPT verdict: `accepted_with_limitations`
- Accepted status: `OPENCODE_COMMAND_POLICY_MATRIX_READY`
- Rework required: `false`

Verification from return:

- `test_security_preflight_p1.py`: `20 passed`
- e2e/m3/business suite: `22 passed`
- py_compile: `PASS`
- `git diff --check`: `PASS`

## Security Scope Covered

- Project commands reject shell metacharacters and execute parsed argv with
  `shell=False`.
- `python -c` / `py -c` are blocked.
- `node -e` / `node --eval` are blocked.
- `pytest` targets are restricted to relative project `tests/` or `test/`
  paths.
- Absolute pytest paths, `..` paths, `@argfile`, external `--rootdir`, and
  `--pyargs` are blocked.
- `unittest` is restricted to `discover tests/`.
- Arbitrary npm scripts, non-lint/test Gradle tasks, and git write commands are
  blocked.
- Ruff/mypy write flags are blocked.
- Generated verifier commands no longer use `|| echo *-ok` fake-green fallback.
- Tester aggregation preserves real failure while allowing pass plus omitted or
  skipped slots.
- `echo` remains as an internal no-shell verifier for dry-run compatibility.
- Command policy matrix is documented at
  `docs/agent-runtime/command-policy-matrix.md`.

## Parent-Side Checks

- `git -C dev-frame-opencode status --short --branch` showed a clean worktree
  on `codex/paper-audit-privacy-hard-gate`.
- `git -C dev-frame-opencode rev-parse HEAD` returned
  `f9ab656fb602b648639d9e27ea3ab54df4f22bad`.
- `Get-FileHash -Algorithm SHA256` for both evidence ZIPs matched the module
  return.
- Parent targeted regression later re-ran
  `python -m pytest tests\test_security_preflight_p1.py -q` with
  `PYTHONPATH=src` and returned `20 passed`.

## Boundary

No real Zotero app/API, Obsidian, RAG, WriteLab, MiniApp, browser/CDP, cloud,
PDF, attachment, full-text, or private runtime was used.

This batch does not make any new external resource live-ready and does not
create final governance acceptance.

## Known Gaps

- This is focused local/security hardening, not a full repository security
  audit.
- Evidence transcript formatting has minor roughness; parent reports normalize
  the wording and do not treat raw command transcript formatting as a polished
  final artifact.

## Parent Decision

Proceed to grouped parent pin as part of the 2026-06-16 security closeout.
