# Codex consumer adapter — generated fragment (Stage-3, built 2026-07-10)

`python3 install.py codex` prints the KNOWN-CONSUMERS guidance fragment (AGENTS.md-style) with
the package's resolved path substituted; `--dest PATH` writes it where the Codex driver loads
its instructions. Source: [`AGENTS-fragment.template`](AGENTS-fragment.template) (placeholder
`{{PACKAGE_HOME}}` — resolved at generation time so no user-specific path lives in the repo).

Content: read ROUTES.md + STATE.md before delegating to a Claude executor; run
`check_state.py` (expired = Unchecked → Fallback column); CONTRACT §3's surface table names
which knobs each spawn surface can pin; fit line per spawn; Contested/CANDIDATE rows are
probes, not priors.
