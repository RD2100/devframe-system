# devframe-system

Route A strict-clean superproject for the devframe family.

This repository pins four source repositories as Git submodules. It does not
copy source code across repository boundaries.

## Submodules

| Path | Role | Branch | Pinned commit |
|---|---|---|---|
| `agent-acceptance` | Governance and acceptance framework | `master` | `285d5c906a074ce7c689c8f656caabbdb32af8dc` |
| `devframe-control-plane` | Control-plane runtime candidate | `codex/route-a-baseline-candidate` | `311847818927d3c7ec8c8718949b38c74605fc83` |
| `dev-frame-opencode` | Opencode workflow/runtime candidate | `master` | `3a3aa5722bd6015bec30a8e9190140148b45167c` |
| `test-frame` | Controlled verification runtime candidate | `codex/harden-baseline` | `aeb4a31f770e35e7f698e5c3169406ddba231a4d` |

## Boundary

- Physical merge type: superproject plus submodules.
- No source squashing or monorepo copy was performed.
- No external runtime was executed during bootstrap.
- Each source repository was clean before pinning.
- `dev-frame-opencode` local tests were verified before pinning:
  `python -m pytest tests -q` -> `2451 passed, 2 skipped, 3 warnings`.

## Verify

```powershell
git submodule status --recursive
git status --porcelain=v1 -uall
git diff --check
```
