from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm
from rooms.models import Room
from .models import Booking
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


@login_required
def book_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.guest = request.user
            booking.room = room
            booking.save()
            return redirect("room_detail", pk=room.id)
    else:
        form = BookingForm()
    return render(request, "bookings/book_room.html", {form: "form", room: "room"})


@login_required
def my_bookings_view(request):
    bookings = Booking.objects.filter(guest=request.user).order_by('-check_in')
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})

@login_required
def booking_detail_view(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, guest=request.user)
    return render(request, 'bookings/booking_detail.html', {'booking': booking})

@login_required
def cancel_booking_view(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, guest=request.user)

    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'رزرو با موفقیت لغو شد.')
        return redirect('my_bookings')

    return render(request, 'bookings/cancel_booking_confirm.html', {'booking': booking})
