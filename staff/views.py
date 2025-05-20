from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from bookings.models import Booking
from services.models import Service
from datetime import date
from services.forms import StaffServiceUpdateForm


def staff_required(function=None, redirect_field_name='next', login_url=None):
    """
    Decorator for views that checks that the user is logged in and is staff,
    redirecting to the log-in page if necessary with the original URL preserved.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.is_staff,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def staff_check(user):
    return user.is_authenticated and user.is_staff


@staff_required(login_url=reverse_lazy('login'))
def staff_dashboard_view(request):
    try:
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
    except Exception as e:
        messages.error(request, f"خطا در بارگیری اطلاعات داشبورد: {str(e)}")
        return redirect('home')
    
    
@staff_required
def staff_service_update_view(request, pk):
    service = get_object_or_404(Service, pk=pk, assigned_to=request.user)

    if request.method == 'POST':
        form = StaffServiceUpdateForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('staff_dashboard')
    else:
        form = StaffServiceUpdateForm(instance=service)
    
    return render(request, 'staff/staff_service_update.html', {'form': form})
