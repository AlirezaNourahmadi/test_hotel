from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.urls import reverse_lazy
from functools import wraps
from .models import Room
from .forms import RoomCreateForm
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
User = get_user_model()

def manager_required(function=None, redirect_field_name='next', login_url=None):
    """
    Decorator for views that checks that the user is logged in and is a manager,
    redirecting to the log-in page if necessary with the original URL preserved.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.is_manager,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

# ✅ عمومی: لیست اتاق‌ها برای همه کاربران


def public_room_list_view(request):
    rooms = Room.objects.all()
    return render(request, 'rooms/public_room_list.html', {'rooms': rooms})

# ✅ عمومی: جزئیات هر اتاق برای همه


def room_detail_view(request, pk):
    room = get_object_or_404(Room, pk=pk)
    return render(request, 'rooms/room_detail.html', {'room': room})

# ✅ تابع بررسی مدیر بودن


def is_manager(user):
    return user.is_authenticated and user.is_manager

# ✅ فقط برای مدیران: لیست اتاق‌ها برای CRUD


def room_list_view(request):
    rooms = Room.objects.all()
    paginator = Paginator(rooms, 6)     #number of rooms in each page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # فیلتر نوع اتاق
    room_type = request.GET.get('room_type')
    if room_type:
        rooms = rooms.filter(room_type=room_type)

    # فیلتر ظرفیت
    capacity = request.GET.get('capacity')
    if capacity:
        rooms = rooms.filter(capacity=capacity)

    # فیلتر امکانات
    amenities = request.GET.getlist('amenities')
    if amenities:
        for amenity in amenities:
            rooms = rooms.filter(amenities__name=amenity)

    paginator = Paginator(rooms, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'rooms/room_list.html', {
        'page_obj': page_obj,
        'selected_room_type': room_type,
        'selected_capacity': capacity,
        'selected_amenities': amenities,
    })


@manager_required(login_url=reverse_lazy('login'))
def room_create_view(request):
    form = RoomCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('room_list')
    return render(request, 'rooms/room_form.html', {'form': form})


@manager_required(login_url=reverse_lazy('login'))
def room_update_view(request, pk):
    room = get_object_or_404(Room, pk=pk)
    form = RoomCreateForm(request.POST or None, instance=room)
    if form.is_valid():
        form.save()
        return redirect('room_list')
    return render(request, 'rooms/room_form.html', {'form': form})


@manager_required(login_url=reverse_lazy('login'))
def room_delete_view(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('room_list')
    return render(request, 'rooms/room_confirm_delete.html', {'room': room})
