# 3 · Local multi-agent "company" (in progress)

**Problem.** Run a hierarchy of AI agents (a CEO agent assigns objectives, department-head agents plan and review, employee agents implement) **locally**, on small open models, with every claim checkable and no runaway cost.

## Design

- **Task ledger (SQLite).** Every unit of work is a task with an owner, dependencies, a priority, a retry budget and an **idempotency key**, so seeding the same objectives twice creates nothing new.
- **Machine-checkable acceptance criteria per task**, for example `children_created ≥ 1`, `produced_json` with required keys, `citations_valid`. A task is done when its checks pass, not when an agent says so.
- **Supervisor** with start/pause/resume/stop scripts (being moved to a Windows Task Scheduler background service) and a status command that explains *what is waiting and why*.
- **Agents** (CEO, department head, employee) are LangGraph graphs with their own identity, memory scope and permissions. Small local models run through llama.cpp. A cloud model (Claude) is an optional backend behind a billing check that blocks dispatch until spending settings are verified.
- **Sandbox** for code execution in Docker; a redaction layer keeps secrets out of logs.

## Status (verified 14 Oct 2026)

- `pytest`: **17 passed, 5 skipped**. The 5 skips are the Docker sandbox tests, which are skipped (not faked) when the Docker engine is off.
- Done: ledger, supervisor, flags, the simulated Claude adapter, the bootstrap tests, and the first versions of the three agents.
- Next: local model benchmark (4B vs 9B), the end-to-end CEO → department head → employee demo, and a soak test.

**What it shows.** Agent systems need the boring parts: durable state, idempotency, acceptance checks, budgets and a kill switch. I start with those, not with the prompts.

*Code written by AI coding agents under my specification and review. The repository is private while the project is in progress; a walkthrough is available on request.*
