# Opencode Agent Acceptance Rules Closed Shape Return Review

Date: 2026-06-15

## Status

`OPENCODE_AGENT_ACCEPTANCE_RULES_CLOSED_SHAPE_A1_ACCEPTED_FOR_PARENT_INTAKE`

Parent intake accepts the `dev-frame-opencode` A18 local/offline slice for
parent pin consideration.

## Source Return

- Module: `dev-frame-opencode`
- Branch: `codex/paper-audit-privacy-hard-gate`
- Commit: `8ae6cb77ac977a602dd834efd14405a523c0cb5a`
- Message: `Close agent acceptance rules pilot shapes`
- Evidence ZIP:
  `D:\devframe-system\.agent\evidence\evidence-opencode-agent-acceptance-rules-closed-shape-a1-8ae6cb7.zip`
- Evidence ZIP SHA256:
  `E97DA005A1F1B6F8D3CCD1DBF916380E8C17880249889620E0C35F8E7B76476D`
- Evidence directory:
  `D:\devframe-system\.agent\evidence\opencode-agent-acceptance-rules-closed-shape-a1-8ae6cb7`

## Accepted Scope

The slice tightens `agent_acceptance_rules` in both real-pilot
RuntimeAuthorization request and human RuntimeAuthorization decision schemas:

- `agent_acceptance_rules` is closed in both schemas
- `real_resource_authorization_granted=false` remains locked
- `rules_ready=true` and `verdict=accepted_with_limitations` are governance
  readiness evidence only
- extra `runtime_authorization_ref` is invalid inside `agent_acceptance_rules`
- agent-acceptance rules remain governance readiness, not runtime authorization

## Parent Verification

- `$env:PYTHONPATH='src'; python -m pytest tests\test_paper_real_pilot_authorization_request.py -q`
  -> 14 passed
- `$env:PYTHONPATH='src'; $files = Get-ChildItem tests -Filter 'test_paper_real_pilot_*.py' | ForEach-Object { $_.FullName }; python -m pytest @files tests\test_paper_real_zotero_metadata_only_pilot.py -q`
  -> 66 passed
- `$env:PYTHONPATH='src'; python -m pytest tests\test_paper_business_capability_validation.py -q`
  -> 7 passed
- `python -m json.tool schemas\paper_real_pilot_runtime_authorization_request.schema.json`
  -> PASS
- `python -m json.tool schemas\paper_real_pilot_human_runtime_authorization_decision.schema.json`
  -> PASS
- `git diff --check` -> PASS, CRLF warnings only

## Parent Boundary Decision

Accepted for parent intake/pin as:

- local synthetic/offline evidence only;
- metadata/local-fixture only;
- governance-readiness evidence only, not runtime authorization;
- not live-ready;
- not final acceptance;
- no real Zotero, Obsidian, RAG, WriteLab, MiniApp, browser/CDP, cloud, H5,
  MeterSphere, Android, PDF, attachment, full text, or private paper runtime
  authorization.

## Reviewer Index

- Changed parent files:
  - This report.
- Critical paths:
  - `agent_acceptance_rules` closed-shape validation in request and decision
    schemas.
  - Rejection of `real_resource_authorization_granted=true`.
  - Rejection of embedded `runtime_authorization_ref`.
  - Governance-readiness to runtime-authorization boundary language.
- Generated artifacts:
  - This report only.
- Known gaps:
  - Parent did not unzip/deep-audit every artifact in this intake pass.
  - Parent did not run real Zotero, Obsidian, RAG, WriteLab, MiniApp, browser,
    PDF, attachment, full-text, or private paper runtime.
  - This is not a production/live readiness verdict.
