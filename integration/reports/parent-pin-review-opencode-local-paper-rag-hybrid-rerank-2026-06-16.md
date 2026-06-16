# Parent Pin Review: Opencode Local Paper RAG Hybrid Rerank

## Decision

`ACCEPTED_AND_PARENT_PINNED`

The parent pins `dev-frame-opencode` to:

`209ac0e0417338c332af59a342fcf5c8a19b51af`

## Parent Updates

- Updated `BASELINE_LOCK.json`
- Updated `integration/lock/submodules.lock.yml`
- Added `integration/reports/opencode-local-paper-rag-hybrid-rerank-return-review-2026-06-16.md`
- Added this parent pin review
- Staged the `dev-frame-opencode` gitlink

## Evidence Checked

- Evidence ZIP: `D:\devframe-system\.agent\evidence\evidence-opencode-local-paper-rag-hybrid-rerank-a1-209ac0e.zip`
- SHA256: `BE65898E071DDC351B6B600A97242774190B62D5D9529630706739C0980A0443`
- ZIP entries: hybrid pipeline report/manifest, hybrid quality eval report/manifest, schema, command logs, changed-files list, ExecutionReport, and Reviewer Index.

## Verification Summary

- ZIP hash matched declared SHA256.
- ZIP entry list was inspected.
- Focused local paper RAG pipeline test passed: 6 passed.
- Schema JSON parsed successfully.
- Commit range diff check passed.
- Minimized report inspection confirmed the Q4-style rerank spot-check passed and overclaim booleans stayed false.

## Non-Final Boundary

The pinned slice addresses the current local RAG usability gap found in parent human spot-check: the virtual-scene Q4-style source routing now has deterministic hybrid rerank evidence.

This remains non-final candidate evidence. It does not grant final governance acceptance, paper-quality acceptance, production readiness, broad/general RAG readiness, whole-vault readiness, external/private RAG readiness, cloud vector DB readiness, cloud readiness, RuntimeAuthorization, or broader private content access.

## Next Recommended Parent Action

Dispatch test-frame consumption for the pinned hybrid rerank minimized evidence, then run agent-acceptance governance review or parent closeout after the consumption gate passes.
