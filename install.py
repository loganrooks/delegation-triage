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
    # ~/.claude/delegation.md is @-imported by the user's global CLAUDE.md (highest-precedence
    # config surface): route values drifting there silently outvote ROUTES.md, so it deploys
    # from canonical and --check diffs it (operator authorization 2026-07-24).
    pairs.append((PKG / "adapters/claude-code/delegation.md", root / "delegation.md"))
    return pairs


def in_history(rel: str, digest: str) -> bool:
    """True if `digest` is the sha256 of this path at ANY commit — i.e. the deployed bytes
    were once canonical and the deployment is merely BEHIND."""
    try:
        revs = subprocess.run(["git", "-C", str(PKG), "rev-list", "--all"],
                              capture_output=True, text=True, check=True).stdout.split()
        for rev in revs:
            blob = subprocess.run(["git", "-C", str(PKG), "show", f"{rev}:{rel}"],
                                  capture_output=True, check=False)
            if blob.returncode == 0 and sha256(blob.stdout) == digest:
                return True
    except Exception:
        pass
    return False


def source_dirty(rel: str) -> bool:
    """True if the source file has uncommitted changes. Then 'not in history' CANNOT mean
    hand-edited: a deploy taken mid-edit puts never-committed—but genuinely canonical—bytes in
    the target. Asserting DIVERGED there would name a failure mode the evidence cannot
    distinguish (this fired against itself on 2026-07-24, one commit after the check was
    written). Undecidable is reported as DRIFT?, never as the accusation."""
    try:
        out = subprocess.run(["git", "-C", str(PKG), "status", "--porcelain", "--", rel],
                             capture_output=True, text=True, check=True).stdout.strip()
        return bool(out)
    except Exception:
        return True  # unknown git state ⇒ refuse to accuse


def extra_deployed(root: Path, pairs):
    """Deployed roster definitions the package does not own. --check is otherwise blind to
    these by construction: it only inspects files it would itself write (review D-3)."""
    owned = {dst.name for src, dst in pairs if dst.parent.name == "agents"}
    agents_dir = root / "agents"
    if not agents_dir.is_dir():
        return []
    return sorted(p for p in agents_dir.glob("*.md") if p.name not in owned)


def run_claude_code(args):
    root = Path(args.root).expanduser()
    pairs = claude_code_plan(root)
    if args.check or args.dry_run:
        counts = {"OK": 0, "BEHIND": 0, "DRIFT?": 0, "DIVERGED": 0, "MISSING": 0}
        for src, dst in pairs:
            if not dst.exists():
                state = "MISSING"
            elif sha256(dst.read_bytes()) == sha256(src.read_bytes()):
                state = "OK"
            else:
                rel = str(src.relative_to(PKG))
                if in_history(rel, sha256(dst.read_bytes())):
                    state = "BEHIND"
                elif source_dirty(rel):
                    state = "DRIFT?"     # undecidable: dirty source, direction unknowable
                else:
                    state = "DIVERGED"   # clean source + bytes never in history ⇒ hand-edited
            counts[state] += 1
            print(f"{state:9} {dst}")
        extras = extra_deployed(root, pairs)
        for p in extras:
            print(f"{'EXTRA':9} {p}")
        verb = "would deploy" if args.dry_run else "checked"
        print(f"\n{verb} {len(pairs)} files: "
              + " · ".join(f"{k.lower()} {v}" for k, v in counts.items())
              + f" · extra {len(extras)}")
        if counts["DIVERGED"]:
            print("DIVERGED = clean source, yet deployed bytes never existed in this repo "
                  "(hand-edited). Reconcile deliberately; a plain re-deploy DISCARDS them.")
        if counts["DRIFT?"]:
            print("DRIFT?   = source file is dirty, so 'never in history' proves nothing — the "
                  "deployed copy may be an earlier uncommitted canonical state. Direction is "
                  "UNDECIDABLE until the source is committed; not an accusation.")
        if extras:
            print("EXTRA = deployed roster definitions the package does not own "
                  "(not stamped in agents/MANIFEST.md; a re-deploy will NOT remove them).")
        # exit 1 only on genuine divergence: lag is normal for a package that appends
        # evidence continuously and deploys occasionally.
        return 1 if (args.check and counts["DIVERGED"]) else 0
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
