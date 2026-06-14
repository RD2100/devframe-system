# Risk Register

Date: 2026-06-15

| ID | Severity | Risk | Current control | Required next action |
|---|---|---|---|---|
| R-001 | P0 | `HUMAN_REQUIRED` or `BLOCKED` is reported as PASS | SADP negative fixtures and review rules; paper CLI final-acceptance labels pinned at `3395033` keep workflow/schema/artifact status separate from final acceptance | Add remaining governance-level finalizer tests that reject status promotion. |
| R-002 | P0 | Dispatch success is treated as task success | Contract separation in plan | Require `ExecutionReport`, `ReviewVerdict`, and governance verdict as separate artifacts. |
| R-003 | P0 | Reviewer and executor roles are mixed | SADP reviewer rules | Enforce `independent_from_executor` in review contract. |
| R-004 | P0 | Worker writes outside approved scope | `write_set` contract planned | Add SourceLock/WorkerLease and post-run diff checks before runtime use. |
| R-005 | P1 | `agent-acceptance` active path drift | Documented in status | Decide whether to rebind active config to submodule path; do not rewrite historical archives. |
| R-006 | P1 | A120 ZIP evidence self-proves acceptance | Independent `PASS_WITH_BOUNDARY` ZIP review report now exists | Keep final acceptance separate from ZIP review; add negative fixtures before promotion. |
| R-007 | P1 | A120 evidence absent from submodule path | Canonical path documented | Record artifact path, hash, and owner in evidence manifest. |
| R-008 | P1 | `test-frame` is treated as plugin or final verdict source | Boundary docs | Keep role language consistent in docs and reports. |
| R-009 | P1 | Live CDP/Playwright capability is over-promoted | Human-gated status documented | Keep live runtime blocked until explicit RuntimeAuthorization exists. |
| R-010 | P1 | GitLab CI starts runtime/test jobs too early | Readonly CI policy | Keep initial CI limited to git, schema, and inventory checks. |
| R-011 | P1 | Paper private full text leaks into evidence, reports, or live WriteLab payloads | Paper runtime/API privacy gate pinned at `145fc05`; audit ZIP candidate sensitive scan pinned at `cb34be3`; live WriteLab sensitive-input guard pinned at `ea0758a`; unauthorized raw `paragraph_text`/`writelab_token` fails closed to `human_required`, human-gate issue text is redacted, audit packaging rejects unredacted state/ledger/report candidates, and direct live WriteLab calls block before HTTP dispatch without explicit `paragraph_text` authorization | Add full redacted reviewer-pack probes before real paper content use. |
| R-012 | P1 | Paper schema/fixture user text becomes unreadable or structurally changed during cleanup | Narrow JSON/YAML parse plus diff review | Review only user-visible text changes; preserve fields, required list, enums, and schema shape. |
| R-013 | P1 | OpenCode post-run detection is mistaken for pre-write prevention | RuntimeAuthorization contract added in submodule branch | Require explicit `prevention_level`; do not claim filesystem sandbox until implemented. |
| R-014 | P2 | WriteLab handoff tests silently lose fixture coverage | Mitigated in `72d1dbd`: tracked `mock_handoff.zip`, refreshed manifest hashes, and added a ZIP/manifest consistency test; WriteLab adapter tests passed 63/63 and the broader paper/WriteLab group passed 221/221 | Keep the handoff ZIP validation tests in CI and add future negative fixtures for privacy-attestation and integrity failures. |
