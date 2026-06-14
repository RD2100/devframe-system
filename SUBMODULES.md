# Submodules

Date: 2026-06-15

This repository uses submodules as the integration boundary. Do not copy source
files across module boundaries unless a reviewed migration plan explicitly says
so.

## Locked Modules

| Path | Project | Role | Branch | Locked commit |
|---|---|---|---|---:|
| `agent-acceptance` | `agent-acceptance` | Governance, acceptance, TaskSpec/Gate0 contracts | `codex/devframe-system-path-gate0-contract` | `88dd58183e705f1df07c32b690ab56766c643642` |
| `devframe-control-plane` | `devframe-control-plane` | Queue/dispatch/control-plane candidate | `codex/lease-source-lock-contracts` | `49c6be859dd726092fc433cc18cb7ea9537498da` |
| `dev-frame-opencode` | `dev-frame-opencode` | Controlled coding runtime candidate | `codex/paper-governance-finalizer-boundary` | `ee08dd181fc992eed3f58754038375933c31145b` |
| `test-frame` | `test-frame` | Controlled verification runtime candidate | `codex/adapter-negative-matrix` | `71caa1c242d9a85d185c4e29ee24eb078183ffd5` |

## Boundary Rules

- `agent-acceptance` owns governance contracts and acceptance policy.
- `devframe-control-plane` owns dispatch/control-plane candidate behavior.
- `dev-frame-opencode` owns controlled coding runtime evidence.
- `test-frame` owns controlled verification runtime evidence. It is not a plugin
  and not a final verdict source.
- `devframe-system` owns integration contracts, submodule pins, evidence policy,
  and cross-module readiness gates.

## Required Checks

Run these from `D:\devframe-system`:

```powershell
git submodule status --recursive
git status --porcelain=v1 -uall
git diff --check
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\check-submodules.ps1
```
