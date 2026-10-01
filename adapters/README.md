# Compatibility adapters

The core skill is vendor-neutral and lives in the repository root as `SKILL.md`.

Use the root directory directly with any tool that supports the Agent Skills open format. The small files `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, and `.github/copilot-instructions.md` exist only as bridges for agents that also recognize vendor-specific repository instruction files.

Do not duplicate or fork the core workflow into these adapters. That prevents behavior drift between agents.
