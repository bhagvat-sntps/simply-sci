from app.gateways.openai_gateway import OpenAIGateway

class SummaryService:
    def __init__(self):
        self.gateway = OpenAIGateway()

    async def summarize_abstract(self, content: str) -> str:
        # future logic:
        # - validate size
        # - cache
        # - chunk large content
        # - choose model dynamically
        return await self.gateway.summarize(content)