from sqlalchemy.orm import Session

from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.security.password import hash_password
from app.models.user import User
from app.security.password import verify_password
from app.security.jwt import create_access_token

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

    @staticmethod
    def login_user(
        db: Session,
        email: str,
        password: str,
    ):
        user = UserRepository.get_by_email(
            db,
            email,
        )

        if not user:
            raise ValueError("Invalid email or password")

        if not verify_password(
            password,
            user.hashed_password,
        ):
            raise ValueError("Invalid email or password")

        access_token = create_access_token(
            data={
                "sub": user.email
            }
        )

        return {
            "access_token": access_token,
            "token_type": "bearer",
        }

        