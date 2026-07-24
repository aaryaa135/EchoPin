from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.echo import Echo
from app.schemas.echo import EchoCreate
from sqlalchemy import func

class EchoRepository:

    @staticmethod
    def create(
        db: Session,
        echo_data: EchoCreate,
        creator_id: int,
    ) -> Echo:

        echo = Echo(
            title=echo_data.title,
            description=echo_data.description,
            latitude=echo_data.latitude,
            longitude=echo_data.longitude,
            location_name=echo_data.location_name,
            visibility=echo_data.visibility,
            creator_id=creator_id,
        )

        db.add(echo)
        db.commit()
        db.refresh(echo)

        return echo

    @staticmethod
    def get_all(
        db,
        skip: int,
        limit: int,
    ):
        stmt = (
            select(Echo)
            .order_by(Echo.created_at.desc())
            .offset(skip)
            .limit(limit)
        )

        return db.execute(stmt).scalars().all()

    @staticmethod
    def count(db):

        stmt = select(func.count()).select_from(Echo)

        return db.scalar(stmt)

    @staticmethod
    def get_by_id(
        db,
        echo_id: int,
    ):
        stmt = select(Echo).where(Echo.id == echo_id)

        return db.execute(stmt).scalar_one_or_none()

    @staticmethod
    def update(
        db,
        echo,
    ):
        db.add(echo)
        db.commit()
        db.refresh(echo)

        return echo
