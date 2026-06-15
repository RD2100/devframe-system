# Real Resource Positive Pilot Authorization Checklist

Date: 2026-06-15

## Status

`RUNTIME_AUTHORIZATION_REQUIRED_BEFORE_POSITIVE_PILOT`

This report prepares the next real-resource positive pilot gate. It does not
authorize any runtime and does not claim live readiness.

## Current Safe Baseline

- Parent branch: `codex/rdinit-phase-0-5`
- Latest parent pin review:
  `integration/reports/parent-pin-review-a18-2026-06-15.md`
- Current pinned modules:
  - `agent-acceptance`: `75f8eb329778d4a8cffb28f6ba79b137038d4fed`
  - `dev-frame-opencode`: `8ae6cb77ac977a602dd834efd14405a523c0cb5a`
  - `devframe-control-plane`: `79399541b8426cff0f362b665bad09e3c23e974b`
  - `test-frame`: `c3353fb34900aa24f56df5b9c9230f3249d6c01a`
- Executed external runtime in this preparation step: `false`
- Baseline refresh note: the current pin includes local/offline closed-shape
  schema gates through A18, including the human RuntimeAuthorization decision
  packet boundary and `agent_acceptance_rules` governance-readiness boundary.
  It still does not authorize any real runtime.

## Hard Boundary

Before any real positive pilot, a human/coordinator must provide a fresh,
single-scope `RuntimeAuthorization` that validates against:

- `D:\devframe-system\schemas\agent-runtime\runtime-authorization.schema.json`
- `D:\devframe-system\schemas\agent-runtime\test-run-spec.schema.json`

`RuntimeAuthorization` authorizes a bounded run only. It is not a quality
verdict, not final acceptance, and not permission to reuse the run for a
different runtime, data class, path, or time window.

## Choose Exactly One Pilot Track

### Track A: Time Goal Manager MiniApp Real E2E

Required human choices:

- `runtime_type`: `miniapp_real_e2e`
- target app/repo/path
- exact WeChat DevTools/miniprogram-automator/Jest command allowlist
- machine/environment prerequisite proof
- allowed evidence output path
- explicit stop condition if environment is missing

Must remain false unless separately authorized:

- H5, MeterSphere, cloud device, Android, browser/CDP, ChatGPT, WriteLab,
  Zotero, Obsidian, RAG, PDF, full text.

Expected missing-env behavior:

- missing environment -> `blocked`, not `pass`
- tool exit 0 with blocked semantics -> `blocked`, not `pass`

### Track B: Zotero Metadata-Only Live Resource Pilot

Required human choices:

- `runtime_type`: `zotero_live`
- `resource_binding`: `live_resource`
- `data_class`: normally `redacted` or `public`, never broad private-library
  access by default
- exact export/input path
- exact command allowlist
- allowed metadata fields and forbidden raw fields
- evidence output path

Must remain false unless separately authorized:

- Zotero attachments, PDF, full text, local storage discovery, Obsidian, RAG,
  live WriteLab, browser/CDP, MiniApp, cloud.

Expected failure behavior:

- unsupported file type -> `blocked`, not `pass`
- private/raw fields in report or manifest -> `failed` or `blocked`, not
  `pass`
- empty or unrecognized metadata export -> `blocked`, not `pass`

### Track C: WriteLab Live Boundary Pilot

Required human choices:

- `runtime_type`: `writelab_live`
- exact WriteLab endpoint/action allowed
- whether `paragraph_text` is allowed; default must be `not allowed`
- redaction rules for every output artifact
- evidence output path
- human gate reference for any real text or live service call

Must remain false unless separately authorized:

- raw paragraph storage in state/report/evidence
- bearer token or WriteLab token in stdout/report/evidence
- reuse of synthetic/offline authorization for live calls

Expected failure behavior:

- missing fresh authorization -> `blocked`, not `pass`
- raw `paragraph_text`, `matched_text`, `text_span`, or token leak -> `failed`
- `human_required` promoted to pass -> `failed`

## Required RuntimeAuthorization Fields

The authorization record must include:

