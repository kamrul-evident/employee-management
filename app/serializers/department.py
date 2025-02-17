from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel


class DepartmentBase(BaseModel):
    name: str


class DepartmentPost(DepartmentBase):
    description: str


class DeparmentResponse(DepartmentBase):
    id: int
    uid: str
    slug: str
    description: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
