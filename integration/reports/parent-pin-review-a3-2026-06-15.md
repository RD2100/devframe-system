# devframe-system Parent Pin Review A3

Date: 2026-06-15
Scope: parent-only pin review after post-A2 submodule drift
Runtime: not executed by parent
Parent action: no pin, no lock mutation, no gitlink update
Verdict: `PIN_NO_GO_ACTIVE_SUBMODULE_DRIFT`

## 1. Executive Decision

`parent-pin-review-a2-2026-06-15.md` remains a valid historical snapshot, but it
is no longer the current pin basis.

Fresh read-only inspection found new active drift after A2:

- `dev-frame-opencode` is dirty again after its accepted local/offline return.
- `test-frame` has advanced from the previously reviewed `eed8d88...` to
  `6eed627...` and has tracked plus untracked dirty state.

Therefore the parent must not prepare or apply a pin now.

## 2. Fresh Observed State

| Module | Branch | HEAD | Worktree | Parent interpretation |
|---|---|---|---|---|
| `agent-acceptance` | `codex/paper-archive-final-verdict-boundary` | `b9bb53a72bbd7b4c4e4402aca11b4cc67f9506f5` | old untracked evidence remains | intake accepted with dirty-note; not enough alone to pin |
| `dev-frame-opencode` | `codex/paper-audit-privacy-hard-gate` | `9d4c2f62c636d91641c5843c43eaa896fbba5243` | tracked dirty files in metadata-only Zotero pilot docs, adapter, and tests | post-return drift observed; requires final return or coordinator decision before pin |
| `devframe-control-plane` | `codex/lease-source-lock-contracts` | `79399541b8426cff0f362b665bad09e3c23e974b` | clean | frozen and already aligned |
| `test-frame` | `codex/adapter-negative-matrix` | `6eed627 Tighten evidence pack path scan` | tracked dirty files plus untracked closeout/test tooling | new unreviewed drift; previous `eed8d88...` intake is superseded for pin purposes |

## 3. Drift Details

`dev-frame-opencode` dirty diff summary:

- `ai-workflow-hub/docs/paper/PAPER_REAL_ZOTERO_METADATA_ONLY_PILOT.md`
- `ai-workflow-hub/src/ai_workflow_hub/context_layer/adapters/zotero_metadata_real_pilot.py`
- `ai-workflow-hub/tests/test_paper_real_zotero_metadata_only_pilot.py`
- diff size: 225 insertions, 22 deletions.

`test-frame` dirty diff summary:

- `cli/main.py`
- `docs/agent-runtime/capability-inventory.md`
- `docs/governance/DOC_COMMAND_AUDIT.md`
- untracked `tests/closeout/`
- untracked `tools/generate_tgm_miniapp_readiness_closeout.py`
- diff size: 47 insertions.

## 4. Superseded Pin Candidate State

A2 candidate pins were:

- `agent-acceptance` -> `b9bb53a72bbd7b4c4e4402aca11b4cc67f9506f5`
- `dev-frame-opencode` -> `9d4c2f62c636d91641c5843c43eaa896fbba5243`
- `test-frame` -> `eed8d88e65684b58b7fe478736eb0a47376fa17e`
- `devframe-control-plane` unchanged at
  `79399541b8426cff0f362b665bad09e3c23e974b`

Current parent interpretation:

- `agent-acceptance` can remain an intake candidate with a local evidence
  dirty-note.
- `dev-frame-opencode` is no longer pin-ready until the new dirty state is
  closed or explicitly accepted.
- `test-frame` is no longer pin-ready because the reviewed candidate commit was
  superseded by a newer HEAD and active dirty state.
- `devframe-control-plane` remains frozen and aligned.

## 5. Required Before Any Parent Pin

Before a parent pin proposal can continue, the coordinator needs one of:

- final module return from `dev-frame-opencode` covering the new dirty state;
- final module return from `test-frame` covering `6eed627...` and current dirty
  state;
- explicit coordinator instruction to ignore current dirty state and pin a
  prior reviewed commit;
- explicit human approval to update parent gitlinks and lock files despite the
  observed drift.

## 6. Current No-Go

Do not pin now.

Do not mutate:

- parent submodule gitlinks;
- `integration/lock/submodules.lock.yml`;
- `BASELINE_LOCK.json`;
- historical evidence archives.

This review does not authorize real Zotero, real Obsidian, live RAG, WriteLab,
MiniApp real runtime, browser/CDP, cloud, private paper content, or final-ready
claims.
