# Parent Pin Review: opencode Capability Map Evidence Binding Batch A49-A50

Date: 2026-06-16

## Decision

ACCEPTED_AND_PARENT_PINNED

## Pin Target

- Module: dev-frame-opencode
- Previous parent pin: 84c59ea577d9dd92ca701e20fd3dc42304866d52
- New parent pin: 1cba29d25fc02dac17ef7bd17ce70cf0d0e5a1be
- Parent lock files updated:
  - D:\devframe-system\BASELINE_LOCK.json
  - D:\devframe-system\integration\lock\submodules.lock.yml

## Lock State

- BASELINE_LOCK.json dev-frame-opencode commit: 1cba29d25fc02dac17ef7bd17ce70cf0d0e5a1be
- integration/lock/submodules.lock.yml dev-frame-opencode commit: 1cba29d25fc02dac17ef7bd17ce70cf0d0e5a1be
- gitlink staged for dev-frame-opencode: 1cba29d25fc02dac17ef7bd17ce70cf0d0e5a1be

## Evidence Recorded

- D:\devframe-system\.agent\evidence\evidence-opencode-capability-map-evidence-binding-a1-54fe378.zip
  - SHA256: A28D873ABFA4A0FC138ABE6C602A230A6219AE2D1D8FFDA833FFCFBA47E31266
- D:\devframe-system\.agent\evidence\evidence-opencode-capability-map-evidence-row-closed-shape-a1-1cba29d.zip
  - SHA256: 31730433C9AAAA00480E02A235F9116C7FAB048D249C677D70F4A70A372223ED

## Verification Summary

- Evidence ZIP hashes matched declared values.
- Business validation plus MVP contract tests: 25 passed.
- Business validation, MVP, closeout, and readiness tests: 34 passed.
- Business validation schema, capability map schema, and capability map JSON parsed with `python -m json.tool`.
- `paper business-validate` CLI smoke generated parseable JSON and included the capability map closed-shape evidence row.
- Module diff check from 84c59ea to 1cba29d passed.

## Non-Claims

- Not final governance acceptance.
- Not production-ready.
- Not live-ready beyond local/offline metadata candidate evidence.
- Does not authorize Zotero key/API reads, notes, attachments, PDF, full text, Obsidian, RAG, WriteLab, browser/CDP, cloud, MiniApp, or private paper runtime.

## Dirty-State Note

The parent worktree contains unrelated local governance/runtime drift that was not staged for this pin, including local registry files, parent governance reports, existing modified planning/report index files, modified prior pin-review reports, and untracked status reports. This pin stages only the opencode gitlink, lock updates, and the two A49-A50 parent reports.
