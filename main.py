from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Vehicle Counter API is running"}

@app.get("/health")
def health():
    return {"ok": True}
