from fastapi import FastAPI
from fastapi import HTTPException

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok v0.2"}


@app.get("/health")
def health():
    #raise HTTPException(status_code=500)
    return {"status": "ok"}


