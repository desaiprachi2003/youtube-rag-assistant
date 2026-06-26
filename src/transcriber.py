from faster_whisper import WhisperModel

model = WhisperModel( "small", device="cpu", compute_type="int8")


def transcribe_audio(audio_file):
    segments, info = model.transcribe(audio_file, task="translate", beam_size=5)

    

    return " ".join(segment.text.strip() for segment in segments)