from __future__ import annotations

import argparse
import hashlib
import json
import sys
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any


EXPECTED_PACKAGE_HASH = "8433B733FEEFE22D2EF48AD8C365D329C6900BDAC6BD2FCE9CBD532912DFB40F"

EXPECTED_PACKAGE_ENTRIES = [
    "SUBMISSION-PREP-README.md",
    "allowed-claims-v1.0.md",
    "gbt7714-preflight-v1.0.md",
    "local-paper-rag-clean-manuscript-v1.0.docx",
    "local-paper-rag-clean-manuscript-v1.0.md",
    "non-claim-boundary-v1.0.md",
    "reference-format-audit-v1.0.md",
    "references-needs-human-check-v1.0.md",
    "submission-decision-matrix-v1.0.md",
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


def verify(root: Path) -> dict[str, Any]:
    artifacts = root / "integration" / "artifacts" / "paper-drafts"
    package = artifacts / "local-paper-rag-submission-prep-v1.0-package.zip"
    gbt = artifacts / "gbt7714-preflight-v1.0.md"
    matrix = artifacts / "submission-decision-matrix-v1.0.md"
    checks: list[CheckResult] = []

    for path in (package, gbt, matrix):
        add_check(checks, f"{path.name}_exists", path.exists(), path=str(path))
    if not package.exists() or not gbt.exists() or not matrix.exists():
        return build_report(root, checks, package)

    actual_hash = sha256_file(package)
    add_check(
        checks,
        "submission_prep_package_sha256",
        actual_hash == EXPECTED_PACKAGE_HASH,
        expected=EXPECTED_PACKAGE_HASH,
        actual=actual_hash,
    )

    with zipfile.ZipFile(package) as zf:
        entries = sorted(zf.namelist())
        readme = zf.read("SUBMISSION-PREP-README.md").decode("utf-8")
    add_check(
        checks,
        "submission_prep_package_entries_exact",
        entries == EXPECTED_PACKAGE_ENTRIES,
        expected=EXPECTED_PACKAGE_ENTRIES,
        actual=entries,
    )

    gbt_text = gbt.read_text(encoding="utf-8")
    matrix_text = matrix.read_text(encoding="utf-8")
    add_check(checks, "gbt_preflight_records_done", "v1.0 已完成顺序编码制" in gbt_text)
    add_check(checks, "gbt_preflight_keeps_human_gate", "人工核对" in gbt_text and "不能替代" in gbt_text)
    add_check(checks, "decision_matrix_blocks_direct_journal_submit", "正式期刊投稿 | 暂不适合直接投" in matrix_text)
    add_check(checks, "decision_matrix_keeps_internal_brief_path", "内部研究简报" in matrix_text)
    add_check(checks, "package_readme_non_final_boundary", "not final journal formatting" in readme)

    return build_report(root, checks, package)


def build_report(root: Path, checks: list[CheckResult], package: Path) -> dict[str, Any]:
    failed = [check for check in checks if check.status != "PASS"]
    return {
        "schema_version": 1,
        "generated_at": "deterministic-local-paper-rag-submission-prep-v1.0-verification",
        "root": str(root),
        "package": str(package),
        "verdict": "PASS_LOCAL_PAPER_RAG_SUBMISSION_PREP_V1_0_VERIFICATION" if not failed else "FAIL",
        "non_final_boundary": {
            "final_journal_formatting": False,
            "final_citation_acceptance": False,
            "paper_quality_acceptance": False,
            "training_effect_acceptance": False,
            "runtime_authorization": False,
        },
        "checks": [check.__dict__ for check in checks],
        "summary": {"passed": len(checks) - len(failed), "failed": len(failed)},
    }


def write_outputs(report: dict[str, Any], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "local-paper-rag-submission-prep-v1-0-verification.json"
    md_path = out_dir / "local-paper-rag-submission-prep-v1-0-verification.md"
    json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = [
        "# Local Paper RAG Submission Prep v1.0 Verification",
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
            "This verification does not grant final journal formatting, final citation",
            "acceptance, paper-quality acceptance, training-effect acceptance, or",
            "RuntimeAuthorization.",
            "",
        ]
    )
    md_path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Verify local paper RAG submission-prep v1.0 artifacts.")
    parser.add_argument("--root", default=".", help="Repository root. Defaults to current directory.")
    parser.add_argument(
        "--out-dir",
        default="integration/reports/local-paper-rag-submission-prep-v1-0-verification",
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
