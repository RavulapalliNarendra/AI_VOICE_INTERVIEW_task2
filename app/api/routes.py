from fastapi import APIRouter, HTTPException
from app.models.schemas import (
    QuestionRequest, InterviewResponse,
    InterviewSummary, HealthResponse
)
from app.services.speech_service import speech_service
from app.services.evaluation_service import evaluation_service
from app.data.questions import QUESTIONS
from app.config import settings

router = APIRouter()


@router.get("/health", response_model=HealthResponse, tags=["Health"])
def health_check():
    return {
        "status": "healthy",
        "app_name": settings.APP_NAME,
        "version": settings.APP_VERSION
    }


@router.get("/questions", tags=["Interview"])
def get_questions():
    return {"total": len(QUESTIONS), "questions": QUESTIONS}


@router.post("/interview", response_model=InterviewResponse, tags=["Interview"])
def conduct_interview(request: QuestionRequest):
    if request.question not in QUESTIONS:
        raise HTTPException(
            status_code=400,
            detail="Invalid question. Use GET /api/v1/questions to see valid options."
        )

    print(f"\n📋 Question: {request.question}")
    transcript = speech_service.record_and_transcribe()
    print(f"📝 Transcript: {transcript}")

    evaluation = evaluation_service.evaluate(request.question, transcript)
    print(f"⭐ Score: {evaluation['score']}/10 — {evaluation['status']}")

    return InterviewResponse(
        question=request.question,
        transcript=transcript,
        score=evaluation["score"],
        keywords_matched=evaluation["keywords_matched"],
        status=evaluation["status"]
    )


@router.post("/interview/full", response_model=InterviewSummary, tags=["Interview"])
def full_interview():
    results = []
    total_score = 0

    for question in QUESTIONS:
        print(f"\n📋 Question: {question}")
        input("   Press ENTER when ready to answer...")

        transcript = speech_service.record_and_transcribe()
        evaluation = evaluation_service.evaluate(question, transcript)
        total_score += evaluation["score"]

        results.append(InterviewResponse(
            question=question,
            transcript=transcript,
            score=evaluation["score"],
            keywords_matched=evaluation["keywords_matched"],
            status=evaluation["status"]
        ))

    max_possible = 10 * len(QUESTIONS)
    return InterviewSummary(
        total_questions=len(QUESTIONS),
        total_score=total_score,
        max_possible_score=max_possible,
        percentage=round((total_score / max_possible) * 100, 2),
        results=results
    )