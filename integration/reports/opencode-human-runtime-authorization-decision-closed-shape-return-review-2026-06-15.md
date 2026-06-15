# Opencode Human RuntimeAuthorization Decision Closed Shape Return Review

Date: 2026-06-15

## Status

`OPENCODE_HUMAN_RUNTIME_AUTHORIZATION_DECISION_CLOSED_SHAPE_A1_ACCEPTED_FOR_PARENT_INTAKE`

Parent intake accepts the `dev-frame-opencode` A17 local/offline slice for
parent pin consideration.

## Source Return

- Module: `dev-frame-opencode`
- Branch: `codex/paper-audit-privacy-hard-gate`
- Commit: `f8de96134d61427854cd6e4c35e376914577e8af`
- Message: `Close human RuntimeAuthorization decision shape`
- Evidence ZIP:
  `D:\devframe-system\.agent\evidence\evidence-opencode-human-runtime-authorization-decision-closed-shape-a1-f8de961.zip`
- Evidence ZIP SHA256:
  `69DC3542CF33C4C64C4D39F443A41F18141A0CF9B825EC10A224F4AC6A0CE887`
- Evidence directory:
  `D:\devframe-system\.agent\evidence\opencode-human-runtime-authorization-decision-closed-shape-a1-f8de961`

## Accepted Scope

The slice tightens the human RuntimeAuthorization decision schema for the
Zotero metadata-only pilot:

- nested `runtime_authorization` is a closed metadata-only shape
- required gate-relevant fields include authorization id, task/project/workflow,
  timestamps, source/operation/repo allowlists, sensitive fields, gate refs,
  live-resource booleans, preflight, and revocation
- raw `paragraph_text` is invalid inside `runtime_authorization`
- raw paper text, PDF text, attachment paths, and WriteLab payload fields must
  not be carried by the human decision packet

## Parent Verification

- Evidence ZIP exists and SHA256 was captured.
- `python -m json.tool schemas\paper_real_pilot_human_runtime_authorization_decision.schema.json`
  from `D:\devframe-system\dev-frame-opencode`
  -> PASS
- `git -C D:\devframe-system\dev-frame-opencode diff --check`
  -> PASS.
- `$env:PYTHONPATH='ai-workflow-hub\src'; python -m pytest ai-workflow-hub\tests\test_paper_real_pilot_authorization_request.py -q`
  from `D:\devframe-system\dev-frame-opencode`
  -> 12 passed.
- `$env:PYTHONPATH='ai-workflow-hub\src'; python -m pytest ai-workflow-hub\tests\test_paper_real_pilot_authorization_request.py ai-workflow-hub\tests\test_paper_real_pilot_blocking.py ai-workflow-hub\tests\test_paper_real_pilot_local_dry_run.py ai-workflow-hub\tests\test_paper_real_pilot_preauth_packet.py ai-workflow-hub\tests\test_paper_real_zotero_metadata_only_pilot.py ai-workflow-hub\tests\test_paper_business_capability_validation.py -q`
  from `D:\devframe-system\dev-frame-opencode`
  -> 71 passed.

## Parent Boundary Decision

Accepted for parent intake/pin as:

- local synthetic/offline evidence only;
- metadata/local-fixture only;
- not live-ready;
- not final acceptance;
- no real Zotero, Obsidian, RAG, WriteLab, MiniApp, browser/CDP, cloud, H5,
  MeterSphere, Android, PDF, attachment, full text, or private paper runtime
  authorization.

## Reviewer Index

- Changed parent files:
  - This report.
- Critical paths:
  - human decision `runtime_authorization` closed-shape validation.
  - raw RuntimeAuthorization/paper payload rejection.
  - candidate-to-final boundary language.
  - evidence ZIP existence and hash capture.
- Generated artifacts:
  - This report only.
- Known gaps:
  - Parent did not unzip/deep-audit every artifact in this intake pass.
  - Parent did not run real Zotero, Obsidian, RAG, WriteLab, MiniApp, browser,
    PDF, attachment, full-text, or private paper runtime.
  - This is not a production/live readiness verdict.
