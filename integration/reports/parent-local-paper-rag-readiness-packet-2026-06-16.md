# Parent Local Paper RAG Readiness Packet

Date: 2026-06-16

## Purpose

This packet is the practical handoff for the current local paper RAG milestone. It tells a human or future agent what is currently pinned, what can be reproduced, what should be spot-checked, and what must not be claimed.

This packet is intentionally practical. It is not another schema-hardening report.

## Current Locked Milestone

Parent HEAD sequence:

- `ca9d270` - pin opencode local paper RAG quality eval
- `03fa31d` - pin test-frame local paper RAG quality eval consumption
- `1cea349` - pin agent-acceptance local paper RAG quality eval governance review
- `fd74422` - close local paper RAG quality eval milestone
- `4ba8991` - record current project landing status after RAG quality eval

Locked module commits:

- `dev-frame-opencode`: `44188cdb627e571bed55b20fe4f8d71d2d0828c1`
- `test-frame`: `9d91a7f7ae1dcfca0c8b6be362ebb3691e3e8528`
- `agent-acceptance`: `41258e8fc041eda1063eb65ecb300f80f2298534`
- `devframe-control-plane`: `09167bc656f8625c97bfae5c52dae5a0280b116c`

Important caveat: the visible `test-frame` checkout is currently ahead of the lock. The parent lock remains authoritative for this readiness packet.

## Local Inputs

- PDF source folder: `E:\厂里\虚拟训练`
- Obsidian vault root: `D:\Obsidian\paper-pilot`
- generated paper notes folder: `D:\Obsidian\paper-pilot\papers\virtual-training`
- runtime directory: `D:\devframe-system\.agent\runtime\local-paper-rag-pipeline-a1`
- quality eval runtime directory: `D:\devframe-system\.agent\runtime\local-paper-rag-quality-eval-a1`

Current observed source counts:

- PDFs in source folder: 6
- Markdown files under current target folder: 13
- latest pipeline document count: 6
- latest pipeline chunk count: 47

## Reproduction Commands

Run from:

```powershell
cd D:\devframe-system\dev-frame-opencode\ai-workflow-hub
$env:PYTHONPATH = "src"
```

### First or Refresh Pipeline Run

```powershell
python -m ai_workflow_hub.cli paper local-rag-pipeline `
  --pdf-folder "E:\厂里\虚拟训练" `
  --vault-root "D:\Obsidian\paper-pilot" `
  --target-folder "D:\Obsidian\paper-pilot\papers\virtual-training" `
  --runtime-dir "D:\devframe-system\.agent\runtime\local-paper-rag-pipeline-a1" `
  --pdf-limit 6 `
  --top-k 3 `
  --output "D:\devframe-system\.agent\runtime\local-paper-rag-pipeline-a1\local-rag-pipeline-report.json" `
  --manifest-output "D:\devframe-system\.agent\runtime\local-paper-rag-pipeline-a1\local-rag-pipeline-manifest.json"
```

### Rerun / Reuse Check

```powershell
python -m ai_workflow_hub.cli paper local-rag-pipeline `
  --pdf-folder "E:\厂里\虚拟训练" `
  --vault-root "D:\Obsidian\paper-pilot" `
  --target-folder "D:\Obsidian\paper-pilot\papers\virtual-training" `
  --runtime-dir "D:\devframe-system\.agent\runtime\local-paper-rag-pipeline-a1" `
  --pdf-limit 6 `
  --top-k 3 `
  --output "D:\devframe-system\.agent\runtime\local-paper-rag-pipeline-a1\local-rag-pipeline-report-rerun.json" `
  --manifest-output "D:\devframe-system\.agent\runtime\local-paper-rag-pipeline-a1\local-rag-pipeline-manifest-rerun.json"
```

Expected rerun result:

- `pipeline_status=PASS_LOCAL_RAG_PIPELINE`
- `refresh_required=false`
- `index_reused=true`
- `retrieval_success_count=3`
- no raw PDF text, Markdown body, chunk text, query text, vectors, source paths, or secrets in the minimized report/manifest.

### Quality Eval

```powershell
python -m ai_workflow_hub.cli paper local-rag-quality-eval `
  --pipeline-report "D:\devframe-system\.agent\runtime\local-paper-rag-pipeline-a1\local-rag-pipeline-report.json" `
  --pipeline-schema "D:\devframe-system\dev-frame-opencode\schemas\paper_local_rag_pipeline_report.schema.json" `
  --source-pipeline-commit "7c13ff0de6de8c50706b77efb58b132bce27dce0" `
  --output "D:\devframe-system\.agent\runtime\local-paper-rag-quality-eval-a1\local-rag-quality-eval-report.json" `
  --manifest-output "D:\devframe-system\.agent\runtime\local-paper-rag-quality-eval-a1\local-rag-quality-eval-manifest.json"
