from typing import Optional, List
from pydantic import BaseModel
from .employee import EmployeeList


class DepartmentBase(BaseModel):
    name: str
    slug: str


class DepartmentPost(DepartmentBase):
    pass


class DeparmentList(DepartmentBase):
    id: int
    uid: str
    employees: List[EmployeeList] = []

    class Config:
        orm_mode = True
