# Zotero 元数据-only 真实资源尝试记录

日期：2026-06-15

## 状态

`BLOCKED_FOR_FORBIDDEN_METADATA_FIELDS`

本报告记录一次真实 Zotero 元数据-only pilot 尝试。它不是通过报告，
不是最终验收，也不授权 Obsidian、RAG、WriteLab、PDF、附件或全文处理。

## 输入

- 用户提供目录：
  `D:\devframe-system\.agent\manual-input`
- 实际输入文件：
  `D:\devframe-system\.agent\manual-input\导出的条目.bib`
- 输入文件大小：66736 bytes
- 输入文件 SHA256：
  `73E636C3F36563B1FB2BD0892C5B01D538D0BDE7EEC9E762A0B82713415363EF`

## 执行范围

本次只允许：

- 读取用户提供的 Zotero metadata export 文件；
- 识别格式；
- 检查安全边界；
- 生成 RuntimeAuthorization decision 和 pilot report。

本次不允许，也没有执行：

- Zotero 本地数据库读取；
- Zotero 附件、PDF、全文、批注读取；
- Obsidian vault 扫描；
- RAG 检索；
- WriteLab live 调用；
- browser/CDP/cloud 调用；
- final acceptance。

## 结果

输出目录：

`D:\devframe-system\.agent\evidence\zotero-metadata-only-pilot-20260615-1901`

生成文件：

- `human-runtime-authorization-decision.json`
- `zotero-metadata-only-pilot-report.json`

pilot report SHA256：

`C1ED4DBFA13A4AF3CFAEE33F3B112D8FC53CE83C4980DD46870CA82A0D06FFB3`

关键结果：

- `pilot_status`: `BLOCKED`
- `metadata_format_detected`: `bibtex`
- `export_size_bytes`: `66736`
- `final_acceptance_claimed`: `false`
- `raw_sensitive_fields_absent`: `true`
- `reasons`: `forbidden_metadata_export_fields_present`
- `forbidden_fields`: `abstract`, `file`, `note`

## 判断

这次阻断是正确行为。

导出的 BibTeX 文件仍包含摘要、附件路径或笔记相关字段。当前项目规则要求
metadata-only pilot 不能处理这些字段，所以不能把本次运行升级为通过。

## 下一步

需要用户从 Zotero 重新导出一个干净文件：

`D:\devframe-system\.agent\manual-input\zotero-metadata-pilot-clean.bib`

导出要求：

- 不导出笔记；
- 不导出文件；
- 不包括注释；
- 排除字段：`abstract,file,note`；
- 不包含 PDF、附件路径、全文、批注、个人笔记。

如果 Zotero 默认导出仍带这些字段，建议安装 Better BibTeX，并在导出设置中
配置省略字段后重新导出。

## 审核索引

- 改动父仓文件：
  - 本报告。
- 关键路径：
  - RuntimeAuthorization decision 生成。
  - Zotero metadata-only pilot report。
  - 禁止字段 fail-closed。
- 已运行命令：
  - `Get-ChildItem D:\devframe-system\.agent\manual-input`
  - `python -m ai_workflow_hub.cli paper real-pilot-authorize-metadata`
  - `python -m ai_workflow_hub.cli paper real-zotero-metadata-pilot`
  - `Get-FileHash` for input and report.
- 未运行命令：
  - 未读取 Zotero 数据库；
  - 未读取 PDF、附件、全文；
  - 未启动 Obsidian、RAG、WriteLab、browser/CDP/cloud。
- 已知缺口：
  - 需要用户重新导出干净 metadata-only 文件。
  - 当前结果是 `BLOCKED`，不是 `PASS_METADATA_ONLY`。
