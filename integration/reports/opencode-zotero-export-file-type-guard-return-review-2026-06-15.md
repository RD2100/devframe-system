# devframe-system Intake Review: opencode Zotero Export File Type Guard Return

Date: 2026-06-15
Scope: parent intake review of `dev-frame-opencode` metadata-only export file
type and encoding guard slice
Runtime: not executed by parent
Parent action: no pin, no lock mutation, no gitlink update
Verdict: `OPENCODE_EXPORT_FILE_TYPE_GUARD_ACCEPTED_FOR_INTAKE`

## 1. Return Observed

Module:

- `dev-frame-opencode`

Branch:

- `codex/paper-audit-privacy-hard-gate`

Observed accepted head:

- `3a722134ca5f693f93796a6e63bc573109d2e48f`

Commit title:

- `Block non-metadata Zotero pilot exports`

Parent verification:

- `git -C dev-frame-opencode log -5 --oneline` showed `3a72213` above
  previously reviewed `6bd9809`.
- `git -C dev-frame-opencode status --short --branch` showed no tracked or
  untracked dirty entries.
- Evidence ZIP exists at
  `D:\devframe-system\.agent\evidence\evidence-opencode-zotero-export-file-type-guard-a1-3a72213.zip`.
- Evidence ZIP SHA256 verified as
  `2F252C3C3216DEEC0EF46063D9C6B5C64449E687215139B73C0909E2E9220D1A`.

## 2. Evidence Reviewed

Parent read:

- `D:\devframe-system\.agent\evidence\opencode-zotero-export-file-type-guard-a1-3a72213\EXECUTION_REPORT.md`
- `D:\devframe-system\.agent\evidence\opencode-zotero-export-file-type-guard-a1-3a72213\REVIEWER_INDEX.md`
- `D:\devframe-system\.agent\evidence\opencode-zotero-export-file-type-guard-a1-3a72213\reports\pdf-file-type-blocked-report.json`
- `D:\devframe-system\.agent\evidence\opencode-zotero-export-file-type-guard-a1-3a72213\reports\sqlite-file-type-blocked-report.json`
- `D:\devframe-system\.agent\evidence\opencode-zotero-export-file-type-guard-a1-3a72213\reports\non-utf8-connection-required-report.json`

Observed ZIP entries include:

- `EXECUTION_REPORT.md`
- `REVIEWER_INDEX.md`
- `commands/*.txt`
- `changed-files/changed-files.txt`
- `reports/pdf-file-type-blocked-report.json`
- `reports/sqlite-file-type-blocked-report.json`
- `reports/non-utf8-connection-required-report.json`
- `reports/synthetic-authorization-decision.json`
- `docs/PAPER_REAL_ZOTERO_METADATA_ONLY_PILOT.md`

## 3. Accepted Local/Offline Scope

Accepted for parent intake:

- obvious non-metadata file suffixes are blocked before content decode;
- `.pdf` and `.sqlite` synthetic inputs return `pilot_status: BLOCKED`;
- non-UTF-8 candidate metadata input returns
  `pilot_status: ZOTERO_METADATA_CONNECTION_REQUIRED`;
- no synthetic report claims final acceptance;
- privacy flags remain false for attachments, PDFs, full text, Obsidian,
  private RAG, and live WriteLab.

This is local/offline entrypoint hardening. It is not real Zotero readiness,
not private-library ingestion approval, and not final governance acceptance.

## 4. Returned Verification

Returned verification summary:

- `tests\test_paper_real_zotero_metadata_only_pilot.py -q`: 23 passed.
- `tests/test_paper_real_pilot_*.py -q`: 36 passed.
- `tests\test_paper_business_capability_validation.py -q`: 7 passed.
- schema JSON parse: pass.
- compileall adapter and CLI: pass.
- `git diff --check HEAD~1 HEAD`: pass with CRLF warnings only.

Parent verified HEAD, clean worktree, ZIP existence, ZIP hash, evidence report
presence, and the synthetic report statuses above.

## 5. Boundary Confirmation

The evidence explicitly preserves these boundaries:

- no plugin install;
- no real Zotero API;
- no Zotero storage discovery;
- no real Zotero export consumed;
- no Obsidian/private RAG/PDF/full text/WriteLab/browser/CDP/cloud access;
- no live runtime;
- no final acceptance claim.

## 6. Parent Decision

Parent intake decision:

- Accept `3a722134ca5f693f93796a6e63bc573109d2e48f` as the current
  `dev-frame-opencode` local/offline metadata-only pilot candidate for pin
  review.
- Treat `parent-pin-review-a7-2026-06-15.md` as superseded for opencode pin
  choice because it referenced `6bd9809...`.
- Do not start real Zotero or other live resources.
- Do not claim final acceptance.

Reason:

- The slice closes a practical pre-runtime safety gap: accidental PDF,
  database, Office/archive, or non-UTF-8 input should not be treated as a
  metadata export success.
- Parent pin mutation still needs a current grouped review across all modules.

## 7. Review Focus

If the coordinator chooses to pin `dev-frame-opencode`, review:

- blocked suffix list is conservative enough for the first metadata-only pilot;
- suffix gate runs before content decode;
- non-UTF-8 input is connection-required rather than pass or crash;
- no private content, attachments, PDFs, notes, database content, or paths are
  emitted.
