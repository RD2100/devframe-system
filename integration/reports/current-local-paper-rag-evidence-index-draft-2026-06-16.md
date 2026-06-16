# Current Local Paper RAG Evidence Index Draft

Date: 2026-06-16

Status: `CURRENT_INDEX_CANDIDATE`

Parent root: `D:\devframe-system`

Parent basis observed by this worker:

- branch: `codex/rdinit-phase-0-5`
- HEAD: `da015e6 Add local paper RAG submission prep packet`
- scope: metadata/report/hash/package-list indexing plus post-draft variant promotion update

## Purpose

This draft indexes the current local paper RAG closeout evidence without changing
the canonical delivery files. It is intended as a practical parent-thread aid for
closeout review.

This draft does not introduce new runtime behavior, new authorization, new
claims, or new evidence. It should not be read as final governance acceptance,
paper-quality acceptance, production readiness, broad/general RAG readiness,
whole-vault readiness, cloud vector DB readiness, or RuntimeAuthorization.

## Read Boundary

Read or inspected by this worker:

- `CURRENT_DELIVERY.md`
- verifier JSON reports under `integration/reports/local-paper-rag-*-verification/`
- selected parent/opencode/test-frame/agent-acceptance return-review reports
- selected ZIP file hashes
- selected ZIP central-directory entry lists
- `git status --short --untracked-files=all`
- parent branch, HEAD, and submodule status

Not read or expanded:

- raw PDFs
- raw Markdown bodies for paper/source content
- raw chunks
- raw query text
- raw source paths
- vectors or FAISS binaries
- secrets, browser/CDP/cloud/MiniApp runtime payloads, or raw WriteLab payloads

## Canonical Current Delivery

`CURRENT_DELIVERY.md` is still the canonical current delivery pointer.

Current reviewer-facing paper draft:

| Artifact | Path | SHA256 | Size |
|---|---|---:|---:|
| DOCX | `integration/artifacts/paper-drafts/local-paper-rag-clean-manuscript-v1.0.docx` | `C92DDF4D53D4E6C16E101580C138626B3911B73959D362964395E259FAA399E8` | 6627 |
| Markdown copy | `integration/artifacts/paper-drafts/local-paper-rag-clean-manuscript-v1.0.md` | `E6AEB7B8CBF45D038EAB12DDCEA3ABB7FFB2F808E6CD0209665D0AEE31E5640C` | 11308 |
| Handoff ZIP | `integration/artifacts/paper-drafts/local-paper-rag-clean-manuscript-v1.0-package.zip` | `88657D835CDEDAFFAF52943C9175F9D659AE2A61A09ED23BFBD147093138DCF4` | 25848 |

Verifier command from `D:\devframe-system`:

```powershell
python scripts\verify_local_paper_rag_v1_0_handoff.py --root D:\devframe-system
```

Expected verifier output:

```text
PASS_LOCAL_PAPER_RAG_V1_0_HANDOFF_VERIFICATION
```

Existing verifier artifacts:

- `integration/reports/local-paper-rag-v1-0-handoff-verification/local-paper-rag-v1-0-handoff-verification.json`
- `integration/reports/local-paper-rag-v1-0-handoff-verification/local-paper-rag-v1-0-handoff-verification.md`
- parent report: `integration/reports/parent-local-paper-rag-v1-0-handoff-verification-a1-2026-06-16.md`

Observed verifier status from JSON/report:

- verdict: `PASS_LOCAL_PAPER_RAG_V1_0_HANDOFF_VERIFICATION`
- checks: 36 passed, 0 failed
- package entry check: PASS

Handoff ZIP entries observed from central directory:

- `ARTIFACTS-README.md`
- `CLOSEOUT-REPORT.md`
- `allowed-claims-v1.0.md`
- `local-paper-rag-clean-manuscript-v1.0.docx`
- `local-paper-rag-clean-manuscript-v1.0.md`
- `non-claim-boundary-v1.0.md`
- `reference-format-audit-v1.0.md`
- `references-needs-human-check-v1.0.md`
- `usage-profile-internal-brief-v1.0.md`
- `usage-profile-short-paper-v1.0.md`
- `usage-profile-technical-note-v1.0.md`
- `v1.0-verification-risk-checklist.md`

