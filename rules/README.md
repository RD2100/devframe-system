# Rules -- RD2100 Agent Runtime v2

> Batch C1, 2026-05-27
> Canonical root: D:\devframe-system

## Priority System

| Priority | Label | Semantic |
|----------|-------|----------|
| **P0** | Hard Stop | Must not violate. Violation = BLOCKED delivery. |
| **P1** | Scope Control | Must not exceed approved boundaries. Violation = FAILED. |
| **P2** | Evidence | Must produce verifiable proof. Violation = WARNING. |
| **P3** | Domain | Should follow domain conventions. Violation = INFO. |
| **P4** | Style | Cosmetic preference. Violation = INFO. |

## Rule Format

Each rule entry:

```
- Rule ID: <domain>-<number>
- Priority: P0/P1/P2/P3/P4
- Trigger: When this rule activates
- Scope: What it applies to
- Rule: The rule text
- Verification: How to check compliance
- Conflict Handling: What to do when two rules conflict
```

## Rule Files

| File | Domain | Rule Count |
|------|--------|:---:|
| `core.md` | Runtime core -- execution, gating, phase boundaries | 8 |
| `coding.md` | Code generation -- edits, style, patterns | 7 |
| `research.md` | Read-only exploration -- reading, searching, CodeGraph | 5 |
| `security.md` | Security hard stops -- secrets, injection, traversal | 8 |
| `review.md` | Review and evidence -- reports, gates, verification | 6 |
| `git.md` | Git safety -- commits, pushes, destructive ops | 6 |
| `frontend.md` | Frontend -- XSS, components, patterns | 6 |

## Conflict Resolution

When two rules conflict, the higher priority rule wins.
When same priority, the more restrictive rule wins.
When still unresolved, escalate to human reviewer.

## Phase 0-5 Application

All P0 and P1 rules apply unconditionally in Phase 0-5.
P2-P4 rules apply within the approved task scope.
