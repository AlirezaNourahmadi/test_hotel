from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Guest

class GuestRegistrationForm(UserCreationForm):
    class Meta:
        model = Guest
        fields = ['username', 'email', 'phone_number', 'address', 'password1', 'password2']