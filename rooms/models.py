from django.db import models

# Amenity model
class Amenity(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Room(models.Model):
    ROOM_TYPES = [
        ('lux_double', 'اتاق دبل لوکس'),
        ('suite_city', 'سوییت با منظره شهر'),
        ('single_modern', 'اتاق سینگل مدرن'),
        ('royal_king', 'رویال کینگ'),
        ('junior_suite', 'جونیور سوییت'),
        ('family_suite', 'سوییت خانوادگی'),
    ]
    
    title = models.CharField(max_length=100, null=True, blank=True)
    room_type = models.CharField(max_length=30, choices=ROOM_TYPES)
    bed_type = models.CharField(max_length=50, default="اتاق سینگل مدرن")
    size = models.IntegerField(help_text="متراژ بر حسب متر مربع", null=True, blank=True)
    capacity = models.IntegerField(null=True, blank=True, help_text="حداکثر تعداد نفرات")
    view = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price_per_night = models.IntegerField(null=True, blank=True, help_text="قیمت هر شب به تومان")
    features = models.TextField(null=True, blank=True)  # JSON یا String ساده
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    amenities = models.ManyToManyField(Amenity, blank=True)

    def __str__(self):
        return self.title
    
    # عکس و گالری می‌تونه جدا باشه




# Model for storing multiple images per Room
class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='room_images/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.room.title}"