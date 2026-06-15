# Parent Pin Review A28

Date: 2026-06-15
Reviewer: parent devframe-system coordinator
Scope: parent gitlink and lock update

## Verdict

Status: `A28_OPENCODE_ZOTERO_METADATA_EXPORT_SANITIZER_PIN_REVIEW_PASS`

Parent pin is accepted for the clean committed `dev-frame-opencode` head:

`c31e490d7297d192f0e7d6b3fd591a36e998ff3b`

## Pin Set After A28

- `agent-acceptance`:
  `75f8eb329778d4a8cffb28f6ba79b137038d4fed`
- `dev-frame-opencode`:
  `c31e490d7297d192f0e7d6b3fd591a36e998ff3b`
- `devframe-control-plane`:
  `79399541b8426cff0f362b665bad09e3c23e974b`
- `test-frame`:
  `c3353fb34900aa24f56df5b9c9230f3249d6c01a`

## Files Updated

- `BASELINE_LOCK.json`
- `integration/lock/submodules.lock.yml`
- `integration/reports/README.md`
- `integration/PROJECT_COMPLETENESS_PLAN.md`
- `integration/reports/opencode-zotero-metadata-export-sanitizer-return-review-2026-06-15.md`
- `integration/reports/parent-pin-review-a28-2026-06-15.md`
- parent gitlink for `dev-frame-opencode`

## Parent-Side Checks Run

- `Get-FileHash -Algorithm SHA256 .agent\evidence\evidence-opencode-zotero-metadata-export-sanitizer-a1-c31e490.zip`
  returned
  `1FD920A89BF9D902257E80BD3AA4A182E1BF14143E71A17999051325268AFC2C`.
- evidence ZIP `EXECUTION_REPORT.md` and `REVIEWER_INDEX.md` read; both keep
  the local/offline-only and no-final-acceptance boundary.
- from `D:\devframe-system\dev-frame-opencode\ai-workflow-hub`:
  `python -m pytest tests\test_paper_real_zotero_metadata_only_pilot.py -q`
  returned `27 passed`.
- from `D:\devframe-system\dev-frame-opencode\ai-workflow-hub`:
  focused real-pilot/business pytest suite returned `83 passed`.
- from `D:\devframe-system\dev-frame-opencode`:
  `python -m json.tool schemas\paper_real_zotero_metadata_only_pilot_report.schema.json`
  passed.
- from `D:\devframe-system\dev-frame-opencode`:
  `git diff --check HEAD~1 HEAD` passed.

## Boundary

This pin does not authorize or execute real Zotero application/API access,
Obsidian, RAG, WriteLab, MiniApp, browser/CDP, cloud, PDF, attachment,
full-text, or private paper runtime.

This pin does not make the paper workflow live-ready and does not create final
acceptance.

## Product Decision Captured

The software now sanitizes ordinary user-provided Zotero/BibTeX exports instead
of requiring users to produce perfectly clean files manually. Sanitized exports
may pass the metadata-only local/offline pilot when forbidden raw fields can be
removed safely.
