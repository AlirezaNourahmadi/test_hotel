from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class meta:
        model = Booking
        fields = ["check_in", "check_out"]
