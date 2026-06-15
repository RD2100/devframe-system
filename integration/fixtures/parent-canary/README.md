# Parent Canary Fixtures

Date: 2026-06-15
Scope: synthetic parent-only canary fixtures
Runtime: not executed

These fixtures support the parent negative cases in:

```text
integration/reports/phase-negative-matrix-v1-2026-06-15.md
integration/reports/parent-canary-fixture-plan-v1-2026-06-15.md
```

They are synthetic. They must not contain private paper content, live resource
credentials, real MiniApp data, live Zotero/Obsidian/RAG/WriteLab payloads, or
real browser/CDP runtime output.

Expected usage:

- parent read-only canary checks;
- future `agent-acceptance` negative gates;
- future `test-frame` report validators.

Hard rule:

```text
runtime_allowed=false
```

for every fixture in this directory.
