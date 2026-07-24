# Source inventory and provenance

## Core PDF sources

| ID | Source | Role | Date | Pages | SHA-256 | Principal use | Material limitations |
|---|---|---|---|---:|---|---|---|
| O5-SC | [Claude Opus 5 System Card](sources/Claude_Opus_5_System_Card.pdf) | Primary vendor evaluation | 24 July 2026 | 193 | `fed3c0e6d150a6ba855f0f117a632d2b27dbb5886fd42815caa92e3e20db1d25` | Opus 5 capability, effort, multi-agent results and methodology | Vendor-produced; multi-agent runs use pre-release configuration and unreleased effort |
| O48-SC | [Claude Opus 4.8 System Card](sources/Claude_Opus_4.8_System_Card.pdf) | Primary vendor evaluation | May 2026 | 246 | `97f11ae3fb305c7105c958599bcf90f216669543393220f674610ddb83ee611a` | Opus 4.8 baseline and async regression | Different card vintage and configuration |
| F5-SC | [Claude Fable 5 & Claude Mythos 5 System Card](sources/Claude_Fable_5_and_Mythos_5_System_Card.pdf) | Primary vendor evaluation | June 2026 | 319 | `d23b49f41fa5f3c523089c75e6718f12b59674d74fa981fd81205daf80c9029a` | Fable/Mythos multi-agent results and harnesses | Mythos configuration underlies some capability results; vendor-produced |

Official discovery page: [Anthropic model system cards](https://www.anthropic.com/system-cards).

## Official web documentation

| ID | Source | Relevant section | Accessed | Role | Limitation |
|---|---|---|---|---|---|
| O5-PG | [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5) | “Multi-agent coordination”; “Task scope and over-verification”; “Controlling subagent spawning”; “Self-correction” | 24 July 2026 | Official behavior and scaffolding guidance | Mutable web documentation; not independent evaluation |
| O48-PG | [Prompting Claude Opus 4.8](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-4-8) | “Tool use triggering”; “Controlling subagent spawning” | 24 July 2026 | Official description of older behavior | Mutable; vendor characterization |
| F5-PG | [Prompting Claude Fable 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5) | “Capability improvements”; “Longer turns by default”; “Consider all effort levels” | 24 July 2026 | Official behavior and effort guidance | Mutable; vendor characterization |
| PRICE | [Pricing](https://platform.claude.com/docs/en/about-claude/pricing) | “Model pricing” | 24 July 2026 | Current official price declaration | Prices may change; total cost is not token rate alone |

## Extraction and verification process

1. PDF metadata and page counts were inspected.
2. Relevant PDF ranges were rendered at 180 DPI.
3. Figures and labels were read from rendered pages.
4. Numeric graph data was manually transcribed into CSV.
5. Source page, figure number, and extraction method were stored with each value.
6. Calculated deltas were recomputed from the transcribed values.
7. The Opus 5 +2.9 versus +2.8 rounded/prose discrepancy was preserved rather than silently normalized.

The rendered pages are in `evidence/`. They are convenience copies; the PDFs remain authoritative.

## Evidence coverage limitation

The core comparative evidence in this report is almost entirely Anthropic-produced. A current, controlled, independent study that holds worker models and harness conditions constant was not located in this pass. Accordingly, recommendations are provisional and explicitly separated from verified card results.
