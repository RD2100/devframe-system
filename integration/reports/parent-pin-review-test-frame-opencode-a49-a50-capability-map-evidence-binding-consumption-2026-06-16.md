# Parent Pin Review: test-frame opencode A49-A50 Capability Map Evidence Binding Consumption

Date: 2026-06-16

## Decision

ACCEPTED_AND_PARENT_PINNED

## Pin Target

- Module: test-frame
- Previous parent pin: 94e66f01dae171c7ef91432ae458a42dfc2be7a0
- New parent pin: 1906c4e923a8de91583102ea746ced5754aff083
- Parent lock files updated:
  - D:\devframe-system\BASELINE_LOCK.json
  - D:\devframe-system\integration\lock\submodules.lock.yml

## Lock State

- BASELINE_LOCK.json test-frame commit: 1906c4e923a8de91583102ea746ced5754aff083
- integration/lock/submodules.lock.yml test-frame commit: 1906c4e923a8de91583102ea746ced5754aff083
- gitlink staged for test-frame: 1906c4e923a8de91583102ea746ced5754aff083
- dev-frame-opencode remains pinned in parent HEAD: 551febfc8da7948fd5b113150b6004413d21ee92

## Evidence Recorded

- D:\devframe-system\test-frame\reports\evidence-opencode-a49-a50-capability-map-evidence-binding-consumption-a1.zip
  - SHA256: 49EC34FBB5340FFBED355CC5B34A775D400AFE8423D5102E2513C8BACC15085D

## Verification Summary

- Evidence ZIP hash matched declared value.
- Synthetic fixture JSON parsed successfully.
- Focused A49-A50 capability evidence binding consumption tests: 9 passed.
- Metadata consumption/orchestration regression suite: 89 passed.
- Evidence collector/manifest plus metadata consumption/orchestration suite: 114 passed.
- Generated evidence manifest JSON parsed successfully.
- Evidence ZIP entry listing contained expected command/report/manifest entries only.

## Non-Claims

- Not final governance acceptance.
- Not production-ready.
- Not live-ready beyond synthetic/offline consumption evidence.
- Does not authorize Zotero API/key reads, PDF, attachments, notes, full text, Obsidian, RAG, WriteLab, browser/CDP, cloud, MiniApp, or private paper runtime.

## Dirty-State Note

The parent worktree contains unrelated local governance/runtime drift that was not staged for this pin, including local registry files, parent governance reports, existing modified planning/report index files, modified prior pin-review reports, and untracked status reports. This pin stages only the test-frame gitlink, lock updates, and the two A49-A50 consumption parent reports.
