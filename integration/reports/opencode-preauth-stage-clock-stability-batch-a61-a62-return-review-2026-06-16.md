# opencode A61-A62 preauth stage and clock stability return review

Status: ACCEPTED_WITH_LIMITATIONS_FOR_PARENT_PIN

Reviewed return:
- Module: dev-frame-opencode
- Path: D:\devframe-system\dev-frame-opencode
- Branch: codex/paper-audit-privacy-hard-gate
- Commit: b249d2f1f6ac25183a89ac4a17750203a09743ce
- Base: 580f6e9f3ad2ff7c22949d1694990a12b822ce12
- TaskSpec batch: OPENCODE_PREAUTH_STAGE_CLOCK_STABILITY_BATCH_A61_A62
- Evidence ZIP: D:\devframe-system\.agent\evidence\evidence-opencode-preauth-stage-clock-stability-batch-a61-a62-b249d2f.zip
- Evidence ZIP SHA256: FDC05D649EB7FA89A64E56B55C0DA8F0400DA4165BB48F85E4D72C9585657D12

Hash correction:
- The initial handoff text contained a typo: b249d2fe9e6ab6a5e6dbb4b9f4f09e213f432066.
- The verified local Git object and evidence report head are b249d2f1f6ac25183a89ac4a17750203a09743ce.
- Parent intake uses the verified local object b249d2f1f6ac25183a89ac4a17750203a09743ce.

Accepted scope:
- Local/offline real-pilot governance schema/test hardening.
- Preauthorization scenario matrix stage coverage and scenario set-like array duplicate rejection.
- Deterministic local test evaluation time for real pilot authorization checks.
- RuntimeAuthorization expiry checks remain active; this does not grant real-resource authorization.

Parent-side verification:
- dev-frame-opencode HEAD matched b249d2f1f6ac25183a89ac4a17750203a09743ce.
- dev-frame-opencode tracked worktree was clean at review time.
- Evidence ZIP SHA256 matched FDC05D649EB7FA89A64E56B55C0DA8F0400DA4165BB48F85E4D72C9585657D12.
- Focused preauth packet pytest: 13 passed.
- Real-pilot focused pytest suite: 81 passed.
- Runtime clock stability pytest suite: 55 passed.
- real-pilot-preauth CLI smoke: PASS, JSON parse PASS.
- real-pilot-dry-run CLI smoke: PASS, JSON parse PASS.
- paper_real_pilot_preauth_packet schema parse: PASS.
- git diff --check 580f6e9f3ad2ff7c22949d1694990a12b822ce12 b249d2f1f6ac25183a89ac4a17750203a09743ce: PASS.

Reviewer Index:
- Changed files:
  - D:\devframe-system\dev-frame-opencode\schemas\paper_real_pilot_preauth_packet.schema.json
  - D:\devframe-system\dev-frame-opencode\ai-workflow-hub\tests\test_paper_real_pilot_preauth_packet.py
  - D:\devframe-system\dev-frame-opencode\ai-workflow-hub\src\ai_workflow_hub\context_layer\adapters\paper_real_pilot_gate.py
  - D:\devframe-system\dev-frame-opencode\ai-workflow-hub\src\ai_workflow_hub\context_layer\adapters\zotero_metadata_real_pilot.py
  - D:\devframe-system\dev-frame-opencode\ai-workflow-hub\tests\test_paper_real_pilot_authorization_request.py
  - D:\devframe-system\dev-frame-opencode\ai-workflow-hub\tests\test_paper_real_pilot_blocking.py
  - D:\devframe-system\dev-frame-opencode\ai-workflow-hub\tests\test_paper_real_zotero_metadata_only_pilot.py
- Critical paths:
  - paper_real_pilot_preauth_packet scenario matrix schema closure
  - scenario allowed_sources / allowed_operations / sensitive_fields / blocking_conditions duplicate rejection
  - evaluate_real_pilot_request evaluation time handling
  - local dry-run and Zotero export report generated_at evaluation time handling
  - RuntimeAuthorization expiry tests
- Tests run:
  - python -m pytest tests\test_paper_real_pilot_preauth_packet.py -q
  - python -m pytest tests\test_paper_real_pilot_authorization_request.py tests\test_paper_real_pilot_local_dry_run.py tests\test_paper_real_pilot_blocking.py tests\test_paper_real_pilot_preauth_packet.py tests\test_paper_real_zotero_metadata_only_pilot.py -q
  - python -m pytest tests\test_paper_runtime_authorization_gate.py tests\test_paper_real_pilot_authorization_request.py tests\test_paper_real_zotero_metadata_only_pilot.py -q
  - python -m ai_workflow_hub.cli paper real-pilot-preauth --output <artifact>
  - python -m ai_workflow_hub.cli paper real-pilot-dry-run --output <artifact>
  - python -m json.tool schemas\paper_real_pilot_preauth_packet.schema.json
  - git diff --check 580f6e9f3ad2ff7c22949d1694990a12b822ce12 b249d2f1f6ac25183a89ac4a17750203a09743ce
- Generated artifacts:
  - D:\devframe-system\.agent\evidence\evidence-opencode-preauth-stage-clock-stability-batch-a61-a62-b249d2f.zip
  - Evidence package EXECUTION_REPORT.md and REVIEWER_INDEX.md
  - Parent review reports under D:\devframe-system\integration\reports
- Known gaps:
  - Local/offline governance schema/test hardening only.
  - No live Zotero/API/key reads.
  - No notes, attachments, PDF, full text, Obsidian, RAG, WriteLab, browser/CDP, cloud, MiniApp, or private runtime.
  - No RuntimeAuthorization grant and no real pilot execution.
  - Parent still owns final governance acceptance.
- Suggested review focus:
  - Confirm scenario matrix cannot duplicate P1/P5 while omitting P2/P4.
  - Confirm scenario set-like arrays reject duplicates without widening pilot scope.
  - Confirm explicit evaluation time stabilizes tests without disabling expiry checks.
  - Confirm non-final/local-offline boundary remains unchanged.

Boundary:
- No live Zotero API call.
- No read of C:\Users\RD\key\zotero.txt or any key file.
- No notes, attachments, PDF, full text, Obsidian, RAG, WriteLab, browser/CDP, cloud, MiniApp, or private runtime.
- No RuntimeAuthorization grant, no real pilot execution, no live-ready claim, and no final governance acceptance.
