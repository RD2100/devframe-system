# Parent Pin Review: opencode Metadata Pipeline Readiness Batch A39-A40

Date: 2026-06-16

## Decision

ACCEPTED_AND_PARENT_PINNED

## Pin Target

- Module: dev-frame-opencode
- Previous parent pin: 9574c71c011bc975575b9d5d301965adb3e21284
- New parent pin: 628ac87b3adafb399edab3faf2995d183c4f43e0
- Parent lock files updated:
  - D:\devframe-system\BASELINE_LOCK.json
  - D:\devframe-system\integration\lock\submodules.lock.yml

## Hash Correction

Delegation short hash `628ac87` matched, but the reported full hash `628ac87c655cf39db20972e2640bf0d31116a7fd` was not found locally. The verified submodule HEAD and staged gitlink use `628ac87b3adafb399edab3faf2995d183c4f43e0`.

## Lock State

- BASELINE_LOCK.json dev-frame-opencode commit: 628ac87b3adafb399edab3faf2995d183c4f43e0
- integration/lock/submodules.lock.yml dev-frame-opencode commit: 628ac87b3adafb399edab3faf2995d183c4f43e0
- gitlink staged for dev-frame-opencode: 628ac87b3adafb399edab3faf2995d183c4f43e0

## Evidence Recorded

- D:\devframe-system\.agent\evidence\evidence-opencode-paper-metadata-pipeline-readiness-a1-d320d1d.zip
  - SHA256: 0F497D446FC72CAEBF18A487DEFCFCD2F9008BF981424292B6564BFAF1DE69F2
- D:\devframe-system\.agent\evidence\evidence-opencode-metadata-pipeline-business-binding-a1-628ac87.zip
  - SHA256: 732184CF14F0BBB446DD06ACE8AE7388B4E3E2EEE05C4C287E7C456B3438C735

## Verification Summary

- Evidence ZIP hashes matched declared values.
- Focused metadata readiness tests: 4 passed.
- Business validation plus metadata readiness tests: 16 passed.
- Expanded metadata/paper regression suite: 105 passed.
- Metadata pipeline readiness and business validation schemas parsed with `python -m json.tool`.
- Module diff check from 9574c71 to 628ac87b passed.

## Non-Claims

- Not final governance acceptance.
- Not production-ready.
- Not live-ready beyond local/offline metadata-only readiness evidence.
- Does not authorize Zotero key/API reads, notes, attachments, PDF, full text, Obsidian, RAG, WriteLab, browser/CDP, cloud, MiniApp, or private paper runtime.

## Dirty-State Note

The parent worktree contains unrelated local governance/runtime drift that was not staged for this pin, including local registry files, parent governance reports, existing modified planning/report index files, modified prior pin-review reports, and current test-frame drift. This pin stages only the opencode gitlink, lock updates, and the two A39-A40 parent reports.
