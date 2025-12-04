from fastapi import APIRouter, File, UploadFile, Depends
from ..services import ml_service
from .. import auth

router = APIRouter(prefix="/ml", tags=["ml"])

@router.post("/disease-detect")
async def disease_detect(file: UploadFile = File(...), current_user=Depends(auth.get_current_user)):
    image_bytes = await file.read()
    res = ml_service.predict_image_bytes(image_bytes)
    return res

# Add endpoints for model2 and model3 similarly (yield prediction, fertilizer rec)
