# Schema pull-forward + north-star adoption — panel spread & adjudication (2026-07-27/28)

**RATIFIED 2026-07-27:** operator — "D-C5-1 (d) yes / D-NS-1 (b)+amendments yes."
Propagation landed same pass: north star (four-status separation, bootstrap-governance
clause, §3 boundary-record rename with content, H5, commitments 7/8 amended + 9/10/11
added, W11+XV-9 registered), worldings (counter-worlding rule, W9/W10/W13 breakdown set,
W1 flip-language bug noted for next touch), CONTRACT §6.8 check-not-veto clarification,
pilot §5 adjudicator-filled fault/timing rows, probes/TEMPLATE.md fields.

**Object:** `.planning/2026-07-27-schema-pull-forward-packet.md` (D-C5-1: pre-pilot crosswalk
v0.2.3 pull-forward; D-NS-1: adoption scope for the external theoretical review
`.planning/delegation-triage-evidence-commons-theoretical-review-2026-07-27.md`).
**Trigger:** operator anti-sunk-cost directive; driver self-diagnosed momentum bias in its
earlier C-5 deferral rationale and drafted (b) as the corrective.
**Spread:** 5 legs, 3 lineages — 2× opus/high reviewer pins (Claude), sol design session
resumed (warm C-5 context, xhigh), sol code session resumed (warm SC context, high), sol
fresh xhigh (epistemic-responsibility prompt — research leg, adjudicated separately when
delivered). Ledger runs `schema-pullforward-panel-{a,b}-20260727`,
`sol-{design-wave2-packet,code-wave2-scoping,epistemic-responsibility}-20260727`.

## Verdicts (4 verdict legs delivered)

| leg | lens | D-C5-1 | D-NS-1 |
|---|---|---|---|
| panel-a (opus/high) | decision economics + schema soundness, both-directions bias | **(d)** — affirmatively correct, not a floor | (b) on packaging economics only; SPLIT the decisions |
| panel-b (opus/high) | commons-alignment + foreclosure (§6.8) | **REVISE → (d)** | **APPROVE-WITH-AMENDMENTS** (three mandatory additions) |
| sol design @ xhigh (warm) | own wave-1 rationale re-examined | **(d+)** — validated per-failure sidecar; reject (b) as drafted | **(b+)** — add plural interpretations, contextual consent, W8/W12-class deps |
| sol code @ high (warm) | writer cost + mechanics | (b) is SMALL/buildable — but its own mitigation wording concedes the field is "a provisional claim, adjudication lives elsewhere" | not asked |

**Unanimous on the operative question: no outcome-record fault fields before the pilot.
D-C5-1 resolves to (d), enriched by sol-design's (d+) typing discipline. D-NS-1 resolves to
(b) + panel-b's three amendments, landed BEFORE any schema work (panel-b F8 sequencing).**

## D-C5-1 adjudication — packet option (b) REJECTED, (d/d+) adopted

The packet's case for (b) died on four independent grounds, each from a different leg:

1. **The load-bearing assumption was executed and falsified (panel-a F1,
   Verified-by-execution).** "Records written now cannot be retroactively typed" — panel-a
   ran the backfill against a temp store and re-validated under a v0.2.3-shaped validator:
   clean. Landing the fields later costs the same as now. The packet's "heuristically, via
   probe-record joins" also misused a crosswalk term of art: `heuristic-join` (§1a) names
   the NO-join-key case; the pilot mandates `run_id = probe_id` exact equality. Adjudicator
   note: the packet borrowed a pejorative from a context where it was earned.
2. **At-write typing of this field never existed (panel-b F1).** Pilot §6 makes cause
   adjudication non-author — structurally impossible at the driver's write moment. The
   packet's own flip condition ("if (d) preserves full retroactive typability at trivial
   cost, (b)'s urgency collapses") is satisfied verbatim.
3. **Wrong semantic home (sol-design W2-1/W2-2 + panel-b F2/F3, convergent across
   lineages).** A fault adjudication on the driver-attested outcome record encodes the
   disposition/evaluation conflation XV-5 was registered to remove; `ATTESTATION =
   "driver-attested"` is a module literal, so the field would flatten the very tier the
   pilot's V-M4 floor protects — with `harness` as the self-exculpating value that
   suppresses lane retirement (pilot §6). A scalar also cannot carry the two corpus
   specimens that motivate it (both mixed-cause), multiple failures per outcome, or
   evaluator disagreement.
4. **Null yield under its own success case (panel-a F4).** Wave 1 hopes for zero severe
   events; cause adjudication is only mandated for severe events; so under success every
   record reads `unadjudicated` — nulls by another name. Not virtuous-but-costly: costly
   AND yielding nothing.

