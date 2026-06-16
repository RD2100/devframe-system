# Local paper RAG one-command real reproduction

Date: 2026-06-16

## Verdict

`PASS_LOCAL_RAG_RUN_REPRODUCED_ON_AUTHORIZED_LOCAL_FOLDERS`

This is a real local reproduction of the pinned one-command runner against the
authorized local PDF folder and Obsidian paper folder. It remains a local
milestone reproduction only. It is not final governance acceptance,
paper-quality acceptance, production readiness, whole-vault readiness,
broad/general RAG readiness, cloud readiness, or RuntimeAuthorization.

## Command Under Test

Submodule:

- `dev-frame-opencode`
- pinned commit: `a22f3bb68988a2107973c46a2df4dab31def31b8`

Entrypoint:

- `python -m ai_workflow_hub.cli paper local-rag-run`

Authorized local inputs:

- PDF folder: `E:\厂里\虚拟训练`
- Obsidian vault root: `D:\Obsidian\paper-pilot`
- Obsidian paper folder: `D:\Obsidian\paper-pilot\papers\virtual-training`

Runtime output directory:

- `D:\devframe-system\.agent\runtime\local-paper-rag-run-real-2026-06-16`

## First Run Summary

- command exit code: `0`
- `runner_status=PASS_LOCAL_RAG_RUN`
- `pipeline_status=PASS_LOCAL_RAG_PIPELINE`
- `quality_eval_status=PASS_LOCAL_RAG_QUALITY_EVAL`
- `answer_preview_status=PASS_LOCAL_RAG_ANSWER_PREVIEW`
- `quality_gate_passed=true`
- `document_count=6`
- `chunk_count=47`
- `retrieval_query_count=3`
- `retrieval_success_count=3`
- `top_k_total_count=9`
- `answer_preview_count=5`
- `refresh_required=true`
- `refresh_completed=true`
- `index_reused=false`
- `index_rebuilt=true`

Artifacts:

- report: `D:\devframe-system\.agent\runtime\local-paper-rag-run-real-2026-06-16\one-command-report.json`
- report SHA256: `6C4E8182A0F3DC5B016DC59055421956A2B21E4F79F0A9AC3F6253CB5B73C8E5`
- manifest: `D:\devframe-system\.agent\runtime\local-paper-rag-run-real-2026-06-16\one-command-manifest.json`
- manifest SHA256: `40A7B90547F70AED1DD94C1B473939B47B814A3AAB532F50641572BD38D364F4`

## Second Run Summary

- command exit code: `0`
- `runner_status=PASS_LOCAL_RAG_RUN`
- `pipeline_status=PASS_LOCAL_RAG_PIPELINE`
- `quality_eval_status=PASS_LOCAL_RAG_QUALITY_EVAL`
- `answer_preview_status=PASS_LOCAL_RAG_ANSWER_PREVIEW`
- `quality_gate_passed=true`
- `document_count=6`
- `chunk_count=47`
- `retrieval_query_count=3`
- `retrieval_success_count=3`
- `top_k_total_count=9`
- `answer_preview_count=5`
- `refresh_required=false`
- `refresh_completed=true`
- `index_reused=true`
- `index_rebuilt=true`

Artifacts:

- report: `D:\devframe-system\.agent\runtime\local-paper-rag-run-real-2026-06-16\one-command-report-rerun.json`
- report SHA256: `407868177BC0DD97A9F5A50AE1EEECCAF6F1CCD7C972DFBF338A2BA95A92693A`
- manifest: `D:\devframe-system\.agent\runtime\local-paper-rag-run-real-2026-06-16\one-command-manifest-rerun.json`
- manifest SHA256: `FFD89F1E27CF3EBAB9F94B02EF3F3A02D8E998E9521E76693F5FB1AF7569D9D6`

Note: the second run records `index_reused=true` and `refresh_required=false`.
It also records `index_rebuilt=true`; this report preserves that exact runtime
output and does not reinterpret it as a pure-reuse-only run.

## Validation

Validation commands:

- report JSON parse: passed
- manifest JSON parse: passed
- report schema validation against `paper_local_rag_one_command_runner_report.schema.json`: passed
- path/content marker scan over the four minimized report/manifest files: passed for path/content values

The marker scan did match schema field names such as
`raw_pdf_text_persisted=false`, `raw_markdown_body_persisted=false`, and
`api_keys_or_secrets_persisted=false`. These are expected boundary booleans, not
raw values.

## Runtime Warnings

The command emitted non-blocking local runtime warnings:

- PyPDF2 warnings for duplicate `/MediaBox` entries.
- PyPDF2 warning for unimplemented `/GBK-EUC-H` advanced encoding.
- Hugging Face Hub unauthenticated request warning.

These warnings did not prevent the minimized one-command report from passing.
They should be considered operational polish items, not current blockers.

## Boundary Confirmation

The minimized reports record:

- `raw_pdf_text_persisted=false`
- `raw_markdown_body_persisted=false`
- `raw_chunks_persisted=false`
- `raw_query_persisted=false`
- `raw_source_paths_persisted=false`
- `vectors_persisted=false`
- `faiss_index_binary_in_evidence=false`
- `api_keys_or_secrets_persisted=false`
- `raw_writelab_payload_persisted=false`
- `raw_writelab_response_persisted=false`
- `zotero_api_called=false`
- `cloud_llm_called=false`
- `cloud_vector_db_called=false`
- `external_rag_called=false`
- `browser_cdp_cloud_or_miniapp_called=false`
- `whole_vault_scanned=false`
- `runtime_authorization_granted=false`
- `final_acceptance_claimed=false`
- `paper_quality_acceptance_claimed=false`
- `production_ready_claimed=false`
- `broad_live_ready_claimed=false`
- `general_rag_ready_claimed=false`
- `whole_vault_ready_claimed=false`
- `external_rag_ready_claimed=false`
- `cloud_ready_claimed=false`

## Practical Meaning

The current project can now be used locally to run the authorized paper RAG
chain through one command and produce minimized report/manifest outputs.

Still not proven:

- paper-quality acceptance,
- target venue compliance,
- whole-vault indexing,
- external/private RAG service readiness,
- cloud vector DB readiness,
- production readiness,
- or final governance acceptance.
