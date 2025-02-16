from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.serializers.user import UserOut, UserPost, UserList

from app.controllers.user import create_user, user_list

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", tags=["users"])
async def get_users(db: Session = Depends(get_db)):
    return await user_list(db)


@router.post("/", tags=["users"])
async def user_create(payload: UserPost, db=Depends(get_db)):
    return await create_user(payload=payload, db=db)


user_routes = router
