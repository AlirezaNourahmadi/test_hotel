from django.urls import path
from . import views

urlpatterns = [
    path('book/<int:room_id>/', views.book_room, name='book_room'),
    path("my_bookings",views.my_bookings_view,name="my_bookings"),
    path('my_bookings/<int:booking_id>/', views.booking_detail_view, name='booking_detail'),
    path('my_bookings/<int:booking_id>/cancel/', views.cancel_booking_view, name='cancel_booking'),
]