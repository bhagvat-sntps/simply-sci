import httpx
import json
import re
from app.core.config import settings
from app.core.exception import ExternalServiceError
from app.schemas.summary import AbstractSummaryResponse

class OpenAIGateway:
    def __init__(self):
        self.client = httpx.AsyncClient(
            base_url="https://models.github.ai/inference",
            timeout=15.0,
            headers={
                "Authorization": f"Bearer {settings.API_TOKEN}",
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
        )

    async def aclose(self) -> None:
        await self.client.aclose()

    async def summarize(self, text: str) -> AbstractSummaryResponse:
        try:
            response = await self.client.post(
                "/chat/completions",
                json={
                    "model": "openai/gpt-4o-mini",
                    "temperature": 0.2,
                    "top_p": 1.0,
                    "max_tokens": 1000,
                    "messages": [
                        {
                            "role": "system",
                            "content": (
                                "You are an educational science explainer. "
                                "Explain research papers in simple, clear language that can be "
                                "understood by a 7–8 grade student or a general reader. "
                                "Use ONLY the information provided in the abstract. "
                                "Do not add new facts or assumptions. "
                                "Explain technical terms in simple words. "
                                "Use short sentences and everyday language. "
                                "If something is not mentioned, say 'Not mentioned in the abstract'."
                                "Create a clear, accurate title (not clickbait). "
                                "Generate 3 to 5 SEO-friendly keywords based only on the abstract."
                            ),
                        },
                        {
                            "role": "user",
                            "content": f"""
                            Read the following research paper abstract and write a simple summary that a general reader can understand.

                            Abstract:
                            {text}

                            Return the result strictly in JSON format:
                            {{
                              "title": "",
                              "summary": {{
                                "problem": "",
                                "goal": "",
                                "what_they_did": "",
                                "what_they_found": "",
                                "why_it_matters": ""
                              }},
                              "seo_keywords": []
                            }}
                            """
                        },
                    ],
                },
            )

            response.raise_for_status()
            payload = response.json()
            content = payload["choices"][0]["message"]["content"]

            # Try direct JSON->model
            try:
                return AbstractSummaryResponse.model_validate_json(content)
            except Exception:
                # Strip optional code fences if present
                cleaned = re.sub(r"^```(?:json)?\s*|\s*```$", "", content.strip())
                try:
                    data = json.loads(cleaned)
                except json.JSONDecodeError as e:
                    raise ExternalServiceError(
                        message="Gateway returned invalid JSON",
                        details=str(e),
                    ) from e
                return AbstractSummaryResponse.model_validate(data)

        except httpx.TimeoutException:
            raise ExternalServiceError(
                message="OpenAI timeout",
                details="Request to OpenAI timed out",
            )
        except httpx.HTTPStatusError as e:
            raise ExternalServiceError(
                message="OpenAI returned an error",
                status_code=e.response.status_code,
                details=e.response.text,
            )
        except Exception as e:
            raise ExternalServiceError(
                message="Unexpected OpenAI error",
                details=str(e),
            )