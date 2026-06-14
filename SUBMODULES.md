# Submodules

Date: 2026-06-15

This repository uses submodules as the integration boundary. Do not copy source
files across module boundaries unless a reviewed migration plan explicitly says
so.

## Locked Modules

| Path | Project | Role | Branch | Locked commit |
|---|---|---|---|---:|
| `agent-acceptance` | `agent-acceptance` | Governance, acceptance, TaskSpec/Gate0 contracts | `codex/paper-archive-final-verdict-boundary` | `f3abb202a9d58044718d3e5b9b920bef8e4000e8` |
| `devframe-control-plane` | `devframe-control-plane` | Queue/dispatch/control-plane candidate | `codex/lease-source-lock-contracts` | `c3edf8528cb853c023929c2c26fef208177e2198` |
| `dev-frame-opencode` | `dev-frame-opencode` | Controlled coding runtime candidate | `codex/paper-audit-privacy-hard-gate` | `b805658a2c9111ab839749ed81a210305127d42d` |
| `test-frame` | `test-frame` | Controlled verification runtime candidate | `codex/adapter-negative-matrix` | `93b95b98e59dbf0ca0bc060c949eb7fa53f3b3ef` |

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
