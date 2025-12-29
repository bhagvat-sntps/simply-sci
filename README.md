# simply-sci

A FastAPI service to summarize research paper abstract in simple terms.

## Tech Stack
- FastAPI (API framework)
- Uvicorn (ASGI server)
- Poetry (dependency and environment management)


## Requirements
- Python >= 3.14
- Dependencies: FastAPI, Uvicorn , Poetry, Pydantic 

## Quickstart
- Install dependencies
  - `poetry install` 
- Run the API:
  - `poetry run uvicorn app.main:app --reload`
- Open API docs:
  - `http://localhost:8000/docs`


## Project Structure
- `app/api/...`: API routers (health, future summarization endpoints).
- `app/core/...`: config, logging, security.
- `app/db/...`: database base and session (future use).
- `app/middleware/...`: request ID middleware (future use).

