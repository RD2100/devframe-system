# Current Delivery

## Use This Artifact

Current recommended human-review package:

- `integration/artifacts/paper-drafts/local-paper-rag-review-variants-v1.1-package.zip`

SHA256:

- `2731FE77DB74BBDF29822AFEB401B25B09431FC93D942C44B1080884918AC574`

Use these files first:

- Short paper: `integration/artifacts/paper-drafts/local-paper-rag-short-paper-v1.1.docx`
- Technical note: `integration/artifacts/paper-drafts/local-paper-rag-technical-note-v1.1.docx`
- Internal research brief: `integration/artifacts/paper-drafts/local-paper-rag-internal-brief-v1.1.docx`
- Human review route: `integration/artifacts/paper-drafts/local-paper-rag-human-review-route-v1.1.md`

Previous reviewer-facing main draft:

- `integration/artifacts/paper-drafts/local-paper-rag-clean-manuscript-v1.0.docx`

Markdown copy:

- `integration/artifacts/paper-drafts/local-paper-rag-clean-manuscript-v1.0.md`

Handoff package:

- `integration/artifacts/paper-drafts/local-paper-rag-clean-manuscript-v1.0-package.zip`

Review variants package:

- `integration/artifacts/paper-drafts/local-paper-rag-review-variants-v1.1-package.zip`

Use these v1.0 files only when comparing history:

- Short paper: `integration/artifacts/paper-drafts/local-paper-rag-short-paper-v1.0.docx`
- Technical note: `integration/artifacts/paper-drafts/local-paper-rag-technical-note-v1.0.docx`
- Internal research brief: `integration/artifacts/paper-drafts/local-paper-rag-internal-brief-v1.0.docx`

## Current Verdict

`SHIP_V1_1_FOR_HUMAN_REVIEW_NON_FINAL`

Fast parallel closeout plan:

- `integration/reports/current-local-paper-rag-fast-parallel-closeout-plan-2026-06-16.md`

Current parent closeout and evidence index:

- `integration/reports/current-local-paper-rag-v1-1-final-closeout-2026-06-16.md`
- `integration/reports/current-local-paper-rag-v1-1-evidence-index-2026-06-16.md`

Previous v1.0 handoff verdict retained for compatibility with the v1.0 verifier:

`SHIP_V1_0_FOR_HUMAN_REVIEW_NON_FINAL`

This means the current local paper RAG pipeline has produced a practical
human-review deliverable. v1.1 adds a clean review route, fixed manifest metadata,
and a smaller final review package. It does not mean final paper-quality acceptance,
training-effect acceptance, production readiness, broad RAG readiness, whole-vault
readiness, or RuntimeAuthorization.

## One-Command Check

Run from `D:\devframe-system`:

```powershell
python scripts\verify_local_paper_rag_v1_0_handoff.py --root D:\devframe-system
python scripts\verify_local_paper_rag_final_review_v1_1.py --root D:\devframe-system
```

Expected output:

```text
PASS_LOCAL_PAPER_RAG_V1_0_HANDOFF_VERIFICATION
PASS_LOCAL_PAPER_RAG_FINAL_REVIEW_V1_1_VERIFICATION
```

Verifier outputs:

- `integration/reports/local-paper-rag-v1-0-handoff-verification/local-paper-rag-v1-0-handoff-verification.json`
- `integration/reports/local-paper-rag-v1-0-handoff-verification/local-paper-rag-v1-0-handoff-verification.md`
- `integration/reports/local-paper-rag-final-review-v1-1-verification/local-paper-rag-final-review-v1-1-verification.json`
- `integration/reports/local-paper-rag-final-review-v1-1-verification/local-paper-rag-final-review-v1-1-verification.md`

## Key Hashes

- DOCX:
  `C92DDF4D53D4E6C16E101580C138626B3911B73959D362964395E259FAA399E8`
- Markdown:
  `E6AEB7B8CBF45D038EAB12DDCEA3ABB7FFB2F808E6CD0209665D0AEE31E5640C`
- Handoff ZIP:
  `88657D835CDEDAFFAF52943C9175F9D659AE2A61A09ED23BFBD147093138DCF4`

## Included Review Supplements

- `integration/artifacts/paper-drafts/reference-format-audit-v1.0.md`
- `integration/artifacts/paper-drafts/references-needs-human-check-v1.0.md`
- `integration/artifacts/paper-drafts/gbt7714-preflight-v1.0.md`
- `integration/artifacts/paper-drafts/submission-decision-matrix-v1.0.md`
- `integration/artifacts/paper-drafts/usage-profile-short-paper-v1.0.md`
- `integration/artifacts/paper-drafts/usage-profile-technical-note-v1.0.md`
- `integration/artifacts/paper-drafts/usage-profile-internal-brief-v1.0.md`
- `integration/artifacts/paper-drafts/allowed-claims-v1.0.md`
- `integration/artifacts/paper-drafts/non-claim-boundary-v1.0.md`
- `integration/artifacts/paper-drafts/v1.0-verification-risk-checklist.md`

## Submission Prep Supplement

