from fastapi import FastAPI

app = FastAPI(
    title="JobPilot AI",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {
        "message": "Welcome to JobPilot AI"
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }