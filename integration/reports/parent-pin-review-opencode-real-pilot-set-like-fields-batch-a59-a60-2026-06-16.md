# Parent Pin Review: opencode Real Pilot Set-Like Fields Batch A59-A60

Date: 2026-06-16

## Decision

ACCEPTED_AND_PARENT_PINNED

## Pin Target

- Module: dev-frame-opencode
- Previous parent pin: 62994c1c45009032c1cb81053a07917b130449b2
- New parent pin: 580f6e9f3ad2ff7c22949d1694990a12b822ce12
- Parent lock files updated:
  - D:\devframe-system\BASELINE_LOCK.json
  - D:\devframe-system\integration\lock\submodules.lock.yml

## Lock State

- BASELINE_LOCK.json dev-frame-opencode commit: 580f6e9f3ad2ff7c22949d1694990a12b822ce12
- integration/lock/submodules.lock.yml dev-frame-opencode commit: 580f6e9f3ad2ff7c22949d1694990a12b822ce12
- gitlink staged for dev-frame-opencode: 580f6e9f3ad2ff7c22949d1694990a12b822ce12
- test-frame remains pinned in parent HEAD: ebf3fc77536be986c800b3be2abeb2059c9cdadc

## Evidence Recorded

- D:\devframe-system\.agent\evidence\evidence-opencode-real-pilot-set-like-fields-batch-a59-a60-580f6e9.zip
  - SHA256: F879907BF10CEFE5C7DA7E1608DB88E695EA0F6A8DE69AFD4CC3385A89C01130

## Verification Summary

- Evidence ZIP hash matched declared value.
- Real-pilot authorization/local dry-run/blocking/preauth/Zotero metadata suite: 80 passed.
- `paper real-pilot-authorization-request` CLI smoke generated parseable JSON.
- `paper real-pilot-dry-run` CLI smoke generated parseable JSON.
- `paper real-pilot-authorize-metadata` CLI smoke generated parseable JSON.
- Runtime authorization request, local dry-run, and human authorization decision schemas parsed with `python -m json.tool`.
- Module diff check from 62994c1 to 580f6e9 passed.

## Non-Claims

- Not final governance acceptance.
- Not production-ready.
- Not live-ready.
- Does not authorize Zotero key/API reads, notes, attachments, PDF, full text, Obsidian, RAG, WriteLab, browser/CDP, cloud, MiniApp, or private paper runtime.
- Does not grant RuntimeAuthorization or start real pilot execution.

## Dirty-State Note

The parent worktree contains unrelated local governance/runtime drift and current test-frame working checkout drift from later test-frame work. This pin stages only the opencode gitlink, lock updates, and the two A59-A60 parent reports.
