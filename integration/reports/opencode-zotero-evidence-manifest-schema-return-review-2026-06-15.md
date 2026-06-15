# devframe-system Intake Review: opencode Evidence Manifest Schema Return

Date: 2026-06-15
Scope: parent intake review of `dev-frame-opencode` schema-gated evidence
manifest contract slice
Runtime: not executed by parent
Parent action: no real runtime, no final acceptance claim
Verdict: `OPENCODE_EVIDENCE_MANIFEST_SCHEMA_ACCEPTED_FOR_INTAKE`

## 1. Return Observed

Module:

- `dev-frame-opencode`

Branch:

- `codex/paper-audit-privacy-hard-gate`

Observed accepted head:

- `f9d381c0f8e974f1dd36642e1e412dfb2581ad5a`

Commit title:

- `Tighten Zotero pilot evidence manifest schema`

Parent verification:

- `git -C dev-frame-opencode log -5 --oneline` showed `f9d381c` above the
  previously pinned `a2cedaa`.
- `git -C dev-frame-opencode status --short --branch` showed a clean
  submodule worktree during intake.
- Evidence ZIP exists at
  `D:\devframe-system\.agent\evidence\evidence-opencode-zotero-evidence-manifest-schema-a1-f9d381c.zip`.
- Evidence ZIP SHA256 verified as
  `0CECF1C0456E29E6665F5B0273AC98D6B0C2EC67056C8D883A6AFD0C716E3529`.

## 2. Evidence Reviewed

Parent read:

- `D:\devframe-system\.agent\evidence\opencode-zotero-evidence-manifest-schema-a1-f9d381c\EXECUTION_REPORT.md`
- `D:\devframe-system\.agent\evidence\opencode-zotero-evidence-manifest-schema-a1-f9d381c\REVIEWER_INDEX.md`

Observed ZIP entries include:

- `EXECUTION_REPORT.md`
- `REVIEWER_INDEX.md`
- `commands/*.txt`
- `changed-files/changed-files.txt`
- `docs/PAPER_REAL_ZOTERO_METADATA_ONLY_PILOT.md`
- `schemas/paper_real_zotero_metadata_only_pilot_report.schema.json`
- `tests/test_paper_real_zotero_metadata_only_pilot.py`

## 3. Accepted Local/Offline Scope

Accepted for parent intake:

- `PASS_METADATA_ONLY` reports must include `metadata_summary`;
- `PASS_METADATA_ONLY` reports must include structured `evidence_manifest`;
- schema requires manifest boundary fields, including
  `metadata_format_detected`, `scope_limits`, `raw_sensitive_fields_absent`,
  `contains_real_private_content=false`,
  `contains_live_writelab_payload=false`,
  `final_acceptance_claimed=false`, and `reviewer_required=true`;
- negative schema tests cover missing manifest fields and
  `final_acceptance_claimed=true`.

This is local/offline schema and test hardening. It is not real Zotero
readiness, not private-library ingestion approval, and not final governance
acceptance.

## 4. Returned Verification

Returned verification summary:

- `tests\test_paper_real_zotero_metadata_only_pilot.py -q`: 26 passed.
- `tests/test_paper_real_pilot_*.py -q`: 36 passed.
- `tests\test_paper_business_capability_validation.py -q`: 7 passed.
- schema JSON parse: pass.
- `git diff --check HEAD~1 HEAD`: pass with CRLF warnings only.

Parent verified HEAD, clean worktree, ZIP existence, ZIP hash, evidence report
presence, and explicit non-live boundary claims.

## 5. Boundary Confirmation

The evidence explicitly preserves these boundaries:

- no plugin install;
- no real Zotero API;
- no Zotero storage discovery;
- no real Zotero export consumed;
- no Obsidian/private RAG/PDF/full text/WriteLab/browser/CDP/cloud access;
- no MiniApp runtime;
- no live runtime;
- no final acceptance claim.

## 6. Parent Decision

Parent intake decision:

- Accept `f9d381c0f8e974f1dd36642e1e412dfb2581ad5a` as the current
  `dev-frame-opencode` local/offline metadata-only pilot candidate for pin
  review.
- Treat `a2cedaa...` as superseded for opencode pin choice.
- Do not start real Zotero or other live resources.
- Do not claim final acceptance.

Reason:

- The slice moves manifest boundary checks from documentation-only to a schema
  gate, reducing fake-green risk in future PASS reports.

## 7. Review Focus

If the coordinator chooses to pin `dev-frame-opencode`, review:

- malformed PASS reports missing manifest boundary fields fail schema
  validation;
- `final_acceptance_claimed=true` cannot be schema-valid in
  `EvidenceManifest`;
- semantic equality between top-level and manifest fields remains covered by
  pytest, as noted by the submodule.
