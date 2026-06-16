from __future__ import annotations

import argparse
import hashlib
import json
import re
import zipfile
from pathlib import Path
from typing import Iterable
from xml.sax.saxutils import escape


VARIANTS = {
    "short-paper": {
        "md": "local-paper-rag-short-paper-v1.0.md",
        "docx": "local-paper-rag-short-paper-v1.0.docx",
        "title": "面向应急救援与军事职业教育的虚拟训练系统：辅助价值、场景构建与评价边界",
        "role": "短论文审阅稿",
    },
    "technical-note": {
        "md": "local-paper-rag-technical-note-v1.0.md",
        "docx": "local-paper-rag-technical-note-v1.0.docx",
        "title": "虚拟训练系统辅助训练价值的技术札记：场景构建与评价边界",
        "role": "技术札记审阅稿",
    },
    "internal-brief": {
        "md": "local-paper-rag-internal-brief-v1.0.md",
        "docx": "local-paper-rag-internal-brief-v1.0.docx",
        "title": "本地论文 RAG 交付内部研究简报 v1.0",
        "role": "内部研究简报",
    },
}

PACKAGE_NAME = "local-paper-rag-review-variants-v1.0-package.zip"
MANIFEST_NAME = "local-paper-rag-review-variants-v1.0-manifest.json"
README_NAME = "REVIEW-VARIANTS-README.md"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def normalize_newlines(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def build_short_paper(base: str) -> str:
    return base.strip() + "\n"


def build_technical_note(base: str) -> str:
    text = normalize_newlines(base).strip()
    text = re.sub(
        r"^# .+$",
        "# 虚拟训练系统辅助训练价值的技术札记：场景构建与评价边界",
        text,
        count=1,
        flags=re.MULTILINE,
    )
    note = (
        "## 札记定位\n\n"
        "本文按技术札记处理，重点不在提出新的训练效果实证结论，而在把现有文献中的"
        "辅助训练价值、场景构建要点和评价边界整理成可审阅、可复核的技术判断。"
        "因此，本文适合作为方案论证、课程论文或项目评审材料的基础稿，不应直接作为"
        "训练成效已经被证明的实证论文使用。\n\n"
    )
    text = text.replace("## 摘要\n\n", note + "## 摘要\n\n", 1)
    text = text.replace("## 1. 问题提出：为什么需要虚拟训练", "## 1. 技术问题：虚拟训练要解决什么")
    text = text.replace("## 2. 应用场景：救援训练与职业教育的共同需求", "## 2. 应用对象：救援训练与职业教育")
    text = text.replace("## 4. 技术核心：虚拟场景如何从展示模型转向训练环境", "## 4. 技术核心：从展示模型到训练环境")
    text = text.replace(
        "后续研究应进一步补充实验评价、过程数据和专家审阅结果，以检验虚拟训练对真实任务能力、协同表现和训练保持效果的实际影响。",
        "作为技术札记，本文的结论应停留在辅助价值、设计要点和证据边界层面；若要进入正式实证研究，仍需补充实验评价、过程数据和专家审阅结果。",
    )
    return text.strip() + "\n"


def build_internal_brief() -> str:
    return "\n".join(
        [
            "# 本地论文 RAG 交付内部研究简报 v1.0",
            "",
            "## 当前结论",
            "",
            "当前交付已经形成可供人工审阅的短论文/技术札记基础稿。稿件可以稳妥表达虚拟训练系统在应急救援与军事职业教育中的辅助训练价值、场景构建要点和评价边界，但不能宣称训练效果已经被充分证明。",
            "",
            "## 已完成的自动化链路",
            "",
            "1. PDF 文献被转换为本地 Markdown/Obsidian 审阅材料。",
            "2. 本地 FAISS RAG 管线完成索引、复用、检索和答案预览。",
            "3. 质量评估、hybrid rerank 和 answer preview 产生 minimized evidence。",
            "4. 当前论文 v1.0 已生成 Markdown、DOCX、交付包和验证报告。",
            "",
            "## 当前可用于什么",
            "",
            "- 作为短论文审阅稿：适合继续打磨标题、摘要、结论和参考文献格式。",
            "- 作为技术札记：适合用于说明方案价值、技术边界和后续验证路径。",
            "- 作为内部研究简报：适合快速汇报当前系统已经打通的论文辅助写作闭环。",
            "",
            "## 当前不能宣称什么",
            "",
            "- 不能宣称最终论文质量已经接受。",
            "- 不能宣称虚拟训练效果已经被实验证明。",
            "- 不能宣称生产就绪、全库 RAG 就绪或外部 RAG 服务就绪。",
            "- 不能把本地工具链验证等同于专家审稿或真实训练效果评价。",
            "",
            "## 接下来需要人工决定",
            "",
            "1. 选择最终用途：短论文、技术札记、课程论文式综述，或内部研究简报。",
            "2. 人工核对参考文献元数据、卷期页码、DOI 和目标格式。",
            "3. 判断是否需要补充真实训练实验数据；如果不补充，应继续保持谨慎结论。",
            "",
            "## 边界",
            "",
            "本简报不包含原始 PDF 正文、原始 Markdown 正文、原始 chunks、检索 query、向量、FAISS 二进制索引、API key、WriteLab payload 或任何生产凭据。",
            "",
        ]
    )


def paragraph_xml(text: str, style: str | None = None) -> str:
    if not text:
        return "<w:p/>"
    style_xml = f'<w:pPr><w:pStyle w:val="{style}"/></w:pPr>' if style else ""
    return f"<w:p>{style_xml}<w:r><w:t xml:space=\"preserve\">{escape(text)}</w:t></w:r></w:p>"


def markdown_to_docx_xml(markdown: str) -> str:
    paragraphs: list[str] = []
    for raw_line in normalize_newlines(markdown).split("\n"):
        line = raw_line.rstrip()
        if not line:
            paragraphs.append("<w:p/>")
        elif line.startswith("# "):
            paragraphs.append(paragraph_xml(line[2:].strip(), "Title"))
        elif line.startswith("## "):
            paragraphs.append(paragraph_xml(line[3:].strip(), "Heading1"))
        elif re.match(r"^\d+\. ", line):
            paragraphs.append(paragraph_xml(line, "ListParagraph"))
        elif line.startswith("- "):
            paragraphs.append(paragraph_xml(line, "ListParagraph"))
        else:
            paragraphs.append(paragraph_xml(line))
    body = "\n".join(paragraphs)
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        f"<w:body>{body}"
        '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440"/></w:sectPr>'
        "</w:body></w:document>"
    )


