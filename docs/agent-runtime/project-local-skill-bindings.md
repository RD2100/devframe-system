# Project-Local Skill Bindings

> Scope: `D:\devframe-system`
> Status: active for this superproject

This file defines how project-local skills and agent conversations must resolve
paths after the four modules were merged under the `devframe-system`
superproject.

## Canonical Roots

| ID | Role | Root |
|---|---|---|
| `devframe-system` | Superproject governance and integration root | `D:\devframe-system` |
| `agent-acceptance` | Acceptance, SADP gates, review artifacts | `D:\devframe-system\agent-acceptance` |
| `dev-frame-opencode` | Paper workflow and ai-workflow-hub implementation | `D:\devframe-system\dev-frame-opencode` |
| `test-frame` | TestFrame orchestration and time-goal-manager integration | `D:\devframe-system\test-frame` |
| `devframe-control-plane` | Runtime orchestration candidate, currently frozen | `D:\devframe-system\devframe-control-plane` |

## `/rdinit`

For this project, `/rdinit` must treat `D:\devframe-system` as the canonical
project root.

Required paths:

- Registry: `D:\devframe-system\.agent\PROJECT_REGISTRY.json`
- Bootstrap script: `D:\devframe-system\templates\runtime-bootstrap\bootstrap.ps1`
- Runtime template source: resolved from the bootstrap script location, not a
  hard-coded external checkout.

`D:\agent-acceptance` is a legacy standalone root. Do not use it for this
superproject unless the user explicitly asks to operate on that old checkout.

## `/bindChrome`

For this project, `/bindChrome` must bind conversations against the local
registry and local module roots.

Required paths:

- Registry: `D:\devframe-system\.agent\PROJECT_REGISTRY.json`
- Superproject binding: `D:\devframe-system\.agent\CONVERSATION_BINDING.json`
- Shared Chrome profile: `D:\devframe-system\.agent\_cdp_profiles\shared`
- Optional per-module bindings:
  `D:\devframe-system\.agent\bindings\<project_id>\CONVERSATION_BINDING.json`

Per-module binding files should stay under the superproject `.agent` directory
unless a task explicitly requires writing inside a submodule. This avoids making
submodules dirty just because a conversation URL changed.

## Dispatch Rule

TaskSpecs sent to module agents must use absolute paths from the registry. The
goal agent should not infer roots from old prompts, browser tabs, or legacy
handoff text.

Minimum TaskSpec path fields:

```yaml
superproject_root: "D:\devframe-system"
target_project_id: "<project_id>"
target_project_root: "<registry.projects[project_id].root>"
allowed_write_roots:
  - "<target_project_root>"
```

For cross-module governance work, the allowed write roots must be explicit. A
module agent may read the superproject integration docs, but it must not write
outside its assigned module unless the TaskSpec names that path.
