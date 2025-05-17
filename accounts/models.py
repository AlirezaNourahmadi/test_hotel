from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Guest(AbstractUser):
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    is_manager = models.BooleanField(default=False, verbose_name="manager")

    def save(self, *args, **kwargs):
        # Ensure is_staff is True if is_manager is True
        if self.is_manager:
            self.is_staff = True
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.username} , ({self.email})"
