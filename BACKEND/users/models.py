from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    wallet_address = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username
