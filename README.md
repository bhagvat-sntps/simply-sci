# simply-sci

A FastAPI service to summarize research papers in simple terms.

## Features
- FastAPI app entrypoint in [app/main.py](app/main.py) with [`app.main.create_app`](app/main.py) and [`app.main.app`](app/main.py).
- Health endpoint router in [app/api/health/health.py](app/api/health/health.py) via [`app.api.health.health.router`](app/api/health/health.py) and handler [`app.api.health.health.health_check`](app/api/health/health.py).
- Centralized config in [app/core/config.py](app/core/config.py) using [`app.core.config.Settings`](app/core/config.py) and instance [`app.core.config.settings`](app/core/config.py).

## Requirements
- Python >= 3.14
- Dependencies: FastAPI, Uvicorn (plus Pydantic for settings in [app/core/config.py](app/core/config.py)).

## Quickstart
- Create a virtual environment and install:
  - `pip install .`
  - If needed: `pip install pydantic`
- Run the API:
  - `uvicorn app.main:app --reload`
- Open API docs:
  - `http://localhost:8000/docs`

## Configuration
- Environment variables (loaded by [`app.core.config.Settings`](app/core/config.py)):
  - `PROJECT_NAME` (default: MyAwesomeApp)
  - `DATABASE_URL`
  - `SECRET_KEY`
- Create a `.env` file in the project root (see `.env.example`):

PROJECT_NAME=simply-sci
DATABASE_URL=postgresql://user:pass@host:5432/dbname
SECRET_KEY=your-secret

## API
- Health: `GET /health/` → `{"status": "ok"}` implemented in [`app.api.health.health.health_check`](app/api/health/health.py).

## Project Structure
- `app/api/...`: API routers (health, future summarization endpoints).
- `app/core/...`: config, logging, security.
- `app/db/...`: database base and session (future use).
- `app/middleware/...`: request ID middleware (future use).

## Development
- Edit the active app in VS Code and use the integrated terminal:
  - Run: `uvicorn app.main:app --reload`
  - Logs and output appear in the Output panel.