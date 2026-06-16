# Local Paper RAG Draft Artifacts

## Current Recommended Artifact

Use this package for normal human review:

- `integration/artifacts/paper-drafts/local-paper-rag-review-variants-v1.1-package.zip`

SHA256:

- `2731FE77DB74BBDF29822AFEB401B25B09431FC93D942C44B1080884918AC574`

Recommended first DOCX:

- `integration/artifacts/paper-drafts/local-paper-rag-short-paper-v1.1.docx`

Human review route:

- `integration/artifacts/paper-drafts/local-paper-rag-human-review-route-v1.1.md`

Verify with:

```powershell
python scripts\verify_local_paper_rag_final_review_v1_1.py --root D:\devframe-system
```

Expected output:

```text
PASS_LOCAL_PAPER_RAG_FINAL_REVIEW_V1_1_VERIFICATION
passed=109 failed=0
```

Previous main manuscript:

- `integration/artifacts/paper-drafts/local-paper-rag-clean-manuscript-v1.0.docx`

Use this file when Markdown editing is preferred:

- `integration/artifacts/paper-drafts/local-paper-rag-clean-manuscript-v1.0.md`

Use this package for handoff:

- `integration/artifacts/paper-drafts/local-paper-rag-clean-manuscript-v1.0-package.zip`

The v1.0 clean manuscript is the current reviewer-facing draft. It preserves the
v0.9 human-review improvements and additionally normalizes sequential citation
order, adds reference-format audit materials, usage profiles, and explicit
claim/non-claim boundaries.

## v1.0 Review Supplements

- `gbt7714-preflight-v1.0.md`
- `submission-decision-matrix-v1.0.md`
- `reference-format-audit-v1.0.md`
- `references-needs-human-check-v1.0.md`
- `usage-profile-short-paper-v1.0.md`
- `usage-profile-technical-note-v1.0.md`
- `usage-profile-internal-brief-v1.0.md`
- `allowed-claims-v1.0.md`
- `non-claim-boundary-v1.0.md`
- `v1.0-verification-risk-checklist.md`

## v1.0 Review Variants

Use these when the target form is known:

- Short paper:
  `local-paper-rag-short-paper-v1.0.docx`
- Technical note:
  `local-paper-rag-technical-note-v1.0.docx`
- Internal research brief:
  `local-paper-rag-internal-brief-v1.0.docx`

Variant source manifest:

- `local-paper-rag-review-variants-v1.0-manifest.json`

Variant handoff package:

- `local-paper-rag-review-variants-v1.0-package.zip`

SHA256:

- `60ABD31ED49B7325B7BAE69002577FCB17D15CFDC865AA999BC6AC5AE3F4A42F`

Verify with:

```powershell
python scripts\verify_local_paper_rag_review_variants_v1_0.py --root D:\devframe-system
```

## Latest Hashes

- v1.0 clean DOCX:
  `C92DDF4D53D4E6C16E101580C138626B3911B73959D362964395E259FAA399E8`
- v1.0 clean Markdown:
  `E6AEB7B8CBF45D038EAB12DDCEA3ABB7FFB2F808E6CD0209665D0AEE31E5640C`
- v1.0 package ZIP:
  `88657D835CDEDAFFAF52943C9175F9D659AE2A61A09ED23BFBD147093138DCF4`
- v1.0 submission-prep ZIP:
  `8433B733FEEFE22D2EF48AD8C365D329C6900BDAC6BD2FCE9CBD532912DFB40F`
- v1.0 review-variants ZIP:
  `60ABD31ED49B7325B7BAE69002577FCB17D15CFDC865AA999BC6AC5AE3F4A42F`

## Supporting Review Artifacts

- v0.9 clean manuscript:
  `integration/artifacts/paper-drafts/local-paper-rag-clean-manuscript-v0.9.docx`
- v0.8 clean manuscript:
  `integration/artifacts/paper-drafts/local-paper-rag-clean-manuscript-v0.8.docx`
- v0.7 clean manuscript:
  `integration/artifacts/paper-drafts/local-paper-rag-clean-manuscript-v0.7.docx`
- v0.6 clean manuscript:
  `integration/artifacts/paper-drafts/local-paper-rag-clean-manuscript-v0.6.docx`
- v0.5 clean manuscript:
  `integration/artifacts/paper-drafts/local-paper-rag-clean-manuscript-v0.5.docx`
- v0.4 reviewer draft with internal boundaries:
  `integration/artifacts/paper-drafts/local-paper-rag-reviewer-draft-v0.4.md`

## Boundary

These are draft paper artifacts. They do not claim final paper-quality
acceptance, final training-effect acceptance, final governance acceptance,
production readiness, broad/general RAG readiness, whole-vault readiness,
external/private RAG readiness, or RuntimeAuthorization.
