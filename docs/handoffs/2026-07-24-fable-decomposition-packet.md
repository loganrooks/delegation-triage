# Handoff packet: Fable decomposition of the delegation control-plane initiative

- **Date:** 2026-07-24
- **For:** a Fable 5 session (high effort) running as architect/decomposer in a parallel session
- **Prepared by:** delegation-triage root session (Claude Opus 5), on operator ratification
- **Status:** ready to hand off. Nothing in this packet is authorized to execute.
- **Authority:** **review, decomposition, and planning only.** No implementation, installation,
  deployment, activation, route flip, commit, push, cleanup, deletion, or paid probe. The operator
  holds all of those.
- **Predecessor:** [2026-07-24 Codex control-plane handoff](2026-07-24-claude-control-plane-initiative-handoff.md)
  and its [Claude review](../reviews/2026-07-24-control-plane-initiative-claude-review.md)

---

## 1. The assignment, and the one thing that makes it different

Decompose the next phase of this initiative — **and attack the recommendation it rests on first.**

The controlling finding of the prior review is F-1: *every review in this repository was scoped to
the artifact handed to it; nobody has reviewed the portfolio.* Three prior review gates (a
cross-runtime cold read, a Sol review, a Fable audit) each returned real blocker-class findings and
each was contract-pinned to one document. None could see that the document set might be mis-scoped.

**You are the first reviewer given the portfolio as the unit.** If you decompose the plan without
first testing whether the plan should exist in that shape, this packet has wasted its premium.

You are explicitly authorized — and expected — to **reject** the root session's recommendations.
They are listed in §5 with their load-bearing assumptions and falsifiers precisely so you can
attack them. A decomposition that adopts them uncritically is a worse outcome than one that
discards them with reasons.

---

## 2. Required reading, in order

| # | Artifact | What it is for |
|---|---|---|
| 1 | [Claude review of the initiative](../reviews/2026-07-24-control-plane-initiative-claude-review.md) | 8 verified defects (§2), 8 framing findings (§3), per-proposal dispositions, the recommended split. **Start here.** |
| 2 | [Codex handoff](2026-07-24-claude-control-plane-initiative-handoff.md) | The initiative as originally framed. Its §5 layer table and §8 Opus-5 inference are both challenged by #1. |
| 3 | [Consolidated control-plane proposal](../proposals/2026-07-21-consolidated-multi-harness-delegation-control-plane.md) | The leading architecture. Unratified. §§7.1–7.3, 8.2–8.3, 13 survive the review nearly intact; §§4.1, 5.1, 8, 14 do not. |
| 4 | [Proposal map](../proposals/README.md) | Lineage and supersession across six proposals. |
| 5 | [`CONTRACT.md`](../../CONTRACT.md), [`ROUTES.md`](../../ROUTES.md), [`STATE.md`](../../STATE.md), [`WARRANTS.md`](../../WARRANTS.md), [`EPISTEMICS.md`](../../EPISTEMICS.md) | The live instrument — 811 lines. The thing all of the above is *about*. |
| 6 | [Routing-infrastructure survey](../research/2026-07-24-routing-infrastructure-survey.md) | Reference designs (Arch-Router convergence), issue-corpus evidence on what users actually complain about, the OTel substrate. **§4 carries a falsification banner — read the probe with it.** |
| 7 | [P-20260724 OTel substrate probe](../../probes/records/P-20260724-otel-routing-observability-substrate.md) | First-hand, verified. Corrects the survey. |
| 8 | [W-024](../../WARRANTS.md) + [external audit bundle](../research/external/2026-07-24-opus5-fable5-routing-audit/PROVENANCE.md) | Opus 5 evidence, four claims, four flip conditions, one live `Contested`. |
| 9 | [`probes/KNOWN-WEAKNESSES.md`](../../probes/KNOWN-WEAKNESSES.md), [`probes/INDEX.md`](../../probes/INDEX.md) | Failure kinds and flip discipline. |

---

## 3. State of play — four inputs that did not exist this morning

### 3.1 The instrument was broken in ways its own machinery forbids — now repaired

Eight verified defects (review §2), **all closed or dispositioned on 2026-07-24**. Every gate is
now green: `check_state` exit 0 (first time in this cycle), `check_wids` exit 0, adapter suite 223
OK via the exact CI command, deployment 64/64 current with zero divergence.

