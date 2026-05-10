import os
from fastapi import FastAPI, HTTPException


app = FastAPI()


@app.get("/")
def read_root():
    return {
        "status": os.getenv("APP_STATUS"),
        "secret": os.getenv("APP_SECRET")
    }
    #return {"status": "ok v0.2"}


@app.get("/health")
def health():
    #raise HTTPException(status_code=500)
    return {"status": "ok"}


