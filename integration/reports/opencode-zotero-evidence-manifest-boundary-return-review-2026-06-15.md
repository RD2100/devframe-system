# devframe-system Intake Review: opencode Evidence Manifest Boundary Return

Date: 2026-06-15
Scope: parent intake review of `dev-frame-opencode` Zotero metadata-only
evidence manifest boundary slice
Runtime: not executed by parent
Parent action: no pin in this report, no lock mutation in this report
Verdict: `OPENCODE_EVIDENCE_MANIFEST_BOUNDARY_ACCEPTED_FOR_INTAKE`

## 1. Return Observed

Module:

- `dev-frame-opencode`

Branch:

- `codex/paper-audit-privacy-hard-gate`

Observed accepted head:

- `a2cedaa280f12f717d4bf0a64c1c12ece6f5fefe`

Commit title:

- `Mirror Zotero pilot boundaries in evidence manifest`

Parent verification:

- `git -C dev-frame-opencode log -1 --oneline` returned
  `a2cedaa Mirror Zotero pilot boundaries in evidence manifest`.
- `git -C dev-frame-opencode status --short --branch` showed no tracked or
  untracked dirty entries at intake time.
- Evidence ZIP exists at
  `D:\devframe-system\.agent\evidence\evidence-opencode-zotero-evidence-manifest-boundary-a1-a2cedaa.zip`.
- Evidence ZIP SHA256 verified as
  `D7D03A5EED7F52E69231BF4B40C6DBD75DA63B72D28733675F8AC989047103B8`.

## 2. Evidence Reviewed

Parent read:

- `D:\devframe-system\.agent\evidence\opencode-zotero-evidence-manifest-boundary-a1-a2cedaa\EXECUTION_REPORT.md`
- `D:\devframe-system\.agent\evidence\opencode-zotero-evidence-manifest-boundary-a1-a2cedaa\REVIEWER_INDEX.md`
- `D:\devframe-system\.agent\evidence\opencode-zotero-evidence-manifest-boundary-a1-a2cedaa\reports\manifest-boundary-report.json`

Observed ZIP entries include:

- `EXECUTION_REPORT.md`
- `REVIEWER_INDEX.md`
- `commands/*.txt`
- `changed-files/changed-files.txt`
- `reports/manifest-boundary-report.json`
- `reports/authorization-decision.synthetic.json`
- `reports/zotero-export.synthetic.json`
- `docs/PAPER_REAL_ZOTERO_METADATA_ONLY_PILOT.md`
- `schemas/paper_real_zotero_metadata_only_pilot_report.schema.json`

## 3. Accepted Local/Offline Scope

Accepted for parent intake:

- `evidence_manifest.metadata_format_detected` mirrors
  `connection.metadata_format_detected`;
- `evidence_manifest.scope_limits` mirrors top-level `scope_limits`;
- `evidence_manifest.final_acceptance_claimed` is `false`;
- manifest report remains metadata-only and synthetic/local;
- privacy flags remain false for attachments, PDFs, full text, Obsidian,
  private RAG, and live WriteLab.

This is local/offline reviewer-evidence hardening. It is not real Zotero
readiness, not private-library ingestion approval, and not final governance
acceptance.

## 4. Returned Verification

Returned verification summary:

- `tests\test_paper_real_zotero_metadata_only_pilot.py -q`: 25 passed.
- `tests/test_paper_real_pilot_*.py -q`: 36 passed.
- `tests\test_paper_business_capability_validation.py -q`: 7 passed.
- schema JSON parse from repo root: pass.
- compileall adapter and CLI: pass.
- `git diff --check HEAD~1 HEAD`: pass with CRLF warnings only.
- synthetic manifest boundary report generation: pass and schema validated.

Parent verified HEAD, clean worktree, ZIP existence, ZIP hash, evidence report
presence, and manifest boundary fields.

Note:

- The evidence package records an initial schema command path mistake against
  `ai-workflow-hub/schemas/...`; the corrected root schema command passed.
  This is a reviewer-command cwd issue, not a product/runtime failure.

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

- Accept `a2cedaa280f12f717d4bf0a64c1c12ece6f5fefe` as the current
  `dev-frame-opencode` local/offline metadata-only pilot candidate for pin
  review.
- Treat `parent-pin-review-a9-2026-06-15.md` as superseded for opencode pin
  choice because it referenced `58b79e2...`.
- Do not start real Zotero or other live resources.
- Do not claim final acceptance.

Reason:

- The slice improves reviewer-side evidence visibility without expanding
  runtime access or exposing raw content.
- Parent pin mutation still needs a current grouped review across all modules.

## 7. Review Focus

If the coordinator chooses to pin `dev-frame-opencode`, review:

- manifest boundary fields match top-level report fields;
- `final_acceptance_claimed=false` is visible in manifest and top-level report;
- the synthetic report contains no private source content;
- path failure in `schema-json-tool.txt` is superseded by
  `schema-json-tool-root.txt`.
