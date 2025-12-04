from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class UserCreate(BaseModel):
    mobile: str
    password: str
    role: Optional[str] = "FARMER"

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserOut(BaseModel):
    id: UUID
    mobile: str
    role: str
    created_at: datetime

    class Config:
        orm_mode = True

class CropIn(BaseModel):
    name: str
    description: Optional[str] = None

class CropOut(BaseModel):
    id: int
    name: str
    description: Optional[str]
    image_url: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True
