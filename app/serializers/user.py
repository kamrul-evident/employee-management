from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    role: str = "employee"
    is_active: bool = True
    is_admin: bool = False


class UserPost(UserBase):
    password: str


class UserList(UserBase):
    id: int
    uid: str

    class Config:
        orm_mode = True
