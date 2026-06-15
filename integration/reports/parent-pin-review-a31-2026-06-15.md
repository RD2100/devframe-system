# Parent Pin Review A31

Date: 2026-06-15
Reviewer: parent devframe-system coordinator
Scope: parent gitlink and lock update

## Verdict

Status: `A31_OPENCODE_REAL_ZOTERO_METADATA_ONLY_PILOT_PIN_REVIEW_PASS`

Parent pin is accepted for the `dev-frame-opencode` real Zotero metadata-only
pilot code baseline:

`b086ca283fb71b16833acc3461e42a3e2e727456`

This is an `accepted_with_limitations` metadata-export-file milestone. It is
not final acceptance and does not authorize PDF, attachment, full-text,
Obsidian, RAG, WriteLab, browser/CDP, MiniApp, cloud, or Zotero app/API access.

## Pin Set After A31

- `agent-acceptance`:
  `75f8eb329778d4a8cffb28f6ba79b137038d4fed`
- `dev-frame-opencode`:
  `b086ca283fb71b16833acc3461e42a3e2e727456`
- `devframe-control-plane`:
  `79399541b8426cff0f362b665bad09e3c23e974b`
- `test-frame`:
  `c3353fb34900aa24f56df5b9c9230f3249d6c01a`

## Files Updated

- `BASELINE_LOCK.json`
- `integration/lock/submodules.lock.yml`
- `integration/reports/README.md`
- `integration/PROJECT_COMPLETENESS_PLAN.md`
- `integration/reports/opencode-real-zotero-metadata-only-pilot-return-review-2026-06-15.md`
- `integration/reports/parent-pin-review-a31-2026-06-15.md`
- parent gitlink for `dev-frame-opencode`

## Parent-Side Checks Run

- `git -C dev-frame-opencode rev-parse HEAD`
  returned
  `b086ca283fb71b16833acc3461e42a3e2e727456`.
- `git -C dev-frame-opencode cat-file -t b086ca283fb71b16833acc3461e42a3e2e727456`
  returned `commit`.
- `git ls-tree HEAD dev-frame-opencode` before this pin showed parent tree
  still at `f5a62aec49ea68e92531e3bc17c982ddb7fd8c55`.
- `git submodule status -- dev-frame-opencode` showed current submodule HEAD
  at `+b086ca283fb71b16833acc3461e42a3e2e727456`.
- `Get-FileHash -Algorithm SHA256` for the three evidence ZIPs matched the
  module return:
  - `7D8780219800C25E7C618196CD1B9DACA1C1267596E5BCFCA78589B5EB5AFF3F`
  - `632CC5CEC80D1A5116315F7764D995C91D329456BBC3E17B300D29EB29BE25FF`
  - `66540F9DF8DBDFE8DC5C410E444592944F18649003C9193C7A6CE99AEC4C60D7`

## Boundary

This pin records a real user-provided Zotero metadata export file run only.

It does not authorize or execute Zotero app/API/library/storage access,
Obsidian, RAG, WriteLab, MiniApp, browser/CDP, cloud, PDF, attachment,
full-text, or private paper runtime.

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

Those files are not part of the `b086ca2` milestone evidence and were not
included in this parent pin decision.
