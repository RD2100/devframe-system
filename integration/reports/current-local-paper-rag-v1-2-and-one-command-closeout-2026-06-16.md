# Current Local Paper RAG Closeout: v1.2 candidate plus one-command runner

Date: 2026-06-16

## Current Verdict

`CURRENT_LOCAL_PAPER_RAG_MILESTONE_READY_FOR_HUMAN_REVIEW`

This is a practical local milestone closeout. It is not final governance
acceptance, paper-quality acceptance, formal submission readiness, production
readiness, whole-vault readiness, broad/general RAG readiness, cloud readiness,
or RuntimeAuthorization.

## What Was Added In This Closeout

The current fast closeout layer includes:

- `b8c50fc Add local paper RAG submission candidate v1.2`
- `bfe4cfd Pin opencode local paper RAG one-command runner`
- `01e3d85 Record local paper RAG one-command reproduction`
- `bad61c9bf8274181a24cb70ed54aad17534c6333` in `agent-acceptance`
  for independent non-final governance review

## User-Visible Deliverables

Submission candidate package:

- `D:\devframe-system\integration\artifacts\paper-drafts\local-paper-rag-submission-candidate-v1.2-package.zip`
- SHA256: `FBFF4C4BF77EA31FF4B9415E07413CF741B058DECF756C52877EE0EB40A76AF5`

Primary manuscript candidate:

- `D:\devframe-system\integration\artifacts\paper-drafts\local-paper-rag-submission-candidate-v1.2.docx`
- `D:\devframe-system\integration\artifacts\paper-drafts\local-paper-rag-submission-candidate-v1.2.md`

Reference and formatting review aids:

- `D:\devframe-system\integration\artifacts\paper-drafts\local-paper-rag-reference-final-check-v1.2.md`
- `D:\devframe-system\integration\artifacts\paper-drafts\local-paper-rag-submission-format-closeout-v1.2.md`
- `D:\devframe-system\integration\artifacts\paper-drafts\local-paper-rag-submission-candidate-v1.2-manifest.json`

One-command local RAG runner:

- submodule: `dev-frame-opencode`
- pinned commit: `a22f3bb68988a2107973c46a2df4dab31def31b8`
- command: `paper local-rag-run`
- evidence ZIP: `D:\devframe-system\.agent\evidence\OPENCODE_LOCAL_PAPER_RAG_ONE_COMMAND_RUNNER_A1-a22f3bb-20260616.zip`
- evidence SHA256: `DF5B07CCAD4A43F06A4C92ED5704458E490738DA484ECB8F8B28D4D9F237A113`

Independent governance review:

- submodule: `agent-acceptance`
- pinned commit: `bad61c9bf8274181a24cb70ed54aad17534c6333`
- verdict: `LOCAL_PAPER_RAG_V1_2_ONE_COMMAND_REPRODUCTION_ACCEPTED_AS_NON_FINAL_MILESTONE_CANDIDATE`
- evidence ZIP: `D:\devframe-system\agent-acceptance\_evidence\AGENT_ACCEPTANCE_LOCAL_PAPER_RAG_V1_2_AND_ONE_COMMAND_REPRODUCTION_GOVERNANCE_REVIEW_A1\evidence-agent-acceptance-local-paper-rag-v1-2-and-one-command-reproduction-governance-review-a1.zip`
- evidence SHA256: `744F83A562CCF89D08AC000398194C78C427F0E68051EF5BB2A8279E41032492`

## How To Re-Run The Current Checks

Submission candidate:

```powershell
python scripts\verify_local_paper_rag_submission_candidate_v1_2.py --root D:\devframe-system
```

Expected:

```text
PASS_LOCAL_PAPER_RAG_SUBMISSION_CANDIDATE_V1_2_VERIFICATION
passed=52 failed=0
```

Prior handoff checks retained:

```powershell
python scripts\verify_local_paper_rag_final_review_v1_1.py --root D:\devframe-system
python scripts\verify_local_paper_rag_v1_0_handoff.py --root D:\devframe-system
python scripts\verify_local_paper_rag_submission_prep_v1_0.py --root D:\devframe-system
python scripts\verify_local_paper_rag_review_variants_v1_0.py --root D:\devframe-system
```

Observed results in this closeout:

- v1.2 candidate: `52 passed, 0 failed`
- v1.1 final review package: `109 passed, 0 failed`
- v1.0 handoff: `36 passed, 0 failed`
- v1.0 submission prep: `10 passed, 0 failed`
- v1.0 review variants: `79 passed, 0 failed`

One-command runner parent intake checks:

- focused pytest: `4 passed`
- adjacent local RAG pytest: `21 passed`
- schema JSON parse: passed
- evidence ZIP hash: matched
- parent `git diff --cached --check`: passed before commit

Real authorized-folder reproduction:

