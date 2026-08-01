# Passive-first reprioritization — the ordinary run is the product

Status: **RATIFIED AS REVISED 2026-07-31 (operator, in-session) — binding priority order
for the control-plane initiative's next phase, including the three named doctrine
revisions in the header and the two reframe guards.** v1 (42cf94c)
was reviewed by a three-leg panel — unanimous CONCUR_WITH_CHANGES; adjudication and
finding-by-finding dispositions:
[`docs/reviews/2026-07-31-passive-first-panel-adjudication.md`](../reviews/2026-07-31-passive-first-panel-adjudication.md).
Two legs independently parsed all 131 live v2 ledger records; one built and ran the
rollup this proposal describes. Every measured claim below cites that run.

**What this document changes, named rather than disclaimed** (v1's "priority only"
disclaimer was found false by two legs): (a) it revises north-star §4's layer ordering — a
status-2 architectural hypothesis, revisable on evidence — for one phase: two L2
workstreams run ahead of the remaining L1 interchange work, on the trial-day evidence
that the local record spine works and nothing consumes it; (b) it demotes ROUTES.md from
sole route-evidence carrier to commentary-over-evidence, with the selector/profile layer
(profiles, budgets, preferences — §7.7's forkable half) named as a distinct layer above
the rollup, unbuilt this phase; (c) it assigns the rollup's product home under D-1:
`delegation-runtime` builds and owns the tool; this repo specifies its contract and
consumes its output. No §7 commitment, no ratified decision, and XV-1 are touched.

## The ruling this encodes

Operator, 2026-07-31, in-session (locator: driver session c4ca9689-0893-4843-a0d8-
d541bcc832f1, turn following the paired-trial countersign; memory:
`passive-signal-infrastructure-first`): the project's goal "was to allow signals to be
extracted even just from ordinary implementation or routing decisions… the priority
should always be getting this kind of infrastructure out there that basically passively
allows people to benefit." Average users "don't have crazy amounts of usage to be
spending on experiments and benchmarking" — they should install, route, drop occasional
small feedback notes, and benefit automatically from a web of others' contributions,
opt-in, privacy-considered. And: textual routing tables share the benchmark failure mode
— language over-generalizes and erases the conditions a routing decision needs.

This is the north star's §2 ("evidence produced as a side effect of ordinary use") made
the ranking rule for work, not just the horizon.

## What the evidence actually shows (corrected from v1 — panel F1/MINOR-11)

Measured against the live ledger (131 records, 57 runs, 2026-07-26→31): **the write path
is proven and cheap, but nothing about it is yet passive.** Every record is
research-program exhaust — trial arms, probe waves, panel legs — deliberately written by
an expensive router (fable-5 or sol, high/xhigh); zero records come from ordinary
non-meta work; no automated writer is wired into any hook. The spine is sound (57/57
intent↔outcome joins, zero orphans, retry modeling 100% well-formed) and nothing consumes
it: no decomposition item (B-1…B-7, C-1…C-5, E-1/E-2) owns the read side, and the loop
today is a Fable session reading JSONL by hand.

So the state is: **capture instrument working; passivity untested (E-1 is its test, §9's
falsifier its judge); consumption absent.** The priority follows from that corrected
statement, not from v1's "quietly worked" framing.

## The reprioritization (ranked workstreams + one reframe)

**P1 — Route-evidence rollup** *(renamed from "projection" — that word already means
three other things in this vocabulary, F6)*: make the ledger consumable at the decision
point.

- **First deliverable, pulled forward from C-5's orbit: publish the crosswalk §2a
  task-class enum.** The rollup's headline axis is null in 57/57 live intents *by the
  writer's own fail-closed design* until that publication; sequencing the enum first is
  what makes every later cell a measurement instead of a regex over prose.
- **Baseline is the existing `summarize`** (route-keyed marginals already ship); P1 is
  the increment: the intent↔outcome join, per-cell rollup over task-class ×
  harness-contract × binding, with **the run collapsed on `terminal` as the unit and
  attempts-per-run a named output** (the shipped per-record view reads retries as
  failures: 57% vs 74% on the same corpus).
- **Writer-side fixes are acceptance criteria, not follow-ons** (all measured): features-
  inclusive harness-contract hash, zero-sentinel abolished (15/57 records unpinned; one
  hash currently spans three contracts differing in `tool_profile` and `review_gate`);
  friction enum extended from the ~34 observed free-text families (43/50 coded entries
  are `other`); model-id normalization (`anthropic:opus-5` vs `anthropic:claude-opus-5`
  fragments the binding axis); host-harness expressible as a field, not prose.
- **Fail loud, never bucket silently:** `UNDERIVABLE` / `NO-IDENTITY` /
  `UNKNOWN-CONTRACT` are first-class cells; every cell carries its transformation list
  and source event_id set (§3 reversibility); no cell collapse (the scalar-leaderboard
  guard); a Contested/disagreement state exists; the rollup reports its own null-rates
  and **refuses decision-grade framing below the flip floor** (24/35 cells in the live
  corpus are n=1 — the honest current output is "insufficient evidence", said by the tool).
- **The rollup surfaces proposals; it never applies a route** (worldings W1's
  known-bug clause, carried in).
- Fable's role: contract design and review. The build is delegated (R4-class work).

**P2 — The average-user surface: install-and-capture + micro-feedback.**
Extend the L2 adapters (B-3/B-5 lineage, E-1 dogfood) so an ordinary Claude Code/Codex
user gets automatic intent/outcome capture on install — closing the measured passivity gap
(no hook writes records today) — plus a feedback affordance specified within §6.4's
binding constraint: **enumerated reason-codes drawn from the registered friction
vocabulary + an optional hash-referenced free-text note that is local-only by
construction and never leaves the machine** (W3's consent screen stays honest). P2 tests,
not assumes, H4's local-first premise: the hypothesis is that a user's own rollup
improves their routing at n=1; §9's E-1 falsifier judges it. P2's deliverable includes
the H5 maintenance clause: adapter repair/migration records and a stamped rollup version
are part of the surface, not externalized onto the steward.

**P3 — folded into C-5** *(v1 ranked this as a separate workstream; the panel showed all
but one sentence of it already lives in binding or registered work — §6
schema-shareable-by-construction, §7.11 contextual consent, C-5's XV-3/4/5/7/8/9/10
list)*. The one new scope cut becomes a C-5 requirement: the interchange design must
support **two consenting operators pooling conditioned records without a registry**
(field list, recipients, purposes, retention, withdrawal made visible per §7.11). §8's
no-new-proposal-cycle rule is thereby honored rather than half-invoked.

**Reframe — experiments become a graded contribution tier, with two guards.**
Runnable probes and paired trials remain the promotion path for claims they can test
(§7.8); XV-1 is untouched. New experiment proposals rank behind P1–P2 by default and
carry a `passive-signal alternative considered:` field — added to `probes/TEMPLATE.md`
as a requested field, **convention-only per B-4** (no deterministic checker yet), worded
at the promotion tier: *could passive signal promote this claim under H3's discipline?*
Guards, per the panel's starvation finding: (i) **falsifier-testing work is exempt from
the demotion** — B-5's cross-harness transfer test (§9's first falsifier, the premise P1
itself rests on) may run whenever ready; (ii) **the ranking is time-boxed to one rollup
cycle** — at the first §9 evaluation over real rollup output, the paired-trial channel's
cadence is re-decided, so XV-1's only promotion channel cannot silently starve while
hypothesis-records accumulate.

## Falsifiers (inherited, both stated)

North-star §9 stands. The two that bind this phase: (1) **B-5 transfer** — if conditioned
tuples fail to transfer across the operator's own two harnesses, L1's premise is damaged
and the sharing story halts (exempt from the demotion for exactly this reason); (2)
**E-1 + rollup** — if natural-traffic dogfood plus the rollup yields no local routing
improvement, the cold-start premise is dead and the sharing layer must not be built.

## Decision asked of the operator

Ratify: P1 (rollup, enum-first, fail-loud) > P2 (capture surface + §6.4-compliant
feedback) > C-5-absorbed sharing design > experiments-as-tier with the two guards; plus
the three named revisions in the header (§4 ordering for this phase, ROUTES.md
carrier→commentary with a named selector layer, rollup product home under D-1).
