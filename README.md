# devframe-system

Route A strict-clean superproject for the devframe family.

This repository pins four source repositories as Git submodules. It does not
copy source code across repository boundaries.

## Current Delivery

The active handoff entrypoint is:

- `CURRENT_DELIVERY.md`

Current reviewer-facing paper/RAG artifact:

- `integration/artifacts/paper-drafts/local-paper-rag-review-variants-v1.1-package.zip`

Recommended first DOCX:

- `integration/artifacts/paper-drafts/local-paper-rag-short-paper-v1.1.docx`

One-command verification:

```powershell
python scripts\verify_local_paper_rag_v1_0_handoff.py --root D:\devframe-system
python scripts\verify_local_paper_rag_final_review_v1_1.py --root D:\devframe-system
```

Submission-prep supplement verification:

```powershell
python scripts\verify_local_paper_rag_submission_prep_v1_0.py --root D:\devframe-system
```

Review-variants supplement verification:

```powershell
python scripts\verify_local_paper_rag_review_variants_v1_0.py --root D:\devframe-system
```

Expected result:

```text
PASS_LOCAL_PAPER_RAG_V1_0_HANDOFF_VERIFICATION
passed=36 failed=0
PASS_LOCAL_PAPER_RAG_FINAL_REVIEW_V1_1_VERIFICATION
passed=109 failed=0
```

Review-variants expected result:

```text
PASS_LOCAL_PAPER_RAG_REVIEW_VARIANTS_V1_0_VERIFICATION
passed=79 failed=0
```

Current optional review variants:

- Short paper:
  `integration/artifacts/paper-drafts/local-paper-rag-short-paper-v1.1.docx`
- Technical note:
  `integration/artifacts/paper-drafts/local-paper-rag-technical-note-v1.1.docx`
- Internal brief:
  `integration/artifacts/paper-drafts/local-paper-rag-internal-brief-v1.1.docx`

This is a non-final human-review handoff. It does not claim final
paper-quality acceptance, training-effect acceptance, production readiness,
broad RAG readiness, or RuntimeAuthorization.

## Submodules

| Path | Role | Branch | Pinned commit |
|---|---|---|---|
| `agent-acceptance` | Governance and acceptance framework | `master` | `285d5c906a074ce7c689c8f656caabbdb32af8dc` |
| `devframe-control-plane` | Control-plane runtime candidate | `codex/route-a-baseline-candidate` | `311847818927d3c7ec8c8718949b38c74605fc83` |
| `dev-frame-opencode` | Opencode workflow/runtime candidate | `master` | `3a3aa5722bd6015bec30a8e9190140148b45167c` |
| `test-frame` | Controlled verification runtime candidate | `codex/harden-baseline` | `aeb4a31f770e35e7f698e5c3169406ddba231a4d` |

## Boundary

- Physical merge type: superproject plus submodules.
- No source squashing or monorepo copy was performed.
- No external runtime was executed during bootstrap.
- Each source repository was clean before pinning.
- `dev-frame-opencode` local tests were verified before pinning:
  `python -m pytest tests -q` -> `2451 passed, 2 skipped, 3 warnings`.

## Verify

```powershell
git submodule status --recursive
git status --porcelain=v1 -uall
git diff --check
```
