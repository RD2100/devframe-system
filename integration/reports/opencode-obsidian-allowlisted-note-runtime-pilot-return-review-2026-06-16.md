# opencode Obsidian Allowlisted Note Runtime Pilot Return Review

Date: 2026-06-16

## Verdict

ACCEPTED_FOR_PARENT_PIN as a scoped Obsidian allowlisted single-note runtime pilot.

This is not final governance acceptance, paper-quality acceptance, production readiness, broad live readiness, RAG readiness, or authorization for whole-vault/attachment/PDF access.

## Reviewed Return

- Module: `dev-frame-opencode`
- Branch: `codex/paper-audit-privacy-hard-gate`
- Commit: `7f9496310547ceef09e3a6d1e40758d321995fdc`
- Message: `Add Obsidian allowlisted note runtime pilot`
- Evidence ZIP: `D:\devframe-system\.agent\evidence\evidence-opencode-obsidian-allowlisted-note-runtime-pilot-a1-7f94963.zip`
- Expected SHA256: `6474305DF16CF249918E9FD249B2C085484383A7C2496E551EAC40EBAFA8190C`
- Observed SHA256: `6474305DF16CF249918E9FD249B2C085484383A7C2496E551EAC40EBAFA8190C`

## Scope Accepted

- Adds scoped Obsidian allowlisted-note runtime pilot support.
- Adds/updates CLI aliases:
  - `paper obsidian-allowlisted-note-pilot`
  - `paper obsidian-note-pilot`
- Extends the existing Obsidian note adapter with vault-root containment, note existence, heading/link/count facts, and boundary booleans.
- Adds closed schema `schemas/paper_obsidian_allowlisted_note_pilot_report.schema.json`.

## Live Scoped Smoke Summary

- Vault root was present.
- One allowlisted Markdown note was read.
- `pilot_status=PASS_ALLOWLISTED_NOTE_METADATA`
- `note_bytes=19316`
- `heading_count=5`
- `link_count=0`
- `full_vault_scanned=false`
- `attachments_read=false`
- `rag_executed=false`
- `final_acceptance_claimed=false`

## Parent Verification

- Evidence hash matched expected SHA256.
- Evidence entry list was limited to changed-files, command logs, minimized reports, schema snapshot, `EXECUTION_REPORT.md`, and `REVIEWER_INDEX.md`.
- `python -m pytest tests\test_obsidian_note_adapter.py -q` -> 11 passed.
- Related regression: `python -m pytest tests\test_obsidian_note_adapter.py tests\test_paper_business_capability_validation.py tests\test_paper_plugin_pilot_closeout.py tests\test_paper_next_plugin_readiness.py tests\test_paper_mvp_end_to_end_closeout.py -q` -> 59 passed.
- `python -m json.tool schemas\paper_obsidian_allowlisted_note_pilot_report.schema.json` -> PASS.
- ZIP report JSON validates against `paper_obsidian_allowlisted_note_pilot_report.schema.json`.
- ZIP raw-sensitive scan: PASS.
- `git diff --check 052b6620a52ac2a525ca5e911e4f090d38f0f9a1 7f9496310547ceef09e3a6d1e40758d321995fdc` -> PASS.

## Privacy Boundary

- The evidence report stores note fingerprint, path fingerprint, note size, and counts only.
- The report records `raw_note_persisted=false` and `raw_note_path_persisted=false`.
- No raw note body, raw paper text, raw note path, raw PDF path content, or vault listing is accepted as parent evidence.

## Known Gaps

- RAG/private retrieval remains unexecuted and requires a fresh scoped TaskSpec.
- Whole-vault scan, attachments, PDF/full-text, and WriteLab remain out of scope for this slice.
- Paper quality acceptance remains a separate human/reviewer decision.
