from typing import Optional

from pydantic import BaseModel
from app.serializers.user import UserResponse
from app.serializers.department import DepartmentResponse


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
        from_attributes = True


class EmployeeDetail(EmployeeBase):
    id: int
    uid: str
    user: UserResponse
    department: DepartmentResponse

    class Config:
        from_attributes = True
