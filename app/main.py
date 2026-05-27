from fastapi import FastAPI
import redis
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Backend Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}
