# ROADMAP — development path

Compiled from commitments the package's own surfaces state; each item cites its source. The
surfaces govern on any divergence. (Maintainer working drafts live in an untracked `.planning/`;
anything decision-bearing graduates into a committed surface — this file is the public index of
that path.)

## Near-term (window close)

1. **2026-07-12 — reviewer pin flip** (SEAS ADR-0022 D3, first exercise of the scheduled-flip
   mechanism): `agents/reviewer.md` fable → opus at the fable-window close; scarcity mode →
   no-fable; ROUTES fable rows re-checked in the same pass; recorded in `probes/` as an
   availability event. *(STATE.md, Scheduled items.)*
2. **Orchestrator pin post-window adjudication** — only the reviewer pin was adjudicated; until
   this lands, expired = route on R13's fallback. *(STATE.md; agents/MANIFEST.md.)*
3. **Cowork surface swap** — install the generated 0.3.0 plugin (replaces the recorded
   unreconciled 0.2.x fork), stamp the deployment. *(agents/MANIFEST.md.)*

## Periodic / dated

4. **2026-08-07 — first periodic pass:** demotion candidates from `probes/INDEX.md`, expired
   STATE entries, warrant records whose flip counters moved. *(README dogfood block.)*
5. **2026-09-01 — sonnet re-price:** update `price-sonnet-5`, re-check budget-conscious deltas'
   economics. *(STATE.md, Scheduled items.)*

## Open probes (accumulate evidence; flip only per W-019 discipline)

- R5 implementer-light demotion opus-high → sonnet: **1/3**. *(probes/INDEX.md)*
- R6 sweeps sonnet→opus re-tier: misses 0/2 (flip at ≥2 of next 5); medium revert 0/1. *(probes/INDEX.md)*
- W-001 review-gate demotion fable→opus: Contested — needs ≥2 clean concordant unconfounded. *(probes/INDEX.md)*
- W-010 sonnet composition demotion: opens on a definitions-fixed re-run ≥ parity. *(probes/INDEX.md)*
- R15 advisor: local probe owed, incl. a high-vs-xhigh pair. *(ROUTES.md)*
- R9 / R12 / R14: CANDIDATE or avoid-pending-probe, unadjudicated; R11 PARKED. *(ROUTES.md)*

## Deferred-until-triggered (recorded do-less decisions — not built early)

- records→INDEX counter consistency script: waits for first observed drift. *(probes/INDEX.md)*
- `quality-max` profile: define when first needed. *(ROUTES.md)*
- `workflow-triage` sibling split: only if workflow-specific knowledge outgrows CONTRACT. *(CONTRACT §6.5)*
- Full probe-record schema enforcement: waits for a logged failure a schema would have caught. *(probes/README.md)*

## Done

- 2026-07-10 — Stage-2: canonical repo minted; Claude Code deployment; guard re-pointed.
- 2026-07-10 — Cowork fork diffed and reconciled by rebuild; `advisor` adopted canonically (R15).
- 2026-07-10 — Stage-3 adapters: multi-target `install.py` (claude-code | cowork | codex);
  0.3.0 plugin generated from canonical.
- 2026-07-10 — public GitHub mint: MIT, CI (checks as build gate — P-D5 partially exercised),
  tag-driven releases.

## Standing disconfirmers (can kill the design — watched, not scheduled)

The P-D items in the README dogfood block: layering audit (P-D1), expired-state routing events
(P-D5), and the decoration test (one work-week with no fit line citing a route/W-ID).
