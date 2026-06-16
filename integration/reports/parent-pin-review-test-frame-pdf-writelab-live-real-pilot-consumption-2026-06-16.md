# Parent Pin Review - TESTFRAME PDF WriteLab Live Real Pilot Consumption

Status: `ACCEPTED_AND_PARENT_PIN_PREPARED`

Parent:

- path: `D:\devframe-system`
- branch: `codex/rdinit-phase-0-5`
- parent commit: recorded by the commit that adds this file

Pinned submodule:

- `test-frame = c2e6789b10490e6d9f2cf331742432fa6d4fa25d`
- previous parent pin: `52483575cc94c097f1be57f7ed3d0d7a80940d32`

Evidence recorded:

- `D:\devframe-system\test-frame\reports\evidence-opencode-pdf-writelab-live-real-pilot-consumption-a1.zip`
- SHA256: `8AB7A34514146CEFBD52F63DEAEF660FFA8829F4D9D1980A976817CC655F8B76`

Parent-side verification summary:

- Evidence ZIP hash matched returned value.
- Evidence ZIP listing contained report/command/manifest entries only.
- Manifest JSON and fixture JSON parsed successfully.
- Focused test passed: 7 passed.
- Range diff check passed.
- `test-frame` worktree was clean at intake.

Boundary confirmation:

- No final governance acceptance.
- No paper-quality acceptance.
- No production-ready or broad live-ready claim.
- No raw PDF text, notes, full text, WriteLab payload/response, token, or authorization decision accepted into parent evidence.
- Obsidian and RAG remain deferred and not required for this milestone.

Dirty-state note:

- Existing unrelated parent drift was not staged.
- This pin should stage only:
  - `test-frame` gitlink
  - `BASELINE_LOCK.json`
  - `integration/lock/submodules.lock.yml`
  - this parent pin review
  - the matching return review

Coordination note:

- `dev-frame-opencode` PDF/WriteLab live pilot dependency was parent-pinned first at parent commit `b93099f`.
- This pin records the dependent `test-frame` consumption evidence after the missing evidence package blocker was resolved.
