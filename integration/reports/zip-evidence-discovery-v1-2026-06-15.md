# devframe-system ZIP Evidence Discovery v1

Date: 2026-06-15
Scope: parent-level ZIP and evidence-pack discovery
Runtime: not executed
Slice: S04

## 1. Purpose

This report records what the parent repo currently knows about ZIP evidence
review coverage.

It does not run the A120 reviewer script and does not validate external ZIP
files. It classifies evidence based on local parent files and reports.

## 2. Known Parent Artifacts

| Artifact | Path | Status | Meaning |
|---|---|---|---|
| A120 markdown review | `integration/reports/a120/a120-evidence-zip-review.md` | `verified` | bounded independent review summary exists |
| A120 JSON review | `integration/reports/a120/a120-evidence-zip-review.json` | `verified` | machine-readable bounded review exists |
| ZIP review contract | `integration/contracts/evidence-zip-review.md` | `verified` | parent contract for reviewer-side checks |
| A120 reviewer script | `scripts/review_a120_evidence_zip.py` | `observed_not_run` | implementation exists but was not executed in this review |

## 3. A120 Review Inputs

The existing A120 review report references external inputs:

| Input | Referenced path | Parent-local status |
|---|---|---|
| ZIP | `D:\dev-frame-opencode\ai-workflow-hub\CDP_EVIDENCE_A120.zip` | `external_to_parent_checkout` |
| Manifest | `D:\dev-frame-opencode\ai-workflow-hub\COUNTS_MANIFEST_A120.json` | `external_to_parent_checkout` |
| Verdict | `D:\dev-frame-opencode\ai-workflow-hub\CDP_VERDICT_A120.txt` | `external_to_parent_checkout` |

Parent conclusion:

- The parent has the review output.
- The parent did not re-open or re-validate the external ZIP in this slice.
- The report remains `PASS_WITH_BOUNDARY`, not final acceptance.

## 4. Coverage Table

| Evidence range | Parent local evidence | Coverage status | Allowed claim |
|---|---|---|---|
| A120 ZIP review | markdown and JSON review reports | `verified_bounded` | A120 review report exists and passed with boundary |
| A120 source input ZIP | referenced by report, not revalidated here | `observed_reference` | input path was recorded by prior report |
| A66-A119 verdict chain | mentioned inside A120 review checks | `indirect_reference` | A120 reviewer checked chain presence in that pack |
| A101-A119 standalone packs | no full parent inventory yet | `unknown` | no global acceptance claim |
| all A101-A120 evidence | no full parent inventory yet | `unknown` | no global acceptance claim |

## 5. Required ZIP Review Checks

The current contract requires checks for:

- readable input files;
- unique ZIP entries;
- relative paths under expected root;
- no traversal, absolute path, drive path, or UNC path;
- size limits;
- required entries;
- embedded manifest matching external manifest;
- acceptance and schema version;
- artifact order;
- transcript, command, chain, and bundle hash recompute;
- flaky metadata consistency;
- test inventory count;
- verdict chain files and status tokens;
- source contract markers;
- external verdict treated as input evidence, not final acceptance.

## 6. Finding Table

| Finding | Status | Risk |
|---|---|---|
| path traversal check exists in A120 reviewer contract | `verified` | low for reviewed A120 pack |
| hash recompute check exists in A120 reviewer contract | `verified` | low for reviewed A120 pack |
| reviewer identity check is not the same as ZIP structure review | `gap` | medium |
| A101-A119 standalone evidence inventory absent | `unknown` | high |
| copy-forward or template `ACCEPTED` risk globally ruled out | `unknown` | high |
| A120 review used as final acceptance | `blocked_by_policy` | high if violated |

## 7. Defects Exist Verdict

```text
defects_exist: UNKNOWN_FOR_GLOBAL_A101_A120
a120_review_defects_found: NO_FROM_EXISTING_REPORT
global_acceptance_ready: NO
```

Reason:

- A120 review report exists and passed with boundary.
- Parent has not inventoried every A101-A120 pack, manifest, reviewer verdict,
  and source artifact.
- Therefore global evidence acceptance is not established.

## 8. Next Parent Work

To advance S04 beyond v1, create a full evidence inventory with:

- evidence id;
- acceptance id;
- pack path;
- manifest path;
- verdict path;
- reviewer report path;
- hash status;
- reviewer independence status;
- final acceptance boundary.

This may require submodule evidence paths or main-coordinator input.

## 9. Parent Conclusion

S04 is complete enough for Master Plan v1 with an explicit limitation:

Only A120 review output is parent-verified. Global A101-A120 evidence acceptance
remains unknown and must not be claimed.
