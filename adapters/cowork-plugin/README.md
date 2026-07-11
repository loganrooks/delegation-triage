# Cowork plugin adapter — generated build (Stage-3, built 2026-07-10)

Build: `python3 install.py cowork [--version X.Y.Z]` → `dist/delegation-roster-<version>.plugin`
(deterministic zip; `--check` byte-compares the artifact against canonical, `--dry-run` lists
contents). Install via the Cowork plugin UI, then stamp `agents/MANIFEST.md` with the printed
hash. The plugin is a recorded deployment, never edited in place — regenerate instead.

Contents: generated `plugin.json` + `SKILL.md` (from the `.template` files here, version +
source commit stamped in), canonical `agents/*.md` (incl. `advisor`, R15), and
ROUTES/CONTRACT/EPISTEMICS/WARRANTS as skill references.

**No volatile state ships in the artifact — by design** (operator direction 2026-07-10,
superseding this file's earlier "ship STATE" requirement): dates go stale inside a plugin that
can't be edited live; what ships is the *rule* — the skill's graceful-degradation step reads
the consuming project's STATE if one is readable, and otherwise treats premium availability as
Unchecked and takes the ROUTES Fallback column. Volatile facts stay project-side.

Replaces the interim `delegation-roster` 0.2.x plugin (a 2026-07-10 GPT-5.6-Pro repackaging of
the pre-package routing table — recorded as an unreconciled fork in `agents/MANIFEST.md`; its
`advisor` mint was adopted into the canonical roster, its explorer-light sonnet/high pin was
not). Version 0.3.0 continues that lineage name so the Cowork UI treats it as an upgrade.