- `authorization_id`
- `authorized_by`
- `authorized_at`
- `expires_at`
- `runtime_type`
- `resource_binding`
- `data_class`
- `allowed_commands`
- `allowed_paths`
- `redaction_required`
- `evidence_output_path`
- `human_gate_reference`
- visible `limitations`

## Required TestRunSpec Fields

The paired `TestRunSpec` must include:

- `test_id`
- `target_module`
- `test_profile=real_env_positive_pilot`
- `runtime_allowed=true`
- `runtime_authorization_id`
- `expected_status`
- `blocked_by_env_policy`
- `artifact_output_path`

Dry-run, synthetic offline, and blocked-env probes must not be represented as
real positive pilot evidence.

## Minimal Authorization Packet Template

Use placeholders until a human fills concrete values. This template is not an
authorization by itself.

```json
{
  "runtime_authorization": {
    "authorization_id": "ra-CHOOSE-ONE-PILOT-YYYYMMDD",
    "authorized_by": "HUMAN_REQUIRED",
    "authorized_at": "YYYY-MM-DDTHH:MM:SSZ",
    "expires_at": "YYYY-MM-DDTHH:MM:SSZ",
    "runtime_type": "miniapp_real_e2e | zotero_live | writelab_live",
    "resource_binding": "live_resource",
    "data_class": "redacted | public | private",
    "allowed_commands": ["EXACT_COMMAND_ONLY"],
    "allowed_paths": ["D:\\\\devframe-system\\\\.agent\\\\evidence\\\\..."],
    "redaction_required": true,
    "evidence_output_path": "D:\\\\devframe-system\\\\.agent\\\\evidence\\\\...",
    "human_gate_reference": "HUMAN-GATE-ID",
    "limitations": [
      "single pilot track only",
      "no final acceptance claim",
      "blocked/failed must not be promoted to pass"
    ]
  },
  "test_run_spec": {
    "test_id": "tr-CHOOSE-ONE-PILOT-YYYYMMDD",
    "target_module": "test-frame | dev-frame-opencode",
    "test_profile": "real_env_positive_pilot",
    "runtime_allowed": true,
    "runtime_authorization_id": "ra-CHOOSE-ONE-PILOT-YYYYMMDD",
    "expected_status": "pass | fail | blocked",
    "blocked_by_env_policy": "blocked_not_pass",
    "artifact_output_path": "D:\\\\devframe-system\\\\.agent\\\\evidence\\\\..."
  }
}
```

## Go / No-Go Rules

Go only if all are true:

- exactly one pilot track is selected;
- authorization validates against the parent schema;
- command allowlist is exact, not wildcard;
- evidence path is inside the approved artifact root;
- redaction rules are explicit;
- missing environment maps to `blocked`, not `pass`;
- final acceptance remains false;
- independent reviewer path is identified before execution.

No-go if any are true:

- authorization is stale, broad, wildcarded, or reused from another track;
- command or path is ambiguous;
- real/private data scope is not explicit;
- token, raw text, attachment, PDF, or full-text handling is unclear;
- the intended result requires final acceptance from the executor.

## Reviewer Index

- Changed parent files:
  - This report.
- Critical paths:
  - RuntimeAuthorization schema boundary.
  - TestRunSpec real positive pilot boundary.
  - Single-track runtime selection.
  - Blocked/failed semantics.
- Commands run:
  - `rg` over `integration`, `docs`, and `schemas` for authorization and pilot
    references.
  - `git status --short --branch -uall`.
  - `git submodule status --recursive`.
- Commands not run:
  - no real MiniApp/H5/MeterSphere/cloud/Android/browser/CDP/ChatGPT/WriteLab;
  - no live Zotero/Obsidian/RAG/PDF/private paper;
  - no package install.
- Generated artifacts:
  - This report only.
- Known gaps:
  - A human has not selected the pilot track.
  - No concrete RuntimeAuthorization has been issued.
  - No real positive pilot has run.
- Suggested review focus:
  - Confirm this report is not mistaken for authorization.
  - Confirm the next step asks for one concrete pilot track and a fresh
    RuntimeAuthorization packet.
