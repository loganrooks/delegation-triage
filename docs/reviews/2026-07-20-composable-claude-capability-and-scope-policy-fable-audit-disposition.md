# Root disposition of the Fable correction audit

- **Date:** 2026-07-20
- **Audit:** [Fable correction audit](2026-07-20-composable-claude-capability-and-scope-policy-fable-audit.md)
- **Audit SHA-256:** `93db2dc01400122ad3ee6145aa26d7f560c1e4335b0de16213e6c6a344cace64`
- **Reviewed proposal SHA-256:** `bbb76fb05c5e298ebf044220c0f2a4cf72132505c4c98adce60c02ab00a6335e`
- **Reviewed plan SHA-256:** `3d860d04b012fe32be7444a5b33e64dc2005d89fd9e5265090bc735520b73f61`
- **Root verdict:** accept `REVISE THEN IMPLEMENT`; C0 execution remains gated
- **Authority:** disposition only; no proposal/plan correction, implementation, activation,
  installation, commit, or paid follow-up is authorized by this artifact

## Run and evidence assessment

The wrapper observed `claude-fable-5`, a successful terminal result, 27 turns, no unexpected tool
exposure, and a materializable response. It reported 30,974 output tokens, 1,168,382 cache-read
tokens, 104,092 cache-creation tokens, and `$4.799322` cost. The full stream remains in the private
run root for session `dd1aac24-b6ad-4507-8b16-752a338c088b`.

Fable could read the repository and candidate code. It did not use the available read-only MCP
queries. It did not re-run the test suite: it twice requested a piped wildcard discovery command
instead of the explicitly admitted test command, and `dontAsk` denied the mismatch. Its statement
that shell access was “revoked” is therefore imprecise. The root had independently run the existing
suite immediately before the audit: 195 tests passed in 21.246 seconds. Findings that depend on
source and contract inspection remain useful; the audit supplies no new test-execution evidence.

The report begins with a short preamble despite the output-only contract. That is a formatting
deviation, not a substantive failure, and the original materialized artifact remains unchanged.

## Finding dispositions

| ID | Disposition | Timing | Root rationale and correction direction |
|---|---|---|---|
| CA-001 | **Accept** | C0 blocker | The plan does not specify the detachment transform between private root bindings and the canonical semantic document. Revision must define separate authority-bearing identity from presentation/operator preferences and test equivalent bindings without exporting raw paths. |
| CA-002 | **Accept** | C0 blocker | `null = unbounded` conflicts with default-deny language and the retained 240/192 MiB generated-state contract. Resource values need explicit `unavailable`/`unknown`, finite, and intentionally unbounded states rather than overloaded nulls. |
| CA-003 | **Accept with chosen resolution** | C0 blocker | Keep notices as `always/once/never`; keep confirmations as `ask/never`. Amend §9.6 rather than adding a stateful `once` confirmation mode. |
| CA-004 | **Revise** | C0 blocker | The missing `unknown` path is real. Do not model `unavailable` as ordinary authority below `deny`: it is activation/runtime state. Add per-dimension relation plus unresolved reasons; the aggregate authority conclusion is `unknown` when unresolved dimensions could change the conclusion, while known broadening remains separately visible. |
| CA-005 | **Accept with corrected comparator** | C0 blocker | Removing a deny under an allow default is broadening. A plain negative atom would invert that relation under set subtraction, so use a separate deny-rule comparator. Allow rules must reference declared named roots; raw paths remain deny-only. |
| CA-006 | **Accept** | C0 blocker | Template IDs without typed content cannot carry authority. Because C0 is the contract core, revision should define the normative template record and content-address its authority-bearing fields rather than silently accepting opaque non-empty templates. |
| CA-007 | **Accept** | C0 blocker | The existing CLI tests spawn a child process, so mock patches cannot prove call boundaries across that process. Add in-process `main()` tests for patched calls and retain subprocess tests for absence of Claude/state effects. |
| CA-008 | **Accept** | C0 blocker | The assurance matrix needs one explicit, versioned source outside the requested policy and authority hash. C0 may only claim labels supported by its evidence; otherwise use `unknown`. |
| CA-009 | **Revise; reject forced final warning** | C0 blocker | Source precedence is underspecified, but Fable's proposal to force the previous policy's display rule conflicts with the stakeholder's explicit warning-off decision. Resolve preferences only from operator-owned current configuration/invocation, never untrusted repository configuration; record preference changes privately, while display follows the operator's newly selected setting. |
| CA-010 | **Accept** | Pre-first-release | A resolved MCP registry record/version and tool-definition identity must enter compiled/cache inputs before `readonly` activates. C0 represents unresolved bundles honestly. |
| CA-011 | **Accept** | Pre-first-release | Define `once` as a presentation-state contract before C1 displays notices. Recommended scope is category plus transition identity within a run lineage; C0 only validates the value. |
| CA-012 | **Accept in part** | C0 blocker | Add explicit reject/normalize rules for empty selected command, MCP, and network allowlists. Do not automatically reject or erase `sandbox.required + commands.deny`; a dormant sandbox request may be valid for a preset or future non-command surface, but must remain non-activating and explainable. |
| CA-013 | **Revise** | C0 blocker | Add sandbox-mode and allowlist-to-unrestricted comparators. Enforcement status (`enforced/sampled/unknown`) is assurance/runtime evidence, not requested authority, so it triggers runtime/assurance analysis rather than being ordered as authority. |

## Additional-case dispositions

| Case | Disposition | Timing |
|---|---|---|
| External named-root rebinding | **Accept:** add private binding identity to context comparison without placing raw paths or stable global fingerprints in telemetry. | Pre-first-release |
| Legacy profile version versus policy preset revision | **Accept:** label the namespaces distinctly in C0 explanations and migration fixtures. | C0 |
| Migration-fixture thinness and alias membership | **Accept:** document that the fixture freezes only the intended historical flag surface and include the alias explicitly. | C0 |
| Schema-upgrade test in schema v1 | **Accept with scope change:** reserve version dispatch now, but move semantic no-op upgrade verification to the first real migration. | C0 wording / later test |
| Exposed-but-denied built-ins versus MCP tools | **Park:** revisit with the C1 configuration/exposure model; exposure alone remains distinct from authority. | C1 |
| Append-only public authority-atom vocabulary | **Park:** useful only if atoms become a supported external automation interface. | Later |
| Scratch hard-link/materialization counterexample | **Accept:** proposal already names hard links; add the concrete materialization test and inode/link-count handling. | C2/C4 |
| Process signaling | **Accept and elevate:** the proposal calls it a separate dimension but schema v1 omits it. Add a denied/unavailable process-control dimension in C0 and probe enforcement in C3. | C0 schema / C3 probe |
| Tools ignoring redirected temporary/cache variables | **Accept:** add a supported-runner counterexample and incompatibility reporting test. | C3 |

## Minimum revision boundary

Before C0 execution, issue a proposal/plan correction covering CA-001 through CA-009, the accepted
parts of CA-012/013, distinct version namespaces, migration-fixture intent, and the missing
process-control dimension. Record stable finding-to-requirement lineage and new hashes. CA-010/011
and the accepted later cases must enter the appropriate cohort plans before those surfaces activate.

No second Fable call is required for faithful corrections within this boundary. Material changes
to stakeholder decisions, the cohort architecture, or the authority model require a new review
decision rather than being hidden inside implementation.
