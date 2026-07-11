#!/usr/bin/env python3
"""install.py — deploy the delegation-triage package to a consumer surface.

Targets:
  claude-code   copy knowledge surfaces + checks + probes/ into the skill home and roster
                definitions into the agents dir (default root: ~/.claude). Restart required —
                roster registers at session START.
  cowork        build a plugin zip (dist/delegation-roster-<version>.plugin) from canonical.
                Ships NO volatile state by design: degradation is a rule the skill carries,
                not dates in the artifact (operator direction 2026-07-10). Install via the
                Cowork plugin UI, then stamp agents/MANIFEST.md.
  codex         emit the consumer guidance fragment (AGENTS.md-style), package path resolved.

Every deploy is a recorded deployment: this script prints the sha256 table to paste into
agents/MANIFEST.md — it does not edit the manifest (curated by hand, by design).

Usage:
  python3 install.py claude-code [--root ~/.claude] [--check | --dry-run]
  python3 install.py cowork      [--version 0.3.0] [--check | --dry-run]
  python3 install.py codex       [--dest PATH]     (no --dest: prints to stdout)

Plain stdlib. Zips are deterministic (fixed timestamps), so --check byte-compares honestly.
"""
import argparse
import hashlib
import io
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

PKG = Path(__file__).resolve().parent
SKILL_FILES = ["SKILL.md", "ROUTES.md", "STATE.md", "WARRANTS.md", "CONTRACT.md",
               "EPISTEMICS.md", "check_state.py", "check_wids.py"]
PLUGIN_NAME = "delegation-roster"
PLUGIN_VERSION_DEFAULT = "0.3.0"
PLUGIN_REFERENCES = ["ROUTES.md", "CONTRACT.md", "EPISTEMICS.md", "WARRANTS.md"]  # no STATE: by design
ZIP_DATE = (2026, 1, 1, 0, 0, 0)  # fixed → deterministic archive → --check is byte-honest


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def agent_files():
    return sorted(p for p in (PKG / "agents").glob("*.md") if p.name != "MANIFEST.md")


def probe_files():
    return sorted(p for p in (PKG / "probes").rglob("*") if p.is_file())


def head_commit():
    try:
        return subprocess.run(["git", "-C", str(PKG), "rev-parse", "--short", "HEAD"],
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "UNKNOWN"


def claude_code_plan(root: Path):
    """(source, destination) pairs for the claude-code target."""
    skill_home = root / "skills" / "delegation-triage"
    pairs = [(PKG / f, skill_home / f) for f in SKILL_FILES]
    pairs += [(p, skill_home / p.relative_to(PKG)) for p in probe_files()]
    pairs += [(p, root / "agents" / p.name) for p in agent_files()]
    return pairs


def run_claude_code(args):
    pairs = claude_code_plan(Path(args.root).expanduser())
    if args.check or args.dry_run:
        drift = 0
        for src, dst in pairs:
            state = ("MISSING" if not dst.exists()
                     else "OK" if sha256(dst.read_bytes()) == sha256(src.read_bytes())
                     else "DRIFT")
            drift += state != "OK"
            print(f"{state:8} {dst}")
        verb = "would deploy" if args.dry_run else "checked"
        print(f"{verb} {len(pairs)} files: {drift} not current")
        return 1 if (args.check and drift) else 0
    for src, dst in pairs:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
    print(f"deployed {len(pairs)} files under {args.root}")
    print("\nMANIFEST stamp (agents/ rows) — paste-ready:")
    for p in agent_files():
        print(f"  {p.name}: {sha256(p.read_bytes())}")
    print(f"\nsource commit: {head_commit()}")
    print("NOW: stamp agents/MANIFEST.md, then RESTART the session (roster registers at START).")
    return 0


def render(template: Path, subs: dict) -> str:
    text = template.read_text(encoding="utf-8")
    for key, value in subs.items():
        text = text.replace("{{" + key + "}}", value)
    return text


def build_plugin_bytes(version: str) -> bytes:
    subs = {"VERSION": version, "COMMIT": head_commit()}
    entries = [(".claude-plugin/plugin.json",
                render(PKG / "adapters/cowork-plugin/plugin.json.template", subs).encode())]
    entries += [(f"agents/{p.name}", p.read_bytes()) for p in agent_files()]
    entries.append(("skills/delegation-triage/SKILL.md",
                    render(PKG / "adapters/cowork-plugin/SKILL.template", subs).encode()))
    entries += [(f"skills/delegation-triage/references/{f}", (PKG / f).read_bytes())
                for f in PLUGIN_REFERENCES]
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        for name, data in entries:
            zf.writestr(zipfile.ZipInfo(name, date_time=ZIP_DATE), data)
    return buf.getvalue()


def run_cowork(args):
    out = PKG / "dist" / f"{PLUGIN_NAME}-{args.version}.plugin"
    data = build_plugin_bytes(args.version)
    if args.dry_run:
        with zipfile.ZipFile(io.BytesIO(data)) as zf:
            for name in zf.namelist():
                print(f"would pack {name}")
        print(f"would write {out} ({len(data)} bytes, sha256 {sha256(data)[:16]}…)")
        return 0
    if args.check:
        if not out.exists():
            print(f"FAIL: {out} not built yet")
            return 1
        ok = sha256(out.read_bytes()) == sha256(data)
        print(f"{'OK: artifact matches canonical' if ok else 'DRIFT: rebuild needed'} ({out.name})")
        return 0 if ok else 1
    out.parent.mkdir(exist_ok=True)
    out.write_bytes(data)
    print(f"built {out}\nsha256 {sha256(data)}\nsource commit {head_commit()}")
    print("NOW: install via the Cowork plugin UI (replaces the fork lineage), "
          "then stamp agents/MANIFEST.md with this hash.")
    return 0


def run_codex(args):
    text = render(PKG / "adapters/codex/AGENTS-fragment.template", {"PACKAGE_HOME": str(PKG)})
    if args.dest:
        dest = Path(args.dest).expanduser()
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(text, encoding="utf-8")
        print(f"wrote {dest}")
    else:
        print(text)
    return 0


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="target", required=True)
    cc = sub.add_parser("claude-code")
    cc.add_argument("--root", default="~/.claude")
    cw = sub.add_parser("cowork")
    cw.add_argument("--version", default=PLUGIN_VERSION_DEFAULT)
    cx = sub.add_parser("codex")
    cx.add_argument("--dest")
    for p in (cc, cw):
        p.add_argument("--check", action="store_true")
        p.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv[1:])
    return {"claude-code": run_claude_code, "cowork": run_cowork, "codex": run_codex}[args.target](args)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
