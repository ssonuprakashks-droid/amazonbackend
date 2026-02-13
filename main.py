from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from db import get_db, DATABASE_URL, engine, Base
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# to create database
Base.metadata.create_all(engine)

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Hello World"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
