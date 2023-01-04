from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

# Register your models here.

admin.site.register(User, UserAdmin)


class PersonAdmin(admin.ModelAdmin):
    list_filter = ['is_staff', 'is_active', "is_superuser"]
    exclude = ('password',)
    readonly_fields = ["last_login", "date_joined"]