## Submission Prep Package

Submission prep supplement:

| Artifact | Path | SHA256 | Size |
|---|---|---:|---:|
| Submission prep ZIP | `integration/artifacts/paper-drafts/local-paper-rag-submission-prep-v1.0-package.zip` | `8433B733FEEFE22D2EF48AD8C365D329C6900BDAC6BD2FCE9CBD532912DFB40F` | 19667 |

Verifier command from `D:\devframe-system`:

```powershell
python scripts\verify_local_paper_rag_submission_prep_v1_0.py --root D:\devframe-system
```

Expected verifier output:

```text
PASS_LOCAL_PAPER_RAG_SUBMISSION_PREP_V1_0_VERIFICATION
```

Existing verifier artifacts:

- `integration/reports/local-paper-rag-submission-prep-v1-0-verification/local-paper-rag-submission-prep-v1-0-verification.json`
- `integration/reports/local-paper-rag-submission-prep-v1-0-verification/local-paper-rag-submission-prep-v1-0-verification.md`
- parent report: `integration/reports/parent-local-paper-rag-submission-prep-verification-a1-2026-06-16.md`

Observed verifier status from JSON/report:

- verdict: `PASS_LOCAL_PAPER_RAG_SUBMISSION_PREP_V1_0_VERIFICATION`
- checks: 10 passed, 0 failed
- package entry check: PASS

Submission prep ZIP entries observed from central directory:

- `SUBMISSION-PREP-README.md`
- `allowed-claims-v1.0.md`
- `gbt7714-preflight-v1.0.md`
- `local-paper-rag-clean-manuscript-v1.0.docx`
- `local-paper-rag-clean-manuscript-v1.0.md`
- `non-claim-boundary-v1.0.md`
- `reference-format-audit-v1.0.md`
- `references-needs-human-check-v1.0.md`
- `submission-decision-matrix-v1.0.md`

## Opencode Local Paper RAG Evidence ZIPs

These are minimized opencode evidence ZIPs. Hashes below were checked with
`Get-FileHash -Algorithm SHA256`, and entry lists were inspected from ZIP central
directories without expanding payload bodies.

| Slice | Source evidence ZIP | SHA256 | Size | Entry status | Key status |
|---|---|---:|---:|---|---|
| closed-loop upstream | `.agent/evidence/evidence-opencode-local-paper-rag-closed-loop-a1-22ad943.zip` | `E1EC86F5A87BF02527E23FD582139B3CE7A4F5B969A859DD724C59FC21596B69` | 8196 | PASS, 13 minimized entries | `PASS_LOCAL_PAPER_RAG_CLOSED_LOOP` |
| usable pipeline | `.agent/evidence/evidence-opencode-local-paper-rag-usable-pipeline-a1-7c13ff0.zip` | `BA8AD8D6E9E012D17A2CE0EA71FDB478232907D6806470801DC6B4A8C1159B9A` | 9904 | PASS, 15 minimized entries | `PASS_LOCAL_RAG_PIPELINE` |
| quality eval | `.agent/evidence/evidence-opencode-local-paper-rag-quality-eval-a1-44188cd.zip` | `8C5296FCE736BC8D9AD0F9218EC2B6C598CB85D2FA6897DEF2350E461FF4EDC5` | 7548 | PASS, 13 minimized entries | `PASS_LOCAL_RAG_QUALITY_EVAL` |
| hybrid rerank | `.agent/evidence/evidence-opencode-local-paper-rag-hybrid-rerank-a1-209ac0e.zip` | `BE65898E071DDC351B6B600A97242774190B62D5D9529630706739C0980A0443` | 10217 | PASS, 16 minimized entries | rerank spot-check passed |
| answer preview | `.agent/evidence/evidence-opencode-local-paper-rag-answer-preview-a1-528f5b8.zip` | `F1AB005DBE53429E825E2ACBF58750635744DE7D8A94F978878C9EEABA4F5FB9` | 9111 | PASS, 12 minimized entries | `PASS_LOCAL_RAG_ANSWER_PREVIEW` |

