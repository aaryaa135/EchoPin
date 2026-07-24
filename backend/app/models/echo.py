from datetime import datetime, UTC

from sqlalchemy import DateTime, Float, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base

from sqlalchemy import Enum
from app.models.enums import Visibility

class Echo(Base):
    __tablename__ = "echoes"

    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    latitude: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    longitude: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    location_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    visibility: Mapped[Visibility] = mapped_column(
        Enum(
            Visibility,
            values_callable=lambda enum: [e.value for e in enum],
        ),
        default=Visibility.PUBLIC,
        nullable=False,
    )

    image_url: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
    )

    creator_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    creator = relationship(
        "User",
        back_populates="echoes",
    )