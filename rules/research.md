# Research Rules -- RD2100 Agent Runtime v2

> Domain: read-only exploration and code intelligence
> Phase 0-5: P0/P1 active; P2-P4 within approved task scope

---

## RULE research-001: No Secrets in Research

- **Priority**: P0 (Hard Stop)
- **Trigger**: Any read operation
- **Scope**: All phases
- **Rule**: Do not read `.env`, `*.key`, `*.pem`, token files, SSH keys, credential stores, or browser profiles during research. If a search result would include secret content, skip that file.
- **Verification**: Research log shows no access to forbidden file patterns.
- **Conflict Handling**: If research requires checking configuration that might contain secrets, use `test -f` (existence only) instead of reading contents.

---

## RULE research-002: Prefer CodeGraph Over Raw Search

- **Priority**: P2 (Evidence)
- **Trigger**: Need to find symbols, callers, callees, or explore code structure
- **Scope**: Indexed projects (dev-frame: 410 files, test-frame: 102 files)
- **Rule**: Use `codegraph_context` as primary exploration tool. Use `codegraph_search` for symbol lookup. Use `codegraph_explore` for area surveys. Fall back to Grep/Read only when CodeGraph is unavailable or index is empty.
- **Verification**: Tool use log shows CodeGraph calls before Grep/Read for code exploration.
- **Conflict Handling**: If CodeGraph index is empty (agent-acceptance: 0 files), use Grep/Read directly.

---

## RULE research-003: Verify Before Acting on Findings

- **Priority**: P2 (Evidence)
- **Trigger**: Research finding that would change a decision or action
- **Scope**: All phases
- **Rule**: Verify key findings with a second source. "The code says X" -> confirm with a direct Read of the relevant lines. "The file exists" -> confirm with `test -f`.
- **Verification**: Decision log shows evidence chain for consequential findings.
- **Conflict Handling**: If verification contradicts initial finding, trust the direct observation, update the finding.

---

## RULE research-004: Respect Research Scope

- **Priority**: P1 (Scope Control)
- **Trigger**: Starting a research task
- **Scope**: All phases
- **Rule**: Research only what the task asks. Do not explore unrelated directories, read unrelated files, or investigate "interesting" tangents. Stay on target.
- **Verification**: Research output maps directly to task questions.
- **Conflict Handling**: If a tangent appears critical (e.g., discovered security issue), note it in ExecutionReport as a finding, do not expand scope without approval.

---

## RULE research-005: Read-Only Confirmation

- **Priority**: P1 (Scope Control)
- **Trigger**: Any research task
- **Scope**: Phase 0-5
- **Rule**: Confirm at task start that research is read-only. List the tools to be used. All must be from the Permitted: Read-Only category in `docs/agent-runtime/tool-policy.md`.
- **Verification**: Task plan includes tool list; all tools are read-only.
- **Conflict Handling**: If task requires a restricted tool for research, flag before starting, get approval.
