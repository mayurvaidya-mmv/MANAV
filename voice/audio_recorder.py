"""
Audio Recorder

Records audio from the microphone.
"""

import sounddevice as sd
import soundfile as sf


class AudioRecorder:

    def record(

        self,

        filename="recording.wav",

        duration=5,

        samplerate=16000

    ):

        print(f"\n🎤 Listening for {duration} seconds...")

        audio = sd.rec(

            int(duration * samplerate),

            samplerate=samplerate,

            channels=1,

            dtype="float32"

        )

        sd.wait()

        sf.write(

            filename,

            audio,

            samplerate

        )

        print(f"Saved to {filename}")

        return filename