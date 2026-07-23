from sqlalchemy.orm import Session

from app.models.echo import Echo
from app.schemas.echo import EchoCreate


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