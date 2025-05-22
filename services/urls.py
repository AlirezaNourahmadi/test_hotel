from django.urls import path
from . import views

urlpatterns = [
    path('',views.service_list_view,name='service_list'),
    path('create',views.service_create_view,name='service_create'),
    path('<int:pk>/update',views.service_update_view,name='service_update'),
    path('<int:pk>/delete',views.service_delete_view,name='service_delete'),
    path('about_services/', views.guest_services_details, name='guest_services_details'),
]
