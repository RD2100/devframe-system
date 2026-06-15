# TS-OPENCODE-SECURITY-PREFLIGHT-FOCUSED-REFRESH

Owner thread: `019ec6c5-7d65-76e2-b9a6-9316c75aeae8`
Module: `dev-frame-opencode`
Expected base: `0c24204fd99e6cab1d853ecadb12200244119fe1`
Priority: P1

## Goal

Run a focused read-only Security Preflight refresh after the SD-07 report UX
slice. The objective is to find blocker security issues in the paper workflow
surface before any move toward real paper content or live WriteLab pilots.

## Scope

Focus on:

- `ai-workflow-hub/src/ai_workflow_hub/cli.py`
- `ai-workflow-hub/src/ai_workflow_hub/daemon.py`
- `ai-workflow-hub/src/ai_workflow_hub/task_queue.py`
- `ai-workflow-hub/tasks.yaml`
- `ai-workflow-hub/pyproject.toml`
- `schemas/paper_business_validation_report.schema.json`

Review risks:

- command execution
- path traversal
- arbitrary file read/write
- workflow/task config injection
- daemon privilege boundary
- queue state pollution
- secret/token leakage
- uncontrolled subprocess
- unsafe deserialization
- unbounded external service calls
- report fields that could promote candidate evidence to live authorization

## Forbidden

- Do not automatically fix findings in this task.
- No real paper content.
- No live WriteLab, daemon worker, OpenCode dispatch, browser/CDP, ChatGPT,
  cloud, package install, push, reset, clean, stash, or MCP config mutation.

## Expected Verification

- Read-only focused review of the listed paths.
- `python -m pytest ai-workflow-hub\tests\test_paper_business_capability_validation.py -q`
- `git diff --check`

## Output

Return `SECURITY_PREFLIGHT_REFRESH_PASS`, `SECURITY_PREFLIGHT_FINDINGS`, or
`BLOCKED`, with findings classified as `BLOCKER_SECURITY_FIX`,
`HUMAN_REQUIRED`, `NON_BLOCKING`, or `FALSE_POSITIVE`. Include Reviewer Index
and exact paths inspected.
