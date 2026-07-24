# Web source notes

These notes make mutable official web sources easier to audit. Use the exact page and section heading; the source itself may change after the access date.

## O5-PG — Prompting Claude Opus 5

URL: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5  
Accessed: 24 July 2026

Relevant sections:

- **Capability improvements → Multi-agent coordination:** states that Opus 5 coordinates subagent teams well and highlights writer–verifier patterns.
- **Task scope and over-verification:** says the model verifies without being told and that legacy verification instructions can add wasted work; also warns about scope expansion.
- **Controlling subagent spawning:** says Opus 5 delegates more readily than prior models and recommends explicit guidance or deterministic caps.
- **Self-correction:** warns against redundant “double-check” instructions.

## O48-PG — Prompting Claude Opus 4.8

URL: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-4-8  
Accessed: 24 July 2026

Relevant sections:

- **Tool use triggering:** says Opus 4.8 tends to favor reasoning over tool calls.
- **Controlling subagent spawning:** says it tends to spawn fewer subagents by default.

## F5-PG — Prompting Claude Fable 5

URL: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5  
Accessed: 24 July 2026

Relevant sections:

- **Capability improvements → Delegation and collaboration:** characterizes Fable as significantly more dependable at dispatching and sustaining parallel subagents and maintaining ongoing communication.
- **Longer turns by default:** describes long, sometimes hours-scale autonomous runs.
- **Consider all effort levels:** recommends High for most tasks, XHigh for capability-sensitive work, and Medium/Low for routine work; warns that higher effort can over-deliberate on routine tasks.

## PRICE — Pricing

URL: https://platform.claude.com/docs/en/about-claude/pricing  
Accessed: 24 July 2026

Relevant section:

- **Model pricing:** Fable 5 is listed at $10/MTok input and $50/MTok output; Opus 5 at $5/MTok input and $25/MTok output.
