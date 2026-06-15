# test-frame Zotero Metadata Adapter Evidence Consumption Parent Intake

Date: 2026-06-16
Parent repo: `D:\devframe-system`
Submodule: `test-frame`
TaskSpec: `TESTFRAME_ZOTERO_METADATA_ADAPTER_EVIDENCE_CONSUMPTION_A1`
Status: `READY_FOR_PARENT_INTAKE`

## Decision

Parent intake accepts `test-frame` commit
`f8bce53333f9087af06b1842716f73777794be27` as the test-frame-side
consumption validation layer for parent-pinned `dev-frame-opencode` Zotero Web
API metadata-only minimized evidence.

This is verification evidence only. It is not final governance acceptance, not
paper quality verdict, and not live/full-paper readiness.

## Source Evidence

Source opencode adapter commit:

`bd31f7feb4353412d2ac70cf614f4db3b70c3770`

Source opencode evidence ZIP:

`D:\devframe-system\.agent\evidence\evidence-opencode-zotero-web-api-metadata-only-adapter-a1-bd31f7f.zip`

Source ZIP SHA256 verified by test-frame:

`8799B7DB7D815954269FA01BB0BF15AAF507882494DE1180707E55F068143B47`

Consumed minimized entries only:

- `LIVE_SMOKE_SUMMARY.json`
- `reports/zotero-web-api-metadata-only-pilot-report.json`

## test-frame Evidence

Evidence ZIP:

`D:\devframe-system\test-frame\reports\evidence-zotero-metadata-adapter-evidence-consumption-a1.zip`

Expected SHA256:

`0FCB3C99E45AC5AAEF467135842A99A2EDE5B5CD5E9485240628EFE1A9010195`

Observed SHA256:

`0FCB3C99E45AC5AAEF467135842A99A2EDE5B5CD5E9485240628EFE1A9010195`

## Implementation Summary

Changed files in submodule commit:

- `docs/test-frame/zotero-web-api-metadata-only/README.md`
- `docs/test-frame/zotero-web-api-metadata-only/opencode-minimized-evidence-consumption.fixture.json`
- `tests/test_zotero_metadata_adapter_evidence_consumption.py`

Implemented behavior:

- added a minimized/redacted opencode evidence consumption fixture;
- fixture keeps counts, item type counts, redaction counts, version range,
  producer commit/hash, and boundary booleans;
- positive `PASS_METADATA_ONLY` minimized evidence can be consumed as
  test-frame verification evidence only;
- fail-closed negative cases cover:
  - `final_acceptance_claimed=true`;
  - `live_ready_claimed=true`;
  - test-frame pass promoted to final governance;
  - raw persistence flags true;
  - notes/attachments/PDF/full-text flags true;
  - records=0 while PASS;
  - forbidden item type counts present while PASS;
  - raw sensitive marker in evidence manifest/report.

## Parent Verification

Commands run:

- `git -C test-frame status --short --branch`
- `git -C test-frame rev-parse HEAD`
- `Get-FileHash test-frame\reports\evidence-zotero-metadata-adapter-evidence-consumption-a1.zip -Algorithm SHA256`
- `python -m pytest tests\test_zotero_web_api_metadata_only_contract.py tests\test_zotero_metadata_adapter_evidence_consumption.py -q`
- `python -m json.tool docs\test-frame\zotero-web-api-metadata-only\opencode-minimized-evidence-consumption.fixture.json`
- `git diff --check HEAD~1 HEAD`

Observed:

- submodule worktree clean at `f8bce53...`;
- evidence ZIP hash matched;
- targeted tests: `12 passed`;
- fixture JSON parse: PASS;
- submodule diff check: PASS.

## Known Gaps

- This does not rerun the opencode adapter production path.
- This does not read Zotero key or call Zotero API.
- This does not inspect raw API response.
- This does not validate PDF, attachment, full text, notes, WriteLab,
  Obsidian, RAG, browser/CDP, cloud, or MiniApp.
- This is not final governance acceptance or live readiness.

## Boundary

No read of `C:\Users\RD\key\zotero.txt`.
No Zotero Web API call.
No raw title, raw abstract, or raw item JSON persisted.
No PDF, attachment, note, full text, or `paragraph_text`.
No live WriteLab, Obsidian, RAG, browser/CDP, cloud, or MiniApp.
No final acceptance claim.
