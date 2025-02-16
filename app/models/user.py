from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from passlib.context import CryptContext
from .base import (
    BaseModelWithUUID,
)  # Assuming the base model is in app/models/base.py

# Initialize password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(BaseModelWithUUID):
    __tablename__ = "users"

    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    role = Column(String, default="employee")

    # Not every User has to be an Employee, so no backref on the User side

    def __repr__(self):
        return f"<User {self.email}> Role: {self.role}"

    def set_password(self, password: str):
        """Hash the password and store it"""
        self.hashed_password = pwd_context.hash(password)

    def verify_password(self, password: str) -> bool:
        """Verify a password against the stored hash"""
        return pwd_context.verify(password, self.hashed_password)