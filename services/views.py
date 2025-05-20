from django.shortcuts import render, get_object_or_404, redirect
from .models import Service
from .forms import ServiceForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse_lazy
from django.contrib import messages
from django.db import transaction


# Create your views here.
def manager_required(function=None, redirect_field_name='next', login_url=None):
    """
    Decorator for views that checks that the user is logged in and is a manager,
    redirecting to the log-in page if necessary with the original URL preserved.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.is_manager,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def is_manager(user):
    return user.is_authenticated and user.is_manager

@manager_required(login_url=reverse_lazy('login'))
def service_list_view(request):
    try:
        services = Service.objects.select_related("room", "assigned_to").all()
        return render(request, "services/service_list.html", {"services": services})
    except Exception as e:
        messages.error(request, f"خطا در بارگیری خدمات: {str(e)}")
        return redirect('home')

@manager_required(login_url=reverse_lazy('login'))
def service_create_view(request):
    form = ServiceForm(request.POST or None)
    if form.is_valid():
        try:
            with transaction.atomic():
                form.save()
                messages.success(request, "خدمت با موفقیت ایجاد شد.")
                return redirect('service_list')
        except Exception as e:
            messages.error(request, f"خطا در ایجاد خدمت: {str(e)}")
    else:
        if request.method == 'POST':
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    return render(request, 'services/service_form.html', {'form': form})

@manager_required(login_url=reverse_lazy('login'))
def service_update_view(request, pk):
    try:
        service = get_object_or_404(Service, pk=pk)
        form = ServiceForm(request.POST or None, instance=service)
        if form.is_valid():
            try:
                with transaction.atomic():
                    form.save()
                    messages.success(request, "خدمت با موفقیت به‌روزرسانی شد.")
                    return redirect('service_list')
            except Exception as e:
                messages.error(request, f"خطا در به‌روزرسانی خدمت: {str(e)}")
        else:
            if request.method == 'POST':
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f"{field}: {error}")
        return render(request, 'services/service_form.html', {'form': form})
    except Exception as e:
        messages.error(request, f"خطا در یافتن خدمت: {str(e)}")
        return redirect('service_list')

@manager_required(login_url=reverse_lazy('login'))
def service_delete_view(request, pk):
    try:
        service = get_object_or_404(Service, pk=pk)
        if request.method == 'POST':
            try:
                with transaction.atomic():
                    service.delete()
                    messages.success(request, "خدمت با موفقیت حذف شد.")
                    return redirect('service_list')
            except Exception as e:
                messages.error(request, f"خطا در حذف خدمت: {str(e)}")
        return render(request, 'services/service_confirm_delete.html', {'service': service})
    except Exception as e:
        messages.error(request, f"خطا در یافتن خدمت: {str(e)}")
        return redirect('service_list')
    
@manager_required(login_url=reverse_lazy('create'))
def service_update_view(request):   
    pass

    
    
    