### Opencode Source Reports

- closed-loop: `integration/reports/opencode-local-paper-rag-closed-loop-return-review-2026-06-16.md`
- usable pipeline: `integration/reports/opencode-local-paper-rag-usable-pipeline-return-review-2026-06-16.md`
- quality eval: `integration/reports/opencode-local-paper-rag-quality-eval-return-review-2026-06-16.md`
- hybrid rerank: `integration/reports/opencode-local-paper-rag-hybrid-rerank-return-review-2026-06-16.md`
- answer preview: `integration/reports/opencode-local-paper-rag-answer-preview-return-review-2026-06-16.md`

### Parent Pin Reports

- closed-loop: `integration/reports/parent-pin-review-opencode-local-paper-rag-closed-loop-2026-06-16.md`
- usable pipeline: `integration/reports/parent-pin-review-opencode-local-paper-rag-usable-pipeline-2026-06-16.md`
- quality eval: `integration/reports/parent-pin-review-opencode-local-paper-rag-quality-eval-2026-06-16.md`
- hybrid rerank: `integration/reports/parent-pin-review-opencode-local-paper-rag-hybrid-rerank-2026-06-16.md`
- answer preview: `integration/reports/parent-pin-review-opencode-local-paper-rag-answer-preview-2026-06-16.md`

### Test-Frame Consumption Evidence

These consumption reports accept the opencode evidence as synthetic/offline
verification evidence only.

| Slice | test-frame evidence ZIP | SHA256 | Consumption status |
|---|---|---:|---|
| closed-loop | `test-frame/reports/evidence-opencode-local-paper-rag-closed-loop-consumption-a1.zip` | `EC01E7AE86471EC11640487984BB27FE595952D9B852EBEE54A2AFB32F9FBEFD` | accepted for parent pin |
| usable pipeline | `test-frame/reports/evidence-opencode-local-paper-rag-usable-pipeline-consumption-a1.zip` | `7ADA51DC43E213022A935730E96CD947940278CA5D4E275FA9CD10A39C119372` | PASS, 12 focused tests and 35 regression tests |
| quality eval | `test-frame/reports/evidence-opencode-local-paper-rag-quality-eval-consumption-a1.zip` | `8C935D9EA9877F91FB01A0FF157E1742A80996183DD29262BB9834707BBB53F3` | PASS, 11 focused tests and 46 regression tests |
| hybrid rerank | `test-frame/reports/evidence-opencode-local-paper-rag-hybrid-rerank-consumption-a1.zip` | `B554D2D6FA681233E26ED1324EAA3C86705C8D01A79D8B17251C749BBEA21426` | PASS, 11 focused tests and 59 extended regression tests |
| answer preview | `test-frame/reports/evidence-opencode-local-paper-rag-answer-preview-consumption-a1.zip` | `B091B9C9BFEE25E46515A2C4561A69CBD1A3527BE7E8FEFBA932A6509F9B769E` | PASS, 11 focused tests |

Consumption reports:

- `integration/reports/test-frame-local-paper-rag-closed-loop-consumption-return-review-2026-06-16.md`
- `integration/reports/test-frame-local-paper-rag-usable-pipeline-consumption-return-review-2026-06-16.md`
- `integration/reports/test-frame-local-paper-rag-quality-eval-consumption-return-review-2026-06-16.md`
- `integration/reports/test-frame-local-paper-rag-hybrid-rerank-consumption-return-review-2026-06-16.md`
- `integration/reports/test-frame-local-paper-rag-answer-preview-consumption-return-review-2026-06-16.md`

### Agent-Acceptance Governance Evidence

These governance reports accept the chain only as non-final milestone candidate
evidence.

