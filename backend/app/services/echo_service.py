from sqlalchemy.orm import Session

from app.repositories.echo_repository import EchoRepository
from app.schemas.echo import EchoCreate
from fastapi import HTTPException, status

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

    @staticmethod
    def get_all_echoes(
        db,
        page: int,
        limit: int,
    ):

        skip = (page - 1) * limit

        echoes = EchoRepository.get_all(
            db=db,
            skip=skip,
            limit=limit,
        )

        total = EchoRepository.count(db)

        return {
            "items": echoes,
            "page": page,
            "limit": limit,
            "total": total,
            "has_next": skip + limit < total,
        }

    @staticmethod
    def get_echo_by_id(
        db,
        echo_id: int,
    ):

        echo = EchoRepository.get_by_id(
            db=db,
            echo_id=echo_id,
        )

        if echo is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Echo not found.",
            )

        return echo