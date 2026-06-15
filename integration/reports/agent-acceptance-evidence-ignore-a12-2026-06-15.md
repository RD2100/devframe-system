# Agent Acceptance Evidence Ignore A12

Date: 2026-06-15

## Status

`AGENT_ACCEPTANCE_EVIDENCE_IGNORE_PINNED`

This report records a narrow parent follow-up after A11 closeout. The old
`agent-acceptance` local evidence packs were kept on disk and marked ignored in
the submodule so they no longer dirty the parent working tree.

## Scope

In scope:

- `agent-acceptance` generated evidence ignore hygiene.
- Parent gitlink and lock update for `agent-acceptance` only.

Out of scope:

- No real MiniApp, H5, MeterSphere, cloud, Android, browser/CDP, ChatGPT,
  WriteLab, Zotero, Obsidian, PDF, or real paper runtime.
- No `dev-frame-opencode` pin update. A concurrent local submodule advance to
  `3c08f3aaadae8282a5ca6d11676d1826d5895ee5` was observed but not staged or
  recorded in this parent pin.
- No final acceptance claim.

## Evidence

- `D:\devframe-system\agent-acceptance\.gitignore` now ignores:
  - `_evidence/agent-acceptance-cross-module-intake-smoke-a1/`
  - `_evidence/agent-acceptance-minimal-rule-center-a1/`
  - `_evidence/agent-acceptance-paper-real-pilot-rules-a1/`
- `git -C D:\devframe-system\agent-acceptance status --ignored --short`
  showed those old evidence files as ignored (`!!`).
- `git -C D:\devframe-system\agent-acceptance diff --check` exited 0.
- New `agent-acceptance` commit:
  `75f8eb329778d4a8cffb28f6ba79b137038d4fed`
  (`Ignore local agent acceptance evidence packs`).

## Parent Lock Update

- `BASELINE_LOCK.json` updates `agent-acceptance` from
  `b9bb53a72bbd7b4c4e4402aca11b4cc67f9506f5` to
  `75f8eb329778d4a8cffb28f6ba79b137038d4fed`.
- `integration/lock/submodules.lock.yml` mirrors the same update.
- The parent gitlink for `agent-acceptance` points to
  `75f8eb329778d4a8cffb28f6ba79b137038d4fed`.

## Known Gaps

- `dev-frame-opencode` has concurrent local progress at
  `3c08f3aaadae8282a5ca6d11676d1826d5895ee5`; this report does not review or
  pin it.
- Real resource pilot remains `RUNTIME_AUTHORIZATION_REQUIRED`.

## Reviewer Index

- Changed files:
  - `D:\devframe-system\agent-acceptance\.gitignore`
  - `D:\devframe-system\BASELINE_LOCK.json`
  - `D:\devframe-system\integration\lock\submodules.lock.yml`
  - `D:\devframe-system\integration\reports\agent-acceptance-evidence-ignore-a12-2026-06-15.md`
- Critical paths:
  - Generated evidence ignore behavior in `agent-acceptance`.
  - Parent lock parity for the `agent-acceptance` gitlink.
  - Avoiding accidental inclusion of concurrent `dev-frame-opencode` work.
- Tests/checks:
  - `git -C D:\devframe-system\agent-acceptance status --ignored --short`
  - `git -C D:\devframe-system\agent-acceptance diff --check`
  - Parent lock/status checks after staging.
- Generated artifacts:
  - This report only.
- Suggested review focus:
  - Confirm ignore rules are exact task evidence directories, not broad
    `_evidence/` suppression.
  - Confirm parent lock matches the `agent-acceptance` gitlink only.
  - Confirm no external runtime or final acceptance claim is introduced.
