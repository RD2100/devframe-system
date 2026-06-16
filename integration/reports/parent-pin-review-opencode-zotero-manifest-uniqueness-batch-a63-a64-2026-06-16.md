# Parent pin review: opencode A63-A64 Zotero manifest uniqueness

Decision: ACCEPTED_AND_PARENT_PINNED

Pinned module:
- dev-frame-opencode: 3667207d28b51e9aa519126a382c4d9537641a13
- Previous parent pin: b249d2f1f6ac25183a89ac4a17750203a09743ce

Parent files updated:
- D:\devframe-system\BASELINE_LOCK.json
- D:\devframe-system\integration\lock\submodules.lock.yml
- D:\devframe-system\integration\reports\opencode-zotero-manifest-uniqueness-batch-a63-a64-return-review-2026-06-16.md
- D:\devframe-system\integration\reports\parent-pin-review-opencode-zotero-manifest-uniqueness-batch-a63-a64-2026-06-16.md
- D:\devframe-system\dev-frame-opencode gitlink

Verification summary:
- dev-frame-opencode HEAD/worktree check: PASS.
- Evidence ZIP SHA256 check: PASS.
- Real Zotero metadata-only pilot tests: 32 passed.
- Zotero Web metadata pilot tests: 17 passed.
- Expanded metadata/business focused suite: 100 passed.
- real-pilot-authorization-request CLI smoke: PASS, JSON parse PASS.
- report/manifest schema parses: PASS.
- git diff --check base..head: PASS.
- Parent staged diff check before commit: required.

Final lock target:
- agent-acceptance: 6b9a83c1dca0ea650dbc7e97f13977ac02e3e3ee
- dev-frame-opencode: 3667207d28b51e9aa519126a382c4d9537641a13
- devframe-control-plane: 09167bc656f8625c97bfae5c52dae5a0280b116c
- test-frame: 3958459be630bab0ae434a68468a21c2aaf33071

Boundary:
- This pin records local/offline metadata evidence manifest hardening only.
- It does not authorize or execute live Zotero API, key reads, PDF, notes, attachments, full text, paragraph_text, WriteLab, Obsidian, RAG, browser/CDP, cloud, MiniApp, or private runtime.
- It is not a RuntimeAuthorization grant, not live-ready, and not final governance acceptance.
