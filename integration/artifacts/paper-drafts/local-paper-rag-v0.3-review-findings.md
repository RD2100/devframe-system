# Local Paper RAG v0.3 Review Findings

## Overall Verdict

`READY_FOR_TARGETED_V0_4_REVISION`

The v0.3 draft is good enough to become a reviewer-facing paper draft after a
targeted revision. It does not need another tooling pass before revision. The
main need is paper-structure cleanup: clarify the problem, make virtual scene
construction the technical core, and keep claims inside the six-source evidence
boundary.

## Top 5 Concrete Edits

1. Strengthen the introduction so it states the training problem before listing
   technologies: high risk, high cost, low repeatability, and evaluation
   difficulty.
2. Reframe section 4 as the technical core: virtual scene construction should
   explain target-driven modeling, object/space fidelity, interaction design,
   feedback, and runtime constraints.
3. Merge repeated cautious wording. The draft repeatedly says virtual training
   is a supplement rather than a replacement; keep the idea but state it more
   cleanly.
4. Add a short boundary/evaluation section before the conclusion so unsupported
   training-effect claims are visibly excluded.
5. Keep the upgraded references, but mark them as human-review citations rather
   than final GB/T 7714 records.

## Citation Cleanup Findings

- `[S1]` supports earthquake rescue training motivation and page/DOI metadata is
  strong enough for draft citation.
- `[S2]` supports background on foreign military virtual training systems, but
  it should not be used to claim broad superiority.
- `[S3]` and `[S4]` support fire-rescue virtual training discussion.
- `[S5]` is the strongest source for virtual scene construction and should carry
  the technical-core section.
- `[S6]` supports military vocational education application value, but not
  stable skill-transfer claims.

## Unsupported Or Over-Strong Claims To Avoid

- Do not claim training effectiveness has been proven.
- Do not claim virtual training can replace real training.
- Do not claim broad RAG readiness, production readiness, or paper-quality
  acceptance from the current pipeline.
- Do not infer whole-vault Obsidian readiness or external/private RAG readiness.

## Recommended v0.4 Patch Plan

- Rewrite the abstract and opening section for problem clarity.
- Reorder the body around a cleaner argument:
  1. training problem and system positioning;
  2. application scenarios in emergency rescue and vocational education;
  3. foreign military system lessons;
  4. virtual scene construction as technical core;
  5. evaluation boundary and implementation caution.
- Preserve references `[S1]` through `[S6]`.
- Preserve non-final and human-review boundaries.
