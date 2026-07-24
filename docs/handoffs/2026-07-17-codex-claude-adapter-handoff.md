# Handoff: Codex-managed Claude delegation proposal

- **Date:** 2026-07-17
- **Audience:** a fresh agent working directly in this repository
- **Current stage:** proposal reviewed and accepted for an implementation-authorization decision
- **Implementation authorized:** no

## Objective

Take over work on the proposed Codex `delegate-to-claude` adapter without relying on chat history.
First review and refine the proposal. Do not implement, install, deploy, call a paid model, or
change routing policy until the operator explicitly authorizes implementation.

Primary artifact:
[`docs/proposals/2026-07-17-cross-runtime-routing-and-claude-delegation.md`](../proposals/2026-07-17-cross-runtime-routing-and-claude-delegation.md).

Cold-read review:
[`docs/reviews/2026-07-17-cross-runtime-routing-proposal-review.md`](../reviews/2026-07-17-cross-runtime-routing-proposal-review.md).
Its initial verdict was `revise` (0 BLOCKER, 5 MAJOR, 2 MINOR, 2 NOTE). All findings were accepted
and addressed. A post-revision audit plus final narrow correction found no remaining Blocker or
Major and gave the effective recommendation `accept for implementation-authorization decision`.

## Repository state and preservation boundary

1. Work from the repository root containing this handoff.
2. Run `git status --short` before editing.
3. A pre-existing modified probe record was present when this handoff was written:
   `probes/records/P-20260717-signal-layer-framing-probe-pair.md`.
4. Treat that file and all other unrelated dirty changes as user-owned. Do not edit, revert,
   reformat, stage, or include them.
5. Do not commit unless the operator explicitly requests a commit.

## Required read order

Read these files exactly before proposing changes:

1. [`CLAUDE.md`](../../CLAUDE.md) — repository workflow and same-pass propagation rules.
2. [`README.md`](../../README.md) and [`ROADMAP.md`](../../ROADMAP.md) — project shape and open work.
3. The [proposal](../proposals/2026-07-17-cross-runtime-routing-and-claude-delegation.md).
4. [`CONTRACT.md`](../../CONTRACT.md), [`ROUTES.md`](../../ROUTES.md), and
   [`STATE.md`](../../STATE.md) — routing and volatile-state contracts.
5. [`WARRANTS.md`](../../WARRANTS.md) and [`EPISTEMICS.md`](../../EPISTEMICS.md) — evidence rules.
6. [`SKILL.md`](../../SKILL.md) — current Claude procedure.
7. [`adapters/codex/README.md`](../../adapters/codex/README.md),
   [`adapters/codex/AGENTS-fragment.template`](../../adapters/codex/AGENTS-fragment.template), and
   [`install.py`](../../install.py) — current Codex boundary and installer.
8. [`LINEAGE.md`](../../LINEAGE.md) — canonical-home decision locators.

If implementation is later authorized, inspect the current CLI locally with non-generative
commands such as `claude --version`, `claude --help`, and `claude agents --help`; do not assume the
2026-07-17 capability observation is still current.

## Decisions already proposed

- Keep this repository as the one canonical home; do not mint a competing central package.
- Use one canonical Claude routing doctrine across host runtimes; keep host-control mechanics in
  runtime-specific adapters and defer any provider-neutral route split.
- Make Codex-managed multiple Claude sessions (Option 3) the primary mode.
- Preserve one Claude-orchestrated session (Option 2) as a later bounded lane-local mode.
- Reuse Claude's canonical `delegation-triage` skill inside each Claude lane.
- Implement fixed-step session management in a deterministic stdlib-only tool.
- Distinguish planned, requested, and observed model/effort.
- Link packet, registry, result, event, and disposition through immutable route-decision,
  lifecycle, and reconciliation identifiers.
- Use only capability-probed write-isolation modes; concurrent writers run in dedicated worktrees
  and undeclared diffs are rejected from integration.
- Distinguish hard spend/runtime enforcement from advisory limits and observation deadlines.
- Treat fake-CLI tests as adapter evidence only; real controls remain Unchecked until a separately
  authorized, dated actual-runtime observation supports them.
