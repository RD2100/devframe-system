# Parent Local Paper RAG Bounded Expanded Outline A1

## Verdict

`BOUNDED_EXPANDED_OUTLINE_READY_FOR_HUMAN_SOURCE_GROUNDING`

This is a non-final paper-planning artifact. It is not a final paper, not
paper-quality acceptance, not final governance acceptance, not production
readiness, not general RAG readiness, and not RuntimeAuthorization.

## Candidate Title

Virtual Training Systems for Emergency Rescue and Military Vocational
Education: A Local RAG-Assisted Draft Outline

## Abstract Skeleton

This draft can introduce virtual training as a practical method for rehearsing
high-risk rescue and military vocational training tasks. The current local RAG
evidence suggests five planning directions: earthquake rescue training
objectives, simulation-supported training characteristics, VR fire-rescue
advantages, virtual-scene construction factors, and vocational education value.
All points below remain draft hypotheses until source-grounded review verifies
the supporting source contexts.

## Evidence Basis

- `preview_status=PASS_LOCAL_RAG_ANSWER_PREVIEW`
- `answer_preview_count=5`
- `document_count=6`
- `chunk_count=47`
- `q4_hybrid_expected_source_matched=true`
- `issue_count=0`
- `warnings_count=0`

## Outline

### 1. Introduction: Why Virtual Training Matters For Rescue Scenarios

Mapped preview:

- `Q1_EARTHQUAKE_RESCUE_PURPOSE`

Draft hypotheses:

- Virtual training can frame rescue training around explicit operational
  objectives.
- Repeated procedure rehearsal may help trainees understand rescue sequences in
  a lower-risk environment.
- Simulated emergency scenes can support training preparation before real-world
  high-risk exposure.

Source fingerprints to ground:

- `sha256:771bd90bae9e97a19ef08a3d50dfecbfa5c2c0c87e963c8abfb97b87d09cc0ae`
- `sha256:22c432f35ccffd6723a28130d22ff317fdab2b3b14854663bfd05dec0623b44b`
- `sha256:8f4146baa4b3d6f1c69ae9c1ca4403ea8f89f2c7c9c0db40eb3986f33894014f`

Reviewer risks:

- Do not turn "lower-risk practice" into proven training effectiveness.
- Confirm the source context specifically supports earthquake rescue framing.

### 2. Background: Simulation-Supported Training Characteristics

Mapped preview:

- `Q2_FOREIGN_MILITARY_CHARACTERISTICS`

Draft hypotheses:

- Simulation-supported training can be discussed as a way to improve readiness
  preparation.
- Repeatable scenario design can make training conditions more controllable.
- Technology-supported training control can help standardize local practice.

Source fingerprints to ground:

- `sha256:8f4146baa4b3d6f1c69ae9c1ca4403ea8f89f2c7c9c0db40eb3986f33894014f`
- `sha256:ef4be5bcc0f3f828c417cdf4c7353b71d2662693eaebb3e74c979af46cf288d3`
- `sha256:22c432f35ccffd6723a28130d22ff317fdab2b3b14854663bfd05dec0623b44b`

Reviewer risks:

- Avoid sweeping claims about all foreign military training systems.
- Confirm each characteristic is present in the source context, not inferred
  from generic wording.

### 3. Application Area: VR Support For Fire-Rescue Training

Mapped preview:

- `Q3_VR_FIRE_RESCUE_ADVANTAGES`

Draft hypotheses:

- VR can provide a safer practice environment for difficult emergency drills.
- Repeatable emergency drills can help trainees revisit key rescue steps.
- Immersive decision rehearsal may be useful where direct real-world practice
  is risky or costly.

Source fingerprints to ground:

- `sha256:f78911a3127834f1a1aa6d7cd1f3f2ba4961c606f00ced9156f77b1d9696e031`
- `sha256:771bd90bae9e97a19ef08a3d50dfecbfa5c2c0c87e963c8abfb97b87d09cc0ae`
- `sha256:22c432f35ccffd6723a28130d22ff317fdab2b3b14854663bfd05dec0623b44b`

