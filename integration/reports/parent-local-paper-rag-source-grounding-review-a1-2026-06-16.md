# Parent Local Paper RAG Source-Grounding Review A1

## Verdict

`SOURCE_GROUNDING_REVIEW_READY_WITH_5_OF_5_SECTIONS_SUPPORTED_AS_DRAFT`

All five bounded outline sections have enough local source support to proceed
to a cautious section-draft packet. This is not paper-quality acceptance. It is
a source-grounding review that identifies where the current draft claims can be
used, where they must be softened, and where human review remains required.

## Scope

Reviewed authorized local Markdown only:

- Corpus root: `D:\Obsidian\paper-pilot\papers\virtual-training`
- Source count observed: 13 Markdown files plus `conversion-manifest.json`
- Focused grounding files: `01` through `06`

This review did not read Zotero keys, call Zotero APIs, read original PDFs
directly, call WriteLab, call cloud or external RAG, inspect FAISS binaries, or
scan an Obsidian vault outside the authorized folder.

## Evidence Basis

- Bounded outline:
  `integration/reports/parent-local-paper-rag-bounded-expanded-outline-a1-2026-06-16.md`
- Source-grounded draft packet:
  `integration/reports/parent-local-paper-rag-source-grounded-draft-packet-a1-2026-06-16.md`
- Human review packet:
  `integration/reports/parent-local-paper-rag-human-review-packet-a1-2026-06-16.md`
- Answer-preview milestone closeout:
  `integration/reports/parent-current-local-paper-rag-answer-preview-milestone-closeout-2026-06-16.md`

## Corpus Snapshot

Core converted source files reviewed:

- `01-关于利用虚拟现实技术建立“地震救援技术虚拟训练系统”的几点思考_褚鑫杰.md`
- `02-国外军用虚拟训练系统研究.md`
- `03-基于虚拟现实技术的灭火救援训练系统.md`
- `04-三维建模技术在灭火救援作战训练安全中的应用初探_吴东瑾.md`
- `05-虚拟训练系统的虚拟场景研究.md`
- `06-虚拟训练系统在军事职业教育中的应用研究.md`

Line references below are local `rg` observations over the authorized Markdown
files. They are used as reviewer navigation aids, not as final citations.

## Section 1: Earthquake Rescue Training Purpose

Mapped preview:

- `Q1_EARTHQUAKE_RESCUE_PURPOSE`

Support verdict:

- `SUPPORTED_AS_DRAFT_WITH_LIMITS`

Primary source support:

- `01`, lines 27-29: frames the paper around earthquake rescue training and
  VR-based system construction.
- `01`, lines 106-116: describes limitations of current earthquake rescue
  training in field, equipment, consumption, and safety terms.
- `01`, lines 120-158: discusses virtual reproduction of earthquake rescue
  scenes and psychological/environmental context.
- `01`, lines 183-204: compares virtual training systems with traditional
  training bases and notes repeatability, cost, and safety advantages.
- `01`, lines 237-240: explicitly limits the claim by stating real base
  training remains needed for backbone and expert training.

Grounded draft claim:

- Virtual training can be used to frame earthquake rescue training around
  explicit rescue objectives, repeatable scenario rehearsal, and lower-risk
  preparation before some real-field training.

Claim limit:

- Do not claim proven rescue-performance improvement. The source itself
  preserves a role for real training bases, especially for advanced trainees.

Next drafting use:

- Use this as the introduction/problem-framing section.

## Section 2: Foreign Military Training Characteristics

Mapped preview:

- `Q2_FOREIGN_MILITARY_CHARACTERISTICS`

Support verdict:

- `SUPPORTED_AS_BACKGROUND_WITH_DESCRIPTIVE_LIMITS`

Primary source support:

- `02`, lines 28-32: states that the paper reviews virtual training systems in
  several foreign militaries and their characteristics.
- `02`, lines 62-80: describes virtual training as economical, safer,
  controllable, and repeatable.
- `02`, lines 85-96: characterizes modern military virtual training systems as
  integrating equipment, communication, battlefield environment, and operational
  assumptions.
- `02`, lines 148-224: lists system characteristics across research/design,
  environment generation, evaluation, and training process support.
- `02`, lines 372-381: notes both increased attention and remaining realism or
  operating-environment limits.

Grounded draft claim:

- Foreign military virtual training can be used as descriptive background for
  simulation-supported readiness, repeatable scenario design, and controlled
  training environments.

Claim limit:

- Avoid "foreign systems are superior" or universal modernization claims. The
  source supports background characteristics, not broad comparative judgment.

Next drafting use:

- Use as the literature/background section after the introduction.

## Section 3: VR Fire-Rescue Training Advantages

Mapped preview:

- `Q3_VR_FIRE_RESCUE_ADVANTAGES`

Support verdict:

- `SUPPORTED_AS_APPLICATION_EXAMPLE_WITH_EFFECTIVENESS_LIMITS`

Primary source support:

- `03`, lines 21-25: presents a VR fire-rescue training-system framework and
  implementation direction.
- `03`, lines 31-46: describes practical constraints in fire rescue training,
  including site, cost, repeatability, and dangerous scenarios.
