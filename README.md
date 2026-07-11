# delegation-triage — routing doctrine, roster, and evidence loop (relocatable package)

**Version:** 0.1.0-stage1-draft (2026-07-10) · **Status:** DRAFT — Stage-1 content redesign;
not deployed; the live surfaces it will replace remain authoritative until Stage-2 ratification.
**Canonicality:** once deployed, this package is canonical wherever it lives; every deployed copy
(`~/.claude/`, any repo) is a recorded deployment under `agents/MANIFEST.md`.

One decision, five surfaces, sized by consultation frequency and volatility:

| Surface | Consulted | Holds |
|---|---|---|
| [`ROUTES.md`](ROUTES.md) | every spawn | task class → route \| fallback \| warrant IDs (≤1 screen) |
| [`STATE.md`](STATE.md) | every spawn | volatile facts: active profile, scarcity mode, windows, prices — each with `valid_until` + re-check trigger. **Expired state reads as Unchecked, never as true.** |
| [`CONTRACT.md`](CONTRACT.md) | onboarding + disputes | the delegation test (whether), control surfaces (how), per-spawn discipline, escalation loop, overlay convention |
| [`WARRANTS.md`](WARRANTS.md) | on demand | typed evidence records W-001…W-021: claim · house label + grade + downgrades · resolvable locators with quoted primary excerpts · flip condition · probe tally |
| [`agents/`](agents/) + [`probes/`](probes/) | mint/deploy + post-mortems | canonical roster definitions; the package's own append-only evidence loop |

[`SKILL.md`](SKILL.md) is the thin procedure wrapper (Claude Code integration);
[`EPISTEMICS.md`](EPISTEMICS.md) carries the label vocabulary so warrant records stay
interpretable if the package relocates. [`check_state.py`](check_state.py) fails on expired
state; [`check_wids.py`](check_wids.py) fails on dangling W-IDs / broken internal links.

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
  [P-D5]. (c) one work-week of active delegation with no fit line citing a route/W-ID → the
  package is decoration, not an instrument.
- **review-by:** 2026-08-07 — first periodic pass: demotion candidates from probes/INDEX.md,
  expired STATE entries, warrant records whose flip counters moved.

## Lineage and couplings (all read-direction; none load-bearing at consultation time)

Descends from: the `~/.claude/skills/delegation-triage/` living routing table (seeded 2026-07-02)
and the SEAS `harness/agents/TRIAGE.md` contract (2026-06-12), reunified per SEAS ADR-0022 and
`proposals/2026-07-10-delegation-triage-offshoot.md`. The epistemics vocabulary descends from SEAS
`governance/epistemics.md`. Optional feeders: SEAS observability ledgers and the external evidence
repos named in WARRANTS.md's KNOWN-REPOS key — quoted excerpts (D6) keep every warrant evaluable
without them. **Named relocation cost:** moving the package severs the live evidence feed from
those repos; the quoted excerpts freeze the warrant base and new evidence then comes from
`probes/` alone.

## KNOWN-CONSUMERS

- **Claude Code:** load as a skill (SKILL.md wrapper); roster deploys to `agents/`; the
  spawn-triage guard reads STATE.md. Roster changes register at session START — deploys require a
  restart to take effect. Deploy via `python3 install.py claude-code` (also: `cowork` builds the
  plugin, `codex` emits the consumer fragment; every deploy stamps `agents/MANIFEST.md`).
- **Cowork / sandboxed sessions:** user-level skills and roster pins do not load; read
  ROUTES/STATE/CONTRACT as project files, run `check_state.py` from the shell, and state per spawn
  that generic-spawn effort inherits the session (CONTRACT §3).
- **Codex / non-Claude drivers:** read ROUTES + STATE before delegating to a Claude executor;
  CONTRACT §3's surface table names which knobs each surface can actually pin.
