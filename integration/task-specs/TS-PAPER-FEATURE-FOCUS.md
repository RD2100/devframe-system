# TS-PAPER-FEATURE-FOCUS

Date: 2026-06-15
Owner thread: `019ec6c5-7d65-76e2-b9a6-9316c75aeae8`
Target path: `D:\devframe-system\dev-frame-opencode`
Suggested branch: `codex/paper-feature-hardening`

## Objective

Continue paper functionality development with priority on user-facing quality,
privacy boundaries, and local/offline workflow reliability.

## Initial Findings

- `paper_task_spec.schema.json` and `paper_task_spec.sample.yaml` contain
  mojibake in Chinese descriptions/comments.
- Paper CLI surface is broad, but the user-facing command map and status
  semantics need integration-level documentation.
- Privacy/redaction controls exist but need explicit integration gates.

## Scope

- Fix mojibake in paper schema/fixture text without changing field names,
  required fields, or enum values.
- Add or update paper feature documentation that maps CLI commands to status and
  evidence behavior.
- Add privacy/redaction negative-case guidance for paper evidence.
- Prefer local/static validation over live workflow execution.

## Forbidden

- Do not run real paper workflow, external WriteLab, OpenCode, or full pytest.
- Do not store real paper full text in reports, memory, logs, or evidence.
- Do not promote `human_required`, `blocked`, or `failed` to accepted.

## Required Report

Reviewer Index plus a `Paper Focus` section: current state, changed files,
verification run, unresolved gaps, and next paper-specific tests.
