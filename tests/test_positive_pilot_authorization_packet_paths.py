from scripts.validate_positive_pilot_authorization_packet import (
    APPROVED_EVIDENCE_ROOT,
    is_under_approved_evidence_root,
)


def test_evidence_child_path_passes():
    assert is_under_approved_evidence_root(
        APPROVED_EVIDENCE_ROOT + r"\positive-pilot\report.json"
    )


def test_evidence_parent_traversal_fails():
    assert not is_under_approved_evidence_root(
        APPROVED_EVIDENCE_ROOT + r"\..\outside\report.json"
    )
