from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import Room
from .forms import RoomCreateForm
from django.contrib.auth import get_user_model

User = get_user_model()

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
    return user.is_authenticated and user.is_staff and user.groups.filter(name="manager").exists()

# ✅ فقط برای مدیران: لیست اتاق‌ها برای CRUD


@user_passes_test(is_manager)
def room_list_view(request):
    rooms = Room.objects.all()
    return render(request, 'rooms/room_list.html', {'rooms': rooms})


@user_passes_test(is_manager)
def room_create_view(request):
    form = RoomCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('room_list')
    return render(request, 'rooms/room_form.html', {'form': form})


@user_passes_test(is_manager)
def room_update_view(request, pk):
    room = get_object_or_404(Room, pk=pk)
    form = RoomCreateForm(request.POST or None, instance=room)
    if form.is_valid():
        form.save()
        return redirect('room_list')
    return render(request, 'rooms/room_form.html', {'form': form})


@user_passes_test(is_manager)
def room_delete_view(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('room_list')
    return render(request, 'rooms/room_confirm_delete.html', {'room': room})
