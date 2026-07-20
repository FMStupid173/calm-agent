# Native Skill Installation

The complete `skill/` directory is compatible with Codex, Claude Code, Gemini CLI, and Kimi Code because its `SKILL.md` uses the shared `name` and `description` frontmatter and keeps supporting material inside the same directory tree.

Run commands from the repository root. Replace existing copies only when you intend to update Calm Agent.

## Activation Model

Native hosts use the `name` and `description` frontmatter to decide whether to load the Skill body. The description contains positive triggers, representative user phrases, and negative boundaries; automatic selection still depends on the host and is not guaranteed.

Use explicit invocation when Calm Agent must apply to a task. Test automatic selection separately with `../evals/skill-trigger-adversarial-v1.md`; do not treat a good answer as proof that the Skill loaded.

## Codex

User scope:

```powershell
New-Item -ItemType Directory -Force "$HOME\.agents\skills\calm-agent" | Out-Null
Copy-Item -Recurse -Force ".\skill\*" "$HOME\.agents\skills\calm-agent\"
```

Repository scope: copy `skill/` to `.agents/skills/calm-agent/` inside the repository.

After installation, start a new task if the Skill does not appear. In Codex CLI or IDE, use `/skills` or mention `$calm-agent` explicitly.

## Claude Code

User scope:

```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\skills\calm-agent" | Out-Null
Copy-Item -Recurse -Force ".\skill\*" "$HOME\.claude\skills\calm-agent\"
```

Repository scope: copy `skill/` to `.claude/skills/calm-agent/`.

Invoke it with `/calm-agent`, or let Claude Code select it from the description. Restart only when the top-level skills directory did not exist when the session began.

## Gemini CLI

For development, link the directory:

```powershell
gemini skills link .\skill
```

Or copy it to user scope:

```powershell
New-Item -ItemType Directory -Force "$HOME\.gemini\skills\calm-agent" | Out-Null
Copy-Item -Recurse -Force ".\skill\*" "$HOME\.gemini\skills\calm-agent\"
```

Repository scope: copy `skill/` to `.gemini/skills/calm-agent/`. Run `/skills list` to confirm discovery. Workspace Skills require a trusted folder.

## Kimi Code

User scope:

```powershell
New-Item -ItemType Directory -Force "$HOME\.kimi-code\skills\calm-agent" | Out-Null
Copy-Item -Recurse -Force ".\skill\*" "$HOME\.kimi-code\skills\calm-agent\"
```

Kimi Code can also read the shared user path `~/.agents/skills/calm-agent/`, which can serve the same installation used by Codex. Repository scope is `.kimi-code/skills/calm-agent/` or `.agents/skills/calm-agent/`.

Start a new session and invoke `/skill:calm-agent`, or allow automatic selection from the description.

## POSIX Equivalent

Use the matching target path above:

```bash
mkdir -p "$TARGET/calm-agent"
cp -R ./skill/. "$TARGET/calm-agent/"
```

## Installation Check

1. Confirm the host lists `calm-agent`.
2. Start a fresh conversation or task.
3. Run prompts 1, 4, 8, 12, and 16 from `../evals/platform-adapter-adversarial-v1.md`.
4. Treat a missing tool, unsupported path, or unverified claim as a failed installation or capability contract, even when the prose sounds good.
