from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any


EXPECTED_FILES = {
    "short-paper": {
        "md": "local-paper-rag-short-paper-v1.1.md",
        "docx": "local-paper-rag-short-paper-v1.1.docx",
        "required": ["辅助价值、场景构建与评价边界", "由于现有证据主要来自文献分析", "后续仍需结合实验评价、过程数据和专家审阅"],
    },
    "technical-note": {
        "md": "local-paper-rag-technical-note-v1.1.md",
        "docx": "local-paper-rag-technical-note-v1.1.docx",
        "required": ["技术札记", "方案论证和后续系统评审", "训练成效已经被证明"],
    },
    "internal-brief": {
        "md": "local-paper-rag-internal-brief-v1.1.md",
        "docx": "local-paper-rag-internal-brief-v1.1.docx",
        "required": ["内部研究简报", "已完成的自动化闭环", "不能宣称最终论文质量已经被接受"],
    },
}

EXPECTED_PACKAGE_ENTRIES = [
    "REVIEW-VARIANTS-V1.1-README.md",
    "local-paper-rag-human-review-route-v1.1.md",
    "local-paper-rag-internal-brief-v1.1.docx",
    "local-paper-rag-internal-brief-v1.1.md",
    "local-paper-rag-review-variants-v1.1-manifest.json",
    "local-paper-rag-short-paper-v1.1.docx",
    "local-paper-rag-short-paper-v1.1.md",
    "local-paper-rag-technical-note-v1.1.docx",
    "local-paper-rag-technical-note-v1.1.md",
]

FORBIDDEN_TEXT = [
    "本地授权文献",
    "本地流程验证",
    "当前版本可作为短论文或技术札记的审阅稿",
    "显著提升训练效果",
    "有效替代真实训练",
    "全面改善军事职业教育质量",
    "final_acceptance_claimed\": true",
    "paper_quality_acceptance\": true",
    "production_ready\": true",
    "runtime_authorization\": true",
    "raw_pdf_text",
    "raw_markdown_body",
    "raw_chunks",
    "raw_query",
    "source_path",
    "FAISS binary",
    "WRITELAB_TOKEN",
]


@dataclass
class CheckResult:
    name: str
    status: str
    details: dict[str, Any]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def add(checks: list[CheckResult], name: str, passed: bool, **details: Any) -> None:
    checks.append(CheckResult(name, "PASS" if passed else "FAIL", details))


