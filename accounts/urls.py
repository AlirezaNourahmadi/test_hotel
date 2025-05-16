from django.urls import path
from . import views

urlpatterns = [
    path("register/",views.register_view,name="register"),
    path("login/",views.login_view,name="login"),
    path("logout/",views.logout_view,name="logout"),
    path('dashboard/manager/', views.manager_dashboard_view, name='manager_dashboard'),
    path('dashboard/staff/', views.staff_dashboard_view, name='staff_dashboard'),
    path('dashboard/guest/', views.guest_dashboard_view, name='guest_dashboard'),
]
