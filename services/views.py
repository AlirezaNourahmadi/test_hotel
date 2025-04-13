from django.shortcuts import render, get_object_or_404 , redirect
from .models import Service
from .forms import ServiceForm
from django.contrib.auth.decorators import login_required , user_passes_test


# Create your views here.
def is_manager(user):
    return user.is_authenticated and user.group.filter(name = "manager").exists()

@user_passes_test
def service_list_view(request):
    services = Service.objects.select_related("room", "assigned_to").all()
    return render(request,"services/service_list.html",{"services":services})

@user_passes_test(is_manager)
def service_create_view(request):
    form = ServiceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('service_list')
    return render(request, 'services/service_form.html', {'form': form})

@user_passes_test(is_manager)
def service_update_view(request, pk):
    service = get_object_or_404(Service, pk=pk)
    form = ServiceForm(request.POST or None, instance=service)
    if form.is_valid():
        form.save()
        return redirect('service_list')
    return render(request, 'services/service_form.html', {'form': form})

@user_passes_test(is_manager)
def service_delete_view(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        return redirect('service_list')
    return render(request, 'services/service_confirm_delete.html', {'service': service})