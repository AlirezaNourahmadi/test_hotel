from django import forms
from .models import Room

class RoomCreateForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = [
            'title', 'room_type', 'bed_type', 'size',
            'capacity', 'view', 'description',
            'price_per_night', 'features'
        ]