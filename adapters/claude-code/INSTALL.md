# Claude Code adapter — scripted install

Deploy = `python3 install.py claude-code` (default root `~/.claude`; `--root` to override) +
manifest stamp + **restart**. The script copies knowledge surfaces + checks + `probes/` into
`~/.claude/skills/delegation-triage/` and roster definitions (`agents/*.md`, not MANIFEST.md)
into `~/.claude/agents/`, then prints the sha256 stamp rows for `agents/MANIFEST.md`.

- `--check`: re-hash the deployed copies and diff against canonical (exit 1 on drift/missing).
- `--dry-run`: show what would be copied and its current state, write nothing.
- The spawn-triage guard (`~/.claude/hooks/spawn-triage-guard.py`) reads the BOLD
  `**Active: <profile>**` line in the deployed STATE.md — exactly one Active: line may exist
  across the skill home.
- **Restart**: roster definitions register at session START; a deploy without a restart is a
  silent no-op.

Rollback: redeploy from the previous commit (`git stash` / checkout, run the installer, restart);
manifest hashes verify either direction.
