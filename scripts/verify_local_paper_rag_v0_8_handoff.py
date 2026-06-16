from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import zipfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


EXPECTED_HASHES = {
    "docx": "8739E522CBA03A0D2F84BB89C92B3F3A6EACFF9C8C5C3F543A661FEACC11A637",
    "markdown": "BCCE83581CC398BFBC344FADB4ACD15C08B7A4CE977B72B94E92B358F75A8CA3",
    "package": "D8FBD5C203E7ACB9ABF412D09986E7B6AFFB34F3C3652CB62C63FF2AE647C742",
    "opencode_answer_preview_zip": "F1AB005DBE53429E825E2ACBF58750635744DE7D8A94F978878C9EEABA4F5FB9",
}

EXPECTED_PACKAGE_ENTRIES = [
    "ARTIFACTS-README.md",
    "CLOSEOUT-REPORT.md",
    "local-paper-rag-clean-manuscript-v0.8.docx",
    "local-paper-rag-clean-manuscript-v0.8.md",
]

EXPECTED_LOCKS = {
    "dev-frame-opencode": "528f5b801082a10759df000a2315486a55a22e79",
    "test-frame": "18c19898c599eca5452f2e10fcaa23f2d151339d",
    "agent-acceptance": "aa0fcd5844454f1ba69cfb62472da55d448feac8",
    "devframe-control-plane": "09167bc656f8625c97bfae5c52dae5a0280b116c",
}


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


def normalize_space(text: str) -> str:
    return " ".join(text.split())


def verify(root: Path) -> dict[str, Any]:
    artifacts = root / "integration" / "artifacts" / "paper-drafts"
    reports = root / "integration" / "reports"
    checks: list[CheckResult] = []

    paths = {
        "docx": artifacts / "local-paper-rag-clean-manuscript-v0.8.docx",
        "markdown": artifacts / "local-paper-rag-clean-manuscript-v0.8.md",
        "package": artifacts / "local-paper-rag-clean-manuscript-v0.8-package.zip",
        "readiness": reports / "parent-current-local-paper-rag-final-readiness-packet-v0-8-2026-06-16.md",
        "closeout": reports / "parent-local-paper-rag-clean-manuscript-v0-8-a1-2026-06-16.md",
        "baseline_lock": root / "BASELINE_LOCK.json",
        "opencode_answer_preview_zip": root
        / ".agent"
        / "evidence"
        / "evidence-opencode-local-paper-rag-answer-preview-a1-528f5b8.zip",
    }

    for label, path in paths.items():
        add_check(checks, f"{label}_exists", path.exists(), path=str(path))

    if not all(path.exists() for path in paths.values()):
        return build_report(root, checks, paths)

    for label in ("docx", "markdown", "package", "opencode_answer_preview_zip"):
        actual = sha256_file(paths[label])
        add_check(
            checks,
            f"{label}_sha256",
            actual == EXPECTED_HASHES[label],
            expected=EXPECTED_HASHES[label],
            actual=actual,
        )

    markdown = read_text(paths["markdown"])
    add_check(checks, "markdown_no_internal_source_markers", re.search(r"\[S\d+\]", markdown) is None)
    add_check(checks, "markdown_numeric_refs_1_to_6", all(f"[{idx}]" in markdown for idx in range(1, 7)))
    add_check(
        checks,
        "markdown_six_reference_entries",
        len(re.findall(r"^\[\d\]", markdown, flags=re.MULTILINE)) == 6,
    )
    add_check(checks, "markdown_no_status_block", "Status:" not in markdown)
    add_check(checks, "markdown_no_source_claim_matrix", "Source-Claim Matrix" not in markdown)
    add_check(checks, "markdown_doi_signals", "10.19384" in markdown and "10.16338" in markdown)
    add_check(checks, "markdown_handoff_boundary_signals", "RAG" in markdown and "Obsidian" in markdown)

    with zipfile.ZipFile(paths["docx"]) as zf:
        docx_xml = zf.read("word/document.xml").decode("utf-8")
    add_check(
        checks,
        "docx_openxml_readable",
        "10.19384" in docx_xml and "10.16338" in docx_xml,
    )

    with zipfile.ZipFile(paths["package"]) as zf:
        package_entries = sorted(zf.namelist())
    add_check(
        checks,
        "package_entries_exact",
        package_entries == EXPECTED_PACKAGE_ENTRIES,
        expected=EXPECTED_PACKAGE_ENTRIES,
        actual=package_entries,
    )

    readiness = read_text(paths["readiness"])
    for token in (
        "SHIP_V0_8_FOR_HUMAN_REVIEW_NON_FINAL",
        "local-paper-rag-clean-manuscript-v0.8.docx",
        EXPECTED_HASHES["docx"],
        EXPECTED_HASHES["markdown"],
        EXPECTED_HASHES["package"],
        "does not authorize new live resource access",
    ):
        add_check(checks, f"readiness_contains_{safe_name(token)}", token in readiness, token=token)

    closeout = normalize_space(read_text(paths["closeout"]))
    add_check(
        checks,
        "closeout_non_final_boundary",
        "not final paper-quality acceptance" in closeout
        and "not final citation acceptance" in closeout
        and "training-effect acceptance" in closeout
        and "not RuntimeAuthorization" in closeout,
    )

    lock_payload = json.loads(read_text(paths["baseline_lock"]))
    for module, expected_commit in EXPECTED_LOCKS.items():
        actual_commit = find_lock_commit(lock_payload, module)
        add_check(
            checks,
            f"baseline_lock_{safe_name(module)}",
            actual_commit == expected_commit,
            expected=expected_commit,
            actual=actual_commit,
        )

    return build_report(root, checks, paths)


