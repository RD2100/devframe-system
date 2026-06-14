"""Independent A120 ZIP evidence reviewer.

This script is intentionally read-only with respect to the evidence source. It
does not call the A120 packer, validator, test runner, or any runtime workflow.
It inspects ZIP metadata and selected entry bytes through Python's standard
library, then writes a reviewer-side JSON/Markdown report.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import zipfile
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


EXPECTED_ARTIFACT_ORDER = [
    "src/ai_workflow_hub/cli.py",
    "SCOPE_DECLARATION_A120.txt",
    "output/REGRESSION_OUTPUT_A120.txt",
    "output/IN_SCOPE_TEST_RESULTS_A120.txt",
    "known_flaky_tests.json",
    "manifest_metadata",
]

DEFAULT_PREFIX = "a120-evidence/"
DEFAULT_MAX_ENTRY_BYTES = 10 * 1024 * 1024
DEFAULT_MAX_TOTAL_BYTES = 50 * 1024 * 1024
VERDICT_START = 66
VERDICT_END = 119


@dataclass
class Check:
    check_id: str
    status: str
    message: str
    details: dict[str, Any] = field(default_factory=dict)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def read_text_entry(zf: zipfile.ZipFile, name: str) -> str:
    return zf.read(name).decode("utf-8", errors="replace")


def sorted_manifest_metadata_hash(manifest: dict[str, Any]) -> str:
    metadata = {key: value for key, value in manifest.items() if key != "evidence_bundle_hash"}
    payload = json.dumps(metadata, sort_keys=True).encode("utf-8")
    return sha256_bytes(payload)


def recompute_bundle_hash(zf: zipfile.ZipFile, prefix: str, manifest: dict[str, Any]) -> str:
    hashes = [
        sha256_bytes(zf.read(prefix + "src/ai_workflow_hub/cli.py")),
        sha256_bytes(zf.read(prefix + "SCOPE_DECLARATION_A120.txt")),
        sha256_bytes(zf.read(prefix + "output/REGRESSION_OUTPUT_A120.txt")),
        sha256_bytes(zf.read(prefix + "output/IN_SCOPE_TEST_RESULTS_A120.txt")),
        sha256_bytes(zf.read(prefix + "known_flaky_tests.json")),
        sorted_manifest_metadata_hash(manifest),
    ]
    return sha256_text("".join(hashes))


def add_check(checks: list[Check], check_id: str, status: str, message: str, **details: Any) -> None:
    checks.append(Check(check_id, status, message, details))


def has_unsafe_zip_name(name: str) -> bool:
    normalized = name.replace("\\", "/")
    parts = [part for part in normalized.split("/") if part]
    return (
        normalized.startswith("/")
        or normalized.startswith("\\")
        or normalized.startswith("//")
        or re.match(r"^[A-Za-z]:", normalized) is not None
        or any(part in {".", ".."} for part in parts)
    )


def load_json_file(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def build_required_entries(prefix: str) -> list[str]:
    required = [
        prefix + "COUNTS_MANIFEST_A120.json",
        prefix + "src/ai_workflow_hub/cli.py",
        prefix + "SCOPE_DECLARATION_A120.txt",
        prefix + "output/REGRESSION_OUTPUT_A120.txt",
        prefix + "output/IN_SCOPE_TEST_RESULTS_A120.txt",
        prefix + "known_flaky_tests.json",
        prefix + "output/VALIDATION_OUTPUT_A120.txt",
        prefix + "output/SELF_CONTAINMENT_OUTPUT_A120.txt",
    ]
    required.extend(
        prefix + f"context/CDP_VERDICT_A{number}.txt"
        for number in range(VERDICT_START, VERDICT_END + 1)
    )
    return required


def review(args: argparse.Namespace) -> tuple[dict[str, Any], int]:
    zip_path = Path(args.zip).resolve()
    manifest_path = Path(args.manifest).resolve()
    verdict_path = Path(args.verdict).resolve() if args.verdict else None
    prefix = args.prefix
    checks: list[Check] = []

    for label, path in (("zip", zip_path), ("manifest", manifest_path), ("verdict", verdict_path)):
        if path is None:
            continue
        if path.exists():
            add_check(checks, f"FILE-{label.upper()}", "PASS", f"{label} file exists", path=str(path))
        else:
            add_check(checks, f"FILE-{label.upper()}", "FAIL", f"{label} file is missing", path=str(path))

    if any(check.status == "FAIL" for check in checks):
        return make_report(args, checks, {}, None), 1

    external_manifest = load_json_file(manifest_path)

    with zipfile.ZipFile(zip_path, "r") as zf:
        infos = zf.infolist()
        names = [info.filename for info in infos]
        name_set = set(names)
        duplicates = sorted({name for name in names if names.count(name) > 1})
        unsafe = sorted(name for name in names if has_unsafe_zip_name(name))
        wrong_prefix = sorted(name for name in names if not name.startswith(prefix))
        total_uncompressed = sum(info.file_size for info in infos)
        max_entry = max((info.file_size for info in infos), default=0)
        required_entries = build_required_entries(prefix)
        missing_required = sorted(entry for entry in required_entries if entry not in name_set)

        add_check(
            checks,
            "ZIP-STRUCTURE",
            "PASS" if not duplicates and not unsafe and not wrong_prefix else "FAIL",
            "ZIP names are unique, relative, and under the expected prefix",
            entry_count=len(names),
            duplicate_entries=duplicates,
            unsafe_entries=unsafe,
            wrong_prefix_entries=wrong_prefix[:20],
            expected_prefix=prefix,
        )
        add_check(
            checks,
            "ZIP-SIZE",
            "PASS" if max_entry <= args.max_entry_bytes and total_uncompressed <= args.max_total_bytes else "FAIL",
            "ZIP uncompressed sizes are within configured reviewer limits",
            max_entry_bytes=max_entry,
            total_uncompressed_bytes=total_uncompressed,
            max_entry_limit=args.max_entry_bytes,
            total_limit=args.max_total_bytes,
        )
        add_check(
            checks,
            "ZIP-REQUIRED-ENTRIES",
            "PASS" if not missing_required else "FAIL",
            "Required A120 entries are present",
            missing_required=missing_required,
            required_count=len(required_entries),
        )

        zip_manifest = json.loads(read_text_entry(zf, prefix + "COUNTS_MANIFEST_A120.json"))
        add_check(
            checks,
            "MANIFEST-IDENTITY",
            "PASS" if zip_manifest == external_manifest else "FAIL",
            "External manifest matches manifest embedded in ZIP",
            external_manifest_sha256=sha256_bytes(manifest_path.read_bytes()),
            embedded_manifest_sha256=sha256_bytes(zf.read(prefix + "COUNTS_MANIFEST_A120.json")),
        )

        manifest = external_manifest
        required_fields = [
            "schema_version",
            "acceptance",
            "regression_command_hash",
            "regression_command_echo",
            "in_scope_command_hash",
            "in_scope_command_echo",
            "regression_transcript_sha256",
            "in_scope_transcript_sha256",
            "transcript_chain_hash",
            "total_test_files",
            "in_scope",
            "out_of_scope",
            "new_tests",
            "regression_passed",
            "in_scope_passed",
            "evidence_bundle_artifacts",
            "evidence_bundle_hash",
        ]
        missing_fields = [field for field in required_fields if field not in manifest]
        add_check(
            checks,
            "MANIFEST-REQUIRED-FIELDS",
            "PASS" if not missing_fields else "FAIL",
            "Manifest required fields are present",
            missing_fields=missing_fields,
        )
        add_check(
            checks,
            "MANIFEST-A120-SCHEMA",
            "PASS" if manifest.get("acceptance") == "A120" and str(manifest.get("schema_version")) == "1.61" else "FAIL",
            "Manifest identifies A120 with schema 1.61",
            acceptance=manifest.get("acceptance"),
            schema_version=manifest.get("schema_version"),
        )
        add_check(
            checks,
            "MANIFEST-ARTIFACT-ORDER",
            "PASS" if manifest.get("evidence_bundle_artifacts") == EXPECTED_ARTIFACT_ORDER else "FAIL",
            "Evidence bundle artifact order matches A120 contract",
            observed=manifest.get("evidence_bundle_artifacts"),
            expected=EXPECTED_ARTIFACT_ORDER,
        )

        regression_bytes = zf.read(prefix + "output/REGRESSION_OUTPUT_A120.txt")
        in_scope_bytes = zf.read(prefix + "output/IN_SCOPE_TEST_RESULTS_A120.txt")
        regression_sha = sha256_bytes(regression_bytes)
        in_scope_sha = sha256_bytes(in_scope_bytes)
        transcript_chain = sha256_text(regression_sha + in_scope_sha)
        add_check(
            checks,
            "TRANSCRIPT-HASHES",
            "PASS"
            if regression_sha == manifest.get("regression_transcript_sha256")
            and in_scope_sha == manifest.get("in_scope_transcript_sha256")
            and transcript_chain == manifest.get("transcript_chain_hash")
            else "FAIL",
            "Transcript hashes and chain hash match manifest",
            regression_sha256=regression_sha,
            in_scope_sha256=in_scope_sha,
            transcript_chain_hash=transcript_chain,
        )

        regression_command_hash = sha256_text(manifest.get("regression_command_echo", ""))
        in_scope_command_hash = sha256_text(manifest.get("in_scope_command_echo", ""))
        add_check(
            checks,
            "COMMAND-HASHES",
            "PASS"
            if regression_command_hash == manifest.get("regression_command_hash")
            and in_scope_command_hash == manifest.get("in_scope_command_hash")
            else "FAIL",
            "Command echo hashes match manifest",
            regression_command_hash=regression_command_hash,
            in_scope_command_hash=in_scope_command_hash,
        )

        bundle_hash = recompute_bundle_hash(zf, prefix, manifest)
        add_check(
            checks,
            "BUNDLE-HASH",
            "PASS" if bundle_hash == manifest.get("evidence_bundle_hash") else "FAIL",
            "Evidence bundle hash recomputes from ordered ZIP artifacts",
            recomputed=bundle_hash,
            manifest=manifest.get("evidence_bundle_hash"),
        )

        known_flaky = json.loads(read_text_entry(zf, prefix + "known_flaky_tests.json"))
        flaky_tests = known_flaky.get("tests", [])
        flaky_deselects = [item.get("deselect_arg", "") for item in flaky_tests]
        regression_command = manifest.get("regression_command_echo", "")
        missing_deselects = [item for item in flaky_deselects if item and item not in regression_command]
        total_known_flaky = known_flaky.get("total_known_flaky")
        add_check(
            checks,
            "KNOWN-FLAKY",
            "PASS" if total_known_flaky == len(flaky_tests) and not missing_deselects else "FAIL",
            "Known flaky metadata matches deselect command evidence",
            total_known_flaky=total_known_flaky,
            test_entries=len(flaky_tests),
            missing_deselects=missing_deselects,
        )

        test_files = [
            name
            for name in names
            if name.startswith(prefix + "tests/test_paper_a") and name.endswith(".py")
        ]
        add_check(
            checks,
            "TEST-INVENTORY",
            "PASS" if len(test_files) == manifest.get("total_test_files") else "FAIL",
            "ZIP test inventory count matches manifest",
            observed_count=len(test_files),
            manifest_total=manifest.get("total_test_files"),
        )

        missing_verdicts: list[str] = []
        bad_verdicts: list[str] = []
        for number in range(VERDICT_START, VERDICT_END + 1):
            entry = prefix + f"context/CDP_VERDICT_A{number}.txt"
            if entry not in name_set:
                missing_verdicts.append(entry)
                continue
            text = read_text_entry(zf, entry)
            verdict_text = text.upper()
            if not text.strip() or ("ACCEPTED" not in verdict_text and "REJECTED" not in verdict_text):
                bad_verdicts.append(entry)
        add_check(
            checks,
            "VERDICT-CHAIN",
            "PASS" if not missing_verdicts and not bad_verdicts else "FAIL",
            "A66-A119 verdict chain exists and contains verdict status tokens",
            expected_count=VERDICT_END - VERDICT_START + 1,
            missing_verdicts=missing_verdicts,
            bad_verdicts=bad_verdicts,
        )

        cli_text = read_text_entry(zf, prefix + "src/ai_workflow_hub/cli.py")
        missing_contract_comments = [
            f"A{number}" for number in range(96, 121) if f"A{number}" not in cli_text
        ]
        schema_match = '_AUDIT_SCHEMA_VERSION = "1.61"' in cli_text
        add_check(
            checks,
            "SOURCE-CONTRACT-CHECKS",
            "PASS" if schema_match and not missing_contract_comments else "FAIL",
            "cli.py contains schema 1.61 and A96-A120 contract markers",
            schema_match=schema_match,
            missing_contract_comments=missing_contract_comments,
        )

    verdict_summary = None
    if verdict_path:
        first_line = verdict_path.read_text(encoding="utf-8", errors="replace").splitlines()[0].strip()
        verdict_summary = {"first_line": first_line, "treated_as_final_acceptance": False}
        add_check(
            checks,
            "EXTERNAL-VERDICT-BOUNDARY",
            "PASS" if first_line == "ACCEPTED" else "WARN",
            "External A120 verdict is readable but is treated as input evidence, not final acceptance",
            first_line=first_line,
            final_acceptance=False,
        )

    report = make_report(
        args,
        checks,
        {
            "zip_sha256": sha256_bytes(zip_path.read_bytes()),
            "manifest_sha256": sha256_bytes(manifest_path.read_bytes()),
            "verdict_sha256": sha256_bytes(verdict_path.read_bytes()) if verdict_path else None,
        },
        verdict_summary,
    )
    return report, 1 if any(check.status == "FAIL" for check in checks) else 0


def make_report(
    args: argparse.Namespace,
    checks: list[Check],
    artifact_hashes: dict[str, Any],
    verdict_summary: dict[str, Any] | None,
) -> dict[str, Any]:
    counts = {
        "pass": sum(1 for check in checks if check.status == "PASS"),
        "warn": sum(1 for check in checks if check.status == "WARN"),
        "fail": sum(1 for check in checks if check.status == "FAIL"),
    }
    return {
        "schema_version": "1.0",
        "review_type": "A120EvidenceZipReviewReport",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "reviewer_boundary": {
            "read_only": True,
            "runs_pack_or_validate_scripts": False,
            "runs_tests_or_runtime": False,
            "claims_final_acceptance": False,
        },
        "inputs": {
            "zip": str(Path(args.zip).resolve()),
            "manifest": str(Path(args.manifest).resolve()),
            "verdict": str(Path(args.verdict).resolve()) if args.verdict else None,
            "prefix": args.prefix,
        },
        "artifact_hashes": artifact_hashes,
        "summary": counts,
        "status": "FAIL" if counts["fail"] else "PASS_WITH_BOUNDARY",
        "verdict_summary": verdict_summary,
        "checks": [
            {
                "id": check.check_id,
                "status": check.status,
                "message": check.message,
                "details": check.details,
            }
            for check in checks
        ],
    }


def write_reports(report: dict[str, Any], out_dir: Path) -> tuple[Path, Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "a120-evidence-zip-review.json"
    md_path = out_dir / "a120-evidence-zip-review.md"
    json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        "# A120 Evidence ZIP Review",
        "",
        f"Generated: {report['generated_at']}",
        f"Status: {report['status']}",
        "",
        "This report is an independent ZIP evidence review input. It is not a final acceptance verdict.",
        "",
        "## Inputs",
        "",
        f"- ZIP: `{report['inputs']['zip']}`",
        f"- Manifest: `{report['inputs']['manifest']}`",
        f"- Verdict: `{report['inputs']['verdict']}`",
        f"- Prefix: `{report['inputs']['prefix']}`",
        "",
        "## Summary",
        "",
        f"- PASS: {report['summary']['pass']}",
        f"- WARN: {report['summary']['warn']}",
        f"- FAIL: {report['summary']['fail']}",
        "",
        "## Checks",
        "",
    ]
    for check in report["checks"]:
        lines.append(f"- `{check['id']}` {check['status']}: {check['message']}")
    lines.append("")
    md_path.write_text("\n".join(lines), encoding="utf-8")
    return json_path, md_path


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Review A120 evidence ZIP without running its workflow.")
    parser.add_argument("--zip", default=r"D:\dev-frame-opencode\ai-workflow-hub\CDP_EVIDENCE_A120.zip")
    parser.add_argument("--manifest", default=r"D:\dev-frame-opencode\ai-workflow-hub\COUNTS_MANIFEST_A120.json")
    parser.add_argument("--verdict", default=r"D:\dev-frame-opencode\ai-workflow-hub\CDP_VERDICT_A120.txt")
    parser.add_argument("--prefix", default=DEFAULT_PREFIX)
    parser.add_argument("--out-dir", default=r"integration\reports\a120")
    parser.add_argument("--max-entry-bytes", type=int, default=DEFAULT_MAX_ENTRY_BYTES)
    parser.add_argument("--max-total-bytes", type=int, default=DEFAULT_MAX_TOTAL_BYTES)
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    report, exit_code = review(args)
    json_path, md_path = write_reports(report, Path(args.out_dir))
    print(f"[{report['status']}] A120 evidence ZIP review")
    print(f"[REPORT] {json_path}")
    print(f"[REPORT] {md_path}")
    print(
        "[BOUNDARY] This verifier did not run pack/validate scripts, tests, runtime, or final acceptance."
    )
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
