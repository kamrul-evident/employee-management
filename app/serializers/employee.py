from typing import Optional

from pydantic import BaseModel


class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str
    job_title: str
    department_id: int


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeOut(EmployeeBase):
    id: int
    uid: str

    class Config:
        orm_mode = True
