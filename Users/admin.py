from django.contrib import admin

from Core.ProjectMixins.Users import AdminProperty
from Core.admin import BaseAdminSlugUser
from .models import User

# Register your models here.


@admin.register(User)
class UserAdmin(BaseAdminSlugUser):
    model = User
    list_display = AdminProperty.User.list_display
    list_filter = AdminProperty.User.list_filter
    list_editable = AdminProperty.User.list_editable
    search_fields = AdminProperty.User.search_fields
    ordering = AdminProperty.User.ordering
    filter_horizontal = AdminProperty.User.filter_horizontal
    fieldsets = AdminProperty.User.fieldsets
    add_fieldsets = AdminProperty.User.add_fieldsets
    readonly_fields = AdminProperty.User.readonly_fields
    list_per_page = AdminProperty.User.list_per_page
    list_max_show_all = AdminProperty.User.list_max_show_all
    prepopulated_fields = AdminProperty.User.prepopulated_fields
