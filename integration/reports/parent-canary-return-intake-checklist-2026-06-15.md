# devframe-system Parent Canary Return Intake Checklist

Date: 2026-06-15
Scope: parent intake checklist for canary returns
Runtime: not executed by parent
Verdict: `INTAKE_READY_WAITING_FOR_RETURNS`

## 1. Required Return Artifacts

Each returning submodule report must include:

- module name;
- branch;
- base commit observed by the submodule;
- final commit if changed;
- dirty state after task completion;
- exact tests or probes run;
- generated artifact paths;
- changed files;
- Reviewer Index;
- known gaps;
- explicit statement that no forbidden runtime was executed.

## 2. Required Evidence Boundaries

The parent must reject a return if it claims any of the following without a
fresh RuntimeAuthorization and human gate:

- real Zotero, Obsidian, RAG, WriteLab, paper full text, MiniApp, browser/CDP,
  cloud, Android, or private user data execution;
- final production readiness;
- final governance acceptance;
- parent pin readiness from dispatch success alone;
- test pass as final acceptance;
- ZIP validity as final acceptance;
- dry-run as live execution.

## 3. `agent-acceptance` Return Checks

Expected TaskSpec:
`integration/task-specs/TS-AGENT-ACCEPTANCE-PARENT-CANARY-GATE-A1.md`

Required checks:

- The report must state whether selected parent canaries fail closed through
  the production validator path.
- If a new SD-11 or equivalent gate is added, it must be scoped to parent
  canary overclaim wrappers or clearly prove it does not misclassify normal
  pass reports.
- The report must list which `NEG-PARENT-*` cases are covered.
- The report must include at least one regression check that would have caught
  the original observed gap where parent canaries were incorrectly accepted.
- Any `PASS` result must mean the validator rejected invalid evidence as
  expected, not that the synthetic canary itself is acceptable evidence.

Acceptable return statuses:

- `PARENT_CANARY_GATE_PASS`
- `PARENT_CANARY_GATE_GAP_FIXED`
- `BLOCKED`

## 4. `test-frame` Return Checks

Expected TaskSpec:
`integration/task-specs/TS-TEST-FRAME-PARENT-CANARY-REPORT-A1.md`

Required checks:

- The report must cover `NEG-PARENT-002-dry-run-live-e2e-pass`.
- The report must cover `NEG-PARENT-013-missing-env-reported-pass`.
- The report must prove dry-run or synthetic execution cannot be promoted to
  live E2E pass.
- The report must prove missing environment or missing authorization cannot be
  reported as pass.
- If local fixture copies are used, the report must list their source parent
  paths or include a consistency check.
- Any readiness or bundle work from the module-local loop must not be mixed
  with the parent canary return as evidence for final readiness.

Acceptable return statuses:

- `PARENT_CANARY_REPORT_PASS`
- `PARENT_CANARY_REPORT_GAP_FIXED`
- `BLOCKED`

## 5. Parent Verification After Return

After both returns arrive, the parent should:

1. Read each ExecutionReport and Reviewer Index.
2. Confirm changed files stay inside the child TaskSpec scope.
3. Confirm tests are local/offline only.
4. Confirm no forbidden runtime was executed.
5. Update `integration/reports/pin-readiness-matrix-v1-2026-06-15.md`.
6. Update `integration/PROJECT_COMPLETENESS_PLAN.md`.
7. Decide whether a pin proposal is eligible.

## 6. No-Go Conditions

Stop and mark `BLOCKED` if:

- either submodule returns without Reviewer Index;
- either submodule reports `pass` while preserving an invalid canary as pass;
- either submodule ran forbidden runtime;
- base mismatch changes the interpretation of the returned evidence;
- the return requires cross-module schema changes not represented in parent
  contracts;
- the return asks for real runtime or private data access.
