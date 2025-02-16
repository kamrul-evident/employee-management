# from sqlalchemy import Column, String, Integer, ForeignKey
# from sqlalchemy.orm import relationship

# from .base import BaseModelWithUUID, NameSlugDescriptionBaseModel


# class Employee(BaseModelWithUUID):
#     __tablename__ = "employees"

#     first_name = Column(String, index=True)
#     last_name = Column(String, index=True)
#     email = Column(String, unique=True, index=True)
#     phone = Column(String, index=True)
#     job_title = Column(String)
#     department_id = Column(Integer, ForeignKey("departments.id"), nullable=True)

#     # Use 'employees' as the backref name in the Department model (this is handled in Department already)
#     department = relationship("Department", backref="employees", lazy="dynamic")

#     user_id = Column(Integer, ForeignKey("users.id"), nullable=True)  # Nullable to allow users who aren't employees
#     user = relationship("User", backref="employee", uselist=False)  # One-to-one relationship, but not required for all users

#     def __repr__(self):
#         return f"<Employee {self.first_name} {self.last_name} {self.job_title}>"