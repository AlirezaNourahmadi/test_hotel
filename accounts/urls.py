from django.urls import path
from . import views

urlpatterns = [
    path("register/",views.register_view,name="register"),
    path("login/",views.login_view,name="login"),
    path("logout/",views.logout_view,name="logout"),
    path('dashboard/manager/', views.manager_dashboard_view, name='manager_dashboard'),
    path('dashboard/staff/', views.staff_dashboard_view, name='staff_dashboard'),
    path('dashboard/guest/', views.guest_dashboard_view, name='guest_dashboard'),
    path('manager/rooms/',views.manager_room_list_view,name='manager_room_list'),
    path('manager/rooms/create/',views.manager_room_add_view,name='manager_room_add'),
    path('manager/rooms/<int:pk>/edit/',views.manager_room_update_view,name='manager_room_update'),
    path('manager/rooms/<int:pk>/delete/',views.manager_room_delete_view,name='manager_room_delete'),
    path('manager/bookings/',views.manager_booking_list_view,name='manager_booking_list'),
    path('manager/staff_management/',views.manager_staff_management_view,name='manager_staff_management'),
    path('manager/staff_management/create/',views.manager_staff_add_view,name='manager_staff_add'),
    path('manager/staff_management/<int:pk>/edit/',views.manager_staff_update_view,name='manager_staff_update'),
    path('manager/staff_management/<int:pk>/delete/',views.manager_staff_delete_view,name='manager_staff_delete'),
    path('manager/services/',views.manager_service_list_view,name='manager_service_list'),
    path('manager/services/create/',views.manager_service_add_view,name='manager_service_add'),
    path('manager/services/<int:pk>/edit/',views.manager_service_update_view,name='manager_service_update'),
    path('manager/services/<int:pk>/delete/',views.manager_service_delete_view,name='manager_service_delete'),
    path('staff/rooms/',views.staff_room_list_view,name='staff_room_list'),
    path('staff/bookings/',views.staff_booking_list_view,name='staff_booking_list'),
    path('staff/services/',views.staff_service_list_view,name='staff_service_list'),
    path('staff/services/update/<int:pk>/',views.staff_service_update_view,name='staff_service_update'),
    path('staff/rooms/update/<int:pk>/',views.staff_room_update_view,name='staff_room_update'),
]
