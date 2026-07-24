from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.models.user import User
from app.schemas.echo import EchoCreate, EchoResponse
from app.security.dependencies import get_current_user
from app.services.echo_service import EchoService
from app.schemas.pagination import PaginatedEchoResponse
from app.schemas.echo import EchoUpdate

from typing import Annotated

from fastapi import Query

router = APIRouter(
    prefix="/echoes",
    tags=["Echoes"],
)


@router.post(
    "",
    response_model=EchoResponse,
    status_code=201,
)
def create_echo(
    echo: EchoCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return EchoService.create_echo(
        db=db,
        echo_data=echo,
        creator_id=current_user.id,
    )

@router.get(
    "",
    response_model=PaginatedEchoResponse
)
def get_echoes(
    page: Annotated[int, Query(ge=1)] = 1,
    limit: Annotated[int, Query(ge=1, le=50)] = 10,
    db: Session = Depends(get_db),
):

    return EchoService.get_all_echoes(
        db=db,
        page=page,
        limit=limit,
    )

@router.get(
    "/{echo_id}",
    response_model=EchoResponse,
)
def get_echo(
    echo_id: int,
    db: Session = Depends(get_db),
):
    return EchoService.get_echo_by_id(
        db=db,
        echo_id=echo_id,
    )

@router.patch(
    "/{echo_id}",
    response_model=EchoResponse,
)
def update_echo(
    echo_id: int,
    echo_data: EchoUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return EchoService.update_echo(
        db=db,
        echo_id=echo_id,
        echo_data=echo_data,
        current_user=current_user,
    )