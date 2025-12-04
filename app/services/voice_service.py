# simple TTS using gTTS (requires internet) or pyttsx3 (offline)
from gtts import gTTS
import tempfile

def text_to_speech(text: str):
    tts = gTTS(text=text, lang="en")
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(tmp.name)
    return tmp.name
