from pydantic import BaseModel, Field


class SummaryRequest(BaseModel):
    content: str


class SimpleSummary(BaseModel):
    problem: str
    goal: str
    what_they_did: str
    what_they_found: str
    why_it_matters: str


class AbstractSummaryResponse(BaseModel):
    title: str
    summary: SimpleSummary
    seo_keywords: list[str]