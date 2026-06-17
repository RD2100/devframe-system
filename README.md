<p align="center">
  <img src="docs/assets/devframe-system-banner.svg" alt="devframe-system: web AI as an external brain" width="100%" />
</p>

<h3 align="center">Use GPT Web first, or bind another capable web AI, as an external brain to raise code quality and keep engineering direction on track.</h3>

<p align="center">
  English | <a href="README.zh-CN.md">简体中文</a>
</p>

<p align="center">
  <a href="#why-it-is-different">Why different</a> ·
  <a href="#how-it-works">How it works</a> ·
  <a href="#what-you-get">What you get</a> ·
  <a href="#getting-started">Quick start</a>
</p>

<p align="center">
  <img alt="Web AI Brain" src="https://img.shields.io/badge/Web%20AI-External%20Brain-1f6feb" />
  <img alt="Focus" src="https://img.shields.io/badge/focus-code%20quality%20%2B%20direction-20c997" />
  <img alt="No new platform" src="https://img.shields.io/badge/no%20new%20platform-required-00a884" />
  <img alt="Agents" src="https://img.shields.io/badge/agents-Codex%20%7C%20Claude%20Code%20%7C%20CLI-6f42c1" />
  <img alt="Cost" src="https://img.shields.io/badge/cost-low%20budget-ffb703" />
  <img alt="Platform" src="https://img.shields.io/badge/platform-Windows%20%7C%20PowerShell-24506b" />
</p>

```text
/rdinit                 # initialize a project with the external-brain operating layer
/bindChrome <url>       # bind a GPT Web, DeepSeek, Doubao, or browser AI URL as the project brain session
```

**The real question is not how to build another governance framework. It is how to improve code quality and direction control with the least cost, the fewest new tools, and the most direct workflow. devframe-system answers by turning a low-cost web AI session into an external brain for software development while every IDE, CLI, browser, script, test runner, and coding agent becomes an interchangeable executor. GPT Web is the default example, but DeepSeek, Doubao, or another browser-accessible AI can play the same coordinating role.**

---

## Table of Contents

