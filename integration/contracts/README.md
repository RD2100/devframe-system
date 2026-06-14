# Integration Contracts

Date: 2026-06-15

This directory contains devframe-system-level contract guidance. Source module
schemas remain owned by their source repositories and by the bootstrapped SADP
schemas under `schemas/agent-runtime/`.

## Contract Boundaries

| Contract | Owner | Purpose |
|---|---|---|
| `TaskSpec` | `agent-acceptance` | User intent, scope, allowed actions, evidence requirements |
| `Gate0Preflight` | `agent-acceptance` | Human gates, capability status, binding freshness |
| `RuntimeAuthorization` | `devframe-system` + human approver | Explicit permission to run controlled runtime |
| `DispatchAssignment` | `devframe-control-plane` | Worker assignment, idempotency, lease inputs |
| `WorkerLease` | `devframe-control-plane` | Prevent stale or overlapping worker completion |
| `SourceLock` | `devframe-control-plane` | Prevent overlapping writes across workers |
| `ExecutionReport` | runtime provider | Exit code, stdout/stderr, diff, changed files, evidence |
| `EvidenceManifest` | runtime provider + reviewer | Hashes, paths, freshness, provenance |
| `ReviewVerdict` | independent reviewer | Review outcome independent from executor |
| `FinalVerdict` | governance layer | Final go/no-go after all evidence is reviewed |

## Hard Rule

No contract may promote its own success to a later layer. For example,
dispatch success is not execution success, execution success is not review
success, and review success is not governance final acceptance.
