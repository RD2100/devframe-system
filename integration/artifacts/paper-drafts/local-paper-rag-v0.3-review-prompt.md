# Local Paper RAG v0.3 Review Prompt

## Review Target

Please review the local paper draft artifacts:

- Markdown draft:
  `integration/artifacts/paper-drafts/local-paper-rag-reviewer-draft-v0.3.md`
- DOCX draft:
  `integration/artifacts/paper-drafts/local-paper-rag-reviewer-draft-v0.3.docx`

Current status: non-final reviewer draft. The draft is ready for human/GPT
paper review, but not paper-quality acceptance or final governance acceptance.

## Context

The draft argues for the application value and scene-construction points of
virtual training systems in emergency rescue and military vocational education.
It was produced from a local paper RAG workflow over an authorized local PDF
corpus. The current v0.3 reference section includes six stable source IDs:
`[S1]` through `[S6]`.

The current references have been improved with locally observed journal, year,
issue, page range, DOI, article number, or thesis metadata where available.
They still need final human citation cleanup.

## Review Tasks

1. Decide whether the draft is best positioned as:
   - a short academic paper;
   - a technical note;
   - a literature-review memo;
   - or an internal research brief.

2. Review the argument structure:
   - Is the opening problem clear enough?
   - Do sections 1-5 form a coherent chain?
   - Should section 4, virtual scene construction, become the technical core?
   - Are any claims stronger than the available sources support?

3. Review evidence and citation use:
   - Are `[S1]` through `[S6]` cited in the right places?
   - Are there citation gaps in the introduction, conclusion, or section 4?
   - Are any claims about training-effect improvement unsupported?
   - Which references need formal GB/T 7714 cleanup?

4. Review writing quality:
   - Improve unclear topic sentences.
   - Remove repetition.
   - Tighten cautious language without turning it into overclaiming.
   - Mark any paragraph that should be rewritten rather than lightly edited.

5. Produce a next-action list:
   - P0/P1 blockers before human submission or sharing.
   - P2 improvements for readability and structure.
   - Optional expansion ideas, clearly separated from required fixes.

## Hard Boundaries

Do not infer final acceptance from the current artifacts. The current draft
does not prove:

- paper-quality acceptance;
- final governance acceptance;
- production readiness;
- broad/general RAG readiness;
- whole-vault readiness;
- external/private RAG readiness;
- RuntimeAuthorization.

Do not request or use raw private source text unless separately authorized.
Review the draft as a paper artifact, not as approval to expand runtime scope.

## Preferred Output

Return:

- overall verdict: ready for light revision / needs major revision / blocked;
- top 5 concrete edits;
- citation cleanup findings;
- unsupported or over-strong claims;
- recommended v0.4 outline or patch plan.
