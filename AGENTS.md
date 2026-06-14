# AGENTS.md -- devframe-system

> Canonical root: D:\devframe-system
> Phase: 0-5 (bootstrap) | Generated: 2026-06-15
> Platform: Both | Bootstrap v1.0

## Quick Start

1. [Operating Model](docs/agent-runtime/operating-model.md)
2. [Integration Contracts](docs/agent-runtime/integration-contracts.md)
3. [Verification Gates](docs/agent-runtime/verification-gates.md)

## Default Development Process: Sub-Agent Dispatch

This project uses the [Sub-Agent Dispatch Protocol](docs/agent-runtime/sub-agent-dispatch-protocol.md) (SADP):

- **Codex Goal Agent** (planning tier): Decomposes goals, dispatches [TaskSpecs](docs/agent-runtime/sub-agent-dispatch-protocol.md#1-taskspec-format), evaluates [ExecutionReports](docs/agent-runtime/sub-agent-dispatch-protocol.md#2-executionreport-format), updates plans.
- **Claude Code Agent** (execution tier): Receives self-contained TaskSpec, implements, collects evidence, returns ExecutionReport.
- All capabilities used must be registered in [capability-inventory.md](docs/agent-runtime/capability-inventory.md) (core-007).

## Hard Stops (P0)

| # | Rule | Source |
|---|------|--------|
| 1 | No destructive git without human approval | `rules/core.md` core-001 |
| 2 | No secrets in code, logs, or reports | `rules/security.md` sec-001 |
| 3 | No command injection or path traversal | `rules/security.md` sec-002, sec-003 |
| 4 | No fake green (FAILED/BLOCKED != PASS) | `rules/review.md` review-001 |
| 5 | No write to files outside approved scope | `rules/core.md` core-005 |
| 6 | No capability without inventory registration | `rules/core.md` core-007 |

## Document Map

```
docs/agent-runtime/
  operating-model.md          <- Execution layers, tiers, lifecycle
  integration-contracts.md    <- 8 core data contracts
  verification-gates.md       <- P0-P3 gate hierarchy
  tool-policy.md              <- Phase-aware tool policy (generated)
  capability-inventory.md     <- Cross-platform capability inventory
  runtime-invariants.md       <- Runtime invariants
  reviewer-playbook.md        <- Reviewer guide + decision tree
  negative-acceptance-tests.md <- 30 negative test definitions
  negative-test-fixtures/     <- 30 JSON
  sub-agent-dispatch-protocol.md <- Default dev workflow: SADP TaskSpec + ExecutionReport
  dispatch-model-profiles.md    <- Per-model capability limits + failure patterns
  lessons-learned.md             <- Operational knowledge log + Knowledge Metabolism
  sub-agent-dispatch-protocol.md <- Default dev workflow: TaskSpec + ExecutionReport test fixtures

rules/
  README.md, core.md, coding.md, security.md, review.md, git.md, research.md, frontend.md

templates/runtime-bootstrap/  <- Self-contained bootstrap (re-runnable)
```

## Phase 0-5 Boundary

NOT active in Phase 0-5:
- External skills: not installed, not executed
- Memory writes: read-only
- Package install: forbidden
- MCP config changes: forbidden
- Git mutations: no commit/push/reset/clean/stash
- Capability registration: all new capabilities must be registered and reviewer-approved before enablement

See [tool-policy.md](docs/agent-runtime/tool-policy.md).

## Project Context

- Project: devframe-system | Root: D:\devframe-system
- Git: git@github.com:RD2100/devframe-system.git | Platform: Both

> Generated from `templates/runtime-bootstrap/AGENTS.template.md`. Re-run bootstrap.ps1 -Force to regenerate.