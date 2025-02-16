from typing import Optional, List
from pydantic import BaseModel
from .employee import EmployeeOut


class DepartmentBase(BaseModel):
    name: str
    slug: str


class DepartmentCreate(DepartmentBase):
    pass


class DeparmentOut(DepartmentBase):
    id: int
    uid: str
    employees: List[EmployeeOut] = []

    class Config:
        orm_mode = True