| Slice | Governance verdict |
|---|---|
| closed-loop | accepted for parent pin; runtime not reproduced by governance review |
| usable pipeline | `LOCAL_PAPER_RAG_USABLE_PIPELINE_ACCEPTED_AS_NON_FINAL_MILESTONE_CANDIDATE` |
| quality eval | `LOCAL_PAPER_RAG_QUALITY_EVAL_ACCEPTED_AS_NON_FINAL_MILESTONE_CANDIDATE` |
| hybrid rerank | `LOCAL_PAPER_RAG_HYBRID_RERANK_ACCEPTED_AS_NON_FINAL_MILESTONE_CANDIDATE` |
| answer preview | `LOCAL_PAPER_RAG_ANSWER_PREVIEW_ACCEPTED_AS_NON_FINAL_MILESTONE_CANDIDATE` |

Governance reports:

- `integration/reports/agent-acceptance-local-paper-rag-closed-loop-governance-review-return-review-2026-06-16.md`
- `integration/reports/agent-acceptance-local-paper-rag-usable-pipeline-governance-review-return-review-2026-06-16.md`
- `integration/reports/agent-acceptance-local-paper-rag-quality-eval-governance-review-return-review-2026-06-16.md`
- `integration/reports/agent-acceptance-local-paper-rag-hybrid-rerank-governance-review-return-review-2026-06-16.md`
- `integration/reports/agent-acceptance-local-paper-rag-answer-preview-governance-review-return-review-2026-06-16.md`

## Verified Local Review Variants

The earlier pending review variants were regenerated and promoted into a
verified parent supplement. The final set is distinct across all three Markdown
variants and is covered by a dedicated verifier.

| Variant artifact | Path | SHA256 |
|---|---|---:|
| short paper DOCX | `integration/artifacts/paper-drafts/local-paper-rag-short-paper-v1.0.docx` | `376D7FA720798DCE82CF8830A2C41313ED0EC513F65645D301DDE9DAB5FA68B9` |
| short paper Markdown | `integration/artifacts/paper-drafts/local-paper-rag-short-paper-v1.0.md` | `B2F36FEF3C2839A06FBC4F1BD1A5EB1C14A8C6BC23488709C3A8B52138D82308` |
| technical note DOCX | `integration/artifacts/paper-drafts/local-paper-rag-technical-note-v1.0.docx` | `0566B1F630A4CD11D7464281A711AD6CAF0BBFE013061154808CB7F4428F5F17` |
| technical note Markdown | `integration/artifacts/paper-drafts/local-paper-rag-technical-note-v1.0.md` | `20D63583ED8163E7B09D075AA318FA37E000F4B5A23C9B0159A15496D03259C1` |
| internal brief DOCX | `integration/artifacts/paper-drafts/local-paper-rag-internal-brief-v1.0.docx` | `1F2093E0091827422501D4B50204117B2DCFF096D10F022715345A60F5A6944D` |
| internal brief Markdown | `integration/artifacts/paper-drafts/local-paper-rag-internal-brief-v1.0.md` | `BB37B3853AF912DE23AF68ACDE2E600654AD9FF771B9A675319D67AC1AAC6887` |
| review variants manifest | `integration/artifacts/paper-drafts/local-paper-rag-review-variants-v1.0-manifest.json` | `4FE00F6C1AC50DF059D2372F4C97E8C938EB8D845129AD0E3B05DCB11BAF13BD` |
| review variants ZIP | `integration/artifacts/paper-drafts/local-paper-rag-review-variants-v1.0-package.zip` | `60ABD31ED49B7325B7BAE69002577FCB17D15CFDC865AA999BC6AC5AE3F4A42F` |

Observed review variants ZIP entries:

- `REVIEW-VARIANTS-README.md`
- `allowed-claims-v1.0.md`
- `local-paper-rag-internal-brief-v1.0.docx`
- `local-paper-rag-internal-brief-v1.0.md`
- `local-paper-rag-review-variants-v1.0-manifest.json`
- `local-paper-rag-short-paper-v1.0.docx`
- `local-paper-rag-short-paper-v1.0.md`
- `local-paper-rag-technical-note-v1.0.docx`
- `local-paper-rag-technical-note-v1.0.md`
- `non-claim-boundary-v1.0.md`
- `submission-decision-matrix-v1.0.md`
- `usage-profile-internal-brief-v1.0.md`
- `usage-profile-short-paper-v1.0.md`
- `usage-profile-technical-note-v1.0.md`

