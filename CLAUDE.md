# vBrownBag Pipeline — Project Context

## What This Project Is

A video automation pipeline for the vBrownBag YouTube channel. It processes a
video title and generates a YouTube description, tags, and a LinkedIn post —
all powered by Claude AI via the Anthropic API.

This is also a structured learning project — built incrementally to teach
Python and software architecture from the ground up.

## Learner Context

- Python level: between beginner and intermediate (assessed — see skill map in
  the Claude.ai tutor project)
- Primary gap: software architecture — understanding *why* code is structured
  the way it is, not just how to write it
- Infrastructure background is strong — use cloud/infra analogies freely
- Explain *why* before *how*, always
- Prefer explicit, readable code over clever/terse code
- Include inline comments explaining *why*, not just *what*
- Introduce new concepts gradually — don't refactor toward patterns that
  haven't been taught yet

## Current Phase

Phases 1–5 complete. Currently hardening and cleaning up before Phase 6.

### Completed
- Phase 1: Foundations (uv, pyproject.toml, .env, package structure)
- Phase 2: FastAPI web interface with Jinja2 templating
- Phase 3: Anthropic API integration
- Phase 4: Service layer pattern (routes → services → agents)
- Phase 5: Multiple agents (description, tags, LinkedIn)

### Up Next
- Phase 6: Real-time progress tracking (Server-Sent Events)
- Phase 7: Token cost tracking per run
- Phase 8: Logging, testing, hardening

## Tooling Stack

- Python 3.12+
- uv for package management (not pip)
- FastAPI for the web layer
- Jinja2 for HTML templating
- python-multipart for form handling
- Anthropic Python SDK for LLM calls
- python-dotenv for environment variable loading
- SQLModel for database (coming in Phase 7)
- Git + GitHub for version control

## Project Structure

```
vbrownbag-pipeline/
├── main.py                  # Entry point — loads env vars, starts server, registers routes
├── pyproject.toml           # Project manifest and dependencies
├── uv.lock                  # Pinned dependency versions, always commit this
├── .env.example             # Template for required environment variables, commit this
├── .env                     # Actual secrets, never commit this
├── CLAUDE.md                # This file — context for AI assistants
├── README.md                # Project overview for humans
├── templates/               # Jinja2 HTML templates
│   └── index.html           # Main web interface — form input and results display
└── app/                     # The application package
    ├── api/
    │   └── routes.py        # FastAPI routes — HTTP in/out only, no business logic
    ├── services/
    │   └── video.py         # Orchestrates the agent pipeline for a given video title
    └── agents/
        ├── description.py   # Generates a YouTube description via Claude
        ├── tags.py          # Generates YouTube tags via Claude
        └── linkedin.py      # Generates a LinkedIn post via Claude
```

## Architecture

The project uses a three-layer architecture:

- `api/` — receives HTTP requests and returns responses. No business logic.
- `services/` — orchestrates the work. Calls agents in sequence, handles errors.
- `agents/` — each file has one job: call the Anthropic API and return a result.

Data flows like this:
```
HTTP request → routes.py → services/video.py → agents/* → Anthropic API
                                                         ↓
HTTP response ← routes.py ← services/video.py ← agents/* ←┘
```

## Conventions

- Never commit `.env`
- Always run `uv sync` after pulling to ensure dependencies are current
- Add new packages with `uv add <package>`, never `pip install`
- Each agent handles its own Anthropic-specific exceptions and re-raises as ValueError
- The service layer catches ValueError and returns a dict with an `"error"` key
- The template checks for `result.error` before rendering results