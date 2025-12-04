from fastapi import FastAPI
from .routers import auth_router, crop_router, ml_router, voice_router
from .db import Base, engine
from . import models
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="Plantage Backend")

# create tables (for dev only; use alembic in production)
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router.router)
app.include_router(crop_router.router)
app.include_router(ml_router.router)
app.include_router(voice_router.router)

@app.get("/")
def root():
    return {"status":"ok"}
