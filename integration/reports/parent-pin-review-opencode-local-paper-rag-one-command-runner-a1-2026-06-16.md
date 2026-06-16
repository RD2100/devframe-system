# Parent Pin Review: opencode local paper RAG one-command runner A1

Date: 2026-06-16

## Verdict

`ACCEPTED_AND_PARENT_PINNED`

This parent intake accepts the `dev-frame-opencode` one-command local RAG runner
as scoped local milestone evidence only. It is not final governance acceptance,
paper-quality acceptance, production readiness, whole-vault readiness,
broad/general RAG readiness, cloud readiness, or RuntimeAuthorization.

## Submodule Pin

- module: `dev-frame-opencode`
- previous parent pin: `528f5b801082a10759df000a2315486a55a22e79`
- accepted commit: `a22f3bb68988a2107973c46a2df4dab31def31b8`
- commit message: `Add local paper RAG one-command runner`

## Evidence

- evidence ZIP: `D:\devframe-system\.agent\evidence\OPENCODE_LOCAL_PAPER_RAG_ONE_COMMAND_RUNNER_A1-a22f3bb-20260616.zip`
- observed SHA256: `DF5B07CCAD4A43F06A4C92ED5704458E490738DA484ECB8F8B28D4D9F237A113`

ZIP entries inspected:

- `artifact/paper-local-rag-one-command-manifest.json`
- `artifact/paper-local-rag-one-command-report.json`
- `artifact/smoke-summary.json`
- `commands/COMMANDS.md`
- `commands/generate_minimized_artifact.py`
- `schema/paper_local_rag_one_command_runner_report.schema.json`
- `EXECUTION_REPORT.md`
- `REVIEWER_INDEX.md`

## Parent Review Checks

- `git -C dev-frame-opencode status --short --branch --untracked-files=all`
  - passed; submodule tracked worktree clean
- `git -C dev-frame-opencode rev-parse HEAD`
  - passed; observed `a22f3bb68988a2107973c46a2df4dab31def31b8`
- `Get-FileHash ... OPENCODE_LOCAL_PAPER_RAG_ONE_COMMAND_RUNNER_A1-a22f3bb-20260616.zip`
  - passed; hash matched reported value
- `python -m pytest tests\test_paper_local_rag_one_command_runner.py -q`
  - passed; `4 passed`
- `python -m pytest tests\test_paper_local_rag_one_command_runner.py tests\test_paper_local_rag_pipeline.py tests\test_paper_local_rag_quality_eval.py tests\test_paper_local_rag_answer_preview.py -q`
  - passed; `21 passed`
- `python -m json.tool schemas\paper_local_rag_one_command_runner_report.schema.json`
  - passed

## Report Summary

The minimized one-command report records:

- `runner_status=PASS_LOCAL_RAG_RUN`
- `pipeline_status=PASS_LOCAL_RAG_PIPELINE`
- `quality_eval_status=PASS_LOCAL_RAG_QUALITY_EVAL`
- `answer_preview_status=PASS_LOCAL_RAG_ANSWER_PREVIEW`
- `quality_gate_passed=true`
- `document_count=6`
- `chunk_count=47`
- `retrieval_query_count=3`
- `retrieval_success_count=3`
- `answer_preview_count=5`

The report also records these boundary flags as false:

- raw PDF text persisted
- raw Markdown body persisted
- raw chunks persisted
- raw query persisted
- raw source paths persisted
- vectors persisted
- FAISS index binary in evidence
- API keys or secrets persisted
- Zotero API called
- cloud LLM called
- cloud vector DB called
- external RAG called
- browser/CDP/cloud/MiniApp called
- whole vault scanned
- RuntimeAuthorization granted
- final acceptance claimed
- paper-quality acceptance claimed
- production-ready claimed
- broad/general RAG readiness claimed

## Known Gap

The submodule evidence explicitly records that its CLI smoke patched the first
stage pipeline builder to avoid real PDF/vector dependency risk in that smoke.
The parent therefore accepts this slice as a usability entrypoint and minimized
runner contract, while real local pipeline behavior remains covered by the
previously accepted local pipeline, quality-eval, hybrid rerank, and answer
preview milestones.

## Reviewer Index

Changed submodule paths:

- `ai-workflow-hub/src/ai_workflow_hub/cli.py`
- `ai-workflow-hub/src/ai_workflow_hub/context_layer/adapters/local_paper_rag_one_command_runner.py`
- `ai-workflow-hub/tests/test_paper_local_rag_one_command_runner.py`
- `schemas/paper_local_rag_one_command_runner_report.schema.json`

Parent paths updated:

- `dev-frame-opencode` gitlink
- `integration/lock/submodules.lock.yml`
- `CURRENT_DELIVERY.md`
- `integration/reports/parent-pin-review-opencode-local-paper-rag-one-command-runner-a1-2026-06-16.md`

Suggested follow-up:

- Run the command against the authorized real local folders when a fresh runtime
  reproduction is desired.
- Keep final paper-quality, production, whole-vault, and cloud/private RAG
  readiness as separate human-gated decisions.
