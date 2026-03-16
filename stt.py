import whisper

model = whisper.load_model("small")

def transcribe(audio_file):

    result = model.transcribe(audio_file, language="en")

    return result["text"]