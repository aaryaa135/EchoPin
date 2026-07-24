from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from app.models.enums import Visibility


class EchoCreate(BaseModel):
    title: Annotated[
        str,
        Field(min_length=3, max_length=100)
    ]

    description: Annotated[
        str,
        Field(min_length=5, max_length=1000)
    ]

    latitude: Annotated[
        float,
        Field(ge=-90, le=90)
    ]

    longitude: Annotated[
        float,
        Field(ge=-180, le=180)
    ]

    location_name: Annotated[
        str,
        Field(min_length=2, max_length=255)
    ]

    visibility: Visibility = Visibility.PUBLIC


class EchoResponse(BaseModel):
    id: int
    title: str
    description: str
    latitude: float
    longitude: float
    location_name: str
    visibility: Visibility
    image_url: str | None
    creator_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)