from django.contrib.auth.models import AbstractUser
from django.db import models

from permissions.roles import ROLE_CHOICES

class User(AbstractUser):
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='user')

    def __str__(self):
        return f"{self.username} ({self.role})"
