# 父仓 pin 审查 A22

日期：2026-06-15

## 状态

`A22_OPENCODE_CAPABILITY_MAP_HASH_PIN_REVIEW_PASS_WITH_DIRTY_WIP_NOTE`

父仓接受 `dev-frame-opencode` A21 后的 capability map、schema closure、
business validation evidence matrix 和 capability map hash 绑定链条，并更新
gitlink/lock 到 committed head `f5b0c80...`。

注意：`dev-frame-opencode` 当前仍有 HOLD 到达前产生的未提交 WIP。父仓本次只 pin
committed head，不纳入 WIP。

## 候选 pin

- `agent-acceptance`：
  `75f8eb329778d4a8cffb28f6ba79b137038d4fed`
- `dev-frame-opencode`：
  `f5b0c80450aed908ae3cddc578c06962a86ddea7`
- `devframe-control-plane`：
  `79399541b8426cff0f362b665bad09e3c23e974b`
- `test-frame`：
  `c3353fb34900aa24f56df5b9c9230f3249d6c01a`

## 决定

将 `dev-frame-opencode` 从：

`a1ed82bb06bb42f4ba0bb14c8518988302cd2894`

更新到：

`f5b0c80450aed908ae3cddc578c06962a86ddea7`

其他三个模块保持不变。

## 证据

- 已审 A22 候选回传：
  `integration/reports/opencode-capability-map-evidence-matrix-return-review-2026-06-15.md`
- 7ffc609 evidence ZIP：
  `D:\devframe-system\.agent\evidence\evidence-opencode-business-validation-capability-map-evidence-matrix-a1-7ffc609.zip`
- 7ffc609 evidence ZIP SHA256：
  `15E21DF9CF382308FAA06F74CDB8F62D8D2FBDC16C10F5AD578E67E4C1927E65`
- 最终 pin head：
  `f5b0c80450aed908ae3cddc578c06962a86ddea7`
- f5b0c80 evidence ZIP：
  `D:\devframe-system\.agent\evidence\evidence-opencode-business-validation-capability-map-hash-a1-f5b0c80.zip`
- f5b0c80 evidence ZIP SHA256：
  `0B2D7DB7B3FFC5C142C4A1F5799A5FF7788EB0A658EA6B2768185F408732EBB9`
- WIP 不纳入 pin：
  `dev-frame-opencode` worktree dirty with modified
  `ai-workflow-hub/tests/test_paper_business_capability_validation.py` and
  `schemas/paper_business_validation_report.schema.json`.

父仓侧验证：

- targeted paper tests：57 passed
- f5 committed slice evidence tests：24 passed
- changed paper schema JSON parse：PASS
- opencode cumulative diff check：PASS

## 边界

本次 pin 只记录 local/offline 合同硬化和证据矩阵进展。

它不代表：

- 真实 Zotero metadata-only pilot 通过；
- Obsidian、RAG、WriteLab 已接入；
- PDF、附件、全文可读；
- live-ready；
- final acceptance。

## 审核索引

- 变更父仓文件：
  - `D:\devframe-system\BASELINE_LOCK.json`
  - `D:\devframe-system\integration\lock\submodules.lock.yml`
  - `D:\devframe-system\integration\reports\opencode-capability-map-evidence-matrix-return-review-2026-06-15.md`
  - `D:\devframe-system\integration\reports\parent-pin-review-a22-2026-06-15.md`
  - `D:\devframe-system\integration\reports\README.md`
  - `D:\devframe-system\integration\PROJECT_COMPLETENESS_PLAN.md`
  - `D:\devframe-system\dev-frame-opencode` gitlink
- 审核重点：
  - 本轮只 pin committed head `f5b0c80...`，不纳入 dirty WIP。
  - `test-frame` 和 `agent-acceptance` pin 未变。
  - `devframe-control-plane` 仍冻结。
  - blocked Zotero metadata-only 真实尝试仍保持 blocked。
  - offline/local candidate 没被升格成 final ready。
