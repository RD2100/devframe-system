# Parent pin review: test-frame A55-A56 schema hardening consumption

Decision: ACCEPTED_AND_PARENT_PINNED

Pinned module:
- test-frame: dec26f0656c185d95efcb2a9b29e1dda2de315ed
- Previous parent pin: ebf3fc77536be986c800b3be2abeb2059c9cdadc

Parent files updated:
- D:\devframe-system\BASELINE_LOCK.json
- D:\devframe-system\integration\lock\submodules.lock.yml
- D:\devframe-system\integration\reports\test-frame-opencode-a55-a56-metadata-closeout-readiness-schema-hardening-consumption-return-review-2026-06-16.md
- D:\devframe-system\integration\reports\parent-pin-review-test-frame-opencode-a55-a56-metadata-closeout-readiness-schema-hardening-consumption-2026-06-16.md
- D:\devframe-system\test-frame gitlink

Verification summary:
- test-frame HEAD/worktree check: PASS.
- Evidence ZIP SHA256 check: PASS.
- Fixture JSON parse: PASS.
- Evidence manifest JSON parse: PASS.
- Focused test: 9 passed.
- Metadata consumption/orchestration regression: 116 passed.
- Evidence collector/manifest plus metadata/orchestration regression: 141 passed.
- git diff --check: PASS, CRLF warning only.
- Parent staged diff check before commit: required.

Final lock target:
- agent-acceptance: 6b9a83c1dca0ea650dbc7e97f13977ac02e3e3ee
- dev-frame-opencode: 580f6e9f3ad2ff7c22949d1694990a12b822ce12
- devframe-control-plane: 09167bc656f8625c97bfae5c52dae5a0280b116c
- test-frame: dec26f0656c185d95efcb2a9b29e1dda2de315ed

Boundary:
- This pin records synthetic/offline verification evidence only.
- It does not authorize or execute live Zotero API, key reads, PDF, notes, attachments, full text, paragraph_text, WriteLab, Obsidian, RAG, browser/CDP, cloud, MiniApp, or external runtime.
- It is not final governance acceptance.
