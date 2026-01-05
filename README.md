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
- `app/api/...`: API routers (with versioning)
- `app/core/...`: config, logging, security.
- `app/models/...` : db models (future use)
- `app/schemas/...` : required dto (Data transfer object for ex: req signature object , response object etc)
-  `app/services/...` : common place for keeping business logic
- `app/db/...`: database base and session (future use).
- `migrations/...` : db migrations (future use)
- `app/middleware/...`: common place for middleware
- `app/gateways/...`: app external connection commom place (open api http call etc)
- `docs/...`: relevant docs

## API Docs
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Examples

### how to generate open api token


visit below docs  -> click <b>Use this model</b> --> click <b>Create Personal access token</b>

Update token to the below req header to test

[github marketplace / gpt 4o model](https://github.com/marketplace/models/azure-openai/gpt-4o/playground/code)

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

