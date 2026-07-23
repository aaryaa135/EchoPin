from sqlalchemy.orm import Session

from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.security.password import hash_password
from app.models.user import User


class UserService:
    @staticmethod
    def register_user(
        db: Session,
        user_data: UserCreate,
    ) -> User:

        existing_user = UserRepository.get_by_email(
            db,
            user_data.email,
        )

        if existing_user:
            raise ValueError("Email already registered")

        hashed_password = hash_password(
            user_data.password
        )

        return UserRepository.create(
            db=db,
            full_name=user_data.full_name,
            email=user_data.email,
            hashed_password=hashed_password,
        )