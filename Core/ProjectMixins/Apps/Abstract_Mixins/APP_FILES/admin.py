from django import forms
from django.contrib import admin
from django.template.loader import get_template

from Core.ProjectMixins.Apps.APP_NAME_Mixins import AdminProperty
import Core.ProjectMixins.Base.AbsoluteUrl
from Core.admin import CustomInlineAdmin, CustomInlineAdminOneToMany
from .models import *

# APP_NAME
# MODEL_NAME

# Register your models here.
@admin.register(MODEL_NAME)
class MODEL_NAMEAdmin(AdminProperty.MODEL_NAME):
    model = MODEL_NAME
    search_fields = MODEL_NAME.SEARCH_FIELDS
    list_display = AdminProperty.MODEL_NAME.list_display
    list_filter = AdminProperty.MODEL_NAME.list_filter
    list_editable = AdminProperty.MODEL_NAME.list_editable
    ordering = AdminProperty.MODEL_NAME.ordering
    filter_horizontal = AdminProperty.MODEL_NAME.filter_horizontal
    fieldsets = AdminProperty.MODEL_NAME.fieldsets
    add_fieldsets = AdminProperty.MODEL_NAME.add_fieldsets
    prepopulated_fields = AdminProperty.MODEL_NAME.prepopulated_fields
    readonly_fields = AdminProperty.MODEL_NAME.readonly_fields
    list_per_page = AdminProperty.MODEL_NAME.list_per_page
    list_max_show_all = AdminProperty.MODEL_NAME.list_max_show_all
    search_help_text = AdminProperty.MODEL_NAME.search_help_text

    inlines = (Inlines.XInlineAdmin)
    x_inline = inlines[0].tag_inline

#### custom query set  # def get_queryset(self, request):  #     # use our manager, rather than the default one  #  #     qs = super().get_queryset(request)  #     qs = qs.annotate(comment_count=Count('comment'))  #     qs = qs.annotate(tag_count=Count('tag'))  #     qs = qs.annotate(brand_count=Count('brand'))  #     qs = qs.annotate(category_count=Count('category'))  #     return qs

