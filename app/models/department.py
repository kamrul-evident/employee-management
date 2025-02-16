from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base import NameSlugDescriptionBaseModel


class Department(NameSlugDescriptionBaseModel):
    __tablename__ = "departments"
    employees = relationship("Employee", backref="department", lazy="dynamic")

    def __repr__(self):
        return f"<Department {self.name}>"
