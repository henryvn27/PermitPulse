#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import sys
import urllib.parse
import urllib.request
from typing import Iterable


API_URL = "https://data.cityofchicago.org/resource/ydr8-5enu.json"
QUERY_LIMIT = 250

STRONG_ROOF_KEYWORDS = (
    "roof replacement",
    "reroof",
    "re-roof",
    "roofing.",
    "complete roof replacement",
)

EXCLUDE_KEYWORDS = (
    "rooftop deck",
    "pergola",
    "trellis",
    "garage roof height",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch Chicago roofing permits and format a PermitPulse digest."
    )
    parser.add_argument("--since", help="Start date in YYYY-MM-DD format.")
    parser.add_argument("--until", help="End date in YYYY-MM-DD format.")
    parser.add_argument("--limit", type=int, default=25, help="Maximum permits to return.")
    parser.add_argument(
        "--format",
        choices=("markdown", "csv", "json"),
        default="markdown",
        help="Output format.",
    )
    return parser.parse_args()


def default_dates(args: argparse.Namespace) -> tuple[str, str]:
    today = dt.date.today()
    since = args.since or (today - dt.timedelta(days=3)).isoformat()
    until = args.until or today.isoformat()
    return since, until


def build_where_clause(since: str, until: str) -> str:
    keyword_sql = " OR ".join(
        f"lower(work_description) like '%{keyword}%'" for keyword in STRONG_ROOF_KEYWORDS
    )
    exclude_sql = " AND ".join(
        f"lower(work_description) not like '%{keyword}%'" for keyword in EXCLUDE_KEYWORDS
    )
    return (
        f"issue_date between '{since}T00:00:00' and '{until}T23:59:59' "
        f"AND ({keyword_sql}) AND ({exclude_sql})"
    )


def fetch_rows(since: str, until: str, limit: int) -> list[dict[str, str]]:
    select = ",".join(
        [
            "permit_",
            "issue_date",
            "application_start_date",
            "street_number",
            "street_direction",
            "street_name",
            "work_description",
            "permit_type",
            "contact_1_type",
            "contact_1_name",
            "contact_1_city",
            "contact_2_type",
            "contact_2_name",
            "reported_cost",
        ]
    )
    params = {
        "$select": select,
        "$where": build_where_clause(since, until),
        "$order": "issue_date desc",
        "$limit": str(min(max(limit, 1), QUERY_LIMIT)),
    }
    url = f"{API_URL}?{urllib.parse.urlencode(params)}"
    request = urllib.request.Request(url, headers={"User-Agent": "PermitPulse/0.1"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def format_address(row: dict[str, str]) -> str:
    parts = [
        row.get("street_number", "").strip(),
        row.get("street_direction", "").strip(),
        row.get("street_name", "").strip(),
    ]
    return " ".join(part for part in parts if part)


def classify_record(row: dict[str, str]) -> str:
    description = row.get("work_description", "").lower()
    owner = row.get("contact_1_name", "").lower()
    if "llc" in owner or "roofing" in owner or "construction" in owner:
        return "Review manually"
    if "asphalt shingle" in description or "house only" in description:
        return "Strong residential lead"
    if "sq. ft." in description and "house only" not in description:
        return "Commercial or multifamily"
    return "Likely roofing lead"


def rows_for_output(rows: Iterable[dict[str, str]]) -> list[dict[str, str]]:
    output = []
    for row in rows:
        output.append(
            {
                "permit_number": row.get("permit_", ""),
                "issue_date": row.get("issue_date", "")[:10],
                "application_start_date": row.get("application_start_date", "")[:10],
                "address": format_address(row),
                "owner_type": row.get("contact_1_type", ""),
                "owner_name": row.get("contact_1_name", ""),
                "applicant_type": row.get("contact_2_type", ""),
                "applicant_name": row.get("contact_2_name", ""),
                "permit_type": row.get("permit_type", ""),
                "reported_cost": row.get("reported_cost", ""),
                "work_description": row.get("work_description", ""),
                "fit": classify_record(row),
            }
        )
    return output


def print_markdown(rows: list[dict[str, str]], since: str, until: str) -> None:
    print(f"# PermitPulse Chicago Roofing Digest")
    print()
    print(f"- Window: {since} to {until}")
    print(f"- Qualified permits: {len(rows)}")
    print()
    for index, row in enumerate(rows, start=1):
        print(f"## Lead {index}: {row['address']}")
        print(f"- Permit: `{row['permit_number']}`")
        print(f"- Issued: {row['issue_date']}")
        print(f"- Applied: {row['application_start_date'] or 'Unknown'}")
        print(f"- Owner: {row['owner_name']} ({row['owner_type']})")
        print(f"- Applicant: {row['applicant_name']} ({row['applicant_type']})")
        print(f"- Permit type: {row['permit_type']}")
        print(f"- Fit: {row['fit']}")
        if row["reported_cost"]:
            print(f"- Reported cost: ${row['reported_cost']}")
        print(f"- Work: {row['work_description']}")
        print()


def print_csv(rows: list[dict[str, str]]) -> None:
    fieldnames = list(rows[0].keys()) if rows else [
        "permit_number",
        "issue_date",
        "application_start_date",
        "address",
        "owner_type",
        "owner_name",
        "applicant_type",
        "applicant_name",
        "permit_type",
        "reported_cost",
        "work_description",
        "fit",
    ]
    writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
    writer.writeheader()
    for row in rows:
        writer.writerow(row)


def main() -> int:
    args = parse_args()
    since, until = default_dates(args)
    rows = rows_for_output(fetch_rows(since, until, args.limit))
    if args.format == "json":
        json.dump(rows, sys.stdout, indent=2)
        print()
        return 0
    if args.format == "csv":
        print_csv(rows)
        return 0
    print_markdown(rows, since, until)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
