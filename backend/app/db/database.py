from sqlalchemy import create_engine

from app.core.settings import settings
from app.db.base import Base

DATABASE_URL = (
    f"postgresql+psycopg://"
    f"{settings.DATABASE_USER}:"
    f"{settings.DATABASE_PASSWORD}@"
    f"{settings.DATABASE_HOST}:"
    f"{settings.DATABASE_PORT}/"
    f"{settings.DATABASE_NAME}"
)

engine = create_engine(
    DATABASE_URL,
    echo=True,
)

# Import models so SQLAlchemy registers them
import app.models  # noqa: E402,F401
