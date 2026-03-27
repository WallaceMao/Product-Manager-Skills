#!/usr/bin/env python3
"""Convert WPS demand markdown tables into normalized CSV files.

This script is intentionally stdlib-only so it runs in a clean repo clone.

Input assumptions:
- Each source file contains a markdown pipe table.
- The first non-separator pipe row is treated as the header.
- Later pipe rows are treated as data rows.

Outputs:
- merged CSV with edition/source metadata
- per-edition CSV files
"""

from __future__ import annotations

import argparse
import csv
import os
import sys
from dataclasses import dataclass
from pathlib import Path


DEFAULT_PERSONAL = "research/wps-project-management/raw-input/WPS项目管理个人版需求聚类分析.md"
DEFAULT_ENTERPRISE = "research/wps-project-management/raw-input/WPS项目管理企业版需求聚类分析.md"
DEFAULT_OUTPUT_DIR = "research/wps-project-management/synthesis/data"


@dataclass
class Row:
    edition: str
    source_file: str
    row_id: str
    team_name: str
    demand_text: str
    level_1: str
    level_2: str


def is_separator_row(line: str) -> bool:
    stripped = line.strip()
    if not stripped.startswith("|"):
        return False
    content = stripped.replace("|", "").replace(":", "").replace("-", "").strip()
    return content == ""


def split_pipe_row(line: str) -> list[str]:
    stripped = line.strip()
    if not stripped.startswith("|"):
        return []
    parts = stripped.split("|")
    parts = parts[1:-1]
    return [part.strip() for part in parts]


def parse_markdown_table(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8") as handle:
        lines = handle.readlines()

    header: list[str] | None = None
    rows: list[dict[str, str]] = []

    for raw_line in lines:
        line = raw_line.rstrip("\n")
        if not line.strip().startswith("|"):
            continue
        if is_separator_row(line):
            continue

        cells = split_pipe_row(line)
        if not cells:
            continue

        if header is None:
            header = cells
            continue

        normalized = list(cells)
        if len(normalized) < len(header):
            normalized.extend([""] * (len(header) - len(normalized)))
        elif len(normalized) > len(header):
            normalized = normalized[: len(header)]

        row = {header[i]: normalized[i].strip() for i in range(len(header))}
        rows.append(row)

    if header is None:
        raise ValueError(f"No markdown table header found in {path}")

    return rows


def normalize_rows(rows: list[dict[str, str]], edition: str, source_file: str) -> list[Row]:
    normalized: list[Row] = []
    for index, row in enumerate(rows, start=1):
        normalized.append(
            Row(
                edition=edition,
                source_file=source_file,
                row_id=f"{edition}-{index:05d}",
                team_name=(row.get("团队名称") or "").strip(),
                demand_text=(row.get("需求描述") or "").strip(),
                level_1=(row.get("一级类目") or "").strip(),
                level_2=(row.get("二级类目") or "").strip(),
            )
        )
    return normalized


def write_csv(path: Path, rows: list[Row]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "edition",
                "source_file",
                "row_id",
                "team_name",
                "demand_text",
                "level_1",
                "level_2",
                "normalized_scenario",
                "user_role_guess",
                "problem_type",
                "request_type",
                "strategic_relevance",
                "decision_bucket",
                "data_quality",
                "notes",
            ]
        )
        for row in rows:
            writer.writerow(
                [
                    row.edition,
                    row.source_file,
                    row.row_id,
                    row.team_name,
                    row.demand_text,
                    row.level_1,
                    row.level_2,
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                ]
            )


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert WPS demand markdown tables into normalized CSV files."
    )
    parser.add_argument("--personal", default=DEFAULT_PERSONAL, help="Path to personal-edition markdown input")
    parser.add_argument(
        "--enterprise",
        default=DEFAULT_ENTERPRISE,
        help="Path to enterprise-edition markdown input",
    )
    parser.add_argument(
        "--output-dir",
        default=DEFAULT_OUTPUT_DIR,
        help="Directory where CSV outputs should be written",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])

    personal_path = Path(args.personal)
    enterprise_path = Path(args.enterprise)
    output_dir = Path(args.output_dir)

    if not personal_path.exists():
        print(f"Missing personal input: {personal_path}", file=sys.stderr)
        return 1
    if not enterprise_path.exists():
        print(f"Missing enterprise input: {enterprise_path}", file=sys.stderr)
        return 1

    personal_rows = normalize_rows(
        parse_markdown_table(personal_path),
        edition="personal",
        source_file=personal_path.name,
    )
    enterprise_rows = normalize_rows(
        parse_markdown_table(enterprise_path),
        edition="enterprise",
        source_file=enterprise_path.name,
    )

    merged = personal_rows + enterprise_rows

    write_csv(output_dir / "wps-demand-personal.csv", personal_rows)
    write_csv(output_dir / "wps-demand-enterprise.csv", enterprise_rows)
    write_csv(output_dir / "wps-demand-master.csv", merged)

    print(f"Wrote {len(personal_rows)} personal rows")
    print(f"Wrote {len(enterprise_rows)} enterprise rows")
    print(f"Wrote {len(merged)} total rows")
    print(f"Output directory: {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
