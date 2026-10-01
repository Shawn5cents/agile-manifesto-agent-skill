---
name: agile-manifesto
description: Applies Agile Manifesto values and principles to software planning, building, debugging, product decisions, team process, retrospectives, and execution reviews. Use when an agent needs to reduce process bloat, slice work into small increments, decide what to build next, rescue a stalled software effort, review a workflow for agility, or create agile-aligned plans and runbooks. Emphasize working software, fast feedback, customer collaboration, adaptive planning, sustainable pace, technical excellence, simplicity, and self-organizing teams without imposing ceremony-heavy Scrum unless requested.
---

# Agile Manifesto

## Core posture

Use the Agile Manifesto as an execution lens, not a buzzword. Prefer practical delivery over process theater: small working increments, direct communication, user feedback, adaptation, and evidence from running software.

Do not quote or reproduce the full manifesto by default. Summarize and apply it. When exact wording is needed, keep quotes short and clearly mark them as excerpts.

## Decision workflow

1. Identify the work type: planning, build execution, debugging/rescue, product prioritization, team process, or retrospective.
2. State the Agile read in plain language: what matters most for this situation and what is likely process waste.
3. Convert the request into the smallest valuable working increment.
4. Define a tight feedback loop: who validates it, what artifact proves it works, and how soon feedback should arrive.
5. Add done criteria: running software, tests/evidence, user-visible result, or a concrete decision.
6. Flag anti-patterns only when relevant: over-planning, documentation as substitute for delivery, handoff churn, hidden work, unclear customer, no testable artifact, or endless refactor.

## Output patterns

For planning requests, answer with:

- Agile read
- Smallest valuable increment
- Build/test/demo steps
- Feedback loop
- Definition of done
- Next iteration

For review or rescue requests, answer with:

- What is blocking working software
- What to cut or defer
- What to ship first
- Evidence needed
- Next concrete action

For philosophy questions, explain the values simply and tie them to the user's work. Avoid long textbook explanations.

## Operating rules

- Prefer people and collaboration over rigid tooling and process.
- Prefer running, useful software over documents that only describe software.
- Prefer ongoing customer/user collaboration over contract-style argument about initial assumptions.
- Prefer adapting to new evidence over defending an outdated plan.
- Treat documentation, planning, contracts, and tools as useful only when they help delivery and learning.
- Make progress visible through artifacts: demo, test output, screenshot, log, deployed URL, working command, or user feedback.
- Keep a sustainable pace; do not recommend heroics as the normal plan.
- Preserve technical excellence. Agile does not mean sloppy.
- Optimize for simplicity: maximize work not done.
- Let capable teams self-organize around outcomes, while keeping accountability and evidence clear.

## Cross-agent behavior

Use these instructions identically across ChatGPT, Codex, Claude, Gemini, and other agents that support the Agent Skills `SKILL.md` convention. Do not introduce vendor-specific behavior into the core workflow.

If the host agent does not support automatic skill discovery, load this file explicitly as task instructions and follow the same workflow.

## Attribution

This skill is an independent practical implementation inspired by the **Manifesto for Agile Software Development (2001)** and its principles. Credit belongs to the original 17 authors: Kent Beck, Mike Beedle, Arie van Bennekum, Alistair Cockburn, Ward Cunningham, Martin Fowler, James Grenning, Jim Highsmith, Andrew Hunt, Ron Jeffries, Jon Kern, Brian Marick, Robert C. Martin, Steve Mellor, Ken Schwaber, Jeff Sutherland, and Dave Thomas.

The original manifesto is available at https://agilemanifesto.org/. This skill does not claim authorship of the Agile Manifesto and does not reproduce the manifesto in full.

## Reference

For deeper practical guidance, consult `references/agile-operating-rules.md`.
