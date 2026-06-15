# devframe-system Return Review: dev-frame-opencode Zotero Metadata Export Hardening

Date: 2026-06-15
Scope: parent intake review for `dev-frame-opencode`
Runtime: local/offline verification only
Verdict: `OPENCODE_METADATA_EXPORT_HARDENING_RETURN_ACCEPTED_FOR_INTAKE`

## 1. Return Summary

| Field | Value |
|---|---|
| Module | `dev-frame-opencode` |
| Branch | `codex/paper-audit-privacy-hard-gate` |
| Commit | `9d4c2f62c636d91641c5843c43eaa896fbba5243` |
| Return status | `PASS_LOCAL_OFFLINE / PARENT_PIN_REVIEW_READY` |
| Submodule dirty state | clean |
| Parent pin decision | not updated by this review |

## 2. Parent Verification Performed

The parent verified:

- `dev-frame-opencode` HEAD is
  `9d4c2f62c636d91641c5843c43eaa896fbba5243`.
- `dev-frame-opencode` worktree is clean.
- `git show --stat` reports commit
  `Harden Zotero metadata export pilot parsing`.
- The evidence ZIP exists:
  `D:\devframe-system\.agent\evidence\evidence-opencode-zotero-metadata-export-hardening-a1-9d4c2f6.zip`
- The evidence directory exists:
  `D:\devframe-system\.agent\evidence\opencode-zotero-metadata-export-hardening-a1-9d4c2f6`
- `EXECUTION_REPORT.md` and `REVIEWER_INDEX.md` exist in that evidence
  directory.

## 3. Accepted Intake Facts

Accepted for parent intake:

- `connection.metadata_format_detected` is now machine-readable.
- Metadata-only JSON variants are supported for local export-file processing:
  - Zotero API-style JSON;
  - Better BibTeX JSON;
  - CSL JSON;
  - generic metadata JSON.
- BibTeX and RDF/XML are detected but fail closed as
  `ZOTERO_METADATA_CONNECTION_REQUIRED`.
- Private/sensitive fields such as storage paths, attachment paths, URI, notes,
  annotations, abstracts, full text, and WriteLab-related fields are blocked
  before report summary or evidence output.
- Documentation now records supported JSON and unsupported BibTeX/RDF behavior.

## 4. Verification From Return

The child return reports:

- `tests\test_paper_real_zotero_metadata_only_pilot.py -q` -> 13 passed.
- `tests/test_paper_real_pilot_*.py -q` -> 36 passed.
- `tests\test_paper_business_capability_validation.py -q` -> 7 passed.
- schema JSON parse -> pass.
- compileall adapter + CLI -> pass.
- `git diff --check HEAD~1 HEAD` -> pass with CRLF warnings only.

## 5. Boundary Confirmation

The return confirms:

- no plugin install;
- no real Zotero API access;
- no Zotero storage scan;
- no real Zotero export consumed;
- no Obsidian, private RAG, PDF/full text, WriteLab, browser/CDP, cloud, or live
  runtime;
- no final readiness claim.

## 6. Known Gaps

- A real metadata-only Zotero export still requires a user-provided
  `ZOTERO_METADATA_EXPORT_PATH`.
- BibTeX/RDF parser support is not implemented; it is intentionally blocked.
- This is local/offline hardening only, not live resource readiness.
- Parent pin still requires explicit coordinator approval.

## 7. Parent Intake Decision

The return is accepted for intake.

This makes `dev-frame-opencode` a cleaner pin-review candidate than before,
because the tracked dirty files are now committed and the submodule worktree is
clean.

This does not authorize parent pin mutation.
