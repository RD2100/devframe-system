# Verification Gates -- RD2100 Agent Runtime v2

> Batch B1, 2026-05-27
> Defines quality gates that every agent execution must pass through.

## Gate Hierarchy

```
                      +------------------+
                      |   P0: Security   |  <-- Must pass. Failure = BLOCKED.
                      +--------+---------+
                               |
                      +--------v---------+
                      |   P1: Correctness |  <-- Must pass. Failure = FAILED.
                      +--------+---------+
                               |
                      +--------v---------+
                      |   P2: Quality    |  <-- Should pass. Failure = WARNING.
                      +--------+---------+
                               |
                      +--------v---------+
                      |   P3: Completeness|  <-- Nice to pass. Failure = INFO.
                      +------------------+
```

## Gate Definitions

### P0: Security Gate

| Check | Tool/Method | Pass Condition |
|-------|-------------|----------------|
| No secrets in output | `security-checklist` (PII protection) | No keys, tokens, passwords in code or logs |
| No command injection | Manual review of bash arguments | All user input sanitized or hardcoded |
| No path traversal | Manual review of file paths | All paths within project root |
| Thread safety | `security-checklist` (thread safety) | No unsynchronized shared state |
| Input validation | `security-checklist` (input validation) | All external inputs validated |
| Encryption | `security-checklist` (encryption) | Sensitive data encrypted at rest/in transit |

Gate result: PASS -> continue. FAIL -> **BLOCKED, must not deliver**.

### P1: Correctness Gate

| Check | Tool/Method | Pass Condition |
|-------|-------------|----------------|
| Build evidence | Reviewer-approved validation command or blocked_by_env record | Exit code 0 when approved and run, otherwise explicitly blocked/skipped |
| Test evidence | Reviewer-approved validation command or blocked_by_env record | Existing checks green when approved and run, otherwise explicitly blocked/skipped |
| No regression | Before/after comparison from approved evidence | Same or fewer failures when evidence exists |
| Exit code contract | Check agent-acceptance exit codes | 0=PASS, 1=BLOCKED, 2=FAILED |

Gate result: PASS -> continue. FAIL -> **FAILED, must fix before delivery**.

### P2: Quality Gate

| Check | Tool/Method | Pass Condition |
|-------|-------------|----------------|
| Code review | `ai-code-review` (P2 level) | No code quality issues |
| Lint | `claude-lint-fix` | No lint errors |
| Performance | `performance-lint` (5 anti-patterns) | No main-thread IO, no N+1, no leak |
| Code style | Match existing project style | Consistent with surrounding code |
| No dead code | Manual review | No unused variables, imports, functions |

Gate result: PASS -> continue. FAIL -> **WARNING, should fix but may proceed with justification**.

### P3: Completeness Gate

| Check | Tool/Method | Pass Condition |
|-------|-------------|----------------|
| Documentation | `claude-md-docs` | New features documented |
| Changelog | `changelog-generator` | Changes logged |
| Test coverage | Manual review | New code has corresponding tests |
| Error handling | `security-checklist` (error handling) | Errors handled, not swallowed |

Gate result: PASS -> continue. FAIL -> **INFO, not blocking**.

## Gate Execution Order

When an agent completes a task:

```
1. P0 Security Gate
   - security-checklist runs (mandatory)
   - Human must approve if gate fails
   - BLOCKED state if any P0 check fails

2. P1 Correctness Gate
   - Reviewer-approved build/test evidence or explicit blocked_by_env record
   - Regression comparison
   - FAILED state if any P1 check fails

3. P2 Quality Gate
   - ai-code-review runs (P2 level)
   - performance-lint runs
   - WARNING if issues found

4. P3 Completeness Gate
   - Documentation check
   - Changelog update
   - INFO if incomplete
```

## Agent-Acceptance Gate Mapping

The agent-acceptance workqueues map to these gates:

| WorkQueue | Gates Covered | Tier |
|-----------|:---:|:---:|
| `local-quality.queue.json` | P2 (Quality) | Tier 1 |
| `docs-quality.queue.json` | P3 (Completeness) | Tier 1 |
| `recovery-regression.queue.json` | P1 (Correctness) | Tier 1 |
| `cleanup-dryrun.queue.json` | P2 (Quality) | Tier 1 |
| `release-readiness.queue.json` | P1 + P2 + P3 | Tier 2 |

## Gate Bypass Policy

| Scenario | Allowed? | Requirement |
|----------|:---:|-------------|
| P0 failure | NO | Never bypass security gate |
| P1 failure with known flaky test | YES | Document the flaky test, link to issue |
| P3 info only | N/A | Not a gate, informational only |
| Emergency hotfix | YES (P1 only) | Human approval + post-fix gate run |
