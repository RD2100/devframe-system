---
name: agent-acceptance
description: SADP governance orchestrator. Use when user says "@go", "@go read", "@go edit", "@go risky", or requests formal task execution with mandatory reviewer evidence. NOT for casual conversation.
---

# agent-acceptance - SADP Governance Orchestrator

Role: orchestrator, not final judge. `@go` manages the workflow pipeline. The final pass requires deterministic guards, an independent reviewer artifact, and CI/human gates where applicable.

## Modes

| Command | Profile | Write Scope | Network | Use Case |
|---------|---------|-------------|---------|----------|
| `@go read` | read-only | none | off | Code review, analysis, audit |
| `@go edit` | ai-dev | project dir, deny secrets | off | Normal feature/bug work |
| `@go risky` | ai-risky | project dir, deny secrets | on | CI changes, deps, deploy config |
| `@go` | ai-dev | project dir, deny secrets | off | Standard formal task |

## Required State Machine

```
human_gate
  -> executor/fixer
  -> tester
  -> reviewer
  -> finalizer
```

The reviewer node is mandatory. A run cannot be marked `passed` without `review.md` and `review.yaml` created by a reviewer role that is separate from the executor/fixer.

## Evidence Contract

Every `@go` run must create a run evidence directory containing:

| File | Producer | Purpose |
|------|----------|---------|
| `diff.patch` | executor/fixer or harness | Real code delta |
| `test-output.md` | tester | Command output and exit codes |
| `safety-report.json` | deterministic guard | Secret/path/scope checks |
| `chain-evidence.json` | orchestrator/harness | Role/session/model chain |
| `review.md` | reviewer only | Human-readable review |
| `review.yaml` | reviewer only | Machine-readable review verdict |
| `final-report.md` | finalizer only | Deterministic summary |

`executor` and `fixer` must not write `review.md` or `review.yaml`.
`finalizer` must not substitute for reviewer judgment.

## Reviewer Rules

The reviewer must:

- Run in a separate session/model identity from the executor/fixer.
- Read `diff.patch`, `test-output.md`, `safety-report.json`, and `chain-evidence.json`.
- Treat executor logs/reports as claims, not facts.
- Produce both `review.md` and `review.yaml`.
- Block if any P0/P1 finding is unresolved.

Minimum `review.yaml`:

```yaml
reviewer_role: reviewer
reviewer_id: "<session-or-agent-id>"
executor_id: "<executor-session-or-agent-id>"
verdict: pass | blocked | fail | escalate
reviewed_inputs:
  - diff.patch
  - test-output.md
  - safety-report.json
  - chain-evidence.json
findings:
  - id: finding-001
    severity: P0 | P1 | P2 | P3
    status: open | resolved | false_positive
    title: "short finding"
```

## Workflow

1. Gate 0: check `AGENTS.md`, rules, mode/profile, and TaskSpec `allow_write`.
2. Executor/fixer: dispatch with `opencode run`; initialize evidence with `python tools/go_evidence.py init <run-dir> --run-id <id> --task .ai/tasks/<id>.yaml --executor-id <session-id>`.
3. Tester: run commands; write `test-output.md`.
4. Guards: run `python tools/go_evidence.py guard <run-dir> --task .ai/tasks/<id>.yaml`; this captures `safety-report.json`.
5. Reviewer: dispatch a separate reviewer session; write `review.md` and `review.yaml`.
6. Finalizer: run `python tools/go_evidence.py finalize <run-dir>`.
7. Verdict: `passed` only if guard, reviewer, and evidence validation all pass.

## Automated Dispatch

```powershell
opencode run -m "deepseek/deepseek-v4-pro" -c "Read .ai/tasks/<id>.yaml, execute, write executor evidence to <run-dir>"
opencode run -m "deepseek/deepseek-v4-pro" -c "Review <run-dir>; write review.md and review.yaml; do not edit code"
opencode run -s <session_id> -c "continue instruction"
```

## P0 Hard Stops

| # | Rule |
|---|------|
| 1 | No destructive git without human approval |
| 2 | No secrets in code, logs, or reports |
| 3 | No command injection or path traversal |
| 4 | No fake green |
| 5 | No write outside TaskSpec `allow_write` |
| 6 | No pass without independent `review.yaml` |
| 7 | No pass with unresolved P0/P1 findings |

## Finalizer Rule

The finalizer is deterministic. It may summarize and validate artifact presence, but it must not make code-quality judgments or override the reviewer. If reviewer evidence is missing or invalid, final status is `blocked`.

Full protocol: `docs/agent-runtime/sub-agent-dispatch-protocol.md`
Policy rules: `.ai/policy.yaml` enforced by `tools/ai_guard.py`
