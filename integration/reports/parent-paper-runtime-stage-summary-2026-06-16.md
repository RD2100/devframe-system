# Parent paper runtime stage summary

Generated at: 2026-06-16
Parent repo: `D:\devframe-system`
Status: `RUNTIME_SMOKE_STAGE_PINNED_NON_FINAL`

## Current pinned modules

- `agent-acceptance`: `6b9a83c1dca0ea650dbc7e97f13977ac02e3e3ee`
- `devframe-control-plane`: `09167bc656f8625c97bfae5c52dae5a0280b116c`
- `dev-frame-opencode`: `a8b5a0143bff87f8aaaed3d50b9b6ad9225f7843`
- `test-frame`: `c2e6789b10490e6d9f2cf331742432fa6d4fa25d`

## What is now practically done

### Zotero metadata-only

- Zotero Web API metadata-only smoke was run earlier and returned `PASS_METADATA_ONLY`.
- Reports and schemas preserve minimized evidence: counts, fingerprints, booleans, and redaction counters.
- Notes, attachments, PDF, and full text remain out of scope.

### PDF redacted excerpt

- Real local PDF access was exercised through a redacted/minimized pilot.
- The evidence path proves PDF read and report minimization, not semantic paper-quality review.
- Raw full text and raw paragraph text were not accepted as persistent report evidence.

### Local WriteLab boundary

- Local WriteLab API was started and reached at `http://127.0.0.1:8001`.
- Synthetic live boundary smoke was run successfully.
- This proves local interface reachability and payload/result minimization, not diagnostic quality.

### Real PDF excerpt to local WriteLab

- Six local PDFs under the user-authorized folder were exercised through a controlled excerpt-to-local-WriteLab path.
- `test-frame` now consumes the minimized evidence and rejects summary-only pass, raw persistence, frontend-required drift, Obsidian/RAG-required drift, and final-acceptance overclaims.
- The parent has pinned:
  - opencode implementation: `fc15f7b829ff1701b6e7e78778cd549608b8a577`
  - test-frame consumption: `c2e6789b10490e6d9f2cf331742432fa6d4fa25d`

### Business validation and plugin closeout binding

- opencode now binds the PDF/WriteLab live pilot into business validation and plugin-pilot closeout as scoped live-smoke evidence.
- Parent pinned final binding target: `a8b5a0143bff87f8aaaed3d50b9b6ad9225f7843`.
- The binding reports remain non-final and do not call live resources.

## Key evidence packages

- `D:\devframe-system\.agent\evidence\evidence-opencode-pdf-writelab-live-pilot-a1-fc15f7b.zip`
  - SHA256: `0A621957EE59B8276F89CBF7336336FFAE5D59CBD32F3DF673A57E5EDC99E9A3`
- `D:\devframe-system\test-frame\reports\evidence-opencode-pdf-writelab-live-real-pilot-consumption-a1.zip`
  - SHA256: `8AB7A34514146CEFBD52F63DEAEF660FFA8829F4D9D1980A976817CC655F8B76`
- `D:\devframe-system\.agent\evidence\evidence-opencode-business-validation-pdf-writelab-live-binding-a1-531337c.zip`
  - SHA256: `9DE248D9DDBA20979F1068CDABED3F633D834DFF75421F2E900BF2BE4AC89222`
- `D:\devframe-system\.agent\evidence\evidence-opencode-plugin-closeout-pdf-writelab-live-binding-a1-a8b5a01.zip`
  - SHA256: `3A1344AF00DEF24213A795C227979B08C51FDCC53073414A219D089945D64D3C`

## What is still not done

- Obsidian vault/plugin testing is not done.
- RAG plugin/runtime testing is not done.
- Browser/CDP/cloud/MiniApp testing is not done.
- Final governance acceptance is not granted.
- Paper-quality acceptance is not granted.
- WriteLab diagnostic quality is not proven; only the interface path and evidence boundary are proven.

## Practical next steps

1. Finish a small WriteLab issue spot-check for the two cases that produced issues.
2. Wait for Obsidian and RAG installation/authorization before testing those paths.
3. Do not spend more time on broad synthetic governance slices unless a new blocker appears.
4. Keep future parent pins serialized: opencode first, then dependent test-frame consumption.

## Boundary

- This report does not grant RuntimeAuthorization for new resources.
- This report does not authorize unrestricted PDF/full-text processing.
- This report does not claim production readiness or final acceptance.
- Existing unrelated parent dirty state remains untouched.
