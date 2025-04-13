from django.db import models
from accounts.models import Guest
from staff.models import Staff
from django.conf import settings
from rooms.models import Room
# Create your models here.


class Service(models.Model):
    SERVICE_CHOICES = [
        ('cleaning', 'نظافت'),
        ('laundry', 'خشکشویی'),
        ('maintenance', 'تعمیرات'),
    ]

    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    done = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    requested_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.get_service_type_display()} برای اتاق {self.room.number}"