Reviewer risks:

- Confirm fire-rescue specificity.
- Avoid implying measured performance improvement unless the source context
  supports it.

### 4. Design Focus: Virtual Scene Construction Factors

Mapped preview:

- `Q4_VIRTUAL_SCENE_CONSTRUCTION_FACTORS`

Draft hypotheses:

- Scene fidelity should be aligned with training objectives rather than pursued
  as visual realism alone.
- Environment modeling and interaction design can be treated as core design
  factors.
- Scenario coverage should map to operational tasks that trainees need to
  practice.

Source fingerprints to ground:

- `sha256:22c432f35ccffd6723a28130d22ff317fdab2b3b14854663bfd05dec0623b44b`
- `sha256:771bd90bae9e97a19ef08a3d50dfecbfa5c2c0c87e963c8abfb97b87d09cc0ae`
- `sha256:8f4146baa4b3d6f1c69ae9c1ca4403ea8f89f2c7c9c0db40eb3986f33894014f`

Reviewer risks:

- Q4 was the earlier retrieval/routing weak spot. Confirm the source match is
  still acceptable before expanding this into paper prose.
- Define "scene fidelity" and "scenario coverage" only after source-grounding.

### 5. Educational Value: Military Vocational Training

Mapped preview:

- `Q5_MILITARY_VOCATIONAL_EDUCATION_VALUE`

Draft hypotheses:

- Virtual training may help connect learning activities to job-oriented skill
  transfer.
- Standardized local practice evidence can help reviewers understand what was
  exercised.
- Repeatable competence-evaluation support is a possible value proposition, but
  it needs source-grounded limits.

Source fingerprints to ground:

- `sha256:ef4be5bcc0f3f828c417cdf4c7353b71d2662693eaebb3e74c979af46cf288d3`
- `sha256:22c432f35ccffd6723a28130d22ff317fdab2b3b14854663bfd05dec0623b44b`
- `sha256:771bd90bae9e97a19ef08a3d50dfecbfa5c2c0c87e963c8abfb97b87d09cc0ae`

Reviewer risks:

- "Skill transfer" and "competence evaluation" should remain hypotheses until
  source-grounded.
- Avoid claims about institutional outcomes or training effectiveness unless
  explicitly supported.

## Suggested Paper Flow

1. Establish virtual training as a response to high-risk rescue training needs.
2. Introduce simulation-supported training characteristics as background.
3. Show fire-rescue VR as an application example.
4. Focus the design discussion on virtual-scene construction factors.
5. Close with vocational education value and limits.

## Source-Grounding Checklist

- [ ] For each section, verify at least one source fingerprint maps to the
      intended section topic.
- [ ] Replace draft hypotheses with source-grounded claims only after review.
- [ ] Mark unsupported hypotheses as removed or needing retrieval refinement.
- [ ] Keep Q4 under special scrutiny because it was the prior weak route.
- [ ] Do not treat minimized fingerprints as quotations.
- [ ] Do not treat this outline as paper-quality acceptance.

## Recommended Next TaskSpec

`PARENT_LOCAL_PAPER_RAG_SOURCE_GROUNDING_REVIEW_A1`

Goal:

- For each section, record whether its source fingerprints are sufficient for
  source-grounded paper drafting.
- If source grounding is insufficient, send only the weak section back to local
  query/rerank refinement.
- Preserve all raw-content boundaries unless a fresh, explicit authorization
  expands the scope.

## Boundary

This outline is derived from minimized evidence only. It does not read or
expose raw PDF text, raw Markdown bodies, raw chunks, raw query text, source
paths, vectors, FAISS binaries, WriteLab payloads/responses, Zotero key/API
material, attachments, notes, full text, `paragraph_text`, browser/CDP/cloud,
MiniApp payloads, or external/private RAG runtime payloads.

It does not claim final governance acceptance, paper-quality acceptance,
production readiness, broad/general RAG readiness, whole-vault readiness,
external/private RAG readiness, cloud readiness, cloud vector DB readiness, or
RuntimeAuthorization.
