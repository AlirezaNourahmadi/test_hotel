from django.db import models


# Create your models here.
class Room(models.Model):
    ROOM_TYPES = [
        ('SGL', 'SINGLE'),
        ('DBL', 'DOUBLE'),
        ('DLX', 'DELUXE'),
    ]
    number = models.IntegerField(unique=True)
    room_type = models.CharField(max_length=3,choices=ROOM_TYPES)
    is_available = models.BooleanField(default=True)
    price_per_night = models.DecimalField(max_digits=7, decimal_places=2)
    capacity = models.PositiveIntegerField(default=1)
    description = models.TextField(blank=True , null=True)
    
    def __str__(self):
        return f"Room {self.number} ({self.get_room_type_display()})"
    
