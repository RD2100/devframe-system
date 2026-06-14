# Minimal Integration DAG v2.1

Date: 2026-06-15

```mermaid
flowchart TD
  A["S00: Baseline inventory"] --> B["S01: /rdinit governance bootstrap"]
  B --> C["S02: Integration contracts"]
  B --> D["S03: Readonly CI and inventory"]
  C --> E["S04: A120 independent ZIP verifier"]
  C --> F["S05: opencode adapter contract"]
  C --> G["S06: test-frame adapter contract"]
  C --> H["S07: control-plane lease and source-lock contract"]
  E --> I["S08: Canary negative matrix"]
  F --> I
  G --> I
  H --> I
  I --> J["S09: Dry-run dispatch"]
  J --> K["S10: Human-gated live pilot"]
```

## Serial Dependencies

1. Baseline inventory must precede all runtime discussion.
2. `/rdinit` governance must precede TaskSpec and review contracts.
3. Independent ZIP verification must precede A120 acceptance claims.
4. Dry-run dispatch must precede live runtime.
5. Human authorization must precede live CDP, OpenCode, or external test-frame use.

## Parallel Work

- Integration contracts, readonly CI, and risk register can proceed in parallel.
- ZIP verifier, opencode adapter mapping, test-frame adapter mapping, and
  control-plane lease/source-lock contract can proceed after contracts are stable.
