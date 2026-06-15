# Parent Pin Review A32

Date: 2026-06-16
Reviewer: parent devframe-system coordinator
Scope: parent gitlink and lock update

## Verdict

Status: `A32_OPENCODE_ZOTERO_RDF_XML_PARSER_HARDENING_PIN_REVIEW_PASS`

Parent pin is accepted for the `dev-frame-opencode` Zotero RDF/XML
metadata-only parser hardening commit:

`6b4a3aaf3b8a6b7ee3877014ccc7b6a11f8d639d`

This is an `accepted_with_limitations` metadata-export-file milestone. It is
not final acceptance and does not authorize PDF, attachment, full-text,
Obsidian, RAG, WriteLab, browser/CDP, MiniApp, cloud, or Zotero app/API access.

## Pin Set After A32

- `agent-acceptance`:
  `75f8eb329778d4a8cffb28f6ba79b137038d4fed`
- `dev-frame-opencode`:
  `6b4a3aaf3b8a6b7ee3877014ccc7b6a11f8d639d`
- `devframe-control-plane`:
  `79399541b8426cff0f362b665bad09e3c23e974b`
- `test-frame`:
  `c3353fb34900aa24f56df5b9c9230f3249d6c01a`

## Files Updated

- `BASELINE_LOCK.json`
- `integration/lock/submodules.lock.yml`
- `integration/reports/README.md`
- `integration/PROJECT_COMPLETENESS_PLAN.md`
- `integration/reports/opencode-zotero-rdf-xml-parser-hardening-return-review-2026-06-16.md`
- `integration/reports/parent-pin-review-a32-2026-06-16.md`
- parent gitlink for `dev-frame-opencode`

## Parent-Side Checks Run

- `git -C dev-frame-opencode rev-parse HEAD`
  returned
  `6b4a3aaf3b8a6b7ee3877014ccc7b6a11f8d639d`.
- `git -C dev-frame-opencode cat-file -t 6b4a3aaf3b8a6b7ee3877014ccc7b6a11f8d639d`
  returned `commit`.
- `git ls-tree HEAD dev-frame-opencode` before this pin showed parent tree
  still at `b086ca283fb71b16833acc3461e42a3e2e727456`.
- `git submodule status -- dev-frame-opencode` showed current submodule HEAD
  at `+6b4a3aaf3b8a6b7ee3877014ccc7b6a11f8d639d`.
- `Get-FileHash -Algorithm SHA256` for
  `D:\devframe-system\.agent\evidence\evidence-opencode-zotero-rdf-xml-parser-hardening-a1-6b4a3aa.zip`
  returned
  `5528084DAF73B5D34627AAD2E31C6B6A67E0F421B2F4C8E0EE6A1EA686CEBC06`.

## Boundary

This pin records a user-provided Zotero RDF/XML metadata export file path only.

It does not authorize or execute Zotero app/API/library/storage access,
Obsidian, RAG, WriteLab, MiniApp, browser/CDP, cloud, PDF, attachment,
full-text, private notes, or private paper runtime.

This pin does not make the paper workflow final-ready and does not create final
governance acceptance.

## Known Dirty State

`dev-frame-opencode` contains unrelated dirty files from a parallel security
bugfix path:

- `ai-workflow-hub/configs/execution-policy.yaml`
- `ai-workflow-hub/src/ai_workflow_hub/cli.py`
- `ai-workflow-hub/src/ai_workflow_hub/nodes/tester.py`
- `ai-workflow-hub/src/ai_workflow_hub/project_detect.py`
- `ai-workflow-hub/src/ai_workflow_hub/shell_runner.py`
- `ai-workflow-hub/tests/test_security_preflight_p1.py`

Those files are not part of commit `6b4a3aa` and were not included in this
parent pin decision.
