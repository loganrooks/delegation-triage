# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

The canonical home of the `delegation-triage` package: evidence-graded routing doctrine for
delegating work to subagents (model × effort routes), the canonical agent roster, and the
package's own evidence loop. It is almost entirely Markdown plus stdlib-only Python scripts
(two checks + a multi-target installer). No dependencies, no test framework — the checks below
are the CI. `dist/` is generated output (untracked).

## Commands

```bash
python3 check_state.py                  # fail (exit 1) on any expired STATE.md entry or a missing/unbolded **Active: <profile>** line
python3 check_state.py --today 2026-07-12   # simulate a date (e.g. test a scheduled expiry)
python3 check_wids.py                   # fail on dangling W-IDs, broken relative md links, or absolute/user-specific paths used as dependencies
shasum -a 256 agents/*.md               # re-hash roster definitions for agents/MANIFEST.md stamps
python3 install.py claude-code          # deploy to ~/.claude (then stamp MANIFEST + restart); --check diffs deployed vs canonical
python3 install.py cowork               # build dist/delegation-roster-<ver>.plugin (deterministic zip; install via Cowork UI)
python3 install.py codex --dest PATH    # emit the consumer guidance fragment (no --dest: stdout)
```

Run both checks before committing any edit to the package's Markdown surfaces.

## Architecture — one decision, five surfaces

The package splits one decision (how to route a delegation) across surfaces sized by
consultation frequency × volatility:

- **`ROUTES.md`** — consulted every spawn. Task class → model × effort route | no-fable fallback |
  warrant IDs. Plus profile deltas (`balanced` / `budget-conscious`). Kept ≤1 screen.
- **`STATE.md`** — consulted every spawn. Volatile facts (active profile, scarcity mode, windows,
  prices), each row with `valid_until` + re-check trigger. **An expired entry reads as Unchecked,
  never as true.** The bold `**Active: <profile>**` line is a format contract — the deployed
  spawn-triage-guard hook parses exactly `\*\*Active:\s*([\w-]+)\*\*` and silently defaults to
  `balanced` otherwise; `check_state.py` enforces its presence.
- **`CONTRACT.md`** — onboarding + disputes. The delegation test (§1 whether to delegate at all),
  control-surface table (§3 — which surfaces can actually pin model/effort), fit-line discipline
  (§4), overlay convention (§5), escalation/feedback loop (§6).
- **`WARRANTS.md`** — load on demand, never per-spawn. Typed evidence records `W-001`…: claim ·
  label + grade + downgrades · resolvable locators with quoted primary excerpts · flip condition ·
  probe tally. Record headers must match `### W-NNN ` — that's how `check_wids.py` finds
  definitions. External repos are cited via the KNOWN-REPOS prefix key (e.g. `bridgewright:path`),
  never absolute paths.
- **`agents/` + `probes/`** — mint/deploy + post-mortems. Canonical roster definitions and the
  append-only evidence loop.

`SKILL.md` is the thin Claude Code procedure wrapper; `EPISTEMICS.md` carries the label
vocabulary (Resolved / Concordant / Reported / Corroborated / Provisional / Conjecture /
Contested / Unchecked) so records stay interpretable if the package relocates. `LINEAGE.md`
records provenance (SEAS ADR-0022/0024). `adapters/` holds per-platform packaging (Claude Code
install, Cowork plugin, Codex consumer notes); the core stays platform-agnostic.

## Canonicality and deployment model

Definitions in THIS repo are canonical; every deployed copy (`~/.claude/`, the Cowork plugin,
etc.) is a recorded deployment stamped in `agents/MANIFEST.md` with a sha256 content hash.
Deploy = copy + manifest stamp + **session restart** (roster definitions register only at session
start — a deploy without a restart is a silent no-op). Manual install steps:
`adapters/claude-code/INSTALL.md`. After editing any `agents/*.md`, re-hash and update the
manifest table in the same commit.

## Editing discipline (the rules the surfaces themselves impose)

- **Same-pass propagation:** a post-mortem or probe outcome edits the affected surface
  (ROUTES row, W-record grade/flip counter, STATE entry) AND appends a `probes/records/` file AND
  updates `probes/INDEX.md` in one pass. Surfaces must never lag the records.
- **Probe records** (`probes/TEMPLATE.md`): only two fields are required — `attestation:` (how
  the outcome is verifiable; `self-reported` is allowed but tallied separately) and `tally:`
  (which W-record flip counter this feeds + count after this record). Everything else is
  requested, not enforced.
- **Flip discipline:** n=1 never flips a route row; ≥2 attested concordant is the floor;
  flip-prone classes accumulate ~3 per side. `probes/records/` is the source of truth on any
  discrepancy with INDEX counts.
- **Warrant records:** supersede in place; every load-bearing record states its flip condition;
  a vendor/model-card number is Concordant/Reported, never Corroborated; a bare grade with no
  downgrade reasoning is non-compliant (see `EPISTEMICS.md`).
- **STATE table format:** `check_state.py` locates the table by its `| key | value | valid_until`
  header and finds `valid_until` by header name — keep that header intact; config rows use an
  em-dash in `valid_until` to be exempt. A window extension is a one-line `valid_until` update.
- **No user-specific paths** in package files outside the WARRANTS KNOWN-REPOS "local hint"
  column and STATE/probes provenance cells — `check_wids.py` flags them. `references/ARCHIVE`
  and `references/routing-table.md` are exempt from W-ID/link checks (archives + stubs).
- **Profile ↔ pin coupling:** a profile delta that changes a pinned route also needs the pin's
  frontmatter edited — flip both in one commit.
- Known open items live in `STATE.md` (Scheduled items) and `agents/MANIFEST.md` (e.g. the
  unreconciled Cowork-plugin fork); check both before touching roster or scarcity entries.
