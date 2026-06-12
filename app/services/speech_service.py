import speech_recognition as sr
from app.config import settings


class SpeechService:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def record_audio(self) -> sr.AudioData:
        with sr.Microphone() as source:
            print("🎤 Adjusting for ambient noise...")
            self.recognizer.adjust_for_ambient_noise(
                source,
                duration=settings.NOISE_ADJUSTMENT_DURATION
            )
            print("🎤 Listening... Speak now!")
            audio = self.recognizer.listen(
                source,
                timeout=settings.MICROPHONE_TIMEOUT
            )
        return audio

    def transcribe(self, audio: sr.AudioData) -> str:
        try:
            return self.recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Could not understand the audio."
        except sr.RequestError as e:
            return f"Speech recognition error: {str(e)}"
        except sr.WaitTimeoutError:
            return "No speech detected within timeout."

    def record_and_transcribe(self) -> str:
        audio = self.record_audio()
        return self.transcribe(audio)


speech_service = SpeechService()