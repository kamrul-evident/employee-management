from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from passlib.context import CryptContext
from models.base import (
    BaseModelWithUUID,
)  # Assuming the base model is in app/models/base.py

# Initialize password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(BaseModelWithUUID):
    __tablename__ = "users"  # Define the name of the table

    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(
        Boolean, default=True
    )  # User's active status (can be False for deactivated users)
    is_admin = Column(
        Boolean, default=False
    )  # User's admin status (can be True for admin users)
    role = Column(String, default="employee")  # User's role (e.g., employee, admin)

    # Relationship with the Employee model
    employee = relationship(
        "Employee", backref="user", uselist=False
    )  # One-to-one relationship with Employee

    def __repr__(self):
        return f"<User {self.email}> Role: {self.role}"

    def set_password(self, password: str):
        """Hash the password and store it"""
        self.hashed_password = pwd_context.hash(password)

    def verify_password(self, password: str) -> bool:
        """Verify a password against the stored hash"""
        return pwd_context.verify(password, self.hashed_password)
