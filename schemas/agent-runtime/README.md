# RD2100 Agent Runtime v2 -- JSON Schemas

> Batch D1, 2026-05-27
> JSON Schema Draft 2020-12

This directory contains JSON Schema definitions for the core integration contracts and @go evidence artifacts.

## Schemas

| # | Schema File | Description |
|---|-------------|-------------|
| 1 | `task-spec.schema.json` | Unit of work description before execution begins |
| 2 | `run-spec.schema.json` | Record of how a task was executed |
| 3 | `evidence-index.schema.json` | Index of evidence artifacts produced during a run |
| 4 | `gate-result.schema.json` | Result of a single verification gate check |
| 5 | `execution-report.schema.json` | Final structured report of a batch execution |
| 6 | `skill-intake-record.schema.json` | Intake evaluation record of an external skill |
| 7 | `tool-risk-record.schema.json` | Risk assessment of a tool available to agents |
| 8 | `memory-update-record.schema.json` | Proposed memory update subject to human approval |
| 9 | `source-lock-record.schema.json` | External skill source lock record (Phase 6) |
| 10 | `review.schema.json` | Independent reviewer verdict for an @go run |
| 11 | `safety-report.schema.json` | Deterministic guard output captured for an @go run |
| 12 | `chain-evidence.schema.json` | Role/session chain for an @go run |
| 13 | `multi-agent-gate0-preflight.schema.json` | Read-only readiness report for multi-agent / multi-GPT pilot startup |
| 14 | `multi-agent-dispatch-plan.schema.json` | Read-only first-wave worker assignment packet with conflict boundaries |

## Constraints

- All schemas use JSON Schema Draft 2020-12.
- `additionalProperties` is `false` on all schemas.
- Phase 0-5 enum constraints are enforced:
  - SkillIntakeRecord disposition: `reference_only`, `candidate`, `defer`, `reject` only (no `install`, `absorb`, `approved`)
  - MemoryUpdateRecord status: `proposed` only for new records (no `approved` at agent level)
  - GateResult signer_role: must not be `executor`, `fixer`, or `coder`
- Forbidden patterns (MCP config modification, UI-TARS/computer-use, package managers, external script execution) are documented in descriptions and NOT listed as permitted values.
