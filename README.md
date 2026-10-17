# dep-triage-demo

Demo target repo for the **Dependency Advisory Triage** agent (Ziro Agentic AI Hackathon 2026).

The dependencies in `requirements.txt` are intentionally pinned to old versions with known public security advisories. **Do not use this code in production.**

| Package | Pinned | What the safe upgrade does | Test case |
|---|---|---|---|
| requests | 2.19.0 | Upgrade keeps the code working, CI passes | TC1 |
| Jinja2 | 2.10 | Upgrade to 3.x removes `jinja2.Markup`, CI fails | TC3 |

CI (`.github/workflows/ci.yml`) installs the requirements and runs `pytest` on every push and pull request. The agent reads this CI result to decide whether an upgrade PR is passing or failing.
