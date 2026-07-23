from sqlalchemy.orm import Session

from app.repositories.echo_repository import EchoRepository
from app.schemas.echo import EchoCreate


class EchoService:

    @staticmethod
    def create_echo(
        db: Session,
        echo_data: EchoCreate,
        creator_id: int,
    ):
        return EchoRepository.create(
            db=db,
            echo_data=echo_data,
            creator_id=creator_id,
        )