<p align="center">
  <img src="docs/assets/devframe-system-banner.svg" alt="devframe-system：网页版 AI 外置大脑" width="100%" />
</p>

<h3 align="center">以 GPT Web 为默认入口，也可绑定 DeepSeek、豆包等网页版 AI；用外置大脑低成本提升代码质量并把住研发方向。</h3>

<p align="center">
  <a href="README.md">English</a> | 简体中文
</p>

<p align="center">
  <a href="#它到底独特在哪里">它到底独特在哪里</a> ·
  <a href="#它如何工作">它如何工作</a> ·
  <a href="#你会得到什么">你会得到什么</a> ·
  <a href="#快速上手">快速上手</a>
</p>

<p align="center">
  <img alt="网页版 AI 外置大脑" src="https://img.shields.io/badge/Web%20AI-External%20Brain-1f6feb" />
  <img alt="Focus" src="https://img.shields.io/badge/focus-code%20quality%20%2B%20direction-20c997" />
  <img alt="No new platform" src="https://img.shields.io/badge/no%20new%20platform-required-00a884" />
  <img alt="Agents" src="https://img.shields.io/badge/agents-Codex%20%7C%20Claude%20Code%20%7C%20CLI-6f42c1" />
  <img alt="Cost" src="https://img.shields.io/badge/cost-low%20budget-ffb703" />
  <img alt="Platform" src="https://img.shields.io/badge/platform-Windows%20%7C%20PowerShell-24506b" />
</p>

```text
/rdinit                 # 初始化项目的外置大脑操作层
/bindChrome <url>       # 绑定 GPT Web、DeepSeek、豆包或浏览器 AI URL
```

**真正的问题不是“怎样再做一套治理框架”，而是：怎样在不增加预算、不替换工具链、不训练新模型的情况下，最简单、最直接地提升代码质量，并持续把住产品与工程方向？**

**devframe-system 的答案，是把 GPT Web、DeepSeek、豆包等网页版 AI 变成软件研发的外置大脑：网页 AI 负责理解目标、拆解任务、记忆上下文、校准方向、调度 agent、审查证据和沉淀经验；IDE、CLI、浏览器、自动化脚本、测试框架以及不同厂商的 coding agent 都作为可替换执行器接入。**

---

## 目录

