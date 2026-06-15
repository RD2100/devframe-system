# dev-frame-opencode Zotero Web API Metadata Manifest Batch A35-A36 Parent Intake

Date: 2026-06-16
Parent repo: `D:\devframe-system`
Submodule: `dev-frame-opencode`
Status: `READY_FOR_BATCH_PARENT_INTAKE`

## Decision

Parent intake accepts the `dev-frame-opencode` Zotero Web API metadata-only
manifest batch from `b097217...` through
`bd1bbb5920dfd714ff053a10d8657f95d4449bfe`.

This is local/offline evidence consumer hardening. It is not final governance
acceptance, not production readiness, and not authorization for notes,
attachments, PDF, full text, Obsidian, RAG, WriteLab, browser/CDP, cloud, or
MiniApp.

## Batch Commits

1. `5542fef9cd7bb9e70e6e772f98384da3580e6149`
   - `Add Zotero Web manifest output`
   - Evidence ZIP:
     `D:\devframe-system\.agent\evidence\evidence-opencode-zotero-web-manifest-output-a1-5542fef.zip`
   - SHA256:
     `82D5E3EB440A67202692C706FFA19D4E0EABCDBFA7539BF6AED4C1A852352F1F`

2. `bd1bbb5920dfd714ff053a10d8657f95d4449bfe`
   - `Add Zotero Web manifest schema`
   - Evidence ZIP:
     `D:\devframe-system\.agent\evidence\evidence-opencode-zotero-web-manifest-schema-a1-bd1bbb5.zip`
   - SHA256:
     `3C9B9BCC20275931AF7763F86C31A8E00FDF2FD495AFEFDE11C6857D0F7346E5`

## Implementation Summary

Changed files across batch:

- `ai-workflow-hub/src/ai_workflow_hub/cli.py`
- `ai-workflow-hub/tests/test_zotero_web_metadata_pilot.py`
- `ai-workflow-hub/docs/paper/PAPER_REAL_ZOTERO_METADATA_ONLY_PILOT.md`
- `schemas/paper_zotero_web_api_metadata_only_evidence_manifest.schema.json`

Batch behavior:

- adds optional CLI flag `paper zotero-web-metadata-pilot --manifest-output`;
- writes standalone minimized EvidenceManifest only when the report contains
  PASS metadata-only `evidence_manifest`;
- BLOCKED, EMPTY, and CONNECTION_REQUIRED reports do not produce standalone
  manifest files;
- adds a standalone closed schema for Zotero Web API metadata-only
  EvidenceManifest;
- validates standalone manifest output against the standalone schema;
- adds negative tests rejecting raw payload fields in the standalone manifest.

## Parent Verification

Commands run:

- `git -C dev-frame-opencode status --short --branch`
- `git -C dev-frame-opencode rev-parse HEAD`
- SHA256 verification for both evidence ZIPs
- `$env:PYTHONPATH='src'; python -m pytest tests\test_zotero_web_metadata_pilot.py -q`
- `python -m json.tool schemas\paper_zotero_web_api_metadata_only_evidence_manifest.schema.json`
- `python -m json.tool schemas\paper_zotero_web_api_metadata_only_pilot_report.schema.json`
- `git diff --check b097217c9ad3b53d4c28a03a7fb1510d2606bf71 bd1bbb5920dfd714ff053a10d8657f95d4449bfe`

Observed:

- submodule worktree clean at `bd1bbb5...`;
- both evidence ZIP hashes matched;
- adapter/manifest tests: `15 passed`;
- both schema JSON parses: PASS;
- batch diff check: PASS.

## Boundary

- Local/offline-only batch.
- No live Zotero API call.
- No read of `C:\Users\RD\key\zotero.txt`.
- Standalone EvidenceManifest is review evidence only.
- Manifest output must not contain API key, raw user id, raw item JSON, raw
  titles, raw abstracts, notes, attachments, PDF paths, or full text.
- Not final governance acceptance and not production ready.

## Reviewer Index

Critical review paths:

- CLI `--manifest-output`;
- standalone EvidenceManifest schema;
- PASS-only manifest generation;
- BLOCKED/EMPTY/CONNECTION_REQUIRED no-manifest behavior;
- raw payload rejection tests.

Review focus:

- standalone manifest is minimized and closed;
- non-PASS reports do not create standalone manifests;
- manifest cannot carry raw/private Zotero payload;
- metadata-only manifest does not become final acceptance.
