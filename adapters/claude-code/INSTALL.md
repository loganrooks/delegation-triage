# Claude Code adapter — documented manual install (Stage-2 form)

Deploy = copy + manifest stamp + restart. From the repo root:

1. Copy knowledge surfaces + procedure into the skill home:
   `SKILL.md ROUTES.md STATE.md WARRANTS.md CONTRACT.md EPISTEMICS.md check_state.py
   check_wids.py probes/` → `~/.claude/skills/delegation-triage/`
2. Copy roster definitions: `agents/*.md` (NOT MANIFEST.md) → `~/.claude/agents/`
3. Stamp `agents/MANIFEST.md` (here, canonical): target, date, `shasum -a 256` of the deployed
   copies. `--check` equivalent: re-hash the target, diff against the manifest.
4. The spawn-triage guard (`~/.claude/hooks/spawn-triage-guard.py`) reads the BOLD
   `**Active: <profile>**` line in the deployed STATE.md — exactly one Active: line may exist
   across the skill home (the archived routing table's line is retired).
5. **Restart**: roster definitions register at session START; a deploy without a restart is a
   silent no-op.

Rollback: single copy-back of the pre-deploy snapshot; manifest hashes verify either direction.
