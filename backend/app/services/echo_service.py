from sqlalchemy.orm import Session

from app.repositories.echo_repository import EchoRepository
from app.schemas.echo import EchoCreate
from fastapi import HTTPException, status
from app.schemas.echo import EchoUpdate
from app.models.user import User

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

    @staticmethod
    def update_echo(
        db,
        echo_id: int,
        echo_data: EchoUpdate,
        current_user: User,
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

        if echo.creator_id != current_user.id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You are not allowed to update this Echo.",
            )

        update_data = echo_data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(echo, field, value)

        return EchoRepository.update(
            db=db,
            echo=echo,
        )

    @staticmethod
    def delete_echo(
        db,
        echo_id: int,
        current_user: User,
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

        if echo.creator_id != current_user.id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You are not allowed to delete this Echo.",
            )

        EchoRepository.delete(
            db=db,
            echo=echo,
        )