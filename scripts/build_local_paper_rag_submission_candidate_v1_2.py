from __future__ import annotations

import argparse
import hashlib
import json
import re
import zipfile
from pathlib import Path

from build_local_paper_rag_review_variants_v1_0 import write_docx, write_zip


VERSION = "v1.2"
MANUSCRIPT_MD = "local-paper-rag-submission-candidate-v1.2.md"
MANUSCRIPT_DOCX = "local-paper-rag-submission-candidate-v1.2.docx"
REFERENCE_CHECK = "local-paper-rag-reference-final-check-v1.2.md"
FORMAT_CLOSEOUT = "local-paper-rag-submission-format-closeout-v1.2.md"
MANIFEST_NAME = "local-paper-rag-submission-candidate-v1.2-manifest.json"
PACKAGE_NAME = "local-paper-rag-submission-candidate-v1.2-package.zip"
README_NAME = "SUBMISSION-CANDIDATE-V1.2-README.md"

REFERENCE_BLOCK = """## 参考文献

[1] 褚鑫杰. 关于利用虚拟现实技术建立“地震救援技术虚拟训练系统”的几点思考[J]. 中国应急救援, 2018(4): 12-15. DOI: 10.19384/j.cnki.cn11-5524/p.2018.04.003.

[2] 张云明, 陈蕾. 基于虚拟现实技术的灭火救援训练系统[J]. 消防科学与技术, 2010, 29(11): 996-998.

[3] 吴东瑾. 三维建模技术在灭火救援作战训练安全中的应用初探[J]. 今日消防, 2024(12): 46-48.

[4] 胡晓琴, 张朝伟, 焦晓丽. 虚拟训练系统在军事职业教育中的应用研究[J]. 产业与科技论坛, 2022, 21(9): 143-144.

[5] 焦楷哲, 程培源, 刘滔, 等. 国外军用虚拟训练系统研究[J]. 飞航导弹, 2013(6): 60-67. DOI: 10.16338/j.issn.1009-1319.2013.06.003.

[6] 沈裕喜. 虚拟训练系统的虚拟场景研究[D]. 国防科学技术大学, 2011.
"""


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


def build_manuscript(source: str) -> str:
    text = source.strip()
    text = re.sub(r"## 参考文献\n[\s\S]*$", REFERENCE_BLOCK.strip(), text)
    text = text.replace("；其中，虚拟场景构建决定了系统能否由展示性模型转向训练性环境。", "。其中，虚拟场景构建决定了系统能否由展示性模型转向训练性环境。")
    text = text.replace("本文的主要工作是：", "本文主要从三个方面展开：")
    return text.rstrip() + "\n"


def build_reference_check() -> str:
    return """# Reference Final Check v1.2

Status: `HUMAN_REFERENCE_METADATA_CHECK_REQUIRED`

This file is a submission-format checklist. It does not verify reference
metadata truth. The manuscript uses a GB/T-style candidate format, but final
venue compliance still requires human checking.

## Manual Checks Required

1. Confirm whether the target venue uses GB/T 7714-2015, GB/T 7714-2025, or a
   venue-specific variant.
2. Verify each author list, title, journal name, year, issue, volume, page
   range, DOI, and dissertation institution.
3. Confirm whether article numbers should be omitted, retained, or moved into
   notes for the target venue.
4. Confirm whether the four-author reference should use all authors or the
   first three authors plus `等`.
5. Confirm the dissertation location for reference [6]. Do not infer a city
   without checking the source.
6. Confirm that in-text citation order matches the final reference order after
   any human edits.

## Current Candidate Decisions

- Article numbers were removed from the manuscript candidate for cleaner
  GB/T-style presentation.
- DOI values already present in the source draft were retained.
- Reference [5] uses the first three authors plus `等`.
- Reference [6] keeps the institution and year without an inferred city.

## Boundary

This checklist does not grant final submission readiness, paper-quality
acceptance, training-effect acceptance, production readiness, broad/general RAG
readiness, whole-vault readiness, or RuntimeAuthorization.
"""


