# Worldings — the evidence commons in inhabited situations

**Status: ORIENTATION.** Companion to the
[evidence-commons north star](2026-07-24-evidence-commons-north-star.md). Nothing here is a
requirement; every vignette is revisable. The people are composites, not real individuals.

**Why "worldings."** A standard user story describes a feature from outside ("as a user, I
want…"). A *worlding* — the term is Heidegger's *Welten*, "die Welt weltet," imperfectly
translated — describes the situation from inside its involvements: a concrete moment in
which the system shows up within someone's already-mattering practice, ready-to-hand, and
the stakes do the normative work. We use them as a grounding check that runs in both
directions:

> **A design element that appears in no worlding is suspect. A worlding that no design
> element serves marks a gap.**

Each worlding carries: the situation; what the system *is* within it; the records produced
or consumed; which design commitments (north star §7) carry it; and **what breaks without
them** — the counterfactual is what keeps these load-bearing rather than decorative.

---

## W1 — Release day *(n=1; nearest horizon — this is E-1 + B-3)*

It's 10am and a new model has shipped. The operator's feeds are already full of it:
benchmark screenshots, a model card, three people declaring it "cracked" at agentic coding
and two declaring it overhyped. Last release, this cost an afternoon of reading and a week
of vibes-based routing.

This time the release lands differently. The vendor's claims file into the local knowledge
base as **Reported priors** attached to a **candidate row** — visible, dated, and
explicitly not-yet-a-route. The operator changes nothing. Over the following week, ordinary
delegated work does the measuring: each spawn writes an intent record (task class, route,
warrant consulted) and each completion writes an outcome record. By Friday the candidate has
a small pile of conditioned evidence from the operator's *own traffic*, and the route either
flips under the flip discipline or visibly fails to earn it. The feeds were never load-bearing.

- **Records:** candidate row + Reported priors in; conditioned intent/outcome tuples out.
- **Commitments:** #5 (release = candidate + trigger, never promotion), #6 (priors
  initialize, records adapt), #1 (local-first — no commons required for any of this).
- **Breaks without:** commitment #5 → the feed *is* the router; #1 → nothing happens until
  a community exists, i.e. nothing happens.

## W2 — The first transfer *(n=2; format only — B-5 is its first test)*

A Codex-harness user — different provider, different spawn surface, no roster pins — imports
a routing claim the operator published: sonnet-tier suffices for exploration lanes. The
record is not a sentence; it is a tuple, and its **harness-contract field** says what the
claim was conditioned on: a prompt contract with claim-tagging, a read-only tool profile, a
review gate downstream. The Codex user can see immediately that two of those three conditions
hold in their setup and one does not — so the claim transfers *as a hypothesis with a named
gap*, not as a fact. They run one paired probe to close the gap instead of ten to start from
nothing.

- **Records:** one conditioned tuple consumed; one paired-probe record produced (and
  publishable back).
- **Commitments:** #3 (conditioning preserved), #8 (runnable probes).
- **Breaks without:** the bare anecdote — "sonnet is fine for review" — imported, applied
  gateless, and burned; the folklore problem reproduced in a fancier costume. This is the
  north star's H1, and B-5 (one operator, two harnesses) is the cheapest place it can fail.

## W3 — The passive contributor *(L2 maturity)*

A developer in a two-person shop will never design an experiment and shouldn't have to.
Their harness writes intent and outcome records as a side effect of ordinary delegation —
they've never opened the schema. One day they opt in to sharing. The consent screen is
legible **because the schema made it so**: "these fourteen routing-relevant fields leave
your machine; your prompts, code, and file paths are in fields that structurally cannot."
No scrubbing pipeline, no trust-us redaction. Their records enter the commons tagged
**observational** — hypothesis-generating, never route-flipping — because they chose their
routes by their own priors, and the aggregation layer knows that confounds difficulty with
choice.

- **Records:** passive intent/outcome tuples, attestation-tiered as observational
  self-reports.
- **Commitments:** #2 (opt-in over an explicit field list), #4 (attestation typed), the
  north star's H3 answers (privacy by schema separation; observational ≠ interventional).
- **Breaks without:** schema separation → an anonymization pipeline nobody fully trusts,
  and rightly; the observational tag → confounded "model X is worse at Y" claims
  mass-produced at community scale.

## W4 — The probe author *(L3 horizon; kept here so L1 doesn't foreclose it)*

Someone with a strong opinion and better habits packages it: a probe artifact with pinned
harness, pinned prompt, a rubric, and a stated expected cost. Re-running it is minutes, not
an afternoon of reconstruction. Within days, three strangers on three setups have attested
concordant re-runs, and the claim promotes under the same flip discipline this repository
uses at n=1 — not because the author is credible, but because the artifact made credibility
unnecessary. A year on, the probe is stale — models have plausibly trained against its
public prompt — and the registry says so, because probe decay is tracked, not denied.

- **Records:** a runnable probe artifact; attested concordant re-run records; a decay
  annotation.
- **Commitments:** #8 (runnable over reported), #4 (attestation tiers); the open remainder
  is H2's rotation/holdout governance, deliberately deferred to L3.
- **Breaks without:** runnability → "trust me" at scale, which is where we started; decay
  tracking → a commons that Goodharts itself.

## W5 — The budget-constrained user *(L2–L3)*

A student gets the same evidence base as a funded lab — and different routes. Their profile
is **selector policy**: a budget ceiling, a stated tolerance for retry-on-failure, a
preference for cheap sweeps with escalation gates. The evidence they consult is
cost-conditioned (every tuple carries its binding, and bindings carry price lineage), so
"best route" is computed *for their constraints*, not read off someone else's. When their
budget changes, the profile changes; the evidence doesn't.

- **Records:** consumed only — tuples filtered through a selector profile.
- **Commitments:** #7 (profiles customize the selector, never fork the evidence), #3
  (conditioning includes cost). Lineage: this package's balanced / budget-conscious
  profile deltas ([ROUTES.md](../../ROUTES.md)).
- **Breaks without:** one-size routing that quietly assumes everyone's budget, or — worse —
  per-user forks of the evidence base itself, which destroys the commons to serve it.

## W6 — The dispute *(L3 horizon)*

Two contributors publish conflicting records on the same task class: one finds the cheap
tier sufficient, the other finds it fails review half the time. Nobody averages them.
The claim goes **Contested** and both records survive *with their conditioning* — and the
conditioning is where the resolution usually lives: one ran under a review-gated contract,
the other gateless. The disagreement was never about the model; it was about the harness,
and the tuple format made that discoverable in minutes rather than a comment-thread war.
What genuinely cannot be resolved this way is named, and becomes a registered open question
with a probe design attached — which is what L3 governance owes the community.

- **Records:** two conflicting attested tuples; a Contested grade; a registered open
  question.
- **Commitments:** #3 (conditioning preserved is what makes disputes *tractable*), #4;
  vocabulary from [EPISTEMICS.md](../../EPISTEMICS.md).
- **Breaks without:** silent averaging or a flame war — both destroy information, one
  politely.

---

## Reading the set

W1–W2 are the current decomposition wearing narrative clothes: B-3 (intent record), B-5
(second harness), E-1 (natural-traffic dogfood). If the vision is real, it must first be
real *there*, at n=1 and n=2. W3 requires L2 maturity; W4–W6 are L3 horizon and are included
now for exactly one reason: so that L1 schema decisions — the only binding work this vision
currently claims (north star §6) — don't foreclose them.
