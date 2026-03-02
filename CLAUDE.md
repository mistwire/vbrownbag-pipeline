# vBrownBag Pipeline — Project Context

## What This Project Is

A video automation pipeline for the vBrownBag YouTube channel. It processes a
video, generates thumbnails, creates social media posts, shows real-time agent
progress, and tracks token costs per run.

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

Phase 1 — Foundations & Project Structure (in progress)

## Tooling Stack

- Python 3.12+
- uv for package management (not pip)
- FastAPI for the web layer
- SQLModel for database (coming in Phase 7)
- Anthropic Python SDK for LLM calls (coming in Phase 3)
- Git + GitHub for version control

## Project Structure

(update this as folders are added — explain what each one is for)

- `main.py` — entry point, starts the server and registers routers
- `pyproject.toml` — project manifest and dependencies
- `uv.lock` — pinned dependency versions, always commit this
- `.env.example` — template for required environment variables, commit this
- `.env` — actual secrets, never commit this
- `app/` — the application package
  - `api/` — HTTP routes only, no business logic
    - `routes.py` — main router
  - `services/` — business logic (coming in Phase 4)
  - `agents/` — LLM agents (coming in Phase 5)

## Conventions

- Never commit `.env`
- Always run `uv sync` after pulling to ensure dependencies are current
- Add new packages with `uv add <package>`, never `pip install``