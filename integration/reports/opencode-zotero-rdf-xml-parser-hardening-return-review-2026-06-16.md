# Opencode Zotero RDF/XML Parser Hardening Return Review

Date: 2026-06-16
Reviewer: parent devframe-system coordinator
Scope: parent intake review only

## Verdict

Status: `ACCEPTED_FOR_PARENT_INTAKE_WITH_LIMITATIONS`

The `dev-frame-opencode` Zotero RDF/XML metadata-only parser hardening slice is
accepted for parent intake. This acceptance is narrow: it covers user-provided
Zotero RDF/XML metadata export handling only.

It is not a generic safe XML parser verdict, not PDF/attachment/full-text
readiness, not Obsidian/RAG/WriteLab readiness, not browser/CDP/cloud readiness,
and not final governance acceptance.

## Reviewed Slice

- Slice: `OPENCODE_ZOTERO_RDF_XML_PARSER_HARDENING_A1`
- Submodule: `D:\devframe-system\dev-frame-opencode`
- Branch: `codex/paper-audit-privacy-hard-gate`
- Commit: `6b4a3aaf3b8a6b7ee3877014ccc7b6a11f8d639d`
- Commit message: `Harden Zotero RDF metadata parser`
- Evidence ZIP:
  `D:\devframe-system\.agent\evidence\evidence-opencode-zotero-rdf-xml-parser-hardening-a1-6b4a3aa.zip`
- Evidence ZIP SHA256:
  `5528084DAF73B5D34627AAD2E31C6B6A67E0F421B2F4C8E0EE6A1EA686CEBC06`

## GPT Verdict

- Verdict: `accepted_with_limitations`
- Accepted status: `OPENCODE_ZOTERO_RDF_XML_PARSER_HARDENING_READY`
- Rework required: `false`
- Continue local metadata slice: `false`
- Main control intervention: grouped parent intake / pin required

## Verification Summary From Return

- focused tests: `46 passed`
- broader real-pilot/business/local-batch suite: `91 passed`
- schema parse: `PASS`
- real RDF smoke schema validate: `PASS`
- `git diff --check HEAD~1 HEAD`: `PASS`

## Real RDF Smoke Summary

The smoke used a user-provided export file under
`D:\devframe-system\.agent\manual-input`. The raw export file was not copied
into the evidence ZIP.

Observed result:

- `pilot_status`: `PASS_METADATA_ONLY`
- `metadata_format_detected`: `rdf`
- `item_count`: `23`
- sanitizer status: `SANITIZED_WITH_REDACTIONS`
- removed field counts: `abstract=23`, `uri=23`
- `raw_sensitive_fields_absent`: `true`
- `final_acceptance_claimed`: `false`

## Metadata Milestone Chain Scope

This intake keeps the current metadata-only chain bounded to export-file
handling:

- BibTeX metadata export sanitizer and evidence minimization are already
  accepted and pinned through A31.
- RDF/XML metadata export parser hardening is accepted here as A32.
- EvidenceManifest parity, artifact minimization, review-pack minimization,
  RuntimeAuthorization metadata-only scope, and agent-acceptance dependency
  checks remain part of the parent review boundary.

## Boundary

No Zotero app/API/library/storage access was authorized or executed.

No PDF, attachment, full-text, private note runtime, Obsidian/private RAG,
WriteLab, MiniApp, browser/CDP, or cloud runtime was authorized or executed.

Future expansion to any of those resources remains `HUMAN_REQUIRED`.

## Known Gaps

- `dev-frame-opencode` contains unrelated dirty files from the parallel
  security-fix path; those files are not part of commit `6b4a3aa`.
- The evidence report includes a full local RDF export path. GPT did not mark
  this as a rework blocker because the user supplied the path and raw RDF was
  absent, but future grouped closeout should prefer minimized fields such as
  `export_path_present`, `metadata_format_detected`,
  `source_export_size_bytes`, and `source_fingerprint`.
- This slice does not authorize the next real resource track.

## Parent Decision

Proceed to parent pin review for
`6b4a3aaf3b8a6b7ee3877014ccc7b6a11f8d639d`.
