# Parent Local Paper RAG Reference Cleanup A1

## Verdict

`REFERENCE_DRAFT_V0_2_READY_FOR_HUMAN_CITATION_REVIEW`

The local paper RAG reviewer draft now has a v0.2 Markdown artifact with a
reference draft section derived from local PDF first-page metadata and text.

This is not final citation acceptance, not paper-quality acceptance, not final
governance acceptance, not production readiness, and not RuntimeAuthorization.

## Artifacts

- v0.1 source:
  `integration/artifacts/paper-drafts/local-paper-rag-reviewer-draft-v0.1.md`
- v0.2 reference-cleanup draft:
  `integration/artifacts/paper-drafts/local-paper-rag-reviewer-draft-v0.2.md`

## Local Source Probe

Authorized local PDF folder:

- `E:\厂里\虚拟训练`

PDF source facts extracted locally with PyMuPDF:

- `三维建模技术在灭火救援作战训练安全中的应用初探_吴东瑾.pdf`
  - first-page title/author observed: `三维建模技术在灭火救援作战训练安全中的应用初探`, `吴东瑾`
  - journal/page signal observed: `今日消防`, `46`, article number `2096-1227(2024)12-0046-03`
- `关于利用虚拟现实技术建立“地震救援技术虚拟训练系统”的几点思考_褚鑫杰.pdf`
  - title/author observed: `关于利用虚拟现实技术建立“地震救援技术虚拟训练系统”的几点思考`, `褚鑫杰`
  - journal signal observed: `中国应急救援`
- `国外军用虚拟训练系统研究.pdf`
  - title/authors observed: `国外军用虚拟训练系统研究`, `焦楷哲`, `程培源`, `刘滔`, `孟超`
  - date signal observed: `本文2012-12-03收到`
- `基于虚拟现实技术的灭火救援训练系统.pdf`
  - title/authors observed: `基于虚拟现实技术的灭火救援训练系统`, `张云明`, `陈蕾`
  - article number observed: `1009-0029(2010)11-0996-03`
- `虚拟训练系统的虚拟场景研究.pdf`
  - thesis signal observed: `工学硕士学位论文`, `沈裕喜`, `国防科学技术大学研究生院`, `二〇一一年十一月`
- `虚拟训练系统在军事职业教育中的应用研究.pdf`
  - title/authors observed: `虚拟训练系统在军事职业教育中的应用研究`, `胡晓琴`, `张朝伟`, `焦晓丽`
  - journal signal observed: `产业与科技论坛`, `2022 年第21 卷第9 期`

## Reference Cleanup Decisions

- Use `[S1]` through `[S6]` as stable draft identifiers.
- Add a `参考文献草案` section to v0.2.
- Mark incomplete year/volume/page fields as `待核`.
- Do not pretend low-confidence bibliographic fields are final.
- Keep human citation cleanup as a required gate.

## Verification

- PyMuPDF availability: PASS.
- Local PDF folder existence and file listing: PASS.
- v0.2 includes `[S1]` through `[S6]`: PASS.
- v0.2 includes `参考文献草案`: PASS.
- v0.2 keeps low-confidence fields marked as `待核`: PASS.
- `git diff --check`: PASS.

## Boundary

This cleanup uses local PDF first-page metadata/text only for citation review.
It does not call Zotero APIs, read Zotero keys, call external bibliography
services, call WriteLab, call cloud LLMs, invoke browser/CDP, MiniApp, external
RAG, or private runtime services.

It does not claim final citation acceptance, final governance acceptance,
paper-quality acceptance, production readiness, broad/general RAG readiness,
whole-vault readiness, external/private RAG readiness, cloud readiness, cloud
vector DB readiness, or RuntimeAuthorization.

