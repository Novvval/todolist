from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User

# Register your models here.

admin.site.register(User, BaseUserAdmin)


class UserAdmin(BaseUserAdmin):
    list_display = ("username", "email", "first_name", "last_name")
    search_fields = ("username", "email", "first_name", "last_name")
    readonly_fields = ("last_login", "date_joined")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info",
            {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Important dates",
         {"fields": ("date_joined", "last_login")}
         )
    )
