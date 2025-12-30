from pydantic import BaseModel


class SummaryRequest(BaseModel):
    content: str


class SummaryResponse(BaseModel):
    summary: str