Vocabulary defects (would have bitten even under (d)): `unadjudicated` reproduces the G1
three-states-one-token defect registered one day earlier (panel-b F4); `detection_timing:
later` duplicates registered friction code `undetected-omission` with no precedence rule
(panel-b F6 + panel-a F3 — caught by BOTH opus legs, neither sol leg); `later` is
structurally unwritable at outcome-write time, and probing the amendment path produces a
second record object — i.e. the field's own semantics walk you to XV-5's evaluation event
(panel-a F3, Verified-by-execution). The `_free` sibling violated the crosswalk's own
`other`-discriminator convention (sol-design W2-6 + sol-code, resolved differently — moot
under (d), preserved for C-5).

**Field selection critique preserved (panel-a F6):** if anything deserved pull-forward it
was G1 (`requested_effort` cannot express harness-cannot-deliver vs not-recorded) — the gap
wave 1 actually instantiates via FP-0a's `requested_effort: unknown` legs. Not pulled
forward either (backfills per-lane), but the omission shows the packet selected fields by
C-5-register salience, not by what wave 1 will write.

**Sol-code's scoping survives as C-5 input:** touch list, 12–15 adversarial tests,
absent ≠ `unadjudicated` migration semantics, and the false-authority SPEC wording
("driver's provisional primary causal claim... consumers MUST require a separate
third-party-verified evaluation artifact") — all transfer to wherever the assessment
record lands. Its SMALL estimate answered "can this be built safely" (yes); the panel
answered "is this the right object" (no). Both are true; the second governs.

**Residual fork within the (d) consensus, deferred to C-5:** panel-b's probe-record rows
(prose, TEMPLATE-carried, zero new machinery) vs sol-design's (d+) validated JSON sidecar
(machine-checked, per-failure keyed, shaped as future evaluation events). Wave 1 proceeds
on panel-b's form — the TEMPLATE already carries `adjudicator:`, `evaluator lineage:`, and
REQUIRED `attestation:`; (d+)'s typing discipline (non-exclusive candidate causes,
adjudication_status separate from cause, detection_timing with `unknown`, assessor
provenance, evidence locator) is registered as the C-5 evaluation-event design seed.

**Disposition:** pilot §5 gains a requirement — every wave-1 outcome's probe record carries
fault-attribution and detection-timing rows using pilot §6's V-M5 vocabulary, filled at
adjudication time by the adjudicator the TEMPLATE already names. No crosswalk bump, no
writer change. Both fields defer to C-5's evaluation-event pass with sol-design's (d+)
shape and sol-code's mechanics as opening inputs, alongside the friction/confounder overlap
question (an environment-fault IS a confounder; `REGISTERED_CONFOUNDER_CODES` still empty —
panel-a F4).

## D-NS-1 adjudication — (b) ADOPTED with panel-b's three amendments, sequenced first

Panel-b's structural finding (its 10/11, corroborated by sol-design W2-3 from a different
lineage): the draft (b) adopted breakdown worldings whose blocking commitments it left
verbatim — W13 (legitimate fork) against north-star §7.7 "never fork the evidence"; W9
(non-runnable incident) against §7.8 "runnable or it is an anecdote". Adopting a worlding
whose blocking commitment stands is decoration. Mandatory amendments:

1. §14 phrase change to commitment #7: preserve source records and lineage; permit forked
   classifications, trust policies, selectors, annotations, derived views.
2. §14 phrase change to commitment #8: runnable probes for claims they can test; field
   reports first-class, differently warranted.
3. W11 registered (not adopted) alongside the XV-9 consent caveat, which rides the next
   crosswalk touch by prior commitment (sol-adj:55-56).

Plus sol-design's dependency additions folded in: plural-interpretations and
contextual-consent commitments (without which "critical uptake" is vocabulary, not
mechanism). Exclusions all sustained after item-by-item carry-testing (panel-b): the
contribution ladder, §20 vocabulary program, Orientation Charter retitle, W7, W8, W12 —
nothing adopted depends on them [per: gardener-not-architect-community-design]. Each
adopted change gets an explicit status (normative floor / architectural hypothesis /
current constraint / design probe) at propagation time — sol-design W2-7's guard against
one large pass re-flattening the very status distinction it fixes.

**The normative-status bug is confirmed real and active** (packet premise verified,
panel-b 15, with the four conflicting passages quoted and a documented instance: the B-3
panel recorded worldings-foreclosure as blocking findings that changed a schema, from
documents declaring themselves non-binding). The practice was sound; the documented
authority for it is missing — which makes the fix a status-clarification pass, cheaper
than the packet implied.

