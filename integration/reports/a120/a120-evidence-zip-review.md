# A120 Evidence ZIP Review

Generated: 2026-06-14T16:45:49.625994+00:00
Status: PASS_WITH_BOUNDARY

This report is an independent ZIP evidence review input. It is not a final acceptance verdict.

## Inputs

- ZIP: `D:\dev-frame-opencode\ai-workflow-hub\CDP_EVIDENCE_A120.zip`
- Manifest: `D:\dev-frame-opencode\ai-workflow-hub\COUNTS_MANIFEST_A120.json`
- Verdict: `D:\dev-frame-opencode\ai-workflow-hub\CDP_VERDICT_A120.txt`
- Prefix: `a120-evidence/`

## Summary

- PASS: 18
- WARN: 0
- FAIL: 0

## Checks

- `FILE-ZIP` PASS: zip file exists
- `FILE-MANIFEST` PASS: manifest file exists
- `FILE-VERDICT` PASS: verdict file exists
- `ZIP-STRUCTURE` PASS: ZIP names are unique, relative, and under the expected prefix
- `ZIP-SIZE` PASS: ZIP uncompressed sizes are within configured reviewer limits
- `ZIP-REQUIRED-ENTRIES` PASS: Required A120 entries are present
- `MANIFEST-IDENTITY` PASS: External manifest matches manifest embedded in ZIP
- `MANIFEST-REQUIRED-FIELDS` PASS: Manifest required fields are present
- `MANIFEST-A120-SCHEMA` PASS: Manifest identifies A120 with schema 1.61
- `MANIFEST-ARTIFACT-ORDER` PASS: Evidence bundle artifact order matches A120 contract
- `TRANSCRIPT-HASHES` PASS: Transcript hashes and chain hash match manifest
- `COMMAND-HASHES` PASS: Command echo hashes match manifest
- `BUNDLE-HASH` PASS: Evidence bundle hash recomputes from ordered ZIP artifacts
- `KNOWN-FLAKY` PASS: Known flaky metadata matches deselect command evidence
- `TEST-INVENTORY` PASS: ZIP test inventory count matches manifest
- `VERDICT-CHAIN` PASS: A66-A119 verdict chain exists and contains verdict status tokens
- `SOURCE-CONTRACT-CHECKS` PASS: cli.py contains schema 1.61 and A96-A120 contract markers
- `EXTERNAL-VERDICT-BOUNDARY` PASS: External A120 verdict is readable but is treated as input evidence, not final acceptance
