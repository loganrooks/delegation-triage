# LINEAGE — where this repo comes from, and what stays behind

**Minted:** 2026-07-10, Stage-2 execution of SEAS ADR-0022 (operator A4 GO + same-day home
decision; amending record: SEAS ADR-0024). Canonical home for the `delegation-triage` package:
routing doctrine (ROUTES/STATE/WARRANTS/CONTRACT/EPISTEMICS), roster (`agents/`), evidence loop
(`probes/`), checks (`check_state.py`, `check_wids.py`).

**Descends from (both ends annotated):**
- SEAS `SelfEvolvingAgentialSystems` — the programme that designed and ratified this package
  (proposal `proposals/2026-07-10-delegation-triage-offshoot.md`; ADR-0022/0024; Stage-1 run
  `research/2026-07-10-delegation-triage-stage1/`, whose `package/` copy is FROZEN as the
  Stage-1 audit artifact — see its MOVED-TO stub). The epistemics vocabulary descends from SEAS
  `governance/epistemics.md`.
- The `~/.claude/skills/delegation-triage/` living routing table (seeded 2026-07-02) and SEAS
  `harness/agents/TRIAGE.md` (2026-06-12) — the two drifted homes this package reunifies; the
  old table is archived (not deleted) at the `~/.claude` deployment.

**Relationship going forward (the §4 graduation model):** this repo is its own selection
environment — new routing evidence accumulates in `probes/` here; SEAS keeps the genealogy and
receives feedback, not control. Deployments (`~/.claude`, the Cowork plugin, any Codex consumer)
are recorded copies stamped in `agents/MANIFEST.md`; drift is diffable, never
discoverable-by-accident.

## adapters/ (platform packaging — core stays platform-agnostic)

| adapter | target | status |
|---|---|---|
| `adapters/claude-code/` | skill + agents + guard hook install into `~/.claude` | Stage-2: documented manual install (INSTALL.md) |
| `adapters/cowork-plugin/` | plugin build (plugin.json + agents/ + skills/) — replaces the 2026-07-10 GPT-5.6-Pro fork as the Cowork surface | Stage-3: build owed; requirements noted |
| `adapters/codex/` | consumer guidance ("read ROUTES/STATE before delegating to Claude") | Stage-3: note owed |