**Sequencing (panel-b F8, adopted):** the bootstrap-governance clause lands BEFORE any
schema change, or the first act under the new governance regime predates the regime.
D-C5-1 and D-NS-1 are un-bundled for operator approval (panel-a F5: doc edits are
git-revertible; schema changes are versioned events — incompatible economics under a
single "yes").

## Fifth leg — sol fresh @ xhigh, epistemic-responsibility prompt (delivered after the
verdict legs; 195,718 tokens)

Research leg, not a verdict leg — it answered the operator's epistemic-responsibility
prompt in full, repo-grounded (report: `.planning/scratch-sol-epistemic-responsibility.out`,
final block). Its independent answer to the ordinary-credit-assignment question CONVERGES
with the panel from a fifth angle: "Do not add a required, single-valued fault_type field
to every outcome... Add a linked, typed **attribution assertion** mechanism instead" — the
speech-act-and-warrant standardized (target · claimed relation ∈ {observed deviation,
plausible contribution, supported contribution, ruled out, contested} · licensing check ·
competing explanations · scope · next discriminating probe · author/attestation/date ·
separate remediation owner), never the cause vocabulary. Its governing principle is the
best one-line formulation any leg produced: **"Causal uncertainty should narrow the scope
of learning before it is converted into a confidence score"** — repeated ordinary negatives
count against the exact configuration CELL, never against a component. Also registered
from this leg, non-blocking for the current decisions: the two-loop architecture
(fast loop executes ratified policy / slow loop compiles versioned proposals; the evidence
compiler must have NO permission to activate a policy); the decision-receipt as first local
value in shadow mode; five graded transfer tests for the two-harness gate (syntactic /
semantic / reconstructive / decision / loss-accounting); a W1 worldings bug find ("flips
under the flip discipline" contradicts proposal-not-application — check at next worldings
touch); the seven-way abandonment/revision list incl. "abandon ordinary fault typing as a
shared feature if cause labels mostly encode hindsight or organizational self-protection";
and provider auto-routers treated as routeable components with identity/version, hidden
bindings preserved as uncertainty. Its C-5 registration list (episode/attempt lineage,
policy version + decision mode, eligible-set + selection provenance, evaluation events,
attribution-assertion references, task-representation lineage, endpoint/router identity)
extends the register; adopted as C-5 input alongside sol-design's (d+) shape.

## Process notes (same-pass, ledger-recorded)

- **panel-a false-abandoned + recovery:** three idle notifications, two nudges, no report →
  parent terminalized the run `abandoned` and stopped the agent WITHOUT reading the
  teammate transcript (the primary artifact; violation of the parent's own recorded rule).
  Operator interrupted; SendMessage-resume recovered the completed report in one message.
  Root cause (teammate's own disclosure): it had sent the report 3× as plain text, which
  never routes to a parent — only SendMessage does; the nudges never named the channel.
  Ledger corrected (false terminal removed with backup + disclosure; true `accepted`
  written); signal `obs-20260728T024839-d54adb`
  (`shared/teammate-plaintext-report-invisible-to-parent`); memory rule amended with the
  ladder: nudge → nudge-naming-the-channel → read transcript → only then terminalize.
  v2 gap noted for C-5: terminalized-in-error has no reopen mechanism.
- **router_effort self-report error:** five intents this session recorded `router_effort:
  xhigh` from session assumption; the transcript (top-level `effort` field, per-record) and
  `CLAUDE_EFFORT` both read `high`. Corrected with backup + disclosure. New practice:
  router identity fields are READ (transcript `message.model` + top-level `effort` /
  `$CLAUDE_EFFORT`), never assumed — the router-side analogue of `observed_model`'s
  `identity_source` discipline. Gateway request logging (`~/.cli-proxy-api/logs`, currently
  off) noted as the wire-level tap candidate for pilot legs; would also close FP-0a by
  observation.
- Packet context drift (panel-a F7): ledger counts moved during review (records written by
  the review's own spawns); `probes/fixtures/flash-pilot/` still absent, further deflating
  (b)'s urgency framing. Both consistent with the adjudicated outcome.
- Zero rejected findings across 4 legs. Convergence quality: the decisive D-C5-1 argument
  was reached independently by three lineages via different routes (execution, foreclosure
  text, own-prior-rationale re-examination) — the strongest spread this instrument has
  produced; catch-sets NOT comparable across legs (different lenses by design)
  [per: claims-discipline].
