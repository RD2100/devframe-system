# Submodules

Date: 2026-06-15

This repository uses submodules as the integration boundary. Do not copy source
files across module boundaries unless a reviewed migration plan explicitly says
so.

## Locked Modules

| Path | Project | Role | Branch | Locked commit |
|---|---|---|---|---:|
| `agent-acceptance` | `agent-acceptance` | Governance, acceptance, TaskSpec/Gate0 contracts | `codex/paper-archive-final-verdict-boundary` | `38d7b2e0aad226cce5732cb4d56e45ae2d065ec7` |
| `devframe-control-plane` | `devframe-control-plane` | Queue/dispatch/control-plane candidate | `codex/lease-source-lock-contracts` | `b001cea174e3a4224bea68786adbb10cd82ce84f` |
| `dev-frame-opencode` | `dev-frame-opencode` | Controlled coding runtime candidate | `codex/paper-audit-privacy-hard-gate` | `08ac4f593006d62bf5b096133dfe9212cce8e49f` |
| `test-frame` | `test-frame` | Controlled verification runtime candidate | `codex/adapter-negative-matrix` | `891b10658c69356cd5a587c3f120fdfdc2b9cb8d` |

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
