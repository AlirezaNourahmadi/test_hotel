from django import forms
from .models import Room

class RoomCreateForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['number', 'room_type', 'price_per_night', 'description', 'is_available']