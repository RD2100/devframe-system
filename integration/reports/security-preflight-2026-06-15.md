# Security Preflight Report

Date: 2026-06-15
Status: `SECURITY_PREFLIGHT_REVIEW_PASS`
Scope: targeted preflight for paper workflow, agent dispatch, daemon/queue, and verdict-boundary risks.

This report is a preflight summary, not final acceptance and not a full
repository-wide security certification.

## 1. Project Stage

`PROJECT_STAGE: SECURITY_PREFLIGHT_REVIEW_PASS`

The old dirty-baseline blocker is obsolete for the canonical repository:

- repo: `D:\dev-frame-opencode`
- branch: `master`
- HEAD: `3a3aa5722bd6015bec30a8e9190140148b45167c`
- upstream: `origin/master`
- upstream hash: `3a3aa5722bd6015bec30a8e9190140148b45167c`
- remote master hash: `3a3aa5722bd6015bec30a8e9190140148b45167c`
- staged diff: `0`
- tracked dirty: `0`
- untracked: `0`
- clean status: `true`

Old dirty state with 7 tracked dirty and about 10469 untracked is obsolete and
must not be used as a current blocker.

## 2. Tool Availability

| Tool | Result | Notes |
|---|---|---|
| SkillSpector targeted scan | `TOOL_NOT_AVAILABLE` | `Get-Command skillspector` and local file search returned no installed tool. No result was fabricated. |
| Codex Security focused scan | `FOCUSED_READ_ONLY_REVIEW_COMPLETED` | Completed by read-only sub-agents over CLI/daemon/queue/security boundaries. This was not an unbounded full-repository scan. |

## 3. Focused Security Findings

| ID | Severity | Status | Finding | Required action |
|---|---|---|---|---|
| SEC-CLI-001 | P1 | Review pass with boundary | TaskSpec verification command strings can enter the execution chain without a strict allowlist/sandbox boundary. | Commit `4558ab8` adds deny-by-default command allowlisting and rejects shell operators, inline Python, unknown executables, and write/fix flags; independent review passed after commit `40ee21b`. |
| SEC-CLI-002 | P1 | Review pass with boundary | `goal_review_recovered` can rely on OpenCode exit status as a safety verdict, which risks fake green. | Commit `4558ab8` requires structured JSON verdict plus independent `diff_scope_ok=true` and `reviewed_diff=true` gate evidence; independent review passed after commit `40ee21b`. |
| SEC-DAEMON-001 | P1 | Review pass with boundary | Queued tasks can trigger daemon write-type execution without a daemon-side permission/risk gate. | Commit `4558ab8` added initial daemon gate; independent review blocked its naked `daemon_write_authorized` trust. Commit `40ee21b` removes the naked self-authorization path and requires structured authorization bound to task/project/workflow/source/expiry; independent review passed. |
| SEC-AUDIT-001 | P2 | Open | Unsigned audit bundles may be interpreted as pass by consumers that ignore trust summary. | Make unsigned status non-promotable and explicit in downstream consumers. |
| SEC-QUEUE-001 | P2 | Open | Queue status pollution and missing transition matrix can blur terminal states. | Enforce allowed status values and state transitions. |
| SEC-DAEMON-002 | P2 | Open | Daemon configuration values are not fully clamped. | Clamp poll interval, concurrency, retry, and stale thresholds. |
| SEC-LOG-001 | P2 | Open | Runtime/audit logs need stronger generic secret/path redaction rules. | Extend redaction beyond known paper field names. |

## 4. New Mitigations Integrated This Round

| Module | Commit | Mitigation |
|---|---|---|
| `dev-frame-opencode` | `40ee21b56e1bf96bd4874098e251eb23c9d05a35` | Closes the daemon self-authorization blocker by removing naked `daemon_write_authorized` trust and requiring structured `daemon_authorization` bound to task, project, workflow, source, and unexpired human-gate evidence. |
| `dev-frame-opencode` | `4558ab819ceacd8998c5b295f51f790c21e55857` | Adds Security Preflight P1 fix candidates for TaskSpec verification command allowlisting, structured review recovery verdicts, and daemon queued-write authorization/risk gating. |
| `dev-frame-opencode` | `8119c85fd4991961accd35507351bf7db9199252` | Expands paper audit/report redaction and fail-closed scanning for raw paragraph payloads, `matched_text`, `text_span`, and WriteLab payload markers. |
| `agent-acceptance` | `b505bf716c55c804302db35f33375afc9524c826` | Adds SD-05 closure validation so dispatch/test-frame/control-plane evidence and expired authorization cannot claim final governance verdict. |
| `test-frame` | `be27de01950a05d743764fd394a3ab9c9336b818` | Adds paper reviewer-pack negative fixtures `NEG-031` to `NEG-038`. |
| `devframe-control-plane` | `c3edf8528cb853c023929c2c26fef208177e2198` | Adds pure in-memory runtime contract probe covering duplicate dispatch, stale lease completion, overlapping SourceLock, cancellation, retry, and dispatch-success promotion. |

