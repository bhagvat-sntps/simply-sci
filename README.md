# simply-sci

A FastAPI service to summarize research paper abstract in simple terms and provide SEO keywords.

## Menu
- [Tech Stack](#tech-stack)
- [Requirements](#requirements)
- [Quickstart](#quickstart)
- [Project Structure](#project-structure)
- [API Docs](#api-docs)
- [Examples](#examples)
- [What's next](#whats-next)

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
- `app/api/...`: API routers
- `app/api/router.py`: single file to export route
- `app/core/...`: config, logging, security.
- `app/db/...`: database base and session (future use).
- `app/middleware/...`: common place for middleware

## API Docs
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Examples

Quick example (from docs/examples.md):

```bash
curl -X POST 'http://localhost:8000/summary/' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <YOUR_TOKEN>' \
  -d '{
    "content": "Paste the abstract text here"
  }'
```

Expected response:

```json
{
  "title": "Study on ...",
  "summary": {
    "problem": "...",
    "goal": "...",
    "what_they_did": "...",
    "what_they_found": "...",
    "why_it_matters": "..."
  },
  "seo_keywords": ["...", "..."]
}
```

See more examples in docs/examples.md.

## Whats Next
- Add database to store open api req/res
- improve api request time
- understand LLM api attributes
- deploy using ketee (docker+kubernetes)

