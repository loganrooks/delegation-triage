---
name: delegation-triage
description: |
  Per-spawn triage for ANY delegation — solo agent, fleet fan-out, or Workflow. Applies the
  delegation test (whether to delegate at all), classifies the task, looks up the model × effort
  route (ROUTES.md), checks volatile state and scarcity mode (STATE.md — expired state reads as
  Unchecked), picks the control surface that can actually deliver the pair, and states + records
  the fit. Warrants (WARRANTS.md) load on demand, never per-spawn.

  TRIGGERS: which model should this agent use, what effort level, delegate this, spawn agents
  for, fan out, plan a workflow's agents, model routing, triage this delegation, fable budget,
  should this be fable/opus/sonnet, roster pick, review gate model, sweep tier.

  Does NOT do: cost forecasting/gating of fan-out SIZE (workflow-prep / the workflow-gate
  plugin — run both for a priced fan-out); editing roster pins or settings (operator approval);
  trusting a UI model label over the transcript.
---

# Delegation Triage

One decision, six steps — full contract in [`CONTRACT.md`](CONTRACT.md):

1. **Whether:** apply the delegation test (CONTRACT §1). No new information channel, no
   parallelism, no isolation need → do it in-session; fixed steps → script.
2. **Classify** the task to a ROUTES row; split delegations that span classes.
3. **Route:** [`ROUTES.md`](ROUTES.md) row → active profile deltas ([`STATE.md`](STATE.md)
   `Active:`) → project overlay (`<repo>/.claude/skill-overlays/delegation-triage.md`; most
   specific wins). Honor the warrant: Contested/Conjecture/CANDIDATE/PARKED rows are probes to
   run, not priors to trust ([`WARRANTS.md`](WARRANTS.md) by W-ID, on demand).
4. **State-check:** scarcity mode + expiry (STATE.md). An expired entry is Unchecked — re-verify
   or take the fallback column. `python check_state.py` makes this deterministic (Cowork-runnable).
5. **Surface:** pick the control surface that can deliver the pair (CONTRACT §3). If the route's
   effort ≠ session effort, a generic spawn is the wrong surface by construction.
6. **Fit + record:** one line per spawn (model · effort + how it arises · surface · class · why,
   citing the row or W-ID); record the outcome; post-mortems edit ROUTES/WARRANTS/STATE in the
   same pass and append to [`probes/`](probes/).
