# Grouped Parent Pin Review: dev-frame-opencode Zotero Evidence Manifest Boundary A1

Date: 2026-06-15

## Status

`GROUPED_PARENT_PIN_READY`

## Scope

This parent closeout pins `dev-frame-opencode` to the accepted local-only
metadata/evidence-manifest boundary slice:

- Target submodule: `dev-frame-opencode`
- Target commit: `a2cedaa280f12f717d4bf0a64c1c12ece6f5fefe`
- Commit title: `Mirror Zotero pilot boundaries in evidence manifest`
- Evidence ZIP: `D:\devframe-system\.agent\evidence\evidence-opencode-zotero-evidence-manifest-boundary-a1-a2cedaa.zip`
- Evidence ZIP SHA256: `D7D03A5EED7F52E69231BF4B40C6DBD75DA63B72D28733675F8AC989047103B8`

## Parent Pin Decision

- `dev-frame-opencode` is pinned to `a2cedaa280f12f717d4bf0a64c1c12ece6f5fefe`.
- No parent lock file was modified.
- No `agent-acceptance` or `test-frame` pin is included in this commit.
- Existing parent dirty/untracked integration files are treated as pre-existing
  workspace state and are not included in this grouped pin commit.

## Boundary

This is a metadata-only/local-fixture governance boundary. It is not live-ready
and is not final product acceptance.

Still forbidden without fresh human-gated RuntimeAuthorization:

- real Zotero
- real Obsidian
- real RAG or private RAG
- live WriteLab
- real paper/PDF/full-text access
- MiniApp/browser/CDP/cloud runtime

## Verification

- `git -C D:\devframe-system\dev-frame-opencode rev-parse HEAD`
  - `a2cedaa280f12f717d4bf0a64c1c12ece6f5fefe`
- `git diff --submodule=short -- dev-frame-opencode`
  - `0c24204fd99e6cab1d853ecadb12200244119fe1` -> `a2cedaa280f12f717d4bf0a64c1c12ece6f5fefe`
- `Get-FileHash -Algorithm SHA256 D:\devframe-system\.agent\evidence\evidence-opencode-zotero-evidence-manifest-boundary-a1-a2cedaa.zip`
  - `D7D03A5EED7F52E69231BF4B40C6DBD75DA63B72D28733675F8AC989047103B8`

## Next Step

`dev-frame-opencode` may continue the next local-only task after it receives
this parent closeout. It must remain metadata/local-fixture only unless a fresh
RuntimeAuthorization explicitly authorizes real resource/runtime access.
