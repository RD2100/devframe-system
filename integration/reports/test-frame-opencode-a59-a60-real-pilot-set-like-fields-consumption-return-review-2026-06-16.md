# test-frame A59-A60 real pilot set-like fields consumption return review

Status: ACCEPTED_WITH_LIMITATIONS_FOR_PARENT_PIN

Reviewed return:
- Module: test-frame
- Path: D:\devframe-system\test-frame
- Branch: codex/adapter-negative-matrix
- Commit: 52483575cc94c097f1be57f7ed3d0d7a80940d32
- TaskSpec: TESTFRAME_OPENCODE_A59_A60_REAL_PILOT_SET_LIKE_FIELDS_CONSUMPTION_A1
- Evidence ZIP: D:\devframe-system\test-frame\reports\evidence-opencode-a59-a60-real-pilot-set-like-fields-consumption-a1.zip
- Evidence ZIP SHA256: 642BA1DCA6206E3B28063740566592CBBC334730D695B0E06D4FBBE62C3CA426

Accepted scope:
- Synthetic/offline consumption validation for parent-pinned opencode A59-A60 real-pilot set-like field hardening.
- Consumes minimized source facts only: opencode commit, parent pin, source evidence ZIP name/hash, schema-hardening semantics, and fail-closed duplicate set value contract expectations.
- This is verification evidence only and does not grant RuntimeAuthorization or claim real pilot readiness.

Parent-side verification:
- test-frame HEAD matched 52483575cc94c097f1be57f7ed3d0d7a80940d32.
- test-frame tracked worktree was clean at review time.
- Evidence ZIP SHA256 matched 642BA1DCA6206E3B28063740566592CBBC334730D695B0E06D4FBBE62C3CA426.
- Fixture JSON parse: PASS.
- Evidence manifest JSON parse: PASS.
- Focused pytest: 9 passed.
- Metadata consumption/orchestration regression suite: 143 passed.
- Evidence collector/manifest plus metadata/orchestration suite: 168 passed.
- git diff --check: PASS.

Reviewer Index:
- Changed files:
  - D:\devframe-system\test-frame\docs\test-frame\paper-pipeline-metadata-only\README.md
  - D:\devframe-system\test-frame\docs\test-frame\paper-pipeline-metadata-only\opencode-a59-a60-real-pilot-set-like-fields-consumption.fixture.json
  - D:\devframe-system\test-frame\tests\test_opencode_a59_a60_real_pilot_set_like_fields_consumption.py
- Critical paths:
  - RuntimeAuthorization request set-like fields
  - local dry-run redaction and known_gaps sets
  - human RuntimeAuthorization decision metadata-only scope
  - fail-closed checks for raw/sensitive/final/live/production/real-pilot overclaims
  - source provenance/package hash/package entries
- Tests run:
  - python -m json.tool docs\test-frame\paper-pipeline-metadata-only\opencode-a59-a60-real-pilot-set-like-fields-consumption.fixture.json
  - python -m pytest tests\test_opencode_a59_a60_real_pilot_set_like_fields_consumption.py -q
  - metadata consumption/orchestration regression suite
  - evidence collector/manifest plus metadata/orchestration suite
  - python -m json.tool reports\opencode-a59-a60-real-pilot-set-like-fields-consumption-a1\manifests\evidence-manifest.json
  - git diff --check
- Generated artifacts:
  - D:\devframe-system\test-frame\reports\opencode-a59-a60-real-pilot-set-like-fields-consumption-a1\EXECUTION_REPORT.md
  - D:\devframe-system\test-frame\reports\opencode-a59-a60-real-pilot-set-like-fields-consumption-a1\REVIEWER_INDEX.md
  - D:\devframe-system\test-frame\reports\opencode-a59-a60-real-pilot-set-like-fields-consumption-a1\STATUS_SUMMARY.md
  - D:\devframe-system\test-frame\reports\opencode-a59-a60-real-pilot-set-like-fields-consumption-a1\commands\preflight.txt
  - D:\devframe-system\test-frame\reports\opencode-a59-a60-real-pilot-set-like-fields-consumption-a1\commands\verification-summary.txt
  - D:\devframe-system\test-frame\reports\opencode-a59-a60-real-pilot-set-like-fields-consumption-a1\manifests\evidence-manifest.json
  - D:\devframe-system\test-frame\reports\evidence-opencode-a59-a60-real-pilot-set-like-fields-consumption-a1.zip
- Known gaps:
  - Synthetic/offline consumption only.
  - No raw ZIP payload inspection beyond declared evidence package shape/hash.
  - No real Zotero/API/key/raw response/PDF/notes/full text/paragraph_text runtime.
  - No WriteLab/Obsidian/RAG/browser/CDP/cloud/MiniApp runtime.
  - No RuntimeAuthorization grant and no real pilot execution.
  - Parent still owns final governance acceptance.
- Suggested review focus:
  - Confirm duplicate masking checks.
  - Confirm metadata-only human authorization is not reusable for broader real access.
  - Confirm local dry-run does not become real-pilot readiness.
  - Confirm fixture contains minimized governance facts only.

Boundary:
- No read of C:\Users\RD\key\zotero.txt or any key file.
- No Zotero Web API call.
- No raw API response, raw item JSON, raw title, raw abstract, raw user id, API key, PDF, notes, attachments, full text, or paragraph_text.
- No WriteLab, Obsidian, live RAG, browser/CDP, cloud, MiniApp, or external runtime.
- No RuntimeAuthorization grant, no final governance acceptance, no live-ready, no production-ready, no paper-quality acceptance, and no real pilot completion.
