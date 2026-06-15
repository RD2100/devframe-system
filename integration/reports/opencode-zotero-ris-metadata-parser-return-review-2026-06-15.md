# devframe-system Intake Review: opencode Zotero RIS Metadata Parser Return

Date: 2026-06-15
Scope: parent intake review of `dev-frame-opencode` RIS metadata parser slice
Runtime: not executed by parent
Parent action: no pin, no lock mutation, no gitlink update
Verdict: `OPENCODE_RIS_METADATA_PARSER_ACCEPTED_FOR_INTAKE`

## 1. Return Observed

Module:

- `dev-frame-opencode`

Branch:

- `codex/paper-audit-privacy-hard-gate`

Observed accepted head:

- `cb4997ae91daed53d6a52193011ebc6701e94a01`

Commit title:

- `Support safe RIS metadata pilot exports`

Parent verification:

- `git -C dev-frame-opencode log -1 --oneline` returned
  `cb4997a Support safe RIS metadata pilot exports`.
- `git -C dev-frame-opencode status --short --branch` showed no tracked or
  untracked dirty entries.
- Evidence ZIP exists at
  `D:\devframe-system\.agent\evidence\evidence-opencode-zotero-ris-metadata-parser-a1-cb4997a.zip`.
- Evidence ZIP SHA256 verified as
  `65E0EA75D81F697C56D8175BFB8593580AB115405EE0EBCF9B3C0F7419679BDA`.

## 2. Evidence Reviewed

Parent read:

- `D:\devframe-system\.agent\evidence\opencode-zotero-ris-metadata-parser-a1-cb4997a\EXECUTION_REPORT.md`
- `D:\devframe-system\.agent\evidence\opencode-zotero-ris-metadata-parser-a1-cb4997a\REVIEWER_INDEX.md`

Observed ZIP entries include:

- `EXECUTION_REPORT.md`
- `REVIEWER_INDEX.md`
- `commands/*.txt`
- `changed-files/changed-files.txt`
- `reports/ris-pass-report.json`
- `reports/ris-forbidden-blocked-report.json`
- `reports/ris-malformed-connection-required-report.json`
- `reports/input-ris-pass.ris`
- `reports/input-ris-forbidden.ris`
- `reports/input-ris-malformed.ris`
- `docs/PAPER_REAL_ZOTERO_METADATA_ONLY_PILOT.md`
- `schemas/paper_real_zotero_metadata_only_pilot_report.schema.json`

## 3. Accepted Local/Offline Scope

Accepted for parent intake:

- dependency-free local RIS metadata parser;
- strict `TY`/`ER` RIS record boundary handling;
- safe RIS metadata-only pass report;
- forbidden RIS fields fail-closed before report/evidence promotion;
- malformed/empty RIS returns `ZOTERO_METADATA_CONNECTION_REQUIRED`;
- JSON schema now recognizes `connection.metadata_format_detected = ris`;
- RDF/XML remains unsupported.

This is local/offline metadata export support. It is not live Zotero readiness
and not final governance acceptance.

## 4. Returned Verification

Returned verification summary:

- `tests\test_paper_real_zotero_metadata_only_pilot.py -q`: 18 passed.
- `tests/test_paper_real_pilot_*.py -q`: 36 passed.
- `tests\test_paper_business_capability_validation.py -q`: 7 passed.
- schema JSON parse: pass.
- compileall adapter + CLI: pass.
- `git diff --check HEAD~1 HEAD`: pass with CRLF warnings only.

Parent verified HEAD, clean worktree, ZIP existence, ZIP hash, and evidence
report presence.

## 5. Boundary Confirmation

The evidence explicitly preserves these boundaries:

- no plugin install;
- no real Zotero API;
- no Zotero storage discovery;
- no real Zotero export consumed;
- no Obsidian/private RAG/PDF/full text/WriteLab/browser/CDP/cloud access;
- no live runtime;
- no final acceptance claim;
- RDF/XML remains unsupported.

## 6. Parent Decision

Parent intake decision:

- Accept `cb4997ae91daed53d6a52193011ebc6701e94a01` as current
  `dev-frame-opencode` local/offline metadata parser candidate for pin review.
- Do not update the parent gitlink now.
- Do not update `integration/lock/submodules.lock.yml` now.
- Do not start real Zotero or other live resources.
- Do not claim final acceptance.

Reason:

- Parent pin mutation needs explicit coordinator/human approval.
- The project still needs a final grouped pin decision across active modules.

## 7. Review Focus

If the coordinator chooses to pin `dev-frame-opencode`, review:

- RIS parser does not read attachments, abstracts, notes, or paths.
- RIS forbidden tags are conservative enough: `AB`, `N1`, `N2`, `NT`, `L1`,
  `L4`.
- malformed RIS is connection-required rather than pass.
- evidence reports use metadata-only redaction.
