# Parent Pin Review: test-frame opencode A46-A48 Capability Map Metadata Scope Consumption

Date: 2026-06-16

## Decision

ACCEPTED_AND_PARENT_PINNED

## Pin Target

- Module: test-frame
- Previous parent pin: fb4367ec33204a87f1d40561dfd4bd617945e440
- New parent pin: 94e66f01dae171c7ef91432ae458a42dfc2be7a0
- Parent lock files updated:
  - D:\devframe-system\BASELINE_LOCK.json
  - D:\devframe-system\integration\lock\submodules.lock.yml

## Lock State

- BASELINE_LOCK.json test-frame commit: 94e66f01dae171c7ef91432ae458a42dfc2be7a0
- integration/lock/submodules.lock.yml test-frame commit: 94e66f01dae171c7ef91432ae458a42dfc2be7a0
- gitlink staged for test-frame: 94e66f01dae171c7ef91432ae458a42dfc2be7a0
- dev-frame-opencode remains pinned in parent HEAD: 1cba29d25fc02dac17ef7bd17ce70cf0d0e5a1be

## Evidence Recorded

- D:\devframe-system\test-frame\reports\evidence-opencode-a46-a48-capability-map-metadata-scope-consumption-a1.zip
  - SHA256: 2570E78299042A46D3DA6BE853DD966A670198DFC42809A2782CF70AB877A16F

## Verification Summary

- Evidence ZIP hash matched declared value.
- Synthetic fixture JSON parsed successfully.
- Focused A46-A48 capability map metadata-scope consumption tests: 9 passed.
- Metadata consumption/orchestration regression suite: 80 passed.
- Evidence collector/manifest plus metadata consumption/orchestration suite: 105 passed.
- Generated evidence manifest JSON parsed successfully.
- Evidence ZIP entry listing contained expected command/report/manifest entries only.

## Non-Claims

- Not final governance acceptance.
- Not production-ready.
- Not live-ready beyond synthetic/offline consumption evidence.
- Does not authorize Zotero API/key reads, PDF, attachments, notes, full text, Obsidian, RAG, WriteLab, browser/CDP, cloud, MiniApp, or private paper runtime.

## Dirty-State Note

The parent worktree contains unrelated local governance/runtime drift that was not staged for this pin, including local registry files, parent governance reports, existing modified planning/report index files, modified prior pin-review reports, and untracked status reports. This pin stages only the test-frame gitlink, lock updates, and the two A46-A48 consumption parent reports.
