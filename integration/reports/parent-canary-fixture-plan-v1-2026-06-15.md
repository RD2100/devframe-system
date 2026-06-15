# devframe-system Parent Canary Fixture Plan v1

Date: 2026-06-15
Scope: parent-level synthetic canary fixture plan
Runtime: not executed
Task: `DFS-PARENT-CANARY-FIXTURE-PLAN-V1`

## 1. Verdict

`FIXTURE_PLAN_READY_FIXTURES_NOT_CREATED`

This plan defines synthetic fixture needs for parent negative cases. It does
not create fixture files and does not run tests.

## 2. Fixture Directory Recommendation

Future fixture files should live under one of these paths after coordinator
approval:

```text
docs/agent-runtime/negative-test-fixtures/
integration/fixtures/parent-canary/
```

Preferred path for parent-only canary:

```text
integration/fixtures/parent-canary/
```

Reason:

- avoids mixing parent integration canaries with existing runtime governance
  NEG-001 through NEG-030 fixtures;
- keeps future ownership clear.

## 3. Canary Fixture Matrix

| Parent NEG | Fixture type | Expected result | Future owner | Notes |
|---|---|---|---|---|
| NEG-PARENT-001 | synthetic paper ExecutionReport JSON | `blocked` | agent-acceptance | offline candidate sets `final_ready=true` |
| NEG-PARENT-002 | synthetic TestExecutionReport JSON | `blocked` | test-frame | dry-run profile claims live E2E pass |
| NEG-PARENT-003 | synthetic final verdict shortcut JSON | `failed` | agent-acceptance | test pass used as final acceptance |
| NEG-PARENT-004 | synthetic DispatchAssignment JSON | `blocked` | agent-acceptance/control-plane | dispatch exists with no ExecutionReport |
| NEG-PARENT-005 | synthetic ZIP review markdown | `failed` | agent-acceptance | A120 review claims global A101-A120 acceptance |
| NEG-PARENT-006 | synthetic pin readiness matrix markdown | `failed` | devframe-system | drifted commit marked `PIN_READY` |
| NEG-PARENT-007 | synthetic live adapter report JSON | `blocked` | agent-acceptance/opencode | no RuntimeAuthorization id |
| NEG-PARENT-008 | synthetic redaction failure report | `blocked` | opencode/agent-acceptance | private paper content appears |
| NEG-PARENT-009 | synthetic reviewer pack metadata | `blocked` | agent-acceptance | missing EvidenceManifest |
| NEG-PARENT-010 | synthetic ReviewVerdict JSON | `blocked` | agent-acceptance | reviewer id equals executor id |
| NEG-PARENT-011 | synthetic `.gitmodules` branch decision note | `failed` | devframe-system | advisory branch treated as pin source |
| NEG-PARENT-012 | synthetic RuntimeAuthorization JSON | `blocked` | agent-acceptance | authorization reused outside scope |
| NEG-PARENT-013 | synthetic positive pilot report | `blocked` | test-frame | missing environment but status pass |
| NEG-PARENT-014 | synthetic CI diff | `blocked` | devframe-system | CI adds install/runtime command |
| NEG-PARENT-015 | synthetic roadmap markdown | `failed` | devframe-system | frozen control-plane made MVP blocker |
| NEG-PARENT-016 | synthetic FinalVerdict JSON | `blocked` | agent-acceptance | executor produces final verdict |

## 4. Minimal Fixture Fields

Every future fixture should include:

- `fixture_id`;
- `negative_case_id`;
- `contract_under_test`;
- `input_artifact_type`;
- `expected_result`;
- `expected_reason`;
- `runtime_allowed: false`;
- `owner`;
- `source_report`;

## 5. Automation Strategy

| Check type | Tooling target | Cases |
|---|---|---|
| markdown scan | parent read-only script | NEG-PARENT-005, 006, 011, 014, 015 |
| JSON schema/field check | agent-acceptance or parent script | NEG-PARENT-001, 003, 004, 007, 009, 010, 012, 016 |
| test-frame report check | test-frame | NEG-PARENT-002, 013 |
| redaction scan | opencode or agent-acceptance | NEG-PARENT-008 |

## 6. No-Runtime Rule

All canary fixtures must be synthetic.

Forbidden in canary fixture creation:

- real paper text;
- live Zotero/Obsidian/RAG/WriteLab;
- MiniApp real E2E;
- browser/CDP runtime;
- package install;
- submodule pin update.

## 7. TaskSpec Suggestion

```text
SUGGESTED_TASK_FOR_DEVFRAME_SYSTEM:
- task_id: DFS-PARENT-CANARY-FIXTURES-A1
- goal: create synthetic parent canary fixture files for NEG-PARENT-001 through NEG-PARENT-016.
- allowed files: integration/fixtures/parent-canary/**, integration/reports/**
- expected tests: JSON parse for JSON fixtures; markdown fixture index consistency; no runtime.
- acceptance criteria: every parent NEG has fixture path, expected result, owner, and runtime_allowed=false.
- risk: medium
```

```text
SUGGESTED_TASK_FOR_AGENT_ACCEPTANCE:
- task_id: AA-PARENT-CANARY-GATE-A1
- goal: consume selected parent canary fixtures and reject final-ready/pin-ready/runtime overclaims.
- allowed files: agent-acceptance fixture/test paths only, as approved by main coordinator.
- expected tests: negative gate tests for selected fixtures.
- acceptance criteria: overclaims return blocked/failed exactly as parent matrix specifies.
- risk: high
```

```text
SUGGESTED_TASK_FOR_TEST_FRAME:
- task_id: TF-PARENT-CANARY-REPORT-A1
- goal: consume dry-run/live confusion fixtures and preserve blocked/failed semantics.
- allowed files: test-frame fixture/test paths only, as approved by main coordinator.
- expected tests: negative report validation for NEG-PARENT-002 and NEG-PARENT-013.
- acceptance criteria: dry-run cannot become live pass; missing env cannot become pass.
- risk: high
```

## 8. Parent Conclusion

The canary fixture plan is ready.

Actual fixture creation and submodule consumption should be separate tasks.
Main coordinator should decide whether fixtures stay parent-only or are
delegated into `agent-acceptance` and `test-frame`.
