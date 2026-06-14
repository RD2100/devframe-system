# GitLab CI Read-only Policy

Date: 2026-06-15

The first GitLab CI stage for `devframe-system` is read-only by design.

## Allowed Commands

- `git status --short --branch`
- `git submodule status --recursive`
- `git diff --check`
- `powershell -NoProfile -ExecutionPolicy Bypass -File scripts/check-submodules.ps1`
- `powershell -NoProfile -ExecutionPolicy Bypass -File scripts/readonly-inventory.ps1`

## Forbidden Commands

- `pytest`, `npm test`, `pnpm test`, `yarn test`, `go test`, `cargo test`,
  `mvn test`, `gradle test`
- OpenCode runtime
- control-plane doctor, run, worker, dispatch, or pipeline execution
- test-frame runtime, browser tests, H5, MiniApp, MeterSphere, cloud device, or
  Android runtime
- package install or build commands
- deployment commands
- git mutation commands such as `commit`, `push`, `reset`, `clean`, `stash`

## Required Job Meaning

The read-only CI job may report inventory health only. It must not report final
acceptance, readiness for live runtime, or production safety.
