# 🎤 AI Voice Interview Agent

An AI-powered Voice Interview Agent built using FastAPI, Speech Recognition, and Python. This project conducts voice-based technical interviews, converts speech to text, evaluates responses using keyword matching, and provides automated scoring.

---

## 📌 Features

* 🎙️ Voice-based interview system
* 🗣️ Speech-to-Text conversion
* 📊 Automated answer evaluation
* ⭐ Response scoring mechanism
* 📑 REST API with FastAPI
* 📚 Swagger API Documentation
* 🧪 Unit Testing with Pytest
* 🔧 Environment-based Configuration

---

## 🛠️ Tech Stack

* Python 3.11+
* FastAPI
* Uvicorn
* SpeechRecognition
* PyAudio
* Pydantic
* Pytest

---

## 📂 Project Structure

```text
ai_interview_agent/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── schemas.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── speech_service.py
│   │   └── evaluation_service.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py
│   └── data/
│       └── questions.py
│
├── tests/
│   ├── __init__.py
│   └── test_api.py
│
├── requirements/
│   ├── base.txt
│   ├── dev.txt
│   └── prod.txt
│
├── .env
├── .env.example
├── .gitignore
├── README.md
└── run.py
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/ai_interview_agent.git
cd ai_interview_agent
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements/dev.txt
```

---

## ⚙️ Environment Variables

Create a `.env` file:

```env
APP_NAME=AI Voice Interview Agent
APP_VERSION=1.0.0
APP_HOST=0.0.0.0
APP_PORT=8000
DEBUG=True
TOTAL_QUESTIONS=5
MICROPHONE_TIMEOUT=10
NOISE_ADJUSTMENT_DURATION=1
```

---

## ▶️ Run Application

```bash
python run.py
```

Server starts at:

```text
http://0.0.0.0:8000 
 to change it
http://127.0.0.1:8000
```

---

## 📖 API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
``

---

## 🔗 Available Endpoints

### Root Endpoint

```http
GET /
```

Response:

```json
{
  "message": "Welcome to AI Voice Interview Agent",
  "version": "1.0.0"
}
```

---

### Health Check

```http
GET /api/v1/health
```

---

### Get Interview Questions

```http
GET /api/v1/questions
```

---

### Conduct Interview

```http
POST /api/v1/interview
```

Request:

```json
{
  "question": "Explain REST APIs"
}
```

Response:

```json
{
  "question": "Explain REST APIs",
  "transcript": "REST API is an architectural style...",
  "score": 8,
  "keywords_matched": [
    "api",
    "http",
    "endpoint"
  ],
  "status": "Excellent"
}
```

---

### Full Interview Session

```http
POST /api/v1/interview/full
```

Returns complete interview summary and performance report.

---

## 🧪 Running Tests

```bash
pytest tests/ -v
```

Expected Output:

```text
4 passed in 1.23s
```

---

## 🎯 Sample Questions

* Explain REST APIs
* What is Machine Learning?
* What is Python?
* What is FastAPI?
* Explain OOP Concepts

---

## 📊 Evaluation Logic

The system evaluates answers using predefined keyword matching.

| Score Range | Result            |
| ----------- | ----------------- |
| 8 - 10      | Excellent         |
| 6 - 7       | Good              |
| 4 - 5       | Average           |
| 0 - 3       | Needs Improvement |

---

## 🔮 Future Enhancements

* AI-based answer evaluation using NLP
* OpenAI integration
* Candidate performance dashboard
* Voice emotion analysis
* Database integration
* Interview history tracking
* JWT Authentication

---

## 👨‍💻 Author

**Ravulapalli Narendra**

AI/ML Intern

---

## 📄 License

This project is developed for educational and internship purposes.
