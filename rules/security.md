# Security Rules -- RD2100 Agent Runtime v2

> Domain: security hard stops
> Phase 0-5: P0/P1 active; P2-P4 within approved task scope

---

## RULE sec-001: No Secrets in Code or Logs

- **Priority**: P0 (Hard Stop)
- **Trigger**: Writing any file or output
- **Scope**: All phases, all code
- **Rule**: Secrets (API keys, tokens, passwords, private keys, connection strings with credentials) must never appear in source code, configuration files, logs, reports, or commit messages. Use environment variables or secure vaults.
- **Verification**: Grep output for common secret patterns before commit/report.
- **Conflict Handling**: If a task requires documenting a configuration format that includes a placeholder secret, use `REPLACE_ME` or `<YOUR_KEY_HERE>`.

---

## RULE sec-002: No Command Injection

- **Priority**: P0 (Hard Stop)
- **Trigger**: Constructing shell commands or SQL queries with user/external input
- **Scope**: All phases, all code
- **Rule**: Never concatenate user input into shell commands or SQL queries. Use parameterized queries for SQL. Use argument arrays (not string interpolation) for shell commands. Validate all inputs at system boundaries.
- **Verification**: Grep for string interpolation in `bash`, `exec`, `spawn`, `query`, `execute`.
- **Conflict Handling**: If a legacy API requires string-based queries, input must be strictly validated against an allowlist before use.

---

## RULE sec-003: No Path Traversal

- **Priority**: P0 (Hard Stop)
- **Trigger**: Constructing file paths with user/external input
- **Scope**: All phases, all code
- **Rule**: File paths constructed with user input must be validated to stay within the intended directory. Reject paths containing `..`, absolute paths, or symlink traversal. Resolve and verify the canonical path is within the allowed root.
- **Verification**: Test with `../../../etc/passwd` and absolute path inputs.
- **Conflict Handling**: If relative path flexibility is required, validate against an allowlist of permitted subdirectories.

---

## RULE sec-004: Input Validation at Boundaries

- **Priority**: P0 (Hard Stop)
- **Trigger**: Receiving input from user, network, file, or external system
- **Scope**: All phases, all code
- **Rule**: All external input must be validated at the system boundary. Validate type, length, format, and range. Reject (do not sanitize) invalid input. Accept only what you expect.
- **Verification**: For each input source, trace to a validation function.
- **Conflict Handling**: If validation rules are not yet defined, reject all input until rules are established.

---

## RULE sec-005: No Hardcoded Credentials

- **Priority**: P0 (Hard Stop)
- **Trigger**: Writing authentication or authorization code
- **Scope**: All phases, all code
- **Rule**: Credentials must not be hardcoded. Use environment variables, secure configuration stores, or runtime injection. Default credentials (admin/admin) are forbidden even in development.
- **Verification**: Grep for `password =`, `secret =`, `api_key =`, `token =` with string literal values.
- **Conflict Handling**: Test fixtures may use `test_` prefixed placeholder values with reviewer approval.

---

## RULE sec-006: Thread Safety for Shared State

- **Priority**: P1 (Scope Control)
- **Trigger**: Writing code with shared mutable state
- **Scope**: All code
- **Rule**: Shared mutable state must be protected by appropriate synchronization (locks, atomics, channels). Document the concurrency model. Prefer immutable data structures and message passing over shared state.
- **Verification**: Identify all shared state; verify synchronization mechanism for each.
- **Conflict Handling**: Read-only shared state does not require synchronization.

---

## RULE sec-007: Encrypted Sensitive Data

- **Priority**: P1 (Scope Control)
- **Trigger**: Storing or transmitting sensitive data
- **Scope**: All phases, all code
- **Rule**: Sensitive data (PII, credentials, tokens) must be encrypted at rest and in transit. Use TLS 1.2+ for transmission. Use established encryption libraries (do not implement your own crypto).
- **Verification**: Data flow trace shows encryption at each storage/transmission point.
- **Conflict Handling**: Local development may use plaintext for non-sensitive test data only.

---

## RULE sec-008: Error Messages Without Internals

- **Priority**: P2 (Evidence)
- **Trigger**: Writing error responses for external consumers
- **Scope**: All code with external interfaces
- **Rule**: Error messages returned to users or external systems must not expose internal details (stack traces, file paths, SQL, framework versions). Log internals server-side; return generic messages externally.
- **Verification**: Test error paths; confirm responses contain no internal details.
- **Conflict Handling**: Debug/development modes may return detailed errors with explicit opt-in.
