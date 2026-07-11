# delegation-triage

**Evidence-graded model routing for multi-agent LLM systems — a working instrument, published
with its lab notebook.**

When an orchestrating agent delegates work to subagents, someone has to decide *whether* to
delegate at all, which model × reasoning-effort pair runs each task, and which spawn surface can
actually deliver that pair. This package makes those decisions **auditable**: every routing rule
is a prior backed by a typed evidence record with quoted primary sources, a confidence grade,
and an explicit flip condition — and the routes change only when accumulated, attested probe
outcomes say so.

This is not a framework; it is a live operational instrument (routing Claude-family agents —
fable/opus/sonnet tiers — day to day) whose method is portable: the label vocabulary, the
warrant discipline, and the probe loop work for any model roster.

- **Version:** 0.3.0 (2026-07-10) · **Status:** live — Stage-2 deployed (Claude Code), Cowork
  plugin generated, canonical here per SEAS ADR-0022/0024.
- **Canonicality:** this repo is canonical; every deployed copy is a recorded deployment
  stamped in [`agents/MANIFEST.md`](agents/MANIFEST.md). Drift is diffable, never
  discoverable-by-accident.

## Quickstart

```bash
python3 check_state.py            # volatile-state expiry gate (expired = Unchecked, never true)
python3 check_wids.py             # evidence-record integrity (dangling W-IDs, broken links)
python3 install.py claude-code    # deploy as a Claude Code skill + agent roster (~/.claude)
python3 install.py cowork         # build the Cowork plugin (dist/*.plugin, deterministic zip)
python3 install.py codex          # emit consumer guidance for non-Claude drivers
```

## How to read this repo

One decision, five surfaces, sized by consultation frequency and volatility:

| Surface | Consulted | Holds |
|---|---|---|
| [`ROUTES.md`](ROUTES.md) | every spawn | task class → model × effort route \| fallback \| warrant IDs (≤1 screen) |
| [`STATE.md`](STATE.md) | every spawn | volatile facts: active profile, scarcity mode, windows, prices — each with `valid_until` + re-check trigger. **Expired state reads as Unchecked, never as true.** |
| [`CONTRACT.md`](CONTRACT.md) | onboarding + disputes | the delegation test (whether), control surfaces (how), per-spawn discipline, escalation loop, overlay convention |
| [`WARRANTS.md`](WARRANTS.md) | on demand | typed evidence records W-001…: claim · label + grade + downgrades · resolvable locators with quoted primary excerpts · flip condition · probe tally |
| [`agents/`](agents/) + [`probes/`](probes/) | mint/deploy + post-mortems | canonical roster definitions; the package's own append-only evidence loop |

Supporting files: [`SKILL.md`](SKILL.md) (thin Claude Code procedure wrapper),
[`EPISTEMICS.md`](EPISTEMICS.md) (the label vocabulary — we *corroborate, never verify*),
[`LINEAGE.md`](LINEAGE.md) (provenance), [`ROADMAP.md`](ROADMAP.md) (development path),
[`adapters/`](adapters/) (per-platform packaging behind `install.py`).

**A note on what you'll find in `probes/` and `STATE.md`.** This repo dogfoods its own
methodology, and the evidence is published as recorded — including operational specifics
(model-availability windows, budget stances) and verbatim operator interventions in post-mortem
records. That is deliberate: a claim's reproduction conditions are part of the claim, and a
routing table without its incident history is just opinion. Read `probes/` as a lab notebook,
not documentation.

## The discipline, in one paragraph

Delegate only when the delegation test passes (new information channel, parallelism, or
isolation — otherwise do it in-session; fixed steps → script). Classify the task to a ROUTES
row; honor the warrant (Contested/CANDIDATE rows are probes to run, not priors to trust); check
volatile state (expired = Unchecked → fallback column); pick a spawn surface that can actually
pin the model × effort pair; state the fit in one line before spawning; record the outcome.
Post-mortems edit ROUTES/WARRANTS/STATE in the same pass and append a probe record — **n=1
never flips a route** (≥2 attested concordant is the floor).

## Dogfood block [per the adopting programme's hard core #7/#8; ADR-0022 rider i]

- **P-C (consumer):** every delegation decision in a consuming session reads ROUTES.md + STATE.md
  at first spawn and cites a route row or W-ID in its fit line; the spawn-triage guard (Claude
  Code deployments) reads STATE.md's `Active:` line; the periodic demotion pass consumes
  `probes/INDEX.md`.
- **P-D (disconfirmer):** (a) a 10-spawn post-deployment audit shows drivers consulting ROUTES but
  not WARRANTS when a warrant was decision-relevant, or routing-compliance regressing vs the
  monolith baseline → the layering is wrong; re-merge and record why [proposal P-D1]. (b) two
  consecutive availability events pass with drivers routing on expired STATE entries → the expiry
  mechanism failed; escalate `check_state.py` from convention to enforced gate, or abandon
  [P-D5] — *partially exercised: CI now runs `check_state.py` as a build gate.* (c) one
  work-week of active delegation with no fit line citing a route/W-ID → the package is
  decoration, not an instrument.
- **review-by:** 2026-08-07 — first periodic pass: demotion candidates from probes/INDEX.md,
  expired STATE entries, warrant records whose flip counters moved.

## Lineage and couplings (all read-direction; none load-bearing at consultation time)

Descends from: a living routing table seeded 2026-07-02 and the SEAS `harness/agents/TRIAGE.md`
contract (2026-06-12), reunified per SEAS ADR-0022 and the 2026-07-10 offshoot proposal. The
epistemics vocabulary descends from SEAS `governance/epistemics.md`. Optional feeders: the
external evidence repos named in WARRANTS.md's KNOWN-REPOS key (private) — quoted excerpts (D6)
keep every warrant evaluable without access to them. **Named relocation cost:** moving the
package severs the live evidence feed from those repos; the quoted excerpts freeze the warrant
base and new evidence then comes from `probes/` alone.

## KNOWN-CONSUMERS

- **Claude Code:** `python3 install.py claude-code`, stamp `agents/MANIFEST.md`, restart (roster
  registers at session START). The spawn-triage guard reads the deployed STATE.md.
- **Cowork / sandboxed sessions:** install the generated plugin (`install.py cowork`). The plugin
  ships no volatile state — its skill degrades gracefully: project-side STATE if readable,
  otherwise premium availability is Unchecked → fallback routes.
- **Codex / non-Claude drivers:** `python3 install.py codex` emits the consumer fragment: read
  ROUTES + STATE before delegating to a Claude executor; CONTRACT §3 names which knobs each
  spawn surface can actually pin.

## License

[MIT](LICENSE).
