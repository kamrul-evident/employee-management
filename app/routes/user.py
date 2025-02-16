from fastapi import APIRouter, Depends, Request
from app.config.database import get_db
from app.serializers.user import UserList, UserPost

from app.controllers.user import create_user

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=UserList)
async def read_users(request: Request):
    return {"message": "Hello World"}


@router.post("/", tags=["users"])
async def user_create(payload: UserPost, db=Depends(get_db)):
    return await create_user(payload=payload, db=db)


user_routes = router
