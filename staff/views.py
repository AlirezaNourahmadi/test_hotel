from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from bookings.models import Booking
from services.models import Service
from datetime import date


def staff_check(user):
    return user.is_authenticated and user.is_staff


@user_passes_test(staff_check)
def staff_dashboard_view(request):
    today = date.today()

    # رزروهای امروز
    bookings = Booking.objects.filter(
        check_in__lte=today, check_out__gte=today
    ).select_related('room', 'guest')

    # سرویس‌های اختصاص‌یافته به کاربر لاگین‌شده
    assigned_services = Service.objects.filter(
        assigned_to=request.user
    ).select_related('room').order_by('-requested_at')

    return render(request, 'staff/staff_dashboard.html', {
        'bookings': bookings,
        'assigned_services': assigned_services,
        'today': today
    })
