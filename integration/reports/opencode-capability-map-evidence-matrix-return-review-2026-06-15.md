# Opencode capability-map evidence matrix 回传审查

日期：2026-06-15

## 状态

`OPENCODE_CAPABILITY_MAP_EVIDENCE_MATRIX_A22_ACCEPTED_FOR_PARENT_INTAKE`

父仓审查了 `dev-frame-opencode` 从 A21 后继续推进的 local/offline 论文能力图谱、
schema 关闭、证据包、business validation evidence matrix 和 capability map hash
绑定链条。

最终父仓 pin 目标是 committed head
`f5b0c80450aed908ae3cddc578c06962a86ddea7`。opencode 当前仍有 HOLD 到达前
产生的未提交 WIP；这些 WIP 不纳入本次 pin。

## 来源

- 模块：`dev-frame-opencode`
- 分支：`codex/paper-audit-privacy-hard-gate`
- A21 基线：`a1ed82bb06bb42f4ba0bb14c8518988302cd2894`
- 当前候选：`f5b0c80450aed908ae3cddc578c06962a86ddea7`
- 最新提交信息：`Bind capability map hash in business validation`
- evidence ZIP：
  `D:\devframe-system\.agent\evidence\evidence-opencode-business-validation-capability-map-hash-a1-f5b0c80.zip`
- evidence ZIP SHA256：
  `0B2D7DB7B3FFC5C142C4A1F5799A5FF7788EB0A658EA6B2768185F408732EBB9`

## 覆盖的提交链

- `3c92c03` Close preauth agent acceptance handoff shape
- `b1147d0` Close local dry run gate and redaction shapes
- `017f451` Close evidence manifest retrieval records
- `d0a559e` Close paper evidence pack summary rows
- `49ff02b` Close paper evidence pack citation rows
- `84bd608` Close paper evidence pack dimension scores
- `9ee1854` Close paper evidence pack root shape
- `7fd43bb` Close paper task IO summary schemas
- `8b21be8` Close MVP common output rows
- `1f1f80a` Close MVP task input and gate objects
- `c7bb212` Close MVP allOf contract payload fields
- `9a977fd` Add paper raw payload schema guard tests
- `801d7a4` Guard paper schema object closure
- `54f2f24` Expose schema privacy guards in business validation
- `73fbe8e` Index schema privacy guard evidence
- `1a080d2` Guard paper capability map boundaries
- `3ee5ccf` Add machine readable paper capability map
- `a680c6e` Expose capability map artifact in business validation
- `dec0a32` Add paper capability map CLI artifact
- `7ffc609` Index capability map in business validation evidence
- `f5b0c80` Bind capability map hash in business validation

## 父仓侧验证

- `python -m pytest tests\test_paper_business_capability_validation.py tests\test_paper_mvp_contracts.py tests\test_paper_schema_raw_payload_guards.py tests\test_paper_evidence_manifest.py tests\test_paper_evidence_pack_schema.py tests\test_paper_task_io_schema.py tests\test_paper_real_pilot_preauth_packet.py tests\test_paper_real_pilot_local_dry_run.py -q`
  -> 57 passed
- `python -m json.tool` for the changed paper schemas
  -> PASS
- `git diff --check a1ed82bb06bb42f4ba0bb14c8518988302cd2894..HEAD`
  -> PASS
- f5 evidence package recorded business/MVP/schema guard tests
  -> 24 passed

## 边界判断

接受范围：

- local synthetic/offline evidence only；
- metadata/local-fixture only；
- capability map、schema closure、EvidenceManifest、paper evidence pack、
  business validation evidence matrix 的合同硬化；
- 父仓候选审查记录。

WIP 边界：

- `ai-workflow-hub/tests/test_paper_business_capability_validation.py` 的未提交修改不纳入本次 pin；
- `schemas/paper_business_validation_report.schema.json` 的未提交修改不纳入本次 pin；
- 父仓只 pin `f5b0c80` committed state。

不接受、不授权：

- 真实 Zotero 通过；
- Obsidian、RAG、WriteLab；
- PDF、附件、全文、private paper runtime；
- browser/CDP/cloud/MiniApp；
- live-ready；
- final acceptance。

## 审核索引

- 父仓本次引用的模块关键路径：
  - `ai-workflow-hub/src/ai_workflow_hub/cli.py`
  - `ai-workflow-hub/tests/test_paper_business_capability_validation.py`
  - `ai-workflow-hub/tests/test_paper_mvp_contracts.py`
  - `ai-workflow-hub/tests/test_paper_schema_raw_payload_guards.py`
  - `ai-workflow-hub/tests/test_paper_evidence_manifest.py`
  - `ai-workflow-hub/tests/test_paper_evidence_pack_schema.py`
  - `ai-workflow-hub/tests/test_paper_task_io_schema.py`
  - `schemas/paper_business_validation_report.schema.json`
  - `schemas/paper_capability_map.schema.json`
  - `schemas/paper_evidence_manifest.schema.json`
  - `schemas/paper_evidence_pack.schema.json`
  - `schemas/paper_mvp_io_contracts.schema.json`
  - `schemas/paper_task_input.schema.json`
  - `schemas/paper_task_output.schema.json`
- 已知缺口：
  - 仍然只是 local/offline candidate。
  - 没有真实资源执行。
  - 本审查没有把 blocked Zotero metadata-only 尝试升级为通过。
