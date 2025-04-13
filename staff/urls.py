from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/",views.staff_dashboard_view,name="dashboard")
]
