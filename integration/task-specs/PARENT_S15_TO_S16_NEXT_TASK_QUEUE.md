# Parent S15 To S16 Next Task Queue

Date: 2026-06-16
Parent repo: `D:\devframe-system`
Status: `TASK_QUEUE_READY_NOT_DISPATCHED`

## Purpose

This queue provides scoped next TaskSpecs after the S15 metadata MVP parent
closeout. It does not dispatch work by itself and does not authorize live
runtime.

## Sequencing Rule

Run these in order unless the parent coordinator explicitly changes the order:

1. clean or close the test-frame local drift;
2. package opencode post-baseline runtime/resource drift for review;
3. update parent artifact registry only after clean child returns;
4. choose at most one real runtime track for future authorization.

## TaskSpec 1 - TESTFRAME_REAL_PILOT_EVIDENCE_BINDING_LOCAL_CLOSEOUT_A1

Module:

- `D:\devframe-system\test-frame`

Observed starting state:

- parent-pinned baseline: `52483575cc94c097f1be57f7ed3d0d7a80940d32`
- current checkout observed: `9673891bb2939ea2d415caba8303cdd793b3a237`
- local dirty files observed:
  - `M docs/test-frame/paper-pipeline-metadata-only/README.md`
  - `?? docs/test-frame/paper-pipeline-metadata-only/opencode-real-pilot-evidence-binding-consumption.fixture.json`
  - `?? tests/test_opencode_real_pilot_evidence_binding_consumption.py`

Goal:

- either complete this local test-frame slice into a clean commit with
  ExecutionReport, Reviewer Index, evidence ZIP, and tests; or explicitly
  return a blocker/rework note.

Allowed:

- test-frame docs/fixtures/tests only;
- synthetic/offline replay only;
- generated test-frame reports/evidence ZIP.

Forbidden:

- reading `C:\Users\RD\key\zotero.txt`;
- calling Zotero API;
- reading raw API response, title, abstract, item JSON, raw user id, PDF,
  attachments, notes, full text, or paragraph_text;
- invoking WriteLab, Obsidian, live RAG, browser/CDP, cloud, MiniApp, or
  external runtime;
- updating parent lock/pin;
- claiming final governance acceptance.

Expected verification:

- JSON parse for any new fixture;
- focused pytest for the new consumption test;
- recent metadata/governance consumption regression;
- evidence manifest JSON parse if generated;
- `git diff --check`;
- clean tracked worktree after commit.

Return:

- commit hash;
- changed files;
- tests run;
- evidence ZIP path and SHA256;
- known gaps;
- boundary confirmation.

## TaskSpec 2 - OPENCODE_POST_S15_RESOURCE_DRIFT_REVIEW_PACKET_A1

Module:

- `D:\devframe-system\dev-frame-opencode`

Observed starting state:

- parent-pinned baseline: `a914e5da642b0aa9484e877cabf5de553d5a7379`
- current checkout observed: `13403c3ddac5b70d6d1cdddb965b4c4e1cc1e476`
- observed commits beyond baseline:
  - `9b57f72` Add PDF redacted excerpt pilot
  - `f71a02b` Add WriteLab boundary pilot
  - `1683d7e` Bind plugin pilots to business validation
  - `460c84d` Add Obsidian allowlisted note pilot
  - `9e211a5` Add RAG local fixture pilot
  - `f25eab2` Add plugin pilot closeout report
  - `13403c3` Bind paper real pilot evidence in business validation

Goal:

- produce a review packet that classifies each post-S15 opencode commit by
  resource class, evidence type, runtime use, authorization requirement, and
  parent intake risk.

Allowed:

- local/offline inspection of committed code and generated minimized reports;
- docs/reports only unless a narrow test is required to prove classification;
- no new live runtime.

Forbidden:

- new Zotero API calls;
- key-file reads;
- PDF/full-text/private note processing;
- live Obsidian/RAG/WriteLab/browser/cloud/MiniApp execution;
- claiming these commits are accepted or parent-pinned;
- changing parent lock.

Expected output:

- a clean opencode commit or a report-only return, depending on module policy;
- ExecutionReport and Reviewer Index;
- clear per-commit classification:
  - metadata MVP compatible;
  - runtime-resource candidate;
  - human-required;
  - no-go for parent S15.

Parent review focus:

- do not batch accept multiple new resource classes as one broad runtime grant;
- keep PDF/WriteLab/Obsidian/RAG/plugin evidence separate;
- require fresh authorization before any live/runtime expansion.

## TaskSpec 3 - PARENT_S16_ARTIFACT_REGISTRY_HARDENING_A1

Module:

- parent repo only: `D:\devframe-system`

Goal:

- consolidate accepted parent evidence into a single registry/index without
  absorbing unreviewed drift.

Allowed:

- `integration/reports/`;
- `integration/contracts/`;
- parent-local read-only hash/status checks.

Forbidden:

- editing submodule business code;
- staging local registry/cache drift;
- executing ZIP contents;
- live runtime;
- final acceptance claim.

Expected output:

- parent evidence registry report or index;
- accepted baseline section;
- quarantined drift section;
- one-module-at-a-time intake queue.

## TaskSpec 4 - PARENT_S16_SINGLE_RUNTIME_TRACK_SELECTION_A1

Module:

- parent repo only: `D:\devframe-system`

Goal:

- choose exactly one future runtime/resource track to open after S15, or record
  that no runtime track will open yet.

Allowed:

- planning and authorization checklist only.

Forbidden:

- running the selected track;
- broad multi-track authorization;
- final acceptance.

Candidate tracks:

- Zotero metadata-only follow-up;
- PDF redacted excerpt;
- WriteLab boundary;
- Obsidian allowlisted note;
- local RAG fixture;
- browser/cloud/MiniApp;
- control-plane dispatch;
- CI/canary/rollback.

Expected output:

- one selected track or explicit hold;
- required RuntimeAuthorization fields;
- forbidden resources;
- evidence minimization rules;
- rollback/stop conditions.

## Queue Verdict

This queue is ready for use, but it is not a dispatch event.

Parent state remains:

`S15_METADATA_MVP_PARENT_CLOSED_WITH_FINALITY_BLOCKED`
