# test-frame Zotero Metadata Manifest Consumption Parent Intake

Date: 2026-06-16
Parent repo: `D:\devframe-system`
Submodule: `test-frame`
TaskSpec: `TESTFRAME_ZOTERO_WEB_API_METADATA_MANIFEST_CONSUMPTION_A1`
Status: `READY_FOR_PARENT_INTAKE`

## Decision

Parent intake accepts `test-frame` commit
`d62356481e24c3c0118fa5b7f705fe576b307fb1` as the test-frame-side standalone
EvidenceManifest consumption contract for parent-pinned `dev-frame-opencode`
A35-A36 Zotero Web API metadata-only manifest output/schema hardening.

This is verification evidence only. It is not final governance acceptance, not
live readiness, and not production readiness.

## Evidence

Evidence ZIP:

`D:\devframe-system\test-frame\reports\evidence-zotero-metadata-manifest-consumption-a1.zip`

Expected SHA256:

`2E7933915C624805062A33735E00E2B3173779B05A0504D7723CB3B9C040C0D3`

Observed SHA256:

`2E7933915C624805062A33735E00E2B3173779B05A0504D7723CB3B9C040C0D3`

Generated artifacts:

- `D:\devframe-system\test-frame\reports\zotero-metadata-manifest-consumption-a1\EXECUTION_REPORT.md`
- `D:\devframe-system\test-frame\reports\zotero-metadata-manifest-consumption-a1\REVIEWER_INDEX.md`
- `D:\devframe-system\test-frame\reports\zotero-metadata-manifest-consumption-a1\STATUS_SUMMARY.md`
- `D:\devframe-system\test-frame\reports\zotero-metadata-manifest-consumption-a1\manifests\evidence-manifest.json`

## Implementation Summary

Changed files in submodule commit:

- `docs/test-frame/zotero-web-api-metadata-only/README.md`
- `docs/test-frame/zotero-web-api-metadata-only/opencode-manifest-consumption.fixture.json`
- `tests/test_zotero_metadata_manifest_consumption.py`

Coverage:

- positive `PASS_METADATA_ONLY` standalone minimized EvidenceManifest can be
  consumed as test-frame verification evidence;
- BLOCKED / EMPTY_REMOTE_LIBRARY / ZOTERO_METADATA_CONNECTION_REQUIRED
  producing standalone manifest fails closed;
- closed manifest/source-record shape is enforced;
- schema ref/provenance is enforced: producer module, producer commit, schema
  path, schema version, `additional_properties=false`, and required field
  parity;
- raw sensitive markers and token-like values fail closed;
- raw item JSON, raw title, raw abstract, notes, attachments, PDF, full text,
  and `paragraph_text` markers fail closed;
- final acceptance, live-ready, and production-ready overclaims fail closed.

## Parent Verification

Commands run:

- `git -C test-frame status --short --branch`
- `git -C test-frame rev-parse HEAD`
- `Get-FileHash test-frame\reports\evidence-zotero-metadata-manifest-consumption-a1.zip -Algorithm SHA256`
- `python -m pytest tests\test_zotero_metadata_manifest_consumption.py -q`
- `python -m pytest tests\test_zotero_web_api_metadata_only_contract.py tests\test_zotero_metadata_adapter_evidence_consumption.py tests\test_zotero_metadata_hardening_consumption.py tests\test_zotero_metadata_manifest_consumption.py -q`
- `python -m json.tool docs\test-frame\zotero-web-api-metadata-only\opencode-manifest-consumption.fixture.json`
- `python -m json.tool reports\zotero-metadata-manifest-consumption-a1\manifests\evidence-manifest.json`
- `git diff --check HEAD~1 HEAD`

Observed:

- submodule worktree clean at `d623564...`;
- evidence ZIP hash matched;
- focused tests: `8 passed`;
- grouped metadata tests: `27 passed`;
- fixture and evidence manifest JSON parse: PASS;
- submodule diff check: PASS.

## Known Gaps

- Synthetic/offline replay only.
- Does not call Zotero API, read credentials, inspect raw response, or validate
  live connectivity.
- Does not validate PDF, attachment, full text, notes, WriteLab, Obsidian, RAG,
  browser/CDP, cloud, or MiniApp.
- test-frame pass is verification evidence only, not final governance
  acceptance.

## Boundary

No read of `C:\Users\RD\key\zotero.txt`.
No Zotero Web API call.
No raw API response, title, abstract, item JSON, API key, or raw user id read.
No PDF, attachments, notes, full text, or real `paragraph_text`.
No WriteLab, Obsidian, RAG, browser/CDP, cloud, or MiniApp.
No final acceptance/live-ready/production-ready claim.
