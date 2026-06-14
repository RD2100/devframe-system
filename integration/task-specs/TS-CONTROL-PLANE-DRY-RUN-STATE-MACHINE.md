# TS-CONTROL-PLANE-DRY-RUN-STATE-MACHINE

Date: 2026-06-15
Owner thread: `019ec6c4-a05c-7053-966e-a260f5b51aa1`
Target path: `D:\devframe-system\devframe-control-plane`
Expected branch: `codex/lease-source-lock-contracts`
Expected base HEAD: `c3edf8528cb853c023929c2c26fef208177e2198`

## Objective

Advance the control-plane contract probe into a minimal pure in-memory dry-run
state machine or validator for dispatch assignment, lease, heartbeat,
completion, cancellation, and failure transitions.

## Scope

- Reuse `runtime_contract_probe.py` where possible.
- Add tests for duplicate dispatch, stale lease completion, overlapping
  SourceLock, cancellation after completion, retry of non-retryable failure,
  and dispatch-success promotion.
- Preserve the boundary that control-plane does not produce task success,
  governance acceptance, or final verdict.

## Forbidden

- Do not start control-plane runtime, doctor, run, worker, or dispatch.
- Do not run external runtime.
- Do not refactor CLI.
- No push/reset/clean/stash.

## Required Report

ExecutionReport and Reviewer Index with branch, commit hash, changed files,
critical paths, tests run, generated artifacts, known gaps, and review focus.
