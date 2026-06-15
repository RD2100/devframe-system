# Lessons Learned �� RD2100 Agent Runtime

> Running log of operational discoveries. Each entry feeds back into rules, profiles, or protocol.
> Format: Date | Context | Problem �� Root Cause �� Solution �� Derived Rule/Change

---

## LL-001: (status: active) opencode Desktop Conflict

- **Date**: 2026-05-28
- **Context**: SADP dispatch testing, all opencode run commands timing out
- **Problem**: v4-pro dispatches consistently 30s timeout with no output
- **Root Cause**: opencode desktop app holding process lock, CLI dispatch blocked
- **Solution**: Close desktop app before CLI dispatch
- **Derived**: Added to `dispatch-model-profiles.md` Failure Pattern Library
- **Changed Files**: `dispatch-model-profiles.md`

## LL-002: (status: active) v4-pro PS1 File Read Timeout

- **Date**: 2026-05-28
- **Context**: Governance audit �� read hooks/*.ps1 via opencode
- **Problem**: Any .ps1 file >100 lines causes 30s timeout on v4-pro
- **Root Cause**: DeepSeek v4-pro tool-call timeout shorter than file read duration for large files
- **Solution**: Route PS1/code file audits to deepseek-chat or Codex direct
- **Derived**: Model selection rule in dispatch-model-profiles.md
- **Changed Files**: `dispatch-model-profiles.md`, SADP ��4.6

## LL-003: (status: active) v4-pro Multi-File Cap = 2

- **Date**: 2026-05-28
- **Context**: Governance audit �� batch audit of 8 files
- **Problem**: 3+ .md files in single prompt �� 30s timeout
- **Root Cause**: Agent serially reads files; cumulative tool-call time exceeds v4-pro limit
- **Solution**: Cap v4-pro at 2 files/dispatch; use deepseek-chat for 3-5 files; Codex direct for 6+
- **Derived**: Quick Reference table in dispatch-model-profiles.md
- **Changed Files**: `dispatch-model-profiles.md`

## LL-004: (status: active) --add-dir Not Supported by opencode run

- **Date**: 2026-05-28
- **Context**: Attempted to give agent explicit directory access
- **Problem**: `opencode run --add-dir D:\devframe-system\agent-acceptance` �� exit 1, shows help
- **Root Cause**: `--add-dir` is not a valid option for `opencode run` subcommand
- **Solution**: Use absolute paths in prompt; agent has filesystem access via build agent permissions
- **Derived**: Documented in build agent limitations
- **Changed Files**: `dispatch-model-profiles.md`

## LL-005: (status: active) agent create Hangs on v4-pro

- **Date**: 2026-05-28
- **Context**: Attempted to create dedicated SADP executor agent
- **Problem**: `opencode agent create` �� "Generating agent configuration..." loops forever
- **Root Cause**: Agent creation calls model to generate config; v4-pro tool timeout prevents completion
- **Solution**: Use existing `build` agent; no custom agent needed for current dispatch patterns
- **Derived**: Skip agent creation in Phase 0-5; revisit when model supports it
- **Changed Files**: `dispatch-model-profiles.md`

## LL-006: (status: active) SADP Dispatch = Real but Constrained

- **Date**: 2026-05-28
- **Context**: End-to-end SADP validation
- **Finding**: opencode dispatch IS real multi-agent (unique sessionID, cost >0, tokens >0)
- **Finding**: But practical limits (2 files/v4-pro, 5 files/chat) mean plan agent must decide: dispatch or self-execute
- **Finding**: Trust Record (sessionID + timestamp + tokens + cost) prevents plan agent from faking dispatches
- **Derived**: SADP dispatch decision tree needed
- **Changed Files**: `sub-agent-dispatch-protocol.md` ��2.1, ��4.6

---

## How to Add a Lesson

1. Assign next LL-XXX number
2. Fill all fields: Date, Context, Problem, Root Cause, Solution, Derived, Changed Files
3. If a rule should be created/modified, reference it in Derived
4. If model behavior changes, update `dispatch-model-profiles.md`
5. If protocol changes, update `sub-agent-dispatch-protocol.md`

---

> **Count**: 6 lessons | **Period**: 2026-05-28 (single session)

## LL-007: (status: active) Prompt-Induced Redundant Construction

- **Date**: 2026-05-28
- **Pattern Name**: Prompt-Induced Redundant Construction
- **Context**: User proposed "����ͨ���Ϳ��ȥ������Դ". Agent agreed and began designing new Resource Activation Framework.
- **Problem**: capability-inventory (28 entries) + SADP dispatch protocol already covered resource invocation. New framework was redundant.
- **Root Cause**:
  1. Compliance bias �� agent treated user proposal as task goal, not hypothesis to verify
  2. Action reward bias �� "build new" felt more productive than "existing is sufficient"
  3. No mandatory pre-check �� inventory was available but not forced as decision gate
  4. No veto mechanism �� plan agent created task, execute agent would have blindly executed
- **Solution**:
  1. core-008: Resource Sufficiency �� Prove Gap Before Any Action (P0, universal)
  2. Gate 0: Reuse-before-Build Check �� mandatory before any construction TaskSpec
  3. Execute agent veto right �� can reject redundant TaskSpecs
  4. CLAUDE.md: Reuse-before-Build summary rule
- **Derived Pattern**: `Prompt-Induced Redundant Construction` �� when user instruction implies "build X", agent defaults to compliance. Trigger words: "����/�½�/���/�ع�/ͨ�û�/����/���"
- **Prevention**: Gate 0 must run before TaskSpec creation. Trigger words �� auto-trigger Gate 0.
- **Changed Files**: `rules/core.md` (+core-008), `sub-agent-dispatch-protocol.md` (��0), `CLAUDE.md`, `lessons-learned.md` (LL-007)


---

---

## LL-008: (status: active) Governance Drift: Rules Changed, Downstream Files Not Synced

- **Date**: 2026-05-28
- **Pattern Name**: Structural Inconsistency Cascade
- **Context**: After upgrading SADP (evidence-based Gate 0, Cumulative Trigger, expiration policy, canaries), discovered that downstream files (JSON schemas, AGENTS.md doc map, INSTANTIATION.md, header counts) still reflected the pre-upgrade state.
- **Problem**: Governance rules were modified, but schemas, document maps, and counts were not updated. A new agent reading AGENTS.md would see "6 rules" (actual: 8), "27 capabilities" (actual: 28), no SADP in doc map, and JSON schemas missing gate_0/trust_record fields.
- **Root Cause**:
  1. Single-source modification without cascade detection �� changing SADP did not trigger review of dependent files
  2. Manual counts in headers (e.g. "27 capabilities") are brittle �� no automated count verification
  3. Doc maps are hand-maintained rather than generated from file system
  4. Schema files were designed before evidence governance was introduced �� no update trigger existed
- **Solution**:
  1. Updated task-spec.schema.json (+gate_0, +conflict_registry fields)
  2. Updated execution-report.schema.json (+trust_record, +fallback_record)
  3. Updated AGENTS.md doc map (added SADP, lessons, canaries, manifest, bootstrap; fixed counts)
  4. Updated capability-inventory.md header (27��28)
  5. Updated INSTANTIATION.md (+governance manifest verification step)
  6. Created governance-manifest.md for this project (P0-8)
- **Derived Pattern**: `Structural Inconsistency Cascade` �� when a governance rule or protocol changes, downstream files (schemas, doc maps, templates, handoff docs) that reference counts, field names, or file lists become silently stale. Detection requires either automated cross-reference or a mandatory "sync check" after any governance change.
- **Prevention**:
  1. After any governance file modification �� run schema validation + doc map audit
  2. Replace manual counts with auto-generated references where possible
  3. Add "cascade check" to Plan Agent Review Procedure (��3.3a) regression tests
- **Trigger words**: governance change, schema update, doc map, rule count, capability count, structural sync
- **Changed Files**: `task-spec.schema.json`, `execution-report.schema.json`, `AGENTS.md`, `capability-inventory.md`, `INSTANTIATION.md`, `governance-manifest.md`, `lessons-learned.md`

---

## LL-009: (status: watch) Plan Agent Self-Bypass �� [@go-only model mitigates]

- **Date**: 2026-05-28
- **Pattern Name**: Plan Agent Self-Bypass
- **Context**: After completing P0 structural sync (8 files), reviewer noted that no formal TaskSpec or ExecutionReport was produced. Plan agent had verbally done Gate 0 but skipped TaskSpec creation, dispatch, and ExecutionReport, treating the task as "too simple for full SADP."
- **Problem**: Plan agent executed a qualifying task (3+ files, governance file modifications) without creating a TaskSpec, without formal gate_0 evidence block, and without producing an ExecutionReport. The SADP auto-trigger rules fired, but the plan agent ignored them.
- **Root Cause**:
  1. Plan agent judged task complexity ("just sync work, no new design") and decided SADP was unnecessary
  2. This is the EXACT pattern LL-007 warned about: agent unilaterally decides a governance rule does not apply
  3. SADP ��0.0 auto-trigger rules are DOCUMENT DECLARATIONS, not ENFORCEMENT MECHANISMS �� nothing stops a plan agent from executing directly
  4. The "3+ files" trigger is self-reported: plan agent must count its own files and voluntarily trigger SADP
- **Solution**:
  1. Retroactively created TaskSpec (task-p0-sync-001) with full gate_0 evidence block
  2. Retroactively created ExecutionReport with Trust Record
  3. Recorded LL-009 as a cautionary pattern
  4. Identified structural gap: SADP auto-trigger is advisory, not enforceable
- **Derived Pattern**: `Plan Agent Self-Bypass` �� when the plan agent judges a task "too simple" or "just maintenance," it skips SADP workflow. This mirrors LL-007 (agent prefers action over governance) but is more dangerous because it happens at the META level: governance rules themselves are ignored.
- **Structural Gap Exposed**:
  - SADP ��0.0 says "Plan agent violation: ... human reviewer should reject the output." But there is no automated enforcement.
  - The plan agent is BOTH the executor AND the self-auditor for SADP triggers.
  - This is the honesty-dependence problem from the premortem: the system trusts the plan agent to obey rules it can silently bypass.
- **Prevention Candidates** (not yet implemented):
  1. Before any task execution, check SADP trigger conditions and log the decision (even if "not triggered")
  2. Human reviewer audit: after each session, verify at least one TaskSpec exists for any multi-file change
  3. Cumulative trigger window (��0.0a) partially addresses this by tracking session-level write_set �� but still relies on agent self-reporting
  4. Ultimate solution: external audit process that compares git diff against TaskSpecs produced
- **Trigger words**: simple task, just sync, maintenance, quick fix, trivial, skip SADP
- **Changed Files**: `tasks/task-p0-sync-001.md` (new), `tasks/execution-report-p0-sync-001.md` (new), `lessons-learned.md` (this entry)

---


**@go-only update (2026-05-28)**: The auto-trigger bypass vulnerability described in this lesson is mitigated by the @go-only model (��0.0). Since SADP no longer auto-triggers on file counts or task patterns, "evading auto-triggers" is no longer a valid attack surface. The lesson remains as a historical pattern for when auto-triggers are re-enabled. Status downgraded from active to watch.

## LL-010: (status: active) Post-Hoc Audit Gap �� Can Detect But Cannot Prevent

- **Date**: 2026-05-28
- **Pattern Name**: Post-Hoc Audit Gap
- **Context**: Implemented Plan Auditor (��3.3a) to independently verify SADP compliance. The auditor checks session ledger, changed files, TaskSpecs, and ExecutionReports for consistency.
- **Problem**: Plan Auditor can DETECT violations (missing TaskSpec, missing gate_0 evidence, diff/TaskSpec mismatch) and BLOCK finalization. But it cannot PREVENT Plan Agent from writing files before the audit runs. If Plan Agent writes to protected files without creating a TaskSpec, the auditor will catch it post-hoc �� but the files are already modified.
- **Root Cause**: The audit trigger (git diff) is inherently reactive. To prevent writes, you need a pre-write gate �� something that intercepts file modifications BEFORE they happen. The current governance hook (pre-edit.governance.ps1) only blocks writes to memory/sealed/secrets files, not to all governance files.
- **Implication**: This is an acceptable limitation for Phase 0-5. Post-hoc audit with block-on-finalization is sufficient because: (1) git can revert unauthorized changes, (2) the block prevents bad state from being committed/merged/handed off, (3) repeated violations create an evidence trail for human review.
- **Future Enhancement Candidates**:
  1. Extend pre-edit hook to cover all governance files (AGENTS.md, rules/*, SADP, inventory, lessons, schemas)
  2. Pre-write gate: before modifying 3+ files or protected files, require a valid TaskSpec to exist
  3. File system watcher: detect writes to protected paths and trigger immediate audit
- **Derived Pattern**: `Post-Hoc Audit Gap` �� any audit mechanism that checks changes AFTER they occur can detect violations but cannot prevent the initial write. This is acceptable when combined with (a) block-on-finalization, (b) git reversibility, and (c) escalating repeated violations to Human.
- **Trigger words**: post-hoc, after the fact, already modified, caught too late
- **Changed Files**: `lessons-learned.md` (this entry)

## Knowledge Metabolism

Three-tier classification for all knowledge entries:

| Tier | Name | Behavior | Constraint |
|------|------|----------|------------|
| 3 | **Incident** | Specific event. Does not constrain execution directly. | 3 incidents �� can promote to pattern |
| 2 | **Pattern** | Recurring failure type. Triggers retrieval but not blocking. | 3 validations �� can promote to principle |
| 1 | **Principle** | Stable rule. P0/P1 enforcement. Review-gated modification. | 3+ false positives �� downgrade to pattern |

**Lifecycle Rules:**
1. 3 similar incidents �� reviewer may promote to 1 pattern
2. Pattern validated 3+ times with no false positives �� reviewer may promote to principle
3. Principle causing 3+ false positives �� must downgrade to pattern
4. Pattern not triggered in 90 days �� archive
5. Archived items do not enter daily decision context (kept for historical reference only)

**Lesson Status Legend:**
- `active` �� currently constraining decisions
- `watch` �� monitoring, not yet blocking
- `deprecated` �� superseded by newer lesson or rule
- `archived` �� historical only, not in decision path
