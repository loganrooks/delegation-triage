# Fable correction-audit packet

You are the independent correction auditor for a user-level Claude delegation policy and its
first implementation plan. Your report will decide whether implementation may begin and what must
change first. Review as a product architect, execution-policy/security reviewer, CLI/runtime
integrator, test strategist, and demanding operator of agentic development systems.

Use the repository files directly. You have read-only file tools, a bounded set of read-only shell
commands, and selected codebase-memory query tools. Do not edit any file, commit, install, delete,
move, download, access the network, launch another model, create descendants, or change runtime
configuration. Repository tests may create only their existing bounded temporary state. You are
not being asked to write the artifact directly: emit the full report as the final response and the
orchestrator will materialize it.

This is a paid external Fable audit. Spend judgment on contradictions, missing cases, and product
quality rather than restating the packet. Do not reproduce this prompt. Do not provide hidden
reasoning or process narration. Quote sparingly; cite narrow file sections, symbols, tests, or line
locations. If a requested check is unavailable, label the limitation and continue with the most
useful partial audit. Do not request or launch a follow-up paid run.

## Decision need

Determine whether proposal revision 3 and the C0 contract-core implementation plan are coherent,
complete enough, appropriately scoped, and safe to implement without creating a policy model that
will constrain or destabilize later cohorts. Return one of: `APPROVE C0`, `REVISE THEN IMPLEMENT`,
or `RETHINK ARCHITECTURE`.

The proposal hash under review is
`bbb76fb05c5e298ebf044220c0f2a4cf72132505c4c98adce60c02ab00a6335e`.
The plan hash under review is
`3d860d04b012fe32be7444a5b33e64dc2005d89fd9e5265090bc735520b73f61`.
Verify these before relying on the packet. If either differs, report the observed hash prominently
but continue against the files present.

## Required inputs

Read at minimum:

1. `docs/proposals/2026-07-20-composable-claude-capability-and-scope-policy.md`
2. `docs/superpowers/plans/2026-07-20-composable-claude-policy-contract-core.md`
3. `docs/reviews/2026-07-20-composable-claude-capability-and-scope-policy-review.md`
4. `docs/proposals/2026-07-19-capability-based-claude-execution-profiles.md`
5. `docs/superpowers/plans/2026-07-19-capability-based-claude-profiles-corrective.md`
6. `probes/records/P-20260720-claude-profile-actual-runtime.md`
7. `README.md`, `CONTRACT.md`, and `EPISTEMICS.md`
8. The current candidate under `adapters/codex/delegate-to-claude/`, focusing on policy/profile,
   runner, reconciliation, state-budget, and integration-test surfaces relevant to C0 boundaries.

The existing Sol review is context, not an answer key. Check whether revision 3 actually resolves
its findings and whether the revision introduced new defects.

## Stakeholder decisions to preserve while auditing consequences

- Named profiles remain low-friction presets over composable capabilities and scopes.
- Changing profiles or authority does not categorically prohibit resume.
- Profile, cache, authority, context, runtime, and sandbox notices are independent.
- Warnings and confirmations can be configured to `never`; warnings inform rather than infantilize.
- Native Claude sandboxing is the standard command boundary, with explicit configurable
  unsandboxed execution when needed; no second general-purpose sandbox is planned now.
- Standard filesystem scope is project plus declared roots; host-wide reads are an advanced custom
  option.
- `mcp-readonly` is generic and registry-backed rather than codebase-memory-specific.
- Generated state retains the 240 MiB configured ceiling and 192 MiB admission threshold.

You may identify serious consequences or recommend precise safeguards, defaults, explanations, or
schema changes. Do not silently replace these product decisions with paternalistic prohibitions.
If you believe a decision makes a safe product impossible, make that an explicit blocker with a
demonstrable counterexample and the smallest decision change that would resolve it.

## Audit questions

These questions are a floor, not a ceiling. Independently identify important workflows, edge
cases, threat paths, product needs, simplifications, or opportunities that the packet did not
anticipate.

1. Does the requested → compiled → preflight-assessed → runtime-observed/effective model keep
   authority, exposure, enforcement, and evidence epistemically distinct?
