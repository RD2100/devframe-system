# opencode A65-A66 evidence manifest/schema guard return review

Status: ACCEPT_FOR_PARENT_INTAKE_WAIT_FOR_PARENT_PIN_COMMAND

Reviewed return:
- Module: dev-frame-opencode
- Path: D:\devframe-system\dev-frame-opencode
- Branch: codex/paper-audit-privacy-hard-gate
- Base: 3667207d28b51e9aa519126a382c4d9537641a13
- Commit: 4907c0d0da66566df6225f95045ed3cc97ab8fcc
- TaskSpec batch:
  - OPENCODE_PAPER_EVIDENCE_MANIFEST_UNIQUENESS_A1
  - OPENCODE_PREAUTH_SCENARIO_CONTAINS_SCHEMA_GUARD_A1
- Evidence ZIP:
  D:\devframe-system\.agent\evidence\evidence-opencode-evidence-manifest-schema-guard-batch-a65-a66-4907c0d.zip
- Evidence ZIP SHA256:
  63B43BBF2726E3EC704E7FBD1D34A93F4E88A7A1239FCC9C4E699B859D2D33DA

Accepted scope:
- Local/offline schema and runtime gate hardening only.
- paper_evidence_manifest source, retrieval, redaction, command, test, and
  artifact arrays reject duplicates.
- validate_evidence_manifest returns duplicate_* failure reasons for repeated
  evidence lists.
- preauth packet scenario contains schemas avoid open object schema paths while
  preserving closed outer item schemas and exact P1-P5 counts.

Parent-side verification:
- dev-frame-opencode HEAD matched 4907c0d0da66566df6225f95045ed3cc97ab8fcc.
- dev-frame-opencode tracked worktree was clean at review time.
- Evidence ZIP SHA256 matched
  63B43BBF2726E3EC704E7FBD1D34A93F4E88A7A1239FCC9C4E699B859D2D33DA.
- Evidence ZIP entries present:
  changed-files/changed-files.txt, command logs, schemas, EXECUTION_REPORT.md,
  and REVIEWER_INDEX.md.
- python -m json.tool schemas\paper_evidence_manifest.schema.json: PASS.
- python -m json.tool schemas\paper_real_pilot_preauth_packet.schema.json:
  PASS.
- $env:PYTHONPATH='src'; python -m pytest
  tests\test_paper_evidence_manifest.py
  tests\test_paper_schema_raw_payload_guards.py
  tests\test_paper_runtime_authorization_gate.py -q: 20 passed.
- $env:PYTHONPATH='src'; python -m pytest
  tests\test_paper_real_pilot_authorization_request.py
  tests\test_paper_real_pilot_blocking.py
  tests\test_paper_real_pilot_local_dry_run.py
  tests\test_paper_real_pilot_preauth_packet.py -q: 50 passed.
- git diff --check
  3667207d28b51e9aa519126a382c4d9537641a13
  4907c0d0da66566df6225f95045ed3cc97ab8fcc: PASS.

Reviewer Index:
- Changed files:
  - D:\devframe-system\dev-frame-opencode\ai-workflow-hub\src\ai_workflow_hub\context_layer\adapters\paper_real_pilot_gate.py
  - D:\devframe-system\dev-frame-opencode\ai-workflow-hub\tests\test_paper_evidence_manifest.py
  - D:\devframe-system\dev-frame-opencode\schemas\paper_evidence_manifest.schema.json
  - D:\devframe-system\dev-frame-opencode\schemas\paper_real_pilot_preauth_packet.schema.json
- Critical code paths:
  - evidence manifest duplicate rejection
  - validate_evidence_manifest fail-closed duplicate reasons
  - preauth packet pilot_scenario_matrix contains constraints
  - no raw-sensitive/live/final overclaim gate
- Tests run:
  - $env:PYTHONPATH='src'; python -m pytest tests\test_paper_evidence_manifest.py tests\test_paper_schema_raw_payload_guards.py tests\test_paper_runtime_authorization_gate.py -q
  - $env:PYTHONPATH='src'; python -m pytest tests\test_paper_real_pilot_authorization_request.py tests\test_paper_real_pilot_blocking.py tests\test_paper_real_pilot_local_dry_run.py tests\test_paper_real_pilot_preauth_packet.py -q
  - python -m json.tool schemas\paper_evidence_manifest.schema.json
  - python -m json.tool schemas\paper_real_pilot_preauth_packet.schema.json
  - git diff --check 3667207d28b51e9aa519126a382c4d9537641a13 4907c0d0da66566df6225f95045ed3cc97ab8fcc
- Generated artifacts:
  - D:\devframe-system\.agent\evidence\evidence-opencode-evidence-manifest-schema-guard-batch-a65-a66-4907c0d.zip
  - D:\devframe-system\.agent\evidence\opencode-evidence-manifest-schema-guard-batch-a65-a66-4907c0d\EXECUTION_REPORT.md
  - D:\devframe-system\.agent\evidence\opencode-evidence-manifest-schema-guard-batch-a65-a66-4907c0d\REVIEWER_INDEX.md
- Known gaps:
  - Local/offline schema and gate evidence only.
  - No live Zotero API call, no Zotero key read, no notes, attachments, PDF,
    full text, Obsidian, RAG, WriteLab, browser/CDP, cloud, MiniApp, or private
    runtime.
  - No RuntimeAuthorization grant, no real pilot execution, no live-ready or
    final governance acceptance claim.
- Suggested review focus:
  - Confirm duplicate entries cannot pad source/retrieval/redaction/command/test/artifact evidence.
  - Confirm duplicate_* validation reasons are fail-closed and not warning-only.
  - Confirm preauth scenario contains constraints still enforce exact P1-P5
    coverage through the outer closed item schema.
  - Confirm no raw sensitive payload fields or final/live overclaims were
    introduced.

Boundary:
- This is not final governance acceptance.
- This is not a parent pin.
- This is not RuntimeAuthorization.
- This does not prove live Zotero, PDF/full-text, Obsidian, RAG, WriteLab, real
  pilot execution, or production readiness.
