# Opencode Preauth Authorization Template Closed Shape Return Review

Date: 2026-06-15

## Status

`OPENCODE_PREAUTH_AUTHORIZATION_TEMPLATE_CLOSED_SHAPE_A1_ACCEPTED_FOR_PARENT_INTAKE`

Parent intake accepts the `dev-frame-opencode` A19 local/offline slice for
parent pin consideration.

## Source Return

- Module: `dev-frame-opencode`
- Branch: `codex/paper-audit-privacy-hard-gate`
- Commit: `86262b49abcf05cb3507aad575fe521c70d8cd51`
- Message: `Close preauth authorization template shape`
- Evidence ZIP:
  `D:\devframe-system\.agent\evidence\evidence-opencode-preauth-authorization-template-closed-shape-a1-86262b4.zip`
- Evidence ZIP SHA256:
  `345F97BB7AB6C766E71AEDA04A1813668D59536EEB9EA68153070CA08BBF3351`
- Evidence directory:
  `D:\devframe-system\.agent\evidence\opencode-preauth-authorization-template-closed-shape-a1-86262b4`

## Accepted Scope

The slice tightens the preauthorization packet schema:

- `human_runtime_authorization_request_template` is closed
- explicit properties are defined with `additionalProperties=false`
- `live_resource_access_permitted` remains `const: false`
- raw `paragraph_text` is invalid inside the template
- premature `live_resource_access_permitted=true` fails schema validation
- the template remains a request template, not a live runtime grant

## Parent Verification

- Evidence ZIP exists and SHA256 was captured.
- `python -m json.tool schemas\paper_real_pilot_preauth_packet.schema.json`
  from `D:\devframe-system\dev-frame-opencode`
  -> PASS.
- `git -C D:\devframe-system\dev-frame-opencode diff --check`
  -> PASS.
- `$env:PYTHONPATH='ai-workflow-hub\src'; python -m pytest ai-workflow-hub\tests\test_paper_real_pilot_preauth_packet.py -q`
  from `D:\devframe-system\dev-frame-opencode`
  -> 8 passed.
- `$env:PYTHONPATH='ai-workflow-hub\src'; python -m pytest ai-workflow-hub\tests\test_paper_real_pilot_preauth_packet.py ai-workflow-hub\tests\test_paper_real_pilot_authorization_request.py ai-workflow-hub\tests\test_paper_real_pilot_blocking.py ai-workflow-hub\tests\test_paper_real_pilot_local_dry_run.py ai-workflow-hub\tests\test_paper_real_zotero_metadata_only_pilot.py ai-workflow-hub\tests\test_paper_business_capability_validation.py -q`
  from `D:\devframe-system\dev-frame-opencode`
  -> 74 passed.

## Parent Boundary Decision

Accepted for parent intake/pin as:

- local synthetic/offline evidence only;
- metadata/local-fixture only;
- preauthorization template only, not real-resource authorization;
- not live-ready;
- not final acceptance;
- no real Zotero, Obsidian, RAG, WriteLab, MiniApp, browser/CDP, cloud, H5,
  MeterSphere, Android, PDF, attachment, full text, or private paper runtime
  authorization.

## Reviewer Index

- Changed parent files:
  - This report.
- Critical paths:
  - `human_runtime_authorization_request_template` closed-shape validation.
  - `live_resource_access_permitted=false` preauth boundary.
  - Rejection of raw `paragraph_text`.
  - Preauthorization-template to runtime-authorization boundary language.
- Generated artifacts:
  - This report only.
- Known gaps:
  - Parent did not unzip/deep-audit every artifact in this intake pass.
  - Parent did not run real Zotero, Obsidian, RAG, WriteLab, MiniApp, browser,
    PDF, attachment, full-text, or private paper runtime.
  - This is not a production/live readiness verdict.
