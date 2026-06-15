# devframe-system Intake Review: opencode Zotero Metadata Scope Limits Return

Date: 2026-06-15
Scope: parent intake review of `dev-frame-opencode` metadata-only pilot scope-limit slice
Runtime: not executed by parent
Parent action: no pin, no lock mutation, no gitlink update
Verdict: `OPENCODE_METADATA_SCOPE_LIMITS_ACCEPTED_FOR_INTAKE`

## 1. Return Observed

Module:

- `dev-frame-opencode`

Branch:

- `codex/paper-audit-privacy-hard-gate`

Observed accepted head:

- `6bd9809cc635e58e066cb0b3d1f38c2534b03d7a`

Commit title:

- `Add Zotero metadata pilot scope limits`

Parent verification:

- `git -C dev-frame-opencode log -3 --oneline` showed `6bd9809` above the
  previously reviewed `cb4997a` RIS parser commit.
- `git -C dev-frame-opencode status --short --branch` showed no tracked or
  untracked dirty entries.
- Evidence ZIP exists at
  `D:\devframe-system\.agent\evidence\evidence-opencode-zotero-metadata-scope-limits-a1-6bd9809.zip`.
- Evidence ZIP SHA256 verified as
  `B0E8F8E04108634C71D010CB53914D17CD26E0E7448751D082C41CCB20D3A3CD`.

## 2. Evidence Reviewed

Parent read:

- `D:\devframe-system\.agent\evidence\opencode-zotero-metadata-scope-limits-a1-6bd9809\EXECUTION_REPORT.md`
- `D:\devframe-system\.agent\evidence\opencode-zotero-metadata-scope-limits-a1-6bd9809\REVIEWER_INDEX.md`
- `D:\devframe-system\.agent\evidence\opencode-zotero-metadata-scope-limits-a1-6bd9809\reports\scope-size-limit-blocked-report.json`
- `D:\devframe-system\.agent\evidence\opencode-zotero-metadata-scope-limits-a1-6bd9809\reports\scope-item-count-limit-blocked-report.json`

Observed ZIP entries include:

- `EXECUTION_REPORT.md`
- `REVIEWER_INDEX.md`
- `commands/*.txt`
- `changed-files/changed-files.txt`
- `reports/scope-size-limit-blocked-report.json`
- `reports/scope-item-count-limit-blocked-report.json`
- `reports/synthetic-authorization-decision.json`
- `docs/PAPER_REAL_ZOTERO_METADATA_ONLY_PILOT.md`
- `schemas/paper_real_zotero_metadata_only_pilot_report.schema.json`

## 3. Accepted Local/Offline Scope

Accepted for parent intake:

- machine-readable `scope_limits` in the metadata-only pilot report;
- fail-closed behavior before parsing oversized export files;
- fail-closed behavior after parsing when item count exceeds local pilot limit;
- conservative local defaults reported by the module: 5 MiB and 500 records;
- synthetic blocked reports for size and item-count over-limit cases.

This is local/offline pilot-scope hardening. It is not real Zotero readiness,
not private-library ingestion approval, and not final governance acceptance.

## 4. Returned Verification

Returned verification summary:

- `tests\test_paper_real_zotero_metadata_only_pilot.py -q`: 20 passed.
- `tests/test_paper_real_pilot_*.py -q`: 36 passed.
- `tests\test_paper_business_capability_validation.py -q`: 7 passed.
- schema JSON parse: pass.
- compileall adapter and CLI: pass.
- `git diff --check HEAD~1 HEAD`: pass with CRLF warnings only.

Parent verified HEAD, clean worktree, ZIP existence, ZIP hash, evidence report
presence, and both synthetic over-limit reports returning `pilot_status:
BLOCKED`.

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

- Accept `6bd9809cc635e58e066cb0b3d1f38c2534b03d7a` as the current
  `dev-frame-opencode` local/offline metadata-only pilot candidate for pin
  review.
- Treat `parent-pin-review-a6-2026-06-15.md` as superseded for opencode pin
  choice because it referenced `cb4997a...`.
- Do not start real Zotero or other live resources.
- Do not claim final acceptance.

Reason:

- The slice adds useful fail-closed scope limits.
- Parent pin mutation still needs a current grouped review across all modules.

## 7. Review Focus

If the coordinator chooses to pin `dev-frame-opencode`, review:

- oversized file is blocked before parser execution;
- too-many-items report is blocked before summary/evidence promotion;
- `scope_limits` fields are required and machine-readable;
- default pilot limits are acceptable for first metadata-only pilot;
- no private content, attachments, PDFs, notes, or paths are emitted.
