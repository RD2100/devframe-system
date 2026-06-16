# Source-Level Safety Review: Runtime Pilots

Date: 2026-06-16

Status: PASSED_WITH_LOW_RISK_FOLLOWUPS

Scope reviewed:
- `D:\devframe-system\dev-frame-opencode\ai-workflow-hub\src\ai_workflow_hub\context_layer\adapters\obsidian_note_adapter.py`
- `D:\devframe-system\dev-frame-opencode\ai-workflow-hub\src\ai_workflow_hub\context_layer\adapters\rag_single_note_retrieval_pilot.py`
- `D:\devframe-system\dev-frame-opencode\ai-workflow-hub\src\ai_workflow_hub\cli.py`
- Relevant tests:
  - `D:\devframe-system\dev-frame-opencode\ai-workflow-hub\tests\test_obsidian_note_adapter.py`
  - `D:\devframe-system\dev-frame-opencode\ai-workflow-hub\tests\test_paper_rag_single_note_retrieval_pilot.py`

Verdict:
- No P0/P1 source-level safety blocker found for the current scoped runtime pilots.
- The reviewed paths preserve the intended boundary: one allowlisted Obsidian Markdown note, local deterministic RAG manifest only, minimized evidence, no whole-vault scan, no external RAG, no embeddings API, no vector DB, no browser/CDP/cloud, no WriteLab call in the RAG slice.
- This review does not grant final governance acceptance, paper-quality acceptance, production readiness, broad live readiness, whole-vault readiness, or general RAG readiness.

Key source checks:
- Obsidian pilot resolves the candidate and allowlist paths before comparison:
  - `obsidian_note_adapter.py:188`
  - `obsidian_note_adapter.py:189`
- Obsidian pilot checks vault containment before reading:
  - `obsidian_note_adapter.py:191`
- Obsidian pilot reads only the explicit candidate file after allowlist and suffix checks:
  - `obsidian_note_adapter.py:229`
- Obsidian report records raw-note/path persistence as false and stores only fingerprints/counts:
  - `obsidian_note_adapter.py:291`
  - `obsidian_note_adapter.py:302`
- RAG pilot resolves candidate and allowlist paths before comparison:
  - `rag_single_note_retrieval_pilot.py:179`
  - `rag_single_note_retrieval_pilot.py:180`
- RAG pilot reads only the explicit allowlisted Markdown note and builds deterministic local chunk fingerprints:
  - `rag_single_note_retrieval_pilot.py:223`
  - `rag_single_note_retrieval_pilot.py:248`
- RAG pilot explicitly reports no whole-vault scan, no raw chunk persistence, and no RAG readiness claim:
  - `rag_single_note_retrieval_pilot.py:322`
  - `rag_single_note_retrieval_pilot.py:334`
  - `rag_single_note_retrieval_pilot.py:344`
- CLI entry points are scoped commands rather than implicit background runtime:
  - `cli.py:4315`
  - `cli.py:4367`
  - `cli.py:4456`

Threat review summary:
- Path traversal: controlled by resolved allowlist matching plus vault containment checks.
- Command injection: no shell execution was found in the reviewed adapter paths.
- Secret leakage: reports persist fingerprints, booleans, and counts; raw note body, chunks, query, and note path are not intended to be persisted.
- Runtime expansion: no reviewed RAG path calls an embedding API, vector database, browser/CDP, cloud runtime, or external/private RAG service.
- Fake green risk: blocked paths return blocked status rather than pass status.

Low-risk followups:
1. Add an explicit maximum note byte size before reading/chunking allowlisted Markdown notes.
   - Current scope is user-authorized local single-note pilots. The observed live note was small, but a future oversized allowlisted note could cause avoidable memory/latency cost.
   - Suggested severity: P3 / operational hardening.
2. Document that `note_path_fingerprint` is a hash of the resolved local path string, not raw path persistence.
   - This is currently acceptable for minimized local evidence, but the privacy model should keep treating path fingerprints as derived metadata.
   - Suggested severity: P3 / evidence hygiene.

Residual gaps:
- This review did not inspect every historical paper adapter, only the current Obsidian/RAG runtime pilot boundary.
- This review did not execute live resource calls.
- This review did not validate paper quality.
- This review does not replace agent-acceptance governance review.

Decision:
- Safe to proceed to post-runtime governance review and parent-level non-final milestone closeout, assuming agent-acceptance returns no P0/P1 blocker.
