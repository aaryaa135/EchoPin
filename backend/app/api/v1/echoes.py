from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.models.user import User
from app.schemas.echo import EchoCreate, EchoResponse
from app.security.dependencies import get_current_user
from app.services.echo_service import EchoService

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