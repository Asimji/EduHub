from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# accounts/models.py

class CustomUser(AbstractUser):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
