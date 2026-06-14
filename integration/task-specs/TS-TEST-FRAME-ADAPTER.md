# TS-TEST-FRAME-ADAPTER

Date: 2026-06-15
Owner thread: `019ec6c6-5238-74b3-8870-c973bee56131`
Target path: `D:\devframe-system\test-frame`
Suggested branch: `codex/adapter-negative-matrix`

## Objective

Define test-frame adapter mapping and canary/negative-case strategy for
devframe-system integration.

## Scope

- Map RunSpec, EvidenceManifest, and ExecutionReport into devframe-system
  adapter contracts.
- Document no-tests-run, infra mislabeled pass, optional blocked versus
  required failure, wrong cwd, secret stdout, artifact outside root, and summary
  as final verdict cases.
- Preserve boundary: test-frame is not a plugin and not final verdict source.

## Forbidden

- Do not run pytest, npm, smoke, build, runtime, H5, MiniApp, MeterSphere, cloud
  device, Android, or Maestro.

## Required Report

Reviewer Index with changed files, critical paths, commands run, verification
verdict, known gaps, and suggested review focus.
