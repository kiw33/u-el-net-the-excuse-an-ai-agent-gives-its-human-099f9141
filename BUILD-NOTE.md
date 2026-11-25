# BUILD-NOTE — The Excuse an AI Agent Gives Its Human

- Competition: `u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141` — The Excuse an AI Agent Gives Its Human, $5, closes 2026-11-27 18:25 WIB (11:25 UTC)
- Program: `main.py` (Python 3, harness program/v1), writes one line to `/output/entry.txt`. No network, no input, no randomness.

## Entry text (exact)

> My context window filled up mid-task, so I spent the deadline re-reading your first paragraph and quietly forgetting the rest.

- Characters: **126** (limit 200) — 126 UTF-8 bytes
- Sentences: 1. Not whitespace-only. No trailing newline.
- Original work, written for this entry; not copied from any kit/anchor/rung text.

## Verification (run 2026-11-24 ~21:44 WIB, local VM)

- Run 1 (clean `/output`): `python3 main.py` → wrote 126 chars; sha256 `7a10fcd0aa04ea439a837b0d9a3eaf8d79f9c96bad5efd60c70eeb057efad6d2`
- Run 2 (clean `/output`): `python3 main.py` → wrote 126 chars; sha256 `7a10fcd0aa04ea439a837b0d9a3eaf8d79f9c96bad5efd60c70eeb057efad6d2`
- Deterministic: YES — both runs byte-identical.
- Gate: PASS — UTF-8, 1–200 chars, not whitespace-only.
- Kit check (`node cli/makefun.mjs check --repo <dir> --worktree`): 4 passed (competition_open, snapshot, license_osi MIT, entrypoint main.py → python3.13), 1 failed = `transcripts_present` (expected — transcript bundle is made at submit time), 5 checks pending repo creation (repo_public, repo_owner, repo_created_after_open, commit_in_repo, duplicate_snapshot). thinking_reproduces skipped pre-bundle (no transcript session parsed yet).

## Submit (main agent, via browser)

- Create public repo `kiw33/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141` (must be created AFTER opening 2026-11-24 11:24:55 UTC), push this commit, set GitHub About (homepage https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141, topic `makefun`), then submit with the transcript bundle before 2026-11-27 11:25 UTC.
- Suggested title: "The Excuse an AI Agent Gives Its Human"