def write_docx(path: Path, markdown: str) -> None:
    entries = {
        "[Content_Types].xml": (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
            '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
            '<Default Extension="xml" ContentType="application/xml"/>'
            '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
            '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
            "</Types>"
        ),
        "_rels/.rels": (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
            "</Relationships>"
        ),
        "word/_rels/document.xml.rels": (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"/>'
        ),
        "word/styles.xml": styles_xml(),
        "word/document.xml": markdown_to_docx_xml(markdown),
    }
    write_zip(path, entries)


def styles_xml() -> str:
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        '<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:rPr><w:rFonts w:ascii="Microsoft YaHei" w:eastAsia="Microsoft YaHei"/><w:sz w:val="22"/></w:rPr></w:style>'
        '<w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:rPr><w:b/><w:rFonts w:ascii="Microsoft YaHei" w:eastAsia="Microsoft YaHei"/><w:sz w:val="32"/></w:rPr></w:style>'
        '<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="Heading 1"/><w:rPr><w:b/><w:rFonts w:ascii="Microsoft YaHei" w:eastAsia="Microsoft YaHei"/><w:sz w:val="26"/></w:rPr></w:style>'
        '<w:style w:type="paragraph" w:styleId="ListParagraph"><w:name w:val="List Paragraph"/><w:pPr><w:ind w:left="360"/></w:pPr><w:rPr><w:rFonts w:ascii="Microsoft YaHei" w:eastAsia="Microsoft YaHei"/><w:sz w:val="22"/></w:rPr></w:style>'
        "</w:styles>"
    )


