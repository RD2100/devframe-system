# test-frame opencode A46-A48 Capability Map Metadata Scope Consumption Return Review

Date: 2026-06-16

## Verdict

ACCEPTED_FOR_PARENT_PIN_WITH_LIMITATIONS

## Reviewed Return

- Module: test-frame
- Branch: codex/adapter-negative-matrix
- Target commit: 94e66f01dae171c7ef91432ae458a42dfc2be7a0
- Previous parent pin: fb4367ec33204a87f1d40561dfd4bd617945e440
- Scope: synthetic/offline consumption checks for parent-pinned opencode A46-A48 capability map metadata-only scope, business validation Zotero metadata status, and closed capability map shape
- Source opencode pin consumed by fixture: 84c59ea577d9dd92ca701e20fd3dc42304866d52
- Current parent opencode pin after later intake remains: 1cba29d25fc02dac17ef7bd17ce70cf0d0e5a1be
- Evidence ZIP: D:\devframe-system\test-frame\reports\evidence-opencode-a46-a48-capability-map-metadata-scope-consumption-a1.zip
- Evidence ZIP SHA256: 2570E78299042A46D3DA6BE853DD966A670198DFC42809A2782CF70AB877A16F

## Parent-Side Verification

- `git -C test-frame rev-parse HEAD` -> 94e66f01dae171c7ef91432ae458a42dfc2be7a0
- `Get-FileHash` for evidence ZIP -> matched declared SHA256
- From `D:\devframe-system\test-frame`:
  - `python -m json.tool docs\test-frame\paper-pipeline-metadata-only\opencode-a46-a48-capability-map-metadata-scope-consumption.fixture.json` -> PASS
  - `python -m pytest tests\test_opencode_a46_a48_capability_map_metadata_scope_consumption.py -q` -> 9 passed
  - `python -m pytest tests\test_zotero_web_api_metadata_only_contract.py tests\test_zotero_metadata_adapter_evidence_consumption.py tests\test_zotero_metadata_hardening_consumption.py tests\test_zotero_metadata_manifest_consumption.py tests\test_paper_pipeline_metadata_only_orchestration.py tests\test_opencode_a37_a38_business_closeout_consumption.py tests\test_opencode_a39_a40_metadata_pipeline_readiness_consumption.py tests\test_opencode_a41_a42_metadata_closeout_cli_consumption.py tests\test_opencode_a43_a45_business_validation_closeout_binding_consumption.py tests\test_opencode_a46_a48_capability_map_metadata_scope_consumption.py -q` -> 80 passed
  - `python -m pytest tests\test_evidence_pack_manifest.py tests\test_evidence_collector.py tests\test_zotero_web_api_metadata_only_contract.py tests\test_zotero_metadata_adapter_evidence_consumption.py tests\test_zotero_metadata_hardening_consumption.py tests\test_zotero_metadata_manifest_consumption.py tests\test_paper_pipeline_metadata_only_orchestration.py tests\test_opencode_a37_a38_business_closeout_consumption.py tests\test_opencode_a39_a40_metadata_pipeline_readiness_consumption.py tests\test_opencode_a41_a42_metadata_closeout_cli_consumption.py tests\test_opencode_a43_a45_business_validation_closeout_binding_consumption.py tests\test_opencode_a46_a48_capability_map_metadata_scope_consumption.py -q` -> 105 passed
  - `python -m json.tool reports\opencode-a46-a48-capability-map-metadata-scope-consumption-a1\manifests\evidence-manifest.json` -> PASS
  - `tar -tf reports\evidence-opencode-a46-a48-capability-map-metadata-scope-consumption-a1.zip` -> expected command/report/manifest entries only

## Reviewer Index

- Changed parent files for intake:
  - D:\devframe-system\BASELINE_LOCK.json
  - D:\devframe-system\integration\lock\submodules.lock.yml
  - D:\devframe-system\integration\reports\test-frame-opencode-a46-a48-capability-map-metadata-scope-consumption-return-review-2026-06-16.md
  - D:\devframe-system\integration\reports\parent-pin-review-test-frame-opencode-a46-a48-capability-map-metadata-scope-consumption-2026-06-16.md
  - D:\devframe-system\test-frame gitlink
- Critical module paths covered by tests:
  - docs/test-frame/paper-pipeline-metadata-only/README.md
  - docs/test-frame/paper-pipeline-metadata-only/opencode-a46-a48-capability-map-metadata-scope-consumption.fixture.json
  - tests/test_opencode_a46_a48_capability_map_metadata_scope_consumption.py
- Generated artifacts reviewed:
  - D:\devframe-system\test-frame\reports\evidence-opencode-a46-a48-capability-map-metadata-scope-consumption-a1.zip
  - D:\devframe-system\test-frame\reports\opencode-a46-a48-capability-map-metadata-scope-consumption-a1\manifests\evidence-manifest.json
- Suggested review focus:
  - confirm fixture provenance is parent-pinned A46-A48 only
  - confirm capability map row set cannot accept missing, duplicate, extra, unknown, or promoted rows
  - confirm Zotero metadata remains metadata-only candidate, not PDF/full-text/notes/attachments/live-ready
  - confirm business validation cannot promote metadata status to final governance acceptance
  - confirm raw/sensitive marker and token-like checks fail closed

## Boundary

- Synthetic/offline replay only.
- No read of C:\Users\RD\key\zotero.txt or any key file.
- No Zotero Web API call.
- No raw API response, raw item JSON, raw title, raw abstract, raw user id, API key, PDF, attachments, notes, full text, or paragraph_text.
- No WriteLab, Obsidian, live RAG, browser/CDP, cloud, MiniApp, or external runtime.
- This is not final governance acceptance and not production/live-ready.

## Known Gaps

- This does not deep-audit ZIP payloads.
- This does not prove live Zotero connectivity, PDF/full-text processing, Obsidian, RAG, WriteLab, paper quality, or production readiness.
