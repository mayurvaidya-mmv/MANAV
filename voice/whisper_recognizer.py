"""
Whisper Speech Recognizer

Offline speech recognition using Faster-Whisper.
"""

from faster_whisper import WhisperModel

from voice.speech_recognizer import SpeechRecognizer


class WhisperRecognizer(SpeechRecognizer):

    def __init__(self):

        print("Loading Whisper model...")

        self.model = WhisperModel(

            "base",

            device="cpu",

            compute_type="int8"

        )

        print("Whisper ready.")

    def transcribe(self, audio_file: str) -> str:

        segments, info = self.model.transcribe(

            audio_file,

            beam_size=5

        )

        text = ""

        for segment in segments:

            text += segment.text + " "

        return text.strip()

    def listen(self):

        raise NotImplementedError(
            "Use AudioRecorder before live listening."
        )