- [devframe-system 是什么？](#devframe-system-是什么)
- [它到底独特在哪里？](#它到底独特在哪里)
- [它如何工作？](#它如何工作)
- [两个技能入口](#两个技能入口)
- [一分钟例子](#一分钟例子)
- [你会得到什么？](#你会得到什么)
- [谁适合使用？](#谁适合使用)
- [架构概览](#架构概览)
- [核心组件](#核心组件)
- [快速上手](#快速上手)
- [具体使用方式](#具体使用方式)
- [把外置大脑系统引导到你的项目](#把外置大脑系统引导到你的项目)
- [状态文档](#状态文档)
- [仓库结构](#仓库结构)
- [许可证](#许可证)

---

## devframe-system 是什么？

devframe-system 是一个**以网页版 AI 为中心的软件质量提升系统**。它先解决最现实的问题：不新增预算、不替换工具链、不训练新模型，只把你已经在用的 GPT Web、DeepSeek、豆包或其他网页版 AI 变成外置大脑，再接入你已经在用的软件、仓库、CLI、浏览器、脚本、测试框架和 coding agent。

它追求的是非常直接的结果：

- 不买新平台，也能提升代码质量；
- 在 agent 开始跑偏前，把产品方向和工程方向拉回视野；
- 让每一次 agent 行动都能靠证据审查，而不是靠信任；
- 把反复踩坑的经验沉淀成可复用的操作记忆。

规则、契约和门禁不是主卖点，而是让这个外置大脑可以安全连接多软件、多 agent 的控制面：

**1. 方向把控** — 被绑定的网页版 AI 在写代码之前持续保留问题、产品意图、取舍和当前上下文。

**2. Agent 调度** — TaskSpec 和 SADP 把模糊需求变成有边界的任务，交给 Codex、Claude Code、CLI 脚本、浏览器自动化或其他执行器。

**3. 质量验证** — ExecutionReport、证据索引、审查门禁和负面测试让代码质量变成可以检查的东西，而不是一句“看起来没问题”。

**4. 可迁移引导** — 规则、契约、验证文档和模板可以通过一条 PowerShell 命令部署到其他仓库。

## 它到底独特在哪里？

多数 AI 编码方案优化的是某一个执行器：一个 IDE 插件、一个 CLI、一个 agent、一个提示词窗口。devframe-system 优化的是它们上方的**思考层**。

| 常见做法 | devframe-system 的做法 |
|---|---|
| 再买或再安装一个编码工具 | 先把 GPT Web、DeepSeek、豆包或其他网页版 AI 变成马上可用的外置大脑 |
| 让 agent “帮我修一下” | 把意图变成 TaskSpec、边界、证据和审查重点 |
| 相信 agent 的最终回答 | 要求 ExecutionReport、验证输出和可审查证据 |
| 每个工具各自保存上下文 | 把方向、决策和经验放在同一个协调大脑里 |
| 最后再补质量检查 | 每轮工作接受前就把质量检查纳入闭环 |

一句话：**GPT 负责思考和协调，工具负责执行，证据决定能不能接受。**

## 它如何工作？

1. **在网页版 AI 会话中校准方向** — 开工前先明确产品目标、约束、验收标准和风险。
2. **把意图转换成 TaskSpec** — 写清任务、允许文件、禁止文件、验证命令和停止条件。
3. **交给最合适的执行器** — Codex、Claude Code、CLI 脚本、浏览器自动化或其他 agent 都可以在同一契约下执行。
4. **收集证据，而不是收集感觉** — 执行器返回改动文件、运行命令、输出、制品和已知缺口。
5. **先审查，再接受** — 用 P0-P3 门禁检查证据，让代码质量、安全和方向都可见。
6. **把经验喂回外置大脑** — 重复踩坑会沉淀成操作记忆，而不是消失在聊天记录里。

## 两个技能入口

真正使用时不应该让人先读完整套文档。整套操作系统应该收敛成两个面向项目的技能入口：

| 技能 | 用来做什么 | agent 能获得什么 |
|---|---|---|
| `/rdinit` | 给一个仓库初始化 devframe-system 外置大脑操作层 | `AGENTS.md`、规则、Schema、工具策略、能力清单、验证文档和 bootstrap 路径 |
| `/bindChrome <url>` | 把 GPT Web、DeepSeek、豆包、项目页面或浏览器 AI URL 绑定到当前项目 | 一个稳定的外置大脑会话，绑定项目注册表、Chrome profile 和本地模块根目录 |

推荐流程：

1. 新项目先运行 `/rdinit`，让项目具备外置大脑工作流。
2. 再运行 `/bindChrome <url>`，把应该作为项目外置大脑的 GPT Web、DeepSeek、豆包或浏览器上下文绑定起来。
3. agent 读取 `AGENTS.md`、`docs/agent-runtime/project-local-skill-bindings.md` 和生成的运行时文档，就能理解完整流程。
4. 之后每轮工作都走 TaskSpec、执行、证据、审查和经验沉淀，而不是临时提示词。

提供商说明：提供商可以替换，治理契约不能替换。被绑定的网页版 AI 必须能稳定保留项目上下文、协调 TaskSpec、审查证据并遵守本地隐私边界。如果某个提供商做不到，就把它当二级审阅器，而不是主外置大脑。

## 一分钟例子

没有 devframe-system：

> “让某个 agent 重构这个模块，希望代码变好，然后人工回头检查它到底改了什么。”

使用 devframe-system：

> “先在 GPT 网页版里明确目标、范围、约束、成功标准和审查重点；再把有边界的 TaskSpec 派发给执行器；只有当 ExecutionReport、验证输出和审查结果证明代码质量提升且没有偏离产品方向时，才接受这轮工作。”

## 你会得到什么？

| 需求 | devframe-system 提供什么 |
|---|---|
| 提升代码质量 | 审查门禁、负面夹具、证据要求和禁止假绿规则 |
| 把控产品与工程方向 | 网页版 AI 规划、TaskSpec 边界和审查重点 |
| 多 agent 协同 | SADP、ExecutionReport、能力清单和文件冲突边界 |
| 低成本落地 | 基于仓库的流程，可接入现有工具和 agent |
| 可复用流程 | Bootstrap 模板、规则、Schema、文档和 runbook 可复制到其他项目 |

## 谁适合使用？

devframe-system 适合已经在用 AI 编码工具，但发现真正昂贵的并不是“写代码”的人。真正昂贵的是：方向有没有跑偏、代码是不是真的变好、上次踩过的坑这次有没有被记住。

适合这些场景：

- 独立开发者想要接近 senior review 的压力，但不想增加团队成本；
- 小团队同时使用多个 agent，经常在工具之间丢上下文；
- 项目负责人需要在代码量膨胀前把住产品方向和工程方向；
- 审查者想看证据包，而不是翻很长的聊天记录；
- agent 工作流构建者需要可迁移的 TaskSpec 和 ExecutionReport 契约。

## 设计理念

系统建立在几个核心原则之上：

- **基于证据的治理**：每一个声明都必须有证据支撑。每一个门禁都必须产出明确的结果。每一个变更都必须可以通过执行前后的 git 状态来验证。"假绿"（将失败报告为通过）是 P0 级硬停止。

- **执行与审批分离**：规划智能体负责规划，执行智能体负责实施，审查者负责审查，终结者负责汇总。任何智能体都不能审批自己的工作——这是结构性强制的，而非依赖信任。

- **先复用再构建（Gate 0）**：在创建任何新内容之前，智能体必须证明现有资源无法满足需求，防止冗余构建。

- **纵深防御**：40 条运行时不变量、46 条规则、30 个负面测试夹具、4 级验证门禁、严格的阶段边界和禁止操作列表，形成多重叠加的保护层。

- **阶段门控演进**：Phase 0-5（当前阶段）是有意设置的严格限制阶段——几乎所有操作都是只读的。能力通过审查者批准后逐步解锁。

- **知识代谢**：运维知识通过 3 层生命周期流转（事件 → 模式 → 原则），配有晋升/降级标准，防止知识流失和规则膨胀（P0 规则上限 7 条）。

## 架构概览

理解价值闭环后再看架构会更清楚：这个仓库是 GPT 网页版外置大脑周围的可迁移操作系统。它保存规则、契约、证据格式、bootstrap 模板和子模块指针，让这套闭环可以在不同项目中重复使用。

```
┌─────────────────────────────────────────────────────────┐
│               devframe-system（超级项目）                 │
│                                                         │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │   rules/    │  │   schemas/   │  │    docs/     │  │
│  │  46 条规则   │  │ 54+ JSON     │  │  agent-      │  │
│  │  7 个领域    │  │  Schema      │  │  runtime/    │  │
│  └─────────────┘  └──────────────┘  └──────────────┘  │
│                                                         │
│  ┌─────────────────────────────────────────────────┐   │
│  │     templates/runtime-bootstrap/bootstrap.ps1    │   │
│  │     一条命令部署到任何项目                          │   │
│  └─────────────────────────────────────────────────┘   │
│                                                         │
│  ┌─────────────────────────────────────────────────┐   │
│  │           子智能体调度协议 (SADP)                  │   │
│  │                                                  │   │
│  │  [Codex 目标智能体] ←──TaskSpec──→ [Claude Code] │   │
│  │        ↑                                    │    │   │
│  │        └────ExecutionReport + 证据──────────┘    │   │
│  │                     ↓                            │   │
│  │              [人类审查者]                          │   │
│  └─────────────────────────────────────────────────┘   │
│                                                         │
│  ┌──────────────────┐  ┌──────────────────────────┐   │
│  │ agent-acceptance │  │ devframe-control-plane   │   │
│  │（治理与验收框架）  │  │（控制平面运行时候选，已冻结）│   │
│  ├──────────────────┤  ├──────────────────────────┤   │
│  │ dev-frame-       │  │ test-frame               │   │
│  │ opencode         │  │（验证运行时与测试编排）      │   │
│  │（工作流/         │  │                          │   │
│  │  RAG 管线）       │  │                          │   │
│  └──────────────────┘  └──────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

### 执行层次

| 层 | 范围 | 触发条件 |
|----|------|---------|
| L0: 冒烟测试 | 7 项基本健康检查 | 会话启动、配置变更 |
| L1: 批次 | 每任务质量批次 | 每次提交、每个 PR |
| L2: 工作队列 | 分级队列执行 | 定时任务、发布前 |
| L3: 并行 | 受控并行队列 | 需要提高吞吐量时 |

### 验证门禁体系

| 级别 | 名称 | 失败结果 | 描述 |
|------|------|---------|------|
| P0 | 安全性 | BLOCKED | 密钥、注入、路径遍历、线程安全——必须通过 |
| P1 | 正确性 | FAILED | 构建、测试、退出码、无回归——必须通过 |
| P2 | 质量 | WARNING | 代码审查、Lint、性能——应当通过 |
| P3 | 完整性 | INFO | 文档、覆盖率、错误处理——最好通过 |

门禁严格按顺序执行：P0 → P1 → P2 → P3。P0 失败永远不能被绕过。

### 退出码契约

| 代码 | 标签 | 含义 |
|------|------|------|
| 0 | PASS | 所有检查通过 |
| 1 | BLOCKED | 无法继续（缺少依赖、环境问题） |
| 2 | FAILED | 检查失败，必须修复 |

## 核心组件

这些是外置大脑工作流背后的实现零件。它们的作用是让方向、执行、证据和审查都可以重复运行。

### 1. 质量护栏（46 条规则，7 个领域）

| 领域 | 规则数 | 核心关注点 |
|------|--------|-----------|
| `rules/core.md` | 8 | Git 安全、密钥、阶段边界、资源复用 |
| `rules/coding.md` | 7 | 错误处理、最小变更、先读后改 |
| `rules/security.md` | 8 | 无密钥、无注入、输入验证、加密 |
| `rules/review.md` | 6 | 无假绿、证据链、审查者分离 |
| `rules/git.md` | 6 | 禁止强推、禁止破坏性操作、干净提交 |
| `rules/research.md` | 5 | 研究中无密钥、行动前先验证 |
| `rules/frontend.md` | 6 | 无 XSS、组件隔离、响应式、可访问性 |

### 2. 集成契约（8 个核心契约）

| 契约 | 用途 |
|------|------|
| **TaskSpec** | 执行前描述一个工作单元 |
| **RunSpec** | 记录任务的执行方式 |
| **EvidenceIndex** | 产出的证据制品索引 |
| **GateResult** | 单个验证门禁的检查结果 |
| **ExecutionReport** | 批次执行的最终结构化报告 |
| **SkillIntakeRecord** | 记录外部技能的接收评估 |
| **ToolRiskRecord** | 记录工具的风险评估 |
| **MemoryUpdateRecord** | 提议的记忆更新（需人类批准） |

### 3. 子智能体调度协议（SADP）

SADP 是多智能体协作的默认开发工作流：

```
用户触发 @go
    ↓
Gate 0: 资源充足性检查（行动前证明缺口）
    ↓
Codex 目标智能体: 分解目标 → TaskSpec
    ↓
Claude Code 执行智能体: 接收 TaskSpec → 执行 → 产出 ExecutionReport
    ↓
审查者（独立身份）: 验证证据 → 发布裁决
    ↓
终结者: 打包制品 → 确定性汇总
```

**强制审查者节点**: 每次变更文件的运行必须经过：`human_gate →
executor/fixer → tester → reviewer → finalizer`。执行者可以实施和报告，
但不能审批自己的工作。

**冲突注册表**: 每个 TaskSpec 声明文件访问范围（read_set, write_set），
以实现安全的并行调度。受保护的文件需要独占锁。

**降级矩阵**: 当调度失败时，按风险等级分类降级方案。
所有级别均禁止静默降级。

### 4. 运行时不变量（40 条不变量，18 个类别）

关键不变量组包括：真实来源完整性、批准输出范围控制、执行前后 git 状态要求、假绿防护、阶段边界执行、记忆写入保护、密钥隔离、危险 git 操作阻断、执行者自我审批防护、命令注入阻断、路径遍历阻断和输入验证。

### 5. 引导部署系统

整套外置大脑操作层可以通过一条 PowerShell 命令部署到任何项目。详见[把外置大脑系统引导到你的项目](#把外置大脑系统引导到你的项目)。

### 6. 负面验收测试

30 个负面测试夹具（NEG-001 到 NEG-030）模拟包含故意违规的报告，审查者必须识别。分布：22 个 blocked（P0 硬停止）、6 个 fail、2 个 warning。覆盖所有审查规则、门禁级别、核心契约和禁止工具类别。

### 7. 知识代谢（经验教训）

通过 3 层生命周期捕获的 10 条运维经验：

- **第 3 层（事件）**：特定事件。3 次事件可晋升为模式。
- **第 2 层（模式）**：反复出现的故障类型。3 次验证可晋升为原则。
- **第 1 层（原则）**：稳定的 P0/P1 强制执行规则。3 次以上误报触发降级。

## 快速上手

最快路径：先读 README 第一屏，再打开 `docs/status/current-delivery.md`，运行其中列出的验证命令，然后查看生成的证据报告。这样可以最快看到核心思路：GPT 负责方向，执行器产出结果，审查用证据说话。

### 前置要求

- Git（支持子模块）
- PowerShell 5.1+（Windows）或 pwsh（跨平台）
- Python 3.8+（用于验证脚本）

### 克隆并初始化

```powershell
git clone --recurse-submodules https://github.com/RD2100/devframe-system.git
cd devframe-system
git submodule status --recursive
```

### 验证仓库

```powershell
# 检查子模块状态
git submodule status --recursive

# 检查工作树是否干净
git status --porcelain=v1 -uall

# 检查空格/格式问题
git diff --check
```

### 运行当前交付物验证

```powershell
# 核心交接验证
python scripts\verify_local_paper_rag_v1_0_handoff.py --root D:\devframe-system
python scripts\verify_local_paper_rag_final_review_v1_1.py --root D:\devframe-system

# 投稿准备验证
python scripts\verify_local_paper_rag_submission_prep_v1_0.py --root D:\devframe-system

# 审稿变体验证
python scripts\verify_local_paper_rag_review_variants_v1_0.py --root D:\devframe-system

# 投稿候选验证
python scripts\verify_local_paper_rag_submission_candidate_v1_2.py --root D:\devframe-system
```

### 探索外置大脑操作层

按顺序阅读核心文档：

1. `docs/agent-runtime/operating-model.md` — 执行层次、分级、生命周期
2. `docs/agent-runtime/integration-contracts.md` — 8 个核心数据契约
3. `docs/agent-runtime/verification-gates.md` — P0-P3 门禁体系
4. `docs/agent-runtime/sub-agent-dispatch-protocol.md` — SADP 工作流
5. `docs/agent-runtime/reviewer-playbook.md` — 10 步确定性审查流程
6. `docs/agent-runtime/lessons-learned.md` — 运维知识库

阅读规则：

- `rules/core.md` — 8 条基础规则（包括 P0 硬停止）
- `rules/security.md` — 8 条安全规则
- `rules/coding.md` — 7 条编码规则
- `rules/review.md` — 6 条审查规则

## 具体使用方式

devframe-system 既可以作为 **参考实现**，也可以作为 **可迁移的运行时套件**。先按你的角色选择入口：

| 如果你是... | 从这里开始 |
|---|---|
| 想判断这个想法值不值得看 | 先读顶部卖点，再读[它到底独特在哪里？](#它到底独特在哪里) |
| 正在审查一次交付 | 打开 `docs/status/current-delivery.md`，验证包，再看 `integration/reports/` |
| 正在运行 agent 工作流 | 编写或审查 `integration/task-specs/` 下的 TaskSpec |
| 想迁移到其他项目 | 先用 `templates/runtime-bootstrap/bootstrap.ps1` 加 `-DryRun` |
| 想扩展系统 | 先检查 `docs/agent-runtime/capability-inventory.md` |

详细使用路径如下：

### 1. 先理解系统，再执行命令

建议从这些轻量入口开始：

1. `README.md` — 项目概览、架构和使用地图。
2. `AGENTS.md` — 当前项目本地运行规则和硬停止。
3. `docs/status/runbook.md` — 安全的只读健康检查和阶段边界。
4. `docs/status/current-delivery.md` — 当前面向审查者的交付物、哈希和验证命令。

当前 Phase 0-5 应把仓库视为治理基线。优先做只读检查、证据审查和 dry run。没有明确人工授权时，不要 push、commit、reset、stash、安装包、修改 MCP 配置，也不要运行 live 外部能力。

### 2. 审计当前超级项目状态

需要快速确认仓库安全状态时，在根目录运行：

```powershell
git status --short --branch
git submodule status --recursive
git diff --check
```

如果需要更完整的只读盘点，按 `docs/status/runbook.md` 执行。Runbook 会列出预期输出、当前阶段门禁、活跃 TaskSpec 和必须触发人工门禁的动作。

### 3. 审查当前交付包

`docs/status/current-delivery.md` 是当前交付入口。它说明审查者应该先打开哪个 artifact package、校验哪个 SHA256、运行哪些验证脚本，以及哪些结论仍然不在本次交付范围内。

典型审查流程：

1. 确认 `docs/status/current-delivery.md` 中的包路径和 SHA256。
2. 只运行该交付物列出的验证命令。
3. 将生成的证据与 `integration/reports/` 下的支持报告交叉核对。
4. 将结论记录为 `pass`、`failed`、`blocked` 或 `human_required`；失败或阻塞不能被包装成通过。

### 4. 用 SADP 管理多智能体协作

涉及派发或多智能体执行时，不要直接发送开放式指令，而是走 Sub-Agent Dispatch Protocol：

1. Goal Agent 写 TaskSpec，明确范围、允许文件、禁止文件、验证命令、回滚方案和硬停止。
2. Executor 只在 TaskSpec 范围内实现，并返回 ExecutionReport。
3. 独立 Reviewer 校验证据、改动文件、测试输出和风险。
4. Finalizer 打包已接受状态，并指向精确 artifact 路径。

核心契约文件：

- `docs/agent-runtime/sub-agent-dispatch-protocol.md`
- `docs/agent-runtime/integration-contracts.md`
- `docs/agent-runtime/reviewer-playbook.md`
- `integration/task-specs/`
- `integration/reports/`

### 5. 把外置大脑套件引导到另一个项目

当其他仓库需要同一套外置大脑操作层时，使用 `templates/runtime-bootstrap/bootstrap.ps1`。务必先 dry run：

```powershell
cd templates\runtime-bootstrap
.\bootstrap.ps1 -ProjectName "my-project" -ProjectRoot "D:\my-project" -DryRun
.\bootstrap.ps1 -ProjectName "my-project" -ProjectRoot "D:\my-project"
```

Bootstrap 会复制规则、Schema、agent-runtime 文档、负面测试夹具和项目本地生成文件。完成后，目标项目会得到自己的 `AGENTS.md`、能力清单、工具策略和治理清单。

### 6. 安全扩展框架

新增规则、契约、验证器或能力时：

1. 先检查 `docs/agent-runtime/capability-inventory.md`；新能力必须注册并通过审查后才能启用。
2. 将改动限制在最小相关区域：`rules/`、`schemas/`、`docs/agent-runtime/`、`templates/` 或 `integration/`。
3. 如果改动影响审查、验证或交付结论，在 `integration/reports/` 下补充或更新证据。
4. 运行最窄的只读检查，证明新增内容内部一致。

### 7. 什么时候必须停止

任何涉及生产数据、密钥、live 外部服务、runtime pilot、安装依赖、git 变更、部署、MCP 配置或大范围重写的动作，都必须先停下并请求人工批准。这不是礼貌约定，而是仓库 P0 安全边界的一部分。

## 把外置大脑系统引导到你的项目

引导部署系统可以通过一条命令将 GPT 网页版外置大脑背后的操作层部署到任何项目：规则、Schema、文档、验证基础设施和项目本地指引。

### 快速开始

```powershell
# 在 devframe-system 仓库中
cd templates\runtime-bootstrap

# 部署到你的项目（先试运行）
.\bootstrap.ps1 -ProjectName "my-project" -ProjectRoot "D:\my-project" -DryRun

# 正式部署
.\bootstrap.ps1 -ProjectName "my-project" -ProjectRoot "D:\my-project"
```

### 参数说明

| 参数 | 默认值 | 描述 |
|------|--------|------|
| `-ProjectName` | 自动检测 | 项目名称（从目录或 git 远程获取） |
| `-ProjectRoot` | 当前目录 | 目标项目根目录 |
| `-Platform` | `Both` | 目标平台：`Claude`、`Codex` 或 `Both` |
| `-Phase` | `0-5` | 阶段标识 |
| `-DryRun` | 关闭 | 预览而不写入文件 |
| `-Force` | 关闭 | 覆盖现有文件 |

### 部署内容

**步骤 1 — 通用资产：**

- 8 个规则文件（7 个领域共 46 条规则）
- 54+ JSON Schema 文件用于契约验证
- 12+ 份 agent-runtime 文档
- 30 个负面测试夹具
- 引导模板（用于重新引导）

**步骤 2 — 项目特定文件（从模板生成）：**

- `AGENTS.md` — 智能体入口，包含快速开始、硬停止、文档地图
- `docs/agent-runtime/capability-inventory.md` — 能力注册表
- `docs/agent-runtime/tool-policy.md` — 阶段感知的工具策略
- `docs/agent-runtime/governance-manifest.md` — 包含 SHA256 哈希的完整性清单

**步骤 3 — 验证：**

- 验证没有未解析的占位符
- 确认能力清单已正确初始化

### 部署后的项目结构

```
your-project/
├── AGENTS.md                          ← 智能体入口
├── rules/                             ← 8 个规则文件
├── schemas/                           ← JSON Schema 验证
├── docs/agent-runtime/                ← 完整治理文档
│   ├── operating-model.md
│   ├── integration-contracts.md
│   ├── verification-gates.md
│   ├── sub-agent-dispatch-protocol.md
│   ├── reviewer-playbook.md
│   ├── capability-inventory.md
│   ├── tool-policy.md
│   ├── governance-manifest.md
│   ├── lessons-learned.md
│   └── negative-test-fixtures/        ← 30 个 JSON 夹具
└── templates/runtime-bootstrap/       ← 用于重新引导
```

---

# 状态文档

GitHub 根目录现在只保留对外产品入口。运行状态、交付报告、风险日志和模块 pin 细节统一收纳在
`docs/status/` 下。

| 需求 | 打开 |
|---|---|
| 当前审查交接 | `docs/status/current-delivery.md` |
| 安全只读检查 | `docs/status/runbook.md` |
| 子模块 pin 摘要 | `docs/status/submodules.md` |
| Bootstrap 结果 | `docs/status/bootstrap-report.md` |
| 完成度矩阵 | `docs/status/completion-matrix.md` |
| 集成状态 | `docs/status/integration-status.md` |
| Paper 功能状态 | `docs/status/paper-feature-status.md` |
| 风险登记表 | `docs/status/risk-register.md` |

# 仓库结构

```text
devframe-system/
├── README.md                 # 默认英文项目入口
├── README.zh-CN.md           # 简体中文项目入口
├── AGENTS.md                 # agent 入口和硬停止规则
├── BASELINE_LOCK.json        # 机器可读的子模块基线
├── docs/
│   ├── agent-runtime/        # 治理契约、门禁和协议
│   ├── assets/               # README 图片资源
│   └── status/               # 交付状态、runbook、风险和报告
├── rules/                    # 可迁移规则集
├── schemas/                  # 运行时契约 JSON Schema
├── templates/                # 可部署到其他项目的 bootstrap 包
├── scripts/                  # 只读检查和打包辅助脚本
├── integration/              # TaskSpec、证据、制品和报告
└── */                        # 已 pin 的子模块工作区
```

# 许可证

This project is proprietary. All rights reserved.
