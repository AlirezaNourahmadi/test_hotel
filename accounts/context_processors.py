def user_roles(request):
    user = request.user
    roles = {
        'is_manager': False,
        'is_staff': False,
        'is_guest': False
    }
    
    if user.is_authenticated:
        # Check session first, then fall back to database
        roles['is_manager'] = request.session.get('is_manager', False) or user.groups.filter(name='manager').exists()
        roles['is_staff'] = request.session.get('is_staff', False) or user.is_staff
        roles['is_guest'] = not (roles['is_manager'] or roles['is_staff'])
        
        # Update session with current values
        request.session['is_manager'] = roles['is_manager']
        request.session['is_staff'] = roles['is_staff']
    
    return roles
