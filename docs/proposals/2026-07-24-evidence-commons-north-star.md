# Evidence commons — north star

**Status: ORIENTATION (north star), not an implementation contract.** This document binds
exactly one near-term design decision (§6); everything else orients. Nothing here authorizes
building, spending, or activating anything, and the §6 constraint awaits operator disposition
alongside decisions D-1–D-4 in the
[2026-07-24 portfolio decomposition review](../reviews/2026-07-24-portfolio-decomposition-fable-review.md).

**Provenance:** operator vision (dictated 2026-07-24) plus the same session's assessment.
Claims about this repository cite paths. External precedents (§10) are training-knowledge,
label **Unverified** — re-check before load-bearing use. Everything else is design intent:
**Conjecture** by construction, falsifiable by §9.

**Companion:** [Worldings](2026-07-24-evidence-commons-worldings.md) — the same vision held to
concrete inhabited situations.

---

## 1. The problem, stated from our own artifacts

Every model release produces a fog: vendor benchmarks that this package's own epistemics
grade as Reported and never Corroborated ([EPISTEMICS.md](../../EPISTEMICS.md)); private
benchmarks that don't transfer because their harness and prompt conditions are unrecorded;
anecdotes ("this one's better at UI") that aggregate into folklore; and leaderboard scalars
that destroy exactly the conditioning a routing decision needs — task class, harness,
effort, prompt contract.

The n=1 counter-effort is real but starved. After months of discipline this repository
holds 24 warrant records ([WARRANTS.md](../../WARRANTS.md)), an effort question still
Contested (W-024), a route ruling with zero paired probes behind it (W-023), and flip
thresholds (W-019) the operator can rarely afford to reach. **One careful operator cannot
generate enough attested evidence to keep a routing table calibrated.** That sentence, read
from our own files, is the demand for the commons.

## 2. The vision in one paragraph

A community-scale version of what this package already does at n=1: an **evidence commons**
in which conditioned, attested, reproducible routing evidence is produced as a side effect of
ordinary use, shared opt-in, aggregated without abstraction, and consumed as calibrated
per-user routing policy. It is not hypothesis-testing science and should not pretend to be;
it is closer to **distributed metrology with graded attestation** — most participants
contribute measurements, not experiments — with this package's epistemics vocabulary as the
shared grading language.

## 3. The atomic object: the conditioned evidence tuple

The unit of exchange is never a score. It is the tuple

> **task-class × harness-contract × binding (model × effort × delivery surface) × outcome ×
> attestation × date**

with one non-negotiable rule: **conditioning travels with every number, and aggregation must
preserve it.** Lineage: the demand + selector + binding representation (review §3, R-D) plus
its harness-assumption refinement — W-023's sonnet-first is policy *conditioned on* harness
discipline and transfers to nobody who lacks the harness. The moment a scalar leaderboard
appears anywhere in this system, the commons has failed at its own premise.

## 4. Three layers, built in order

| layer | what it is | status / posture |
|---|---|---|
| **L1 — record standard** | The interchange format: conditioned-tuple schema, epistemics grades, attestation tiers, stable IDs, namespacing. A "delegation evidence interchange format." | **First.** Cheap, durable, wins even if L3 is never built. Formats beat platforms — and a good format makes someone else's platform interoperable rather than competing. |
| **L2 — local tooling** | Per-harness adapters that write records passively (intent + outcome) and probe runners that produce them interventionally. | This is the current decomposition's B-3 / B-5 / E-1, unchanged. |
| **L3 — registry + governance** | Aggregation service, dispute adjudication, contamination defense, conflict-of-interest handling, forking rights over the evidence base. | **Deferred.** Every hardest problem lives here. Building it before L1–L2 have proven the records are worth sharing is building the marketplace before the currency. |

## 5. Hard-problems register

Each entry: the problem, the design answer already in hand, and the open remainder.

- **H1 — Transfer without abstraction.** Results are conditioned on harness × prompt ×
  task class; strip the conditioning and you rebuild the leaderboard failure. *Answer:* the
  tuple carries its harness-contract field (§3). *Open:* whether tuples actually transfer is
  empirical — the first test is one operator's own two harnesses (decomposition item B-5,
  Codex OTel leg).
- **H2 — Trust inverts at scale.** Locally, `attestation: self-reported` works because one
  operator has skin in the game. At scale: vendor astroturfing, Goodharting (models trained
  against public probes — benchmark contamination recurring one level up), and honest-but-
  sloppy reports drowning signal. *Answer:* attestation tiers with self-reported tallied
  separately (the [probes/TEMPLATE.md](../../probes/TEMPLATE.md) discipline, scaled), and
  probes shipped as **runnable artifacts** — pinned harness, prompt, rubric, expected cost —
  so reproduction is by construction, not by trust. *Open:* probe decay and rotation/holdout
  strategy; both are L3 governance, deferred.
