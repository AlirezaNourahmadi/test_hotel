from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/",views.staff_dashboard_view,name="dashboard"),
    path("services/update/<int:pk>/",views.staff_service_update_view,name="staff_service_update"),
    
]
