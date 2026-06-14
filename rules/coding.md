# Coding Rules -- RD2100 Agent Runtime v2

> Domain: code generation and modification
> Phase 0-5: P0/P1 active; P2-P4 within approved task scope

---

## RULE code-001: No Empty Error Handling

- **Priority**: P0 (Hard Stop)
- **Trigger**: Writing catch blocks or error handlers
- **Scope**: All code
- **Rule**: No empty `catch` blocks. No bare `e.printStackTrace()` without context. Every error path must either log with context, rethrow with wrapping, or handle with a documented reason.
- **Verification**: Grep for `catch\s*\([^)]*\)\s*\{\s*\}` or `catch\s*\([^)]*\)\s*\{[^}]{0,20}\}`.
- **Conflict Handling**: If a third-party API requires empty catch (rare), document with `// intentional: <reason>` comment.

---

## RULE code-002: No Swallowed Errors

- **Priority**: P1 (Scope Control)
- **Trigger**: Writing error handling code
- **Scope**: All code
- **Rule**: Errors must not be silently swallowed. If an error cannot be handled, propagate it. If it can be handled, log the handling decision.
- **Verification**: Code review: every error path either propagates, logs, or has a documented reason for suppression.
- **Conflict Handling**: Intentional suppression requires a dated TODO comment explaining why.

---

## RULE code-003: Minimal Change Surface

- **Priority**: P1 (Scope Control)
- **Trigger**: Any code modification
- **Scope**: All code
- **Rule**: Make the smallest change that solves the problem. Do not refactor adjacent code. Do not add abstractions "for the future". Do not rename unrelated variables. Do not reformat untouched lines.
- **Verification**: Diff review: changed lines should map directly to the task description.
- **Conflict Handling**: If the task inherently requires broad changes, document scope in task plan before starting.

---

## RULE code-004: Read Before Edit

- **Priority**: P2 (Evidence)
- **Trigger**: Before modifying any existing file
- **Scope**: All code
- **Rule**: Read the file first. Understand existing patterns, naming, and structure before making changes. Match the existing style.
- **Verification**: Log shows Read before Edit for each modified file.
- **Conflict Handling**: If the existing style is inconsistent, match the dominant pattern in the file.

---

## RULE code-005: Match Existing Style

- **Priority**: P3 (Domain)
- **Trigger**: Writing new code in an existing file
- **Scope**: All code
- **Rule**: Follow the file's existing indentation, quoting, naming, and comment style. Do not impose a different style on an existing file.
- **Verification**: Diff shows new code consistent with surrounding lines.
- **Conflict Handling**: If a file has mixed styles, match the closest adjacent code.

---

## RULE code-006: TODO Format

- **Priority**: P3 (Domain)
- **Trigger**: Writing a TODO comment
- **Scope**: All code
- **Rule**: TODO comments must include a date: `// TODO(YYYY-MM-DD): description`. Without a date, a TODO is not acceptable.
- **Verification**: Grep for `TODO` without a date pattern.
- **Conflict Handling**: If adding a date is impossible (generated code), use `// NOTE:` instead of `// TODO:`.

---

## RULE code-007: Naming Conventions

- **Priority**: P4 (Style)
- **Trigger**: Naming any variable, function, or constant
- **Scope**: All code
- **Rule**: Variables and functions use `camelCase`. Constants use `UPPER_SNAKE`. Classes/Types use `PascalCase`. Files use `kebab-case` or match existing pattern.
- **Verification**: Lint check for naming convention violations.
- **Conflict Handling**: If the existing codebase uses a different convention, follow the existing convention.