- **H3 — Passive traces are the best and most confounded signal.** Best because they are
  real demand (the E-1 conclusion). Confounded three ways: privacy (traces contain code and
  prompts), selection effects (people route by their priors, so observational records
  confound route choice with task difficulty — a causal-inference gap), and weak outcome
  labels. *Answer:* privacy by **schema separation, not scrubbing**; observational records
  are hypothesis-generating only, with paired/interventional probes as the promotion path
  (W-019 flip discipline, scaled); outcome capture must sit at the driver's decision point
  (review constraint DR-2). *Open:* causal-aware aggregation design — L3.
- **H4 — Cold start.** A system useful only at scale dies at n=10. *Answer:* local-first
  value — the instrument pays for itself for a single user (better routing for *me*), and
  sharing is an opt-in overlay on records that already exist. *Open:* none by design; §9
  makes this a falsifier instead.

## 6. The one binding near-term constraint (proposed)

Decomposition item **B-3** (intent/outcome record + sidecar) must design its schema
**shareable by construction**. *(As amended 2026-07-24 by the
[decision-panel adjudication](../reviews/2026-07-24-decision-panel-adjudication.md) after both
panel legs checked these constraints against the live Codex orchestration-learning schema —
which B-5 discovered after this document was first committed.)*

1. **stable IDs with defined scopes** (event / run / origin-namespace / project-pseudonym)
   that survive leaving one machine — scope definitions and a pseudonym rekey/migration rule
   come first; a machine-local-salted ID (the Codex `project_id` pattern) does not qualify
   as-is;
2. an explicit **harness-contract field** — which prompt/skill/gate discipline was in force;
3. an explicit **attestation field** — the tiered vocabulary **must first be defined as an
   enum** (today only free-form locators + `self-reported` exist; EPISTEMICS labels are
   claim-grades, not attestation tiers);
   *(2 and 3 are absent from the Codex v1 schema, whose strict validator rejects unknown
   fields — they enter as a **v2 with dual-read migration**, never as appended fields)*;
4. **sensitive fields separated from routing-relevant fields at the schema level** — a
   **floor**: Codex v1's allowlist-plus-reject posture already exceeds it and must not be
   weakened to meet it. Free-text routing fields (e.g. a `why`) violate this by construction —
   use enumerated reason-codes + optional hash-referenced note;
5. namespacing-ready (a record can later carry an origin without format change).

Cost: **not near-zero** (corrected 2026-07-24 — the original sentence predated B-5): B-3 is
now a three-schema crosswalk plus a v2 migration of a schema this package does not own;
schema-change governance across the two products belongs to the D-1 compatibility contract.
Retrofit cost later remains higher still. This section is the only part of this document that
touches the current plan.

## 7. Design commitments

What any future implementation must not violate. A change to one of these is a change to the
north star itself and needs operator disposition, not a local edit.

1. **Local-first value** — every layer must be worth running at n=1.
2. **Opt-in sharing** — records exist locally by default; sharing is an explicit act over an
   explicit field list.
3. **Conditioning preserved end-to-end** — no scalar leaderboards, ever (§3).
4. **Attestation graded, self-reported tallied separately** — trust is typed, not assumed.
5. **A release is a candidate and a review trigger, never an automatic promotion** —
   ([README.md](README.md), interpretation rule 3, already doctrine).
6. **Literature initializes priors; on-the-ground records adapt them** (W-018 lineage —
   curated priors, then probes).
7. **Per-user profiles are selector policy over a shared demand ontology** — budgets and
   preferences customize the selector, never fork the evidence
   ([ROUTES.md](../../ROUTES.md) profile-delta lineage).
8. **Runnable probes over reported claims** — a shared probe is an artifact you can re-run,
   or it is an anecdote.

## 8. Non-goals now

No platform build. No governance body. No anonymization pipeline. No new proposal cycle —
the portfolio review's finding stands: four review rounds have run on zero new runtime
evidence, and this document must not spawn a fifth. The next moves are unchanged from the
[review's decomposition](../reviews/2026-07-24-portfolio-decomposition-fable-review.md) (§5);
this vision constrains one schema (§6) and otherwise waits.

## 9. Falsifiers / flip conditions

- **Tuples fail to transfer across the operator's own two harnesses** (B-5's test): the L1
  premise is damaged — redesign the conditioning before any sharing story.
- **E-1 natural-traffic dogfood yields no local routing improvement:** the cold-start
  premise (H4) is dead — there is no unit worth sharing, and the commons should not be built.
- **The conditioning proves too heavy for contributors** (records chronically unfilled):
  the schema is wrong — simplify before scaling, don't evangelize harder.
- **An external format or community emerges that satisfies §7:** join it; don't compete.
  Formats-beat-platforms cuts both ways.

## 10. Precedents (training knowledge — Unverified today; re-check before citing onward)

- **Chatbot Arena** — the closest existing thing (passive preference aggregation at scale)
  and the cautionary syllabus: unrepresentative traffic, style confounds, gaming once the
  leaderboard mattered — every failure traceable to aggregating away the conditioning.
- **Cochrane / GRADE** — evidence grading as a community practice; this package's
  epistemics vocabulary is essentially homegrown GRADE.
- **Package registries + reproducible builds** — attestation and provenance at scale.
- **OpenStreetMap** — community data sustained by local verification and local usefulness.
