from fastapi import FastAPI

app = FastAPI(title="DarkoLab API")

@app.get("/health")
def health():
    return {"status": "ok"}
