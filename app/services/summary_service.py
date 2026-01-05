from app.gateways.openai_gateway import OpenAIGateway
from app.schemas.summary import AbstractSummaryResponse


class SummaryService:
    def __init__(self):
        self.gateway = OpenAIGateway()

    async def summarize_abstract(
        self, content: str, authorization: str
    ) -> AbstractSummaryResponse:
        return await self.gateway.summarize(content, authorization)
