# S15 Execution Boundary Lock Table

Date: 2026-06-16
Parent repo: `D:\devframe-system`
Status: `BOUNDARY_KERNEL_DRAFT_LOCKED_FOR_PARENT_USE`

## Purpose

This report defines the parent execution boundary for S15. It is intentionally
stricter than a runtime roadmap. It says what the parent may classify, what it
may only read, what remains design-only, and what cannot run without a later
human RuntimeAuthorization.

## Boundary Classes

| Class | Name | Parent action allowed | Runtime allowed |
|---|---|---|---|
| A | Strict non-execution layer | classify only | no |
| B | Design-only layer | document and review contracts | no |
| C | Read-only evidence layer | read, hash, parse, compare | no new runtime |
| D | Human-only authority | request or record decision | only after explicit authorization |

## Locked Resource Table

| Resource or action | S15 state | Parent may do | Parent must not do |
|---|---|---|---|
| Submodule parent pin | `PARENT_ACTION_ONLY` | review evidence and update parent pin when accepted | let child self-pin or treat drift as accepted |
| Evidence ZIP | `READ_ONLY_EVIDENCE` | hash, list entries, compare manifests | execute contained scripts or promote ZIP pass to final verdict |
| EvidenceManifest | `READ_ONLY_EVIDENCE` | parse and check provenance | treat as autonomous approval |
| ExecutionReport | `READ_ONLY_EVIDENCE` | compare claimed results to artifacts | convert pass to final acceptance |
| ReviewVerdict | `REVIEW_INPUT_ONLY` | record independent reviewer result | bypass final governance rules |
| FinalVerdict | `NOT_AVAILABLE` | record blocker and prerequisites | issue automatically from child/test/ZIP success |
| `dev-frame-opencode` runtime | `CANDIDATE_ONLY` | consume parent-pinned minimized evidence | run new runtime from parent boundary task |
| `test-frame` runtime | `CANDIDATE_ONLY` | consume parent-pinned synthetic/offline evidence | run live external verification |
| `devframe-control-plane` dispatch | `FROZEN_BOUNDARY_PENDING_DEEP_AUDIT` | inspect interface evidence | activate dispatch/state machine |
| `agent-acceptance` rule center | `GOVERNANCE_RULE_INPUT` | consume rule-center evidence | let it execute external runtime |
| Zotero Web API | `HUMAN_REQUIRED_BY_TRACK` | record previously authorized metadata-only reports | open new reads without fresh authorization |
| Zotero app/local database | `HUMAN_REQUIRED` | document plan | read app storage/database |
| PDF, attachments, full text | `HUMAN_REQUIRED` | document plan | read/process content |
| Notes/private paper text | `HUMAN_REQUIRED` | document plan | persist or inspect content |
| Obsidian vault | `HUMAN_REQUIRED` | document plan | read vault |
| RAG/vector store | `HUMAN_REQUIRED` | document plan | build/query live index |
| WriteLab live runtime | `HUMAN_REQUIRED` | document plan or prior boundary evidence | call live service |
| Browser/CDP/cloud/MiniApp | `HUMAN_REQUIRED` | document plan | run live automation |
| GitLab CI/CD pipeline | `DESIGN_ONLY` | write design or policy draft | enable runner/pipeline |
| Canary repo/rollback drill | `DESIGN_ONLY` | write drill design | execute drill |

## Parent-local Verification Allowed

The following are not considered runtime execution under this boundary:

- `git status`, `git log`, `git diff --check`, `git submodule status`;
- file hash calculation;
- JSON/YAML syntax parsing;
- markdown existence and link checks;
- read-only report comparison.

These commands may validate boundary documents and evidence metadata. They do
not authorize external resources or final acceptance.

## Hard Stop Rule

If a proposed next step requires external runtime, live resource access, final
verdict issuance, control-plane dispatch, CI/CD execution, or canary execution,
the S15 state is `HUMAN_REQUIRED` or `NO_GO` until a later scoped authorization
changes that specific action.
