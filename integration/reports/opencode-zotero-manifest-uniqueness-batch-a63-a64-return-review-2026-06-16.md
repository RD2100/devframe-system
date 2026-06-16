# opencode A63-A64 Zotero manifest uniqueness return review

Status: ACCEPTED_WITH_LIMITATIONS_FOR_PARENT_PIN

Reviewed return:
- Module: dev-frame-opencode
- Path: D:\devframe-system\dev-frame-opencode
- Branch: codex/paper-audit-privacy-hard-gate
- Commit: 3667207d28b51e9aa519126a382c4d9537641a13
- Base: b249d2f1f6ac25183a89ac4a17750203a09743ce
- TaskSpec batch: OPENCODE_ZOTERO_MANIFEST_UNIQUENESS_BATCH_A63_A64
- Evidence ZIP: D:\devframe-system\.agent\evidence\evidence-opencode-zotero-manifest-uniqueness-batch-a63-a64-3667207.zip
- Evidence ZIP SHA256: 7F655A9C4974DEB8A86E878AE22CD4D888FE7A3B20838595F9B68B4C830B62B9

Accepted scope:
- Local/offline metadata evidence manifest schema/test hardening.
- Export-file metadata-only pilot evidence manifest source, retrieval, and redaction records reject duplicates.
- Export-file metadata-only commands_run, tests_run, and artifacts_generated reject duplicates.
- Zotero Web API report item_fingerprints and evidence manifest source_records reject duplicates.
- Standalone Zotero Web API EvidenceManifest source_records reject duplicates.

Parent-side verification:
- dev-frame-opencode HEAD matched 3667207d28b51e9aa519126a382c4d9537641a13.
- dev-frame-opencode tracked worktree was clean at review time.
- Evidence ZIP SHA256 matched 7F655A9C4974DEB8A86E878AE22CD4D888FE7A3B20838595F9B68B4C830B62B9.
- Real Zotero metadata-only pilot tests: 32 passed.
- Zotero Web metadata pilot tests: 17 passed.
- Expanded metadata/business focused suite: 100 passed.
- real-pilot-authorization-request CLI smoke: PASS, JSON parse PASS.
- paper_real_zotero_metadata_only_pilot_report schema parse: PASS.
- paper_zotero_web_api_metadata_only_pilot_report schema parse: PASS.
- paper_zotero_web_api_metadata_only_evidence_manifest schema parse: PASS.
- git diff --check b249d2f1f6ac25183a89ac4a17750203a09743ce 3667207d28b51e9aa519126a382c4d9537641a13: PASS.

Reviewer Index:
- Changed files:
  - D:\devframe-system\dev-frame-opencode\schemas\paper_real_zotero_metadata_only_pilot_report.schema.json
  - D:\devframe-system\dev-frame-opencode\ai-workflow-hub\tests\test_paper_real_zotero_metadata_only_pilot.py
  - D:\devframe-system\dev-frame-opencode\schemas\paper_zotero_web_api_metadata_only_pilot_report.schema.json
  - D:\devframe-system\dev-frame-opencode\schemas\paper_zotero_web_api_metadata_only_evidence_manifest.schema.json
  - D:\devframe-system\dev-frame-opencode\ai-workflow-hub\tests\test_zotero_web_metadata_pilot.py
- Critical paths:
  - export-file metadata-only pilot report EvidenceManifest duplicate rejection
  - Zotero Web API report remote_summary.item_fingerprints uniqueness
  - Zotero Web API report evidence_manifest.source_records uniqueness
  - standalone Zotero Web API EvidenceManifest source_records uniqueness
  - metadata-only privacy boundary and non-final report semantics
- Tests run:
  - python -m pytest tests\test_paper_real_zotero_metadata_only_pilot.py -q
  - python -m pytest tests\test_zotero_web_metadata_pilot.py -q
  - python -m pytest tests\test_paper_real_zotero_metadata_only_pilot.py tests\test_zotero_web_metadata_pilot.py tests\test_paper_real_pilot_authorization_request.py tests\test_paper_business_capability_validation.py -q
  - python -m ai_workflow_hub.cli paper real-pilot-authorization-request --output <artifact>
  - python -m json.tool schemas\paper_real_zotero_metadata_only_pilot_report.schema.json
  - python -m json.tool schemas\paper_zotero_web_api_metadata_only_pilot_report.schema.json
  - python -m json.tool schemas\paper_zotero_web_api_metadata_only_evidence_manifest.schema.json
  - git diff --check b249d2f1f6ac25183a89ac4a17750203a09743ce 3667207d28b51e9aa519126a382c4d9537641a13
- Generated artifacts:
  - D:\devframe-system\.agent\evidence\evidence-opencode-zotero-manifest-uniqueness-batch-a63-a64-3667207.zip
  - Evidence package EXECUTION_REPORT.md and REVIEWER_INDEX.md
  - Parent review reports under D:\devframe-system\integration\reports
- Known gaps:
  - Local/offline schema/test hardening only.
  - No live Zotero/API/key reads.
  - No notes, attachments, PDF, full text, Obsidian, RAG, WriteLab, browser/CDP, cloud, MiniApp, or private runtime.
  - No RuntimeAuthorization grant and no real pilot execution.
  - Parent still owns final governance acceptance.
- Suggested review focus:
  - Confirm duplicate evidence records cannot mask missing distinct source/retrieval/redaction evidence.
  - Confirm duplicate item fingerprints/source records are rejected in Web API report and standalone manifest schemas.
  - Confirm no raw metadata/title/abstract/API key/user id/PDF/note/attachment path was introduced.
  - Confirm local/offline and non-final boundary remains unchanged.

Boundary:
- No live Zotero API call.
- No read of C:\Users\RD\key\zotero.txt or any key file.
- No notes, attachments, PDF, full text, Obsidian, RAG, WriteLab, browser/CDP, cloud, MiniApp, or private runtime.
- No RuntimeAuthorization grant, no real pilot execution, no live-ready claim, and no final governance acceptance.
