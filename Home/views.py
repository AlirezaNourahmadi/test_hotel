from django.shortcuts import render

# Create your views here.

def home_view(request):
    is_manager = False
    if request.user.is_authenticated and request.user.is_staff:
        is_manager = request.user.groups.filter(name='manager').exists()
    return render(request, 'Home/home.html', {'is_manager': is_manager})

def about_us_view(request):
    return render(request, 'about_us.html')
