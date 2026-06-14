# TS-AGENT-ACCEPTANCE-PATH-GATE0

Date: 2026-06-15
Owner thread: `019ec6c5-0855-7b11-812a-a099010b9b18`
Target path: `D:\devframe-system\agent-acceptance`
Suggested branch: `codex/devframe-system-path-gate0-contract`

## Objective

Converge the `agent-acceptance` path drift and Gate0/HUMAN_REQUIRED boundary
for `devframe-system` integration.

## Scope

- Document standalone path versus superproject submodule path.
- Preserve historical `_archive/**` evidence paths.
- Add or update guidance/fixtures for path drift, expired authorization, and
  HUMAN_REQUIRED preservation.
- Define RuntimeAuthorization fields relevant to active binding validation.

## Forbidden

- Do not run pytest, smoke suite, runtime, or live session refresh.
- Do not rewrite historical archives.
- Do not convert HUMAN_REQUIRED or BLOCKED into success.

## Required Report

Reviewer Index with changed files, critical paths, commands run, verification
verdict, known gaps, and suggested review focus.
