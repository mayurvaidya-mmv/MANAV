from voice.whisper_recognizer import WhisperRecognizer

recognizer = WhisperRecognizer()

text = recognizer.transcribe("recording.wav")

print()

print("=" * 60)

print(text)

print("=" * 60)