Verifier command from `D:\devframe-system`:

```powershell
python scripts\verify_local_paper_rag_review_variants_v1_0.py --root D:\devframe-system
```

Observed verifier result:

```text
PASS_LOCAL_PAPER_RAG_REVIEW_VARIANTS_V1_0_VERIFICATION
passed=79 failed=0
```

## Known Dirty Drift Not To Mix Into Current Closeout

Observed before this draft was created:

- `.agent/PROJECT_REGISTRY.json` is modified local workspace registry drift.
- `agent-acceptance` and `test-frame` show submodule working tree drift.
- Several existing integration reports are modified, including:
  - `integration/reports/README.md`
  - `integration/reports/opencode-metadata-closeout-coverage-cli-batch-a41-a42-return-review-2026-06-16.md`
  - `integration/reports/opencode-preauth-stage-clock-stability-batch-a61-a62-return-review-2026-06-16.md`
  - `integration/reports/opencode-real-pilot-set-like-fields-batch-a59-a60-return-review-2026-06-16.md`
  - `integration/reports/opencode-zotero-manifest-uniqueness-batch-a63-a64-return-review-2026-06-16.md`
  - `integration/reports/parent-pin-review-opencode-zotero-web-manifest-business-closeout-batch-a37-a38-2026-06-16.md`
  - `integration/reports/parent-pin-review-test-frame-paper-pipeline-metadata-only-dry-run-orchestration-2026-06-16.md`
  - multiple `integration/reports/test-frame-opencode-*` return-review reports.
- Many untracked parent status/drift reports exist under `integration/reports/`.
- Runtime pilot artifacts exist under `integration/reports/runtime-pilots/`,
  including redacted evidence manifests/reports, live-service logs, and one
  synthetic authorized PDF path. These are outside this current local paper RAG
  handoff index and should stay quarantined from closeout claims unless reviewed
  by a dedicated task.
- Python bytecode caches exist under `scripts/__pycache__/` and
  `tests/__pycache__/`.
- The review variants have since been regenerated and promoted as a verified
  supplement, while unrelated runtime-pilot artifacts remain quarantined.

The existing report
`integration/reports/parent-final-verdict-readiness-and-current-drift-2026-06-16.md`
also records a final-verdict stop line of
`FINAL_VERDICT_NOT_READY_METADATA_ONLY_BASELINE_READY`. That boundary should
remain in force: metadata-only passes, ZIP validation, test-frame consumption,
and non-final governance reviews must not be promoted into final acceptance.

## Concise Next Steps For Parent Closeout

1. Keep `CURRENT_DELIVERY.md` as the canonical v1.0 human-review handoff pointer.
2. For current closeout evidence, cite the two verifier commands and their
   existing PASS artifacts rather than re-opening raw content.
3. Treat the opencode/test-frame/agent-acceptance RAG chain as non-final
   milestone evidence only; it supports local pipeline usability, quality-eval
   proxying, deterministic hybrid rerank, and answer-preview review.
4. Use the verified review variants package when a short-paper, technical-note,
   or internal-brief form is preferred.
5. Classify or quarantine current dirty drift before any commit, tag, push, or
   final closeout claim.
6. Do not claim paper-quality acceptance, production readiness, general RAG
   readiness, whole-vault readiness, cloud vector DB readiness, or
   RuntimeAuthorization from the evidence indexed here.

## Worker Verification

Commands run by this worker for this draft:

- `Get-FileHash -Algorithm SHA256` over the canonical handoff artifacts,
  submission prep package, opencode local paper RAG evidence ZIPs, and verified
  review variant artifacts.
- ZIP central-directory entry inspection for handoff, submission prep, opencode
  evidence packages, and review variants package.
- `git status --short --untracked-files=all`
- `git branch --show-current`
- `git rev-parse --short HEAD`
- `git log -1 --oneline`
- `git submodule status`

No files were staged or committed by this worker.
