# Operating Model -- RD2100 Agent Runtime v2

> Batch B1, 2026-05-27
> Canonical root: D:\devframe-system

## Overview

The RD2100 Agent Runtime is a layered execution and verification framework. Agents operate within defined tiers, gates, and escalation rules. The runtime does not dictate what agents do -- it enforces how they prove correctness.

## Execution Layers

| Layer | Runner | Scope | Trigger |
|-------|--------|-------|---------|
| L0: Smoke | `scripts/Run-Smoke.ps1` | 7 basic health checks | On session start, on config change |
| L1: Batch | `scripts/Run-Batch.ps1` | N-task quality batch | Per-commit, per-PR |
| L2: WorkQueue | `scripts/Run-AllQueues.ps1` | Tier-graded queue execution | Scheduled, pre-release |
| L3: Parallel | `scripts/Run-QueueGroup.ps1` | Controlled parallel queues | When throughput needed |

## Tier Semantics

| Tier | Auto-execute | Escalation | Description |
|------|:---:|:---:|-------------|
| Tier 0 | YES | None | Safe, fast, always-run checks |
| Tier 1 | YES | Log warning | May require context, still safe |
| Tier 2 | NO | Must escalate to human | Destructive, expensive, or requires judgment |

## Exit Code Contract

| Code | Label | Meaning |
|------|-------|---------|
| 0 | PASS | All checks passed |
| 1 | BLOCKED | Cannot proceed (missing dependency, env issue) |
| 2 | FAILED | Check failed, must fix |

Rule: FAILED and BLOCKED must never be reported as PASS ("no fake green").

## Dry-Run Default

All runners default to dry-run mode. Real operations (file writes, mutations, external calls) require explicit flags:
- `-Real` on Run-WorkQueue.ps1
- `-Apply` on fix-oriented batches

## Agent Lifecycle

```
Session Start
  -> Memory inject (top 3-5 relevant memories)
  -> Smoke (L0) gate
  -> Task dispatch
       -> L1 Batch (per-task quality)
       -> L2 WorkQueue (tiered escalation)
       -> L3 Parallel (if throughput needed)
  -> Verification gates
  -> Report generation
  -> MemoryUpdateRecord proposal (no memory write in Phase 0-5)
Session End
```

## Integration Points

| Component | Direction | Protocol |
|-----------|-----------|----------|
| ai-workflow-hub | Upstream | CLI via `$env:AI_WORKFLOW_HUB` |
| CodeGraph | Sidecar | MCP (codegraph_* tools) |
| test-frame | Downstream | Future: CLI trigger from workqueues |

## Governance

- All task completions may propose self-evolution evidence through MemoryUpdateRecord; memory writes remain forbidden in Phase 0-5
- No agent may skip verification gates without explicit human approval

## File System Layout

```
D:\devframe-system\              <- CANONICAL_ROOT
  scripts/                        <- Superproject integration checks
  agent-acceptance/
    scripts/                      <- SADP PowerShell runners (L0-L3)
    agent-workqueue/              <- Tier-graded queue definitions
    skills-inbox/                 <- Incoming skill intake area
    runs/                         <- Historical execution records
    templates/                    <- AGENTS and queue templates
  dev-frame-opencode/             <- Paper workflow implementation
  test-frame/                     <- Test orchestration implementation
  devframe-control-plane/         <- Frozen runtime orchestration candidate
  docs/
    agent-runtime/                <- Runtime documentation (this file set)
  templates/                      <- AGENTS and queue templates
  .codegraph/                     <- Code intelligence index
```

## Constraint Enforcement

| Constraint | Mechanism |
|------------|-----------|
| No fake green | Exit code contract enforced by runners |
| Dry-run default | Runners require explicit -Real/-Apply flags |
| Tier 2 escalation | WorkQueue runner blocks Tier 2 without upgrade |
