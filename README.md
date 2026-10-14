# AI Automation Portfolio: Mathuruban Manoharan

I design, run and harden **AI agent pipelines**: multi-step workflows where LLM agents research, write, review and publish, with hard quality gates and a human approval step wherever a mistake would be public.

**How I work:** I own the problem, the specification, the gates and the verification. **AI coding agents (Claude Code, Codex) write most of the code and scenario configuration** under my direction, and I check every result against logs, test runs and receipts before calling anything done. I say that openly because it is the skill: directing agents reliably is the job now.

| # | Project | Stack | Status | Evidence |
|---|---|---|---|---|
| 1 | [AI news-video pipeline](case-studies/01-ai-news-video-pipeline.md): RSS research → AI editorial agent + independent AI reviewer → voice → render → YouTube | Make, AI agents, ElevenLabs, Creatomate, Gemini, YouTube API, Buffer API | **Live** (daily run) | 90-module scenario ([generated diagram](architecture/ai-news-video-pipeline.md)), 11 public videos, metrics loop feeding the editor |
| 2 | [Fact-check video pipeline](case-studies/02-factcheck-video-pipeline.md): 5 stages, 14 scenarios, AI audiovisual QA gate | Make, LLM research/review agents, ElevenLabs, Creatomate, Gemini, Buffer | Built and audited, **paused by design** | 121 modules ([generated diagrams](architecture/factcheck-pipeline/)), governance audit with fixes |
| 3 | [Local multi-agent "company"](case-studies/03-local-multi-agent-company.md): CEO → department head → employee agents on a task ledger | Python 3.12, LangGraph, SQLite, llama.cpp, pytest | In progress | 17 tests passing, 5 skipped (Docker sandbox) |
| 4 | [Agentic job-search operations](case-studies/04-agentic-job-search-operations.md): browser agent with a human approval step per submission | Claude (browser + file agents), Markdown tracker, headless PDF rendering | In use | 18 tracked submissions, duplicate checks before each one |
| tool | [make-blueprint-inspector](tools/make-blueprint-inspector/): turns a Make scenario export into a **safe-to-share** architecture summary + Mermaid diagram | Python, pytest | Open source (MIT) | 6 tests incl. a secret-leak test |

## What the projects have in common

- **Gates before side effects.** Nothing renders, spends or publishes unless the record proves it is allowed: "Official HTTPS sources only", "No existing publication claim", "Uploaded bytes match downloaded bytes" are real filter names in these pipelines.
- **Idempotency.** Records are *claimed* before work starts, so a retry or a second run can't double-post or double-spend.
- **Independent review.** The agent that writes is not the agent that approves.
- **Honest status.** Every project separates *built*, *tested*, *live* and *earning*. Numbers below are as measured, including the unimpressive ones.

## Contact

Niederweningen (near Zurich), Switzerland · mathuruban.ch@gmail.com · English (working language), German (conversational)
