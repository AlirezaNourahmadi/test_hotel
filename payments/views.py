from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from bookings.models import Booking
from .forms import PaymentForm
from .models import Payment

@login_required
def payment_view(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, guest=request.user)

    if hasattr(booking, 'payment'):
        return redirect('booking_detail', booking_id=booking.id)  # قبلاً پرداخت شده

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.booking = booking
            payment.amount = booking.room.price_per_night
            payment.save()
            return redirect('booking_detail', booking_id=booking.id)
    else:
        form = PaymentForm()

    return render(request, 'payments/payment_form.html', {'form': form, 'booking': booking})