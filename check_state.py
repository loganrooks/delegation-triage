#!/usr/bin/env python3
"""check_state.py — deterministic expiry check for STATE.md (D3 / P-D5).

Exit 1 if any dated `valid_until` entry has expired (expired state = Unchecked, never true).
Plain stdlib; runnable from any session's shell, including Cowork sandboxes.

Usage:
    python3 check_state.py [path/to/STATE.md] [--today YYYY-MM-DD]

Rules:
  - Parses ONLY the state table: rows between the header line starting `| key | value |
    valid_until` and the next non-table line (review lens 2 F8 — a second table or an inserted
    column must not silently shift the check). The `valid_until` column is located BY HEADER
    NAME, not by position.
  - A valid_until cell with no YYYY-MM-DD date (e.g. config rows marked em-dash) is exempt.
  - An entry expiring TODAY is still valid through end of day.
  - Also fails if the BOLD `**Active: <profile>**` line is missing or unbolded — the deployed
    spawn-triage-guard parses exactly that format and silently defaults otherwise (lens 2 F2).
"""
import re
import sys
from datetime import date
from pathlib import Path

DATE_RE = re.compile(r"(\d{4})-(\d{2})-(\d{2})")


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    state_path = Path(args[0]) if args else Path(__file__).resolve().parent / "STATE.md"
    today = date.today()
    for i, a in enumerate(argv):
        if a == "--today" and i + 1 < len(argv):
            y, m, d = DATE_RE.match(argv[i + 1]).groups()
            today = date(int(y), int(m), int(d))

    if not state_path.is_file():
        print(f"FAIL: STATE file not found: {state_path}")
        return 1
    text = state_path.read_text(encoding="utf-8")

    failures, checked, exempt = [], 0, 0

    if not re.search(r"^\*\*Active:\s*[\w-]+\*\*", text, re.MULTILINE):
        failures.append("missing or unbolded `**Active: <profile>**` line — the deployed guard "
                        "hook parses exactly `**Active: ...**` and silently defaults otherwise")

    # Locate the state table by its header; read only its rows; find valid_until by name.
    in_table, vu_idx = False, None
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            in_table, vu_idx = False, None
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        headers = [c.lower().strip("*` ") for c in cells]
        if not in_table:
            if "key" in headers and "valid_until" in headers:
                in_table, vu_idx = True, headers.index("valid_until")
            continue
        if set(cells[0]) <= {"-", " "} or len(cells) <= vu_idx:
            continue
        key, valid_until = cells[0], cells[vu_idx]
        m = DATE_RE.search(valid_until)
        if not m:
            exempt += 1
            continue
        checked += 1
        y, mo, d = (int(g) for g in m.groups())
        if date(y, mo, d) < today:
            failures.append(f"EXPIRED: `{key}` (valid_until {y:04d}-{mo:02d}-{d:02d} < {today}) "
                            f"— treat as Unchecked; re-verify or route on the fallback column")

    if checked + exempt == 0:
        failures.append("no state table found (header `| key | value | valid_until ... |`)")

    for f in failures:
        print(f"FAIL: {f}")
    print(f"checked {checked} dated entries, {exempt} exempt (no date), as of {today}: "
          f"{'FAIL' if failures else 'OK'}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
