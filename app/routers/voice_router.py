from fastapi import APIRouter, Depends, Form
from ..services.voice_service import text_to_speech
from fastapi.responses import FileResponse
from .. import auth

router = APIRouter(prefix="/voice", tags=["voice"])

@router.post("/tts")
def tts(text: str = Form(...), current_user=Depends(auth.get_current_user)):
    mp3_path = text_to_speech(text)
    return FileResponse(mp3_path, media_type="audio/mpeg")
