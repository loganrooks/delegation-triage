# Passive-first reprioritization — the ordinary run is the product

Status: **DRAFT 2026-07-31, awaiting panel review (§6.7a-style, commons-alignment lens
mandatory) and then operator ratification.** Authored under the operator's 2026-07-31
in-session ruling; changes PRIORITY and POSTURE only — no architectural hypothesis, §7
commitment, or ratified decision (D-1/D-2/D-4, north-star §6) is touched.

## The ruling this encodes

Operator, 2026-07-31 (after countersigning the paired substitution trial): the project's
goal "was to allow signals to be extracted even just from ordinary implementation or
routing decisions… the priority should always be getting this kind of infrastructure out
there that basically passively allows people to benefit." Average users of
Claude/Codex/Cursor "don't have crazy amounts of usage to be spending on experiments and
benchmarking" — they should install, route, drop occasional small feedback notes, and
benefit automatically from a web of others' contributions, opt-in, privacy-considered.
And: textual routing tables share the benchmark failure mode — language over-generalizes
and erases the conditions a routing decision needs; the commons answers "is this good for
MY case?" with situation-conditioned evidence, not global averages.

This is the north star's own §2 ("evidence produced as a side effect of ordinary use") made
the *ranking rule* for work, not just the horizon.

## What today's evidence adds

The trial day (P-20260731-pst-paired-trial) is the demonstration in both directions:

- The **expensive path** — Fable orchestrating a bespoke 12-leg paired trial — produced one
  high-grade answer at a usage cost no ordinary user can pay, and its driver-seat cost was
  itself dispositioned as misallocated (memory: fable-drives-judgment-not-pipelines).
- The **cheap path quietly worked**: ~30 delegation attempts wrote conditioned intents and
  outcomes to the v2 ledger (friction codes, attestation, observed identity) at near-zero
  marginal cost, as a side effect of ordinary orchestration. What is missing is everything
  DOWNSTREAM: no projection turns the accumulating ledger into route evidence consumable at
  triage time; the loop is a Fable session reading JSONL by hand.

H4's local-first premise (the instrument pays for itself at n=1) is therefore live but
UNREALIZED: records accumulate; value does not yet flow back.

## The reprioritization (three ranked workstreams + one reframe)

**P1 — Projection: ledger → conditioned route evidence at the decision point.**
A local, deterministic projector over `~/.delegation/v2/*.jsonl` producing per-cell
summaries (task-class × harness-contract × binding → outcome/friction tallies, attestation
split, dates) consumable when a spawn decision is made — the data-plane complement to the
textual ROUTES.md, which becomes commentary on evidence rather than the sole carrier.
Draws on the consolidated proposal's learning-plane material (B-2/B-3); honors H3's
discipline (observational records are hypothesis-generating; promotion still needs the
probe path). Ships even at n=1 (§7.1). Fable's role: design review, not driving.

**P2 — The average-user surface: install-and-benefit capture + micro-feedback.**
Extend the L2 adapters (B-3/B-5 lineage, E-1 dogfood) so an ordinary Claude Code/Codex
user gets passive intent/outcome capture on install plus a one-line feedback affordance
("that route felt wrong / right, because <optional note>") — the signal-skill discipline
scaled down to zero ceremony. Their P1 projections improve from their OWN usage first
(H4), before any sharing exists.

**P3 — Opt-in sharing layer: design only, consent-first.**
The L1 interchange work (§6 schema-shareable-by-construction, already binding) plus the
§7.11 contextual-consent gate: explicit field list, recipients, purposes, retention,
withdrawal limits. No platform build (§8 stands); the deliverable is the record-exchange
design that would let two consenting operators pool conditioned records without a
registry.

**Reframe — experiments become a graded contribution tier, not the evidence pathway.**
Runnable probes and paired trials remain the promotion path for claims they can test
(§7.8) and keep their flip discipline (XV-1 untouched). But no new experiment is proposed
without first stating what passive signal could answer the same question and why it
cannot; experiment proposals rank behind P1–P3 by default. (Memory:
passive-signal-infrastructure-first.)

## Foreclosure check requested of the panel

Per the worldings rule: does ranking P1–P3 above experiment work foreclose any §7
commitment or worlding? Specific worries to probe: (a) does P1's projector, built on the
CURRENT v2 schema, bake in the known schema gaps (projection-field conflation, signal
obs-20260731T192941-2ccc2f lineage; host-harness axis) in a way that resists the §6
v2-migration path? (b) does P2's zero-ceremony feedback re-run the careless-responding
curve the signal skill's one-interaction wall exists for? (c) does deferring experiments
starve H2's attestation tiers of the high-grade records that anchor grading?

## Falsifiers (inherited, restated)

North-star §9 stands unchanged — most sharply: if E-1-style natural-traffic dogfood plus
P1 projection yields no local routing improvement, the cold-start premise is dead and the
sharing layer must not be built.

## Decision this will ask of the operator (after panel)

Ratify P1 > P2 > P3 > experiments as the binding priority order for the control-plane
initiative's next phase, with the reframe clause as standing doctrine (CONTRACT §1
addition: the delegation test gains a "could passive signal answer this?" clause for
proposed probes).
