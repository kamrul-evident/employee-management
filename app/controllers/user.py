from http import HTTPStatus

from fastapi.responses import ORJSONResponse
from pydantic import ValidationError
from sqlalchemy.orm import Session
import orjson

from app.models.user import User
from app.serializers.user import UserPost, UserList


async def create_user(payload: UserPost, db: Session):
    try:
        user = db.query(User).filter_by(email=payload.email).first()
        if user:
            return ORJSONResponse(content={"message": "User with this email already exists"}, status_code=HTTPStatus.OK)
        
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

        return ORJSONResponse(content=orjson.dumps(user), status_code=HTTPStatus.CREATED)

    except ValidationError as e:
        return ORJSONResponse(
            content={"error": e.errors()}, status_code=HTTPStatus.UNPROCESSABLE_ENTITY
        )