# PROGRAMME — the delegation-triage charter

role: charter-by-pointer (direction + pace + adoption; fast state lives in [LANES.md](LANES.md))
adopts: SEAS ADR-0023 (the programme-charter pattern) — adoption record §3; repo lineage is
SEAS ADR-0022/0024 ([LINEAGE.md](LINEAGE.md)), a different decision
lifecycle: **ratified** (v1 2026-07-31; v2 2026-08-01 after two-leg review —
Claude-lineage pointer/thinness leg + cross-vendor sol×xhigh design leg, both
CONCUR_WITH_CHANGES: [docs/reviews/2026-08-01-programme-charter-reviews.md](docs/reviews/2026-08-01-programme-charter-reviews.md);
ratified by operator 2026-08-01, in-session)
review_by: **2026-08-31** — past this date with no re-ratification, §1 reads as Unchecked
direction (the STATE expiry discipline, applied to this file): keep working the last-ratified
order but mark [LANES.md](LANES.md) `decision_due` and surface at next operator contact
ratification log (the canonical amendment record — one dated line per §0-governed change):
- 2026-07-31 · §1 direction · operator, in-session ("ratified as revised") · passive-first
  priority order + its three named doctrine revisions
- 2026-08-01 · charter v2 (whole document, §0–§4 + LANES.md split) · operator, in-session
  ("ratified.") · adoption of the SEAS ADR-0023 pattern becomes effective

This document is deliberately thin: pointers, never copies. This repo has measured what a
second copy costs (route values in a pointer file drifted within days — the note stands in
`adapters/claude-code/delegation.md`; v1 of THIS file reproduced a superseded CLAUDE.md
claim in its first lane-board, caught in review). If doctrine text appears below, that is
a bug.

## 0. Pace key and amendment transaction

| § | section | pace | amendment rule |
|---|---|---|---|
| 0 | this key | slowest | operator ratification, logged above |
| 1 | Direction | slow | operator ratification with a dated log line above; effective at the commit that adds it |
| 2 | Typed pointers | slow | pointer/type updates same-pass when a target supersedes; type changes need a log line |
| 3 | Adoption record | slow | supersede in place, dated |
| [LANES.md](LANES.md) | fast state | fast | same-pass updates, no ceremony; its own header rules govern |

**The transaction** (what makes a slow edit effective, per the sol review's governance
findings):

- A §0–§3 change is effective when its dated line lands in the ratification log AND the
  operator statement it cites exists (in-session statement or dated record) — the log line
  + its commit are the canonical locator.
- **Same-pass** means one commit in this repo. A dependent that lives in another repo
  cannot be same-pass by construction: it becomes an owed row in [LANES.md](LANES.md) with
  an owner, closed by the closing commit id — never silently assumed done.
- **Boot and refresh:** sessions read §1 + [LANES.md](LANES.md) at session start, again
  after compaction or resume, and before any lane-affecting change; durable handoffs record
  the charter commit consulted. A lane-affecting commit that finds §1 changed since its
  boot re-reads before landing.
- **Operator absence at a checkpoint** (e.g. the §1 time-box expiring unratified): the
  last-ratified direction stays binding, [LANES.md](LANES.md) marks the affected lane
  `decision_due`, and nothing reopens a demoted channel by default.
- **Supremacy and the citation guard** *(adopted from SEAS PROGRAMME §0, external-review
  F6)*: a faster-pace edit never authorizes work that nonconforms with a slower section,
  and citation-presence never substitutes for conformance — a rote `[per: PROGRAMME]`
  clears nothing.

## 1. Direction (ratified 2026-07-31 — passive-first)

The ordinary run is the product: priority goes to infrastructure that extracts routing
signal passively from ordinary delegation work, for users who cannot spend usage on
experiments. Ratified as
[docs/proposals/2026-07-31-passive-first-reprioritization.md](docs/proposals/2026-07-31-passive-first-reprioritization.md)
(panel: [docs/reviews/2026-07-31-passive-first-panel-adjudication.md](docs/reviews/2026-07-31-passive-first-panel-adjudication.md)),
which binds BOTH the order and three doctrine revisions:

