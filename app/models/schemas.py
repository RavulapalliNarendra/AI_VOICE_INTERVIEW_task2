from pydantic import BaseModel

class QuestionRequest(BaseModel):
    question: str

    class Config:
        json_schema_extra = {
            "example": {"question": "Explain REST APIs"}
        }

class InterviewResponse(BaseModel):
    question: str
    transcript: str
    score: int
    max_score: int = 10
    keywords_matched: list[str]
    status: str

class InterviewSummary(BaseModel):
    total_questions: int
    total_score: int
    max_possible_score: int
    percentage: float
    results: list[InterviewResponse]

class HealthResponse(BaseModel):
    status: str
    app_name: str
    version: str