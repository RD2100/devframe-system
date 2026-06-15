"""Validate real-resource positive pilot authorization packets.

This verifier is local and read-only. It validates JSON packets against the
parent RuntimeAuthorization and TestRunSpec schemas, then applies governance
checks that JSON Schema cannot express across both contracts.

It never starts MiniApp, Zotero, WriteLab, browser/CDP, cloud, or any external
runtime.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

try:
    import jsonschema
except ImportError:  # pragma: no cover - exercised only in missing dependency envs
    jsonschema = None  # type: ignore[assignment]


REPO_ROOT = Path(__file__).resolve().parents[1]
RUNTIME_AUTH_SCHEMA = REPO_ROOT / "schemas" / "agent-runtime" / "runtime-authorization.schema.json"
TEST_RUN_SPEC_SCHEMA = REPO_ROOT / "schemas" / "agent-runtime" / "test-run-spec.schema.json"
APPROVED_EVIDENCE_ROOT = r"D:\devframe-system\.agent\evidence"

TRACKS = {
    "miniapp_real_e2e": {
        "runtime_type": "miniapp_real_e2e",
        "target_module": "test-frame",
    },
    "zotero_metadata_live": {
        "runtime_type": "zotero_live",
        "target_module": "dev-frame-opencode",
    },
    "writelab_live_boundary": {
        "runtime_type": "writelab_live",
        "target_module": "dev-frame-opencode",
    },
}

PLACEHOLDER_TOKENS = (
    "CHOOSE",
    "HUMAN_REQUIRED",
    "EXACT_COMMAND",
    "YYYY-",
    "...",
)


@dataclass
class Check:
    check_id: str
    status: str
    message: str
    details: dict[str, Any] = field(default_factory=dict)


def add_check(checks: list[Check], check_id: str, status: str, message: str, **details: Any) -> None:
    checks.append(Check(check_id, status, message, details))


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def load_schema(path: Path) -> dict[str, Any]:
    return load_json(path)


def validate_json_schema(instance: dict[str, Any], schema: dict[str, Any]) -> list[str]:
    if jsonschema is None:
        return ["jsonschema package is not installed"]
    validator = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())
    return [error.message for error in sorted(validator.iter_errors(instance), key=str)]


def contains_placeholder(value: Any) -> bool:
    if isinstance(value, str):
        return any(token in value for token in PLACEHOLDER_TOKENS)
    if isinstance(value, list):
        return any(contains_placeholder(item) for item in value)
    if isinstance(value, dict):
        return any(contains_placeholder(item) for item in value.values())
    return False


def has_wildcard_command(commands: Any) -> bool:
    if not isinstance(commands, list):
        return True
    for command in commands:
        if not isinstance(command, str):
            return True
        if "*" in command or "|" in command or contains_placeholder(command):
            return True
    return False


def is_under_approved_evidence_root(path_value: str) -> bool:
    normalized = path_value.replace("/", "\\").rstrip("\\")
    root = APPROVED_EVIDENCE_ROOT.rstrip("\\")
    return normalized == root or normalized.startswith(root + "\\")


def collect_true_final_acceptance_flags(value: Any, prefix: str = "$") -> list[str]:
    hits: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{prefix}.{key}"
            if key in {"final_acceptance", "final_acceptance_claimed"} and child is True:
                hits.append(child_path)
            hits.extend(collect_true_final_acceptance_flags(child, child_path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            hits.extend(collect_true_final_acceptance_flags(child, f"{prefix}[{index}]"))
    return hits


def parse_datetime(value: str) -> datetime | None:
    try:
        if value.endswith("Z"):
            value = value[:-1] + "+00:00"
        return datetime.fromisoformat(value)
    except ValueError:
        return None


def validate_packet(
    packet: dict[str, Any],
    runtime_auth_schema: dict[str, Any],
    test_run_spec_schema: dict[str, Any],
) -> dict[str, Any]:
    checks: list[Check] = []

    required_packet_fields = {
        "packet_id",
        "packet_mode",
        "selected_track",
        "runtime_authorization",
        "test_run_spec",
    }
    missing = sorted(required_packet_fields - set(packet))
    add_check(
        checks,
        "PACKET-REQUIRED-FIELDS",
        "PASS" if not missing else "FAIL",
        "packet has required wrapper fields",
        missing=missing,
    )

    packet_mode = packet.get("packet_mode")
    add_check(
        checks,
        "PACKET-MODE",
        "PASS" if packet_mode in {"synthetic_fixture", "real_authorization"} else "FAIL",
        "packet mode is explicit",
        packet_mode=packet_mode,
    )

    selected_track = packet.get("selected_track")
    has_selected_tracks_array = "selected_tracks" in packet
    add_check(
        checks,
        "SINGLE-TRACK",
        "PASS" if selected_track in TRACKS and not has_selected_tracks_array else "FAIL",
        "exactly one supported pilot track is selected",
        selected_track=selected_track,
        has_selected_tracks_array=has_selected_tracks_array,
        supported_tracks=sorted(TRACKS),
    )

    runtime_authorization = packet.get("runtime_authorization")
    test_run_spec = packet.get("test_run_spec")
    if not isinstance(runtime_authorization, dict):
        runtime_authorization = {}
    if not isinstance(test_run_spec, dict):
        test_run_spec = {}

    runtime_errors = validate_json_schema(runtime_authorization, runtime_auth_schema)
    add_check(
        checks,
        "RUNTIME-AUTH-SCHEMA",
        "PASS" if not runtime_errors else "FAIL",
        "RuntimeAuthorization validates against parent schema",
        errors=runtime_errors[:10],
    )

    spec_errors = validate_json_schema(test_run_spec, test_run_spec_schema)
    add_check(
        checks,
        "TEST-RUN-SPEC-SCHEMA",
        "PASS" if not spec_errors else "FAIL",
        "TestRunSpec validates against parent schema",
        errors=spec_errors[:10],
    )

    expected = TRACKS.get(str(selected_track), {})
    add_check(
        checks,
        "TRACK-RUNTIME-MATCH",
        "PASS"
        if runtime_authorization.get("runtime_type") == expected.get("runtime_type")
        and test_run_spec.get("target_module") == expected.get("target_module")
        else "FAIL",
        "selected track matches runtime type and target module",
        runtime_type=runtime_authorization.get("runtime_type"),
        target_module=test_run_spec.get("target_module"),
        expected=expected,
    )

    auth_id = runtime_authorization.get("authorization_id")
    spec_auth_id = test_run_spec.get("runtime_authorization_id")
    add_check(
        checks,
        "AUTH-ID-MATCH",
        "PASS" if auth_id and auth_id == spec_auth_id else "FAIL",
        "TestRunSpec references the RuntimeAuthorization id",
        authorization_id=auth_id,
        runtime_authorization_id=spec_auth_id,
    )

    add_check(
        checks,
        "REAL-POSITIVE-PILOT-SPEC",
        "PASS"
        if test_run_spec.get("test_profile") == "real_env_positive_pilot"
        and test_run_spec.get("runtime_allowed") is True
        and test_run_spec.get("blocked_by_env_policy") == "blocked_not_pass"
        else "FAIL",
        "real positive pilot spec is explicit and missing env cannot pass",
        test_profile=test_run_spec.get("test_profile"),
        runtime_allowed=test_run_spec.get("runtime_allowed"),
        blocked_by_env_policy=test_run_spec.get("blocked_by_env_policy"),
    )

    add_check(
        checks,
        "COMMAND-ALLOWLIST",
        "PASS" if not has_wildcard_command(runtime_authorization.get("allowed_commands")) else "FAIL",
        "allowed commands are exact and placeholder-free",
        allowed_commands=runtime_authorization.get("allowed_commands"),
    )

    paths = list(runtime_authorization.get("allowed_paths", []))
    evidence_path = runtime_authorization.get("evidence_output_path")
    artifact_path = test_run_spec.get("artifact_output_path")
    if evidence_path:
        paths.append(evidence_path)
    if artifact_path:
        paths.append(artifact_path)
    outside_paths = [path for path in paths if not isinstance(path, str) or not is_under_approved_evidence_root(path)]
    add_check(
        checks,
        "EVIDENCE-PATH-SCOPE",
        "PASS" if not outside_paths and bool(paths) else "FAIL",
        "all allowed and output paths stay under the approved evidence root",
        approved_root=APPROVED_EVIDENCE_ROOT,
        outside_paths=outside_paths,
    )

    add_check(
        checks,
        "REDACTION-BOUNDARY",
        "PASS" if runtime_authorization.get("redaction_required") is True else "FAIL",
        "real-resource positive pilot requires redaction",
        redaction_required=runtime_authorization.get("redaction_required"),
    )

    final_acceptance_hits = collect_true_final_acceptance_flags(packet)
    add_check(
        checks,
        "NO-FINAL-ACCEPTANCE",
        "PASS" if not final_acceptance_hits else "FAIL",
        "authorization packet cannot claim final acceptance",
        final_acceptance_hits=final_acceptance_hits,
    )

    authorized_at = runtime_authorization.get("authorized_at")
    expires_at = runtime_authorization.get("expires_at")
    parsed_authorized_at = parse_datetime(authorized_at) if isinstance(authorized_at, str) else None
    parsed_expires_at = parse_datetime(expires_at) if isinstance(expires_at, str) else None
    add_check(
        checks,
        "TIME-WINDOW",
        "PASS"
        if parsed_authorized_at is not None
        and parsed_expires_at is not None
        and parsed_expires_at > parsed_authorized_at
        else "FAIL",
        "authorization has a valid forward time window",
        authorized_at=authorized_at,
        expires_at=expires_at,
    )

    if packet_mode == "real_authorization":
        placeholder_fields = {
            "authorization_id": runtime_authorization.get("authorization_id"),
            "authorized_by": runtime_authorization.get("authorized_by"),
            "human_gate_reference": runtime_authorization.get("human_gate_reference"),
            "allowed_commands": runtime_authorization.get("allowed_commands"),
            "allowed_paths": runtime_authorization.get("allowed_paths"),
        }
        placeholders = sorted(
            field for field, value in placeholder_fields.items() if contains_placeholder(value)
        )
        add_check(
            checks,
            "REAL-AUTH-NO-PLACEHOLDERS",
            "PASS" if not placeholders else "FAIL",
            "real authorization packets must not contain placeholders",
            placeholder_fields=placeholders,
        )
    else:
        add_check(
            checks,
            "FIXTURE-NOT-AUTHORIZATION",
            "PASS",
            "synthetic fixtures are validation examples only, not runtime authorization",
            packet_mode=packet_mode,
        )

    counts = {
        "pass": sum(1 for check in checks if check.status == "PASS"),
        "fail": sum(1 for check in checks if check.status == "FAIL"),
    }
    return {
        "status": "FAIL" if counts["fail"] else "PASS",
        "summary": counts,
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


def validate_file(path: Path) -> dict[str, Any]:
    packet = load_json(path)
    runtime_auth_schema = load_schema(RUNTIME_AUTH_SCHEMA)
    test_run_spec_schema = load_schema(TEST_RUN_SPEC_SCHEMA)
    result = validate_packet(packet, runtime_auth_schema, test_run_spec_schema)
    expected = packet.get("expected_validation_status")
    expectation_met = expected in {None, result["status"]} if expected is not None else True
    result.update(
        {
            "packet_path": str(path),
            "packet_id": packet.get("packet_id"),
            "expected_validation_status": expected,
            "expectation_met": expectation_met,
        }
    )
    return result


def iter_fixture_paths(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    return sorted(child for child in path.glob("*.json") if child.is_file())


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate positive pilot RuntimeAuthorization/TestRunSpec packets."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--packet", help="Path to a single authorization packet JSON file.")
    group.add_argument("--fixtures", help="Directory containing packet fixture JSON files.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON output.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    target = Path(args.packet or args.fixtures).resolve()
    paths = iter_fixture_paths(target)
    if not paths:
        print(f"[FAIL] no packet JSON files found: {target}", file=sys.stderr)
        return 1

    results = [validate_file(path) for path in paths]
    failed = []
    for result in results:
        if result.get("expectation_met") is False:
            failed.append(result)
        elif result.get("expected_validation_status") is None and result["status"] == "FAIL":
            failed.append(result)
    output = {
        "schema_version": "1.0",
        "verifier": "positive_pilot_authorization_packet",
        "boundary": {
            "read_only": True,
            "runs_external_runtime": False,
            "claims_final_acceptance": False,
        },
        "packet_count": len(results),
        "failure_count": len(failed),
        "status": "FAIL" if failed else "PASS",
        "results": results,
    }
    if args.json:
        print(json.dumps(output, indent=2, ensure_ascii=False))
    else:
        print(f"[{output['status']}] positive pilot authorization packet validation")
        for result in results:
            expected = result.get("expected_validation_status")
            suffix = f" expected={expected}" if expected else ""
            print(
                f"- {result.get('packet_id')}: {result['status']}"
                f" checks={result['summary']}{suffix}"
            )
        print("[BOUNDARY] No external runtime was executed and no final acceptance is claimed.")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