> **Order:** P1 route-evidence rollup (task-class enum first; fail-loud; run-collapsed
> units) → P2 install-and-capture surface (§6.4-compliant micro-feedback; local-only
> notes) → sharing design inside C-5 (two-operator pooling, consent-first) → experiments
> as a graded contribution tier (falsifier-testing exempt — B-5 transfer test foremost;
> paired-trial cadence re-decided at the first north-star §9 evaluation over real rollup
> output — the time-box whose expiry rule is §0's operator-absence clause).
>
> **Revisions ratified with it:** (a) north-star §4 layer ordering revised for this
> phase (two L2 workstreams ahead of remaining L1); (b) ROUTES.md demoted from sole
> route-evidence carrier to commentary-over-evidence, with the selector/profile layer
> named as a distinct layer above the rollup (unbuilt this phase); (c) the rollup's
> product home is `delegation-runtime` under D-1 — this repo specifies and consumes.

The long-horizon vision is NOT here: it lives at the north star (pointer below) under its
own amendment discipline. This charter contains the vision by pointer, deliberately
diverging from SEAS's charter-⊃-vision-by-inclusion, because the vision doc predates this
charter and already governs its own amendments.

## 2. Typed pointers (what a session boots from; types per the sol review)

**Precedence rule:** binding constraints and normative floors CONSTRAIN work; §1 direction
RANKS it; an unresolved conflict between them halts the work and queues an operator
disposition — direction never overrides a floor.

Types: **binds-to** = pinned decision, confers authority, re-pin needs a §0 log line ·
**orients-to** = follows current text, cannot authorize work by itself · **status-map** =
informational index · **volatile** = intentionally follows head.

1. *(volatile)* [LANES.md](LANES.md) — current state; then [CLAUDE.md](CLAUDE.md) — repo
   architecture and editing discipline.
2. *(volatile)* [ROUTES.md](ROUTES.md) + [STATE.md](STATE.md) — every-spawn surfaces,
   expiry-as-Unchecked; per §1 revision (b), ROUTES.md is commentary-over-evidence once
   the P1 rollup ships, and the selector/profile layer is distinct from both.
3. *(orients-to)* [CONTRACT.md](CONTRACT.md) · the
   [north star](docs/proposals/2026-07-24-evidence-commons-north-star.md) + companion
   [Worldings](docs/proposals/2026-07-24-evidence-commons-worldings.md). A target changing
   under its own faster rules does not re-authorize work here: direction-level effects
   re-enter through a §0 log line, never silently through a pointer.
4. *(binds-to)* the
   [passive-first ratification](docs/proposals/2026-07-31-passive-first-reprioritization.md)
   (decision of record for §1) · north-star **§6 schema constraint** (the one current
   binding constraint,
   [north star §6](docs/proposals/2026-07-24-evidence-commons-north-star.md)) · **XV-1**
   promotion discipline (home: the
   [Gemini-Flash pilot](docs/proposals/2026-07-26-gemini-flash-36-pilot.md) §1/§6,
   mirrored at [WARRANTS.md](WARRANTS.md) W-026; applied by the 2026-07-31 pilot-closure
   adjudication) · **D-1** two-product split WITH its compatibility-contract condition
   ([decision-panel adjudication](docs/reviews/2026-07-24-decision-panel-adjudication.md)).
5. *(status-map)* [proposal map](docs/proposals/README.md) ·
   [probes/INDEX.md](probes/INDEX.md) · [agents/MANIFEST.md](agents/MANIFEST.md).
6. *(orients-to)* [WARRANTS.md](WARRANTS.md) — evidence on demand, supersede-in-place;
   never copy a W-clause into any other surface (v1 of this file did; review blocker).

## 3. Adoption record (cite-vs-adopt; supersedable in place)

- **Adopted decision:** SEAS **ADR-0023** (programme-charter pattern: pace-layered charter
  + fast lane surface as the session boot pair). Repo lineage — SEAS ADR-0022/0024, this
  repo's existence — is cited as lineage, not adopted as authority. The marker lives in
  this file's header (`adopts:`); this repo carries the rule **by convention, no lint**
  (stated plainly per the review — no decisions index or frontmatter machinery exists
  here).
- **Local basis, not borrowed authority:** no surface in this repo carried *direction*.
  CLAUDE.md is session-start × slow but carries architecture, not priority; the operator's
  2026-07-31 "why are we doing this?" had no consultable answer — direction was scattered
  across a handoff, a README overlay, and the reviews of four same-day ratifications
  (account, not measurement; the anchoring event is the operator's question itself,
  locator: driver session c4ca9689, post-countersign turn).
- **P-C (consumer):** [CLAUDE.md](CLAUDE.md) and the root [AGENTS.md](AGENTS.md) open with
  a pointer here; §0's boot-and-refresh rule makes consultation a stated obligation, and
  handoffs record the charter commit consulted. Adapter/deployment surfaces (codex
  fragment, Cowork plugin) carry the pointer as an owed [LANES.md](LANES.md) row until
  their next rebuild.
- **P-D (disconfirmer, behavioral — not citation-countable):** if two consecutive working
  sessions either find [LANES.md](LANES.md) stale against reality or select work that
  contradicts §1's order without a logged reason, the LANES header flips to `needs-review`
  and an operator disposition is queued; a token citation does not clear the flag. If that
  fires twice in a phase, this adoption is ceremony — supersede it, don't defend it.
- **Named mode of betrayal** *(adopted near-verbatim from SEAS PROGRAMME's dogfood block —
  marked as adopted text, not locally authored)*: this file renders direction as settled
  clauses and necessarily drops the deliberation that produced them; where force matters,
  read the provenance records, not this rendering. A charter that reads as complete is the
  failure mode; this one points outward on purpose.

## 4. Lane-board

Moved to [LANES.md](LANES.md) (fast surface, own header rules: owner · as-of · source ·
state per row). This section intentionally holds nothing else.
