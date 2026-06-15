# Security Closeout

Date: 2026-06-16
Reviewer: parent devframe-system coordinator
Scope: security-fix closeout and parent pin alignment

## Verdict

Status: `SECURITY_CLOSEOUT_TARGETED_REGRESSION_PASS`

The current security-fix line has been closed at targeted-regression level and
pinned into the parent lock set.

This is not a four-repository full regression pass.

## Closed Findings

- `DS-CAND-005`: `agent-acceptance` batch manifest command execution no longer
  allows arbitrary shell strings or interpreter eval paths through
  `Run-Batch.ps1`.
- `DS-CAND-003`: `dev-frame-opencode` project commands now use constrained
  argv execution and command policy checks. `pytest` targets are bounded to
  project-local test paths.
- `DS-CAND-004`: TaskSpec verification rejects single Windows `&` and other
  shell operators.
- `DS-CAND-006`: generated verifier commands no longer contain
  `|| echo *-ok` fake-green fallbacks.
- `DS-CAND-007`: `devframe-control-plane` closure status and
  `CLOSURE_REPORT.md` now fail closed on verifier failures.
- `DS-CAND-008`: parent positive-pilot authorization packet validation resolves
  evidence paths before containment checks.
- `DS-CAND-001`: `test-frame` ToolContract lifecycle URLs are subject to
  default-deny URL policy and lifecycle host allowlisting.
- `DS-CAND-002`: `test-frame` lifecycle download `save_as` paths are constrained
  under an artifact root.

## Pinned Security Heads

- `agent-acceptance`:
  `c37bf85a06c2c8a5be1710fb2f7b988ed14fcb7f`
- `dev-frame-opencode`:
  `f9ab656fb602b648639d9e27ea3ab54df4f22bad`
- `devframe-control-plane`:
  `09167bc656f8625c97bfae5c52dae5a0280b116c`
- `test-frame`:
  `a30758a3b309dd5f0e33e57cce5a15a90b725c82`

## Parent Files Included

- `scripts/validate_positive_pilot_authorization_packet.py`
- `tests/test_positive_pilot_authorization_packet_paths.py`
- `BASELINE_LOCK.json`
- `integration/lock/submodules.lock.yml`
- `integration/reports/opencode-grouped-command-policy-return-review-2026-06-16.md`
- `integration/reports/security-closeout-2026-06-16.md`
- `integration/reports/parent-current-status-overview-2026-06-16.md`
- `integration/reports/README.md`
- `integration/PROJECT_COMPLETENESS_PLAN.md`

## Opencode Grouped Intake Evidence

`dev-frame-opencode` returned a grouped command-policy/security hardening batch:

- `OPENCODE_PROJECT_COMMAND_EXECUTION_POLICY_A1`
  - commit: `1b08ebca36b7b730bcdf5137b9f7953a43b03736`
  - evidence ZIP:
    `D:\devframe-system\.agent\evidence\evidence-opencode-project-command-execution-policy-a1-1b08ebc.zip`
  - SHA256:
    `B7C37067779B4FD779C5352DA2EA4941957947734A9896E57AF3AA044DC614E7`
  - GPT verdict: `accepted_with_limitations`
  - accepted status: `OPENCODE_PROJECT_COMMAND_EXECUTION_POLICY_READY`
- `OPENCODE_COMMAND_POLICY_MATRIX_AND_NEGATIVE_CASES_A1`
  - commit: `f9ab656fb602b648639d9e27ea3ab54df4f22bad`
  - evidence ZIP:
    `D:\devframe-system\.agent\evidence\evidence-opencode-command-policy-matrix-and-negative-cases-a1-f9ab656.zip`
  - SHA256:
    `2E70F127A25DDDFCC37881ED74ED485A433D0178CED69FE0F0E1EA31C455345D`
  - GPT verdict: `accepted_with_limitations`
  - accepted status: `OPENCODE_COMMAND_POLICY_MATRIX_READY`

Parent-side hash checks matched both ZIPs, and the submodule worktree was clean
at `f9ab656fb602b648639d9e27ea3ab54df4f22bad`.

## Verification Run

- from `D:\devframe-system\agent-acceptance`:
  `python -m pytest tests\test_run_batch_command_policy.py -q`
  returned `4 passed`.
- from `D:\devframe-system\dev-frame-opencode\ai-workflow-hub` with
  `PYTHONPATH=src`:
  `python -m pytest tests\test_security_preflight_p1.py -q`
  returned `20 passed`.
- from `D:\devframe-system\devframe-control-plane`:
  `python -m pytest tests\test_paper_b2_synthetic_workflow.py -q`
  returned `6 passed`.
- from `D:\devframe-system\test-frame`:
  `python -m pytest tests\test_async_executor.py tests\contracts\test_contracts.py -q`
  returned `26 passed`.
- from `D:\devframe-system`:
  `python -m pytest tests\test_positive_pilot_authorization_packet_paths.py -q`
  returned `2 passed`.
- `python -m py_compile scripts\validate_positive_pilot_authorization_packet.py`
  passed.
- from `D:\devframe-system\dev-frame-opencode\ai-workflow-hub` with
  `PYTHONPATH=src`:
  `python -m py_compile src\ai_workflow_hub\shell_runner.py src\ai_workflow_hub\cli.py src\ai_workflow_hub\project_detect.py src\ai_workflow_hub\nodes\tester.py`
  passed.
- `git diff --check` passed in the parent and each submodule; output contained
  CRLF warnings only.

## Known Gaps

- Four-repository full test suites were not run.
- No real Zotero app/API, Obsidian, RAG, WriteLab, MiniApp, browser/CDP, cloud,
  PDF, attachment, or full-text runtime was executed.
- `.agent/PROJECT_REGISTRY.json` changes in the parent and `agent-acceptance`
  are unrelated workspace registration changes and are intentionally not part
  of this security closeout.
- Python `__pycache__` artifacts remain untracked and are not part of this
  closeout.

## Reviewer Focus

- Confirm the four pinned submodule heads match the lock files.
- Confirm the command-policy changes reject shell metacharacter injection,
  interpreter eval entry points, and external pytest targets.
- Confirm ToolContract lifecycle URL/download policies default deny until
  callers provide explicit allowed hosts and artifact roots.
- Confirm verifier failures cannot produce completed closure reports.