## 5. P1 Verification and Independent Review

Main-thread verification observed for `dev-frame-opencode` commit `4558ab8`:

- `PYTHONPATH=D:\devframe-system\dev-frame-opencode\ai-workflow-hub\src; python -m pytest ai-workflow-hub\tests\test_security_preflight_p1.py ai-workflow-hub\tests\test_paper_a21_daemon_queue_e2e.py ai-workflow-hub\tests\test_paper_a22_daemon_soak_hardening.py ai-workflow-hub\tests\test_paper_runtime.py -q` -> `144 passed in 13.95s`.
- `PYTHONPATH=D:\devframe-system\dev-frame-opencode\ai-workflow-hub\src; python -m pytest ai-workflow-hub\tests\test_batch_retry.py ai-workflow-hub\tests\test_stage3b_idempotency.py -q` -> `14 passed in 0.59s`.
- `python -m compileall -q ai-workflow-hub\src` -> passed.
- `git diff --check` -> passed.

Independent review then blocked `4558ab8` for `SEC-DAEMON-001`, because the
daemon gate still trusted a queued task's naked `daemon_write_authorized=True`.

Follow-up commit `40ee21b` removed that self-authorization path. Main-thread
verification observed for `40ee21b`:

- `PYTHONPATH=D:\devframe-system\dev-frame-opencode\ai-workflow-hub\src; python -m pytest ai-workflow-hub\tests\test_security_preflight_p1.py ai-workflow-hub\tests\test_paper_a21_daemon_queue_e2e.py ai-workflow-hub\tests\test_paper_a22_daemon_soak_hardening.py ai-workflow-hub\tests\test_paper_runtime.py -q` -> `146 passed in 12.91s`.
- `PYTHONPATH=D:\devframe-system\dev-frame-opencode\ai-workflow-hub\src; python -m pytest ai-workflow-hub\tests\test_batch_retry.py ai-workflow-hub\tests\test_stage3b_idempotency.py -q` -> `14 passed in 0.60s`.
- `python -m compileall -q ai-workflow-hub\src` -> passed.
- `git diff --check` -> passed.

Independent sub-agent reviews:

- `agent-acceptance`: `SECURITY_PREFLIGHT_REVIEW_PASS` for P1 preflight only.
- `test-frame`: `NEGATIVE_MATRIX_REVIEW_PASS`; recommended future exact SPF
  fixtures and high-risk daemon canary, not blockers for this P1 review.

This evidence is a P1 preflight review pass with boundary, not live-runtime
authorization and not final paper acceptance.

## 6. Acceptance Recommendation

`A_NEXT_RECOMMENDATION: PAPER_FUNCTION_BUSINESS_CAPABILITY_VALIDATION`

The next acceptance can switch to Paper Function Business Capability Validation
using synthetic/offline evidence first. Real paper content and live WriteLab
flows still require fresh RuntimeAuthorization.

Use the next available acceptance number. The purpose is Paper Function
Business Capability Validation, not cumulative evidence-chain hardening.

## 7. Devframe-System Integration Branch Note

Do not confuse:

- canonical clean repo: `D:\dev-frame-opencode` on `master` at `3a3aa57`
- superproject integration submodule: `D:\devframe-system\dev-frame-opencode`
  on `codex/paper-audit-privacy-hard-gate` at `40ee21b`

The canonical clean baseline proves Route A source cleanliness. It does not
prove the superproject integration branch is safe or that paper business
capability is complete.

## 8. Blocking Items

| Blocker | Reason | Decision owner | Suggested option |
|---|---|---|---|
| Fresh RuntimeAuthorization absent | Real paper text and live WriteLab flows remain sensitive and human-gated. | Human operator. | Keep real paper content blocked; use synthetic/offline fixtures only. |
| Live daemon authorization provenance | `40ee21b` binds structured task authorization fields, but authorization still lives in task data rather than a signed or out-of-band authorization store. | Runtime/governance owner before live daemon worker use. | Add signed/out-of-band daemon authorization before live worker execution. |

## 9. Final Recommendation

Canonical repo is clean. Do not continue dirty-baseline cleanup. Security
Preflight P1 review has passed with boundary at `40ee21b`. Switch the next
available acceptance to Paper Function Business Capability Validation with
synthetic/offline evidence first; keep real paper content and live WriteLab
blocked until fresh RuntimeAuthorization exists.
