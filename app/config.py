from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "AI Voice Interview Agent"
    APP_VERSION: str = "1.0.0"
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    DEBUG: bool = True
    TOTAL_QUESTIONS: int = 5
    MICROPHONE_TIMEOUT: int = 10
    NOISE_ADJUSTMENT_DURATION: int = 1

    class Config:
        env_file = ".env"

settings = Settings()