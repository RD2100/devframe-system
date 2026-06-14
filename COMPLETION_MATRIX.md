# Completion Matrix

Date: 2026-06-15

This matrix tracks project completeness by evidence, not intent. A phase is
complete only when its evidence is present and current.

| Phase | Area | Status | Evidence | Remaining work |
|---|---|---|---|---|
| 0.5 | `/rdinit` bootstrap | Complete | `AGENTS.md`, `rules/`, `schemas/`, `docs/agent-runtime/`, `templates/runtime-bootstrap/` | Reviewer sign-off |
| 0.5 | Baseline lock | Complete | `BASELINE_LOCK.json`, `integration/lock/submodules.lock.yml`, `scripts/check-submodules.ps1` | None for current pins |
| 0.5 | Readonly inventory | Complete | `scripts/readonly-inventory.ps1`, `.gitlab-ci.yml`, `integration/runbooks/gitlab-ci-readonly-policy.md`; inventory also parses JSON as UTF-8 | GitLab runner proof |
| 1A | A120 ZIP independent review | Complete with boundary | `scripts/review_a120_evidence_zip.py`, `integration/reports/a120/a120-evidence-zip-review.json` | Negative fixtures and reviewer sign-off |
| 1B | `agent-acceptance` path/Gate0 and verdict contract | Complete with boundary | Parent pins commit `b505bf7`; path/Gate0 contract retained, SD-04 rejects paper reviewer-pack/report/test/zip final-verdict promotion, and SD-05 rejects dispatch/test-frame/control-plane promotion plus expired authorization success | Human decision for active config rebinding |
| 1B | `dev-frame-opencode` runtime authorization contract | Complete with boundary | Parent pins commit `4558ab8`; RuntimeAuthorization/EvidenceManifest contracts include paper `data_policy`, direct live WriteLab calls require explicit `paragraph_text` authorization before HTTP dispatch, post-run changed files are checked against effective write scope, paper audit/report gates cover paragraph/matched-text/text-span payloads, and Security Preflight P1 gates are present | Fresh authorization before live execution |
| 1B | Paper feature hardening | In progress with pinned gate, handoff fixture, audit scan, live WriteLab guard, CLI status boundary, redacted reviewer pack boundary, finalizer acceptance boundary, focused mojibake cleanup, archive-side verdict boundary, post-run write-set hard gate, paper audit privacy hard gate, reviewer negative fixtures, and Security Preflight P1 fix candidate | Parent pins opencode commit `4558ab8`, agent-acceptance commit `b505bf7`, and test-frame commit `be27de0`; main-thread checks passed for opencode 144 security/paper/daemon tests, 14 batch/idempotency tests, compileall, agent-acceptance 22 closure tests, and test-frame 31 fixture/gate tests | Independent Security Preflight review; fresh authorization before live execution; Paper Business Capability Validation |
| 1B | `test-frame` adapter/negative matrix | Complete with boundary | Parent pins commit `be27de0`; paper reviewer-pack negative fixture tests passed 31/31 with `ai_guard full` PASS | Canary implementation before external verification runtime use |
| 2-pre | `control-plane` lease/source-lock contract | Complete with boundary | Parent pins commit `c3edf85`; in-memory runtime contract probe tests passed 8/8 | Runtime lease/heartbeat/cancellation enforcement |
| 2-pre | Security Preflight | Fix candidate ready; independent review pending | `integration/reports/security-preflight-2026-06-15.md`; no P0 found, P1 findings have fix candidates pinned in `dev-frame-opencode` commit `4558ab8` | Independent security review before paper business acceptance |
| 3 | Canary negative matrix | Not started | None | Consolidate module negative cases |
| 4 | Multi-worker dry-run | Not started | None | Requires lease/source-lock contract |
| 5 | Human-gated live pilot | Not started | None | Requires fresh RuntimeAuthorization |

## Completion Rules

- `Complete` means evidence exists in this repository and passed its verification.
- `Complete with boundary` means the evidence is valid for its stated boundary
  but does not imply final acceptance.
- `Delegated` means a sub-agent has an active TaskSpec and the main thread is
  awaiting a Reviewer Index.
- `Submodule branch complete; parent pin pending` means a sub-agent returned a
  Reviewer Index, but the superproject has not yet advanced the submodule
  gitlink.
- `Submodule branch active` means a sub-agent is still working or has not yet
  returned a final Reviewer Index.
- `Not started` means no current evidence exists.
