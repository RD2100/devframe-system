# Opencode evidence row command binding 回传审查

日期：2026-06-15

## 状态

`OPENCODE_BUSINESS_VALIDATION_EVIDENCE_ROW_COMMAND_BINDING_A23_ACCEPTED_FOR_PARENT_INTAKE`

父仓接受 `dev-frame-opencode` A23 local/offline schema-contract hardening
切片，用于父仓 pin。

## 来源

- 模块：`dev-frame-opencode`
- 分支：`codex/paper-audit-privacy-hard-gate`
- A22 基线：`f29fe61fdf9952bfa77fe6e5f858219293355641`
- 当前候选：`4333c1218d5c7871e090b8364bbe96c4e57ecd50`
- 提交信息：`Bind business validation evidence row commands`
- evidence ZIP：
  `D:\devframe-system\.agent\evidence\evidence-opencode-business-validation-evidence-row-command-binding-a1-4333c12.zip`
- evidence ZIP SHA256：
  `30D85B4901EFC0DA4D3A4B6B84CB8318B50766D199DD7BF2F74DC54CD723C7CE`

## 内容

该切片进一步收紧 paper business validation report 的 `evidence_matrix`
合同：

- 每个已允许的 `capability` 必须绑定到精确 `command`；
- 伪造“合法 capability + 错误 command”的证据行会被 schema 拒绝；
- business validation report 仍是 candidate evidence，不是 final acceptance。

## 父仓侧验证

- `python -m pytest tests\test_paper_business_capability_validation.py tests\test_paper_mvp_contracts.py tests\test_paper_schema_raw_payload_guards.py -q`
  -> 26 passed
- `python -m json.tool schemas\paper_business_validation_report.schema.json`
  -> PASS
- `git diff --check HEAD~1 HEAD`
  -> PASS

## 边界

接受范围：

- local/offline schema-contract hardening；
- business validation evidence row command binding；
- evidence ambiguity fail-closed。

不接受、不授权：

- 真实 Zotero 通过；
- Obsidian、RAG、WriteLab；
- PDF、附件、全文；
- browser/CDP/cloud/MiniApp；
- live-ready；
- final acceptance。

## 审核索引

- 模块变更文件：
  - `D:\devframe-system\dev-frame-opencode\schemas\paper_business_validation_report.schema.json`
  - `D:\devframe-system\dev-frame-opencode\ai-workflow-hub\tests\test_paper_business_capability_validation.py`
- 关键路径：
  - evidence matrix capability/command binding；
  - mismatched row negative validation。
- 已知缺口：
  - 仍是 local/offline candidate。
  - 不代表真实资源接入完成。
