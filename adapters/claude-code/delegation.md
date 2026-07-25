# Subagent Delegation

Frame: capability belongs to the **agent-harness-task system**, not to a model as a substance with
fixed properties. A delegation decision is a system design — model × effort × harness (prompt
contract, skill, roster pin, review gate) × task. State the fit in one line per spawn; record it
(see Instrumentation) so capability questions are answered later from artifacts, not impressions.

## Routing — one authority, no copies

**All model × effort routing lives in the `delegation-triage` skill — load it for ANY spawn
decision.** Per-spawn surface = its `ROUTES.md` + `STATE.md` (active profile · scarcity mode;
expired state reads as Unchecked); contract = `CONTRACT.md`; evidence = `WARRANTS.md` +
`probes/`, load-on-demand. Canonical home: the `delegation-triage` repo (local hint: ~/Projects/delegation-triage); the
skill dir AND this file are stamped deployments — see its `agents/MANIFEST.md`. Post-mortems update THOSE surfaces in the
same pass, never this file.

**This file deliberately carries NO route values** (which model reviews, which effort
implements, when fable). It used to — and they drifted from the table within days [per:
propagation]. If you are reading a model name here to make a spawn decision, something is wrong:
load the skill.

Stable spawn discipline (mechanism, not values):
- Prefer the minted roster pins (`~/.claude/agents/`) over generic spawns — generic spawns
  inherit session effort (observed live 2026-07-10: an intended fable/high orchestration ran at
  session-inherited xhigh through the generic Agent tool). If the route's effort ≠ session
  effort, the pin or a per-call `{model, effort}` surface (Workflow `agent()`) is the only
  correct delivery; pins register at session START.
- Tier escalation is evidence-driven: cheaper-tier output failing review, high/irreversible
  blast radius, or operator request — never task prestige.
- Top-tier effort needs a stated reason; when unsure, take the cheaper tier under the stronger
  harness and record the outcome — that is the experiment.

## Verification rules (operator rulings, 2026-07-24)

- **Decisions get a review spread first:** anything needing an operator decision goes through
  an independent review panel (≥2 legs, distinct lenses, cross-vendor where the fleet affords
  it, structured verdicts) BEFORE it reaches the operator — surface the five-point decision
  WITH the spread and your adjudication attached. Disclose any leg's conflict of interest.
  Trivially-reversible or time-critical calls may skip; say so.
- **Evidence graded from a sample gets an adversarial remainder-read:** a warrant/evidence
  record whose source you sampled rather than exhausted gets a delegated deep-read leg over
  the unread remainder before (or immediately after) the grade lands. First exercise caught a
  half-quote, a mis-scope, and a phrase overclaim in one record.

## Instrumentation (standing)
- Record per spawn: model, effort, agent type, harness/skill in play, task class, outcome proxy
  (survived review? output used or discarded?).
- **Paired probes:** when a fan-out has a naturally duplicable lane, run it at two tiers under the
  IDENTICAL harness and diff the yield. "Harness offsets tier" is a hypothesis we measure in our
  setting, not a premise imported from benchmark-scoped literature.
- **Registered open question (not for now):** can fable AUTHOR the contract/harness — goal
  contracts, workflow scripts, review rubrics — and have non-fable executors deliver fable-grade
  results? Every fable review gate and contract-driven run is data for this: keep verdicts,
  per-finding dispositions, executor + reviewer identity, and contract hashes durable and greppable.

## Prompt contract for research agents
Every delegated research prompt MUST include:
- Today's date, and: "do not rely on training data for anything post-cutoff — search and verify."
- Claim tagging: every claim marked **[CONFIRMED — URL]**, **[REPORTED — URL]**, or **[UNCERTAIN]**;
  shipped vs announced vs rumored separated explicitly.
- For local-file exploration: a source file path (and short quote) for every claim.
- Output bounds (e.g., 1200–2500 words, structured by numbered points). A closing
  "N strongest implications, in your judgment" section ONLY for synthesis/review-tier agents —
  explorer-tier agents (explorer, explorer-light) report facts plus follow-up pointers
  (control readings), never judgments, verdicts, or recommendations (operator correction
  2026-07-10).
- Beware SEO/AI-content sites; check sensational specifics against primary sources.

## Process
- Launch independent agents **in parallel in one block**; don't re-run their searches yourself.
- SendMessage is exposed (verified 2026-07-02); still design delegations self-contained by default —
  continue an agent only when its accumulated context genuinely carries value.
- Treat subagent output as *Reported, not verified*: spot-check load-bearing claims against
  primary sources (fetch them) before building on them.