def build_format_closeout() -> str:
    return f"""# Submission Format Closeout v1.2

Status: `SUBMISSION_CANDIDATE_FORMATTED_NON_FINAL`

The v1.2 manuscript is a generic GB/T-style submission candidate derived from
the v1.1 short-paper human-review draft.

## What Changed From v1.1

- Preserved the short-paper route as the recommended formal-review path.
- Kept the title focused on auxiliary value, scenario construction, and
  evaluation boundary.
- Kept the cautious training-effect conclusion.
- Added a cleaner GB/T-style candidate reference block.
- Added a separate human reference metadata checklist.

## What This Does Not Prove

- It does not prove paper quality.
- It does not prove empirical training effect.
- It does not prove final target-venue compliance.
- It does not grant production readiness, broad/general RAG readiness,
  whole-vault readiness, cloud/vector DB readiness, or RuntimeAuthorization.

## Recommended Next Human Action

Open `local-paper-rag-submission-candidate-v1.2.docx`, check the title,
abstract, contribution paragraph, conclusion, and all six references. If a
target venue is known, apply that venue's exact template after the reference
metadata check.
"""


def package_readme() -> str:
    return f"""# Local Paper RAG Submission Candidate v1.2

This package contains a generic GB/T-style submission candidate for human
review. It is derived from the v1.1 short-paper draft.

Contents:

- `{MANUSCRIPT_MD}`
- `{MANUSCRIPT_DOCX}`
- `{REFERENCE_CHECK}`
- `{FORMAT_CLOSEOUT}`
- `{MANIFEST_NAME}`

Boundary: this package does not grant final paper-quality acceptance,
training-effect acceptance, final governance acceptance, production readiness,
broad/general RAG readiness, whole-vault readiness, cloud/vector DB readiness,
or RuntimeAuthorization.
"""


def build(root: Path) -> dict[str, object]:
    artifacts = root / "integration" / "artifacts" / "paper-drafts"
    artifacts.mkdir(parents=True, exist_ok=True)
    source_path = artifacts / "local-paper-rag-short-paper-v1.1.md"
    source = read_utf8(source_path)

    manuscript = build_manuscript(source)
    manuscript_md = artifacts / MANUSCRIPT_MD
    manuscript_docx = artifacts / MANUSCRIPT_DOCX
    reference_check = artifacts / REFERENCE_CHECK
    format_closeout = artifacts / FORMAT_CLOSEOUT
    manifest_path = artifacts / MANIFEST_NAME
    package_path = artifacts / PACKAGE_NAME

    write_utf8(manuscript_md, manuscript)
    write_docx(manuscript_docx, manuscript)
    write_utf8(reference_check, build_reference_check())
    write_utf8(format_closeout, build_format_closeout())

    manifest = {
        "schema_version": 1,
        "generated_at": "deterministic-local-paper-rag-submission-candidate-v1.2",
        "source": "local-paper-rag-short-paper-v1.1.md",
        "manuscript_markdown": MANUSCRIPT_MD,
        "manuscript_docx": MANUSCRIPT_DOCX,
        "reference_check": REFERENCE_CHECK,
        "format_closeout": FORMAT_CLOSEOUT,
        "recommended_use": "generic-gbt-style-human-review-candidate",
        "requires_human_reference_metadata_check": True,
        "requires_target_venue_template_check": True,
        "non_final_boundary": {
            "paper_quality_acceptance": False,
            "training_effect_acceptance": False,
            "final_governance_acceptance": False,
            "production_ready": False,
            "broad_rag_ready": False,
            "whole_vault_ready": False,
            "cloud_vector_db_ready": False,
            "runtime_authorization": False,
        },
        "hashes": {
            MANUSCRIPT_MD: sha256_file(manuscript_md),
            MANUSCRIPT_DOCX: sha256_file(manuscript_docx),
            REFERENCE_CHECK: sha256_file(reference_check),
            FORMAT_CLOSEOUT: sha256_file(format_closeout),
        },
    }
    write_utf8(manifest_path, json.dumps(manifest, indent=2, ensure_ascii=False))
    manifest["hashes"][MANIFEST_NAME] = sha256_file(manifest_path)

    entries: dict[str, str | bytes] = {
        README_NAME: package_readme(),
        MANIFEST_NAME: manifest_path.read_bytes(),
        MANUSCRIPT_MD: manuscript_md.read_bytes(),
        MANUSCRIPT_DOCX: manuscript_docx.read_bytes(),
        REFERENCE_CHECK: reference_check.read_bytes(),
        FORMAT_CLOSEOUT: format_closeout.read_bytes(),
    }
    write_zip(package_path, entries)
    package_hash = sha256_file(package_path)

    with zipfile.ZipFile(package_path) as zf:
        package_entries = sorted(zf.namelist())

    return {
        "package": str(package_path),
        "package_sha256": package_hash,
        "package_entries": package_entries,
        "manifest": str(manifest_path),
        "manuscript": str(manuscript_docx),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build local paper RAG submission candidate v1.2.")
    parser.add_argument("--root", default=".", help="Repository root.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    print(json.dumps(build(Path(args.root).resolve()), indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
