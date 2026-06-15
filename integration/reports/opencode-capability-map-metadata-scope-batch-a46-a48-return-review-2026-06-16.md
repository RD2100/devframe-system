# dev-frame-opencode A46-A48 Capability Map Metadata Scope Return Review

Date: 2026-06-16

## Verdict

ACCEPTED_FOR_PARENT_PIN_WITH_LIMITATIONS

## Reviewed Return

- Module: dev-frame-opencode
- Branch: codex/paper-audit-privacy-hard-gate
- Target commit: 84c59ea577d9dd92ca701e20fd3dc42304866d52
- Previous parent pin: fde1ff0a3b6d5824e57789fc3e88d0fd90ef3f54
- Scope: local/offline paper capability map and business validation metadata-scope synchronization

## Batch Commits

1. 724bfab63c213dbcdf1e0f1bdb110d1bed0e1b85
   - Sync capability map metadata scope
   - Evidence ZIP: D:\devframe-system\.agent\evidence\evidence-opencode-capability-map-metadata-scope-a1-724bfab.zip
   - SHA256: 0EA82DC88A1569E73176F440D1C0A3E54E57F9CB75B9B456A453DD181B37DCB6
2. 488a207567253d3c640aebdf0c64521dc21273ba
   - Mark Zotero metadata as metadata-only candidate
   - Evidence ZIP: D:\devframe-system\.agent\evidence\evidence-opencode-business-validation-zotero-metadata-status-a1-488a207.zip
   - SHA256: C6981737E71BEF6D54EA254031BB944FD228160D16D3217BFAA8FBA4A9026A09
3. 84c59ea577d9dd92ca701e20fd3dc42304866d52
   - Close paper capability map shape
   - Evidence ZIP: D:\devframe-system\.agent\evidence\evidence-opencode-capability-map-closed-shape-a1-84c59ea.zip
   - SHA256: 13D31290FD89DB6831B5BF33773A57E4D2C06A1718CF25A8A802405DC09B338B

## Parent-Side Verification

- `git -C dev-frame-opencode rev-parse HEAD` -> 84c59ea577d9dd92ca701e20fd3dc42304866d52
- `git -C dev-frame-opencode status --short --branch` -> clean except branch ahead marker
- `Get-FileHash` for all three evidence ZIPs -> matched declared SHA256 values
- From `D:\devframe-system\dev-frame-opencode\ai-workflow-hub`:
  - `$env:PYTHONPATH='src'; python -m pytest tests\test_paper_mvp_contracts.py tests\test_paper_business_capability_validation.py -q` -> 24 passed
  - `$env:PYTHONPATH='src'; python -m pytest tests\test_paper_business_capability_validation.py tests\test_paper_mvp_contracts.py tests\test_paper_zotero_metadata_local_batch_closeout.py tests\test_paper_metadata_pipeline_readiness.py -q` -> 33 passed
  - `$env:PYTHONPATH='src'; python -m ai_workflow_hub.cli paper business-validate --output <temp json>` -> PASS
  - generated business validation JSON parse -> PASS
- From `D:\devframe-system\dev-frame-opencode`:
  - `python -m json.tool schemas\paper_capability_map.schema.json` -> PASS
  - `python -m json.tool ai-workflow-hub\docs\paper\PAPER_CAPABILITY_MAP.json` -> PASS
  - `python -m json.tool schemas\paper_business_validation_report.schema.json` -> PASS
  - `git diff --check fde1ff0a3b6d5824e57789fc3e88d0fd90ef3f54 84c59ea577d9dd92ca701e20fd3dc42304866d52` -> PASS

## Reviewer Index

- Changed parent files for intake:
  - D:\devframe-system\BASELINE_LOCK.json
  - D:\devframe-system\integration\lock\submodules.lock.yml
  - D:\devframe-system\integration\reports\opencode-capability-map-metadata-scope-batch-a46-a48-return-review-2026-06-16.md
  - D:\devframe-system\integration\reports\parent-pin-review-opencode-capability-map-metadata-scope-batch-a46-a48-2026-06-16.md
  - D:\devframe-system\dev-frame-opencode gitlink
- Critical module paths covered by tests:
  - ai-workflow-hub/docs/paper/PAPER_CAPABILITY_MAP.md
  - ai-workflow-hub/docs/paper/PAPER_CAPABILITY_MAP.json
  - ai-workflow-hub/src/ai_workflow_hub/cli.py
  - ai-workflow-hub/tests/test_paper_mvp_contracts.py
  - ai-workflow-hub/tests/test_paper_business_capability_validation.py
  - schemas/paper_business_validation_report.schema.json
  - schemas/paper_capability_map.schema.json
- Generated artifacts reviewed:
  - three declared evidence ZIPs listed above
- Suggested review focus:
  - confirm capability map allowed scope only adds sanitized/minimized metadata candidate surfaces
  - confirm forbidden scope excludes notes, attachments, PDF paths, full text, raw abstracts/titles, API keys, and unauthorized live API
  - confirm business validation status says metadata_only_candidate without implying live-ready behavior
  - confirm capability map schema requires exactly one row for each expected capability

## Boundary

- No live Zotero API call was run in parent review.
- No read of C:\Users\RD\key\zotero.txt or any key file was performed.
- No notes, attachments, PDF, full text, Obsidian, RAG, WriteLab, browser/CDP, cloud, or MiniApp were used.
- This is not final governance acceptance and not production/live-ready.

## Known Gaps

- Parent review did not unzip and deep-audit every evidence artifact payload.
- This does not validate live Zotero connectivity, live citation correctness, paper quality, PDF/full-text, Obsidian, RAG, or WriteLab behavior.
