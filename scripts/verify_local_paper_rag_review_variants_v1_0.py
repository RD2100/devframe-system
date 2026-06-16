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


EXPECTED_VARIANTS = {
    "short-paper": {
        "md": "local-paper-rag-short-paper-v1.0.md",
        "docx": "local-paper-rag-short-paper-v1.0.docx",
        "required": ["辅助价值、场景构建与评价边界", "## 摘要", "## 参考文献"],
    },
    "technical-note": {
        "md": "local-paper-rag-technical-note-v1.0.md",
        "docx": "local-paper-rag-technical-note-v1.0.docx",
        "required": ["技术札记", "## 札记定位", "从展示模型到训练环境"],
    },
    "internal-brief": {
        "md": "local-paper-rag-internal-brief-v1.0.md",
        "docx": "local-paper-rag-internal-brief-v1.0.docx",
        "required": ["内部研究简报", "已完成的自动化链路", "当前不能宣称什么"],
    },
}

EXPECTED_PACKAGE_ENTRIES = [
    "REVIEW-VARIANTS-README.md",
    "allowed-claims-v1.0.md",
    "local-paper-rag-internal-brief-v1.0.docx",
    "local-paper-rag-internal-brief-v1.0.md",
    "local-paper-rag-review-variants-v1.0-manifest.json",
    "local-paper-rag-short-paper-v1.0.docx",
    "local-paper-rag-short-paper-v1.0.md",
    "local-paper-rag-technical-note-v1.0.docx",
    "local-paper-rag-technical-note-v1.0.md",
    "non-claim-boundary-v1.0.md",
    "submission-decision-matrix-v1.0.md",
    "usage-profile-internal-brief-v1.0.md",
    "usage-profile-short-paper-v1.0.md",
    "usage-profile-technical-note-v1.0.md",
]

