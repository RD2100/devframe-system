# Parent Local Paper RAG Human Spot Check A1

Date: 2026-06-16

## Verdict

PASS_WITH_LIMITATIONS

This parent spot check confirms that the current local paper RAG corpus can route practical user questions to plausible source papers for 4 of 5 questions directly, with 1 question requiring a simple rerank/keyword assist.

This is a usability spot check only. It is not final governance acceptance, paper-quality acceptance, production readiness, broad live readiness, whole-vault readiness, general RAG readiness, external/private RAG readiness, cloud readiness, cloud vector DB readiness, or RuntimeAuthorization.

## Scope

Inputs inspected:

- minimized runtime reports and manifests under `D:\devframe-system\.agent\runtime\local-paper-rag-pipeline-a1`
- minimized quality-eval reports and manifests under `D:\devframe-system\.agent\runtime\local-paper-rag-quality-eval-a1`
- allowlisted Markdown notes under `D:\Obsidian\paper-pilot\papers\virtual-training`

Raw note bodies were used only for local keyword/source plausibility checks. This report does not persist raw note body text, raw chunks, raw query text, raw source paths, vectors, FAISS index contents, API keys, or private runtime payloads.

## Verification Commands

Structural checks:

```powershell
python -m json.tool D:\devframe-system\.agent\runtime\local-paper-rag-pipeline-a1\local-rag-pipeline-report.json
python -m json.tool D:\devframe-system\.agent\runtime\local-paper-rag-quality-eval-a1\local-rag-quality-eval-report.json
python -m json.tool D:\devframe-system\.agent\runtime\local-paper-rag-pipeline-a1\local-rag-pipeline-manifest.json
python -m json.tool D:\devframe-system\.agent\runtime\local-paper-rag-quality-eval-a1\local-rag-quality-eval-manifest.json
```

Result: PASS.

Local runtime dependency check:

- `faiss`: 1.14.3
- `sentence-transformers`: 5.5.1
- `numpy`: 1.26.4

Current minimized facts:

- `pipeline_status=PASS_LOCAL_RAG_PIPELINE`
- `document_count=6`
- `chunk_count=47`
- `retrieval_query_count=3`
- `retrieval_success_count=3`
- `quality_eval_status=PASS_LOCAL_RAG_QUALITY_EVAL`
- `quality_gate_passed=true`
- `retrieval_coverage_ratio=1.0`
- `citation_source_consistency_passed=true`
- `answer_readiness_proxy_passed=true`

## Spot-Check Method

Two checks were used:

1. keyword/source-count sanity check over the six numbered Markdown notes;
2. lightweight document-level semantic matching with `sentence-transformers/all-MiniLM-L6-v2`, using titles plus the first portion of each Markdown note.

The runtime `chunks.jsonl` is intentionally minimized and does not contain raw chunk text. Therefore this spot check did not use raw persisted chunks from the FAISS runtime. It used the allowlisted Obsidian Markdown notes as the permitted source corpus.

## Results

| # | Question | Top Semantic Hit | Expected/Plausible Source | Result |
|---|---|---|---|---|
| 1 | 地震救援技术虚拟训练系统主要解决什么训练问题？ | `01-关于利用虚拟现实技术建立“地震救援技术虚拟训练系统”的几点思考_褚鑫杰.md` score `0.3638` | same source | PASS |
| 2 | 国外军用虚拟训练系统有哪些典型特点？ | `02-国外军用虚拟训练系统研究.md` score `0.4404` | same source | PASS |
| 3 | 虚拟现实技术用于灭火救援训练的优势是什么？ | `03-基于虚拟现实技术的灭火救援训练系统.md` score `0.5446` | same source, with `04-三维建模技术...` also plausible | PASS |
| 4 | 虚拟训练系统的虚拟场景建设需要关注哪些要素？ | `01-关于利用虚拟现实技术建立“地震救援技术虚拟训练系统”的几点思考_褚鑫杰.md` score `0.2575` | `05-虚拟训练系统的虚拟场景研究.md` by title and keyword-count signal | PASS_WITH_LIMITATIONS |
| 5 | 虚拟训练系统在军事职业教育中的应用价值是什么？ | `06-虚拟训练系统在军事职业教育中的应用研究.md` score `0.3013` | same source | PASS |

## Source Sanity Signals

Keyword/source-count checks support the expected sources:

- `01-关于利用虚拟现实技术建立“地震救援技术虚拟训练系统”的几点思考_褚鑫杰.md`: strong `地震`, `救援`, and `虚拟训练` signal.
- `02-国外军用虚拟训练系统研究.md`: strong `国外`, `军用`, and `虚拟训练` signal.
- `03-基于虚拟现实技术的灭火救援训练系统.md`: strong `灭火`, `救援`, `虚拟训练`, and `场景` signal.
- `05-虚拟训练系统的虚拟场景研究.md`: dominant `场景` signal and direct title match for virtual-scene construction.
- `06-虚拟训练系统在军事职业教育中的应用研究.md`: direct `军事职业教育` and `虚拟训练` signal.

## Practical Findings

The local RAG loop is useful enough for a first paper-workflow milestone:

- The corpus is ingested and indexed.
- Most natural questions route to the expected paper.
- Quality eval signals are clean.
- Evidence remains minimized and non-final.

The main observed weakness is ranking quality for broad conceptual questions. Q4 should route to the virtual-scene research paper, but semantic matching alone ranked the earthquake rescue paper first. This is not a blocker for the local milestone, but it is a real usability improvement target.

Recommended improvement:

- add a hybrid retrieval/rerank layer that combines embedding similarity with title, filename, and keyword/source-count signals;
- keep minimized evidence output unchanged;
- re-run spot-check after hybrid rerank.

## Suggested Answer Themes

These are paraphrased themes for human review, not generated final answers:

- Q1: virtual training can support rescue training by simulating high-risk earthquake rescue scenarios, improving repeatability, safety, and scenario coverage.
- Q2: foreign military virtual training systems emphasize simulation environments, repeatable exercises, system integration, and training efficiency.
- Q3: VR fire/rescue training can reduce real-world training risk, support repeatable scenarios, and improve operational preparation.
- Q4: virtual-scene construction should consider scene fidelity, modeling workflow, environment realism, interaction needs, and training objectives.
- Q5: in military vocational education, virtual training can improve teaching flexibility, scenario practice, and training-resource efficiency.

These themes still require human acceptance before being used as paper-quality output.

## Boundary

This spot check does not claim:

- paper-quality acceptance
- final governance acceptance
- production readiness
- whole-vault readiness
- general RAG readiness
- external/private RAG readiness
- cloud vector DB readiness
- RuntimeAuthorization

## Reviewer Index

- changed files:
  - `integration/reports/parent-local-paper-rag-human-spot-check-a1-2026-06-16.md`
- critical code paths: none; parent spot-check report only.
- tests/probes run:
  - JSON parse checks for current minimized runtime reports/manifests
  - local dependency version check
  - keyword/source-count check over allowlisted Markdown notes
  - document-level semantic matching over allowlisted Markdown notes
- generated artifacts:
  - this spot-check report
- known gaps:
  - no new pipeline rebuild in this report
  - no final answer generation workflow
  - no human paper-quality acceptance
  - ranking quality issue observed on Q4
- suggested review focus:
  - confirm Q4 limitation is real and should feed a hybrid rerank task
  - confirm raw note/chunk content is not persisted in this report
  - decide whether to proceed to hybrid rerank or final milestone packet