GB/T 7714 and use-case preflight package:

- `integration/artifacts/paper-drafts/local-paper-rag-submission-prep-v1.0-package.zip`

SHA256:

- `8433B733FEEFE22D2EF48AD8C365D329C6900BDAC6BD2FCE9CBD532912DFB40F`

Verify with:

```powershell
python scripts\verify_local_paper_rag_submission_prep_v1_0.py --root D:\devframe-system
```

## Review Variants Supplement

Three v1.1 use-case variants are available for faster human review:

- Short paper draft:
  `integration/artifacts/paper-drafts/local-paper-rag-short-paper-v1.1.docx`
- Technical note draft:
  `integration/artifacts/paper-drafts/local-paper-rag-technical-note-v1.1.docx`
- Internal research brief:
  `integration/artifacts/paper-drafts/local-paper-rag-internal-brief-v1.1.docx`

Review-variants package:

- `integration/artifacts/paper-drafts/local-paper-rag-review-variants-v1.1-package.zip`

SHA256:

- `2731FE77DB74BBDF29822AFEB401B25B09431FC93D942C44B1080884918AC574`

Verify with:

```powershell
python scripts\verify_local_paper_rag_final_review_v1_1.py --root D:\devframe-system
```

Expected output:

```text
PASS_LOCAL_PAPER_RAG_FINAL_REVIEW_V1_1_VERIFICATION
passed=109 failed=0
```

## Submission Candidate Supplement

Generic GB/T-style submission candidate package:

- `integration/artifacts/paper-drafts/local-paper-rag-submission-candidate-v1.2-package.zip`

SHA256:

- `FBFF4C4BF77EA31FF4B9415E07413CF741B058DECF756C52877EE0EB40A76AF5`

Primary file:

- `integration/artifacts/paper-drafts/local-paper-rag-submission-candidate-v1.2.docx`

Human reference checklist:

- `integration/artifacts/paper-drafts/local-paper-rag-reference-final-check-v1.2.md`

Verify with:

```powershell
python scripts\verify_local_paper_rag_submission_candidate_v1_2.py --root D:\devframe-system
```

Expected output:

```text
PASS_LOCAL_PAPER_RAG_SUBMISSION_CANDIDATE_V1_2_VERIFICATION
passed=52 failed=0
```

This is still a non-final candidate. It requires human reference metadata
checking and target-venue template checking before any submission-ready claim.

## Current Local RAG Evidence

Latest local RAG pipeline evidence accepted for current milestone review:

- Usable pipeline:
  `D:\devframe-system\.agent\evidence\evidence-opencode-local-paper-rag-usable-pipeline-a1-7c13ff0.zip`
  SHA256 `BA8AD8D6E9E012D17A2CE0EA71FDB478232907D6806470801DC6B4A8C1159B9A`
- Quality eval:
  `D:\devframe-system\.agent\evidence\evidence-opencode-local-paper-rag-quality-eval-a1-44188cd.zip`
  SHA256 `8C5296FCE736BC8D9AD0F9218EC2B6C598CB85D2FA6897DEF2350E461FF4EDC5`
- Hybrid rerank:
  `D:\devframe-system\.agent\evidence\evidence-opencode-local-paper-rag-hybrid-rerank-a1-209ac0e.zip`
  SHA256 `BE65898E071DDC351B6B600A97242774190B62D5D9529630706739C0980A0443`
- Answer preview:
  `D:\devframe-system\.agent\evidence\evidence-opencode-local-paper-rag-answer-preview-a1-528f5b8.zip`
  SHA256 `F1AB005DBE53429E825E2ACBF58750635744DE7D8A94F978878C9EEABA4F5FB9`

## Supporting Reports

- v1.0 manuscript closeout:
  `integration/reports/parent-local-paper-rag-clean-manuscript-v1-0-a1-2026-06-16.md`
- v1.0 readiness:
  `integration/reports/parent-current-local-paper-rag-final-readiness-packet-v1-0-2026-06-16.md`
- v1.0 handoff verification:
  `integration/reports/parent-local-paper-rag-v1-0-handoff-verification-a1-2026-06-16.md`

## Human Review Checklist

1. Read the v1.0 DOCX.
2. Choose the use case: short paper, technical note, review-style course paper,
   or internal research brief.
3. If the target is already known, open the matching review-variant DOCX first.
4. Check whether the title, abstract, contribution statement, conclusion, and
   cautious evidence boundary match the intended use case.
5. Review `reference-format-audit-v1.0.md` and manually verify metadata that
   automation cannot safely infer.
6. Decide whether tonight's target is satisfied as a human-review handoff, or
   whether stronger empirical training-effect evidence is required.

## Boundary

The current delivery does not inspect or include raw PDFs, raw Obsidian note
bodies, raw chunks, source paths, vectors, FAISS binaries, WriteLab payloads,
Zotero keys, browser/CDP/cloud/MiniApp runtime content, external RAG services,
or cloud vector DB artifacts.

It does not authorize new live resource access and does not claim final
paper-quality acceptance, training-effect acceptance, production readiness, or
RuntimeAuthorization.
