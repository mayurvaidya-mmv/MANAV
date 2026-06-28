"""
Piper Speech Synthesizer

Temporary implementation.
"""

from voice.speech_synthesizer import SpeechSynthesizer


class PiperSynthesizer(SpeechSynthesizer):

    def speak(self, text: str):

        print()

        print("🔊 MANAS says:")

        print(text)

        print()