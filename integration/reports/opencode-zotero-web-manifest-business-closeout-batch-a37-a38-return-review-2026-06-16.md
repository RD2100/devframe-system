# dev-frame-opencode A37-A38 Return Review

Date: 2026-06-16

## Verdict

ACCEPTED_FOR_PARENT_PIN_WITH_LIMITATIONS

## Reviewed Return

- Module: dev-frame-opencode
- Branch: codex/paper-audit-privacy-hard-gate
- Target commit: 9574c71c011bc975575b9d5d301965adb3e21284
- Parent base before this batch: bd1bbb5920dfd714ff053a10d8657f95d4449bfe
- Scope: local/offline Zotero Web API metadata-only business-validation and closeout hardening

## Batch Commits

1. 9a930fe5f25f27c347639308e6253dcb42632879
   - Bind Zotero Web manifest to business validation
   - Evidence ZIP: D:\devframe-system\.agent\evidence\evidence-opencode-zotero-web-manifest-business-validation-a1-9a930fe.zip
   - SHA256: E9857E2AC0CDDDF4370C809BCD84ABBCAEE6DC0D215A48859EBC3A24EA106C1E
2. 9574c71c011bc975575b9d5d301965adb3e21284
   - Extend Zotero metadata closeout manifest coverage
   - Evidence ZIP: D:\devframe-system\.agent\evidence\evidence-opencode-zotero-metadata-closeout-manifest-coverage-a1-9574c71.zip
   - SHA256: 318DE825925E10F4E2525B3987AB559C08FE5FDC27F41AAF90597CA8E03F908D

## Parent-Side Verification

- `git -C dev-frame-opencode rev-parse HEAD` -> 9574c71c011bc975575b9d5d301965adb3e21284
- `git -C dev-frame-opencode status --short --branch` -> clean except branch ahead marker
- `Get-FileHash` for both evidence ZIPs -> matched declared SHA256 values
- From `D:\devframe-system\dev-frame-opencode\ai-workflow-hub`:
  - `$env:PYTHONPATH='src'; python -m pytest tests\test_paper_zotero_metadata_local_batch_closeout.py tests\test_paper_business_capability_validation.py tests\test_zotero_web_metadata_pilot.py -q` -> 31 passed
  - `$env:PYTHONPATH='src'; python -m pytest tests\test_paper_zotero_metadata_local_batch_closeout.py tests\test_paper_business_capability_validation.py tests\test_zotero_web_metadata_pilot.py tests\test_paper_real_pilot_authorization_request.py tests\test_paper_real_zotero_metadata_only_pilot.py -q` -> 76 passed
- From `D:\devframe-system\dev-frame-opencode`:
  - `python -m json.tool schemas\paper_zotero_metadata_local_batch_closeout_report.schema.json` -> PASS
  - `python -m json.tool schemas\paper_business_validation_report.schema.json` -> PASS
  - `git diff --check bd1bbb5920dfd714ff053a10d8657f95d4449bfe 9574c71c011bc975575b9d5d301965adb3e21284` -> PASS

## Reviewer Index

- Changed parent files for intake:
  - D:\devframe-system\BASELINE_LOCK.json
  - D:\devframe-system\integration\lock\submodules.lock.yml
  - D:\devframe-system\integration\reports\opencode-zotero-web-manifest-business-closeout-batch-a37-a38-return-review-2026-06-16.md
  - D:\devframe-system\integration\reports\parent-pin-review-opencode-zotero-web-manifest-business-closeout-batch-a37-a38-2026-06-16.md
  - D:\devframe-system\dev-frame-opencode gitlink
- Critical module paths reviewed by tests:
  - ai-workflow-hub/src/ai_workflow_hub/cli.py
  - ai-workflow-hub/src/ai_workflow_hub/context_layer/adapters/zotero_metadata_real_pilot.py
  - schemas/paper_business_validation_report.schema.json
  - schemas/paper_zotero_metadata_local_batch_closeout_report.schema.json
- Generated artifacts reviewed:
  - two declared evidence ZIPs listed above
- Suggested review focus:
  - confirm business validation does not promote metadata-only manifest evidence to final/live readiness
  - confirm closeout remains local/offline and non-final
  - confirm no raw Zotero title, abstract, item JSON, API key, user id, notes, attachments, PDF paths, or full text were added to reports/evidence

## Boundary

- No live Zotero API call was run in parent review.
- No read of C:\Users\RD\key\zotero.txt was performed in parent review.
- No notes, attachments, PDF, full text, Obsidian, RAG, WriteLab, browser/CDP, cloud, or MiniApp were used.
- This is not final governance acceptance and not production/live-ready.

## Known Gaps

- Parent review did not unzip and deep-audit every evidence artifact payload.
- This intake records local/offline metadata-only governance progress only.
