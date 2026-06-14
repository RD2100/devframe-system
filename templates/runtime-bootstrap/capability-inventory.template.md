# Capability Inventory -- {{PROJECT_NAME}}

> Bootstrap: {{CURRENT_DATE}} | Template v1.0
> 10 universal capabilities pre-registered. Add project-specific (#11+) with Status: proposed.
> All: auto_use_allowed=false, execution_allowed=false, mutation_allowed=false.

## Registration Procedure

1. **Propose**: Add entry with Status: proposed + all required fields
2. **Review**: Submit to human reviewer
3. **Approve**: Reviewer changes Status: proposed -> Status: approved
4. **Enable**: Enable on target platform (codex plugin add / register-hooks.ps1)
5. **Verify**: Confirm via codex plugin list (Codex) or settings.json (Claude)
6. **Report**: Include in batch ExecutionReport

Rule reference: rules/core.md core-007. Status: proposed = NOT usable until approved.

## Platform Key

| Label | Meaning |
|-------|---------|
| Both | Available on Claude Code and Codex |
| Claude | Claude Code only |
| Codex | Codex only |

---

## 1. CodeGraph
- **Platform**: Both
- **Type**: code_intelligence | **Access**: read_only | **Risk**: high
- **Preferred for**: structural code understanding, symbol lookup, caller/callee analysis
- **Forbidden for**: literal string search, current fact without freshness check
- **Fallback**: rg, Read, Grep
- **Human gate**: yes (reindex) | **Must explain if skipped**: yes
- **Evidence**: codegraph_status output, index_freshness

## 2. rg / Grep / Read
- **Platform**: Both
- **Type**: search | **Access**: read_only | **Risk**: low
- **Preferred for**: literal string search, pattern matching, file content reading
- **Forbidden for**: structural code understanding (use CodeGraph first), secret file reading
- **Fallback**: Select-String (PowerShell)
- **Human gate**: no | **Must explain if skipped**: no
- **Evidence**: command output

## 3. Shell (read-only)
- **Platform**: Both
- **Type**: shell | **Access**: read_only | **Risk**: medium
- **Preferred for**: Test-Path, Get-Content, Get-FileHash, Measure-Object, Get-ChildItem
- **Forbidden for**: Set-Content, Remove-Item, Invoke-WebRequest, Start-Process, script execution
- **Fallback**: bash test/ls/wc
- **Human gate**: yes (any write) | **Must explain if skipped**: no
- **Evidence**: command output

## 4. JSON Schema Validation
- **Platform**: Both
- **Type**: validation | **Access**: read_only | **Risk**: low
- **Preferred for**: schema parse audit, JSON structure validation
- **Forbidden for**: schema modification without approval
- **Fallback**: manual review
- **Human gate**: no | **Must explain if skipped**: no
- **Evidence**: ConvertFrom-Json output

## 5. Runtime Docs
- **Platform**: Both
- **Type**: documentation | **Access**: read_only | **Risk**: low
- **Preferred for**: policy lookup, contract reference, gate definition
- **Forbidden for**: current fact without cross-reference
- **Fallback**: direct file read
- **Human gate**: no | **Must explain if skipped**: no
- **Evidence**: doc path + section reference

## 6. Runtime Rules
- **Platform**: Both
- **Type**: rules | **Access**: read_only | **Risk**: low
- **Preferred for**: rule violation check, coding standard, security hard stop
- **Forbidden for**: overriding reviewer decision, auto-approving gates
- **Fallback**: docs search
- **Human gate**: no | **Must explain if skipped**: no
- **Evidence**: rule ID + file reference

## 7. Negative Tests
- **Platform**: Both
- **Type**: testing | **Access**: reference_only | **Risk**: low
- **Preferred for**: validating reviewer checklists, gate enforcement testing
- **Forbidden for**: execution, substituting for actual tests
- **Fallback**: N/A
- **Human gate**: no | **Must explain if skipped**: no
- **Evidence**: test ID + expected_gate_decision

## 8. Reviewer Playbooks
- **Platform**: Both
- **Type**: review | **Access**: reference_only | **Risk**: low
- **Preferred for**: reviewer decision-making, gate evaluation
- **Forbidden for**: auto-approving gates, skipping reviewer
- **Fallback**: verification-gates.md
- **Human gate**: no | **Must explain if skipped**: no
- **Evidence**: playbook reference + decision path

## 9. Governance Hooks (Draft)
- **Platform**: Claude
- **Type**: hook | **Access**: reference_only (audit-only draft) | **Risk**: medium
- **Preferred for**: audit draft reference
- **Forbidden for**: registration without human gate, blocking without reviewer approval
- **Fallback**: N/A
- **Human gate**: yes (registration/activation) | **Must explain if skipped**: no
- **Evidence**: AUDIT-ONLY DRAFT header

## 10. Phase 6 SourceLock / Quarantine
- **Platform**: Both
- **Type**: source_lock | **Access**: reference_only (design only) | **Risk**: critical
- **Preferred for**: external code intake planning
- **Forbidden for**: clone, install, execute, enable MCP without human gate
- **Fallback**: N/A
- **Human gate**: yes (clone, any Phase 6C action) | **Must explain if skipped**: no
- **Evidence**: Phase 6 design docs

---

<!-- Add project-specific capabilities (#11+) below. Set Status: proposed. Reviewer changes to approved. -->

---

## Summary

| # | Capability | Platform | Type | Risk | Status | Phase {{PHASE}} |
|---|-----------|:---:|------|:---:|:---:|:---:|
| 1 | CodeGraph | Both | code_intelligence | high | approved | read-only |
| 2 | rg/Grep/Read | Both | search | low | approved | read-only |
| 3 | Shell | Both | shell | medium | approved | read-only |
| 4 | JSON Validation | Both | validation | low | approved | read-only |
| 5 | Runtime Docs | Both | docs | low | approved | read-only |
| 6 | Runtime Rules | Both | rules | low | approved | read-only |
| 7 | Negative Tests | Both | testing | low | approved | reference |
| 8 | Reviewer Playbooks | Both | review | low | approved | reference |
| 9 | Hooks (Draft) | Claude | hook | medium | approved | audit-only |
| 10 | Phase 6 SourceLock | Both | source_lock | critical | approved | design_only |

### Status Legend

| Status | Meaning |
|--------|---------|
| approved | Reviewer-approved, enabled |
| proposed | Awaiting approval; NOT usable |
| disabled | Previously approved, now off |
| rejected | Proposal rejected; do not use |