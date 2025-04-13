from django.db import models

# Create your models here.


class Staff(models.Model):
    ROLE_CHOICES = [
        ("RCPT", "Receptionist"),
        ("CLNR", "Cleaner"),
        ("MGMT", "Manager"),
        ("SVP", "Service Provider"),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=4, choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    hire_date = models.DateField()
    
    
    def __str__(self):
        return f"{self.first_name}  {self.last_name} - {self.get_role_display()}"
