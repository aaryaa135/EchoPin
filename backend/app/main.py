from fastapi import FastAPI
from sqlalchemy import text

from app.core.settings import settings
from app.db.database import engine

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)


@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.APP_NAME} 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "app": settings.APP_NAME,
    }


@app.get("/database")
def database_check():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        version = result.scalar()

    return {
        "database": "Connected",
        "postgres_version": version,
    }