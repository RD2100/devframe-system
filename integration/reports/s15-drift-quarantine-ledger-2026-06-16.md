# S15 Drift Quarantine Ledger

Date: 2026-06-16
Parent repo: `D:\devframe-system`
Status: `DRIFT_QUARANTINED_NOT_PARENT_ACCEPTED`

## Purpose

This ledger separates the parent S15 metadata MVP baseline from current local
workspace drift. It is a quarantine record only. It does not accept, reject,
clean, reset, stash, or pin any drift.

## Parent Baseline

Authoritative parent baseline comes from parent HEAD gitlinks and the committed
lock file:

| Module | Parent-pinned commit |
|---|---|
| `agent-acceptance` | `6b9a83c1dca0ea650dbc7e97f13977ac02e3e3ee` |
| `dev-frame-opencode` | `a914e5da642b0aa9484e877cabf5de553d5a7379` |
| `devframe-control-plane` | `09167bc656f8625c97bfae5c52dae5a0280b116c` |
| `test-frame` | `52483575cc94c097f1be57f7ed3d0d7a80940d32` |

Verification commands:

- `git ls-tree HEAD agent-acceptance dev-frame-opencode devframe-control-plane test-frame`
- `git show HEAD:integration/lock/submodules.lock.yml`

## Current Drift Snapshot

| Area | Observed state | Quarantine class | Parent action now |
|---|---|---|---|
| `.agent/PROJECT_REGISTRY.json` | modified | local workspace registry drift | do not stage in S15 closeout |
| `agent-acceptance` | local submodule has `.agent/PROJECT_REGISTRY.json` modified | local runtime registry drift | do not stage without separate TaskSpec |
| `dev-frame-opencode` | checkout at `13403c3ddac5b70d6d1cdddb965b4c4e1cc1e476`, parent pin at `a914e5d...` | candidate child drift | requires separate parent intake |
| `test-frame` | checkout at `9673891bb2939ea2d415caba8303cdd793b3a237`, parent pin at `5248357...`; working tree has modified/untracked files | candidate child drift plus uncommitted local drift | requires child cleanup/return before parent intake |
| parent reports | multiple modified and untracked `integration/reports/*.md` | historical parent drift | do not treat as S15 closeout evidence |
| parent runtime-pilot reports | untracked `integration/reports/runtime-pilots/` | runtime evidence drift | quarantine from S15 metadata MVP |
| parent task specs | untracked PDF/WriteLab pilot TaskSpecs | future runtime track drafts | design-only until explicitly opened |
| Python caches | untracked `scripts/__pycache__`, `tests/__pycache__` | local generated cache | do not stage |

## Opencode Drift Queue

The current opencode checkout contains these commits beyond parent baseline:

| Commit | Message | S15 treatment |
|---|---|---|
| `9b57f72` | Add PDF redacted excerpt pilot | outside metadata MVP baseline; requires runtime/resource review |
| `f71a02b` | Add WriteLab boundary pilot | outside metadata MVP baseline; requires runtime/resource review |
| `1683d7e` | Bind plugin pilots to business validation | not parent accepted |
| `460c84d` | Add Obsidian allowlisted note pilot | outside metadata MVP baseline; requires resource review |
| `9e211a5` | Add RAG local fixture pilot | outside metadata MVP baseline; requires resource review |
| `f25eab2` | Add plugin pilot closeout report | not parent accepted |
| `13403c3` | Bind paper real pilot evidence in business validation | not parent accepted |

Parent may review these later, but they must not be included in the S15
metadata MVP baseline without a separate return, evidence review, and parent
pin.

## Test-frame Drift Queue

The current test-frame checkout contains these commits beyond parent baseline:

| Commit | Message | S15 treatment |
|---|---|---|
| `b657723` | Add opencode A61 A62 preauth clock checks | not parent accepted in this baseline |
| `9673891` | Add opencode A63 A64 manifest uniqueness checks | not parent accepted in this baseline |

The test-frame working tree also has:

- `M docs/test-frame/paper-pipeline-metadata-only/README.md`
- `?? docs/test-frame/paper-pipeline-metadata-only/opencode-real-pilot-evidence-binding-consumption.fixture.json`
- `?? tests/test_opencode_real_pilot_evidence_binding_consumption.py`

These uncommitted files cannot be parent-pinned. They require child-side
completion or explicit discard/cleanup instruction before parent intake.

## Quarantine Rules

1. Drift is not evidence.
2. Uncommitted child work cannot be parent-pinned.
3. A clean child commit is still not parent-accepted until parent review.
4. Runtime-resource drift cannot enter metadata MVP baseline.
5. Existing dirty parent reports are not part of S15 closeout unless separately
   staged and reviewed.
6. Local registry/cache drift should remain uncommitted unless a TaskSpec says
   otherwise.

## Safe Next Actions

Safe parent actions:

- write parent drift ledgers and closeout docs;
- review a clean child return with evidence ZIP and SHA256;
- pin one module at a time after explicit parent intake;
- keep runtime tracks design-only until authorized.

Unsafe parent actions:

- stage all modified parent reports blindly;
- pin test-frame while it has uncommitted local drift;
- include opencode PDF/WriteLab/Obsidian/RAG/plugin drift in S15 metadata MVP;
- treat runtime-pilot reports as final evidence;
- clean/reset/stash without explicit user instruction.

## Current Verdict

Drift state:

`QUARANTINED`

S15 baseline state remains:

`METADATA_MVP_PARENT_CLOSED_WITH_FINALITY_BLOCKED`
