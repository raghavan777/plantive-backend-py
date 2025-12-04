from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from .. import schemas, models, auth
import shutil, os
from datetime import datetime

router = APIRouter(prefix="/crops", tags=["crops"])

@router.post("/", response_model=schemas.CropOut)
def create_crop(data: schemas.CropIn, current_user = Depends(auth.get_current_user), db: Session = Depends(auth.get_db)):
    crop = models.Crop(user_id=current_user.id, name=data.name, description=data.description)
    db.add(crop); db.commit(); db.refresh(crop)
    return crop

@router.post("/upload/{crop_id}", response_model=schemas.CropOut)
def upload_image(crop_id: int, file: UploadFile = File(...), current_user = Depends(auth.get_current_user), db: Session = Depends(auth.get_db)):
    crop = db.query(models.Crop).filter(models.Crop.id==crop_id, models.Crop.user_id==current_user.id).first()
    if not crop:
        raise HTTPException(404, "Crop not found")
    folder = "uploads"
    os.makedirs(folder, exist_ok=True)
    filename = f"{crop_id}_{int(datetime.utcnow().timestamp())}_{file.filename}"
    path = os.path.join(folder, filename)
    with open(path,"wb") as f:
        shutil.copyfileobj(file.file, f)
    crop.image_url = path
    db.commit(); db.refresh(crop)
    return crop
