# TS-CONTROL-PLANE-LEASE-LOCK

Date: 2026-06-15
Owner thread: `019ec6c4-a05c-7053-966e-a260f5b51aa1`
Target path: `D:\devframe-system\devframe-control-plane`
Suggested branch: `codex/lease-source-lock-contracts`

## Objective

Define the control-plane contract inputs for WorkerLease, SourceLock,
heartbeat, cancellation, stale completion, duplicate dispatch, and audit.

## Scope

- Add or update schemas/docs for `DispatchAssignment`, `WorkerLease`,
  `SourceLock`, `AuditEvent`, and `FailureRecord`.
- Document dry-run and negative cases.
- Preserve boundary: dispatch success is not task success.

## Forbidden

- Do not start control-plane runtime, doctor, run, worker, or dispatch.
- Do not run pytest, npm, or external runtime.

## Required Report

Reviewer Index with changed files, critical paths, commands run, verification
verdict, known gaps, and suggested review focus.