- [What is devframe-system?](#what-is-devframe-system)
- [Why It Is Different](#why-it-is-different)
- [How It Works](#how-it-works)
- [Two Skill Entrypoints](#two-skill-entrypoints)
- [One-Minute Example](#one-minute-example)
- [What You Get](#what-you-get)
- [Who Should Use This](#who-should-use-this)
- [Architecture Overview](#architecture-overview)
- [Core Components](#core-components)
- [Getting Started](#getting-started)
- [How to Use This Repository](#how-to-use-this-repository)
- [Bootstrap the External-Brain System into Your Project](#bootstrap-the-external-brain-system-into-your-project)
- [Status Documents](#status-documents)
- [Repository Layout](#repository-layout)
- [License](#license)

---

## What is devframe-system?

devframe-system is a **web-AI-centered software quality system**. It starts
from a practical promise: use the web AI session you already have as an external
brain, then connect it to the software, repositories, CLIs, browsers, scripts,
test runners, and coding agents you already use. GPT Web is the default
reference path; DeepSeek, Doubao, or another browser-accessible AI can be bound
the same way when it can hold project context and coordinate work.

The goal is direct and concrete:

- improve code quality without buying a new platform;
- keep product and engineering direction visible before agents drift;
- make every agent action reviewable through evidence, not trust;
- turn repeated lessons into reusable operating memory.

The governance pieces are not the main attraction. They are the control surface
that lets the external brain work safely across many tools:

**1. Direction Control** — the bound web AI session keeps the problem, product
intent, tradeoffs, and current context in view before code is written.

**2. Agent Dispatch** — TaskSpec and SADP turn vague requests into bounded work
for Codex, Claude Code, CLI scripts, browser automation, or other executors.

**3. Quality Verification** — ExecutionReport, evidence indexes, review gates,
and negative tests make code quality measurable instead of rhetorical.

**4. Portable Bootstrap** — Rules, contracts, verification docs, and templates
can be deployed into another repository with one PowerShell command.

## Why It Is Different

Most AI coding setups optimize for a single executor: one IDE plugin, one CLI,
one agent, one prompt window. devframe-system optimizes for **the thinking layer
above them**.

| Common approach | devframe-system approach |
|---|---|
| Buy or install another coding tool | Use GPT Web, DeepSeek, Doubao, or another web AI as the external brain you can start with immediately |
| Ask an agent to "fix this" | Turn intent into TaskSpec, boundaries, evidence, and review focus |
| Trust the agent's final answer | Require ExecutionReport, verification output, and reviewer-readable evidence |
| Let each tool keep its own context | Keep direction, decisions, and lessons in one coordinating brain |
| Treat quality as a final cleanup step | Make quality checks part of every loop before work is accepted |

The result is a simple mental model: **GPT thinks and coordinates; tools execute;
evidence decides whether the work is accepted.**

## How It Works

1. **Set direction in the web AI session** — clarify the product goal, constraints,
   acceptance criteria, and risk before any executor starts changing files.
2. **Convert intent into a TaskSpec** — describe the exact task, allowed files,
   forbidden files, verification commands, and stop conditions.
3. **Send work to the best executor** — Codex, Claude Code, a CLI script, browser
   automation, or another agent can implement within the same contract.
4. **Collect evidence, not vibes** — the executor returns changed files, commands
   run, outputs, artifacts, and known gaps in an ExecutionReport.
5. **Review before accepting** — evidence is checked against P0-P3 gates so code
   quality, safety, and direction are visible.
6. **Feed lessons back into the brain** — repeated failures become operating
   memory instead of disappearing into chat history.

## Two Skill Entrypoints

The repository should feel simple at the point of use. The complete operating
system collapses into two project-facing skills:

| Skill | Use it for | What it gives the agent |
|---|---|---|
| `/rdinit` | Initialize a repository with the devframe-system operating layer | `AGENTS.md`, rules, schemas, tool policy, capability inventory, verification docs, and bootstrap paths |
| `/bindChrome <url>` | Bind a GPT Web, DeepSeek, Doubao, project page, or browser AI URL to the current project | A stable external-brain session tied to the project registry, Chrome profile, and local module roots |

Recommended flow:

1. Run `/rdinit` when a project needs the external-brain workflow.
2. Run `/bindChrome <url>` to bind the GPT Web, DeepSeek, Doubao, or browser
   context that should act as the project's external brain.
3. The agent reads `AGENTS.md`,
   `docs/agent-runtime/project-local-skill-bindings.md`, and the generated
   runtime docs to understand the complete process.
4. From that point on, work moves through TaskSpec, execution, evidence,
   review, and lessons learned instead of ad hoc prompting.

Provider note: the provider is replaceable; the governance contract is not. The
bound web AI must preserve context, coordinate TaskSpecs, review evidence, and
respect local privacy boundaries. If a provider cannot reliably do that for a
project, use it as a secondary reviewer rather than the primary external brain.

## One-Minute Example

Without devframe-system:

> "Ask an agent to refactor this module. Hope the code is better. Manually check
> what changed afterward."

With devframe-system:

> "Use the bound web AI session to define the goal, scope, constraints, success
> criteria, and review focus. Dispatch the bounded TaskSpec to an executor.
> Accept the work only when the ExecutionReport, verification output, and
> reviewer checks prove that code quality improved without drifting from the
> product direction."

## What You Get

| Need | What devframe-system provides |
|---|---|
| Better code quality | Review gates, negative fixtures, evidence requirements, and no-fake-green rules |
| Better direction control | Web-AI-centered planning, TaskSpec boundaries, and reviewer focus |
| Multi-agent coordination | SADP, ExecutionReport, capability inventory, and conflict-aware file scopes |
| Low-cost adoption | A repository-based workflow that works with existing tools and agents |
| Reusable process | Bootstrap templates, rules, schemas, docs, and runbooks you can copy into another project |

## Who Should Use This

devframe-system is useful when you already use AI coding tools, but still feel
the expensive part is not typing code. The expensive part is keeping the work
pointed at the right problem, checking whether the code is actually better, and
remembering what went wrong last time.

Use it if you are:

- a solo builder who wants senior-review pressure without hiring a team;
- a small team using several agents and losing context between them;
- a project owner who needs direction control before code volume explodes;
- a reviewer who wants evidence packages instead of long chat transcripts;
- an agent-workflow builder looking for portable TaskSpec and ExecutionReport
  contracts.

## Design Philosophy

The system is built on several core principles:

- **Evidence-Based Governance**: Every claim must have evidence. Every gate must
  produce an explicit result. Every change must be verifiable via pre/post git
  status. "No fake green" (reporting failures as passes) is a P0 hard stop.

- **Separation of Execution and Approval**: The plan agent plans, the execute
  agent implements, the reviewer reviews, the finalizer summarizes. No agent can
  approve its own work — this is enforced structurally, not by trust.

- **Reuse Before Build (Gate 0)**: Before creating anything new, agents must
  prove that existing resources do not already cover the need, preventing
  redundant construction.

- **Defense in Depth**: 40 runtime invariants, 46 rules, 30 negative test
  fixtures, 4-level verification gates, strict phase boundaries, and forbidden
  action lists create overlapping protection layers.

- **Phase-Gated Evolution**: Phase 0-5 (current) is intentionally restrictive —
  almost everything is read-only. Capabilities are progressively unlocked through
  reviewer approval.

- **Knowledge Metabolism**: Operational knowledge flows through a 3-tier
  lifecycle (Incident → Pattern → Principle) with promotion/demotion criteria,
  preventing both knowledge loss and rule inflation (P0 rules capped at 7).

## Architecture Overview

Read the architecture after the value loop is clear: this repository is the
portable operating system around the GPT-web external brain. It stores the
rules, contracts, evidence formats, bootstrap templates, and submodule pins that
make the loop repeatable across projects.

```
┌─────────────────────────────────────────────────────────┐
│                  devframe-system (Superproject)          │
│                                                         │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │   rules/    │  │   schemas/   │  │    docs/     │  │
│  │  46 rules   │  │ 54+ JSON     │  │  agent-      │  │
│  │  7 domains  │  │  Schemas     │  │  runtime/    │  │
│  └─────────────┘  └──────────────┘  └──────────────┘  │
│                                                         │
│  ┌─────────────────────────────────────────────────┐   │
│  │     templates/runtime-bootstrap/bootstrap.ps1    │   │
│  │     One-command deployment to any project        │   │
│  └─────────────────────────────────────────────────┘   │
│                                                         │
│  ┌─────────────────────────────────────────────────┐   │
│  │           Sub-Agent Dispatch Protocol            │   │
│  │                                                  │   │
│  │  [Codex Goal Agent] ←──TaskSpec──→ [Claude Code]│   │
│  │        ↑                                    │    │   │
│  │        └────ExecutionReport + Evidence──────┘    │   │
│  │                     ↓                            │   │
│  │              [Human Reviewer]                    │   │
│  └─────────────────────────────────────────────────┘   │
│                                                         │
│  ┌──────────────────┐  ┌──────────────────────────┐   │
│  │ agent-acceptance │  │ devframe-control-plane   │   │
│  │ (Governance/     │  │ (Control-plane runtime   │   │
│  │  SADP gates)     │  │  candidate, frozen)      │   │
│  ├──────────────────┤  ├──────────────────────────┤   │
│  │ dev-frame-       │  │ test-frame               │   │
│  │ opencode         │  │ (Verification runtime    │   │
│  │ (Workflow/       │  │  & test orchestration)   │   │
│  │  RAG pipeline)   │  │                          │   │
│  └──────────────────┘  └──────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

### Execution Layers

| Layer | Scope | Trigger |
|-------|-------|---------|
| L0: Smoke | 7 basic health checks | Session start, config change |
| L1: Batch | Per-task quality batch | Per-commit, per-PR |
| L2: WorkQueue | Tier-graded queue execution | Scheduled, pre-release |
| L3: Parallel | Controlled parallel queues | When throughput needed |

### Verification Gate Hierarchy

| Level | Name | Failure Result | Description |
|-------|------|---------------|-------------|
| P0 | Security | BLOCKED | Secrets, injection, traversal, thread safety — must pass |
| P1 | Correctness | FAILED | Build, tests, exit codes, no regression — must pass |
| P2 | Quality | WARNING | Code review, lint, performance — should pass |
| P3 | Completeness | INFO | Documentation, coverage, error handling — nice to have |

Gates execute in strict order: P0 → P1 → P2 → P3. P0 failures can never be
bypassed.

### Exit Code Contract

| Code | Label | Meaning |
|------|-------|---------|
| 0 | PASS | All checks passed |
| 1 | BLOCKED | Cannot proceed (missing dependency, env issue) |
| 2 | FAILED | Check failed, must fix |

## Core Components

These are the implementation pieces behind the external-brain workflow. They
exist to make direction, execution, evidence, and review repeatable.

### 1. Quality Guardrails (46 rules, 7 domains)

| Domain | Rules | Key Focus |
|--------|-------|-----------|
| `rules/core.md` | 8 | Git safety, secrets, phase boundaries, resource reuse |
| `rules/coding.md` | 7 | Error handling, minimal changes, read-before-edit |
| `rules/security.md` | 8 | No secrets, no injection, input validation, encryption |
| `rules/review.md` | 6 | No fake green, evidence chains, reviewer separation |
| `rules/git.md` | 6 | No force push, no destructive ops, clean commits |
| `rules/research.md` | 5 | No secrets in research, verify before acting |
| `rules/frontend.md` | 6 | No XSS, component isolation, responsive, accessible |

### 2. Integration Contracts (8 core contracts)

| Contract | Purpose |
|----------|---------|
| **TaskSpec** | Describes a unit of work before execution |
| **RunSpec** | Records how a task was executed |
| **EvidenceIndex** | Index of evidence artifacts produced |
| **GateResult** | Result of a single verification gate check |
| **ExecutionReport** | Final structured report of batch execution |
| **SkillIntakeRecord** | Records intake evaluation of external skills |
| **ToolRiskRecord** | Records risk assessment of tools |
| **MemoryUpdateRecord** | Proposed memory updates (human-approved) |

### 3. Sub-Agent Dispatch Protocol (SADP)

SADP is the default development workflow for multi-agent collaboration:

```
User triggers @go
    ↓
Gate 0: Resource Sufficiency Check (prove gap before action)
    ↓
Codex Goal Agent: Decomposes goal → TaskSpecs
    ↓
Claude Code Agent: Receives TaskSpec → Executes → Produces ExecutionReport
    ↓
Reviewer (separate identity): Validates evidence → Issues verdict
    ↓
Finalizer: Packages artifacts → Deterministic summary
```

**Mandatory Reviewer Node**: Every run that changes files must pass through:
`human_gate → executor/fixer → tester → reviewer → finalizer`. The executor
may implement and report, but cannot approve its own work.

**Conflict Registry**: Each TaskSpec declares file access scope (read_set,
write_set) for safe parallel dispatch. Protected files require exclusive locks.

**Fallback Matrix**: When dispatch fails, fallback is classified by risk level.
Silent fallback is forbidden at all levels.

### 4. Runtime Invariants (40 invariants, 18 categories)

Key invariant groups include: source-of-truth integrity, approved output
containment, pre/post git status requirements, fake-green prevention, phase
boundary enforcement, memory write protection, secret isolation, dangerous git
operation blocking, executor self-approval prevention, command injection
blocking, path traversal blocking, and input validation.

### 5. Bootstrap System

The external-brain operating system can be deployed to any project with a single
PowerShell command. See [Bootstrap the External-Brain System into Your
Project](#bootstrap-the-external-brain-system-into-your-project).

### 6. Negative Acceptance Tests

30 negative test fixtures (NEG-001 through NEG-030) simulate reports with
deliberate violations that the reviewer must catch. Distribution: 22 blocked
(P0 hard stops), 6 fail, 2 warning. Coverage spans all review rules, gate
levels, core contracts, and forbidden tool categories.

### 7. Knowledge Metabolism (Lessons Learned)

10 operational lessons captured through a 3-tier lifecycle:

- **Tier 3 (Incident)**: Specific event. 3 incidents promote to pattern.
- **Tier 2 (Pattern)**: Recurring failure type. 3 validations promote to
  principle.
- **Tier 1 (Principle)**: Stable rule with P0/P1 enforcement. 3+ false
  positives trigger downgrade.

## Getting Started

Fastest path: read the first screen, open `docs/status/current-delivery.md`, run the listed
verification command, and inspect the evidence report. That shows the core idea
in practice: GPT-centered direction, executor output, and reviewer evidence.

### Prerequisites

- Git (with submodule support)
- PowerShell 5.1+ (Windows) or pwsh (cross-platform)
- Python 3.8+ (for verification scripts)

### Clone and Initialize

```powershell
git clone --recurse-submodules https://github.com/RD2100/devframe-system.git
cd devframe-system
git submodule status --recursive
```

### Verify the Repository

```powershell
# Check submodule status
git submodule status --recursive

# Check working tree is clean
git status --porcelain=v1 -uall

# Check for whitespace/formatting issues
git diff --check
```

### Run Current Delivery Verification

```powershell
# Core handoff verification
python scripts\verify_local_paper_rag_v1_0_handoff.py --root D:\devframe-system
python scripts\verify_local_paper_rag_final_review_v1_1.py --root D:\devframe-system

# Submission-prep verification
python scripts\verify_local_paper_rag_submission_prep_v1_0.py --root D:\devframe-system

# Review-variants verification
python scripts\verify_local_paper_rag_review_variants_v1_0.py --root D:\devframe-system

# Submission-candidate verification
python scripts\verify_local_paper_rag_submission_candidate_v1_2.py --root D:\devframe-system
```

### Explore the External-Brain Operating Layer

Read the core documentation in order:

1. `docs/agent-runtime/operating-model.md` — Execution layers, tiers, lifecycle
2. `docs/agent-runtime/integration-contracts.md` — 8 core data contracts
3. `docs/agent-runtime/verification-gates.md` — P0-P3 gate hierarchy
4. `docs/agent-runtime/sub-agent-dispatch-protocol.md` — SADP workflow
5. `docs/agent-runtime/reviewer-playbook.md` — 10-step deterministic review
6. `docs/agent-runtime/lessons-learned.md` — Operational knowledge

Read the rules:

- `rules/core.md` — 8 foundational rules (including the P0 hard stops)
- `rules/security.md` — 8 security rules
- `rules/coding.md` — 7 coding rules
- `rules/review.md` — 6 review rules

## How to Use This Repository

Use devframe-system as both a **reference implementation** and a **portable
runtime kit**. Pick the workflow that matches your role:

| If you are... | Start here |
|---|---|
| Evaluating the idea | Read the hero, then [Why It Is Different](#why-it-is-different) |
| Reviewing a delivery | Open `docs/status/current-delivery.md`, verify the package, then inspect `integration/reports/` |
| Running an agent workflow | Write or review a TaskSpec under `integration/task-specs/` |
| Porting the system elsewhere | Use `templates/runtime-bootstrap/bootstrap.ps1` with `-DryRun` first |
| Extending the system | Check `docs/agent-runtime/capability-inventory.md` before adding capabilities |

The detailed workflows are:

### 1. Understand the System Before Running Anything

Start from the lightweight entry points:

1. `README.md` — project overview, architecture, and usage map.
2. `AGENTS.md` — active project-local operating instructions and hard stops.
3. `docs/status/runbook.md` — safe read-only health checks and phase boundaries.
4. `docs/status/current-delivery.md` — current reviewer-facing deliverables and their
   verification commands.

In Phase 0-5, treat the repository as a governance baseline. Prefer read-only
inspection, evidence review, and dry runs. Do not push, commit, reset, stash,
install packages, change MCP configuration, or run live external capabilities
without explicit human authorization.

### 2. Audit the Current Superproject State

Run these checks from the repository root when you need a quick safety snapshot:

```powershell
git status --short --branch
git submodule status --recursive
git diff --check
```

For a fuller read-only inventory, follow `docs/status/runbook.md`. The runbook lists the
expected outputs, current phase gates, active TaskSpecs, and human-gate triggers.

### 3. Review a Current Delivery Package

Use `docs/status/current-delivery.md` as the active handoff index. It tells reviewers which
artifact package to open first, which hashes to verify, which scripts correspond
to the current delivery, and which claims are intentionally out of scope.

Typical review flow:

1. Confirm the package path and SHA256 in `docs/status/current-delivery.md`.
2. Run only the listed verification command for that package.
3. Compare produced evidence with the supporting reports under
   `integration/reports/`.
4. Record the verdict as `pass`, `failed`, `blocked`, or `human_required`; never
   turn a failed or blocked check into a pass.

### 4. Use SADP for Multi-Agent Work

For delegated work, follow the Sub-Agent Dispatch Protocol instead of sending
free-form instructions:

1. The goal agent writes a TaskSpec with scope, allowed files, forbidden files,
   verification commands, rollback plan, and hard-stop rules.
2. The executor implements only the TaskSpec scope and returns an ExecutionReport.
3. A separate reviewer validates evidence, changed files, test output, and risk.
4. A finalizer packages the accepted state and points to exact artifacts.

The core contract files are:

- `docs/agent-runtime/sub-agent-dispatch-protocol.md`
- `docs/agent-runtime/integration-contracts.md`
- `docs/agent-runtime/reviewer-playbook.md`
- `integration/task-specs/`
- `integration/reports/`

### 5. Bootstrap the External-Brain Kit into Another Project

Use `templates/runtime-bootstrap/bootstrap.ps1` when another repository needs the
same external-brain operating layer. Always dry-run first:

```powershell
cd templates\runtime-bootstrap
.\bootstrap.ps1 -ProjectName "my-project" -ProjectRoot "D:\my-project" -DryRun
.\bootstrap.ps1 -ProjectName "my-project" -ProjectRoot "D:\my-project"
```

The bootstrap copies the rules, schemas, agent-runtime documentation, negative
fixtures, and generated project-local files. After bootstrap, the target project
gets its own `AGENTS.md`, capability inventory, tool policy, and governance
manifest.

### 6. Extend the Framework Safely

When adding a new rule, contract, verifier, or capability:

1. Check `docs/agent-runtime/capability-inventory.md` first; new capabilities
   need inventory registration and reviewer approval before use.
2. Keep the change in the smallest relevant area: `rules/`, `schemas/`,
   `docs/agent-runtime/`, `templates/`, or `integration/`.
3. Add or update evidence under `integration/reports/` when the change affects
   review, verification, or delivery claims.
4. Run the narrowest read-only checks that prove the new material is internally
   consistent.

### 7. Know When to Stop

Stop and ask for human approval before any action involving production data,
secrets, live external services, runtime pilots, package installation, git
mutation, deployment, MCP configuration, or broad repository rewrites. These are
not etiquette rules; they are part of the repository's P0 safety boundary.

## Bootstrap the External-Brain System into Your Project

The bootstrap system deploys the practical operating layer behind the GPT-web
external brain: rules, schemas, documentation, verification infrastructure, and
project-local guidance.

### Quick Start

```powershell
# From the devframe-system repository
cd templates\runtime-bootstrap

# Deploy to your project (dry run first)
.\bootstrap.ps1 -ProjectName "my-project" -ProjectRoot "D:\my-project" -DryRun

# Actual deployment
.\bootstrap.ps1 -ProjectName "my-project" -ProjectRoot "D:\my-project"
```

### Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `-ProjectName` | Auto-detected | Project name (from directory or git remote) |
| `-ProjectRoot` | Current directory | Target project root |
| `-Platform` | `Both` | Target platform: `Claude`, `Codex`, or `Both` |
| `-Phase` | `0-5` | Phase designation |
| `-DryRun` | Off | Preview without writing files |
| `-Force` | Off | Overwrite existing files |

### What Gets Deployed

**Step 1 — Universal Assets:**

- 8 rule files (46 rules across 7 domains)
- 54+ JSON Schema files for contract validation
- 12+ agent-runtime documentation files
- 30 negative test fixtures
- Bootstrap templates for re-bootstrapping

**Step 2 — Project-Specific Files (generated from templates):**

- `AGENTS.md` — Agent entry point with Quick Start, Hard Stops, Document Map
- `docs/agent-runtime/capability-inventory.md` — Capability registry
- `docs/agent-runtime/tool-policy.md` — Phase-aware tool policy
- `docs/agent-runtime/governance-manifest.md` — Integrity manifest with SHA256
  hashes

**Step 3 — Verification:**

- Validates no unresolved placeholders remain
- Confirms capability inventory is properly initialized

### After Bootstrap

After running bootstrap, your project will have:

```
your-project/
├── AGENTS.md                          ← Agent entry point
├── rules/                             ← 8 rule files
├── schemas/                           ← JSON Schema validation
├── docs/agent-runtime/                ← Full governance documentation
│   ├── operating-model.md
│   ├── integration-contracts.md
│   ├── verification-gates.md
│   ├── sub-agent-dispatch-protocol.md
│   ├── reviewer-playbook.md
│   ├── capability-inventory.md
│   ├── tool-policy.md
│   ├── governance-manifest.md
│   ├── lessons-learned.md
│   └── negative-test-fixtures/        ← 30 JSON fixtures
└── templates/runtime-bootstrap/       ← For re-bootstrapping
```

---

# Status Documents

The GitHub root is intentionally kept as the public product entry. Operational
state, delivery reports, risk logs, and module pin details live under
`docs/status/`.

| Need | Open |
|---|---|
| Current reviewer handoff | `docs/status/current-delivery.md` |
| Safe read-only checks | `docs/status/runbook.md` |
| Submodule pin summary | `docs/status/submodules.md` |
| Bootstrap result | `docs/status/bootstrap-report.md` |
| Completion matrix | `docs/status/completion-matrix.md` |
| Integration status | `docs/status/integration-status.md` |
| Paper feature status | `docs/status/paper-feature-status.md` |
| Risk register | `docs/status/risk-register.md` |

# Repository Layout

```text
devframe-system/
├── README.md                 # default English project entry
├── README.zh-CN.md           # Simplified Chinese project entry
├── AGENTS.md                 # agent entrypoint and hard-stop rules
├── BASELINE_LOCK.json        # machine-readable submodule baseline
├── docs/
│   ├── agent-runtime/        # governance contracts, gates, and protocols
│   ├── assets/               # README artwork
│   └── status/               # delivery state, runbooks, risks, and reports
├── rules/                    # portable rule set
├── schemas/                  # JSON Schemas for runtime contracts
├── templates/                # bootstrap package for other projects
├── scripts/                  # read-only checks and packaging helpers
├── integration/              # task specs, evidence, artifacts, and reports
└── */                        # pinned submodule workspaces
```

# License

This project is proprietary. All rights reserved.
