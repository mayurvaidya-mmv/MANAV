"""
Voice Manager
"""
from voice.speech_recognizer import SpeechRecognizer
from voice.speech_synthesizer import SpeechSynthesizer


class VoiceManager:

    def __init__(

        self,

        recognizer: SpeechRecognizer,
        synthesizer: SpeechSynthesizer

    ):

        self.recognizer = recognizer
        self.synthesizer = synthesizer

    def listen(self):

        return self.recognizer.listen()

    def speak(self, text):

        self.synthesizer.speak(text)