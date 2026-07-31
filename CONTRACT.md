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

### §3a Does the work need to TALK BACK? (added 2026-07-25)

The table above answers *which knobs a surface can pin*. This one answers a question that
precedes it — **how many times does information need to cross between you and the delegate?**
Get this wrong and the model/effort pin is irrelevant.

| Shape | Surface | Signature |
|---|---|---|
| One question, one answer | **plain subagent** (Agent tool) | reports to the parent only; no cross-talk; own file under `<session>/subagents/` |
| You steer, it works, it never answers | **one-way SendMessage** to a named background agent | `SendMessage` out, no reciprocal `agentName` traffic back |
| Two roles iterate to convergence | **agent team** | shared `teamName`, reciprocal messaging, each teammate owns a top-level session file with `agentName` set |
| Fixed control flow over N items | **Workflow** | deterministic loops/fan-out; per-call `{model, effort}`; resumable by `runId` |

**Chose a team? Load the `agent-teams` skill** — sizing, the convergence signature, lifecycle
costs, and the paired-lane pattern live there, kept out of this file because genuine team use is
rare (measured below) and would otherwise tax every spawn decision.

**Measured base rates** (corpus scan 2026-07-25, this account, 3,122 transcripts —
verified independently, not relayed): **47 files** contain a `SendMessage` call; only
**~5 distinct `teamName` lineages** exist corpus-wide. So the *majority* of SendMessage traffic
is row 2, not row 3 — one-way steering that resembles a team and is not one. An explorer
grepped every steer-target name as a potential message SENDER and got zero hits.

**Why the distinction is worth a row:** the most available error here is not picking the wrong
surface, it is **believing you are running a team when you are running a steered subagent** —
you get none of the iteration benefit and pay the coordination overhead anyway. Discriminate
mechanically, not by intent: teammates have `teamName` + `agentName`; plain subagents live
under `subagents/` with neither.

**Hazards that change the choice, all measured:**
- **`TaskStop` is irreversible.** A stopped teammate cannot be resumed by SendMessage, only
  respawned with reconstructed context. Observed cost: a failed reviewer respawned ~25s later
  with its brief rebuilt from scratch (2026-07-25, chatgpt-cli).
- **External cutoff kills lead and teammates together.** An account usage limit ended one
  audiobookify team-lead session mid-task with a teammate's fix unlanded; the limit text is the
  last line of both transcripts. Long team runs need checkpointing, not optimism.
- **Teams require `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`.** Verify before designing around
  them.
- **Team identity is not stable and the docs overstate cleanup.** Membership state lives at
  `~/.claude/teams/<teamName>/config.json`; dirs outlive their sessions, a team can outlive its
  own lead session's transcript entirely, and `teamName` has been observed changing mid-session.
  Never build on `teamName` stability — read the config dir. Detail in `agent-teams`.

A deployed PreToolUse guard (Claude Code only) enforces the single invariant "a decision was
made": explicit models and pinned types pass silently; a pinless, model-less spawn gets an
overridable prompt when it would inherit a premium session model (always, under
budget-conscious). It reads STATE.md's `Active:` line; it never second-guesses an explicit
choice; fail-open on internal error.

### §3b Who owns the authoritative artifact? (added 2026-07-27)

Choose this before launch, together with the surface:

| Deliverable | Authoritative owner | Transport | Root integration |
|---|---|---|---|
| One durable review/report from one delegate | delegate | verbatim materialization, or one exact owned path | finding-ID delta ledger only |
| Direct implementation | delegate | owned checkout/worktree | inspect diff + verify |
| Synthesis across multiple independent artifacts | root | preserve each source artifact first | synthesis is the named deliverable |

A reviewer owns the full review; the root owns whether to accept it. Do not turn that separation
into two copies of the same prose. The root ledger contains only `accept`, `qualify`, `park`, or
`reject`, plus new evidence, disagreement, or integration action. Never ask a reviewer to write the
root's disposition.

For a read-only worker, prefer a harness that materializes the successful structured result
verbatim. For direct authorship, expose no broader write surface than one exact artifact or isolated
output directory. If the available surface cannot preserve a required durable artifact within the
authorized boundary, change the surface or keep the task at root.

## §4 State the fit; record it; scarcity-check it

