from django import forms
from .models import Staff
from django.contrib.auth.models import User



class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'role', 'hire_date']
        