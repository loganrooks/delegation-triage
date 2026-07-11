# Contributing

This repo is a live routing instrument with an evidence discipline. PRs are welcome, but the
bar is evidential, not stylistic — the surfaces encode measured outcomes, and edits that break
the discipline will be declined even when they read better.

## The rules the checks enforce (CI runs both on every push/PR)

- `python3 check_state.py` — any `STATE.md` entry past its `valid_until` **fails the build**
  (expired state is Unchecked, never true). The bold `**Active: <profile>**` line is a parsed
  format contract; keep it bold, keep exactly one.
- `python3 check_wids.py` — every cited `W-ID` must resolve to a `### W-NNN` record in
  `WARRANTS.md`; every relative link must resolve; no user-specific absolute paths outside the
  marked locator-hint columns.

## The rules the checks can't enforce

- **Route changes need evidence, not arguments.** A ROUTES row flips only on ≥2 attested
  concordant probe outcomes (n=1 never flips a row; flip-prone classes accumulate ~3 per side).
  Propose a probe, not a rewrite: paired configs, identical harness, diff the yield, record it
  in `probes/records/` (template: `probes/TEMPLATE.md`; only `attestation:` and `tally:` are
  required).
- **Same-pass propagation.** A post-mortem or probe outcome edits the affected surface (ROUTES
  row, W-record grade/flip counter, STATE entry) AND appends the probe record AND updates
  `probes/INDEX.md` in one pass. No surface may silently lag the records.
- **Warrant records** carry: claim · label + grade + downgrade reasoning (see
  `EPISTEMICS.md` — a vendor number is Concordant/Reported, never Corroborated) · resolvable
  locators with quoted primary excerpts · a flip condition. A record without a flip condition
  is a guess and must say so. Supersede in place.
- **Roster changes are supersessions:** edit the canonical definition in `agents/`, re-hash,
  stamp `agents/MANIFEST.md`, and record basis + disconfirmer in the row.

## Scope notes

- `probes/` is an append-only lab notebook — don't retrofit or "clean up" existing records
  (grandfathered prose is grandfathered deliberately).
- Some evidence locators point at private repos; the quoted excerpts in `WARRANTS.md` exist so
  records stay evaluable without them. Don't strip the excerpts.
- Platform packaging goes through `install.py` and `adapters/` — deployed copies are generated,
  never hand-edited.
