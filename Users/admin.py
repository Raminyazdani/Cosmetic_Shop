from django.contrib import admin
from .models import User
from Core.admin import BaseAdmin, BaseAdminSlugUser


# Register your models here.


@admin.register(User)
class UserAdmin(BaseAdminSlugUser):
    list_display = ['id', 'phone_number', 'is_costumer', 'is_market', 'is_staff', 'is_active', 'is_admin',
                    'is_superuser', 'is_verified', 'slug', 'is_delete', 'created_at', 'modified_at']
    list_filter = ['is_costumer', 'is_market', 'is_staff', 'is_active', 'is_admin',
                   'is_superuser', 'is_verified', 'is_delete', 'created_at']
    list_editable = ['is_costumer', 'is_market', 'is_staff', 'is_active', 'is_admin',
                     'is_superuser', 'is_verified', 'is_delete']

    search_fields = ['phone_number']
    ordering = ['phone_number']
    filter_horizontal = []
    fieldsets = ((
                     "Profiling", {
                         'fields': (('phone_number', 'slug'), ('is_costumer', 'is_market')),

                         'classes': ('extrapretty')
                     }),
                 ("Conditions", {
                     'fields': (('is_staff', 'is_active', 'is_admin',
                                 'is_superuser', 'is_verified',
                                 'is_delete'),),
                     'classes': ('extrapretty')
                 }),
                 ("Time", {
                     'fields': (('created_at', 'modified_at'),),
                     'classes': ('extrapretty')
                 })
    )
    add_fieldsets = []
    readonly_fields = ['created_at', 'modified_at']
    list_per_page = 25
    list_max_show_all = 100
    prepopulated_fields = {"slug": ("phone_number",)}
