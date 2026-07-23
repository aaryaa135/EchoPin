from fastapi import FastAPI

app = FastAPI(
    title="EchoPin API",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to EchoPin 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }