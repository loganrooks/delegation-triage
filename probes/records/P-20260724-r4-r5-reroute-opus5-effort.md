# P-20260724-r4-r5-reroute-opus5-effort — re-route event: R4 opus xhigh→medium, R5 opus high→low (operator ruling)

**Date:** 2026-07-24 · **Class:** availability/re-route event (not a scored probe — moves no
flip counter)
**Recorded by:** fable leg, 2026-07-24 campaign session (Claude Code)

## What changed

R4 (coding / agentic implementation) re-routed **opus xhigh → opus medium** and R5 (mechanical,
fully-specified edits) **opus high → opus low**, by operator in-session ruling: "the implementer
agent you should use is opus medium for most things … opus low as the lite implementor (bc
opus 5), and opus high can be a reviewer agent, this will be our proposal for now, until we get
more data." The reviewer third of the ruling was already executed the same day by the concurrent
session (P-20260724-r1-reroute-opus); this record covers the two implementer lanes.

## Label

**Provisional** — operator ruling + one vendor source (O5-SC FrontierCode, non-monotonic:
medium 53.4 > xhigh 43.6), *contested* by the vendor's own 2026-07-24 announcement charts
(monotonic through xhigh) [W-024(c)]. The operator asked for the routing judgment explicitly
("based on priors … this seems like the right routing choice no?"); the recorded answer: the
direction is defensible on the O5-SC leg and on price ($5/$25, STATE `price-opus-5`), but it is
an adoption of one side of a Contested pair — hence Provisional, hence the probe below stays
open with roles reversed. R5's `low` is the weaker leg: W-024(b) shows low's shape is
benchmark-dependent, and no source measures mechanical-edit tasks at all.

## Coupled edits (profile↔pin rule honored, one pass)

- `ROUTES.md` R4 + R5 rows re-pointed (both marked Provisional, W-024 added to R5's warrants)
- `agents/implementer.md` frontmatter `effort: xhigh` → `medium`
- `agents/implementer-light.md` frontmatter `effort: high` → `low`
- `agents/MANIFEST.md` both rows re-hashed and annotated
- `WARRANTS.md` W-024 "Route impact" bullet amended in place (dated UPDATE)

## Registration caveat

Pins register at session START. Sessions already running at flip time (including the fable leg
recording this) keep the old deployed pin until restart; per-call `{model, effort}` via the
Workflow `agent()` surface is the only way to honor the new route mid-session (CONTRACT §3).

## Basis and disconfirmer

The registered paired probe **P-20260724-r4-effort-frontier** is unchanged in design and now
tests the **incumbent** (medium) against the **challenger** (xhigh): PH-1's falsifier ("xhigh
passes review on a task medium fails, twice") becomes the re-flip condition for R4. For R5,
the open sonnet demotion probe re-scopes to **sonnet high vs opus low** (cost order inverted by
Opus 5 pricing: sonnet-5 intro $2/$10 vs opus-5 $5/$25 — sonnet is now the cheaper leg).

- **attestation:** operator ruling verbatim in the 2026-07-24 session transcript (fable leg);
  vendor numbers via W-024's SHA-verified bundle. Self-reported execution of the coupled edits;
  gates (`check_wids`, `check_state`) green at commit.
- **tally:** feeds W-024 claim (c) context only — count after this record: **0 local**
  (a ruling is not a probe; the counter opens when the first frontier leg runs).
