# dev-frame-opencode Real Zotero Metadata Export Smoke Parent Intake

Date: 2026-06-16
Parent repo: `D:\devframe-system`
Submodule: `dev-frame-opencode`
Submodule head: `7ccbdefa4037a40c76ce137b2d16b48931701c94`
TaskSpec: `OPENCODE_REAL_ZOTERO_METADATA_EXPORT_SMOKE_A1`
Status: `GPT_ACCEPTED_WITH_LIMITATIONS`

## Decision

Parent intake accepts this as an evidence-only milestone record.

No parent gitlink update is needed because the relevant code head is already
`7ccbdefa4037a40c76ce137b2d16b48931701c94`.

This is not final acceptance and does not authorize Zotero app/API/storage,
PDF, attachments, full text, private notes, Obsidian, RAG, WriteLab,
browser/CDP, cloud, or any other real runtime.

## Evidence

Evidence ZIP:

`D:\devframe-system\.agent\evidence\evidence-opencode-real-zotero-metadata-export-smoke-a1-r2.zip`

Expected SHA256:

`8A726BFCD4CE91B871CCD5F977418CF39F32B47EB15EDE254AA11C55F2B88F45`

Observed SHA256:

`8A726BFCD4CE91B871CCD5F977418CF39F32B47EB15EDE254AA11C55F2B88F45`

Generated evidence directory:

`D:\devframe-system\.agent\evidence\opencode-real-zotero-metadata-export-smoke-a1-r2`

## Input Scope

The user authorized reading real exported metadata files under:

`D:\devframe-system\.agent\manual-input`

Parent-facing summary intentionally records inputs as anonymized slots:

| Input | Format | Items | Status | Sanitizer | Redactions |
|---|---:|---:|---|---|---|
| input_1 | BibTeX | 23 | `PASS_METADATA_ONLY` | `SANITIZED_WITH_REDACTIONS` | `abstract=23`, `file=2`, `note=23` |
| input_2 | RDF | 23 | `PASS_METADATA_ONLY` | `SANITIZED_WITH_REDACTIONS` | `abstract=23`, `uri=23` |
| input_3 | BibTeX | 23 | `PASS_METADATA_ONLY` | `SANITIZED_WITH_REDACTIONS` | `abstract=23`, `file=2`, `note=23` |

Raw export files were not included in the evidence ZIP according to the
submodule return. Parent review did not copy raw exports into integration
reports.

## Parent Verification

Commands run:

- `git status --short --branch`
- `git -C dev-frame-opencode status --short --branch`
- `git -C dev-frame-opencode rev-parse HEAD`
- `Get-FileHash .agent\evidence\evidence-opencode-real-zotero-metadata-export-smoke-a1-r2.zip -Algorithm SHA256`
- Python summary check over
  `.agent\evidence\opencode-real-zotero-metadata-export-smoke-a1-r2\REAL_METADATA_EXPORT_SMOKE_SUMMARY.json`

Observed:

- Parent has existing local dirty state unrelated to this intake:
  `.agent/PROJECT_REGISTRY.json`, `agent-acceptance` local dirty state,
  `scripts/__pycache__/`, and `tests/__pycache__/`.
- `dev-frame-opencode` worktree is clean at
  `7ccbdefa4037a40c76ce137b2d16b48931701c94`.
- Evidence ZIP SHA256 matches the delegated value.
- Summary verdict is `PASS`.
- `schema_validated_reports=3`.
- `raw_assignment_pattern_hits=0`.
- `raw_sensitive_value_hits=0`.
- All three reports have `pilot_status=PASS_METADATA_ONLY`.
- All three reports have `raw_sensitive_fields_absent=true`.
- All three reports have `final_acceptance_claimed=false`.

## GPT Review

Bound GPT review:

- GPT URL: `https://chatgpt.com/c/6a2e02e2-5ff8-83ee-8718-95ff5ac4242f`
- verdict: `accepted_with_limitations`
- accepted status: `OPENCODE_REAL_ZOTERO_METADATA_EXPORT_SMOKE_READY`
- rework required: `false`
- next TaskSpec: `OPENCODE_GROUPED_PARENT_INTAKE_A1`

## Known Gaps

- The evidence package includes local input paths and file names in
  ExecutionReport context. This is non-blocking because the user authorized the
  directory, but parent-facing reports should prefer anonymized input names and
  source fingerprints.
- The raw-sensitive scan result is recorded in
  `REAL_METADATA_EXPORT_SMOKE_SUMMARY.json` and the ExecutionReport, but there
  is no separate `commands/raw-sensitive-scan.txt` transcript.
- This smoke did not use Zotero app/API/storage.
- This smoke did not read PDF, attachments, full text, private notes, Obsidian,
  RAG, WriteLab, browser/CDP, cloud, or MiniApp resources.

## Boundary

Accepted scope:

- local/offline user-provided metadata export files only;
- metadata-only parsing and sanitizer evidence;
- evidence-only parent recording at already-pinned code head.

Rejected promotions:

- metadata export smoke is not live Zotero app/API readiness;
- metadata export smoke is not PDF/full-text readiness;
- metadata export smoke is not Obsidian/RAG/WriteLab/browser/cloud readiness;
- metadata export smoke is not final governance acceptance.

Any expansion beyond user-provided metadata export files must re-enter
`HUMAN_REQUIRED` / `RUNTIME_AUTHORIZATION_REQUIRED`.
