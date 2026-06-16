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


MANUSCRIPT_MD = "local-paper-rag-submission-candidate-v1.2.md"
MANUSCRIPT_DOCX = "local-paper-rag-submission-candidate-v1.2.docx"
REFERENCE_CHECK = "local-paper-rag-reference-final-check-v1.2.md"
FORMAT_CLOSEOUT = "local-paper-rag-submission-format-closeout-v1.2.md"
MANIFEST_NAME = "local-paper-rag-submission-candidate-v1.2-manifest.json"
PACKAGE_NAME = "local-paper-rag-submission-candidate-v1.2-package.zip"
README_NAME = "SUBMISSION-CANDIDATE-V1.2-README.md"

EXPECTED_PACKAGE_ENTRIES = [
    README_NAME,
    REFERENCE_CHECK,
    MANIFEST_NAME,
    MANUSCRIPT_DOCX,
    MANUSCRIPT_MD,
    FORMAT_CLOSEOUT,
]

FORBIDDEN_IN_MANUSCRIPT = [
    "本地授权文献",
    "本地流程验证",
    "当前版本可作为",
    "文章编号:",
    "文章编号：",
    "RuntimeAuthorization",
    "production_ready",
    "final_acceptance",
    "raw_pdf_text",
    "raw_markdown_body",
    "raw_chunks",
    "raw_query",
    "source_path",
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
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def add(checks: list[CheckResult], name: str, passed: bool, **details: Any) -> None:
    checks.append(CheckResult(name, "PASS" if passed else "FAIL", details))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def safe_name(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", value).strip("_").lower()[:72] or "token"


def verify(root: Path) -> dict[str, Any]:
    artifacts = root / "integration" / "artifacts" / "paper-drafts"
    paths = {
        "md": artifacts / MANUSCRIPT_MD,
        "docx": artifacts / MANUSCRIPT_DOCX,
        "reference_check": artifacts / REFERENCE_CHECK,
        "format_closeout": artifacts / FORMAT_CLOSEOUT,
        "manifest": artifacts / MANIFEST_NAME,
        "package": artifacts / PACKAGE_NAME,
    }
    checks: list[CheckResult] = []

    for key, path in paths.items():
        add(checks, f"{key}_exists", path.exists(), path=str(path))
    if not all(path.exists() for path in paths.values()):
        return report(root, checks, paths["package"])

    manifest = json.loads(read_text(paths["manifest"]))
    add(checks, "manifest_schema_version", manifest.get("schema_version") == 1)
    add(checks, "manifest_requires_reference_check", manifest.get("requires_human_reference_metadata_check") is True)
    add(checks, "manifest_requires_template_check", manifest.get("requires_target_venue_template_check") is True)
    add(checks, "manifest_recommended_use", manifest.get("recommended_use") == "generic-gbt-style-human-review-candidate")

    boundary = manifest.get("non_final_boundary", {})
    for key in (
        "paper_quality_acceptance",
        "training_effect_acceptance",
        "final_governance_acceptance",
        "production_ready",
        "broad_rag_ready",
        "whole_vault_ready",
        "cloud_vector_db_ready",
        "runtime_authorization",
    ):
        add(checks, f"boundary_{key}_false", boundary.get(key) is False)

    manuscript = read_text(paths["md"])
    required_tokens = [
        "面向应急救援与军事职业教育的虚拟训练系统",
        "摘要",
        "关键词",
        "本文主要从三个方面展开",
        "由于现有证据主要来自文献分析",
        "训练效果已经得到充分证明",
        "参考文献",
        "[5] 焦楷哲, 程培源, 刘滔, 等.",
    ]
    for token in required_tokens:
        add(checks, f"manuscript_contains_{safe_name(token)}", token in manuscript, token=token)
    for token in FORBIDDEN_IN_MANUSCRIPT:
        add(checks, f"manuscript_excludes_{safe_name(token)}", token not in manuscript, token=token)

    refs = re.findall(r"^\[\d+\] ", manuscript, flags=re.MULTILINE)
    add(checks, "reference_count_six", len(refs) == 6, count=len(refs))
    add(checks, "citation_ranges_present", "[2-3]" in manuscript and "[1-4,6]" in manuscript)

    reference_check = read_text(paths["reference_check"])
    add(checks, "reference_check_requires_human", "HUMAN_REFERENCE_METADATA_CHECK_REQUIRED" in reference_check)
    add(checks, "reference_check_no_city_guess", "Do not infer a city" in reference_check)

    with zipfile.ZipFile(paths["docx"]) as zf:
        document_xml = zf.read("word/document.xml").decode("utf-8")
    add(checks, "docx_readable", "面向应急救援与军事职业教育" in document_xml)

    with zipfile.ZipFile(paths["package"]) as zf:
        entries = sorted(zf.namelist())
        payload = "\n".join(entries)
        for entry in entries:
            if entry.endswith(".md") or entry.endswith(".json"):
                payload += "\n" + zf.read(entry).decode("utf-8")
    add(checks, "package_entries_exact", entries == EXPECTED_PACKAGE_ENTRIES, actual=entries)
    add(checks, "package_has_no_absolute_paths", all(":\\" not in entry and not entry.startswith("/") for entry in entries))
    add(checks, "package_boundary_non_final", "does not grant final paper-quality acceptance" in payload)

    hashes = manifest.get("hashes", {})
    for name, path in (
        (MANUSCRIPT_MD, paths["md"]),
        (MANUSCRIPT_DOCX, paths["docx"]),
        (REFERENCE_CHECK, paths["reference_check"]),
        (FORMAT_CLOSEOUT, paths["format_closeout"]),
    ):
        add(checks, f"manifest_hash_{safe_name(name)}", hashes.get(name) == sha256_file(path))

    return report(root, checks, paths["package"])


def report(root: Path, checks: list[CheckResult], package_path: Path) -> dict[str, Any]:
    failed = [check for check in checks if check.status != "PASS"]
    return {
        "schema_version": 1,
        "generated_at": "deterministic-local-paper-rag-submission-candidate-v1.2-verification",
        "root": str(root),
        "package": str(package_path),
        "package_sha256": sha256_file(package_path) if package_path.exists() else None,
        "verdict": "PASS_LOCAL_PAPER_RAG_SUBMISSION_CANDIDATE_V1_2_VERIFICATION" if not failed else "FAIL",
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


def write_outputs(result: dict[str, Any], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "local-paper-rag-submission-candidate-v1-2-verification.json"
    md_path = out_dir / "local-paper-rag-submission-candidate-v1-2-verification.md"
    json_path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = [
        "# Local Paper RAG Submission Candidate v1.2 Verification",
        "",
        f"- Verdict: `{result['verdict']}`",
        f"- Passed checks: {result['summary']['passed']}",
        f"- Failed checks: {result['summary']['failed']}",
        f"- Package SHA256: `{result['package_sha256']}`",
        "",
        "## Checks",
        "",
    ]
    for check in result["checks"]:
        lines.append(f"- `{check['status']}` {check['name']}")
    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "This verifier checks package integrity, candidate GB/T-style",
            "formatting markers, reference-human-check gates, and non-final",
            "claim boundaries. It does not grant final paper-quality acceptance",
            "or target-venue submission readiness.",
            "",
        ]
    )
    md_path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Verify local paper RAG submission candidate v1.2.")
    parser.add_argument("--root", default=".", help="Repository root.")
    parser.add_argument(
        "--out-dir",
        default="integration/reports/local-paper-rag-submission-candidate-v1-2-verification",
        help="Output report directory.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    result = verify(root)
    write_outputs(result, root / args.out_dir)
    print(result["verdict"])
    print(f"passed={result['summary']['passed']} failed={result['summary']['failed']}")
    return 0 if result["verdict"].startswith("PASS_") else 1


if __name__ == "__main__":
    sys.exit(main())
