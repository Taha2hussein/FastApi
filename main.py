from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.utils import get_current_user
from src.routes import authRouter
from src.utils import create_tables
from src.utils.protct_Route import get_current_user

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    print("created tables")
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(authRouter, prefix="/auth", tags=["auth"])

@app.get("/")   
async def root():
    return {"message": "Hello World"}
