from django.db import models
from accounts.models import Guest
from rooms.models import Room
# Create your models here.

class Review(models.Model):
    guest = models.ForeignKey(Guest , on_delete=models.CASCADE)
    room = models.ForeignKey(Room , on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True , null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.guest.username} - Room {self.room.number} - {self.rating}/5"
    