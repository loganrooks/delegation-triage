# Agent entry point (all harnesses)

Boot order for any session working in this repo:

1. [PROGRAMME.md](PROGRAMME.md) — ratified direction and pace rules (§1 is the priority
   order; re-read after compaction/resume and before lane-affecting changes).
2. [LANES.md](LANES.md) — current fast state.
3. [CLAUDE.md](CLAUDE.md) — repo architecture, commands, editing discipline (harness-
   neutral despite the filename).
4. [ROUTES.md](ROUTES.md) + [STATE.md](STATE.md) — every-spawn routing surfaces (an
   expired STATE entry reads as Unchecked, never as true).

Run `python3 check_state.py` and `python3 check_wids.py` before committing any Markdown
edit. Probe records need `attestation:` and `tally:` ([probes/TEMPLATE.md](probes/TEMPLATE.md)).
