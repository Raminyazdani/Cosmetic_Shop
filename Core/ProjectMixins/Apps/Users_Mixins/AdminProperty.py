from Core.admin import BaseAdminInlineRender, BaseAdminSlug, CustomInlineAdmin
from Core.ProjectMixins.Base.BaseInline import InlineMethods
from Markets.models import *
from Customers.models import *
from Shops.models import *
from Products.models import *
from Users.models import *

class User(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True
    add_fieldsets = []
    fieldsets = (('Profiling', {'classes': ('extrapretty',), 'fields': (('password', 'id', 'phone_number'), ('slug', 'groups', 'user_permissions'))}), ('Conditions', {'classes': 'extrapretty', 'fields': (('is_customer', 'is_market', 'is_staff', 'is_active', 'is_admin', 'is_superuser', 'is_verified', 'is_delete'),)}), ('Time', {'classes': ('extrapretty',), 'fields': (('last_login', 'deleted_on', 'created_at', 'modified_at'),)}), ('Relations', {'classes': ('extrapretty', 'collapse'), 'fields': ('market', 'customer', 'logentry')}))
    filter_horizontal = []
    list_display = ['__str__', 'id', 'phone_number', 'slug', 'market', 'customer', 'is_customer', 'is_market', 'is_staff', 'is_active', 'is_admin', 'is_superuser', 'is_verified', 'is_delete', 'created_at']
    list_display_links = ['__str__', 'market', 'customer']
    list_editable = ['phone_number', 'is_customer', 'is_market', 'is_staff', 'is_active', 'is_admin', 'is_superuser', 'is_verified', 'is_delete']
    list_filter = ['is_customer', 'is_market', 'is_staff', 'is_active', 'is_admin', 'is_superuser', 'is_verified', 'is_delete', 'market', 'customer', 'logentry']
    list_max_show_all = 100
    list_per_page = 25
    list_select_related = True
    ordering = ['created_at']
    prepopulated_fields = {'slug': ('id',)}
    readonly_fields = ['last_login', 'slug', 'last_login', 'deleted_on', 'created_at', 'modified_at', 'logentry', 'id', 'slug', 'market', 'customer']
    search_help_text = ''

    def logentry(self, obj):
        if  obj.logentry.all().count() > 0:
            return obj.logentry.all()
        return None
            
