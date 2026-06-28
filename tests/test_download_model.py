from faster_whisper import WhisperModel

print("Downloading model...")

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

print("Model ready.")