2. Is the normative schema sufficiently typed and extensible? Identify ambiguous defaults,
   missing invariants, invalid cross-field states, unstable identifiers, or dimensions that C0
   would prematurely freeze.
3. Is `authority_atoms` plus directional comparison capable of correctly classifying path scopes,
   operation sets, command templates, MCP bundles, network policy, sandbox fallback, resource
   limits, context changes, and unknowns? Supply concrete counterexamples.
4. Are cache expectations separated correctly from profile transitions and authorization? What
   can be known from Claude Code versus only observed from provider counters?
5. Do independently suppressible notices/confirmations remain auditable and usable in interactive
   and unattended flows without turning presentation preferences into authority?
6. Is the sandbox design honest and robust across writable working directories, inherited merged
   settings, unsandboxed retries, sockets/Docker, Apple Events, credentials, symlink/mount/hardlink
   aliases, MCP process placement, resource exhaustion, crashes, and test incompatibility? Find
   additional failure scenarios and distinguish first-release mitigations from later hardening.
7. Does `mcp-readonly` have a workable trust/update model for server versions, tools, annotations,
   startup effects, state roots, network behavior, and partially observed exposure?
8. Will C0 truly remain non-activating and leave current paid `run`/`resume` behavior unchanged?
   Audit the write set, imports, CLI dispatch, tests, migration fixture, and likely coupling points.
9. Is the C0 plan executable by a fresh worker without guessing? Identify missing RED cases,
   misleading test expectations, incorrect interfaces, repository conflicts, or verification gaps.
10. Is the cohort split C0–C6 ordered correctly, or does C0 require a small piece of a later
    cohort to avoid encoding abstractions that cannot be compiled or observed?
11. Does the product support both low-friction preset users and advanced operators without profile
    explosion, configuration burden, unsafe implicit inheritance, or verbose warning fatigue?
12. Is this design overly broad or dependency-heavy? Recommend deletions or simplifications that
    improve reliability without sacrificing the approved flexibility.
13. Classify every recommended change as `C0 blocker`, `pre-first-release`, or `later` and explain
    the dependency ordering.

## Anti-anchoring challenges

Before issuing the verdict, independently steelman and test these alternatives against the actual
requirements:

- keep the current fixed version-3 profiles and make only narrow corrections;
- expose Claude settings directly rather than maintain a provider-neutral policy schema;
- always start a fresh session across profile changes;
- use a container or second OS sandbox instead of native Claude sandboxing;
- skip the non-activating C0 cohort and implement one thin end-to-end review profile first.

Recommend an alternative only if its lifecycle and evidence burden is genuinely lower after
accounting for the approved advanced-use cases.

## Evidence standard

Separate observed facts, documented/reported behavior, inferences, recommendations, stakeholder
decisions, and open questions. Do not infer runtime enforcement from fake-CLI tests. Do not infer a
cache hit from unchanged local fields. Treat missing evidence as unknown, not as proof of absence.
For every blocker or major finding, give a narrow source locator and a concrete failure example or
counterexample. Avoid generic security advice.

Run the existing adapter suite if useful. Report exact commands and outcomes. Use read-only MCP
queries if they materially improve code-path analysis, but do not re-index, mutate, or delete any
graph state.

## Return shape

Emit only a complete Markdown report with:

1. **Audit identity** — reviewed paths and observed hashes; model/effort only if exposed by the
   runtime; checks performed and limitations.
2. **Executive verdict** — one required verdict plus a concise explanation.
3. **Blockers and major findings** — stable IDs, severity, evidence, failure scenario, required
   change, and release timing.
4. **Missing cases and opportunities** — including issues not suggested by this prompt.
5. **Sandbox and unsandboxed-execution assessment** — what is sound, what is unknown, and what must
   be tested.
6. **C0 plan corrections** — task-by-task changes precise enough for the root to disposition.
7. **First-release versus later matrix**.
8. **Alternative architecture assessment**.
9. **Residual risks and open questions**.
10. **Minimum approval conditions** — the smallest bounded set of revisions after which C0 may
    proceed.

Be concise enough to use as a gate artifact, but do not omit a substantive finding merely because
the prompt did not name it.
