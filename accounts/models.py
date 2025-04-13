from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Guest(AbstractUser):
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.username} ({self.email})"
