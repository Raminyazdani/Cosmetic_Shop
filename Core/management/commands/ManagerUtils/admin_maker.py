from Core.management.commands.ManagerUtils.CheckLines import check_lines
from Core.management.commands.ManagerUtils.RemoveEmptyLines import remove_empty_lines

def admin_maker(File, Models, App_name, Scope_parent, Option):

    header = f"""
from django import forms
from django.contrib import admin
from django.template.loader import get_template

from Core.ProjectMixins.Apps.{App_name.capitalize()}_Mixins import AdminProperty
import Core.ProjectMixins.Base.AbsoluteUrl
from Core.admin import CustomInlineAdmin, CustomInlineAdminOneToMany
from .models import *

"""
    result = []
    remove_empty_lines(File)

    if Option == "hard":
        mode_file = "w"
    else:
        mode_file = "a"
        Models = check_lines(File, Models, App_name, Scope_parent, header, prefix= "Admin")

    with open(File, mode_file) as f:
        if mode_file== "w" :
            f.write(header)
        for Model in Models:
            body = f"""


@admin.register({Model.capitalize()})
class {Model.capitalize()}Admin(AdminProperty.{Model.capitalize()}):
    model = {Model.capitalize()}
    search_fields = {Model.capitalize()}.SEARCH_FIELDS
    list_display = AdminProperty.{Model.capitalize()}.list_display
    list_filter = AdminProperty.{Model.capitalize()}.list_filter
    list_editable = AdminProperty.{Model.capitalize()}.list_editable
    ordering = AdminProperty.{Model.capitalize()}.ordering
    filter_horizontal = AdminProperty.{Model.capitalize()}.filter_horizontal
    fieldsets = AdminProperty.{Model.capitalize()}.fieldsets
    add_fieldsets = AdminProperty.{Model.capitalize()}.add_fieldsets
    prepopulated_fields = AdminProperty.{Model.capitalize()}.prepopulated_fields
    readonly_fields = AdminProperty.{Model.capitalize()}.readonly_fields
    list_per_page = AdminProperty.{Model.capitalize()}.list_per_page
    list_max_show_all = AdminProperty.{Model.capitalize()}.list_max_show_all
    search_help_text = AdminProperty.{Model.capitalize()}.search_help_text

    inlines = (Inlines.XInlineAdmin)
    x_inline = inlines[0].tag_inline


"""
            f.write(body)
            if Model!="":
                result.append(f"{App_name:10}.{Model.capitalize():<25}\t {'Admin':25} \t\tadded in admin.py")
    return result
