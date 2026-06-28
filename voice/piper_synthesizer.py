"""
Piper Speech Synthesizer

Offline Text-to-Speech using Piper.
"""

import subprocess
from pathlib import Path

from voice.speech_synthesizer import SpeechSynthesizer


class PiperSynthesizer(SpeechSynthesizer):

    def __init__(self):

        self.base_dir = Path("piper")

        self.piper = self.base_dir / "piper.exe"

        self.model = (
            self.base_dir
            / "voices"
            / "en_US-lessac-high.onnx"
        )

        self.output = (
            self.base_dir
            / "output"
            / "speech.wav"
        )

    def speak(self, text: str):

        process = subprocess.run(

            [
                str(self.piper),

                "-m",
                str(self.model),

                "-f",
                str(self.output),
            ],

            input=text,

            text=True,

            capture_output=True

        )

        if process.returncode != 0:

            print(process.stderr)

            return

        subprocess.run(
            [
                "powershell",
                "-c",
                f"(New-Object Media.SoundPlayer '{self.output}').PlaySync();"
            ]
        )