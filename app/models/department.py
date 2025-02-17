from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from .base import NameSlugDescriptionBaseModel


class Department(NameSlugDescriptionBaseModel):
    __tablename__ = "departments"

    def __repr(self):
        return f"ID: {self.id} Name: {self.name}"
