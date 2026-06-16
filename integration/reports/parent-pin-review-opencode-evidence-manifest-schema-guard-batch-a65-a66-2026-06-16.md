# Parent Pin Review: opencode evidence manifest schema guard batch A65-A66

Status: ACCEPTED_AND_PARENT_PINNED

Parent scope:
- Repository: D:\devframe-system
- Submodule: dev-frame-opencode
- Previous parent pin: 3667207d28b51e9aa519126a382c4d9537641a13
- New pin: 4907c0d0da66566df6225f95045ed3cc97ab8fcc
- Batch:
  - OPENCODE_PAPER_EVIDENCE_MANIFEST_UNIQUENESS_A1
  - OPENCODE_PREAUTH_SCENARIO_CONTAINS_SCHEMA_GUARD_A1

Evidence reviewed:
- ZIP: D:\devframe-system\.agent\evidence\evidence-opencode-evidence-manifest-schema-guard-batch-a65-a66-4907c0d.zip
- SHA256: 63B43BBF2726E3EC704E7FBD1D34A93F4E88A7A1239FCC9C4E699B859D2D33DA
- Return review: D:\devframe-system\integration\reports\opencode-evidence-manifest-schema-guard-batch-a65-a66-return-review-2026-06-16.md

Accepted changes:
- Generic paper EvidenceManifest duplicate source/retrieval/redaction records fail closed.
- Generic paper EvidenceManifest duplicate commands/tests/artifacts fail closed.
- Runtime validate_evidence_manifest returns duplicate_* reasons for repeated evidence lists.
- Preauth scenario matrix contains guards no longer introduce undocumented open object schema paths.
- P1-P5 scenario exact-count constraints remain enforced through outer closed item schema.

Verification summary:
- Evidence ZIP SHA256 matched the declared value.
- Evidence ZIP contained EXECUTION_REPORT.md, REVIEWER_INDEX.md, command logs, changed-files, and schema copies.
- dev-frame-opencode HEAD matched 4907c0d0da66566df6225f95045ed3cc97ab8fcc at intake.
- Parent lock files updated to 4907c0d0da66566df6225f95045ed3cc97ab8fcc.
- Parent staged diff check required before commit.

Source verification recorded by opencode evidence:
- python -m pytest tests\test_paper_evidence_manifest.py tests\test_paper_schema_raw_payload_guards.py tests\test_paper_runtime_authorization_gate.py -q -> 20 passed
- python -m pytest tests\test_paper_real_pilot_authorization_request.py tests\test_paper_real_pilot_blocking.py tests\test_paper_real_pilot_local_dry_run.py tests\test_paper_real_pilot_preauth_packet.py -q -> 50 passed
- python -m json.tool schemas\paper_evidence_manifest.schema.json -> PASS
- python -m json.tool schemas\paper_real_pilot_preauth_packet.schema.json -> PASS
- git diff --check 3667207d28b51e9aa519126a382c4d9537641a13 4907c0d0da66566df6225f95045ed3cc97ab8fcc -> PASS

Boundary:
- Local/offline schema and gate hardening only.
- No live Zotero API call.
- No read of C:\Users\RD\key\zotero.txt or any key file.
- No notes, attachments, PDF, full text, Obsidian, RAG, WriteLab, browser/CDP, cloud, MiniApp, or private runtime.
- No RuntimeAuthorization grant.
- No real pilot execution.
- No live-ready, production-ready, or final governance acceptance claim.

Known parent dirty state:
- Existing unrelated parent drift remains outside this pin and must not be inferred as part of A65-A66.
- test-frame currently has separate local drift beyond the parent lock; it is not included in this opencode pin.
