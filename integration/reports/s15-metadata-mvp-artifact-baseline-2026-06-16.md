# S15 Metadata MVP Artifact Baseline

Date: 2026-06-16
Parent repo: `D:\devframe-system`
Parent HEAD observed: `dbb0605 Add S15 contract ownership index`
Status: `METADATA_MVP_BASELINE_INDEXED`

## Purpose

This report records the parent-committed metadata MVP baseline after the S15
boundary kernel. It separates accepted parent state from local checkout drift.

It is not a final governance acceptance report.

## Parent-committed Lock Set

The parent HEAD gitlinks and committed lock file currently agree on this set:

| Module | Parent-pinned commit | S15 classification |
|---|---|---|
| `agent-acceptance` | `6b9a83c1dca0ea650dbc7e97f13977ac02e3e3ee` | governance rule-center candidate |
| `dev-frame-opencode` | `a914e5da642b0aa9484e877cabf5de553d5a7379` | metadata/runtime-authorization schema hardening candidate |
| `devframe-control-plane` | `09167bc656f8625c97bfae5c52dae5a0280b116c` | frozen runtime candidate |
| `test-frame` | `52483575cc94c097f1be57f7ed3d0d7a80940d32` | synthetic/offline verification candidate |

Verification source:

- `git ls-tree HEAD agent-acceptance dev-frame-opencode devframe-control-plane test-frame`
- `git show HEAD:integration/lock/submodules.lock.yml`

## Latest Parent-accepted Evidence Anchors

| Track | Parent commit | Evidence | SHA256 | Boundary |
|---|---|---|---|---|
| Opencode A67-A68 runtime authorization set fields | `3c519c797cf210ad5a5c8dfa12c2116514cf1668` | `D:\devframe-system\.agent\evidence\evidence-opencode-runtime-auth-request-set-fields-batch-a67-a68-a914e5d.zip` | `4178A7E9730E6F7181F3B2F8EAB3B93495E320D63992413AF19B7C7CEBC05EA0` | local/offline schema hardening only |
| Test-frame A59-A60 real-pilot set-like consumption | `dd61da4e0ee2566ab85df345571188862cabdfdf` | `D:\devframe-system\test-frame\reports\evidence-opencode-a59-a60-real-pilot-set-like-fields-consumption-a1.zip` | `642BA1DCA6206E3B28063740566592CBBC334730D695B0E06D4FBBE62C3CA426` | synthetic/offline consumption only |
| Agent-acceptance rule-center closeout | previously parent-pinned | `D:\devframe-system\.agent\evidence\evidence-agent-acceptance-rule-center-closeout-a1-6b9a83c.zip` | `E8D34A283609659EAF27CB84B239F07D2ED3180C10281D18323517BA675247C9` | governance rule-center closeout only |

## Accepted Capability Scope

This baseline supports:

- parent intake and pin workflow;
- metadata-only Zotero governance evidence;
- runtime-authorization schema hardening evidence;
- synthetic/offline test-frame consumption checks;
- evidence hash/report provenance checks;
- non-final capability and business-validation reporting;
- parent boundary and finality blocker documentation.

## Explicitly Not Accepted

This baseline does not accept:

- final governance acceptance;
- production readiness;
- live-ready status;
- broad RuntimeAuthorization grant;
- control-plane dispatch activation;
- CI/CD runner activation;
- canary or rollback drill execution;
- live Zotero app/local database access;
- new Zotero Web API reads beyond previously authorized scoped reports;
- PDF, attachments, notes, full text, or private paper text;
- Obsidian vault, RAG/vector store, WriteLab live runtime, browser/CDP, cloud,
  or MiniApp execution.

## Current Local Checkout Drift

Current working checkout is ahead of the parent baseline:

| Module | Parent-pinned commit | Working checkout observed | Drift status |
|---|---|---|---|
| `dev-frame-opencode` | `a914e5da642b0aa9484e877cabf5de553d5a7379` | `f25eab2733a06932b8872fe4fa20e877b82d41b5` | not parent-accepted in this baseline |
| `test-frame` | `52483575cc94c097f1be57f7ed3d0d7a80940d32` | `9673891bb2939ea2d415caba8303cdd793b3a237` | not parent-accepted in this baseline |

The opencode checkout includes later local commits with names indicating plugin,
RAG, Obsidian, WriteLab, and PDF pilot work. These are not included in this S15
metadata MVP baseline and must not be used as accepted parent evidence until
separately reviewed and pinned.

The test-frame checkout includes later local consumption checks beyond A59-A60.
These are also outside this baseline until separately reviewed and pinned.

## Parent Dirty State Not Normalized

This report does not clean, reset, stash, or normalize current local drift.
Known non-baseline state includes:

- `.agent/PROJECT_REGISTRY.json` local drift;
- modified parent reports and project plan files from earlier work;
- untracked parent observation reports;
- untracked `integration/reports/runtime-pilots/`;
- untracked Python cache directories;
- submodule checkout drift.

## Baseline Verdict

Current parent baseline:

`S15_METADATA_MVP_BASELINE_INDEXED_WITH_RUNTIME_NO_GO`

This is enough to continue parent S15 closeout. It is not enough to run or
accept live resource tracks.
