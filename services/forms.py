from django import forms
from .models import Service

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['room', 'service_type', 'description', 'assigned_to', 'done']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'done': forms.CheckboxInput(),
        }