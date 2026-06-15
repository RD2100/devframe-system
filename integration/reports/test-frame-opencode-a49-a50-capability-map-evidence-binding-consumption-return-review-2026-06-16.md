# test-frame opencode A49-A50 Capability Map Evidence Binding Consumption Return Review

Date: 2026-06-16

## Verdict

ACCEPTED_FOR_PARENT_PIN_WITH_LIMITATIONS

## Reviewed Return

- Module: test-frame
- Branch: codex/adapter-negative-matrix
- Target commit: 1906c4e923a8de91583102ea746ced5754aff083
- Previous parent pin: 94e66f01dae171c7ef91432ae458a42dfc2be7a0
- Scope: synthetic/offline consumption checks for parent-pinned opencode A49-A50 capability map evidence binding and closed capability_map_artifact row
- Source opencode pin consumed by fixture: 1cba29d25fc02dac17ef7bd17ce70cf0d0e5a1be
- Current parent opencode pin after later intake remains: 551febfc8da7948fd5b113150b6004413d21ee92
- Evidence ZIP: D:\devframe-system\test-frame\reports\evidence-opencode-a49-a50-capability-map-evidence-binding-consumption-a1.zip
- Evidence ZIP SHA256: 49EC34FBB5340FFBED355CC5B34A775D400AFE8423D5102E2513C8BACC15085D

## Parent-Side Verification

- `git -C test-frame rev-parse HEAD` -> 1906c4e923a8de91583102ea746ced5754aff083
- `Get-FileHash` for evidence ZIP -> matched declared SHA256
- From `D:\devframe-system\test-frame`:
  - `python -m json.tool docs\test-frame\paper-pipeline-metadata-only\opencode-a49-a50-capability-map-evidence-binding-consumption.fixture.json` -> PASS
  - `python -m pytest tests\test_opencode_a49_a50_capability_map_evidence_binding_consumption.py -q` -> 9 passed
  - metadata consumption/orchestration regression suite -> 89 passed
  - evidence collector/manifest plus metadata consumption/orchestration suite -> 114 passed
  - `python -m json.tool reports\opencode-a49-a50-capability-map-evidence-binding-consumption-a1\manifests\evidence-manifest.json` -> PASS
  - `tar -tf reports\evidence-opencode-a49-a50-capability-map-evidence-binding-consumption-a1.zip` -> expected command/report/manifest entries only

## Reviewer Index

- Changed parent files for intake:
  - D:\devframe-system\BASELINE_LOCK.json
  - D:\devframe-system\integration\lock\submodules.lock.yml
  - D:\devframe-system\integration\reports\test-frame-opencode-a49-a50-capability-map-evidence-binding-consumption-return-review-2026-06-16.md
  - D:\devframe-system\integration\reports\parent-pin-review-test-frame-opencode-a49-a50-capability-map-evidence-binding-consumption-2026-06-16.md
  - D:\devframe-system\test-frame gitlink
- Critical module paths covered by tests:
  - docs/test-frame/paper-pipeline-metadata-only/README.md
  - docs/test-frame/paper-pipeline-metadata-only/opencode-a49-a50-capability-map-evidence-binding-consumption.fixture.json
  - tests/test_opencode_a49_a50_capability_map_evidence_binding_consumption.py
- Generated artifacts reviewed:
  - D:\devframe-system\test-frame\reports\evidence-opencode-a49-a50-capability-map-evidence-binding-consumption-a1.zip
  - D:\devframe-system\test-frame\reports\opencode-a49-a50-capability-map-evidence-binding-consumption-a1\manifests\evidence-manifest.json
- Suggested review focus:
  - confirm fixture provenance is parent-pinned A49-A50 only
  - confirm capability_map_artifact appears exactly once and cannot be missing, duplicated, renamed, blocked, promoted, or reshaped
  - confirm capability_map_artifact.command remains paper capability-map
  - confirm required evidence includes test_capability_map_schema_rejects_missing_or_duplicate_capabilities
  - confirm raw/sensitive marker and final/live/production overclaim checks fail closed

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
