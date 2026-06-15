# test-frame opencode A39-A40 Metadata Pipeline Readiness Consumption Return Review

Date: 2026-06-16

## Verdict

ACCEPTED_FOR_PARENT_PIN_WITH_LIMITATIONS

## Reviewed Return

- Module: test-frame
- Branch: codex/adapter-negative-matrix
- Target commit: 68482818ab6dd06500e30bbf8d664db6aa91d6ba
- Previous parent pin: 36c363d87813cb19ee4e8117d47d78537b26911b
- Scope: synthetic/offline consumption checks for parent-pinned opencode A39-A40 metadata pipeline readiness report and business validation binding
- Evidence ZIP: D:\devframe-system\test-frame\reports\evidence-opencode-a39-a40-metadata-pipeline-readiness-consumption-a1.zip
- Evidence ZIP SHA256: 59585767023EBE00554A7F68C5C88AA80035DF42A0DEFD51080A402006B60F4E

## Parent-Side Verification

- `git -C test-frame rev-parse HEAD` -> 68482818ab6dd06500e30bbf8d664db6aa91d6ba
- `Get-FileHash` for evidence ZIP -> matched declared SHA256
- From `D:\devframe-system\test-frame`:
  - `python -m json.tool docs\test-frame\paper-pipeline-metadata-only\opencode-a39-a40-metadata-pipeline-readiness-consumption.fixture.json` -> PASS
  - `python -m pytest tests\test_opencode_a39_a40_metadata_pipeline_readiness_consumption.py -q` -> 9 passed
  - `python -m pytest tests\test_zotero_web_api_metadata_only_contract.py tests\test_zotero_metadata_adapter_evidence_consumption.py tests\test_zotero_metadata_hardening_consumption.py tests\test_zotero_metadata_manifest_consumption.py tests\test_paper_pipeline_metadata_only_orchestration.py tests\test_opencode_a37_a38_business_closeout_consumption.py tests\test_opencode_a39_a40_metadata_pipeline_readiness_consumption.py -q` -> 54 passed
  - `python -m pytest tests\test_evidence_pack_manifest.py tests\test_evidence_collector.py tests\test_zotero_web_api_metadata_only_contract.py tests\test_zotero_metadata_adapter_evidence_consumption.py tests\test_zotero_metadata_hardening_consumption.py tests\test_zotero_metadata_manifest_consumption.py tests\test_paper_pipeline_metadata_only_orchestration.py tests\test_opencode_a37_a38_business_closeout_consumption.py tests\test_opencode_a39_a40_metadata_pipeline_readiness_consumption.py -q` -> 79 passed
  - `python -m json.tool reports\opencode-a39-a40-metadata-pipeline-readiness-consumption-a1\manifests\evidence-manifest.json` -> PASS
  - `git diff --check 36c363d87813cb19ee4e8117d47d78537b26911b 68482818ab6dd06500e30bbf8d664db6aa91d6ba` -> PASS

## Reviewer Index

- Changed parent files for intake:
  - D:\devframe-system\BASELINE_LOCK.json
  - D:\devframe-system\integration\lock\submodules.lock.yml
  - D:\devframe-system\integration\reports\test-frame-opencode-a39-a40-metadata-pipeline-readiness-consumption-return-review-2026-06-16.md
  - D:\devframe-system\integration\reports\parent-pin-review-test-frame-opencode-a39-a40-metadata-pipeline-readiness-consumption-2026-06-16.md
  - D:\devframe-system\test-frame gitlink
- Critical module paths covered by tests:
  - docs/test-frame/paper-pipeline-metadata-only/README.md
  - docs/test-frame/paper-pipeline-metadata-only/opencode-a39-a40-metadata-pipeline-readiness-consumption.fixture.json
  - tests/test_opencode_a39_a40_metadata_pipeline_readiness_consumption.py
- Generated artifacts reviewed:
  - D:\devframe-system\test-frame\reports\evidence-opencode-a39-a40-metadata-pipeline-readiness-consumption-a1.zip
  - D:\devframe-system\test-frame\reports\opencode-a39-a40-metadata-pipeline-readiness-consumption-a1\manifests\evidence-manifest.json
- Suggested review focus:
  - confirm fixture uses parent-pinned opencode A39-A40 provenance
  - confirm metadata pipeline readiness cannot be converted to final/live/production readiness
  - confirm business validation requires metadata_pipeline_readiness_ready evidence row
  - confirm raw/sensitive marker detection and minimized-evidence policy fail closed

## Boundary

- Synthetic/offline replay only.
- No read of C:\Users\RD\key\zotero.txt.
- No Zotero Web API call.
- No raw API response, source payload, raw source fields, API key, or raw user id read.
- No PDF, attachments, notes, full text, paragraph_text, WriteLab, Obsidian, live RAG, browser/CDP, cloud, or MiniApp.
- This is not final governance acceptance and not production/live-ready.

## Known Gaps

- This does not deep-audit ZIP payloads.
- This does not prove live Zotero connectivity, live citation correctness, PDF/full-text processing, Obsidian, RAG, or WriteLab behavior.
