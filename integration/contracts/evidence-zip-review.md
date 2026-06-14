# Evidence ZIP Review Contract

Date: 2026-06-15

This contract defines the reviewer-side checks for evidence ZIP files such as
the A120 CDP evidence pack.

## Required Checks

- Input files exist and are readable.
- ZIP entries are unique.
- ZIP entries are relative paths under the expected root prefix.
- No path traversal, absolute path, drive path, or UNC-style path is present.
- Single-entry and total uncompressed sizes stay below configured limits.
- Required entries are present.
- Manifest embedded in the ZIP matches the external manifest.
- Manifest `acceptance` and `schema_version` match the expected acceptance.
- Ordered evidence bundle artifacts match the contract.
- Transcript hashes, command hashes, transcript chain hash, and evidence bundle
  hash recompute from ZIP entry bytes.
- Known flaky metadata matches command deselect evidence.
- Test inventory count matches manifest.
- Verdict chain files exist, are non-empty, and contain verdict status tokens.
- Source contract markers and schema version are present.

## Boundary

The ZIP review report is evidence for a reviewer. It is not final acceptance.
It must not run pack scripts, validation scripts, tests, runtime workflows, or
external services.

## Current Implementation

`scripts/review_a120_evidence_zip.py` implements this contract for A120.
