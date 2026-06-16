# Parent Current Local Paper RAG Usable Pipeline Milestone Closeout

## Verdict

`LOCAL_PAPER_RAG_USABLE_PIPELINE_CLOSED_AS_NON_FINAL_MILESTONE_CANDIDATE`

The parent now has a pinned, reviewable local paper RAG usable pipeline milestone across implementation, verification consumption, and governance review.

This is not final governance acceptance, paper-quality acceptance, production readiness, broad live readiness, whole-vault readiness, general RAG readiness, external/private RAG readiness, cloud vector DB readiness, cloud readiness, or RuntimeAuthorization.

## Parent Pins

| Module | Commit | Parent intake |
|---|---:|---|
| `dev-frame-opencode` | `7c13ff0de6de8c50706b77efb58b132bce27dce0` | `ffc571c Pin opencode local paper RAG usable pipeline` |
| `test-frame` | `210e47d9353736347e2fbafedc0d67312789b0bb` | `9873363 Pin test-frame local paper RAG usable pipeline consumption` |
| `agent-acceptance` | `c8e73a2a983bf41ce183be40ebb7364803b3e25e` | `6d3bc8c Pin agent-acceptance local paper RAG usable pipeline governance review` |

## What Is Working

The local paper RAG pipeline has a usable scoped loop:

- Discovers PDFs from the authorized local paper area.
- Generates local Markdown notes.
- Builds a local FAISS index.
- Stores local runtime state for source fingerprints and refresh decisions.
- Runs retrieval probes over the local index.
- Proves a second run can reuse the existing index when sources are unchanged.
- Produces minimized reports and manifests without raw private content in evidence ZIPs.

Observed opencode smoke facts:

- First run status: `PASS_LOCAL_RAG_PIPELINE`
- PDF count: 6
- Markdown note count: 13
- Document count: 6
- Chunk count: 47
- Source fingerprint count: 19
- First run: 19 new, 0 changed, 0 unchanged, 0 deleted; refresh required and completed; index rebuilt
- Second run: 0 new, 0 changed, 19 unchanged, 0 deleted; refresh not required; index reused
- Retrieval query count: 3
- Retrieval success count: 3
- Top-k result total: 9
- Warnings: 0

## Evidence Chain

### Implementation Evidence

- ZIP: `D:\devframe-system\.agent\evidence\evidence-opencode-local-paper-rag-usable-pipeline-a1-7c13ff0.zip`
- SHA256: `BA8AD8D6E9E012D17A2CE0EA71FDB478232907D6806470801DC6B4A8C1159B9A`
- Scope: repeatable local RAG pipeline implementation and live/local smoke.

### Verification Consumption Evidence

- ZIP: `D:\devframe-system\test-frame\reports\evidence-opencode-local-paper-rag-usable-pipeline-consumption-a1.zip`
- SHA256: `7ADA51DC43E213022A935730E96CD947940278CA5D4E275FA9CD10A39C119372`
- Scope: synthetic/offline consumption validation for minimized first-run and rerun evidence.
- Focused tests: 12 passed
- Related RAG regression: 35 passed

### Governance Review Evidence

- ZIP: `D:\devframe-system\.agent\evidence\evidence-agent-acceptance-local-paper-rag-usable-pipeline-governance-review-a1-c8e73a2.zip`
- SHA256: `C6FE3FB9D9A5753AEDB97634F18A2CD86A838848EE31D3D45D8DF724079ADF17`
- Verdict: `LOCAL_PAPER_RAG_USABLE_PIPELINE_ACCEPTED_AS_NON_FINAL_MILESTONE_CANDIDATE`

## Boundary

Evidence ZIPs exclude raw PDF text, raw Markdown bodies, raw chunks, raw query text, raw source paths, vectors, FAISS binaries, secrets, API keys, and raw WriteLab payload/response.

Runtime Markdown, index, and state artifacts remain local runtime artifacts and are not treated as review evidence payloads.

No cloud LLM, cloud vector DB, external/private RAG service, browser/CDP/cloud/MiniApp, Zotero key/API, whole-vault scan, or parent-side live runtime expansion is authorized by this milestone.

## Current Parent State Notes

`BASELINE_LOCK.json` and `integration/lock/submodules.lock.yml` pin the three milestone modules listed above.

The visible `test-frame` checkout currently contains unrelated later local drift. The parent pinned the intended test-frame consumption commit via the gitlink/lock and did not include that unrelated checkout drift in the milestone evidence.

`.agent/PROJECT_REGISTRY.json` remains local runtime/workspace registry drift and is excluded from this closeout.

## What Remains

The milestone does not yet prove:

- paper-quality acceptance or answer-quality scoring;
- retrieval ranking quality across a broader corpus;
- whole-vault indexing;
- scheduled/incremental background refresh;
- user-facing Obsidian workflow polish;
- external/private RAG service integration;
- cloud vector DB integration;
- production deployment readiness;
- final governance acceptance.

## Practical Next Steps

1. Run a small human quality spot-check over retrieved passages and generated answers.
2. Add a refresh command or task wrapper for routine local re-indexing.
3. Decide whether the next expansion is whole-vault Obsidian, quality evaluation, or UI/workflow packaging.
4. Keep any broader vault, external RAG, cloud, or production move behind a fresh scoped TaskSpec and RuntimeAuthorization boundary.
