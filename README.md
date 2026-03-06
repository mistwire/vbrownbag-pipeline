# vBrownBag Pipeline

A video automation pipeline for the [vBrownBag YouTube channel](https://www.youtube.com/vbrownbag). Point it at a video title and it generates a description, tags, and a LinkedIn post — all powered by Claude AI.

This is also a structured Python learning project, built incrementally to teach software architecture from the ground up. If you're following along, the commit history tells the story of how it was built and why decisions were made along the way.

---

## What It Does

Submit a video title through the web interface and the pipeline:

1. Generates a YouTube description
2. Generates a set of tags
3. Writes a LinkedIn post

Each of those is handled by a separate AI agent. The web interface shows all three results on a single page.

---

## Why It's Structured This Way

The project uses a three-layer architecture — and the separation is intentional:

```
app/
├── api/         # HTTP layer — receives requests, returns responses. No business logic.
├── services/    # Orchestration layer — coordinates the agents, owns the workflow.
└── agents/      # AI layer — each file has one job: talk to the LLM and return a result.
```

Think of it like a hospital:
- `api/` is the reception desk — it routes incoming requests but doesn't do the work
- `services/` is the medical staff — it decides what needs to happen and in what order
- `agents/` are the specialists — each one does one thing well

This separation means you can swap out any layer without touching the others. If you wanted to replace the Anthropic API with a different LLM, you'd only change the agents. If you wanted to add a CLI interface alongside the web interface, you'd only touch the API layer.

---

## Project Structure

```
vbrownbag-pipeline/
├── main.py                  # Entry point — starts the server, loads env vars
├── pyproject.toml           # Project manifest and dependencies (managed by uv)
├── uv.lock                  # Pinned dependency versions — always commit this
├── .env.example             # Template for required environment variables
├── .env                     # Your actual secrets — never commit this
├── CLAUDE.md                # Context file for AI assistants working in this repo
├── templates/               # Jinja2 HTML templates
│   └── index.html           # Main web interface
└── app/
    ├── api/
    │   └── routes.py        # FastAPI routes
    ├── services/
    │   └── video.py         # Video processing orchestration
    └── agents/
        ├── description.py   # Generates YouTube descriptions
        ├── tags.py          # Generates video tags
        └── linkedin.py      # Generates LinkedIn posts
```

---

## Getting Started

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) for package management
- An [Anthropic API key](https://console.anthropic.com)

### Setup

```bash
# Clone the repo
git clone https://github.com/mistwire/vbrownbag-pipeline.git
cd vbrownbag-pipeline

# Install dependencies
uv sync

# Set up your environment variables
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY

# Start the server
uv run uvicorn main:app --reload
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## Tooling

| Tool | Purpose |
|------|---------|
| [FastAPI](https://fastapi.tiangolo.com) | Web framework — handles HTTP routing and serving HTML |
| [Jinja2](https://jinja.palletsprojects.com) | Templating engine — renders HTML with dynamic data |
| [Anthropic SDK](https://github.com/anthropic/anthropic-sdk-python) | Python client for the Claude API |
| [uv](https://docs.astral.sh/uv/) | Fast, modern Python package manager |
| [python-dotenv](https://github.com/theskumar/python-dotenv) | Loads `.env` files into environment variables |

---

## Roadmap

- [x] Project foundations (uv, FastAPI, folder structure)
- [x] Web interface with Jinja2 templating
- [x] Anthropic API integration
- [x] Multi-agent pipeline (description, tags, LinkedIn)
- [ ] Real-time progress tracking (Phase 6)
- [ ] Token cost tracking per run (Phase 7)
- [ ] Logging and hardening (Phase 8)

---

## Contributing

This is a personal learning project — but if you're from the vBrownBag community and want to follow along or suggest improvements, issues and PRs are welcome.