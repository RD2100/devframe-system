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
| 1B | `agent-acceptance` path/Gate0 contract | Complete with boundary | Parent pins commit `88dd581`; Reviewer Index returned | Human decision for active config rebinding |
| 1B | `dev-frame-opencode` runtime authorization contract | Complete with boundary | Parent pins commit `51215f1`; RuntimeAuthorization/EvidenceManifest contracts include paper `data_policy`, and direct live WriteLab calls require explicit `paragraph_text` authorization before HTTP dispatch | Fresh authorization before live execution |
| 1B | Paper feature hardening | In progress with pinned gate, handoff fixture, audit scan, live WriteLab guard, CLI status boundary, and redacted reviewer pack boundary | Parent pins commit `51215f1`; 173 CLI/report/audit regression tests passed; 276 paper runtime/graph/WriteLab regression tests passed; 115 audit/e2e regression tests passed | Governance-level finalizer tests and remaining user-visible mojibake cleanup |
| 1B | `test-frame` adapter/negative matrix | Complete with boundary | Parent pins commit `71caa1c`; Reviewer Index returned | Canary implementation before external verification runtime use |
| 2-pre | `control-plane` lease/source-lock contract | Complete with boundary | Parent pins commit `49c6be8`; Reviewer Index returned | Runtime lease/heartbeat/cancellation enforcement |
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
