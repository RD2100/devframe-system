# dev-frame-opencode A59-A60 Real Pilot Set-Like Fields Return Review

Date: 2026-06-16

## Verdict

ACCEPTED_FOR_PARENT_PIN_WITH_LIMITATIONS

## Reviewed Return

- Module: dev-frame-opencode
- Branch: codex/paper-audit-privacy-hard-gate
- Target commit: 580f6e9f3ad2ff7c22949d1694990a12b822ce12
- Previous parent pin: 62994c1c45009032c1cb81053a07917b130449b2
- Scope: local/offline real-pilot schema hardening

## Batch Commits

1. be06c811bde50ef4c85d92629ba22f762bc02acd
   - Close real pilot request set fields
2. 580f6e9f3ad2ff7c22949d1694990a12b822ce12
   - Close real pilot authorization decision sets

## Evidence

- Evidence ZIP: D:\devframe-system\.agent\evidence\evidence-opencode-real-pilot-set-like-fields-batch-a59-a60-580f6e9.zip
- SHA256: F879907BF10CEFE5C7DA7E1608DB88E695EA0F6A8DE69AFD4CC3385A89C01130

## Parent-Side Verification

- `git -C dev-frame-opencode rev-parse HEAD` -> 580f6e9f3ad2ff7c22949d1694990a12b822ce12
- `git -C dev-frame-opencode status --short --branch` -> clean except branch ahead marker
- `Get-FileHash` for evidence ZIP -> matched declared SHA256
- From `D:\devframe-system\dev-frame-opencode\ai-workflow-hub`:
  - `$env:PYTHONPATH='src'; python -m pytest tests\test_paper_real_pilot_authorization_request.py tests\test_paper_real_pilot_local_dry_run.py tests\test_paper_real_pilot_blocking.py tests\test_paper_real_pilot_preauth_packet.py tests\test_paper_real_zotero_metadata_only_pilot.py -q` -> 80 passed
  - `$env:PYTHONPATH='src'; python -m ai_workflow_hub.cli paper real-pilot-authorization-request --output <temp json>` -> PASS
  - generated authorization request JSON parse -> PASS
  - `$env:PYTHONPATH='src'; python -m ai_workflow_hub.cli paper real-pilot-dry-run --output <temp json>` -> PASS
  - generated dry-run JSON parse -> PASS
  - `$env:PYTHONPATH='src'; python -m ai_workflow_hub.cli paper real-pilot-authorize-metadata --output <temp json>` -> PASS
  - generated authorization decision JSON parse -> PASS
- From `D:\devframe-system\dev-frame-opencode`:
  - `python -m json.tool schemas\paper_real_pilot_runtime_authorization_request.schema.json` -> PASS
  - `python -m json.tool schemas\paper_real_pilot_local_dry_run_report.schema.json` -> PASS
  - `python -m json.tool schemas\paper_real_pilot_human_runtime_authorization_decision.schema.json` -> PASS
  - `git diff --check 62994c1c45009032c1cb81053a07917b130449b2 580f6e9f3ad2ff7c22949d1694990a12b822ce12` -> PASS

## Reviewer Index

- Changed parent files for intake:
  - D:\devframe-system\BASELINE_LOCK.json
  - D:\devframe-system\integration\lock\submodules.lock.yml
  - D:\devframe-system\integration\reports\opencode-real-pilot-set-like-fields-batch-a59-a60-return-review-2026-06-16.md
  - D:\devframe-system\integration\reports\parent-pin-review-opencode-real-pilot-set-like-fields-batch-a59-a60-2026-06-16.md
  - D:\devframe-system\dev-frame-opencode gitlink
- Critical module paths covered:
  - schemas/paper_real_pilot_runtime_authorization_request.schema.json
  - schemas/paper_real_pilot_local_dry_run_report.schema.json
  - schemas/paper_real_pilot_human_runtime_authorization_decision.schema.json
  - ai-workflow-hub/tests/test_paper_real_pilot_authorization_request.py
  - ai-workflow-hub/tests/test_paper_real_pilot_local_dry_run.py
- Suggested review focus:
  - confirm added uniqueItems constraints cover only set-like governance fields
  - confirm duplicate sensitive fields, redaction fields, verdict options, non-claims, known_gaps, and non-approved resources are rejected
  - confirm no real-resource authorization semantics were expanded
  - confirm local/offline and non-final boundary remains unchanged

## Boundary

- Local/offline schema and CLI smoke only.
- No live Zotero API call.
- No read of C:\Users\RD\key\zotero.txt or any key file.
- No notes, attachments, PDF, full text, Obsidian, RAG, WriteLab, browser/CDP, cloud, MiniApp, or private runtime.
- This does not grant RuntimeAuthorization, does not start real pilot execution, and is not final governance acceptance.

## Known Gaps

- Parent review did not unzip and deep-audit every evidence artifact payload.
- This does not prove live Zotero, PDF/full-text, Obsidian, RAG, WriteLab, paper-quality acceptance, or real pilot execution.
