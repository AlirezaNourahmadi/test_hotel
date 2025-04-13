def role_context(request):
    is_manager = False
    if request.user.is_authenticated and request.user.is_staff:
        is_manager = request.user.groups.filter(name='manager').exists()

    return {
        'is_manager': is_manager
    }