- first run: `PASS_LOCAL_RAG_RUN`, `document_count=6`, `chunk_count=47`,
  `retrieval_success_count=3`, `answer_preview_count=5`
- second run: `PASS_LOCAL_RAG_RUN`, `refresh_required=false`,
  `index_reused=true`
- reproduction report:
  `D:\devframe-system\integration\reports\local-paper-rag-one-command-real-reproduction-2026-06-16.md`

Independent governance review checks:

- v1.2 package ZIP hash: matched
- opencode runner evidence ZIP hash: matched
- ZIP inspection limited to entry names and sizes
- py_compile: passed
- workflow closure pytest: `43 passed`
- git diff checks: passed

## Practical Current Capability

The project can now demonstrate this local loop:

1. Build or reuse local paper RAG artifacts.
2. Run minimized local quality evaluation.
3. Generate deterministic answer-preview evidence.
4. Produce a generic GB/T-style manuscript candidate package for human review.
5. Preserve raw-content safety in evidence packages.
6. Keep final acceptance, paper-quality acceptance, production readiness, broad
   RAG readiness, and RuntimeAuthorization outside automated claims.

## Known Gaps

These are still not done:

- Human reference metadata validation against the original sources.
- Target journal or conference template adaptation.
- Human paper-quality acceptance.
- Independent reproduction of one-command runner against the real authorized PDF
  folder after parent pin.
- Whole-vault Obsidian indexing.
- External/private RAG service integration.
- Cloud vector DB integration.
- Production deployment and monitoring.
- RuntimeAuthorization for broader live-resource operations.

## Important Limitation On The One-Command Runner Evidence

The opencode one-command runner evidence records that its CLI smoke patched the
first-stage pipeline builder to avoid real PDF/vector dependency risk in that
smoke. The parent therefore accepts the slice as:

- a usability entrypoint,
- a minimized runner contract,
- a chain-level PASS/FAIL gate over pipeline, quality-eval, and answer-preview,
- and a local milestone candidate.

It does not by itself prove a fresh real PDF/vector run. The previous accepted
local pipeline, quality-eval, hybrid rerank, and answer-preview milestones remain
the broader evidence base for local pipeline behavior.

## Recommended Next Step

Stop adding small schema hardening. Use the current package for human review:

1. Open `local-paper-rag-submission-candidate-v1.2.docx`.
2. Check title, abstract, conclusion, and reference metadata.
3. Decide whether the target is short paper, technical note, course paper, or
   internal research brief.
4. If the paper target is chosen, run one final target-template formatting slice.
5. If the RAG product target is chosen, run one real-folder reproduction of
   `paper local-rag-run` and record the minimized report.

## Reviewer Index

Parent files added or updated in this closeout:

- `CURRENT_DELIVERY.md`
- `README.md`
- `integration/lock/submodules.lock.yml`
- `integration/artifacts/paper-drafts/local-paper-rag-reference-final-check-v1.2.md`
- `integration/artifacts/paper-drafts/local-paper-rag-submission-candidate-v1.2-manifest.json`
- `integration/artifacts/paper-drafts/local-paper-rag-submission-candidate-v1.2-package.zip`
- `integration/artifacts/paper-drafts/local-paper-rag-submission-candidate-v1.2.docx`
- `integration/artifacts/paper-drafts/local-paper-rag-submission-candidate-v1.2.md`
- `integration/artifacts/paper-drafts/local-paper-rag-submission-format-closeout-v1.2.md`
- `integration/reports/local-paper-rag-submission-candidate-v1-2-verification/local-paper-rag-submission-candidate-v1-2-verification.json`
- `integration/reports/local-paper-rag-submission-candidate-v1-2-verification/local-paper-rag-submission-candidate-v1-2-verification.md`
- `integration/reports/parent-local-paper-rag-submission-candidate-v1-2-a1-2026-06-16.md`
- `integration/reports/parent-pin-review-opencode-local-paper-rag-one-command-runner-a1-2026-06-16.md`
- `integration/reports/local-paper-rag-one-command-real-reproduction-2026-06-16.md`
- `integration/reports/current-local-paper-rag-v1-2-and-one-command-closeout-2026-06-16.md`
- `scripts/build_local_paper_rag_submission_candidate_v1_2.py`
- `scripts/verify_local_paper_rag_submission_candidate_v1_2.py`
- `agent-acceptance` gitlink
- `dev-frame-opencode` gitlink

Suggested review focus:

- Confirm v1.2 manuscript is a candidate, not final submission-ready output.
- Confirm one-command runner is pinned and documented as scoped local evidence.
- Confirm evidence artifacts exclude raw PDF text, raw Markdown bodies, raw
  chunks, raw query text, raw source paths, vectors, FAISS binaries, secrets,
  API keys, and raw WriteLab payloads/responses.
- Confirm remaining human gates are explicit.
