from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import GuestRegistrationForm, PersianAuthenticationForm
from django.contrib.auth.decorators import login_required
from rooms.models import Room
from rooms.forms import RoomCreateForm
from services.models import Service
from services.forms import ServiceForm
from bookings.models import Booking
from staff.models import Staff
from staff.forms import StaffForm


def register_view(request):
    if request.method == 'POST':
        form = GuestRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = GuestRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = PersianAuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()

            login(request, user)

            # Set session variables for roles
            request.session['is_staff'] = user.is_staff
            request.session['is_manager'] = user.is_manager

            # Redirect based on role
            if request.session['is_manager']:
                return redirect('manager_dashboard')
            elif request.session['is_staff']:
                return redirect('staff_dashboard')
            else:
                return redirect('guest_dashboard')
    else:
        form = PersianAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def manager_dashboard_view(request):
    return render(request, 'accounts/managerdashboard.html')


@login_required
def staff_dashboard_view(request):
    return render(request, 'accounts/staffdashboard.html')


@login_required
def guest_dashboard_view(request):
    return render(request, 'accounts/guestdashboard.html')


def public_rooms_view(request):
    rooms = Room.objects.all()
    return render(request, 'accounts/public_room_list.html', {'rooms': rooms})


@login_required
def manager_room_list_view(request):
    rooms = Room.objects.all()
    return render(request, 'accounts/manager_room_list.html', {'rooms': rooms})

@login_required
def manager_room_detail_view(request, pk):
    room = Room.objects.get(id=pk)
    return render(request, 'accounts/manager_room_detail.html', {'room': room})

@login_required
def manager_room_update_view(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        form = RoomCreateForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('manager_room_list')
    else:
        form = RoomCreateForm(instance=room)
    return render(request, 'accounts/manager_room_update.html', {'form': form, 'room': room})


@login_required
def manager_room_delete_view(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('manager_room_list')
    return render(request, 'accounts/manager_room_delete.html', {'room': room})


@login_required
def manager_room_add_view(request):
    if request.method == 'POST':
        form = RoomCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manager_room_list')
    else:
        form = RoomCreateForm()
    return render(request, 'accounts/manager_room_add.html', {'form': form})


@login_required
def manager_service_list_view(request):
    services = Service.objects.all()
    rooms = Room.objects.all()
    return render(request, 'accounts/manager_service_list.html', {'services': services, 'rooms': rooms})


@login_required
def manager_service_detail_view(request, pk):
    service = Service.objects.get(id=pk)
    return render(request, 'accounts/manager_service_detail.html', {'service': service})


@login_required
def manager_service_update_view(request, pk):
    service = Service.objects.get(id=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('manager_service_list')
        else:
            print(form.errors)
            # form = ServiceForm(instance=service)  # Remove this line to avoid overwriting form with unbound form
            return render(request, 'accounts/manager_service_update.html', {'form': form, 'service': service})
    else:
        form = ServiceForm(instance=service)
    return render(request, 'accounts/manager_service_update.html', {'form': form, 'service': service})


@login_required
def manager_service_delete_view(request, pk):
    service = Service.objects.get(id=pk)
    if request.method == 'POST':
        service.delete()
        return redirect('manager_service_list')
    return render(request, 'accounts/manager_service_delete.html', {'service': service})


@login_required
def manager_service_add_view(request):
    form = ServiceForm()
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manager_service_list')
        else:
            print(form.errors)
            form = ServiceForm()
        return render(request, 'accounts/manager_service_add.html', {'form': form})
    return render(request, 'accounts/manager_service_add.html', {'form': form})


@login_required
def manager_booking_list_view(request):
    bookings = Booking.objects.all()
    return render(request, 'accounts/manager_booking_list.html', {'bookings': bookings})


@login_required
def manager_staff_management_view(request):
    staff_members = Staff.objects.all()
    return render(request, 'accounts/manager_staff_management.html', {'staff_members': staff_members})


@login_required
def manager_staff_add_view(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manager_staff_management')
        return render(request, 'accounts/manager_staff_add.html', {'form': form})
    return render(request, 'accounts/manager_staff_add.html', {'form': form})


@login_required
def manager_staff_update_view(request, pk):
    staff_member = Staff.objects.get(id=pk)
    if request.method == 'POST':
        form = StaffForm(request.POST, instance=staff_member)
        if form.is_valid():
            form.save()
            return redirect('manager_staff_management')
        else:
            print(form.errors)
            form = StaffForm(instance=staff_member)
            return render(request, 'accounts/manager_staff_update.html', {'form': form, 'staff_member': staff_member})
    else:
        form = StaffForm(instance=staff_member)
    return render(request, 'accounts/manager_staff_update.html', {'form': form, 'staff_member': staff_member})


@login_required
def manager_staff_delete_view(request, pk):
    staff_member = Staff.objects.get(id=pk)
    if request.method == 'POST':
        staff_member.delete()
        return redirect('manager_staff_management')
    return render(request, 'accounts/manager_staff_delete.html', {'staff_member': staff_member})


# staff views region
@login_required
def staff_room_list_view(request):
    rooms = Room.objects.all()
    return render(request, 'accounts/staff_room_list.html', {'rooms': rooms})


@login_required
def staff_room_update_view(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        form = RoomCreateForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('staff_room_list')
        else:
            print(form.errors)
            form = RoomCreateForm(instance=room)
        return render(request, 'accounts/staff_room_update.html', {'form': form, 'room': room})
    return render(request, 'accounts/staff_room_update.html', {'form': form, 'room': room})


@login_required
def staff_service_list_view(request):
    services = Service.objects.all()
    return render(request, 'accounts/staff_service_list.html', {'services': services})


@login_required
def staff_service_update_view(request, pk):
    service = Service.objects.get(id=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('staff_service_list')
        else:
            print(form.errors)
            form = ServiceForm(instance=service)
        return render(request, 'accounts/staff_service_update.html', {'form': form, 'service': service})
    return render(request, 'accounts/staff_service_update.html', {'form': form, 'service': service})


@login_required
def staff_booking_list_view(request):
    bookings = Booking.objects.all()
    return render(request, 'accounts/staff_booking_list.html', {'bookings': bookings})
