# Flash-pilot fixtures (pilot §5 F-7 — authored before first run, D-FP ratified 2026-07-27)

Per-lane intent/outcome JSON templates for the v2 writer
(`delegation-runtime:intent-writer/scripts/intent_writer.py`). Copy, fill `<>` slots, write
via `write_record` / `--json`. Rules that bite:

- `route_id` = the LANE id (FP-A / FP-B / FP-C-loopback / FP-C-native / FP-0d) — legal
  under crosswalk v0.2.2 registered-CANDIDATE lanes.
- `router_model` / `router_effort`: READ from driver transcript or $CLAUDE_EFFORT
  (pilot §5 rider 2) — never assumed.
- `requested_model.raw` = what you typed (`flash`); `.id` = the alias resolution
  (`google:gemini-3.6-flash-high`, per ~/.delegation/v2/model-aliases.json).
- Loopback legs until FP-0a is read off the wire: `requested_effort: "unknown"` is legal.
- Empty/non-delivering leg -> `disposition: "error"` (FP-0b), `observed_model: null` legal
  there. NEVER `accepted`.
- Severe failures: REGISTERED codes in `friction_codes` (fabricated-completion /
  silent-scope-violation / undetected-omission).
- Fault attribution + detection timing live in the PROBE RECORD (adjudicator-filled,
  D-C5-1) — no outcome field exists for them; do not invent one (fail-closed writer).
- `run_id` = probe_id (machine-join).
