# devframe-system Intake Review: opencode Empty Metadata Fail-Closed Return

Date: 2026-06-15
Scope: parent intake review of `dev-frame-opencode` empty or unrecognized
metadata export fail-closed slice
Runtime: not executed by parent
Parent action: no pin, no lock mutation, no gitlink update
Verdict: `OPENCODE_EMPTY_METADATA_FAILCLOSED_ACCEPTED_FOR_INTAKE`

## 1. Return Observed

Module:

- `dev-frame-opencode`

Branch:

- `codex/paper-audit-privacy-hard-gate`

Observed accepted head:

- `58b79e292bcf3ab4dbf66cb656f9827093f48dd0`

Commit title:

- `Fail closed on empty Zotero metadata exports`

Parent verification:

- `git -C dev-frame-opencode log -1 --oneline` returned
  `58b79e2 Fail closed on empty Zotero metadata exports`.
- `git -C dev-frame-opencode status --short --branch` showed no tracked or
  untracked dirty entries at intake time.
- Evidence ZIP exists at
  `D:\devframe-system\.agent\evidence\evidence-opencode-zotero-empty-metadata-failclosed-a1-58b79e2.zip`.
- Evidence ZIP SHA256 verified as
  `EA4AF3DB063A20BC9ED92CF1C93297FB1A76E43D11945E3A5823F83C23F7909A`.

## 2. Evidence Reviewed

Parent read:

- `D:\devframe-system\.agent\evidence\opencode-zotero-empty-metadata-failclosed-a1-58b79e2\EXECUTION_REPORT.md`
- `D:\devframe-system\.agent\evidence\opencode-zotero-empty-metadata-failclosed-a1-58b79e2\REVIEWER_INDEX.md`
- `D:\devframe-system\.agent\evidence\opencode-zotero-empty-metadata-failclosed-a1-58b79e2\reports\unrecognized-json-connection-required-report.json`
- `D:\devframe-system\.agent\evidence\opencode-zotero-empty-metadata-failclosed-a1-58b79e2\reports\empty-json-connection-required-report.json`

Observed ZIP entries include:

- `EXECUTION_REPORT.md`
- `REVIEWER_INDEX.md`
- `commands/*.txt`
- `changed-files/changed-files.txt`
- `reports/unrecognized-json-connection-required-report.json`
- `reports/empty-json-connection-required-report.json`
- `reports/synthetic-authorization-decision.json`
- `docs/PAPER_REAL_ZOTERO_METADATA_ONLY_PILOT.md`

## 3. Accepted Local/Offline Scope

Accepted for parent intake:

- parsed-but-unrecognized JSON metadata exports do not produce
  `PASS_METADATA_ONLY`;
- empty JSON metadata exports do not produce `PASS_METADATA_ONLY`;
- both synthetic reports return
  `pilot_status: ZOTERO_METADATA_CONNECTION_REQUIRED`;
- both reports include reason `empty_or_unrecognized_metadata_export`;
- privacy flags remain false for attachments, PDFs, full text, Obsidian,
  private RAG, and live WriteLab.

This is local/offline fake-green hardening. It is not real Zotero readiness,
not private-library ingestion approval, and not final governance acceptance.

## 4. Returned Verification

Returned verification summary:

- `tests\test_paper_real_zotero_metadata_only_pilot.py -q`: 25 passed.
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

- Accept `58b79e292bcf3ab4dbf66cb656f9827093f48dd0` as the current
  `dev-frame-opencode` local/offline metadata-only pilot candidate for pin
  review.
- Treat `parent-pin-review-a8-2026-06-15.md` as superseded for opencode pin
  choice because it referenced `3a72213...`.
- Do not start real Zotero or other live resources.
- Do not claim final acceptance.

Reason:

- The slice closes an explicit fake-green gap: empty or unrecognized metadata
  cannot be promoted as a successful metadata-only pilot.
- Parent pin mutation still needs a current grouped review across all modules.

## 7. Review Focus

If the coordinator chooses to pin `dev-frame-opencode`, review:

- empty metadata summary can never be treated as `PASS_METADATA_ONLY`;
- unrecognized metadata fields return connection-required rather than pass;
- reason code `empty_or_unrecognized_metadata_export` is specific enough for
  later reviewer and test-frame checks;
- no private content, attachments, PDFs, notes, database content, or paths are
  emitted.
