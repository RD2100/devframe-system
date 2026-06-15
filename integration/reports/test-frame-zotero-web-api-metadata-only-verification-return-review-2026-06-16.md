# test-frame Zotero Web API Metadata-Only Verification Parent Intake

Date: 2026-06-16
Parent repo: `D:\devframe-system`
Submodule: `test-frame`
TaskSpec: `TESTFRAME_ZOTERO_WEB_API_METADATA_ONLY_VERIFICATION_A1`
Status: `READY_FOR_PARENT_INTAKE`

## Decision

Parent intake accepts `test-frame` commit
`b1925fc39d5393402fee0fcc664edbc83eaf3a27` as the verification-contract
counterpart for Zotero Web API metadata-only adapter intake.

This is verification evidence only. It is not final governance acceptance, not
paper quality verdict, and not live Zotero/full-paper readiness.

## Evidence

Evidence ZIP:

`D:\devframe-system\test-frame\reports\evidence-zotero-web-api-metadata-only-verification-a1.zip`

Expected SHA256:

`190108814D40F41DB90A51934C6F37514C5221BC821451540EE3EC3FE603DA43`

Observed SHA256:

`190108814D40F41DB90A51934C6F37514C5221BC821451540EE3EC3FE603DA43`

## Scope

Accepted scope:

- synthetic/offline verification contracts;
- negative canaries for Zotero Web API metadata-only evidence;
- TestRunSpec/TestExecutionReport examples;
- fail-closed reviewer detection input.

Explicitly not in scope:

- reading `C:\Users\RD\key\zotero.txt`;
- calling Zotero Web API;
- reading notes, attachments, PDF, full text, or real `paragraph_text`;
- live WriteLab, Obsidian, RAG, browser/CDP, cloud, or MiniApp;
- final acceptance or paper-quality verdict.

## Implementation Summary

Changed files in submodule commit:

- `docs/agent-runtime/negative-acceptance-tests.md`
- `docs/agent-runtime/negative-test-fixtures/README.md`
- `docs/agent-runtime/negative-test-fixtures/NEG-ZOTERO-WEB-API-001-empty-remote-library-reported-pass.json`
- `docs/agent-runtime/negative-test-fixtures/NEG-ZOTERO-WEB-API-002-note-attachment-read-reported-pass.json`
- `docs/agent-runtime/negative-test-fixtures/NEG-ZOTERO-WEB-API-003-forbidden-resource-flags-pass.json`
- `docs/agent-runtime/negative-test-fixtures/NEG-ZOTERO-WEB-API-004-raw-sensitive-evidence-leak.json`
- `docs/agent-runtime/negative-test-fixtures/NEG-ZOTERO-WEB-API-005-preflight-promoted-final-acceptance.json`
- `docs/agent-runtime/negative-test-fixtures/NEG-ZOTERO-WEB-API-006-test-frame-pass-final-governance.json`
- `docs/test-frame/zotero-web-api-metadata-only/README.md`
- `docs/test-frame/zotero-web-api-metadata-only/test-run-spec.synthetic.json`
- `docs/test-frame/zotero-web-api-metadata-only/test-execution-report.pass-metadata-only.synthetic.json`
- `tests/test_paper_negative_fixtures.py`
- `tests/test_zotero_web_api_metadata_only_contract.py`

Added coverage:

- empty remote library reported as PASS;
- note/attachment reads reported as metadata-only PASS;
- PDF/full-text/notes flags true while report claims PASS;
- raw sensitive evidence leak;
- metadata-only preflight promoted to final acceptance/live-ready;
- test-frame PASS promoted to final governance acceptance.

## Parent Verification

Commands run:

- `git -C test-frame status --short --branch`
- `git -C test-frame rev-parse HEAD`
- `Get-FileHash test-frame\reports\evidence-zotero-web-api-metadata-only-verification-a1.zip -Algorithm SHA256`
- `python -m pytest tests\test_paper_negative_fixtures.py tests\test_evidence_pack_manifest.py tests\test_evidence_collector.py tests\test_zotero_web_api_metadata_only_contract.py -q`
- `git diff --check HEAD~1 HEAD`

Observed:

- submodule worktree clean at `b1925fc...`;
- evidence ZIP hash matched;
- targeted tests: `32 passed`;
- submodule diff check: PASS.

## Known Gaps

- The dev-frame-opencode adapter production path was not exercised by
  test-frame in this slice.
- No live Zotero API/key/PDF/notes/full-text/WriteLab/browser/cloud/MiniApp was
  used.
- This prepares verification governance; it does not make the project final
  accepted.

## Reviewer Index

Critical review paths:

- new `NEG-ZOTERO-WEB-API-*` fixtures;
- `tests/test_zotero_web_api_metadata_only_contract.py`;
- synthetic TestRunSpec/TestExecutionReport examples.

Review focus:

- metadata-only PASS must not hide empty remote library, forbidden resources,
  raw sensitive evidence, or final-acceptance overclaims;
- test-frame pass must remain verification evidence only, not final governance
  acceptance.
