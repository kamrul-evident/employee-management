from typing import Optional

from pydantic import BaseModel


class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str
    job_title: str
    department_id: int


class EmployeePost(EmployeeBase):
    password: str


class EmployeeUpdate(EmployeeBase):
    pass


class EmployeeResponse(EmployeeBase):
    id: int
    uid: str
    user_id: int

    class Config:
        orm_mode = True
