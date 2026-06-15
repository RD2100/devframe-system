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
| 1B | `agent-acceptance` path/Gate0 and verdict contract | Complete with boundary | Parent pins commit `54d60a2`; SD-04 through SD-07 boundaries retained, and TaskSpec `agent-acceptance-minimal-rule-center-a1` now passes runner start for the next minimal rule-center iteration | Child agent executes the TaskSpec and returns ExecutionReport |
| 1B | `dev-frame-opencode` runtime authorization contract | Complete with boundary | Parent pins commit `0c24204`; RuntimeAuthorization/EvidenceManifest contracts include paper `data_policy`, direct live WriteLab calls require explicit `paragraph_text` authorization before HTTP dispatch, post-run changed files are checked against effective write scope, paper audit/report gates cover paragraph/matched-text/text-span payloads, Security Preflight P1 gates are independently reviewed, synthetic/offline business validation has a machine-readable JSON artifact, and SD-07 governance status is visible in the report schema/output | Fresh authorization before live execution |
| 1B | Paper feature hardening | SD-07 readiness slices pinned with boundary | Parent pins opencode commit `0c24204`, agent-acceptance commit `54d60a2`, test-frame commit `bdd7b67`, and control-plane commit `7939954`; previous SD-07 checks remain bounded, and test-frame now has time-goal-manager MiniApp dry-run plus missing-environment BLOCKED/FAILED reports | Human review of candidate and fresh RuntimeAuthorization before real paper content or live WriteLab execution |
| 1B | `test-frame` adapter/negative matrix and TGM MiniApp dry-run | Complete with boundary | Parent pins commit `bdd7b67`; paper negative matrix remains, time-goal-manager MiniApp smoke dry-run contract is recorded, and missing WeChat DevTools semantics fail non-zero without fake green | Real MiniApp E2E remains human-authorized future work |
| 2-pre | `control-plane` lease/source-lock contract | Complete with boundary | Parent pins commit `7939954`; in-memory dry-run runtime state-machine tests passed 21/21 and unauthorized paper real-content/live WriteLab dispatch is blocked without fresh scoped RuntimeAuthorization | Runtime lease/heartbeat/cancellation enforcement |
| 2-pre | Security Preflight | P1 review pass with boundary | `integration/reports/security-preflight-2026-06-15.md`; no P0 found, P1 findings reviewed after `dev-frame-opencode` commits `4558ab8` and `40ee21b`; real content remains human-gated | Fresh RuntimeAuthorization before real paper content or live WriteLab flow |
| 3 | Canary negative matrix | Seeded, not runtime-active | `test-frame` fixtures `NEG-031` through `NEG-049` cover paper privacy, fake-green, business-validation promotion, business report shape failures, and synthetic/offline live-authorization overclaim | Wire these fixtures into future canary/runtime execution before external verification use |
| 4 | Multi-worker dry-run | Not started | None | Requires lease/source-lock contract |
| 5 | Human-gated live pilot | Not started | `agent-acceptance` commit `54d60a2` retains SD-07 real-content/live WriteLab RuntimeAuthorization boundary and adds the minimal rule-center TaskSpec; main-thread SD-07 verification remains recorded in `integration/reports/sd07-runtime-authorization-boundary-2026-06-15.md` | Requires fresh RuntimeAuthorization, pilot TaskSpec, and independent review before any real-content or live WriteLab execution |

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
