from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from helper.cards.crud import models
from helper.database import engine
from helper.settings import settings

from .api import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)
