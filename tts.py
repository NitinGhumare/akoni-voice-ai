from gtts import gTTS

def speak(text):

    tts = gTTS(text=text, lang="en")

    output_file = "response.mp3"

    tts.save(output_file)

    return output_file