FORBIDDEN_MARKERS = [
    "????????",
    "WRITELAB_TOKEN",
    "raw_pdf_text",
    "raw_markdown_body",
    "raw_chunks",
    "raw_query",
    "source_path",
    "FAISS binary",
    "final_acceptance_claimed\": true",
    "paper_quality_acceptance\": true",
    "production_ready\": true",
    "runtime_authorization\": true",
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


def add_check(checks: list[CheckResult], name: str, passed: bool, **details: Any) -> None:
    checks.append(CheckResult(name=name, status="PASS" if passed else "FAIL", details=details))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def safe_name(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", value).strip("_").lower()[:72] or "token"


def verify(root: Path) -> dict[str, Any]:
    artifacts = root / "integration" / "artifacts" / "paper-drafts"
    manifest_path = artifacts / "local-paper-rag-review-variants-v1.0-manifest.json"
    package_path = artifacts / "local-paper-rag-review-variants-v1.0-package.zip"
    checks: list[CheckResult] = []

    for path in (manifest_path, package_path):
        add_check(checks, f"{path.name}_exists", path.exists(), path=str(path))
    if not manifest_path.exists() or not package_path.exists():
        return build_report(root, checks, manifest_path, package_path)

    manifest = json.loads(read_text(manifest_path))
    add_check(checks, "manifest_schema_version", manifest.get("schema_version") == 1)
    add_check(checks, "manifest_non_final_boundary", manifest.get("non_final_boundary", {}).get("paper_quality_acceptance") is False)

    seen_hashes: dict[str, str] = {}
    variant_ids = {variant.get("id") for variant in manifest.get("variants", [])}
    add_check(checks, "manifest_variant_ids_exact", variant_ids == set(EXPECTED_VARIANTS), actual=sorted(variant_ids))

    for variant_id, spec in EXPECTED_VARIANTS.items():
        md_path = artifacts / spec["md"]
        docx_path = artifacts / spec["docx"]
        add_check(checks, f"{variant_id}_markdown_exists", md_path.exists(), path=str(md_path))
        add_check(checks, f"{variant_id}_docx_exists", docx_path.exists(), path=str(docx_path))
        if not md_path.exists() or not docx_path.exists():
            continue
        text = read_text(md_path)
        for token in spec["required"]:
            add_check(checks, f"{variant_id}_contains_{safe_name(token)}", token in text, token=token)
        for token in FORBIDDEN_MARKERS:
            add_check(checks, f"{variant_id}_excludes_{safe_name(token)}", token not in text, token=token)
        with zipfile.ZipFile(docx_path) as zf:
            xml = zf.read("word/document.xml").decode("utf-8")
        add_check(checks, f"{variant_id}_docx_readable", spec["required"][0] in xml)
        seen_hashes[variant_id] = sha256_file(md_path)

    add_check(
        checks,
        "variant_markdown_hashes_are_distinct",
        len(set(seen_hashes.values())) == len(EXPECTED_VARIANTS),
        hashes=seen_hashes,
    )

    manifest_by_id = {variant["id"]: variant for variant in manifest.get("variants", []) if "id" in variant}
    for variant_id, spec in EXPECTED_VARIANTS.items():
        manifest_row = manifest_by_id.get(variant_id, {})
        for key, file_name in (("markdown_sha256", spec["md"]), ("docx_sha256", spec["docx"])):
            path = artifacts / file_name
            if path.exists():
                actual = sha256_file(path)
                add_check(
                    checks,
                    f"{variant_id}_{key}_matches_manifest",
                    manifest_row.get(key) == actual,
                    expected=manifest_row.get(key),
                    actual=actual,
                )

    with zipfile.ZipFile(package_path) as zf:
        entries = sorted(zf.namelist())
        package_payload = "\n".join(entries)
        for entry in entries:
            if entry.endswith(".md") or entry.endswith(".json"):
                package_payload += "\n" + zf.read(entry).decode("utf-8")
    add_check(
        checks,
        "package_entries_exact",
        entries == EXPECTED_PACKAGE_ENTRIES,
        expected=EXPECTED_PACKAGE_ENTRIES,
        actual=entries,
    )
    for token in FORBIDDEN_MARKERS:
        add_check(checks, f"package_excludes_{safe_name(token)}", token not in package_payload, token=token)

    return build_report(root, checks, manifest_path, package_path)


def build_report(root: Path, checks: list[CheckResult], manifest_path: Path, package_path: Path) -> dict[str, Any]:
    failed = [check for check in checks if check.status != "PASS"]
    return {
        "schema_version": 1,
        "generated_at": "deterministic-local-paper-rag-review-variants-v1.0-verification",
        "root": str(root),
        "manifest": str(manifest_path),
        "package": str(package_path),
        "package_sha256": sha256_file(package_path) if package_path.exists() else None,
        "verdict": "PASS_LOCAL_PAPER_RAG_REVIEW_VARIANTS_V1_0_VERIFICATION" if not failed else "FAIL",
        "non_final_boundary": {
            "paper_quality_acceptance": False,
            "training_effect_acceptance": False,
            "production_ready": False,
            "broad_rag_ready": False,
            "runtime_authorization": False,
        },
        "checks": [check.__dict__ for check in checks],
        "summary": {"passed": len(checks) - len(failed), "failed": len(failed)},
    }


def write_outputs(report: dict[str, Any], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "local-paper-rag-review-variants-v1-0-verification.json"
    md_path = out_dir / "local-paper-rag-review-variants-v1-0-verification.md"
    json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = [
        "# Local Paper RAG Review Variants v1.0 Verification",
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
            "This verification proves packaging and review-variant integrity only. It does",
            "not grant paper-quality acceptance, training-effect acceptance, production",
            "readiness, broad RAG readiness, or RuntimeAuthorization.",
            "",
        ]
    )
    md_path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Verify local paper RAG review variants v1.0 artifacts.")
    parser.add_argument("--root", default=".", help="Repository root.")
    parser.add_argument(
        "--out-dir",
        default="integration/reports/local-paper-rag-review-variants-v1-0-verification",
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
