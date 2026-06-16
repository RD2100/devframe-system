# Parent Local Paper RAG Citation Style And Review A1

## Verdict

`CITATION_REVIEW_PACKET_READY_FOR_HUMAN_PAPER_REVIEW`

This packet turns the source-grounded section draft into a reviewer-facing
paper draft aid. It adds citation placeholders, a source table, and decision
gates. It does not claim final paper quality, final governance acceptance,
production readiness, broad/general RAG readiness, or RuntimeAuthorization.

## Evidence Basis

- Section draft:
  `integration/reports/parent-local-paper-rag-section-draft-a1-2026-06-16.md`
- Source grounding review:
  `integration/reports/parent-local-paper-rag-source-grounding-review-a1-2026-06-16.md`
- Authorized source folder:
  `D:\Obsidian\paper-pilot\papers\virtual-training`

## Citation Placeholder Policy

Use stable placeholders before final citation cleanup:

- `[S1]` Earthquake rescue VR training paper.
- `[S2]` Foreign military virtual training systems paper.
- `[S3]` VR fire-rescue training system paper.
- `[S4]` 3D modeling in fire-rescue training safety paper.
- `[S5]` Virtual scene research paper.
- `[S6]` Virtual training in military vocational education paper.

Formal GB/T 7714 entries are not finalized in this packet because the converted
Markdown front matter contains encoding noise. Human citation cleanup should
use the original PDF metadata or a trusted bibliographic source before final
paper submission.

## Source Table

| ID | Local Source File | Role In Draft | Stable Evidence |
|---|---|---|---|
| S1 | `01-关于利用虚拟现实技术建立“地震救援技术虚拟训练系统”的几点思考_褚鑫杰.md` | earthquake rescue purpose, virtual training as supplement | lines 27-29, 106-116, 120-158, 183-204, 237-240 |
| S2 | `02-国外军用虚拟训练系统研究.md` | foreign military background and system characteristics | lines 28-32, 62-80, 85-96, 148-224, 372-381 |
| S3 | `03-基于虚拟现实技术的灭火救援训练系统.md` | VR fire-rescue application and training functions | lines 21-25, 31-46, 69-88, 183-209 |
| S4 | `04-三维建模技术在灭火救援作战训练安全中的应用初探_吴东瑾.md` | 3D modeling and fire-rescue repeated immersive training support | lines 24-29, 66-82 |
| S5 | `05-虚拟训练系统的虚拟场景研究.md` | virtual scene construction, fidelity, real-time interaction, optimization | lines 259-269, 335-342, 379-392, 523-528, 551-564, 640-646, 1407-1411, 2081-2099 |
| S6 | `06-虚拟训练系统在军事职业教育中的应用研究.md` | military vocational education, equipment operation, assessment workflows | lines 23-26, 29-43, 49-60, 83-90, 118-121, 153-176, 180-184 |

## Draft With Citation Placeholders

### Abstract

虚拟训练系统为高风险、强情境和高成本的训练任务提供了一种可重复、可控制的辅助训练方式。基于本地授权语料的源文献核对，当前草稿可以从五个方向展开：地震救援训练目标、国外军用虚拟训练系统特征、灭火救援训练中的虚拟现实应用、虚拟场景构建要点，以及军事职业教育中的训练价值。本文草稿强调虚拟训练的辅助定位：它可以用于训练目标梳理、流程演练、场景复现、交互操作和评价支持，但不能据此直接断言训练效果已经被充分证明。[S1][S2][S3][S5][S6]

### 1. 应急救援训练为什么需要虚拟训练

地震救援等应急训练具有场景复杂、风险较高、装备和场地约束明显等特点。传统训练能够提供真实环境和实装操作经验，但在场地复现、反复训练、危险情境模拟和成本控制方面存在现实限制。因此，虚拟训练更适合作为一种前置准备和补充训练方式：它可以帮助训练者理解救援目标、熟悉基本流程，并在较低风险的环境中反复接触典型灾害场景。[S1]

在地震救援场景中，虚拟现实技术的意义不应被表述为取代真实训练，而应被表述为补充真实训练。它更适合承担训练目标组织、救援环境熟悉、流程演练和真实训练前准备等任务。[S1]

Reviewer citation decision:

- Keep `[S1]` as the primary source.
- Do not add outcome-effectiveness wording unless a human reviewer adds a
  stronger evaluation source.

### 2. 国外军用虚拟训练系统的启示

国外军用虚拟训练系统的相关研究可以作为背景参照。现有资料支持把军用虚拟训练理解为一种围绕装备操作、通信环境、战场环境、作战设想和训练评估组织起来的训练体系，而不是单一仿真软件。[S2]

对本文来说，这部分背景的价值不在于简单比较“国外先进、国内不足”，而在于提炼虚拟训练系统的一般设计方向：训练场景服务明确任务，训练过程可记录和评估，系统支持重复训练和条件控制，同时承认真实感、运行环境和复杂战场复现方面的限制。[S2]

