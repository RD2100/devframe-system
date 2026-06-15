# 父仓 pin 审查 A22

日期：2026-06-15

## 状态

`A22_OPENCODE_CAPABILITY_MAP_PIN_REVIEW_NO_GO_MOVING_DIRTY_HEAD`

父仓已审到 `dev-frame-opencode` A21 后的 capability map 和 business validation
evidence matrix 链条，但本轮不更新 gitlink/lock。

原因：父仓准备 pin `7ffc609...` 时，`dev-frame-opencode` 又前进到
`f5b0c80450aed908ae3cddc578c06962a86ddea7`，并且当前子模块工作树出现未提交修改。
父仓已向 opencode 线程发送 `HOLD-3_FROM_PARENT_CONTROL`，要求暂停继续切片并回传
干净最终 head。

## 候选 pin

- `agent-acceptance`：
  `75f8eb329778d4a8cffb28f6ba79b137038d4fed`
- `dev-frame-opencode`：
  `a1ed82bb06bb42f4ba0bb14c8518988302cd2894`，保持 A21 父仓基线，不更新
- `devframe-control-plane`：
  `79399541b8426cff0f362b665bad09e3c23e974b`
- `test-frame`：
  `c3353fb34900aa24f56df5b9c9230f3249d6c01a`

## 决定

不 pin。

当前父仓 lock 继续保持：

`a1ed82bb06bb42f4ba0bb14c8518988302cd2894`

等待 opencode 返回：

- clean worktree；
- 最终 head；
- 对应 evidence ZIP；
- 测试摘要；
- 不再继续移动的 HOLD 确认。

## 证据

- 已审 A22 候选回传：
  `integration/reports/opencode-capability-map-evidence-matrix-return-review-2026-06-15.md`
- evidence ZIP：
  `D:\devframe-system\.agent\evidence\evidence-opencode-business-validation-capability-map-evidence-matrix-a1-7ffc609.zip`
- evidence ZIP SHA256：
  `15E21DF9CF382308FAA06F74CDB8F62D8D2FBDC16C10F5AD578E67E4C1927E65`
- 新观察到的 superseding head：
  `f5b0c80450aed908ae3cddc578c06962a86ddea7`
- 新 evidence ZIP：
  `D:\devframe-system\.agent\evidence\evidence-opencode-business-validation-capability-map-hash-a1-f5b0c80.zip`
- 新 evidence ZIP SHA256：
  `0B2D7DB7B3FFC5C142C4A1F5799A5FF7788EB0A658EA6B2768185F408732EBB9`
- 当前阻断：
  `dev-frame-opencode` worktree dirty with modified
  `ai-workflow-hub/tests/test_paper_business_capability_validation.py` and
  `schemas/paper_business_validation_report.schema.json`.

父仓侧验证：

- targeted paper tests：57 passed
- changed paper schema JSON parse：PASS
- opencode cumulative diff check：PASS

## 边界

本次审查只记录 local/offline 合同硬化和证据矩阵进展。

它不代表：

- 真实 Zotero metadata-only pilot 通过；
- Obsidian、RAG、WriteLab 已接入；
- PDF、附件、全文可读；
- live-ready；
- final acceptance。

## 审核索引

- 变更父仓文件：
  - `D:\devframe-system\integration\reports\opencode-capability-map-evidence-matrix-return-review-2026-06-15.md`
  - `D:\devframe-system\integration\reports\parent-pin-review-a22-2026-06-15.md`
  - `D:\devframe-system\integration\reports\README.md`
  - `D:\devframe-system\integration\PROJECT_COMPLETENESS_PLAN.md`
- 审核重点：
  - 本轮没有 lock/gitlink 更新。
  - `test-frame` 和 `agent-acceptance` pin 未变。
  - `devframe-control-plane` 仍冻结。
  - blocked Zotero metadata-only 真实尝试仍保持 blocked。
  - offline/local candidate 没被升格成 final ready。
