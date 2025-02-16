from http import HTTPStatus

from fastapi.responses import ORJSONResponse
from pydantic import ValidationError
from sqlalchemy.orm import Session, defer
import orjson

from app.models.user import User
from app.serializers.user import UserBase, UserPost, UserList


async def create_user(payload: UserPost, db: Session):
    try:
        user = db.query(User).filter_by(email=payload.email).first()
        if user:
            return ORJSONResponse(
                content={"message": "User with this email already exists"},
                status_code=HTTPStatus.OK,
            )

        user = User(
            email=payload.email,
            role=payload.role,
            is_active=payload.is_active,
            is_admin=payload.is_admin,
        )
        user.set_password(password=payload.password)
        db.add(user)
        db.commit()
        db.refresh(user)

        return ORJSONResponse(
            content={
                "uid": user.uid,
                "email": user.email,
                "role": user.role,
                "created_at": user.created_at,
            },
            status_code=HTTPStatus.CREATED,
        )

    except ValidationError as e:
        return ORJSONResponse(
            content={"error": e.errors()}, status_code=HTTPStatus.UNPROCESSABLE_ENTITY
        )


async def user_list(db: Session):
    users = db.query(User).all()
    return {"users": users}
