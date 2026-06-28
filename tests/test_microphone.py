from voice.audio_recorder import AudioRecorder

recorder = AudioRecorder()

filename = recorder.record()

print()

print("Recording saved as:", filename)