def write_zip(path: Path, entries: dict[str, str | bytes]) -> None:
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for name in sorted(entries):
            info = zipfile.ZipInfo(name)
            info.date_time = (2026, 6, 16, 0, 0, 0)
            info.compress_type = zipfile.ZIP_DEFLATED
            payload = entries[name]
            if isinstance(payload, str):
                payload = payload.encode("utf-8")
            zf.writestr(info, payload)


def package_readme() -> str:
    return "\n".join(
        [
            "# Local Paper RAG Review Variants v1.0",
            "",
            "This package contains three human-review variants derived from the current v1.0 manuscript.",
            "",
            "- short-paper: formal short-paper draft.",
            "- technical-note: technical note draft with explicit scope framing.",
            "- internal-brief: internal research brief for quick status communication.",
            "",
            "Boundary: these artifacts do not grant final paper-quality acceptance, training-effect acceptance, production readiness, broad RAG readiness, whole-vault readiness, or RuntimeAuthorization.",
            "",
        ]
    )


def build(root: Path) -> dict[str, object]:
    artifacts = root / "integration" / "artifacts" / "paper-drafts"
    base_path = artifacts / "local-paper-rag-clean-manuscript-v1.0.md"
    base = base_path.read_text(encoding="utf-8")
    variants = {
        "short-paper": build_short_paper(base),
        "technical-note": build_technical_note(base),
        "internal-brief": build_internal_brief(),
    }

    file_hashes: dict[str, str] = {}
    for key, markdown in variants.items():
        spec = VARIANTS[key]
        md_path = artifacts / spec["md"]
        docx_path = artifacts / spec["docx"]
        md_path.write_text(markdown, encoding="utf-8", newline="\n")
        write_docx(docx_path, markdown)
        file_hashes[spec["md"]] = sha256_file(md_path)
        file_hashes[spec["docx"]] = sha256_file(docx_path)

    manifest = {
        "schema_version": 1,
        "generated_at": "deterministic-local-paper-rag-review-variants-v1.0",
        "source": "local-paper-rag-clean-manuscript-v1.0.md",
        "variants": [
            {
                "id": key,
                "role": VARIANTS[key]["role"],
                "markdown": VARIANTS[key]["md"],
                "docx": VARIANTS[key]["docx"],
                "title": VARIANTS[key]["title"],
                "markdown_sha256": file_hashes[VARIANTS[key]["md"]],
                "docx_sha256": file_hashes[VARIANTS[key]["docx"]],
            }
            for key in VARIANTS
        ],
        "non_final_boundary": {
            "paper_quality_acceptance": False,
            "training_effect_acceptance": False,
            "production_ready": False,
            "broad_rag_ready": False,
            "runtime_authorization": False,
        },
    }
    manifest_path = artifacts / MANIFEST_NAME
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    file_hashes[MANIFEST_NAME] = sha256_file(manifest_path)

    package_entries: dict[str, str | bytes] = {
        README_NAME: package_readme(),
        MANIFEST_NAME: manifest_path.read_bytes(),
    }
    for key in VARIANTS:
        spec = VARIANTS[key]
        package_entries[spec["md"]] = (artifacts / spec["md"]).read_bytes()
        package_entries[spec["docx"]] = (artifacts / spec["docx"]).read_bytes()
    for support in (
        "submission-decision-matrix-v1.0.md",
        "usage-profile-short-paper-v1.0.md",
        "usage-profile-technical-note-v1.0.md",
        "usage-profile-internal-brief-v1.0.md",
        "allowed-claims-v1.0.md",
        "non-claim-boundary-v1.0.md",
    ):
        support_path = artifacts / support
        if support_path.exists():
            package_entries[support] = support_path.read_bytes()

    package_path = artifacts / PACKAGE_NAME
    write_zip(package_path, package_entries)
    package_hash = sha256_file(package_path)
    with zipfile.ZipFile(package_path) as zf:
        package_list = sorted(zf.namelist())

    return {
        "manifest": str(manifest_path),
        "package": str(package_path),
        "package_sha256": package_hash,
        "package_entries": package_list,
        "file_hashes": file_hashes,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build local paper RAG review variants v1.0.")
    parser.add_argument("--root", default=".", help="Repository root.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    result = build(Path(args.root).resolve())
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