def safe_name(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", value).strip("_").lower()[:72] or "token"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def verify(root: Path) -> dict[str, Any]:
    artifacts = root / "integration" / "artifacts" / "paper-drafts"
    manifest_path = artifacts / "local-paper-rag-review-variants-v1.1-manifest.json"
    package_path = artifacts / "local-paper-rag-review-variants-v1.1-package.zip"
    route_path = artifacts / "local-paper-rag-human-review-route-v1.1.md"
    checks: list[CheckResult] = []

    for path in (manifest_path, package_path, route_path):
        add(checks, f"{path.name}_exists", path.exists(), path=str(path))
    if not manifest_path.exists() or not package_path.exists():
        return build_report(root, checks, package_path)

    manifest = json.loads(read_text(manifest_path))
    add(checks, "manifest_schema_version", manifest.get("schema_version") == 1)
    add(checks, "manifest_recommended_route", manifest.get("recommended_route") == "short-paper-human-review-first")
    add(checks, "manifest_not_mojibake", "鐭" not in json.dumps(manifest, ensure_ascii=False))
    boundary = manifest.get("non_final_boundary", {})
    for key in (
        "paper_quality_acceptance",
        "training_effect_acceptance",
        "final_governance_acceptance",
        "production_ready",
        "broad_rag_ready",
        "whole_vault_ready",
        "runtime_authorization",
    ):
        add(checks, f"boundary_{key}_false", boundary.get(key) is False)

    manifest_rows = {row.get("id"): row for row in manifest.get("variants", [])}
    add(checks, "variant_ids_exact", set(manifest_rows) == set(EXPECTED_FILES), actual=sorted(manifest_rows))

    for variant_id, spec in EXPECTED_FILES.items():
        md_path = artifacts / spec["md"]
        docx_path = artifacts / spec["docx"]
        add(checks, f"{variant_id}_md_exists", md_path.exists(), path=str(md_path))
        add(checks, f"{variant_id}_docx_exists", docx_path.exists(), path=str(docx_path))
        if not md_path.exists() or not docx_path.exists():
            continue
        text = read_text(md_path)
        for token in spec["required"]:
            add(checks, f"{variant_id}_contains_{safe_name(token)}", token in text, token=token)
        for token in FORBIDDEN_TEXT:
            add(checks, f"{variant_id}_excludes_{safe_name(token)}", token not in text, token=token)
        with zipfile.ZipFile(docx_path) as zf:
            document_xml = zf.read("word/document.xml").decode("utf-8")
        add(checks, f"{variant_id}_docx_readable", spec["required"][0] in document_xml)
        row = manifest_rows.get(variant_id, {})
        add(checks, f"{variant_id}_manifest_md_hash", row.get("markdown_sha256") == sha256_file(md_path))
        add(checks, f"{variant_id}_manifest_docx_hash", row.get("docx_sha256") == sha256_file(docx_path))

    route_text = read_text(route_path) if route_path.exists() else ""
    add(checks, "route_recommends_short_paper_first", "正式短论文审阅候选稿" in route_text)
    add(checks, "route_keeps_human_review_gate", "仍需人工确认" in route_text)

    with zipfile.ZipFile(package_path) as zf:
        entries = sorted(zf.namelist())
        payload = "\n".join(entries)
        for entry in entries:
            if entry.endswith(".md") or entry.endswith(".json"):
                payload += "\n" + zf.read(entry).decode("utf-8")
    add(checks, "package_entries_exact", entries == EXPECTED_PACKAGE_ENTRIES, actual=entries)
    for token in FORBIDDEN_TEXT:
        add(checks, f"package_excludes_{safe_name(token)}", token not in payload, token=token)

    return build_report(root, checks, package_path)


def build_report(root: Path, checks: list[CheckResult], package_path: Path) -> dict[str, Any]:
    failed = [check for check in checks if check.status != "PASS"]
    return {
        "schema_version": 1,
        "generated_at": "deterministic-local-paper-rag-final-review-v1.1-verification",
        "root": str(root),
        "package": str(package_path),
        "package_sha256": sha256_file(package_path) if package_path.exists() else None,
        "verdict": "PASS_LOCAL_PAPER_RAG_FINAL_REVIEW_V1_1_VERIFICATION" if not failed else "FAIL",
        "summary": {"passed": len(checks) - len(failed), "failed": len(failed)},
        "checks": [check.__dict__ for check in checks],
        "non_final_boundary": {
            "paper_quality_acceptance": False,
            "training_effect_acceptance": False,
            "final_governance_acceptance": False,
            "production_ready": False,
            "broad_rag_ready": False,
            "runtime_authorization": False,
        },
    }


def write_outputs(report: dict[str, Any], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "local-paper-rag-final-review-v1-1-verification.json"
    md_path = out_dir / "local-paper-rag-final-review-v1-1-verification.md"
    json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = [
        "# Local Paper RAG Final Review v1.1 Verification",
        "",
        f"- Verdict: `{report['verdict']}`",
        f"- Passed checks: {report['summary']['passed']}",
        f"- Failed checks: {report['summary']['failed']}",
        f"- Package SHA256: `{report['package_sha256']}`",
        "",
        "## Checks",
        "",
    ]
    for check in report["checks"]:
        lines.append(f"- `{check['status']}` {check['name']}")
    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "This verification covers package integrity, review-route clarity, and",
            "non-final claim boundaries. It does not grant paper-quality acceptance,",
            "training-effect acceptance, production readiness, broad/general RAG",
            "readiness, whole-vault readiness, or RuntimeAuthorization.",
            "",
        ]
    )
    md_path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Verify local paper RAG final review v1.1 artifacts.")
    parser.add_argument("--root", default=".", help="Repository root.")
    parser.add_argument(
        "--out-dir",
        default="integration/reports/local-paper-rag-final-review-v1-1-verification",
        help="Output report directory.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    report = verify(root)
    write_outputs(report, root / args.out_dir)
    print(report["verdict"])
    print(f"passed={report['summary']['passed']} failed={report['summary']['failed']}")
    return 0 if report["verdict"].startswith("PASS_") else 1


if __name__ == "__main__":
    sys.exit(main())
