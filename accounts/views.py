from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import GuestRegistrationForm
from django.contrib.auth.decorators import login_required
def register_view(request):
    if request.method == 'POST':
        form = GuestRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = GuestRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            
            login(request, user)
            
            # Set session variables for roles
            request.session['is_staff'] = user.is_staff
            request.session['is_manager'] = user.is_manager
            
            # Redirect based on role
            if request.session['is_manager']:
                return redirect('manager_dashboard')
            elif request.session['is_staff']:
                return redirect('staff_dashboard')
            else:
                return redirect('guest_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def manager_dashboard_view(request):
    return render(request, 'accounts/managerdashboard.html')

@login_required
def staff_dashboard_view(request):
    return render(request, 'staff/staff_dashboard.html')

@login_required
def guest_dashboard_view(request):
    return render(request, 'accounts/guestdashboard.html')