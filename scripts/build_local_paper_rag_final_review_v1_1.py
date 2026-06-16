from __future__ import annotations

import argparse
import hashlib
import json
import re
import zipfile
from pathlib import Path

from build_local_paper_rag_review_variants_v1_0 import write_docx, write_zip


VERSION = "v1.1"
VARIANT_IDS = ("short-paper", "technical-note", "internal-brief")

VARIANTS = {
    "short-paper": {
        "role": "正式短论文审阅候选稿",
        "title": "面向应急救援与军事职业教育的虚拟训练系统：辅助价值、场景构建与评价边界",
        "md": "local-paper-rag-short-paper-v1.1.md",
        "docx": "local-paper-rag-short-paper-v1.1.docx",
    },
    "technical-note": {
        "role": "技术札记审阅候选稿",
        "title": "虚拟训练系统辅助训练价值的技术札记：场景构建与评价边界",
        "md": "local-paper-rag-technical-note-v1.1.md",
        "docx": "local-paper-rag-technical-note-v1.1.docx",
    },
    "internal-brief": {
        "role": "内部研究简报",
        "title": "本地论文 RAG 交付内部研究简报 v1.1",
        "md": "local-paper-rag-internal-brief-v1.1.md",
        "docx": "local-paper-rag-internal-brief-v1.1.docx",
    },
}

MANIFEST_NAME = "local-paper-rag-review-variants-v1.1-manifest.json"
PACKAGE_NAME = "local-paper-rag-review-variants-v1.1-package.zip"
ROUTE_NAME = "local-paper-rag-human-review-route-v1.1.md"
README_NAME = "REVIEW-VARIANTS-V1.1-README.md"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def read_utf8(path: Path) -> str:
    return path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")


def write_utf8(path: Path, text: str) -> None:
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def refine_common(text: str) -> str:
    text = text.replace("本地授权文献", "相关文献")
    text = text.replace("本地流程验证", "文献分析与人工审阅")
    text = text.replace("当前版本可作为短论文或技术札记的审阅稿", "本文可作为后续人工审阅与格式校订的基础稿")
    text = re.sub(r"\[1\]\[3\]\[4\]\[5\]\[6\]", "[1,3-6]", text)
    return text


def build_short_paper(artifacts: Path) -> str:
    text = refine_common(read_utf8(artifacts / "local-paper-rag-short-paper-v1.0.md"))
    contribution = (
        "本文的主要工作是：第一，梳理虚拟训练系统在应急救援与军事职业教育中的辅助训练价值；"
        "第二，总结虚拟场景由展示模型转向训练环境的关键设计要点；"
        "第三，明确现有证据条件下训练效果评价的边界。"
    )
    if contribution not in text:
        marker = "这一定位可以避免技术乐观主义式过度承诺，也能让系统设计更聚焦于可验证、可组织、可复盘的训练任务。"
        text = text.replace(marker, marker + contribution, 1)
    return text


def build_technical_note(artifacts: Path) -> str:
    text = refine_common(read_utf8(artifacts / "local-paper-rag-technical-note-v1.0.md"))
    text = text.replace(
        "本文按技术札记处理",
        "本文按技术札记处理，优先服务于方案论证和后续系统评审",
        1,
    )
    return text


def build_internal_brief() -> str:
    return """# 本地论文 RAG 交付内部研究简报 v1.1

## 当前结论

当前交付已经形成可供人工审阅的短论文、技术札记和内部研究简报三种稿件形态。稿件可以稳妥表达虚拟训练系统在应急救援与军事职业教育中的辅助训练价值、场景构建要点和评价边界，但不能宣称训练效果已经被充分证明。

## 已完成的自动化闭环

1. 本地 PDF 文献已被转换为 Markdown/Obsidian 审阅材料。
2. 本地 FAISS RAG 管线已完成索引、复用、检索、质量评估、hybrid rerank 和 answer preview。
3. 已生成主稿、短论文稿、技术札记稿、内部简报稿、DOCX、Markdown、证据包和验证报告。
4. test-frame 和 agent-acceptance 已完成当前闭环的非最终里程碑验证。

## 当前可用于什么

- 作为正式短论文审阅候选稿：适合继续做人工审阅、引用核对和目标格式化。
- 作为技术札记：适合说明方案价值、技术边界和后续验证路径。
- 作为内部研究简报：适合快速汇报当前系统已经打通的论文辅助写作闭环。

## 当前不能宣称什么

- 不能宣称最终论文质量已经被接受。
- 不能宣称虚拟训练效果已经被实验证明。
- 不能宣称生产就绪、全域 RAG 就绪、外部 RAG 服务就绪或 RuntimeAuthorization 已授予。
- 不能把本地工具链验证等同于专家审稿、真实训练效果评价或正式投稿接收。

## 接下来需要人工决定

1. 选择最终用途：短论文、技术札记、课程论文式综述，或内部研究简报。
2. 核对参考文献元数据、卷期页码、DOI 和目标格式。
3. 判断是否需要补充真实训练实验数据；如果不补充，应继续保持谨慎结论。

## 边界

本简报不包含原始 PDF 正文、原始 Markdown 正文、原始 chunks、检索 query、向量、FAISS 二进制索引、API key、WriteLab payload 或任何生产凭据。
"""


