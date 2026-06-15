# devframe-system Parent Pin Review A7

Date: 2026-06-15
Scope: parent-only pin review after opencode scope limits, test-frame closeout,
and agent-acceptance parent canary return
Runtime: not executed by parent
Parent action: no pin yet, no lock mutation yet, no gitlink update yet
Verdict: `GROUP_PIN_CANDIDATE_READY_CURRENT_HEADS_VERIFIED`

## 1. Executive Decision

The A6 grouped candidate is superseded because `dev-frame-opencode` advanced
from RIS parser commit `cb4997a...` to scope-limit commit `6bd9809...`.

Current observed module heads now have usable local/offline or synthetic intake
evidence:

- `agent-acceptance`: parent canary gate accepted at `b9bb53a...`.
- `dev-frame-opencode`: metadata-only pilot scope limits accepted at
  `6bd9809...`.
- `test-frame`: TGM MiniApp readiness closeout accepted at `c3353fb...`.
- `devframe-control-plane`: frozen and still aligned at `7939954...`.

This makes a grouped parent pin possible if the coordinator proceeds with the
already requested authorization. This review itself does not mutate pins.

## 2. Fresh Pin Candidate Matrix

| Module | Locked commit | Observed commit | Worktree | Parent intake state | Pin state |
|---|---|---|---|---|---|
| `agent-acceptance` | `3cf2c9be9f33ddabdc029a652dca512d8193a5e5` | `b9bb53a72bbd7b4c4e4402aca11b4cc67f9506f5` | old untracked evidence remains | parent canary gate accepted | candidate with dirty-note |
| `dev-frame-opencode` | `0c24204fd99e6cab1d853ecadb12200244119fe1` | `6bd9809cc635e58e066cb0b3d1f38c2534b03d7a` | clean | metadata scope limits accepted for intake | candidate |
| `devframe-control-plane` | `79399541b8426cff0f362b665bad09e3c23e974b` | `79399541b8426cff0f362b665bad09e3c23e974b` | clean | frozen aligned baseline | keep frozen |
| `test-frame` | `bdd7b67a4bb9cfee2c6601c2f755abfd68164da7` | `c3353fb34900aa24f56df5b9c9230f3249d6c01a` | clean | closeout milestone accepted for intake | candidate |

## 3. Accepted Intake Reports

- `integration/reports/parent-canary-agent-acceptance-return-review-2026-06-15.md`
- `integration/reports/opencode-zotero-metadata-scope-limits-return-review-2026-06-15.md`
- `integration/reports/test-frame-readiness-closeout-return-review-2026-06-15.md`

Supporting historical intake reports:

- `integration/reports/opencode-zotero-metadata-export-hardening-return-review-2026-06-15.md`
- `integration/reports/opencode-zotero-ris-metadata-parser-return-review-2026-06-15.md`
- `integration/reports/parent-canary-test-frame-return-review-2026-06-15.md`
- `integration/reports/parent-canary-combined-intake-review-2026-06-15.md`

## 4. Current Candidate Pin Set

If the coordinator proceeds, the grouped parent pin set should use:

- `agent-acceptance` ->
  `b9bb53a72bbd7b4c4e4402aca11b4cc67f9506f5`
- `dev-frame-opencode` ->
  `6bd9809cc635e58e066cb0b3d1f38c2534b03d7a`
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

- If the coordinator wants integration now, update parent gitlinks and lock
  files to the A7 candidate set, then run parent diff/submodule verification.

Safe alternative:

- Keep all pins held and continue module self-iteration until a larger
  milestone is requested.