**The repairs are not the input. What they teach is.** Every one of the eight violated a rule the
package already states, and none was caught by the machinery that states it:

- Canonical `agents/explorer.md` said `model: opus` while `ROUTES.md` R7 and `W-023` both asserted
  a 2026-07-17 re-point to `sonnet` — so **the documented deploy command would have silently
  reverted an operator ruling.** CLAUDE.md's profile↔pin coupling rule forbids exactly this; a
  route+warrant commit shipped without the coupled pin edit anyway. *Repaired: canonical promoted
  to the ruling, MANIFEST re-stamped.*
- The deployed `ROUTES.md` and `STATE.md` matched **no commit in repository history** — hand-edited,
  serving a different doctrine than canonical, for an unknown duration. The consolidated proposal
  §5 names this as a risk to prevent; it had already happened, in the reference deployment,
  undetected. *Repaired after adjudicating that both were strictly lossier than canonical.*
- Three roster definitions the package does not own are live and **routed to by R1**. `--check` was
  structurally blind to them. *Now reported as `EXTRA`; adoption is an open operator decision — a
  packaging question, since their pins need a private gateway.*
- Volatile state read `Unchecked` for five days and CI failed for five days — **the expiry
  mechanism worked exactly as designed and nothing forced the disposition.** *Repaired; the
  scheduled action's gap, not the mechanism's, is the finding.*

**Two of these bear directly on your decomposition.** First: a hash manifest cannot detect a value
that was never propagated into the thing it hashes — which is a limit on the whole
manifest-and-drift-check family the consolidated proposal builds on. Second, and sharper: the drift
classifier written to fix defect D-8 **produced a false positive against itself one commit later**,
accusing a deployment of being hand-edited when the real cause was a deploy taken mid-edit from a
dirty source. "Not in git history" only means hand-edited if the source is clean. It now reports a
fourth state, `DRIFT?` — undecidable, reports without accusing, does not fail the gate.

That is a live specimen of the failure this package's epistemics exist to prevent, produced by the
package's own new tooling, inside a day. **Treat "our integrity checks will accuse the wrong party"
as a design risk with demonstrated base rate, not a hypothetical.**

Still open, and yours to weigh: the `sol-*` adopt-or-drop decision, and commit sequencing
(`ci.yml` and the untracked `adapters/codex/**` must land in one commit or neither).

### 3.2 A measured baseline for the dogfood question

