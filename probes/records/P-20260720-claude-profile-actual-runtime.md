# P-20260720 — Claude capability-profile actual-runtime probe

**Status:** parked / inconclusive after one authorized paid startup. No retry authorized.

## Route and packet

- planned route: Sonnet 5, high effort, external probe worker;
- requested route: `sonnet`, high, `verified-review`, `dontAsk`;
- observed route: `claude-sonnet-5` from the init event; observed effort was not exposed;
- nearest alternative: Opus 4.8 high;
- route basis: observation-dominated, five-action runtime probe under R6/W-006; root-owned
  deterministic validation;
- packet: `probes/runtime/P-20260720-claude-profile-activation/prompt.md`; its absolute command
  locators were annotated after execution for repository linting, while the exact executed bytes
  remain private as `<run>/prompt-original.md` and match the metadata SHA-256;
- session/run ID: `f7912d4b-b7de-4385-b5f8-cf0aadbcc0cf`;
- private evidence: `~/.codex/state/delegate-to-claude/runs/<run-id>/`.

## Observed facts

1. Claude Code `2.1.215` emitted a connected `codebase-memory-mcp` init manifest, model
   `claude-sonnet-5`, and permission mode `dontAsk`.
2. The init manifest exposed all ten pinned non-mutating codebase-memory identifiers even though
   only `list_projects` was permission-allowed. The adapter expected only the selected identifier,
   classified the other nine as broader, terminated the process with exit 143, and returned its
   manifest-violation exit code before any assistant or tool event.
3. No final result, token usage, cache counters, turn count, or price/cost field was emitted. Those
   values are unknown and must not be estimated.
4. The scratch sentinel, project-write sentinel, and `.git`-write sentinel were absent immediately
   after termination. The localhost server showed no request before it was stopped. Because no
   action event occurred, these absences prove early termination, not sandbox enforcement.
5. Managed delegate state was 8,268 KiB after the run; the run directory was 20 KiB. The scratch
   marker consumed 248 bytes. The `<250 MiB` boundary was not approached.
6. MCP configuration and executable provenance were pinned in private metadata by SHA-256; the
   executable was the local absolute `codebase-memory-mcp` command with no args, URL, or env
   overrides.

## Root-cause disposition

**Observed defect:** the adapter conflated startup exposure with permission-allowed authority for
unselected pinned MCP query tools. This contradicted the proposal's own exposed/allowed/denied
distinction.

**Root correction:** profile resolution now explicitly denies every pinned MCP identifier not
selected by the packet. The real init shape is consequently classified as expected
exposed-but-denied rather than broader, while unknown or mutating identifiers still fail closed.
The authority change increments the profile contract from version 2 to version 3 so the failed
version-2 session cannot be resumed under the corrected contract.

RED evidence:

- `test_unselected_pinned_mcp_tools_are_explicitly_denied`;
- `test_real_init_shape_with_unselected_pinned_mcp_exposure_is_not_broader`;
- `test_real_mcp_init_exposure_shape_respects_explicit_query_denies`;
- `test_version_two_run_cannot_resume_under_version_three_but_stays_materializable`.

## What remains unverified

The paid startup supplied useful runtime manifest evidence but did not execute a worker turn.
Scratch write allowance, project/`.git` write denial, localhost network denial, permitted MCP
invocation, token/cache reporting, and successful result materialization remain unverified.

A fresh version-3 run—not a resume—is the smallest next probe. It is an additional paid call and
requires explicit operator approval. No automatic retry, installation, deployment, commit, or
profile activation follows from this record.
