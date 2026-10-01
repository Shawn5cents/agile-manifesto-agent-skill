#!/usr/bin/env python3
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
skill = root / "SKILL.md"
text = skill.read_text(encoding="utf-8")
errors = []

if not text.startswith("---\n"):
    errors.append("SKILL.md must start with YAML frontmatter")
match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
if not match:
    errors.append("SKILL.md frontmatter is malformed")
else:
    fm = match.group(1)
    name = re.search(r"^name:\s*(.+)$", fm, re.M)
    desc = re.search(r"^description:\s*(.+)$", fm, re.M)
    if not name or name.group(1).strip() != "agile-manifesto":
        errors.append("name must be agile-manifesto")
    if not desc or len(desc.group(1).strip()) < 80:
        errors.append("description must contain useful discovery triggers")
    if desc and len(desc.group(1).strip()) > 1024:
        errors.append("description exceeds 1024 characters")

for required in [
    "references/agile-operating-rules.md",
    "agents/openai.yaml",
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
    ".github/copilot-instructions.md",
]:
    if not (root / required).exists():
        errors.append(f"missing {required}")

for phrase in ["Manifesto for Agile Software Development", "Kent Beck", "Dave Thomas", "https://agilemanifesto.org/"]:
    if phrase not in text and phrase not in (root / "README.md").read_text(encoding="utf-8"):
        errors.append(f"missing attribution marker: {phrase}")

if errors:
    print("FAIL")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("PASS: canonical skill, attribution, and cross-agent bridges validated")
