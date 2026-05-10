from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok v0.2"}


@app.get("/health")
def health():
    return {"status": "broken"}