```

Expected quality eval result:

- `quality_eval_status=PASS_LOCAL_RAG_QUALITY_EVAL`
- `quality_gate_passed=true`
- `retrieval_coverage_ratio=1.0`
- `citation_source_consistency_passed=true`
- `answer_readiness_proxy_passed=true`

## Current Verified Minimized Facts

The latest local minimized reports currently parse successfully and show:

- `pipeline_status=PASS_LOCAL_RAG_PIPELINE`
- `pdf_count=6`
- `markdown_note_count=13`
- `document_count=6`
- `chunk_count=47`
- `source_fingerprint_count=19`
- `retrieval_query_count=3`
- `retrieval_success_count=3`
- `top_k_total_count=9`
- `coverage_count=3`
- `empty_result_count=0`
- `duplicate_result_count=0`
- `low_confidence_count=0`
- `warnings_count=0`
- `quality_eval_status=PASS_LOCAL_RAG_QUALITY_EVAL`
- `quality_gate_passed=true`
- `issue_count=0`

Verification performed for this packet:

```powershell
python -m json.tool D:\devframe-system\.agent\runtime\local-paper-rag-pipeline-a1\local-rag-pipeline-report.json
python -m json.tool D:\devframe-system\.agent\runtime\local-paper-rag-quality-eval-a1\local-rag-quality-eval-report.json
python -m json.tool D:\devframe-system\.agent\runtime\local-paper-rag-pipeline-a1\local-rag-pipeline-manifest.json
python -m json.tool D:\devframe-system\.agent\runtime\local-paper-rag-quality-eval-a1\local-rag-quality-eval-manifest.json
```

Result: PASS.

## Human Spot-Check Questions

Use these questions to judge whether the current local RAG behavior is practically useful. The current automated quality gate is a proxy; these questions are where human quality starts.

| # | Question | Expected Source Direction | Pass Criteria |
|---|---|---|---|
| 1 | 地震救援技术虚拟训练系统主要解决什么训练问题？ | virtual earthquake rescue training system note | Answer identifies rescue training scenario, virtual simulation purpose, and training-system value without hallucinating unrelated domains. |
| 2 | 国外军用虚拟训练系统有哪些典型特点？ | foreign military virtual training system note | Answer distinguishes military training context and gives concrete system/practice traits. |
| 3 | 虚拟现实技术用于灭火救援训练的优势是什么？ | fire rescue VR training note | Answer mentions training safety, repeatability, scenario simulation, or operational preparation. |
| 4 | 虚拟训练系统的虚拟场景建设需要关注哪些要素？ | virtual scene research note | Answer discusses scene construction/modeling/environment fidelity rather than generic RAG boilerplate. |
| 5 | 虚拟训练系统在军事职业教育中的应用价值是什么？ | military vocational education note | Answer ties virtual training to education/training effectiveness and does not claim production-grade proof. |

Spot-check outcome labels:

- `PASS_SPOT_CHECK`: answers are useful and sources are plausible.
- `PASS_WITH_LIMITATIONS`: answers are directionally useful but need better citation grounding or coverage.
- `REWORK_REQUIRED`: answers miss obvious source material, hallucinate, or cannot map to corpus sources.

## Hard No-Claim Boundary

The following remain blocked:

- final governance acceptance
- paper-quality acceptance
- production readiness
- broad live readiness
- whole-vault readiness
- general RAG readiness
- external/private RAG readiness
- cloud vector DB readiness
- cloud readiness
- RuntimeAuthorization

`quality_gate_passed=true` is not a paper-quality verdict. It is a deterministic local evidence signal.

## Rollback Reference

No rollback was executed. If a human later decides to rollback the latest parent-only reports, the relevant parent commits are:

- `4ba8991` - current landing status report
- `fd74422` - quality eval milestone closeout
- `1cea349` - agent-acceptance quality eval pin
- `03fa31d` - test-frame quality eval consumption pin
- `ca9d270` - opencode quality eval pin

Use normal Git review before any rollback. Do not run destructive rollback commands without explicit approval.

## Next Recommended Task

`PARENT_LOCAL_PAPER_RAG_HUMAN_SPOT_CHECK_A1`

Goal:

- Run or inspect answers for the five spot-check questions above.
- Record answer usefulness, source plausibility, and whether any obvious paper is missing.
- Keep raw/private evidence out of parent reports unless explicitly authorized and minimized.

This is the highest-value next step because the engineering loop is already proven at milestone level; the remaining question is whether the output is useful enough for the user's paper workflow.

## Reviewer Index

- changed files:
  - `integration/reports/parent-local-paper-rag-readiness-packet-2026-06-16.md`
- critical code paths: none; parent readiness packet only.
- tests/probes run:
  - `git status --short --branch`
  - `git submodule status --recursive`
  - CLI source inspection for `paper local-rag-pipeline` and `paper local-rag-quality-eval`
  - JSON parse checks for current minimized runtime reports/manifests
  - minimized fact extraction from current pipeline and quality-eval reports
- generated artifacts:
  - this readiness packet
- known gaps:
  - no new runtime execution in this packet
  - no raw/private content inspection
  - no human answer-quality spot check yet
- suggested review focus:
  - verify reproduction commands match CLI definitions
  - verify spot-check questions cover the actual current corpus
  - verify no final/production/RAG-ready claim is made
