from django.contrib import admin
from .models import User
from Core.admin import BaseAdmin

# Register your models here.


@admin.register(User)
class UserAdmin(BaseAdmin):
    list_display = ['id', 'phone_number', 'is_staff', 'is_superuser', 'is_admin', 'is_verified', 'is_delete',
                    'is_market', 'is_costumer', 'is_active', 'created_at']
    list_filter = ['is_staff', 'is_superuser', 'is_active', 'is_costumer', 'is_market', "is_delete", "is_verified",
                   "is_active"]
    search_fields = ['phone_number']
    ordering = ['phone_number']
    filter_horizontal = []
    fieldsets = []
    add_fieldsets = []
    readonly_fields = ['created_at', 'modified_at']
    list_per_page = 25
    list_max_show_all = 100
