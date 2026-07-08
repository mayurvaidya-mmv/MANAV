"""
Voice Interface for MANAS
"""

from core.application import MANAS
from core.config import Config

from voice.audio_recorder import AudioRecorder
from voice.whisper_recognizer import WhisperRecognizer
from voice.piper_synthesizer import PiperSynthesizer


def main():

    # Boot MANAS
    app = MANAS()

    app.boot()

    # Voice components
    recorder = AudioRecorder()

    recognizer = WhisperRecognizer()

    speaker = PiperSynthesizer()

    print("=" * 60)
    print("🎤 MANAS Voice Assistant v0.1")
    print("=" * 60)

    while True:

        choice = input(
            "\nPress ENTER to speak (or type 'quit'): "
        ).strip().lower()

        if choice == "quit":

            print("\nGoodbye!")

            break

        audio_file = recorder.record()

        command = recognizer.transcribe(audio_file).strip()

        print()

        print(f"🗣️ You said: {command}")

        if not command:

            print("\nI didn't hear anything.")

            continue

        # Whisper sometimes returns only punctuation
        if command.replace(".", "").strip() == "":

            print("\nSpeech not recognized.")

            continue

        if command.lower() in (

            "quit",

            "exit",

            "stop",

            "goodbye",

            "bye"

        ):

            print("\nGoodbye!")

            break

        result = app.process(command)

        if result is not None:

            print()

            print("=" * 70)

            print(f"Topic:\n{result.topic}\n")

            print(f"Summary:\n{result.summary}")

            speaker.speak(result.summary)

            print("=" * 70)


if __name__ == "__main__":

    main()