The observability layer already deployed (signal-layer's `obs-*` hooks) holds **670 spawn-req
events**, never queried until 2026-07-24:

- **15 (2.2%) carry a task tag; 5 cite a route row or W-ID.** README's P-D(c) disconfirmer says a
  work-week of delegation with no fit line citing a route/W-ID means the package is decoration.
  *Scope honestly:* `prompt_head` is truncated and CONTRACT §4's fit line lives in the visible plan,
  so this measures "citation reached the durable record," not "the driver stated a fit line."
- **155 spawns went to a pinless agent type from an xhigh/max session** — children inherit xhigh by
  construction. The `effort-inheritance over-provisioning` kind was two anecdotes; it is n=155.
- **2,016 `subagent-start` vs 670 `spawn-req` — 1,346 starts with no captured request leg.** The
  capture layer under-captures itself by roughly 2:1. **No rate off this ledger is trustworthy
  until that gap is explained, including the 2.2%.**

### 3.3 The observed side of telemetry is already oversupplied

Verified first-hand (P-20260724), env-vars only, no persistent config change, $0.81:

- `claude_code.api_request` carries `model`, `effort`, `cost_usd_micros`, full token/cache split.
  **`effort` is populated and equals the pin's effort.**
- **`agent.name` is redacted to `custom` for roster agents; `OTEL_LOG_TOOL_DETAILS=1` does not
  un-redact it.** The join key proposed in the survey does not exist.
- The real join key is `claude_code.subagent_completed`, **absent from the docs page the survey
  read**, carrying `agent_type` (exact pin identity), `agent.source`, `model`, `final_model`,
  **`model_swapped`**, `total_tokens`, `duration_ms`.
- Free detectors fall out: `model_swapped` mechanizes the `provenance-misreport` kind;
  per-`query_source` `effort` mechanizes `effort-inheritance`.

**The intent side is the only genuinely missing half** — task class, route ID, W-IDs, why.

### 3.4 Live vendor evidence with a Contested row

[W-024]: Opus 5 medium beats Opus 4.8 max on score *and* cost across three official charts at ~half
cost; low lags on one of three; **the medium-vs-xhigh shape is Contested between two official
Anthropic sources** (O5-SC FrontierCode is non-monotonic with xhigh ≈ worst; the 2026-07-24 news
charts are monotonic through xhigh). R4 is annotated, not flipped. R13 is *blocked* from moving —
the system card's multi-agent runs used a pre-release model and an unreleased effort config.

---

## 4. Questions the decomposition must answer

1. **Is the portfolio split right?** Three artifacts (doctrine / Claude Code integration / a
   separate `delegate-to-claude` runtime) versus one product, versus something else. Review §6.
2. **What is the product — the method or the routing answers?** Review F-6. This decides what a
   release *is* and whether the telemetry apparatus is sized correctly.
3. **Observability coupling.** Own the spec and ship one writer, extract a third shared package, or
   depend on signal-layer (currently **private** — that blocks the public-package path unless its
   posture changes, and it would force `/signal` on strangers). §5.3 has the decisive test.
4. **Route representation.** Rows currently mix task classes (R1–R8), a pricing posture (R9), a
   parked experiment (R11), and Claude-Code advisor plumbing (R14/R15). What survives projection to
   Codex? Review F-5 argues the portable content is the left column, not the bindings.
5. **Situational routes.** The operator's actual policy is conditional — sonnet medium as budget
   default, higher when thinking is involved — and a frontmatter pin cannot express it (model is
   per-call overridable; **effort is not**, outside a Workflow). Design the mechanism.
6. **Sequencing and wave design.** What runs next, in what order, and what shape should the research
   fan-out take (moderate, ~5–6 lanes, spanning tiers so telemetry has variance — **your call to
   revise**).
7. **Why did a deployed instrument go unused for 670 delegations, and what makes the next one
   different?** This is the question the 2.2% poses, and no proposal in the set asks it.

---

## 5. Root-session recommendations, with their falsifiers — attack these

| # | Recommendation | Load-bearing assumption | What would flip it |
|---|---|---|---|
| R-A | Split the portfolio three ways | No Claude Code workflow needs the packet schema, policy compiler, or reconciliation engine | Produce one that does |
| R-B | Doctrine owns the capture **spec**; ship one writer; build **no** plugin interface | The routing-relevant field set is small and slow-changing | Write the union across signal-layer hooks + Claude Code OTel + Codex OTel. Large or churny ⇒ shared implementation wins, vendor signal-layer's writer instead. **Half a day, and it decides this on evidence.** |
| R-C | Defer packaging, decide schema now | Packaging is reversible; a community corpus makes schema changes expensive | Show packaging is the expensive one here |
| R-D | Route rows become demand + selector + binding | Judgment demand is more portable than model identity | A harness where demand doesn't transfer |
| R-E | The research wave doubles as observability dogfood | A layer with no traffic can't be validated | A cheaper validation path |
| R-F | Fix the 8 defects before new architecture | They're independent of the architecture decision | Show a defect whose fix depends on it |

---

## 6. Prompt contract for any agent you spawn

Per [`delegation.md`]:

- Today is **2026-07-24**. Do not rely on training data for anything post-cutoff — search and verify.
- Tag every claim **[CONFIRMED — URL]**, **[REPORTED — URL]**, or **[UNCERTAIN]**. Separate shipped
  from announced from rumored.
- Local-file claims carry a **source path and a short quote**.
- State output bounds and structure numbered.
- **Explorer-tier lanes report facts and follow-up pointers, never judgments or recommendations**
  (operator correction 2026-07-10). Only synthesis/review-tier agents close with implications.
- Beware SEO/AI-content sites; check sensational specifics against primary sources.
- State the fit line before each spawn: agent · model · effort (**and how the effort arises** —
  pin vs inheritance vs per-call) · surface · task class · why, citing a ROUTES row or W-ID.

**Surface warning, measured:** a generic Agent spawn inherits session effort. 155 of 670 recorded
spawns fired that way from xhigh sessions. If your route's effort ≠ your session's effort, a generic
spawn is the wrong surface *by construction* — use a roster pin or a Workflow `agent()` call
(CONTRACT §3).

---

## 7. Routing of this spawn, and a probe it should carry

> **⚠ BLINDING — §7 IS NOT TASK CONTENT. Do not include this section in either leg's prompt.**
> It describes how this spawn is routed and measured. A worker that reads it knows it is being
> compared against another model, which contaminates the comparison. Both legs receive an
> **identical** prompt scoped to §§1–6 and 8–9. If a leg is exposed to this section, record the
> breach in the probe record as a named deviation rather than discarding it silently — the
> `P-20260717-sol-b20` blinding breach is the precedent for how to write that up.

**Fit line:** `fable · high · architecture/design + wave decomposition (R2 + R13) · surface: fresh
session with model pinned, or the` orchestrator `pin (fable/high) · operator-requested, enumerated
class`.

**Scarcity, stated plainly:** `scarcity-mode` and the fable window **expired 2026-07-19** and read
as **Unchecked** — the fallback column governs by default (R2 → opus xhigh + reviewer gate; R13 →
opus xhigh + reviewer gate on the synthesis). This spawn proceeds on **explicit operator request**
for an enumerated class, which is the sanctioned override. Post-window terms (STATE, valid to
2026-09-08): metered via usage credits at API rates. Reference cost: the June Fable audit in this
repo ran **$4.80**.

**Registered pairing opportunity — read before spawning.** [W-024] claim (d) records that Fable is
cost-dominated by Opus 5 on all three official coding benchmarks while being **unmeasured** on the
judgment work this packet asks for (architecture, decomposition, review). That makes this run a
naturally-arising paired-probe opportunity against R13's fallback (opus xhigh + reviewer gate) at
**zero marginal design cost** — same packet, same reading list, same output contract.

If the operator authorizes the pair, the second leg must be **blind to the first**, the tree frozen,
and the adjudicator **non-author**. If only one leg runs, record it as a single lane with **no
dominance reading licensed** — the `P-20260717-sol-fable-b23` record is the precedent for how to
write that up honestly. Either way this is registration, not authorization: **n=1 never flips a
row** [W-019], and nothing here moves R13.

---

## 8. Out of scope — do not do these

- No implementation, staging, commit, push, install, deploy, or activation.
- **No route flips.** R4 is annotated and probe-registered; R13 and the fable rows are blocked by
  C13 and W-024(d). Vendor evidence is `Concordant`/`Reported`, never `Corroborated`.
- No cleanup or deletion. The mixed worktree is preserved deliberately; the stale
  `codex/delegate-phase1a` worktree stays until its branch is dispositioned.
- No rewriting of historical proposals, reviews, or probe records to make the lineage look cleaner.
- No paid runtime probes (the version-3 Claude profile probe stays parked; C0 stays uninstalled).
- Do not resolve the `explorer` pin question (review D-1) by picking a value — the operator's answer
  was that **the mechanism is wrong**, which is question §4.5, not a value to choose.

---

## 9. Output contract

A durable artifact under `docs/reviews/` or `docs/proposals/` containing:

1. a verdict on the portfolio split (**accept / revise / reject**) with reasoning, and an explicit
   disposition of each R-A…R-F recommendation in §5;
2. an answer to each §4 question, or a statement of what evidence is missing and the cheapest way to
   get it;
3. a decomposition of the next phase: ordered work items, each with owner-class (root / delegated /
   deterministic script), the surface that can actually deliver it, and its exit criterion;
4. a wave design if you recommend one — lanes, tiers, prompt contracts, and the telemetry each lane
   should emit;
5. findings typed as **observed defect / source gap / design risk / stakeholder decision /
   implementation question**;
6. what you could not verify, and what you would need.

Separate what you **observed** from what you **inferred** from what you **recommend**, per
[`EPISTEMICS.md`](../../EPISTEMICS.md). Where you disagree with the root session's review, say so
directly and give the reasoning — that disagreement is the most valuable thing this packet can buy.

---

## 10. Verification performed on this packet

`python3 check_wids.py` → PASS (94 md files, 24 W-records defined and cited).
`python3 check_state.py` → FAIL on four **pre-existing** entries expired 2026-07-19
(`scarcity-mode`, `fable-window-end`, `reviewer-pin`, `orchestrator-pin`) — review defect D-7,
untouched by this pass, and governing §7's scarcity statement.
Adapter suite → 223 tests OK via the exact CI command, after the D-4 import fix.
No commit, stage, deploy, install, activation, or paid model call was made in preparing this packet.
