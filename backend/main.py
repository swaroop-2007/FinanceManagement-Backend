from fastapi import FastAPI, HTTPException, Depends 
from typing import Annotated 
from sqlalchemy.orm import Session 
from pydantic import BaseModel 
from database import SessionLocal, engine 
import models 
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Our frontend will run on port 3000 and our CORS middleware will take care of it.
origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
)
