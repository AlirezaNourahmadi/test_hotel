from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Guest
from django.utils.translation import gettext_lazy as _


@admin.register(Guest)
class GuestAdmin(UserAdmin):
    model = Guest

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("اطلاعات شخصی"), {"fields": ("first_name", "last_name", "email", "phone_number", "address")}),
        (_("دسترسی‌ها"), {"fields": ("is_active", "is_staff", "is_superuser", "is_manager", "groups", "user_permissions")}),
        (_("تاریخ‌ها"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "password1", "password2", "is_staff", "is_manager", "is_active"),
        }),
    )

    list_display = ("username", "email", "is_staff", "is_manager", "is_active")
    search_fields = ("username", "email")
    ordering = ("username",)
