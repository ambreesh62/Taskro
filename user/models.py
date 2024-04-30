from django.db import models
from base.models import BaseModel
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(("Name"), max_length=50)
    role_title = models.CharField(("Role Title"),max_length=50, blank=True)
    dept = models.CharField(max_length=50, blank=True)
    employee_no = models.CharField(("Employee No"), max_length=50, blank=True)
    
    def __str__(self) -> str:
        return self.name