Reviewer citation decision:

- Keep `[S2]` as descriptive background.
- Avoid using `[S2]` as proof of universal military training superiority.

### 3. 虚拟现实对灭火救援训练的支持

灭火救援训练同样面临真实场景难复现、危险程度高、训练资源消耗大和重复组织困难等问题。虚拟现实训练系统可以通过三维场景、交互操作和训练流程设置，让受训者在模拟火灾和救援环境中进行观察、路线熟悉、装备选择、操作练习和过程评估。[S3][S4]

这类系统的价值主要体现在训练组织层面：它有助于反复接触典型灾情、熟悉装备和操作流程，并通过记录和评价模块形成训练反馈。对于高风险救援任务，这种虚拟训练更适合作为真实训练之前的准备、真实训练之间的巩固，以及难以频繁组织的复杂场景演练。[S3][S4]

Reviewer citation decision:

- Use `[S3]` for VR fire-rescue system functions.
- Use `[S4]` for 3D modeling and repeated immersive training support.
- Avoid claiming measured operational effectiveness.

### 4. 虚拟场景构建的关键因素

虚拟场景是虚拟训练系统能否服务训练目标的关键基础。场景构建不能只追求视觉真实，而应围绕训练任务决定需要复现哪些环境要素、保留哪些交互环节、采用何种建模精度，以及如何平衡真实感和实时运行性能。[S5]

从设计角度看，虚拟场景建设至少包括四个问题：场景 fidelity 服务训练目标，环境和装备建模覆盖关键对象与空间关系，交互设计支持观察、选择、操作和反馈行为，系统优化保证训练过程实时性。这样处理后，虚拟场景才能从“展示性模型”转向“训练性环境”。[S5]

Reviewer citation decision:

- Treat `[S5]` as the technical core source.
- This section is currently the strongest candidate for expansion.
- Keep fidelity tied to training usefulness and real-time interaction.

### 5. 军事职业教育中的训练价值

在军事职业教育中，虚拟训练的价值主要来自岗位任务和训练内容之间的连接。装备类、操作类和维修类训练往往受到实装数量、训练成本、故障复现难度和练习机会限制。虚拟训练系统可以将装备结构、工作原理、操作流程、参数测试、故障排查和考核评价组织到同一训练环境中。[S6]

因此，这一部分更适合强调“岗位导向的训练支持”，而不是直接宣称“能力迁移已经完成”。较稳妥的表述是：虚拟训练可以帮助军事职业教育把理论学习、操作练习、故障处理和评价反馈结合起来，特别适用于需要反复练习但实装训练成本较高的场景。[S6]

Reviewer citation decision:

- Use `[S6]` for job-oriented training and assessment workflow support.
- Do not use the current source set to prove skill transfer.

## Source-Claim Matrix

| Draft Claim | Supported By | Current Decision |
|---|---|---|
| Virtual training can support earthquake rescue preparation. | S1 | keep, cautious |
| Virtual training replaces real rescue training. | none | reject |
| Foreign military systems show repeatable and controllable training traits. | S2 | keep as background |
| Foreign military systems prove broad superiority. | none | reject |
| VR supports fire-rescue scenario practice and training functions. | S3, S4 | keep, cautious |
| VR fire-rescue systems prove operational performance gains. | none | reject |
| Scene construction is the design core of virtual training systems. | S5 | keep, expand |
| Vocational education can use virtual training for operation and assessment workflows. | S6 | keep, cautious |
| Current sources prove stable job skill transfer. | none | reject |

## Human Review Gate

Before this becomes a paper draft, a human reviewer should decide:

- whether the six source placeholders are enough for the intended paper scope;
- whether formal GB/T 7714 citation metadata should be repaired manually from
  original PDFs;
- whether Q4 should be expanded into the main technical contribution;
- whether Q1/Q3/Q5 need additional empirical or evaluation sources;
- whether the current draft should become a short paper, a technical note, or a
  literature-review memo.

## Recommended Next TaskSpec

`PARENT_LOCAL_PAPER_RAG_REVIEWER_READY_DRAFT_A1`

Goal:

- Produce one reviewer-ready Markdown draft that combines the section draft,
  citation placeholders, source-claim matrix, and human review gates.
- Keep all claims non-final.
- Preserve the requirement that paper-quality acceptance is a human decision.

## Boundary

This packet is a parent-level review artifact. It uses local source references
and short draft prose only. It does not expose long raw source excerpts, raw PDF
text, raw Markdown bodies, raw chunks, raw query text, vectors, FAISS binaries,
WriteLab payloads/responses, Zotero key/API material, attachments, full text,
`paragraph_text`, browser/CDP/cloud, MiniApp payloads, external/private RAG
payloads, or secrets.

It does not claim final governance acceptance, paper-quality acceptance,
production readiness, broad/general RAG readiness, whole-vault readiness,
external/private RAG readiness, cloud readiness, cloud vector DB readiness, or
RuntimeAuthorization.

