from datetime import datetime

from pydantic import BaseModel, ConfigDict


class EchoCreate(BaseModel):
    title: str
    description: str
    latitude: float
    longitude: float
    location_name: str
    visibility: str = "public"


class EchoResponse(BaseModel):
    id: int
    title: str
    description: str
    latitude: float
    longitude: float
    location_name: str
    visibility: str
    image_url: str | None
    creator_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)