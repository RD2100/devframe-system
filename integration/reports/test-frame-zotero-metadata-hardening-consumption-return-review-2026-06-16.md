# test-frame Zotero Metadata Hardening Consumption Parent Intake

Date: 2026-06-16
Parent repo: `D:\devframe-system`
Submodule: `test-frame`
TaskSpec: `TESTFRAME_ZOTERO_WEB_API_METADATA_HARDENING_CONSUMPTION_A1`
Status: `READY_FOR_PARENT_INTAKE`

## Decision

Parent intake accepts `test-frame` commit
`fc22a3ba891b342e24d384888b2b707d66f3c81a` as the test-frame-side
consumption validation layer for parent-pinned `dev-frame-opencode` A31-A34
Zotero Web API metadata-only hardening evidence.

This is verification evidence only. It is not final governance acceptance, not
live readiness, and not production readiness.

## Source Evidence

Source opencode commit:

`b097217c9ad3b53d4c28a03a7fb1510d2606bf71`

Source parent pin:

`8fa38bc88e68bbecec359adbafdd913d1a4c2cab`

Consumed only minimized evidence shapes from the parent-accepted batch:

- pagination/page-limit ZIP hashes;
- consumed entry names;
- metadata counts;
- pagination booleans;
- minimized failure summary categories.

## test-frame Evidence

Evidence ZIP:

`D:\devframe-system\test-frame\reports\evidence-zotero-metadata-hardening-consumption-a1.zip`

Expected SHA256:

`305751BDF00E48D6797E0312DF2F4E4C12CCDB8ECC52FCDE895FED9EB2514C7E`

Observed SHA256:

`305751BDF00E48D6797E0312DF2F4E4C12CCDB8ECC52FCDE895FED9EB2514C7E`

Generated artifacts:

- `D:\devframe-system\test-frame\reports\zotero-metadata-hardening-consumption-a1\EXECUTION_REPORT.md`
- `D:\devframe-system\test-frame\reports\zotero-metadata-hardening-consumption-a1\REVIEWER_INDEX.md`
- `D:\devframe-system\test-frame\reports\zotero-metadata-hardening-consumption-a1\STATUS_SUMMARY.md`
- `D:\devframe-system\test-frame\reports\zotero-metadata-hardening-consumption-a1\manifests\evidence-manifest.json`

## Implementation Summary

Changed files in submodule commit:

- `docs/test-frame/zotero-web-api-metadata-only/README.md`
- `docs/test-frame/zotero-web-api-metadata-only/opencode-metadata-hardening-consumption.fixture.json`
- `tests/test_zotero_metadata_hardening_consumption.py`

Implemented behavior:

- added a minimized hardening consumption fixture for A31-A34 fields:
  `metadata_page_limit`, `metadata_pages_read`,
  `metadata_pagination_complete`, `metadata_api_calls`,
  `over_limit_condition`, `pilot_status`, `metadata_records_read`,
  `item_type_counts`, raw/forbidden resource flags, final/live claim flags, and
  minimized failure summary examples;
- positive pagination/page-limit `PASS_METADATA_ONLY` evidence can be consumed
  as test-frame verification evidence only;
- fail-closed cases cover pages read above limit, incomplete pagination with
  PASS, over-limit with PASS, records=0 with PASS, non-minimized failure
  summary, response body/traceback/raw URL with secret/token-like/low-level
  exception leakage, final/live overclaims, raw persistence flags,
  notes/attachments/pdf/full-text flags, and forbidden note/attachment counts.

## Parent Verification

Commands run:

- `git -C test-frame status --short --branch`
- `git -C test-frame rev-parse HEAD`
- `Get-FileHash test-frame\reports\evidence-zotero-metadata-hardening-consumption-a1.zip -Algorithm SHA256`
- `python -m pytest tests\test_zotero_metadata_hardening_consumption.py -q`
- `python -m json.tool docs\test-frame\zotero-web-api-metadata-only\opencode-metadata-hardening-consumption.fixture.json`
- `git diff --check HEAD~1 HEAD`

Observed:

- submodule worktree clean at `fc22a3b...`;
- evidence ZIP hash matched;
- targeted tests: `7 passed`;
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
No raw API response read.
No raw title, raw abstract, raw item JSON, API key, or raw user id persisted.
No PDF, attachment, note, full text, or `paragraph_text`.
No live WriteLab, Obsidian, RAG, browser/CDP, cloud, or MiniApp.
No final acceptance/live-ready/production-ready claim.
