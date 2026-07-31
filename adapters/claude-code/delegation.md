# Subagent Delegation — pointer

Frame: capability belongs to the **agent-harness-task system**, not to a model as a substance
with fixed properties. A delegation decision is a system design — model × effort × harness
(prompt contract, skill, roster pin, review gate) × task. State the fit in one line per spawn
and record it, so capability questions are answered later from artifacts, not impressions.

**Everything operative lives in the `delegation-triage` skill. Load it for ANY spawn
decision** — routing (`ROUTES.md`), active profile and scarcity mode (`STATE.md`), the
procedure, prompt contract, verification rules and instrumentation (`CONTRACT.md`), evidence
(`WARRANTS.md` + `probes/`). Canonical home: the `delegation-triage` repo (local hint:
`Projects/delegation-triage` under the home dir); the skill dir AND this file are stamped
deployments — see its
`agents/MANIFEST.md`. Post-mortems update the SKILL's surfaces in the same pass, never this
file.

**This file deliberately carries NO route values, no prompt-contract clauses, and no
verification rules.** It used to carry route values and they drifted from the table within
days [per: propagation]; on 2026-07-25 the prompt contract, verification rules, and process
notes moved into `CONTRACT.md` for the same reason — a second copy is a second thing to
drift. If you are reading a model name, an effort level, or a prompt clause *here* to make a
spawn decision, something is wrong: load the skill.

## The one thing that must be true before you load anything

Spawning any subagent, teammate, or Workflow → **load `delegation-triage` first.**

Generic spawns inherit session effort (observed live 2026-07-10: an intended fable/high
orchestration ran at session-inherited xhigh through the generic Agent tool). If the route's
effort ≠ session effort, a roster pin (`~/.claude/agents/`) or a per-call `{model, effort}`
surface is the only correct delivery; pins register at session START.
