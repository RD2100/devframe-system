# TS-OPENCODE-RUNTIME-AUTH

Date: 2026-06-15
Owner thread: `019ec6c5-7d65-76e2-b9a6-9316c75aeae8`
Target path: `D:\devframe-system\dev-frame-opencode`
Suggested branch: `codex/runtime-authorization-contract`

## Objective

Define opencode controlled runtime adapter boundaries for RuntimeAuthorization,
write_set, preflight, post-run safety, ExecutionReport, and EvidenceManifest.

## Scope

- Document required RuntimeAuthorization fields.
- Separate pre-write prevention from post-run violation detection.
- Add negative-case guidance for exit code, timeout, stdout/stderr, forbidden
  paths, missing reviewer artifacts, and write_set bypass.

## Forbidden

- Do not run opencode.
- Do not run paper workflow, A121/A122, pack/validate scripts, pytest, or npm.

## Required Report

Reviewer Index with changed files, critical paths, commands run, verification
verdict, known gaps, and suggested review focus.
