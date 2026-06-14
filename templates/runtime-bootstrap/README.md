# RD2100 Agent Runtime -- Bootstrap Template

> Version: 1.0 | Requires: PowerShell 5.1+, git
> Target: Any project needing Agent Runtime governance (Claude Code / Codex / Both)

## What This Is

A one-command bootstrap that initializes the RD2100 Agent Runtime governance framework in any project. Copies universal assets (rules, schemas, reviewer docs) and generates project-specific files (AGENTS.md, capability inventory, tool policy) from templates.

## What You Get

| Asset | Type | Count |
|-------|------|:---:|
| Rules | Copied (universal) | 8 files, 44 rules |
| Schemas | Copied (universal) | 18 JSON Schema files |
| AGENTS.md | Generated | 1 file |
| Capability Inventory | Generated | 10 universal + N project-specific |
| Tool Policy | Generated | 1 file |
| Reviewer Docs | Copied (universal) | 5 files |
| Negative Test Fixtures | Copied (universal) | 30 fixtures |

## Quick Start

```powershell
# In project root (auto-detect):
.\templates\runtime-bootstrap\bootstrap.ps1

# Explicit params:
.\bootstrap.ps1 -ProjectName "my-app" -ProjectRoot "D:\my-app" -Platform Both

# Dry-run:
.\bootstrap.ps1 -DryRun
```

## Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| -ProjectName | Auto-detected | Project name |
| -ProjectRoot | Current dir | Absolute project root |
| -Platform | Both | Claude / Codex / Both |
| -Phase | 0-5 | Phase designation |
| -DryRun | false | Preview only |
| -Force | false | Overwrite existing |

## Template Files

| Template | Placeholders | Generates |
|----------|-------------|-----------|
| AGENTS.template.md | {{PROJECT_NAME}}, {{PROJECT_ROOT}}, {{CURRENT_DATE}}, {{GIT_REMOTE}}, {{PHASE}}, {{PLATFORM}} | AGENTS.md |
| capability-inventory.template.md | {{PROJECT_NAME}}, {{CURRENT_DATE}}, {{PHASE}} | capability-inventory.md |
| tool-policy.template.md | {{PROJECT_NAME}}, {{PROJECT_ROOT}}, {{PHASE}} | tool-policy.md |