from django.db import models
from bookings.models import Booking

class Payment(models.Model):
    PAYMENT_METHODS = [
        ('CRD', 'Credit Card'),
        ('CASH', 'Cash'),
        ('PAY', 'PayPal'),
    ]

    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_method = models.CharField(max_length=4, choices=PAYMENT_METHODS)
    paid_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Booking ID {self.booking.id}"