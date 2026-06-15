# Test-Frame Opencode A37-A38 Business Closeout Consumption Parent Intake

Date: 2026-06-16
Parent repo: `D:\devframe-system`
Submodule: `test-frame`
TaskSpec: `TESTFRAME_OPENCODE_A37_A38_BUSINESS_CLOSEOUT_CONSUMPTION_A1`
Status: `READY_FOR_PARENT_INTAKE`

## Decision

Parent intake accepts `test-frame` commit
`36c363d87813cb19ee4e8117d47d78537b26911b` as synthetic/offline verification
evidence that consumes parent-pinned opencode A37-A38 business closeout
minimized evidence.

This is not parent-pinned yet. It is verification evidence only, not final
governance acceptance, not live readiness, and not production readiness.

## Evidence

Evidence ZIP:

`D:\devframe-system\test-frame\reports\evidence-opencode-a37-a38-business-closeout-consumption-a1.zip`

Observed SHA256:

`CA124E60DA29D79334787C7506CC452B9A50301277B726DF4EF1FC5892621B8C`

Generated artifacts:

- `D:\devframe-system\test-frame\reports\opencode-a37-a38-business-closeout-consumption-a1\EXECUTION_REPORT.md`
- `D:\devframe-system\test-frame\reports\opencode-a37-a38-business-closeout-consumption-a1\REVIEWER_INDEX.md`
- `D:\devframe-system\test-frame\reports\opencode-a37-a38-business-closeout-consumption-a1\STATUS_SUMMARY.md`
- `D:\devframe-system\test-frame\reports\opencode-a37-a38-business-closeout-consumption-a1\manifests\evidence-manifest.json`

## Implementation Summary

Changed files in submodule commit:

- `docs/test-frame/paper-pipeline-metadata-only/README.md`
- `docs/test-frame/paper-pipeline-metadata-only/opencode-a37-a38-business-closeout-consumption.fixture.json`
- `tests/test_opencode_a37_a38_business_closeout_consumption.py`

Coverage:

- consumes parent-pinned opencode commit
  `9574c71c011bc975575b9d5d301965adb3e21284`;
- checks parent pin commit
  `ac513772d417fb702c22ea51205b9e16b4f0e80c`;
- verifies business validation binds `zotero_web_api_metadata_manifest`;
- verifies seven schema-locked closeout slices;
- fails closed on package hash/entry mismatch, provenance mismatch, missing
  binding, failed slices, raw/sensitive markers, final/live/production
  overclaims, and parent-pin request.

## Parent Verification

Commands run:

- `git -C test-frame status --short --branch`
- `git -C test-frame show --stat --oneline --no-renames HEAD`
- `Get-FileHash test-frame\reports\evidence-opencode-a37-a38-business-closeout-consumption-a1.zip -Algorithm SHA256`
- from `test-frame`:
  `python -m pytest tests\test_opencode_a37_a38_business_closeout_consumption.py -q`
- from `test-frame`:
  `python -m json.tool docs\test-frame\paper-pipeline-metadata-only\opencode-a37-a38-business-closeout-consumption.fixture.json`
- from `test-frame`:
  `python -m pytest tests\test_zotero_web_api_metadata_only_contract.py tests\test_zotero_metadata_adapter_evidence_consumption.py tests\test_zotero_metadata_hardening_consumption.py tests\test_zotero_metadata_manifest_consumption.py tests\test_paper_pipeline_metadata_only_orchestration.py tests\test_opencode_a37_a38_business_closeout_consumption.py -q`
- from parent repo:
  `git -C test-frame diff --check 878fe5e18e009ddcc5af308af00bb07ac31f2a57..36c363d87813cb19ee4e8117d47d78537b26911b`

Observed:

- submodule worktree clean at `36c363d...`;
- evidence ZIP hash observed as
  `CA124E60DA29D79334787C7506CC452B9A50301277B726DF4EF1FC5892621B8C`;
- focused parent tests: `8 passed`;
- parent Zotero metadata + paper pipeline consumption suite: `45 passed`;
- executor evidence reports expanded evidence-pack suite: `70 passed`;
- fixture JSON parse: PASS;
- submodule diff check from `878fe5e...` to `36c363d...`: PASS.

## Pin Readiness

Verdict: `ACCEPT_FOR_PARENT_INTAKE_WAIT_FOR_PARENT_PIN_COMMAND`

Reason:

- clean committed submodule head;
- complete ExecutionReport, Reviewer Index, Status Summary, evidence manifest,
  and evidence ZIP;
- evidence ZIP hash observed;
- focused and broader parent verification passed;
- fixture consumes only parent-pinned opencode A37-A38 evidence, not unpinned
  opencode drift.

Do not update the parent `test-frame` gitlink unless the coordinator explicitly
requests a parent pin.

## Boundary

No read of `C:\Users\RD\key\zotero.txt`.
No Zotero Web API call.
No raw API response, title, abstract, item JSON, API key, or raw user id read.
No PDF, attachments, notes, full text, or real `paragraph_text`.
No WriteLab, Obsidian, RAG, browser/CDP, cloud, or MiniApp.
No final acceptance/live-ready/production-ready/paper-quality claim.