One line per spawn, in the visible plan BEFORE the call: **agent/type · model · effort (+ how the
effort arises: pin vs inheritance vs per-call) · surface · task class · one-line why citing the
ROUTES row or W-ID.** For a durable delegated artifact, append **artifact owner · transport ·
integration mode**. Check STATE.md's scarcity mode: in fable-window, a fable spawn must be an
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
7. **Independent-verification rules (operator rulings 2026-07-24, both first-exercised same
   day):** (a) *decisions get a review spread first* — anything needing an operator decision
   runs through an independent panel (≥2 legs, distinct lenses, cross-vendor where the fleet
   affords, structured CONCUR/CONCUR_WITH_CHANGES/OBJECT verdicts, conflicts disclosed) before
   surfacing; the operator receives the five-point decision + spread + adjudication
   (first exercise: `docs/reviews/2026-07-24-decision-panel-adjudication.md` — 4 MAJOR spec
   errors caught pre-ratification). (b) *sampled evidence gets a remainder-read* — a W-record
   graded from a partial read of its source gets a delegated adversarial deep-read of the
   unread remainder before (or immediately after) the grade lands; supersede-in-place on
   findings (first exercise: W-025 amendment — half-quote, mis-scope, phrase overclaim).
   Skips allowed for trivially-reversible or time-critical calls, stated.
8. **North-star alignment lens (operator ruling 2026-07-24):** every review panel (§6.7a) and
   every decision surfaced to the operator includes an explicit **commons-alignment check**
   against the evidence-commons north star's design commitments (its §7) and worldings —
   "does this move toward or away from the vision; does it foreclose any worlding?" Decisions
   predating the north star (committed 2026-07-24) get re-reviewed under this lens on next
   touch. The worldings grounding rule is the test: a design element serving no worlding is
   suspect; a worlding no element serves marks a gap. *(Clarified 2026-07-27, D-NS-1:
   running this check is mandatory; the worlding's verdict is not a veto. A foreclosure
   finding obliges the panel to explain, name who loses what, and either revise or record
   the tradeoff — per the north star's four-status separation, worldings are design probes,
   status 4. The B-3 panel's practice was exactly this; this sentence is the documented
   authority it lacked.)*
9. **Project-originated orchestration friction:** preserve the project and artifact locator in a
   probe record and include a Signal Layer observation ID when one exists. A human-approved
   contract amendment may land from one strong incident, but it remains reversible and receives a
   later outcome check. Do not query raw signal stores or change routing automatically per spawn.

## Prompt contract for delegated agents (migrated 2026-07-25)

*Was in `~/.claude/delegation.md`, always-loaded. Moved here on the doctor pass
because it applies only at spawn time — the one moment this skill is already
loaded. If a spawn goes out without it, that is a load-failure worth recording,
not a style lapse: it is what makes a delegated result auditable instead of
merely believable.*

Every delegated research prompt MUST include:

- **Today's date**, and: "do not rely on training data for anything post-cutoff —
  search and verify."
- **Claim tagging**, every claim marked **[CONFIRMED — URL or path:line + short
  quote]**, **[REPORTED — source]**, or **[UNCERTAIN]**; shipped vs announced vs
  rumored separated explicitly. This is the clause that earns the delegation:
  tagged output can be spot-checked in one command without redoing the work.
- **A source file path (and short quote) for every claim**, for local-file
  exploration.
- **Output bounds** (e.g. 1200–2500 words, structured by numbered points). A
  closing "N strongest implications, in your judgment" section ONLY for
  synthesis/review-tier agents — explorer-tier agents (explorer,
  explorer-light) report facts plus follow-up pointers (control readings), never
  judgments, verdicts, or recommendations (operator correction 2026-07-10).
- **A warning about SEO/AI-content sites**; check sensational specifics against
  primary sources.

**One defect this contract does not yet cover** (observed 2026-07-25,
chatgpt-cli): *the reviewee wrote the reviewer's brief.* A cross-vendor review
of my own proposal was framed by me — I chose which inferences to flag as weak
and which files to point at. It still found what I did not want found, so it was
not worthless, but a review whose brief is curated by its subject is not
structurally independent. Where the stakes justify it, route the brief unfiltered
or have a third party write it.

### Process (migrated with the above)

- Launch independent agents **in parallel in one block**; don't re-run their
  searches yourself.
- SendMessage is exposed (verified 2026-07-02); still design delegations
  self-contained by default — continue an agent only when its accumulated
  context genuinely carries value. `TaskStop` is irreversible: a stopped
  teammate cannot be resumed, only respawned with reconstructed context.
- Treat subagent output as *Reported, not verified*: spot-check load-bearing
  claims against primary sources (fetch them) before building on it.
