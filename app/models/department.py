# from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship
# from .base import NameSlugDescriptionBaseModel


# # Department Model
# class Department(NameSlugDescriptionBaseModel):
#     __tablename__ = "departments"
    
#     # Remove the 'employees' backref here, since it's already set in the Employee model
#     employees = relationship("Employee", lazy="dynamic", backref="department")

#     def __repr__(self):
#         return f"<Department {self.name}>"