- `03`, lines 69-88: describes virtual fire scenes, interaction, and trainee
  experience in simulated rescue settings.
- `03`, lines 183-209: lists system functions such as scene roaming, training
  settings, equipment selection/operation, recording, and assessment.
- `04`, lines 24-29 and 66-82: supports 3D modeling and immersive repeated
  training in fire rescue safety contexts.

Grounded draft claim:

- VR can be framed as a fire-rescue training aid that supports safer scenario
  practice, repeated drills, equipment-operation rehearsal, and assessment
  workflows.

Claim limit:

- Do not turn "safer practice environment" into measured operational
  effectiveness unless later human paper review verifies stronger evidence.

Next drafting use:

- Use as the concrete application case before the design-focused section.

## Section 4: Virtual Scene Construction Factors

Mapped preview:

- `Q4_VIRTUAL_SCENE_CONSTRUCTION_FACTORS`

Support verdict:

- `STRONGLY_SUPPORTED_FOR_DESIGN_SECTION`

Primary source support:

- `05`, lines 259-269: identifies virtual scenes as a foundation of virtual
  training and describes modeled objects, terrain, sky, and immersion.
- `05`, lines 335-342: states that virtual scene construction and training
  control are key system-development problems.
- `05`, lines 379-392: connects virtual scenes with simulated environments,
  cost/risk reduction, and training efficiency.
- `05`, lines 523-528: describes the virtual scene as the system background
  and operating environment.
- `05`, lines 551-564: discusses scene modeling and level-of-detail tradeoffs.
- `05`, lines 640-646 and 1407-1411: emphasizes real-time, interaction, and
  realism requirements.
- `05`, lines 2081-2099: summarizes modeling, optimization, real-time, and
  fidelity considerations.

Grounded draft claim:

- Virtual scene construction should be treated as a core design problem: scene
  fidelity, real-time performance, interaction design, and training-task
  coverage need to be balanced against the training objective.

Claim limit:

- Keep "fidelity" tied to training usefulness and real-time interaction, not
  visual realism alone.

Next drafting use:

- Use this as the technical/design core of the paper. Q4 is no longer the weak
  section after direct source review.

## Section 5: Military Vocational Education Value

Mapped preview:

- `Q5_MILITARY_VOCATIONAL_EDUCATION_VALUE`

Support verdict:

- `SUPPORTED_AS_VALUE_SECTION_WITH_TERMINOLOGY_LIMITS`

Primary source support:

- `06`, lines 23-26: frames a radar virtual training system for military
  vocational education.
- `06`, lines 29-43: connects military vocational education with professional
  quality and job competence.
- `06`, lines 49-60: describes equipment-practice difficulty, cost, and
  insufficient practical training.
- `06`, lines 83-90: lists training-system functions for work principle,
  process, parameter measurement, fault repair, and assessment.
- `06`, lines 118-121 and 153-176: describes operation training, parameter
  testing, fault repair, and assessment/evaluation platforms.
- `06`, lines 180-184: summarizes repeated training, equipment protection,
  efficiency, convenience, and cost-related benefits.

Grounded draft claim:

- Virtual training can be positioned as support for job-oriented military
  vocational education, especially where equipment operation, parameter
  testing, fault handling, and assessment workflows require repeated practice.

Claim limit:

- Use "supports job-oriented training and assessment workflows" rather than
  broad "proves skill transfer" unless later review adds stronger evidence.

Next drafting use:

- Use as the closing value/education section.

## Cross-Section Decisions

- `5/5` sections can proceed to cautious section drafting.
- Q4 can be promoted from earlier weak routing concern to a strong design-core
  section because direct source review found multiple relevant line ranges.
- Q1, Q3, and Q5 need careful wording around effectiveness, safety, and skill
  transfer.
- Q2 should stay descriptive and background-oriented.

## Drafting Rules For Next Step

Use:

- "can support"
- "can be framed as"
- "the reviewed source describes"
- "the draft should treat this as"

Avoid:

- "proves"
- "guarantees"
- "significantly improves" unless independently reviewed
- "production-ready"
- "paper-quality accepted"
- "general RAG-ready"

## Recommended Next TaskSpec

`PARENT_LOCAL_PAPER_RAG_SECTION_DRAFT_A1`

Goal:

- Produce a source-grounded, non-final section draft using the five supported
  sections above.
- Keep each paragraph mapped to source file/line ranges.
- Preserve cautious language and explicit claim limits.
- Mark the output as human-review draft only.

## Boundary

This source-grounding review reads only the user-authorized local Markdown
corpus under `D:\Obsidian\paper-pilot\papers\virtual-training`.

It does not expose long raw source excerpts, raw PDF text, raw chunks, raw query
text, source paths beyond reviewer file references, vectors, FAISS binaries,
WriteLab payloads/responses, Zotero key/API material, attachments, full text,
`paragraph_text`, browser/CDP/cloud, MiniApp payloads, external/private RAG
payloads, or secrets.

It does not claim final governance acceptance, paper-quality acceptance,
production readiness, broad/general RAG readiness, whole-vault readiness,
external/private RAG readiness, cloud readiness, cloud vector DB readiness, or
RuntimeAuthorization.

