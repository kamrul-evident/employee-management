from typing import Optional, List
from pydantic import BaseModel
from uuid import UUID


class UserBase(BaseModel):
    email: str
    role: str = "employee"
    is_active: bool = True
    is_admin: bool = False

    class Config:
        from_attributes = True


class UserPost(UserBase):
    password: str

class UserUpdate(BaseModel):
    email: Optional[str] = None
    role: Optional[str] = None
    is_active: Optional[bool] = None

class UserResponse(UserBase):
    id: int
    uid: UUID

    class Config:
        from_aatributes = True
