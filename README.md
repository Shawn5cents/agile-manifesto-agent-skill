# Agile Manifesto Agent Skill

A portable Agent Skill that applies Agile Manifesto values and principles to real software work: planning, implementation, debugging, product prioritization, team process, retrospectives, and project rescue.

The goal is not to add Scrum ceremony. The goal is to help an AI coding or planning agent prefer working software, short feedback loops, customer collaboration, adaptation, technical excellence, simplicity, and sustainable delivery.

## Why this exists

AI coding agents often over-plan, produce documentation instead of working increments, refactor before validating value, or keep following a stale plan after evidence changes. This skill gives them a compact Agile execution lens.

## Attribution

This project was created from the ideas in the **Manifesto for Agile Software Development (2001)** and its accompanying principles. The original work is credited to its 17 authors: Kent Beck, Mike Beedle, Arie van Bennekum, Alistair Cockburn, Ward Cunningham, Martin Fowler, James Grenning, Jim Highsmith, Andrew Hunt, Ron Jeffries, Jon Kern, Brian Marick, Robert C. Martin, Steve Mellor, Ken Schwaber, Jeff Sutherland, and Dave Thomas.

Original source: https://agilemanifesto.org/

This repository is an independent Agent Skill implementation. It does not claim authorship of the Agile Manifesto and intentionally does not reproduce the full manifesto.

## Agent compatibility

The repository uses the open `SKILL.md` Agent Skills structure as the canonical format.

- **ChatGPT / OpenAI / Codex:** `SKILL.md` plus `agents/openai.yaml` metadata.
- **Claude / Anthropic:** compatible `SKILL.md` frontmatter and progressive-loading structure; `CLAUDE.md` is a thin fallback bridge.
- **Gemini CLI:** the repository can be installed as an Agent Skill; `GEMINI.md` documents manual placement.
- **Generic agents:** `AGENTS.md` points non-native skill consumers to the same canonical instructions.
- **GitHub Copilot:** `.github/copilot-instructions.md` points matching work to `SKILL.md`.

No vendor gets its own fork of the Agile logic. That keeps behavior consistent across agents.

## Install

### Gemini CLI

```bash
gemini skills install https://github.com/Shawn5cents/agile-manifesto-agent-skill.git
```

### Universal workspace layout

Clone or copy the repo into a skills directory recognized by your agent. A common interoperable workspace layout is:

```text
.agents/skills/agile-manifesto/
  SKILL.md
  references/
  assets/
```

### Claude Code

If your Claude environment discovers project skills, place the skill folder in its supported skill location. If skill discovery is unavailable, add the repo to the project and point Claude to `SKILL.md`; the included `CLAUDE.md` bridge does this inside this repository.

### ChatGPT / OpenAI

Install the packaged `skill.zip` through the Skills interface, or use the repository contents in an Agent Skills-compatible OpenAI environment.

## Example prompts

- "Plan this feature using the Agile Manifesto skill."
- "We are stuck in architecture work. What is the smallest working slice?"
- "Review this workflow for process waste and missing feedback loops."
- "What should we ship next if the goal is working evidence, not more planning?"
- "Turn this large project into a testable vertical slice."

## What the skill returns

For planning work it favors:

1. Agile read
2. Smallest valuable increment
3. Build/test/demo steps
4. Feedback loop
5. Definition of done
6. Next iteration

For rescue/review work it favors:

1. What blocks working software
2. What to cut or defer
3. What to ship first
4. Evidence needed
5. Next concrete action

## Repository structure

```text
SKILL.md                         Canonical cross-agent skill
references/agile-operating-rules.md
agents/openai.yaml               OpenAI UI metadata
assets/icon.svg
AGENTS.md                        Generic agent bridge
CLAUDE.md                        Claude bridge
GEMINI.md                        Gemini bridge
.github/copilot-instructions.md  GitHub Copilot bridge
adapters/README.md               Compatibility design notes
tests/validate_skill.py          Cross-agent format checks
```

## Discoverability keywords

Agent Skills, AI agents, coding agents, Agile Manifesto, agile software development, Claude Code skills, ChatGPT skills, Codex skills, Gemini CLI skills, SKILL.md, AGENTS.md, software planning, project rescue, iterative development, working software, developer productivity.

## License

The implementation in this repository is released under the MIT License. The Agile Manifesto itself remains © 2001 its original authors; see the attribution above and the original site for its copying notice.
