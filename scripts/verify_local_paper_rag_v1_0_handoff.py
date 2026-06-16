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


EXPECTED_HASHES = {
    "docx": "C92DDF4D53D4E6C16E101580C138626B3911B73959D362964395E259FAA399E8",
    "markdown": "E6AEB7B8CBF45D038EAB12DDCEA3ABB7FFB2F808E6CD0209665D0AEE31E5640C",
    "package": "88657D835CDEDAFFAF52943C9175F9D659AE2A61A09ED23BFBD147093138DCF4",
}

EXPECTED_PACKAGE_ENTRIES = [
    "ARTIFACTS-README.md",
    "CLOSEOUT-REPORT.md",
    "allowed-claims-v1.0.md",
    "local-paper-rag-clean-manuscript-v1.0.docx",
    "local-paper-rag-clean-manuscript-v1.0.md",
    "non-claim-boundary-v1.0.md",
    "reference-format-audit-v1.0.md",
    "references-needs-human-check-v1.0.md",
    "usage-profile-internal-brief-v1.0.md",
    "usage-profile-short-paper-v1.0.md",
    "usage-profile-technical-note-v1.0.md",
    "v1.0-verification-risk-checklist.md",
]

REQUIRED_TOKENS = [
    "辅助与增强手段",
    "而非真实训练和实装操作的替代方案",
    "本文不主张训练效果已经得到充分证明",
    "实验评价、过程数据和专家审阅",
]

FORBIDDEN_TOKENS = [
    "本地授权文献",
    "本地流程验证",
    "Source-Claim Matrix",
    "Status:",
    "[S1]",
    "[S2]",
    "[S3]",
    "[S4]",
    "[S5]",
    "[S6]",
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


def add_check(results: list[CheckResult], name: str, passed: bool, **details: Any) -> None:
    results.append(CheckResult(name=name, status="PASS" if passed else "FAIL", details=details))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def verify(root: Path) -> dict[str, Any]:
    artifacts = root / "integration" / "artifacts" / "paper-drafts"
    checks: list[CheckResult] = []
    paths = {
        "docx": artifacts / "local-paper-rag-clean-manuscript-v1.0.docx",
        "markdown": artifacts / "local-paper-rag-clean-manuscript-v1.0.md",
        "package": artifacts / "local-paper-rag-clean-manuscript-v1.0-package.zip",
        "reference_audit": artifacts / "reference-format-audit-v1.0.md",
        "reference_human_check": artifacts / "references-needs-human-check-v1.0.md",
        "allowed_claims": artifacts / "allowed-claims-v1.0.md",
        "non_claim_boundary": artifacts / "non-claim-boundary-v1.0.md",
        "verification_checklist": artifacts / "v1.0-verification-risk-checklist.md",
        "current_delivery": root / "CURRENT_DELIVERY.md",
    }

    for label, path in paths.items():
        add_check(checks, f"{label}_exists", path.exists(), path=str(path))
    if not all(path.exists() for path in paths.values()):
        return build_report(root, paths, checks)

    for label in ("docx", "markdown", "package"):
        actual = sha256_file(paths[label])
        add_check(
            checks,
            f"{label}_sha256",
            actual == EXPECTED_HASHES[label],
            expected=EXPECTED_HASHES[label],
            actual=actual,
        )

    markdown = read_text(paths["markdown"])
    for token in REQUIRED_TOKENS:
        add_check(checks, f"markdown_contains_{safe_name(token)}", token in markdown, token=token)
    for token in FORBIDDEN_TOKENS:
        add_check(checks, f"markdown_excludes_{safe_name(token)}", token not in markdown, token=token)

    reference_entries = re.findall(r"^\[\d\]", markdown, flags=re.MULTILINE)
    add_check(checks, "markdown_six_reference_entries", len(reference_entries) == 6, actual=len(reference_entries))
    add_check(
        checks,
        "markdown_no_repeated_bracket_citation_groups",
        re.search(r"\[[0-9,\-]+\](?:\[[0-9,\-]+\])+", markdown) is None,
    )
    add_check(checks, "markdown_sequential_reference_groups", "[1]" in markdown and "[2-3]" in markdown)

    with zipfile.ZipFile(paths["docx"]) as zf:
        docx_xml = zf.read("word/document.xml").decode("utf-8")
    add_check(checks, "docx_openxml_readable", "虚拟训练系统" in docx_xml and "参考文献" in docx_xml)

    with zipfile.ZipFile(paths["package"]) as zf:
        entries = sorted(zf.namelist())
    add_check(
        checks,
        "package_entries_exact",
        entries == EXPECTED_PACKAGE_ENTRIES,
        expected=EXPECTED_PACKAGE_ENTRIES,
        actual=entries,
    )

    delivery = read_text(paths["current_delivery"])
    for token in (
        "local-paper-rag-clean-manuscript-v1.0.docx",
        "SHIP_V1_0_FOR_HUMAN_REVIEW_NON_FINAL",
        EXPECTED_HASHES["docx"],
        EXPECTED_HASHES["markdown"],
        EXPECTED_HASHES["package"],
    ):
        add_check(checks, f"current_delivery_contains_{safe_name(token)}", token in delivery, token=token)

    return build_report(root, paths, checks)


def safe_name(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", value).strip("_").lower()[:72] or "token"


def build_report(root: Path, paths: dict[str, Path], checks: list[CheckResult]) -> dict[str, Any]:
    failed = [check for check in checks if check.status != "PASS"]
    return {
        "schema_version": 1,
        "generated_at": "deterministic-local-paper-rag-v1.0-handoff-verification",
        "root": str(root),
        "verdict": "PASS_LOCAL_PAPER_RAG_V1_0_HANDOFF_VERIFICATION" if not failed else "FAIL",
        "non_final_boundary": {
            "final_paper_quality_acceptance": False,
            "training_effect_acceptance": False,
            "production_ready": False,
            "broad_rag_ready": False,
            "runtime_authorization": False,
        },
        "paths": {key: str(path) for key, path in paths.items()},
        "checks": [check.__dict__ for check in checks],
        "summary": {"passed": len(checks) - len(failed), "failed": len(failed)},
    }


def write_outputs(report: dict[str, Any], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "local-paper-rag-v1-0-handoff-verification.json"
    md_path = out_dir / "local-paper-rag-v1-0-handoff-verification.md"
    json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = [
        "# Local Paper RAG v1.0 Handoff Verification",
        "",
        f"- Verdict: `{report['verdict']}`",
        f"- Passed checks: {report['summary']['passed']}",
        f"- Failed checks: {report['summary']['failed']}",
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
            "This verification is read-only. It does not inspect raw PDFs, raw Obsidian",
            "note bodies, raw chunks, vectors, FAISS binaries, WriteLab payloads, Zotero",
            "keys, browser/CDP/cloud/MiniApp runtimes, or private runtime artifacts.",
            "It does not grant paper-quality acceptance, training-effect acceptance,",
            "production readiness, broad RAG readiness, or RuntimeAuthorization.",
            "",
        ]
    )
    md_path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Verify local paper RAG v1.0 handoff artifacts.")
    parser.add_argument("--root", default=".", help="Repository root. Defaults to current directory.")
    parser.add_argument(
        "--out-dir",
        default="integration/reports/local-paper-rag-v1-0-handoff-verification",
        help="Directory for JSON and Markdown verification reports.",
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
