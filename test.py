from django.db import models
import uuid


class BaseModelWithUID(models.Model):
    uid = models.CharField(unique=True, db_index=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(BaseModelWithUID):
    email = models.EmailField(unique=True, blank=False)
    role = models.CharField(max_length=30, default="employee")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)


class Department(BaseModelWithUID):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=2000)


class Employee(BaseModelWithUID):
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="department_employees"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_employee"
    )
    first_name = models.CharField(max_length=64, blank=True)
    last_name = models.CharField(max_length=64, blank=True)
    phone = models.CharField(max_length=20)
    designation = models.CharField(max_length=100, blank=True)
