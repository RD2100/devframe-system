# Submodules

Date: 2026-06-15

This repository uses submodules as the integration boundary. Do not copy source
files across module boundaries unless a reviewed migration plan explicitly says
so.

## Locked Modules

| Path | Project | Role | Branch | Locked commit |
|---|---|---|---|---:|
| `agent-acceptance` | `agent-acceptance` | Governance, acceptance, TaskSpec/Gate0 contracts | `codex/paper-archive-final-verdict-boundary` | `3cf2c9be9f33ddabdc029a652dca512d8193a5e5` |
| `devframe-control-plane` | `devframe-control-plane` | Queue/dispatch/control-plane candidate | `codex/lease-source-lock-contracts` | `79399541b8426cff0f362b665bad09e3c23e974b` |
| `dev-frame-opencode` | `dev-frame-opencode` | Controlled coding runtime candidate | `codex/paper-audit-privacy-hard-gate` | `0c24204fd99e6cab1d853ecadb12200244119fe1` |
| `test-frame` | `test-frame` | Controlled verification runtime candidate | `codex/adapter-negative-matrix` | `bdd7b67a4bb9cfee2c6601c2f755abfd68164da7` |

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
