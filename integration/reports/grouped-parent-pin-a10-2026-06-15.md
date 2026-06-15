# devframe-system Grouped Parent Pin A10

Date: 2026-06-15
Scope: grouped parent gitlink and lock update
Runtime: not executed
Verdict: `GROUPED_PARENT_PIN_A10_APPLIED_PENDING_VERIFICATION`

## 1. Pin Set

The grouped parent pin uses the A10 candidate set:

- `agent-acceptance` ->
  `b9bb53a72bbd7b4c4e4402aca11b4cc67f9506f5`
- `dev-frame-opencode` ->
  `a2cedaa280f12f717d4bf0a64c1c12ece6f5fefe`
- `test-frame` ->
  `c3353fb34900aa24f56df5b9c9230f3249d6c01a`
- `devframe-control-plane` unchanged at
  `79399541b8426cff0f362b665bad09e3c23e974b`

## 2. Basis

Accepted intake reports:

- `integration/reports/parent-canary-agent-acceptance-return-review-2026-06-15.md`
- `integration/reports/opencode-zotero-evidence-manifest-boundary-return-review-2026-06-15.md`
- `integration/reports/test-frame-readiness-closeout-return-review-2026-06-15.md`

The parent sent a HOLD to `dev-frame-opencode` before pin so the parent would
not chase another moving head.

## 3. Files Updated

- parent submodule gitlinks for `agent-acceptance`, `dev-frame-opencode`, and
  `test-frame`
- `integration/lock/submodules.lock.yml`
- `BASELINE_LOCK.json`

## 4. Boundary

This pin does not authorize:

- real Zotero export/API/plugin/storage;
- real Obsidian, RAG, PDF/full text, WriteLab;
- real MiniApp runtime, WeChat DevTools, miniprogram-automator, Jest E2E;
- H5, MeterSphere, cloud, Android, browser/CDP product runtime;
- final governance acceptance.

All pinned evidence remains local/offline/synthetic/candidate evidence unless
separately reviewed and authorized.

## 5. Required Verification

After applying this pin, run:

- `git submodule status`
- `git ls-files -s agent-acceptance dev-frame-opencode devframe-control-plane test-frame`
- `git diff --check`
- `git diff --submodule=log --cached`
- JSON/YAML parse checks for the updated lock files
