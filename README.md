# dep-triage-demo

Demo target repo for the **Dependency Advisory Triage** agent (Ziro Agentic AI Hackathon 2026).

The dependencies in `requirements.txt` are intentionally pinned to old versions with known public security advisories. **Do not use this code in production.**

| Package | Pinned | What the safe upgrade does | Test case |
|---|---|---|---|
| requests | 2.28.0 | Upgrade keeps the code working, CI passes | TC1 |
| Werkzeug | 2.2.2 | Upgrade to 3.x removes `werkzeug.urls.url_quote`, CI fails | TC3 |

CI (`.github/workflows/ci.yml`) uses Python 3.12, installs the requirements and runs `pytest` on every push and pull request. The agent reads this CI result to decide whether an upgrade PR is passing or failing.
