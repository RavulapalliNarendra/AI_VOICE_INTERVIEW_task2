from app.data.questions import ANSWER_KEYS


class EvaluationService:
    def evaluate(self, question: str, transcript: str, max_score: int = 10) -> dict:
        keywords = ANSWER_KEYS.get(question, [])
        transcript_lower = transcript.lower()

        matched = [kw for kw in keywords if kw in transcript_lower]

        score = round((len(matched) / len(keywords)) * max_score) if keywords else 0

        if score >= 8:
            status = "Excellent"
        elif score >= 6:
            status = "Good"
        elif score >= 4:
            status = "Average"
        else:
            status = "Needs Improvement"

        return {
            "score": score,
            "keywords_matched": matched,
            "status": status
        }


evaluation_service = EvaluationService()