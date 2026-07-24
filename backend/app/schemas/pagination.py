from pydantic import BaseModel

from app.schemas.echo import EchoResponse


class PaginatedEchoResponse(BaseModel):
    items: list[EchoResponse]
    page: int
    limit: int
    total: int
    has_next: bool