def safe_name(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", value).strip("_").lower()[:72]


def find_lock_commit(payload: Any, module: str) -> str | None:
    if isinstance(payload, dict):
        if module in payload and isinstance(payload[module], str):
            return payload[module]
        if module in payload and isinstance(payload[module], dict):
            for key in ("commit", "locked_commit", "revision", "sha"):
                value = payload[module].get(key)
                if isinstance(value, str):
                    return value
        for value in payload.values():
            found = find_lock_commit(value, module)
            if found:
                return found
    if isinstance(payload, list):
        for item in payload:
            if isinstance(item, dict) and (
                item.get("name") == module or item.get("project_id") == module or item.get("path") == module
            ):
                for key in ("commit", "locked_commit", "revision", "sha"):
                    value = item.get(key)
                    if isinstance(value, str):
                        return value
            found = find_lock_commit(item, module)
            if found:
                return found
    return None


def build_report(root: Path, checks: list[CheckResult], paths: dict[str, Path]) -> dict[str, Any]:
    failed = [check for check in checks if check.status != "PASS"]
    return {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "root": str(root),
        "verdict": "PASS_LOCAL_PAPER_RAG_V0_8_HANDOFF_VERIFICATION" if not failed else "FAIL",
        "non_final_boundary": {
            "final_paper_quality_acceptance": False,
            "training_effect_acceptance": False,
            "production_ready": False,
            "broad_rag_ready": False,
            "runtime_authorization": False,
        },
        "paths": {key: str(path) for key, path in paths.items()},
        "checks": [check.__dict__ for check in checks],
        "summary": {
            "passed": len(checks) - len(failed),
            "failed": len(failed),
        },
    }


def write_outputs(report: dict[str, Any], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "local-paper-rag-v0-8-handoff-verification.json"
    md_path = out_dir / "local-paper-rag-v0-8-handoff-verification.md"
    json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = [
        "# Local Paper RAG v0.8 Handoff Verification",
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
    parser = argparse.ArgumentParser(description="Verify local paper RAG v0.8 handoff artifacts.")
    parser.add_argument("--root", default=".", help="Repository root. Defaults to current directory.")
    parser.add_argument(
        "--out-dir",
        default="integration/reports/local-paper-rag-v0-8-handoff-verification",
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
