# devframe-system Parent Pin Review A10

Date: 2026-06-15
Scope: parent-only pin review after opencode evidence-manifest boundary,
test-frame closeout, and agent-acceptance parent canary return
Runtime: not executed by parent
Parent action: ready for lock/gitlink update after fresh re-check
Verdict: `GROUP_PIN_CANDIDATE_READY_HOLD_ACTIVE`

## 1. Executive Decision

The A9 grouped candidate is superseded because `dev-frame-opencode` advanced
from empty-metadata fail-closed commit `58b79e2...` to evidence-manifest
boundary commit `a2cedaa...`.

Current observed module heads now have usable local/offline or synthetic intake
evidence:

- `agent-acceptance`: parent canary gate accepted at `b9bb53a...`.
- `dev-frame-opencode`: evidence-manifest boundary accepted at `a2cedaa...`.
- `test-frame`: TGM MiniApp readiness closeout accepted at `c3353fb...`.
- `devframe-control-plane`: frozen and still aligned at `7939954...`.

The parent sent a short HOLD to `dev-frame-opencode` so it should not start a
new slice before grouped parent pin. The next parent action is fresh re-check
and lock/gitlink update if no module moved again.

## 2. Fresh Pin Candidate Matrix

| Module | Locked commit | Observed commit | Worktree | Parent intake state | Pin state |
|---|---|---|---|---|---|
| `agent-acceptance` | `3cf2c9be9f33ddabdc029a652dca512d8193a5e5` | `b9bb53a72bbd7b4c4e4402aca11b4cc67f9506f5` | old untracked evidence remains | parent canary gate accepted | candidate with dirty-note |
| `dev-frame-opencode` | `0c24204fd99e6cab1d853ecadb12200244119fe1` | `a2cedaa280f12f717d4bf0a64c1c12ece6f5fefe` | clean at intake | evidence manifest boundary accepted for intake | candidate |
| `devframe-control-plane` | `79399541b8426cff0f362b665bad09e3c23e974b` | `79399541b8426cff0f362b665bad09e3c23e974b` | clean | frozen aligned baseline | keep frozen |
| `test-frame` | `bdd7b67a4bb9cfee2c6601c2f755abfd68164da7` | `c3353fb34900aa24f56df5b9c9230f3249d6c01a` | clean | closeout milestone accepted for intake | candidate |

## 3. Accepted Intake Reports

- `integration/reports/parent-canary-agent-acceptance-return-review-2026-06-15.md`
- `integration/reports/opencode-zotero-evidence-manifest-boundary-return-review-2026-06-15.md`
- `integration/reports/test-frame-readiness-closeout-return-review-2026-06-15.md`

Supporting historical intake reports:

- `integration/reports/opencode-zotero-metadata-export-hardening-return-review-2026-06-15.md`
- `integration/reports/opencode-zotero-ris-metadata-parser-return-review-2026-06-15.md`
- `integration/reports/opencode-zotero-metadata-scope-limits-return-review-2026-06-15.md`
- `integration/reports/opencode-zotero-export-file-type-guard-return-review-2026-06-15.md`
- `integration/reports/opencode-zotero-empty-metadata-failclosed-return-review-2026-06-15.md`
- `integration/reports/parent-canary-test-frame-return-review-2026-06-15.md`
- `integration/reports/parent-canary-combined-intake-review-2026-06-15.md`

## 4. Current Candidate Pin Set

If the fresh re-check still matches this report, grouped parent pin should use:

- `agent-acceptance` ->
  `b9bb53a72bbd7b4c4e4402aca11b4cc67f9506f5`
- `dev-frame-opencode` ->
  `a2cedaa280f12f717d4bf0a64c1c12ece6f5fefe`
- `test-frame` ->
  `c3353fb34900aa24f56df5b9c9230f3249d6c01a`
- `devframe-control-plane` unchanged at
  `79399541b8426cff0f362b665bad09e3c23e974b`

## 5. Mutation Preconditions

Before changing parent gitlinks or lock files, re-check:

- `git status --short --branch`
- `git submodule status`
- `git -C dev-frame-opencode status --short --branch`
- `git -C test-frame status --short --branch`
- `git -C agent-acceptance status --short --branch`
- `git -C devframe-control-plane status --short --branch`

Hard stop if:

- any candidate module advances again;
- `dev-frame-opencode` or `test-frame` becomes dirty;
- evidence ZIP or hash is missing;
- a newer submodule final return supersedes this review.

## 6. Boundary

This review does not authorize:

- real Zotero export/API/plugin/storage;
- real Obsidian, RAG, PDF/full text, WriteLab;
- real MiniApp runtime, WeChat DevTools, miniprogram-automator, Jest E2E;
- H5, MeterSphere, cloud, Android, browser/CDP product runtime;
- final governance acceptance.

All current evidence remains local/offline/synthetic/candidate evidence unless
separately reviewed and authorized.

## 7. Parent Recommendation

Recommended next action:

- Perform fresh re-check.
- If stable, update parent gitlinks, `integration/lock/submodules.lock.yml`,
  and `BASELINE_LOCK.json` to the A10 candidate set.
- Run parent diff/submodule verification.
