# Cowork plugin adapter — Stage-3 build (owed)

Target: a plugin (plugin.json + agents/ + skills/delegation-triage/) built FROM this repo's
core, replacing the interim `delegation-roster` plugin (a 2026-07-10 GPT-5.6-Pro repackaging of
the pre-package routing table — recorded as an unreconciled fork in `agents/MANIFEST.md`).

Requirements gathered from the fork's design + our review of it:
- Ship ROUTES/STATE/CONTRACT (the fork omitted STATE — its fable pins have no expiry; do NOT
  repeat that); WARRANTS may ship load-on-demand or by pointer.
- Include the `advisor` agent shape (fable-class checkpoint, no tools, bounded output) as the
  Cowork instrument for the R14 probe — but pin per STATE's scarcity mode, and prefer
  auditability (a subagent advisor is NOT the API advisor tool; it sees only the snapshot sent).
- Build = generated copy + manifest stamp; the plugin is a recorded deployment, never edited
  in place.
