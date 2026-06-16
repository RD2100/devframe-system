# Parent Pin Review: Test-Frame Local Paper RAG Hybrid Rerank Consumption

## Decision

`ACCEPTED_AND_PARENT_PINNED`

The parent pins `test-frame` to:

`1cd659f7f5b8f7edfda81fffa994a188fda8bf5d`

## Parent Updates

- Updated `BASELINE_LOCK.json`
- Updated `integration/lock/submodules.lock.yml`
- Added `integration/reports/test-frame-local-paper-rag-hybrid-rerank-consumption-return-review-2026-06-16.md`
- Added this parent pin review
- Staged the `test-frame` gitlink directly with `git update-index --cacheinfo` to avoid visible checkout drift.

## Evidence Checked

- Evidence ZIP: `D:\devframe-system\test-frame\reports\evidence-opencode-local-paper-rag-hybrid-rerank-consumption-a1.zip`
- SHA256: `B554D2D6FA681233E26ED1324EAA3C86705C8D01A79D8B17251C749BBEA21426`
- ZIP entries: command summaries, manifest, ExecutionReport, Reviewer Index, and status summary only.

## Verification Summary

- Fixture JSON parse: PASS
- Focused test: 11 passed
- Local RAG consumption regression: 34 passed
- Evidence collector/manifest plus local RAG consumption regression: 59 passed
- Evidence manifest JSON parse: PASS
- Diff check: PASS, CRLF warning only

## Non-Final Boundary

The pinned test-frame commit validates minimized hybrid-rerank evidence only. It does not make the RAG pipeline final, paper-quality accepted, production-ready, broad/general RAG-ready, whole-vault-ready, external/private RAG-ready, cloud-ready, or RuntimeAuthorization-granted.

## Next Recommended Parent Action

Dispatch an agent-acceptance governance review for the opencode plus test-frame hybrid-rerank chain, then create a parent closeout if accepted.
