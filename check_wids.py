#!/usr/bin/env python3
"""check_wids.py — W-ID resolvability + internal-link + forbidden-path pass (P-D7 support).

Exit 1 if: (a) a W-ID cited anywhere in the package is not defined in WARRANTS.md, or a defined
W-record is cited nowhere (orphan → warning only); (b) a relative markdown link inside the
package points at a file that does not exist; (c) any package file contains an absolute
user-specific path or a SEAS-relative path used as a *dependency* (heuristic: outside the
KNOWN-REPOS key and STATE/probes provenance columns, flags `/Users/`, `~/Projects/`,
`~/Development/`). Plain stdlib; run from anywhere: `python3 check_wids.py [package_dir]`.
"""
import re
import sys
from pathlib import Path

WID_DEF_RE = re.compile(r"^### (W-\d{3}) ", re.MULTILINE)
WID_USE_RE = re.compile(r"\bW-\d{3}\b")
LINK_RE = re.compile(r"\]\((?!https?://|#|mailto:)([^)#]+)")
ABS_PATH_RE = re.compile(r"/Users/\w+|(?<![\w.])~/(?:Projects|Development)/")


def main(argv):
    pkg = Path(argv[1]).resolve() if len(argv) > 1 else Path(__file__).resolve().parent
    md_files = sorted(pkg.rglob("*.md"))
    warrants = pkg / "WARRANTS.md"
    failures, warnings = [], []

    defined = set(WID_DEF_RE.findall(warrants.read_text(encoding="utf-8"))) if warrants.is_file() else set()
    if not defined:
        failures.append("no W-records defined in WARRANTS.md")

    used = set()
    for f in md_files:
        text = f.read_text(encoding="utf-8")
        rel = f.relative_to(pkg)
        # Stage-2 validation 2026-07-10: archives + deployment stubs exempt
        if "references/ARCHIVE" in str(rel) or str(rel) == "references/routing-table.md":
            continue
        if f.name != "WARRANTS.md":
            used |= set(WID_USE_RE.findall(text))
        # relative links must resolve
        for target in LINK_RE.findall(text):
            target = target.strip()
            if not target or target.startswith("<"):
                continue
            if not (f.parent / target).exists():
                failures.append(f"{rel}: broken relative link -> {target}")
        # forbidden absolute/user paths (allow the marked env-hint column in WARRANTS' repo key)
        for n, line in enumerate(text.splitlines(), 1):
            if ABS_PATH_RE.search(line) and "local hint" not in line and "env-specific" not in line \
                    and not line.strip().startswith("| `"):
                failures.append(f"{rel}:{n}: absolute/user-specific path outside the locator key")

    for wid in sorted(used - defined):
        failures.append(f"cited but undefined W-ID: {wid}")
    for wid in sorted(defined - used):
        warnings.append(f"defined but never cited (orphan): {wid}")

    for f in failures:
        print(f"FAIL: {f}")
    for w in warnings:
        print(f"WARN: {w}")
    print(f"{len(md_files)} md files · {len(defined)} W-records defined · "
          f"{len(used)} cited: {'FAIL' if failures else 'OK'}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
