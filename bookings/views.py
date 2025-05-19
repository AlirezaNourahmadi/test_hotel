from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm
from rooms.models import Room
from .models import Booking
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.db import transaction

# Create your views here.


@login_required(login_url=reverse_lazy('login'))
def book_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    booking = form.save(commit=False)
                    booking.guest = request.user
                    booking.room = room
                    booking.save()
                    messages.success(request, "رزرو شما با موفقیت ثبت شد.")
                    return redirect("room_detail", pk=room.id)
            except Exception as e:
                messages.error(request, f"خطا در ثبت رزرو: {str(e)}")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = BookingForm()
    
    return render(request, "bookings/book_room.html", {"form": form, "room": room})


@login_required(login_url=reverse_lazy('login'))
def my_bookings_view(request):
    try:
        bookings = Booking.objects.filter(guest=request.user).order_by('-check_in')
        return render(request, 'bookings/my_bookings.html', {'bookings': bookings})
    except Exception as e:
        messages.error(request, f"خطا در بارگیری رزروها: {str(e)}")
        return redirect('home')

@login_required(login_url=reverse_lazy('login'))
def booking_detail_view(request, booking_id):
    try:
        booking = get_object_or_404(Booking, id=booking_id, guest=request.user)
        return render(request, 'bookings/booking_detail.html', {'booking': booking})
    except Exception as e:
        messages.error(request, f"خطا در بارگیری اطلاعات رزرو: {str(e)}")
        return redirect('my_bookings')

@login_required(login_url=reverse_lazy('login'))
def cancel_booking_view(request, booking_id):
    try:
        booking = get_object_or_404(Booking, id=booking_id, guest=request.user)
        
        if request.method == 'POST':
            try:
                with transaction.atomic():
                    booking.delete()
                    messages.success(request, 'رزرو با موفقیت لغو شد.')
                    return redirect('my_bookings')
            except Exception as e:
                messages.error(request, f"خطا در لغو رزرو: {str(e)}")
        
        return render(request, 'bookings/cancel_booking_confirm.html', {'booking': booking})
    except Exception as e:
        messages.error(request, f"خطا در یافتن رزرو: {str(e)}")
        return redirect('my_bookings')
