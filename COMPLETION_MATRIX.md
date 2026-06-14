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
| 1B | `agent-acceptance` path/Gate0 and verdict contract | Complete with boundary | Parent pins commit `38d7b2e`; path/Gate0 contract retained, SD-04 rejects paper reviewer-pack/report/test/zip final-verdict promotion, SD-05 rejects dispatch/test-frame/control-plane promotion, SD-06 rejects business-validation promotion, and SD-07 rejects real-content/live WriteLab evidence without fresh scoped RuntimeAuthorization | Human decision for active config rebinding |
| 1B | `dev-frame-opencode` runtime authorization contract | Complete with boundary | Parent pins commit `08ac4f5`; RuntimeAuthorization/EvidenceManifest contracts include paper `data_policy`, direct live WriteLab calls require explicit `paragraph_text` authorization before HTTP dispatch, post-run changed files are checked against effective write scope, paper audit/report gates cover paragraph/matched-text/text-span payloads, Security Preflight P1 gates are independently reviewed, and synthetic/offline business validation now has a machine-readable JSON artifact | Fresh authorization before live execution |
| 1B | Paper feature hardening | Machine-readable business validation report artifact candidate with SD-07 gate | Parent pins opencode commit `08ac4f5`, agent-acceptance commit `38d7b2e`, and test-frame commit `891b106`; main-thread checks passed for opencode business/report and CLI tests, test-frame 19 negative/contract tests, agent-acceptance 27 closure tests plus compile, control-plane 14 dry-run tests, and parent read-only checks | Human review of candidate and fresh RuntimeAuthorization before real paper content or live WriteLab execution |
| 1B | `test-frame` adapter/negative matrix | Complete with boundary | Parent pins commit `891b106`; paper reviewer-pack fixtures `NEG-031` through `NEG-038`, business validation fixtures `NEG-039` through `NEG-043`, and business report fixtures `NEG-044` through `NEG-048` are tracked and tested | Canary implementation before external verification runtime use |
| 2-pre | `control-plane` lease/source-lock contract | Complete with boundary | Parent pins commit `b001cea`; in-memory dry-run runtime state-machine tests passed 14/14 | Runtime lease/heartbeat/cancellation enforcement |
| 2-pre | Security Preflight | P1 review pass with boundary | `integration/reports/security-preflight-2026-06-15.md`; no P0 found, P1 findings reviewed after `dev-frame-opencode` commits `4558ab8` and `40ee21b`; real content remains human-gated | Fresh RuntimeAuthorization before real paper content or live WriteLab flow |
| 3 | Canary negative matrix | Seeded, not runtime-active | `test-frame` fixtures `NEG-031` through `NEG-048` cover paper privacy, fake-green, business-validation promotion, and business report shape failures | Wire these fixtures into future canary/runtime execution before external verification use |
| 4 | Multi-worker dry-run | Not started | None | Requires lease/source-lock contract |
| 5 | Human-gated live pilot | Not started | `agent-acceptance` commit `38d7b2e` implements SD-07 real-content/live WriteLab RuntimeAuthorization boundary, with main-thread verification recorded in `integration/reports/sd07-runtime-authorization-boundary-2026-06-15.md` | Requires fresh RuntimeAuthorization, pilot TaskSpec, and independent review before any real-content or live WriteLab execution |

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
