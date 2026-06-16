# Runtime vs Contract Separation - S15

Date: 2026-06-16
Parent repo: `D:\devframe-system`
Status: `CONTRACT_BOUNDARY_DEFINED`

## Purpose

This contract prevents implementation artifacts from being mistaken for runtime
authorization or final governance acceptance.

## Separation Model

| Layer | May produce | Must not produce |
|---|---|---|
| Contract schema | allowed shape, required fields, closed properties | runtime success |
| RuntimeAuthorization request | requested scope and constraints | authorization decision |
| Human RuntimeAuthorization decision | explicit bounded permission | final result or broader permission |
| Runtime/executor | ExecutionReport and artifacts | independent review or final verdict |
| EvidenceManifest | provenance and hashes | approval |
| Test-frame | verification evidence | production readiness |
| Opencode adapter | candidate report/evidence | parent acceptance |
| Agent-acceptance | governance rule evidence | live runtime proof |
| Parent superproject | intake, pin, lock, boundary status | child runtime execution in S15 |
| Final governance layer | final verdict after all gates | automatic promotion from lower layers |

## Required Contract Flags

Any parent-level evidence consumption report should preserve these distinctions:

- `candidate_evidence_only = true` when applicable;
- `final_acceptance_claimed = false`;
- `live_ready_claimed = false`;
- `production_ready = false`;
- `runtime_authorization_required = true` for any live resource expansion;
- `raw_sensitive_fields_absent = true` for minimized evidence;
- resource booleans must be explicit for PDF, notes, attachments, full text,
  Obsidian, RAG, WriteLab, browser/CDP, cloud, and MiniApp.

## Boundary Rule

Contract validity is necessary but not sufficient for runtime execution.

Runtime execution requires:

1. an explicit scoped RuntimeAuthorization decision;
2. a TestRunSpec or equivalent bounded run description;
3. evidence storage and minimization rules;
4. a parent review path;
5. a final state that does not exceed the authorized resource class.

## Anti-overclaim Rule

Any report that states or implies these claims from child evidence alone must be
rejected by parent review:

- final governance acceptance;
- production-ready;
- live-ready;
- paper-quality accepted;
- full-system verified;
- PDF/full-text/notes/attachments ready from metadata-only evidence;
- WriteLab/Obsidian/RAG/browser/cloud/MiniApp ready from dry-run evidence.

## S15 Scope

S15 may improve documentation, contracts, and parent boundary reports.

S15 must not implement or activate:

- CI/CD runtime enforcement;
- ZIP runtime processor;
- control-plane dispatch runtime;
- canary repo execution;
- rollback drill execution;
- new live resource pilots.
