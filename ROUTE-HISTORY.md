# ROUTE-HISTORY — provenance for ROUTES.md (load-on-demand; never needed for routing)

Everything here was moved out of the routing table 2026-07-25 (operator directive: progressive
disclosure — the table is ingested by every triage; provenance is not). Canonical repo only — not
packaged into adapters. Full detail: `probes/records/`, `WARRANTS.md`, `docs/reviews/`.

## Per-row provenance

**R1** — re-pointed fable→opus high 2026-07-24, operator ruling: *"opus 5 is now the model… you can
get away with opus high for reviews."* Record: `P-20260724-r1-reroute-opus`. Cross-vendor lens
datum: n=1 deviated known-answer (P-20260717-sol-b20 — blind catch of the hardest MAJOR with
executable repro, 0 false positives). The fable-retained-classes clarification (incl. "driving
long-horizon work") was folded 2026-07-24/25.

**R2/R3 fallbacks** — xhigh→high 2026-07-25 (batch-A ruling, `P-20260725-batch-tier-rulings`):
FrontierCode Main favors high over xhigh by 4.4 pts for opus-5; authoring-adjacent cuts concur.

**R4** — opus xhigh→medium 2026-07-24, operator ruling *"opus medium for most things"*; adopts the
O5-SC leg (FrontierCode Main: medium 53.4 > xhigh 43.6) of a vendor pair still Contested against
the release-page monotone charts [W-024(c)]. Ruling record: `P-20260724-r4-r5-reroute-opus5-effort`.
The effort-frontier probe (`P-20260724-r4-effort-frontier`) stays open, now medium-incumbent vs
xhigh-challenger; **Run 1 (2026-07-25, Cowork Workflow dual-knob): medium leg blind-ACCEPTED,
xhigh leg blind-REJECTED (1 MAJOR), narrow margin — concordant, n=1.** Second documentary reading:
W-025(a).

**R5** — opus high→low, same ruling; W-024(b): low's shape is benchmark-dependent and unmeasured on
mechanical edits. Sonnet demotion probe re-scoped to sonnet high vs opus low (cost order inverted
by opus-5 pricing), count 1/3.

**R7** — re-pointed opus→sonnet high 2026-07-17 (operator ruling: sonnet-first, harness carries the
discipline) [W-023].

**R10** — xhigh→high 2026-07-25 (batch-A): was the last live xhigh opus pin; carried the F2
`thinking:disabled`+xhigh HTTP-400 exposure; HLE delta +0.4 (inside CSV read error).

**R13** — scope-refinement CANDIDATE from W-025(b): external taxonomy scopes fable's premium to
persistent-async / dynamic-decomposition / days-scale orchestration, opus high for bounded
fan-outs (known lanes, one synthesis). Surfaced via panel, not executed — fable-row moves stay
blocked by W-024(d): no controller-isolation measurement exists (see the packet's
`local_eval/` preregistered design and missing-evidence register M-001–M-007). Fallback xhigh→high
2026-07-25 (batch-A), concordant with the W-025 bounded-fan-out tier.

**R14 (retired)** — merged into R15 2026-07-25 (batch-B): its opus-only rationale held only for the
encrypted advisor TOOL; the plaintext advisor SUBAGENT path (W-022) is the shipped pattern. Prior
row text had referenced an opus-4.8 advisor (plaintext measured on 4.8; opus-5 format Unchecked).

**R15 fallback** — xhigh→high 2026-07-25 (batch-A): O5-SC HLE gives opus xhigh only +0.4 over high;
the fable-xhigh pin itself is SUPPORTED (fable HLE 54.4→57.8, +3.4 — largest fable gain in the CSV).

## Constraints provenance

**Judgment floor at sonnet** — P-20260720 logs-verification triad (n=1, post-hoc): haiku overclaimed
and missed the one load-bearing discrepancy; both sonnet legs caught it and scoped what they could
not check.

**Subagent-spawn cap (default 4)** — adopted 2026-07-25 (batch-D) per O5-PG via W-025: Opus 5
"delegates more readily" than 4.8; deterministic caps recommended.

**Preamble Unchecked caveat** — W-016/W-017 re-graded `Unchecked for opus-5` 2026-07-24 (proposal
F3); renewal path = the open effort probes.

## Profiles

**budget-conscious** — deleted 2026-07-25 (batch-C): its deltas predated opus-5 repricing
($5/$25, half fable) and the R1/R4/R5/R7 re-routes; one delta had become cost-raising. Re-derive
from `docs/reviews/2026-07-24-post-opus5-routing-issues.md` #1–#3.
