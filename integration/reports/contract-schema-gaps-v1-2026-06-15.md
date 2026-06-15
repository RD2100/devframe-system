# devframe-system Contract Schema Gaps v1

Date: 2026-06-15
Scope: parent-level contract schema gap analysis
Runtime: not executed
Task: `DFS-CONTRACT-SCHEMA-GAPS-V1`

## 1. Verdict

`DESIGN_READY_SCHEMA_NOT_CREATED`

The parent repo has enough contract alignment to proceed with schema design,
but should not create new canonical JSON schemas in this slice.

Reason:

- schema names and owners are now clear;
- invalid cases are known;
- actual schema creation should be separately reviewed.

## 2. Missing Or Partial Contracts

| Contract | Current status | Owner | Consumers | Next action |
|---|---|---|---|---|
| `RuntimeAuthorization` | missing centralized parent schema | parent + human gate | opencode, test-frame, reviewer, agent-acceptance | create schema after approval |
| `TestRunSpec` | missing centralized parent schema | test-frame + parent | test-frame, parent, reviewer | create schema before positive pilot |
| `TestExecutionReport` | missing centralized parent schema | test-frame | parent, reviewer, agent-acceptance | create schema before positive pilot |
| `FailureRecord` | missing centralized parent schema | any layer reporting blocked/failed | parent ledger, risk register | create lightweight schema |
| `AuditEvent` | missing centralized parent schema | parent/governance/finalizer | audit trail, reviewer | define append-only event fields |
| `FinalVerdict` | partial governance target | agent-acceptance + human/main coordinator | parent, release/pin decision | define mapping, not executor-owned schema |

## 3. Required Field Sets

### RuntimeAuthorization

Required fields:

- `authorization_id`;
- `authorized_by`;
- `authorized_at`;
- `expires_at`;
- `runtime_type`;
- `resource_binding`;
- `data_class`;
- `allowed_commands`;
- `allowed_paths`;
- `redaction_required`;
- `evidence_output_path`;
- `human_gate_reference`;

Invalid cases:

- missing human approver;
- wildcard runtime scope;
- private data with no redaction;
- reused authorization outside runtime/data/time scope;
- live adapter run without authorization id.

### TestRunSpec

Required fields:

- `test_id`;
- `target_module`;
- `test_profile`;
- `runtime_allowed`;
- `fixture_path`;
- `expected_status`;
- `blocked_by_env_policy`;
- `artifact_output_path`.

Invalid cases:

- dry-run profile used for live claim;
- missing expected result;
- real runtime allowed without RuntimeAuthorization;
- no artifact path.

### TestExecutionReport

Required fields:

- `test_id`;
- `run_id`;
- `status`;
- `exit_code`;
- `profile_used`;
- `artifacts`;
- `blocked_reason`;
- `failed_reason`;
- `environment_summary`.

Invalid cases:

- `blocked` or `failed` summarized as pass;
- live pass claimed from dry-run profile;
- missing artifacts;
- final acceptance field included.

### FailureRecord

Required fields:

- `failure_id`;
- `source_contract`;
- `severity`;
- `status`;
- `reason`;
- `owner`;
- `next_action`;
- `evidence_path`.

Invalid cases:

- no owner;
- no evidence path;
- P0 failure downgraded;
- blocked state converted to pass.

### AuditEvent

Required fields:

- `event_id`;
- `timestamp`;
- `actor`;
- `action`;
- `subject_type`;
- `subject_id`;
- `before_state`;
- `after_state`;
- `reason`;

Invalid cases:

- missing actor;
- mutable or overwritten event;
- event claims unverified state transition;
- executor creates final acceptance event.

### FinalVerdict

Required fields:

- `verdict_id`;
- `produced_by`;
- `produced_at`;
- `inputs_reviewed`;
- `gate_summary`;
- `reviewer_summary`;
- `limitations`;
- `final_state`;
- `human_or_governance_reference`;

Invalid cases:

- executor produces final verdict;
- missing reviewer evidence;
- candidate promoted to final ready;
- dry-run promoted to live ready;
- ZIP review treated as final verdict.

## 4. Recommended Schema Order

1. `RuntimeAuthorization`
2. `TestRunSpec`
3. `TestExecutionReport`
4. `FailureRecord`
5. `FinalVerdict` mapping
6. `AuditEvent`

Reason:

- real runtime and positive pilot safety depend first on authorization and test
  contracts;
- failure/final/audit contracts then close fake-green and traceability gaps.

## 5. TaskSpec Suggestion

```text
SUGGESTED_TASK_FOR_DEVFRAME_SYSTEM:
- task_id: DFS-CONTRACT-SCHEMA-CREATION-V1
- goal: create draft JSON schemas for RuntimeAuthorization, TestRunSpec, TestExecutionReport, FailureRecord, AuditEvent, and FinalVerdict mapping.
- allowed files: schemas/agent-runtime/**, integration/contracts/**, integration/reports/**
- expected tests: schema JSON parse; documentation cross-reference; no runtime.
- acceptance criteria: every schema has required fields, invalid examples, producer/consumer mapping, and phase boundary.
- risk: high
```

## 6. Parent Conclusion

The contract schema gap is now explicit.

No real runtime, positive pilot, or final readiness claim should proceed until
RuntimeAuthorization, TestRunSpec, and TestExecutionReport are formalized or
explicitly accepted as temporary contracts by the main coordinator.
