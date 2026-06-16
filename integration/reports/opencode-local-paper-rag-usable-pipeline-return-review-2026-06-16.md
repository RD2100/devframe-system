# Return Review: opencode Local Paper RAG Usable Pipeline

Date: 2026-06-16

## Reviewed Return

- TaskSpec: `OPENCODE_LOCAL_PAPER_RAG_USABLE_PIPELINE_A1`
- Submodule: `D:\devframe-system\dev-frame-opencode`
- Branch: `codex/paper-audit-privacy-hard-gate`
- Commit: `7c13ff0de6de8c50706b77efb58b132bce27dce0`
- Message: `Add usable local paper RAG pipeline`
- Evidence ZIP: `D:\devframe-system\.agent\evidence\evidence-opencode-local-paper-rag-usable-pipeline-a1-7c13ff0.zip`
- ZIP SHA256: `BA8AD8D6E9E012D17A2CE0EA71FDB478232907D6806470801DC6B4A8C1159B9A`

## Intake Decision

ACCEPTED_FOR_PARENT_PIN.

This return upgrades the previous local paper RAG closed-loop smoke into a repeatable local pipeline command. It proves a first run can build a local index and a second run can detect unchanged inputs and reuse the index. The evidence remains minimized and non-final.

## Evidence Verification

- Evidence hash: PASS.
- Evidence entry list: PASS.
- First-run minimized report inspection: PASS.
- Rerun minimized report inspection: PASS.
- Focused tests: PASS, `5 passed`.
- Adjacent RAG/Obsidian/closed-loop regression: PASS, `37 passed`.
- Schema parse: PASS.
- Report schema validation for first run and rerun: PASS.
- Raw value/path marker scan over minimized report and manifest: PASS.
- Submodule diff whitespace check: PASS.

## Live Smoke Summary

First run:

- `pipeline_status`: `PASS_LOCAL_RAG_PIPELINE`
- PDFs: 6
- Markdown notes: 13
- FAISS documents: 6
- Chunks: 47
- Source fingerprints: 19
- New sources: 19
- Changed sources: 0
- Unchanged sources: 0
- Deleted sources: 0
- Refresh required/completed: true/true
- Index rebuilt: true
- Retrieval queries/successes: 3/3
- Total top-k results: 9
- Coverage count: 3
- Empty/duplicate/low-confidence/warnings: 0/0/0/0

Second run:

- `pipeline_status`: `PASS_LOCAL_RAG_PIPELINE`
- New/changed/unchanged/deleted: 0/0/19/0
- Refresh required/completed: false/true
- Index reused: true

## Evidence Boundary

The evidence ZIP excludes raw PDF text, raw Markdown bodies, raw chunks, raw query text, raw source paths, vectors, FAISS binary, secrets, API keys, and raw WriteLab payload/response. Runtime Markdown/index/state artifacts remain local runtime artifacts and are not evidence payloads.

## Known Gaps

- Scoped repeatable local pipeline only.
- Quality spot-check is deterministic/rules-only and does not claim paper-quality acceptance.
- Whole-vault RAG, external/private RAG, production readiness, and final governance acceptance remain out of scope.
- Test-frame consumption and agent-acceptance governance review remain required before milestone closeout.
