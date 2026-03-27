#!/usr/bin/env python3
"""Profile and lightly clean structured WPS demand data.

This script does not make product decisions. It only:
- tags rows as valid / weak / invalid
- records conservative quality reasons
- flags exact duplicates
- emits cleaned CSVs and a summary markdown report
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path


DEFAULT_INPUT = "research/wps-project-management/synthesis/data/wps-demand-master.csv"
DEFAULT_OUTPUT_DIR = "research/wps-project-management/synthesis/data"
DEFAULT_SUMMARY = "research/wps-project-management/synthesis/demand-cleaning-summary.md"

KNOWN_INVALID_LITERALS = {
    "",
    "0",
    "1",
    "11",
    "111",
    "1111",
    "无",
    "暂无",
    "没有",
    "null",
    "NULL",
    "-",
    "--",
    "/",
}


def contains_chinese(text: str) -> bool:
    return re.search(r"[\u4e00-\u9fff]", text) is not None


def classify_quality(row: dict[str, str]) -> tuple[str, list[str]]:
    reasons: list[str] = []
    demand_text = (row.get("demand_text") or "").strip()
    level_1 = (row.get("level_1") or "").strip()
    level_2 = (row.get("level_2") or "").strip()

    if demand_text in KNOWN_INVALID_LITERALS:
        reasons.append("invalid_literal")
    if demand_text and re.fullmatch(r"[0-9]+", demand_text):
        reasons.append("digits_only")
    if not demand_text:
        reasons.append("empty_text")

    if level_1 in {"", "无"}:
        reasons.append("missing_level_1")
    if level_2 in {"", "无"}:
        reasons.append("missing_level_2")
    if demand_text and len(demand_text) <= 2:
        reasons.append("very_short_text")
    if demand_text and not contains_chinese(demand_text):
        reasons.append("no_chinese_text")

    invalid_markers = {"invalid_literal", "digits_only", "empty_text"}
    if any(reason in invalid_markers for reason in reasons):
        return "invalid", reasons

    weak_markers = {"missing_level_1", "missing_level_2", "very_short_text", "no_chinese_text"}
    if any(reason in weak_markers for reason in reasons):
        return "weak", reasons

    return "valid", reasons


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Clean and profile WPS demand CSV data.")
    parser.add_argument("--input", default=DEFAULT_INPUT, help="Input CSV path")
    parser.add_argument("--output-dir", default=DEFAULT_OUTPUT_DIR, help="Output data directory")
    parser.add_argument("--summary", default=DEFAULT_SUMMARY, help="Summary markdown path")
    return parser.parse_args(argv)


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    input_path = Path(args.input)
    output_dir = Path(args.output_dir)
    summary_path = Path(args.summary)

    if not input_path.exists():
        print(f"Missing input file: {input_path}", file=sys.stderr)
        return 1

    rows = read_rows(input_path)

    duplicate_counter = Counter()
    for row in rows:
        key = (
            (row.get("edition") or "").strip(),
            (row.get("demand_text") or "").strip(),
            (row.get("level_1") or "").strip(),
            (row.get("level_2") or "").strip(),
        )
        duplicate_counter[key] += 1

    profiled_rows: list[dict[str, str]] = []
    quality_counts = Counter()
    reason_counts = Counter()
    quality_by_edition = defaultdict(Counter)
    category_by_edition = defaultdict(Counter)

    for row in rows:
        edition = (row.get("edition") or "").strip()
        quality, reasons = classify_quality(row)
        duplicate_key = (
            (row.get("edition") or "").strip(),
            (row.get("demand_text") or "").strip(),
            (row.get("level_1") or "").strip(),
            (row.get("level_2") or "").strip(),
        )
        duplicate_count = duplicate_counter[duplicate_key]
        duplicate_flag = "yes" if duplicate_count > 1 else "no"

        enriched = dict(row)
        enriched["data_quality"] = quality
        enriched["quality_reasons"] = "|".join(reasons)
        enriched["exact_duplicate_flag"] = duplicate_flag
        enriched["exact_duplicate_count"] = str(duplicate_count)
        profiled_rows.append(enriched)

        quality_counts[quality] += 1
        quality_by_edition[edition][quality] += 1
        for reason in reasons:
            reason_counts[reason] += 1
        category_by_edition[edition][(row.get("level_1") or "").strip() or "(empty)"] += 1

    fieldnames = list(profiled_rows[0].keys()) if profiled_rows else []

    master_out = output_dir / "wps-demand-master-profiled.csv"
    personal_out = output_dir / "wps-demand-personal-profiled.csv"
    enterprise_out = output_dir / "wps-demand-enterprise-profiled.csv"
    valid_only_out = output_dir / "wps-demand-master-valid-only.csv"

    write_csv(master_out, fieldnames, profiled_rows)
    write_csv(personal_out, fieldnames, [row for row in profiled_rows if row.get("edition") == "personal"])
    write_csv(enterprise_out, fieldnames, [row for row in profiled_rows if row.get("edition") == "enterprise"])
    write_csv(valid_only_out, fieldnames, [row for row in profiled_rows if row.get("data_quality") == "valid"])

    summary_lines = [
        "# Demand Cleaning Summary",
        "",
        "## Overview",
        "",
        f"- Input file: `{input_path}`",
        f"- Total rows: {len(profiled_rows)}",
        f"- Valid rows: {quality_counts['valid']}",
        f"- Weak rows: {quality_counts['weak']}",
        f"- Invalid rows: {quality_counts['invalid']}",
        "",
        "## Quality by Edition",
        "",
        "| Edition | Valid | Weak | Invalid |",
        "| --- | --- | --- | --- |",
    ]

    for edition in sorted(quality_by_edition):
        summary_lines.append(
            f"| {edition} | {quality_by_edition[edition]['valid']} | {quality_by_edition[edition]['weak']} | {quality_by_edition[edition]['invalid']} |"
        )

    summary_lines.extend(
        [
            "",
            "## Top Quality Flags",
            "",
            "| Flag | Count |",
            "| --- | --- |",
        ]
    )
    for reason, count in reason_counts.most_common(12):
        summary_lines.append(f"| {reason} | {count} |")

    summary_lines.extend(
        [
            "",
            "## Top Level-1 Categories by Edition",
            "",
        ]
    )

    for edition in ("personal", "enterprise"):
        summary_lines.append(f"### {edition}")
        summary_lines.append("")
        summary_lines.append("| Level 1 | Count |")
        summary_lines.append("| --- | --- |")
        for category, count in category_by_edition[edition].most_common(12):
            summary_lines.append(f"| {category} | {count} |")
        summary_lines.append("")

    summary_lines.extend(
        [
            "## Outputs",
            "",
            f"- `{master_out}`",
            f"- `{personal_out}`",
            f"- `{enterprise_out}`",
            f"- `{valid_only_out}`",
            "",
            "## Notes",
            "",
            "- `invalid` means the row is very likely unusable without manual recovery.",
            "- `weak` means the row may still hold signal, but category or text quality is poor.",
            "- `valid-only` should not be treated as the final truth set; it is a convenience cut for faster analysis.",
        ]
    )

    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text("\n".join(summary_lines) + "\n", encoding="utf-8")

    print(f"Profiled {len(profiled_rows)} rows")
    print(f"Valid: {quality_counts['valid']}, Weak: {quality_counts['weak']}, Invalid: {quality_counts['invalid']}")
    print(f"Wrote summary: {summary_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
