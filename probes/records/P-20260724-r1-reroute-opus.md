# P-20260724-r1-reroute-opus — availability/re-route event: R1 reviews fable→opus (Opus 5)

**Date:** 2026-07-24 · **Class:** availability/re-route event (not a scored probe)
**Recorded by:** fable leg, 2026-07-24 campaign session (Cowork)

## What changed

R1 (review gates) re-routed **fable high → opus high** by operator in-session ruling:
"use opus for reviewing now over fable, fable for orchestrating decomposing tasks,
brainstorming etc." + "opus 5 is now the model, and its good, you can get away with opus high
for reviews." Fable retained for orchestration/decomposition/brainstorming (R13 unchanged;
R2/R3/R8/R15 untouched by this ruling).

## Coupled edits (profile↔pin rule honored, one pass)

- `agents/reviewer.md` frontmatter `model: fable` → `opus` (effort stays `high`);
  new sha256 `2369d9d3e53dc16c4aaadca63468c31a067bf7fbe763fd920360d528c7727c46`
- `ROUTES.md` R1 row re-pointed; fallback column now "same; xhigh per stated reason;
  fable per stated operator request"
- `STATE.md` reviewer-pin row updated (basis: quality ruling, NOT the ADR-0022 cliff —
  the scheduled flip is superseded, executed early on a different basis)
- `agents/MANIFEST.md` reviewer row re-stamped

## Registration caveat

Pins register at session START. Sessions already running at flip time (including the opus leg
live at 2026-07-24 ~18:5x) keep the old pin until restart.

## Basis and disconfirmer

Basis: operator ruling; context = Opus 5 released 2026-07-24 at $5/$25 (half fable's sticker),
vendor-Concordant review quality claims — no local paired R1 datum yet. Disconfirmer: an R1
review miss attributable to opus-vs-fable capability, adjudicated via a paired fable/opus review
on the same artifact + charter (the P-20260717 pairing pattern) → flip back with the datum
recorded here.
