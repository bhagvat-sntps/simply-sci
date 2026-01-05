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

[Quick example from docs/example.md](./docs/example.md):

```bash
curl -X POST 'http://localhost:8000/summary/' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <YOUR_TOKEN>' \
  -d '{
    "content": "High-precision transmission spectroscopy of temperate super-Earth exoplanets has revealed atmospheric features inconsistent with chemical equilibrium predictions. In this work, we analyze multi-epoch observations obtained with space-based infrared instruments using a hierarchical Bayesian retrieval framework. The inferred molecular abundances suggest the presence of photochemically driven disequilibrium processes, vertical mixing, and possible aerosol formation. While no definitive biosignatures are identified, the observed atmospheric complexity challenges existing models of terrestrial exoplanet evolution."
  }'
```

Expected response:

```json
{
	"title": "Studying the Atmospheres of Super-Earth Exoplanets",
	"summary": {
		"problem": "Scientists want to understand the atmospheres of super-Earth exoplanets, which are planets outside our solar system that are larger than Earth.",
		"goal": "The goal is to find out if the chemical makeup of these atmospheres matches what we expect based on scientific models.",
		"what_they_did": "Researchers used advanced space-based tools to observe these planets multiple times and analyzed the data using a special method called Bayesian retrieval.",
		"what_they_found": "They found that the chemical compositions of the atmospheres do not match predictions, suggesting complex processes are happening, like mixing of gases and possible formation of tiny particles.",
		"why_it_matters": "These findings challenge our current understanding of how planets like Earth evolve and could have implications for finding signs of life on other planets."
	},
	"seo_keywords": [
		"super-Earth exoplanets",
		"atmospheric features",
		"chemical equilibrium",
		"Bayesian retrieval",
		"planetary evolution"
	]
}
```

See more examples in docs/examples.md.

## Whats Next
- Add database to store open api req/res
- improve api request time
- understand LLM api attributes
- deploy using ketee (docker+kubernetes)

