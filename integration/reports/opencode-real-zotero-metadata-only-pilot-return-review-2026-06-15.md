# Opencode Real Zotero Metadata-Only Pilot Return Review

Date: 2026-06-15
Reviewer: parent devframe-system coordinator
Scope: parent intake review only

## Verdict

Status: `ACCEPTED_FOR_PARENT_INTAKE_WITH_LIMITATIONS`

The `dev-frame-opencode` real Zotero metadata-only pilot milestone is accepted
for parent intake as a metadata-export-file pilot. It is not final acceptance,
not live paper workflow readiness, and not authorization for PDF, attachment,
full-text, Obsidian, RAG, WriteLab, browser/CDP, MiniApp, cloud, or Zotero
application/API access.

## Reviewed Milestone

- Submodule: `D:\devframe-system\dev-frame-opencode`
- Branch: `codex/paper-audit-privacy-hard-gate`
- Code baseline commit:
  `b086ca283fb71b16833acc3461e42a3e2e727456`
- Code slice:
  `OPENCODE_ZOTERO_METADATA_LOCAL_BATCH_CLOSEOUT_A1`
- GPT verdict: `accepted_with_limitations`
- GPT accepted status:
  `OPENCODE_ZOTERO_METADATA_LOCAL_BATCH_CLOSEOUT_READY`

Evidence ZIP:

- `D:\devframe-system\.agent\evidence\evidence-opencode-zotero-metadata-local-batch-closeout-a1-b086ca2.zip`
- SHA256:
  `7D8780219800C25E7C618196CD1B9DACA1C1267596E5BCFCA78589B5EB5AFF3F`

## Real Metadata-Only Pilot Run

- Slice: `PAPER_REAL_ZOTERO_METADATA_EXPORT_RUN_A1`
- Evidence ZIP:
  `D:\devframe-system\.agent\evidence\evidence-paper-real-zotero-metadata-export-run-a1-b086ca2.zip`
- SHA256:
  `632CC5CEC80D1A5116315F7764D995C91D329456BBC3E17B300D29EB29BE25FF`
- GPT verdict: `accepted_with_limitations`
- GPT accepted status: `PAPER_REAL_ZOTERO_METADATA_ONLY_PILOT_READY`

Observed pilot result:

- Input: user-provided metadata export file only.
- Raw export file was not included in the evidence ZIP.
- `pilot_status`: `PASS_METADATA_ONLY`
- `metadata_format_detected`: `bibtex`
- `item_count`: `23`
- sanitizer status: `SANITIZED_WITH_REDACTIONS`
- removed field counts: `abstract=23`, `file=2`, `note=23`
- `contains_real_private_content`: `false`
- `contains_live_writelab_payload`: `false`
- `final_acceptance_claimed`: `false`

## Pilot Closeout

- Slice: `PAPER_REAL_ZOTERO_METADATA_ONLY_PILOT_CLOSEOUT_A1`
- Evidence ZIP:
  `D:\devframe-system\.agent\evidence\evidence-paper-real-zotero-metadata-only-pilot-closeout-a1-b086ca2.zip`
- SHA256:
  `66540F9DF8DBDFE8DC5C410E444592944F18649003C9193C7A6CE99AEC4C60D7`
- GPT verdict: `accepted_with_limitations`
- GPT accepted status:
  `PAPER_REAL_ZOTERO_METADATA_ONLY_PILOT_CLOSEOUT_READY`
- GPT confirmed: `MILESTONE_READY_FOR_MAIN_CONTROL_PIN`

## Verification Summary From Return

- local batch closeout focused tests: `42 passed`
- local batch closeout real-pilot/business suite: `87 passed`
- real export run focused tests: `42 passed`
- closeout focused tests: `42 passed`
- schema/report JSON parse: `PASS`
- closeout JSON parse: `PASS`
- raw sensitive scan: `PASS` for raw BibTeX markers and full local path in
  closeout
- `git diff --check HEAD~1 HEAD`: `PASS`

Parent-side checks:

- all three evidence ZIP paths exist;
- all three SHA256 hashes match the module return;
- current `dev-frame-opencode` HEAD is
  `b086ca283fb71b16833acc3461e42a3e2e727456`.

## Boundary

No Zotero app/API/library/storage access was authorized or executed.

No PDF, attachment, full-text, Obsidian/private RAG, WriteLab, MiniApp,
browser/CDP, or cloud runtime was authorized or executed.

This milestone proves only that the metadata-export-file path can process a
user-provided BibTeX export with sanitizer redaction and produce bounded
metadata-only evidence.

Future expansion to PDF, Obsidian, RAG, WriteLab, browser/CDP, MiniApp, or
cloud requires a fresh `HUMAN_REQUIRED` authorization.

## Known Gaps

- `dev-frame-opencode` worktree contains unrelated dirty files from the
  parallel security bugfix path; those files are not part of the `b086ca2`
  milestone evidence.
- No final governance acceptance is claimed.
- This return does not authorize the next real resource track.

## Parent Decision

Proceed to parent pin review for
`b086ca283fb71b16833acc3461e42a3e2e727456`.
