from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('owner', 'Owner'),
        ('karigar', 'Karigar'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='karigar')

    def __str__(self):
        return f"{self.username} ({self.role})"
