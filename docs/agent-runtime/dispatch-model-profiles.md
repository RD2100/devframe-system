# Dispatch Model Profiles ¡ª RD2100 Agent Runtime

> 2026-05-28 | Purpose: Document practical limits of each model used in SADP dispatch.
> Update when: New model tested, existing model behavior changes, new failure pattern discovered.

---

## Quick Reference (for agent before dispatch)

| If task involves... | Use | Max files/batch |
|---------------------|-----|:---:|
| **Audit / review tasks** | `deepseek-v4-pro` | 2 (report + 1 source) |
| .md files only, ¡Ü2 files | `deepseek-v4-pro` | 2 |
| .md files, 3-5 files | `deepseek-chat` | 5 |
| .ps1 / .py / code files | `deepseek-chat` or Codex direct | 1 |
| 6+ files of any type | Codex direct (grep/shell) | ¡ª |
| Tool-heavy operations (init, create) | Skip dispatch, Codex direct | ¡ª |

**Audit dispatch**: Always use `deepseek-v4-pro --model deepseek/deepseek-v4-pro`. Audits read only the report + at most 1 source file for cross-check. Audit quality > speed.

---

## deepseek/deepseek-v4-pro

- **Provider**: DeepSeek (your API key)
- **Cost**: ~£¤0.00016/simple task
- **Strengths**: Fast simple replies, concise output, low cost
- **Limitations**:
  - ? Max 2 `.md` files per dispatch (tool-call timeout ~15s)
  - ? Cannot handle `.ps1`/`.py` (Read tool times out on files >100 lines)
  - ? Multi-file prompts (3+) hang at 30s
  - ? `agent create` tool hangs indefinitely
  - ? `--add-dir` flag not supported by `opencode run`
- **Full pass rate**: 4/8 tasks (50%) ¡ª file size sensitive
- **Best for**: Quick single-file reads, simple code generation, "say hi" validation

## deepseek/deepseek-chat

- **Provider**: DeepSeek (your API key)
- **Cost**: ~£¤0.002/task (10x v4-pro but more capable)
- **Strengths**: Handles .ps1 files, multi-file prompts, tool calling
- **Limitations**:
  - ?? Higher cost per task
  - ?? Slower responses (15-20s vs v4-pro 5-10s)
- **Full pass rate**: 5/5 tasks (100%)
- **Best for**: Multi-file audits, code file reading, complex tool operations

## opencode build agent

- **Permissions**: bash, read, edit, glob, grep, webfetch, task, todowrite, websearch, lsp, skill
- **Limitations**:
  - ? No `--add-dir` support in `opencode run`
  - ? `agent create` hangs (generates config via model call)
  - ?? Filesystem access requires explicit absolute paths
  - ?? Desktop app conflicts with CLI dispatch (process lock)

## Codex Goal Agent (direct)

- **Strengths**: Native file reading, grep, shell, no tool-call timeout
- **Best for**: Large file audits, batch operations, PS1/Python analysis
- **SADP role**: Planning, evaluation, and tasks exceeding dispatch model limits

---

## Failure Pattern Library

| Pattern | Symptom | Models affected | Mitigation |
|---------|---------|:---:|------------|
| Desktop app conflict | All dispatches 30s timeout | All | Close opencode desktop before CLI dispatch |
| PS1 file timeout | No output, 30s wall time | v4-pro | Use chat model or Codex direct |
| Multi-file overload | 3+ files ¡ú hang | v4-pro | Limit to 2 files/batch |
| Tool creation hang | "Generating..." endless loop | v4-pro | Skip `agent create`, use `build` |
| Large prompt | No output, immediate timeout | v4-pro | Keep prompt <500 chars, files <5KB |

---

> **Update log**: 2026-05-28 ¡ª Initial profile from SADP debugging session (6 failure patterns, 2 models)
