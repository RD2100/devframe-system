# Project 10-Track Progress Matrix

Date: 2026-06-16
Parent repo: `D:\devframe-system`
Parent HEAD at report time: `8ac3f8c2da55423367f24d999ac5e01b10cbddb9`

## Decision

Status: `NON_FINAL_MILESTONE_CANDIDATE_RUNTIME_PILOTS_RECORDED`

The project has moved past pure schema/mock work. It now has parent-recorded evidence for:

- Zotero Web API metadata-only live access.
- PDF excerpt to local WriteLab scoped smoke.
- Obsidian single allowlisted note runtime pilot.
- RAG single-note deterministic local retrieval manifest.
- `/rdtest` external project intake.
- `D:\order-dish` real local MiniApp E2E verification evidence.

This is still not final governance acceptance, not paper-quality acceptance, not production-ready, and not broad live-ready.

## Current Parent Pins

- `agent-acceptance = 0769485321f3ab733f7315e5f2ff5e44b82d731c`
- `dev-frame-opencode = d4d8a85a54d17c3d787e2e90903776dcf809150e`
- `devframe-control-plane = 09167bc656f8625c97bfae5c52dae5a0280b116c`
- `test-frame = 22b9220cd3620805fe13b28898636cace8d9b158`

## Ten-Track Status

| # | Track | Current Status | Useful Evidence | Remaining Gap |
|---|---|---|---|---|
| 1 | integration superproject | Mostly complete for current milestone | Parent pins and reports through `8ac3f8c`; `integration/lock/submodules.lock.yml`; `BASELINE_LOCK.json` | Dirty report/registry drift still needs final cleanup before a polished release tag. |
| 2 | cross-repo contracts | Mostly complete for current milestone | agent-acceptance rule center, test-frame consumption contracts, opencode schemas, parent lock reports | Need one fresh post-runtime-pilots governance verdict. Task dispatched as `AGENT_ACCEPTANCE_POST_RUNTIME_PILOTS_GOVERNANCE_REVIEW_A1`. |
| 3 | opencode adapter | Strong candidate | Zotero metadata adapter, PDF/WriteLab smoke, Obsidian note pilot, RAG single-note pilot, MVP closeout; latest opencode pin `d4d8a85` | No whole-vault RAG, no external/private RAG service, no production paper-quality verdict. |
| 4 | test-frame adapter / TestRunSpec | Strong for external project intake and evidence validation | `/rdtest` skill/interface parent-pinned; `order-dish` project intake installed; real E2E evidence recorded | `order-dish` evidence is parent-recorded but not a final release verdict; no cloud/payment production matrix. |
| 5 | control-plane state machine conformance | Stable but not recently expanded | Pinned `devframe-control-plane = 09167bc...`; prior security closeout fail-closed behavior | Needs final pass in release closeout to prove no drift from current integration assumptions. |
| 6 | artifact registry / evidence store | Mostly operational | `.agent\evidence` ZIPs, parent reports, EvidenceManifest paths, rdtest evidence packs | Parent has many accumulated untracked/modified report artifacts; needs final evidence index pruning or explicit classification. |
| 7 | RuntimeAuthorization signer / validator | Strong for scoped pilots | RuntimeAuthorization schemas, real pilot authorization packets, PDF/WriteLab scoped auth, Obsidian/RAG scoped task boundaries | No broad authorization; each new live/private resource still requires fresh scoped TaskSpec. |
| 8 | source-level safety review | Partial but meaningful | command policy hardening, raw-sensitive scans, fail-closed negative tests, parent evidence scans | Needs final source-level release review over the small current changed surface, not the whole historical backlog. |
| 9 | dry-run end-to-end harness | Strong plus one real local E2E | metadata pipeline dry-run; paper MVP closeout; `order-dish` real MiniApp E2E: doctor 14/14, Jest 56/56 | Paper pipeline has scoped live smokes, but not a single broad final production E2E. |
| 10 | canary repo + rollback drill | Partial | parent canary fixtures/reports exist from earlier phase; `/rdtest` external target now proven on `D:\order-dish` | Need a compact rollback drill or release-blocker rehearsal if claiming operational readiness. |

## Evidence Added Since Paper MVP Closeout

### Obsidian Single Note

- Parent commit: `c04386e`
- opencode commit: `7f9496310547ceef09e3a6d1e40758d321995fdc`
- Evidence ZIP: `D:\devframe-system\.agent\evidence\evidence-opencode-obsidian-allowlisted-note-runtime-pilot-a1-7f94963.zip`
- SHA256: `6474305DF16CF249918E9FD249B2C085484383A7C2496E551EAC40EBAFA8190C`
- Boundary: one allowlisted Markdown note, minimized counts/facts only, no whole-vault scan.

### RAG Single Note

- Parent commit: `f7bcb3d904fe25a3d9d830820f5d9470b030eecd`
- opencode commit: `d4d8a85a54d17c3d787e2e90903776dcf809150e`
- Evidence ZIP: `D:\devframe-system\.agent\evidence\evidence-opencode-rag-single-note-retrieval-pilot-a1-d4d8a85.zip`
- SHA256: `D4683D043B1917ED1F38D116A1E0D6BBE4763C342A3374122CD8C5E253620D71`
- Boundary: deterministic local single-note retrieval manifest only, no external RAG, embeddings API, vector DB, raw note/chunk/query/path persistence.

### order-dish Real MiniApp E2E

- Parent evidence commit: `8ac3f8c2da55423367f24d999ac5e01b10cbddb9`
- Evidence ZIP: `D:\devframe-system\test-frame\reports\evidence-rdtest-order-dish-real-miniapp-e2e-a1.zip`
- SHA256: `529F8A54949D5CF7D930DF2ACE3B417F3736BBB4DF44FCFA7CD594AD6C9797F6`
- Result: command exit `0`, doctor `14/14`, Jest suites `10/10`, tests `56/56`.
- Boundary: scoped local MiniApp E2E evidence only, no production/cloud/payment readiness.

## Practical Next Steps

1. Wait for `AGENT_ACCEPTANCE_POST_RUNTIME_PILOTS_GOVERNANCE_REVIEW_A1` and parent-intake it if accepted.
2. Produce one parent release-candidate closeout report that references the latest pins and evidence-only E2E result.
3. Run a compact source-level safety review over the current release surface.
4. Decide whether tonight's target is `NON_FINAL_MILESTONE_ACCEPTED` or a stricter `FINAL_GOVERNANCE_ACCEPTANCE`; current evidence supports the former much more safely.

## Boundary

This report does not:

- update submodule pins;
- authorize new runtime;
- read secrets or private raw content;
- claim final governance acceptance;
- claim production readiness;
- claim broad live readiness.
