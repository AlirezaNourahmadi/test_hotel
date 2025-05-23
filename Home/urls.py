from django.urls import path
from .views import home_view, about_us_view


urlpatterns = [
    path('',home_view,name='home'),
    path('about_us/', about_us_view, name='about_us'),
]
