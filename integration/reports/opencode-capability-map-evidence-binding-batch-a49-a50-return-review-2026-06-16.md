# dev-frame-opencode A49-A50 Capability Map Evidence Binding Return Review

Date: 2026-06-16

## Verdict

ACCEPTED_FOR_PARENT_PIN_WITH_LIMITATIONS

## Reviewed Return

- Module: dev-frame-opencode
- Branch: codex/paper-audit-privacy-hard-gate
- Target commit: 1cba29d25fc02dac17ef7bd17ce70cf0d0e5a1be
- Previous parent pin: 84c59ea577d9dd92ca701e20fd3dc42304866d52
- Scope: local/offline business validation and capability map evidence binding hardening

## Batch Commits

1. 54fe378a761ac0619c5cc707f7718c2b110b4866
   - Bind capability map closed-shape evidence
   - Evidence ZIP: D:\devframe-system\.agent\evidence\evidence-opencode-capability-map-evidence-binding-a1-54fe378.zip
   - SHA256: A28D873ABFA4A0FC138ABE6C602A230A6219AE2D1D8FFDA833FFCFBA47E31266
2. 1cba29d25fc02dac17ef7bd17ce70cf0d0e5a1be
   - Close capability map evidence row shape
   - Evidence ZIP: D:\devframe-system\.agent\evidence\evidence-opencode-capability-map-evidence-row-closed-shape-a1-1cba29d.zip
   - SHA256: 31730433C9AAAA00480E02A235F9116C7FAB048D249C677D70F4A70A372223ED

## Parent-Side Verification

- `git -C dev-frame-opencode rev-parse HEAD` -> 1cba29d25fc02dac17ef7bd17ce70cf0d0e5a1be
- `git -C dev-frame-opencode status --short --branch` -> clean except branch ahead marker
- `Get-FileHash` for both evidence ZIPs -> matched declared SHA256 values
- From `D:\devframe-system\dev-frame-opencode\ai-workflow-hub`:
  - `$env:PYTHONPATH='src'; python -m pytest tests\test_paper_business_capability_validation.py tests\test_paper_mvp_contracts.py -q` -> 25 passed
  - `$env:PYTHONPATH='src'; python -m pytest tests\test_paper_business_capability_validation.py tests\test_paper_mvp_contracts.py tests\test_paper_zotero_metadata_local_batch_closeout.py tests\test_paper_metadata_pipeline_readiness.py -q` -> 34 passed
  - `$env:PYTHONPATH='src'; python -m ai_workflow_hub.cli paper business-validate --output <temp json>` -> PASS
  - generated business validation JSON parse -> PASS
- From `D:\devframe-system\dev-frame-opencode`:
  - `python -m json.tool schemas\paper_business_validation_report.schema.json` -> PASS
  - `python -m json.tool schemas\paper_capability_map.schema.json` -> PASS
  - `python -m json.tool ai-workflow-hub\docs\paper\PAPER_CAPABILITY_MAP.json` -> PASS
  - `git diff --check 84c59ea577d9dd92ca701e20fd3dc42304866d52 1cba29d25fc02dac17ef7bd17ce70cf0d0e5a1be` -> PASS

## Reviewer Index

- Changed parent files for intake:
  - D:\devframe-system\BASELINE_LOCK.json
  - D:\devframe-system\integration\lock\submodules.lock.yml
  - D:\devframe-system\integration\reports\opencode-capability-map-evidence-binding-batch-a49-a50-return-review-2026-06-16.md
  - D:\devframe-system\integration\reports\parent-pin-review-opencode-capability-map-evidence-binding-batch-a49-a50-2026-06-16.md
  - D:\devframe-system\dev-frame-opencode gitlink
- Critical module paths covered by tests:
  - ai-workflow-hub/src/ai_workflow_hub/cli.py
  - ai-workflow-hub/tests/test_paper_business_capability_validation.py
  - ai-workflow-hub/tests/test_paper_mvp_contracts.py
  - schemas/paper_business_validation_report.schema.json
  - schemas/paper_capability_map.schema.json
  - ai-workflow-hub/docs/paper/PAPER_CAPABILITY_MAP.json
- Generated artifacts reviewed:
  - two declared evidence ZIPs listed above
- Suggested review focus:
  - confirm business validation evidence matrix references the capability map closed-shape negative test
  - confirm schema rejects deletion or drift of that evidence item
  - confirm no schema expansion, raw payload path, or final/live-ready claim was introduced
  - confirm this remains local/offline candidate evidence only

## Boundary

- No live Zotero API call was run in parent review.
- No read of C:\Users\RD\key\zotero.txt or any key file was performed.
- No notes, attachments, PDF, full text, Obsidian, RAG, WriteLab, browser/CDP, cloud, or MiniApp were used.
- This is not final governance acceptance and not production/live-ready.

## Known Gaps

- Parent review did not unzip and deep-audit every evidence artifact payload.
- This does not validate live Zotero connectivity, live citation correctness, paper quality, PDF/full-text, Obsidian, RAG, or WriteLab behavior.
