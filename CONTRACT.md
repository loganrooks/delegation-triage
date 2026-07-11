# CONTRACT — the triage contract (whether → who → how → record → learn)

Governs any orchestrating session that delegates work. Every assignment is a prior with a basis
and a disconfirmer, not a fact. The routing priors live in ROUTES.md; the volatile config in
STATE.md; the evidence in WARRANTS.md; outcomes feed probes/.

## §1 The delegation test — when NOT to delegate (decide *whether* before *who*)

Delegate only if at least one holds [W-021]:

- **(a) New information channel** — fresh context, independent judgment, or a lens the
  orchestrator cannot hold itself (the review-gate case). A delegated network that adds no new
  exogenous information is dominated by deciding centrally.
- **(b) Parallelism** across genuinely independent legs.
- **(c) Context/cost isolation** — the work would pollute or bloat premium context.
- **(d) Tool/permission isolation** — read-only enforcement, sandboxing.

Otherwise: do it in-session. **Fixed-step transformations prefer scripts over agents** [W-021].
This subsumes class-matching: the roster answers "who"; this test answers "whether."

## §2 Classify, route, and honor the warrant

Match the task to a ROUTES row (split delegations that span classes — never split the
difference). Take model × effort from the row, apply the active profile's deltas (STATE.md
`Active:`), then the project overlay (§5). Read the cited W-record when the decision is
close or the row is marked Contested/Conjecture/CANDIDATE/PARKED — those are probes to run
(paired, identical harness, diff the yield), not priors to trust.

## §3 Pick the control surface that can deliver the pair

This is where delegations silently go wrong. Surfaces, by what they can actually pin:

| Surface | model | effort | Use |
|---|---|---|---|
| Workflow `agent()` | per-call | per-call | the ONLY per-call surface for both knobs; promote to a Workflow when no pin matches a non-default pair |
| Roster pin (`agents/`) | frontmatter | frontmatter | immune to session effort; prefer when a pin matches |
| Generic Agent tool | per-call | **INHERITED from session** | acceptable only when session effort ≈ route effort — otherwise the wrong surface *by construction* (observed firing 2026-07-10: intended fable/high ran at session-inherited xhigh) |

Rules: never assume a generic spawn's effort; fit lines state effort **as delivered by the
surface**, not as intended. In Cowork, only generic surfaces exist — say "effort:
session-inherited" per spawn. Hazards (measured): SendMessage-resume drops the spawn-time model
override and rebills on the session model — prefer relaunch + transcript-mining. UI model labels
can mislead; the transcript JSONL is ground truth
(`grep -oE '"model":"claude-[^"]*"' <task-output.jsonl> | sort | uniq -c`).

A deployed PreToolUse guard (Claude Code only) enforces the single invariant "a decision was
made": explicit models and pinned types pass silently; a pinless, model-less spawn gets an
overridable prompt when it would inherit a premium session model (always, under
budget-conscious). It reads STATE.md's `Active:` line; it never second-guesses an explicit
choice; fail-open on internal error.

## §4 State the fit; record it; scarcity-check it

One line per spawn, in the visible plan BEFORE the call: **agent/type · model · effort (+ how the
effort arises: pin vs inheritance vs per-call) · surface · task class · one-line why citing the
ROUTES row or W-ID.** Check STATE.md's scarcity mode: in fable-window, a fable spawn must be an
enumerated class AND pass the durable-artifact test (output outlives fable access); expired STATE
= Unchecked (re-verify or take the fallback). Record the spawn (model, effort, type, harness,
task class, tokens if observable, outcome proxy, **and the router: the deciding driver's own
model/surface** — routing competence is model-conditional and un-audited until it's recorded) —
where an observability layer exists it records automatically; the visible statement is still
required (it is the decision-surfacing mechanism; the ledger is the audit trail).

## §5 Overlay convention (reused mechanism, not a new surface)

A consuming project may carry `<repo>/.claude/skill-overlays/delegation-triage.md` with
project-local pins, task classes this table lacks, and project-scoped probes. **Most specific
source wins: overlay > profile > ROUTES.** Overlay rows carry the same discipline — warrant grade
+ flip condition — and post-mortems update the overlay for project classes, this package for
general ones.

## §6 Escalation and feedback (mismatch is signal, not noise)

1. **Too hard** — BLOCKED, or output grades low: re-delegate one tier up
   (light → standard → generic-with-justification) and LOG the mismatch (task descriptor, agent,
   signal) to probes/. `BLOCKED: <what> | NEED: <input> | TRIED: <attempts>` is a triage
   *success* — honest refusal beats confident overreach.
2. **Too easy** — trivial completion, tokens ≪ class norm, no judgment exercised: note it; the
   next task of this shape goes one tier down. Over-provisioning never announces itself — it must
   be queried for.
3. **Mis-shaped** — BLOCKED citing missing decisions on a task triaged as mechanical: the defect
   is the task description or ROUTES, not the agent. Fix the contract, log the intervention.
4. **Roster amendments are supersessions:** edit the canonical definition in `agents/`, re-deploy
   (manifest stamp), restart, record basis + disconfirmer. Definitions are versioned precisely so
   assignment history is reconstructable next to outcome history.
5. **Split condition (for the package itself):** one procedure + one route table serves solo
   spawns, fleets, and Workflows because the decision structure is identical. Split a
   `workflow-triage` sibling only if workflow-specific knowledge (budget loops, resume semantics,
   schema design) outgrows its place here — the split is cheap then. (Migrated from the
   predecessor table; review lens 2 F10.)
6. **Post-mortems and probe outcomes edit the affected surface in the same pass** — ROUTES row,
   W-record (grade, flip counter), STATE entry — and append a probes/ record. The surfaces must
   never lag what the ledger shows. Handoff/contract route prescriptions are checked against
   ROUTES at FIRST spawn; on conflict, surface both sources and state which governs before
   spawning (route-rule-inheritance guard, probes/KNOWN-WEAKNESSES.md).
