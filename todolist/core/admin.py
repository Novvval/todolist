from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

# Register your models here.

admin.site.register(User, UserAdmin)


class PersonAdmin(admin.ModelAdmin):
    list_filter = ['is_staff', 'is_active', "is_superuser"]
    exclude = ('Password',)
    readonly_fields = ["Last login", "Date joined"]
