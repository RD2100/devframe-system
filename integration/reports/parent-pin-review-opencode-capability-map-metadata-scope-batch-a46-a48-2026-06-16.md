# Parent Pin Review: opencode Capability Map Metadata Scope Batch A46-A48

Date: 2026-06-16

## Decision

ACCEPTED_AND_PARENT_PINNED

## Pin Target

- Module: dev-frame-opencode
- Previous parent pin: fde1ff0a3b6d5824e57789fc3e88d0fd90ef3f54
- New parent pin: 84c59ea577d9dd92ca701e20fd3dc42304866d52
- Parent lock files updated:
  - D:\devframe-system\BASELINE_LOCK.json
  - D:\devframe-system\integration\lock\submodules.lock.yml

## Lock State

- BASELINE_LOCK.json dev-frame-opencode commit: 84c59ea577d9dd92ca701e20fd3dc42304866d52
- integration/lock/submodules.lock.yml dev-frame-opencode commit: 84c59ea577d9dd92ca701e20fd3dc42304866d52
- gitlink staged for dev-frame-opencode: 84c59ea577d9dd92ca701e20fd3dc42304866d52

## Evidence Recorded

- D:\devframe-system\.agent\evidence\evidence-opencode-capability-map-metadata-scope-a1-724bfab.zip
  - SHA256: 0EA82DC88A1569E73176F440D1C0A3E54E57F9CB75B9B456A453DD181B37DCB6
- D:\devframe-system\.agent\evidence\evidence-opencode-business-validation-zotero-metadata-status-a1-488a207.zip
  - SHA256: C6981737E71BEF6D54EA254031BB944FD228160D16D3217BFAA8FBA4A9026A09
- D:\devframe-system\.agent\evidence\evidence-opencode-capability-map-closed-shape-a1-84c59ea.zip
  - SHA256: 13D31290FD89DB6831B5BF33773A57E4D2C06A1718CF25A8A802405DC09B338B

## Verification Summary

- Evidence ZIP hashes matched declared values.
- MVP contracts plus business validation tests: 24 passed.
- Business validation, MVP, closeout, and readiness tests: 33 passed.
- Capability map schema, capability map JSON, and business validation schema parsed with `python -m json.tool`.
- `paper business-validate` CLI smoke generated parseable JSON.
- Module diff check from fde1ff0 to 84c59ea passed.

## Non-Claims

- Not final governance acceptance.
- Not production-ready.
- Not live-ready beyond local/offline metadata candidate evidence.
- Does not authorize Zotero key/API reads, notes, attachments, PDF, full text, Obsidian, RAG, WriteLab, browser/CDP, cloud, MiniApp, or private paper runtime.

## Dirty-State Note

The parent worktree contains unrelated local governance/runtime drift that was not staged for this pin, including local registry files, parent governance reports, existing modified planning/report index files, modified prior pin-review reports, and untracked status reports. This pin stages only the opencode gitlink, lock updates, and the two A46-A48 parent reports.
