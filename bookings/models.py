from django.db import models
from django.conf import settings
from rooms.models import Room
# Create your models here.

class Booking(models.Model):
    guest = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.guest.username} - Room {self.room.number} ({self.check_in} + {self.check_out})"
    