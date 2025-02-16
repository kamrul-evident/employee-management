from typing import Optional, List
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    role: str = "employee"
    is_active: bool = True
    is_admin: bool = False

    class Config:
        orm_mode = True
        from_attributes = True


class UserPost(UserBase):
    password: str


class UserOut(UserBase):
    id: int
    uid: str

    class Config:
        orm_mode = True


class UserList(UserBase):
    users: List[UserBase]

    class Config:
        orm_mode = True
        from_attributes = True