- Permit automatic manager termination only for an operator-pre-authorized, capability-probed
  `hard_runtime_limit`; distinguish provider-limit, manager-limit, and interactive termination.
- Require the normative descendant manifest if Option 2 is later enabled.
- Promise cache eligibility only; report cache counters and never guarantee a hit.
- Keep evidence content-free; never feed prompts/transcripts/commands/tool output into routing
  analytics.
- Notify and show drift without silently fetching, installing, or activating policy.
- Keep initial generated state local and bounded; no remote database, Dionysus, or monitor.

These are proposal decisions, not yet accepted implementation authority. Challenge them with
evidence, not preference.

## Review task

Produce a finding-led review that answers:

1. Does the architecture preserve ADR-0024 canonicality and existing route/warrant discipline?
2. Is the Option 2/Option 3 boundary clear and migration-compatible?
3. Can planned/requested/observed route, resume lineage, cache observations, and final disposition
   be reconstructed without storing content?
4. Are permission, spend, timeout, recovery, and concurrent-write boundaries fail-safe?
5. Are policy updates separated from capability/tooling updates and protected from silent
   activation?
6. Are phases independently testable, and is the first implementation slice small enough?
7. Which claims need stronger labels, warrants, capability probes, or explicit stakeholder
   decisions?

Use severities `BLOCKER`, `MAJOR`, `MINOR`, and `NOTE`. Every finding must cite an exact heading or
file location, explain impact, and propose a bounded correction. Include explicit sections for
strengths checked, assumptions, open questions, and a verdict: `accept`, `revise`, `park`, or
`reject`.

## Reviewer output contract

The designated reviewer owns only:

`docs/reviews/2026-07-17-cross-runtime-routing-proposal-review.md`

It must not edit the proposal, this handoff, routing surfaces, installer, adapters, or probe
records. Its return message must contain:

- status;
- artifact path;
- verdict and finding counts by severity;
- key findings;
- assumptions/open questions;
- verification performed;
- risks or conflicts.

## Later implementation boundary

If and only if implementation is authorized, begin with Phase 1 of the proposal:

1. pure packet, route-decision, lifecycle/reconciliation, result, descendant-manifest, and event
   schemas with fake fixtures;
2. read-only `plan --dry-run` consuming those schemas;
3. progressive-disclosure skill and references;
4. installer drift checks and deployment stamps only after dry-run output stabilizes.

Do not begin with live Opus/Sonnet runs or concurrency. Before editing, write a concrete plan with
the exact owned files, tests, generated-state budget, and migration boundary. Use test-first
vertical slices. Until the operator approves a generated-state root and sub-budgets, use only
in-memory/test-runner-owned temporary fixtures and fail closed on persistent-state configuration.
Keep real external calls behind a separate operator-approved smoke-test gate.

## Constraints

- No deletion, movement, installation, network downloads, background monitoring, remote telemetry,
  Dionysus changes, commits, pushes, or paid model calls without explicit authority.
- Keep new generated state for this campaign below 250 MiB; proposal/docs do not count as
  generated runtime state, but test fixtures and logs do.
- Never record prompt text, transcript text, command text, tool output, secrets, credentials, or
  raw hook payloads in telemetry.
- Preserve partial external-model output and diagnose before requesting approval for another paid
  call.
- Do not infer success from silence, a zero cache counter, or an unobserved model label.

## Verification

For proposal/review changes, run from the repository root:

```bash
python3 check_state.py
python3 check_wids.py
git diff --check
```

Also inspect the exact diff and confirm that the pre-existing probe record is unchanged by this
work. When implementation begins, add deterministic unit/integration checks appropriate to each
new stdlib module before claiming a phase complete.

## Current open decisions

The operator must decide before implementation:

- generated-state root and the initial sub-budget allocation within the `<250 MiB` campaign cap;
- whether any real paid-model smoke tests are authorized and their maximum spend/run count;
- whether explicit termination belongs in the first manager release;
- whether Option 2 is part of the first public milestone or deferred through Phase 4.

If no operator response is available, preserve these as open; do not choose silently.