def build_route_note() -> str:
    return """# Local Paper RAG Human Review Route v1.1

## 推荐路线

当前最务实的路线是先按“正式短论文审阅候选稿”推进。理由是：正文结构已经完整，标题、摘要和结论都保持了训练效果边界；如果后续发现目标期刊要求更严格，再降级为技术札记或内部研究简报也容易。

## 人工审阅重点

1. 标题是否采用“辅助价值、场景构建与评价边界”这一聚焦表达。
2. 摘要是否避免项目内部流程词，保持正式论文语气。
3. 结论是否继续避免超出现有证据基础的强证明表达。
4. 参考文献是否按目标格式统一，尤其是作者、题名、期刊、年份、卷期、页码、DOI 和学位论文地点。
5. 是否需要补充真实训练实验数据；若不补充，文章应定位为短论文、技术札记或综述型研究札记。

## 自动化已经完成

- 生成三种稿件形态：短论文、技术札记、内部研究简报。
- 生成 Markdown 与 DOCX。
- 生成 manifest 和 ZIP 交付包。
- 校验文稿中没有内部流程词、最终接受过度声明、生产就绪或 RuntimeAuthorization 声明。

## 仍需人工确认

- 目标使用场景。
- 参考文献元数据真实性。
- 是否需要进一步投期刊格式化。
- 是否接受当前“训练效果不能强证明”的谨慎结论。
"""


def package_readme(package_hash: str | None = None) -> str:
    hash_line = f"\nPackage SHA256: `{package_hash}`\n" if package_hash else ""
    return f"""# Local Paper RAG Review Variants v1.1

This package is the current human-review candidate bundle.

Contents:

- `local-paper-rag-short-paper-v1.1.md/docx`
- `local-paper-rag-technical-note-v1.1.md/docx`
- `local-paper-rag-internal-brief-v1.1.md/docx`
- `local-paper-rag-human-review-route-v1.1.md`
- `local-paper-rag-review-variants-v1.1-manifest.json`

Boundary: this package does not grant final paper-quality acceptance, training-effect acceptance, final governance acceptance, production readiness, broad/general RAG readiness, whole-vault readiness, cloud/vector DB readiness, or RuntimeAuthorization.
{hash_line}"""


def build(root: Path) -> dict[str, object]:
    artifacts = root / "integration" / "artifacts" / "paper-drafts"
    artifacts.mkdir(parents=True, exist_ok=True)

    contents = {
        "short-paper": build_short_paper(artifacts),
        "technical-note": build_technical_note(artifacts),
        "internal-brief": build_internal_brief(),
    }

    hashes: dict[str, str] = {}
    for variant_id in VARIANT_IDS:
        spec = VARIANTS[variant_id]
        md_path = artifacts / spec["md"]
        docx_path = artifacts / spec["docx"]
        write_utf8(md_path, contents[variant_id])
        write_docx(docx_path, contents[variant_id])
        hashes[spec["md"]] = sha256_file(md_path)
        hashes[spec["docx"]] = sha256_file(docx_path)

    route_path = artifacts / ROUTE_NAME
    write_utf8(route_path, build_route_note())
    hashes[ROUTE_NAME] = sha256_file(route_path)

    manifest = {
        "schema_version": 1,
        "generated_at": "deterministic-local-paper-rag-review-variants-v1.1",
        "source": "local-paper-rag-review-variants-v1.0",
        "recommended_route": "short-paper-human-review-first",
        "variants": [
            {
                "id": variant_id,
                "role": VARIANTS[variant_id]["role"],
                "title": VARIANTS[variant_id]["title"],
                "markdown": VARIANTS[variant_id]["md"],
                "docx": VARIANTS[variant_id]["docx"],
                "markdown_sha256": hashes[VARIANTS[variant_id]["md"]],
                "docx_sha256": hashes[VARIANTS[variant_id]["docx"]],
            }
            for variant_id in VARIANT_IDS
        ],
        "review_route": ROUTE_NAME,
        "review_route_sha256": hashes[ROUTE_NAME],
        "non_final_boundary": {
            "paper_quality_acceptance": False,
            "training_effect_acceptance": False,
            "final_governance_acceptance": False,
            "production_ready": False,
            "broad_rag_ready": False,
            "whole_vault_ready": False,
            "runtime_authorization": False,
        },
    }
    manifest_path = artifacts / MANIFEST_NAME
    write_utf8(manifest_path, json.dumps(manifest, indent=2, ensure_ascii=False))
    hashes[MANIFEST_NAME] = sha256_file(manifest_path)

    entries: dict[str, str | bytes] = {
        README_NAME: package_readme(),
        MANIFEST_NAME: manifest_path.read_bytes(),
        ROUTE_NAME: route_path.read_bytes(),
    }
    for variant_id in VARIANT_IDS:
        spec = VARIANTS[variant_id]
        entries[spec["md"]] = (artifacts / spec["md"]).read_bytes()
        entries[spec["docx"]] = (artifacts / spec["docx"]).read_bytes()
    package_path = artifacts / PACKAGE_NAME
    write_zip(package_path, entries)
    package_hash = sha256_file(package_path)

    entries[README_NAME] = package_readme(package_hash)
    write_zip(package_path, entries)
    package_hash = sha256_file(package_path)

    with zipfile.ZipFile(package_path) as zf:
        package_entries = sorted(zf.namelist())

    return {
        "manifest": str(manifest_path),
        "package": str(package_path),
        "package_sha256": package_hash,
        "package_entries": package_entries,
        "file_hashes": hashes,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build local paper RAG final review package v1.1.")
    parser.add_argument("--root", default=".", help="Repository root.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    print(json.dumps(build(Path(args.root).resolve()), indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
