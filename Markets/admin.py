
from django import forms
from django.contrib import admin
from django.template.loader import get_template

from Core.ProjectMixins.Apps.Markets_Mixins import AdminProperty
import Core.ProjectMixins.Base.AbsoluteUrl
from Core.admin import CustomInlineAdmin, CustomInlineAdminOneToMany
from .models import *

# Register your models here.



@admin.register(Market)
class MarketAdmin(AdminProperty.Market):
    model = Market
    search_fields = Market.SEARCH_FIELDS
    list_display = AdminProperty.Market.list_display
    list_filter = AdminProperty.Market.list_filter
    list_editable = AdminProperty.Market.list_editable
    ordering = AdminProperty.Market.ordering
    filter_horizontal = AdminProperty.Market.filter_horizontal
    fieldsets = AdminProperty.Market.fieldsets
    add_fieldsets = AdminProperty.Market.add_fieldsets
    prepopulated_fields = AdminProperty.Market.prepopulated_fields
    readonly_fields = AdminProperty.Market.readonly_fields
    list_per_page = AdminProperty.Market.list_per_page
    list_max_show_all = AdminProperty.Market.list_max_show_all
    search_help_text = AdminProperty.Market.search_help_text

    # inlines = (Inlines.XInlineAdmin)
    # x_inline = inlines[0].tag_inline





@admin.register(Inventory)
class InventoryAdmin(AdminProperty.Inventory):
    model = Inventory
    search_fields = Inventory.SEARCH_FIELDS
    list_display = AdminProperty.Inventory.list_display
    list_filter = AdminProperty.Inventory.list_filter
    list_editable = AdminProperty.Inventory.list_editable
    ordering = AdminProperty.Inventory.ordering
    filter_horizontal = AdminProperty.Inventory.filter_horizontal
    fieldsets = AdminProperty.Inventory.fieldsets
    add_fieldsets = AdminProperty.Inventory.add_fieldsets
    prepopulated_fields = AdminProperty.Inventory.prepopulated_fields
    readonly_fields = AdminProperty.Inventory.readonly_fields
    list_per_page = AdminProperty.Inventory.list_per_page
    list_max_show_all = AdminProperty.Inventory.list_max_show_all
    search_help_text = AdminProperty.Inventory.search_help_text

    # inlines = (Inlines.XInlineAdmin)
    # x_inline = inlines[0].tag_inline





@admin.register(InventoryItem)
class InventoryitemAdmin(AdminProperty.Inventoryitem):
    model = InventoryItem
    search_fields = InventoryItem.SEARCH_FIELDS
    list_display = AdminProperty.Inventoryitem.list_display
    list_filter = AdminProperty.Inventoryitem.list_filter
    list_editable = AdminProperty.Inventoryitem.list_editable
    ordering = AdminProperty.Inventoryitem.ordering
    filter_horizontal = AdminProperty.Inventoryitem.filter_horizontal
    fieldsets = AdminProperty.Inventoryitem.fieldsets
    add_fieldsets = AdminProperty.Inventoryitem.add_fieldsets
    prepopulated_fields = AdminProperty.Inventoryitem.prepopulated_fields
    readonly_fields = AdminProperty.Inventoryitem.readonly_fields
    list_per_page = AdminProperty.Inventoryitem.list_per_page
    list_max_show_all = AdminProperty.Inventoryitem.list_max_show_all
    search_help_text = AdminProperty.Inventoryitem.search_help_text

    # inlines = (Inlines.XInlineAdmin)
    # x_inline = inlines[0].tag_inline





@admin.register(Inventoryitemproperty)
class InventoryitempropertyAdmin(AdminProperty.Inventoryitemproperty):
    model = Inventoryitemproperty
    search_fields = Inventoryitemproperty.SEARCH_FIELDS
    list_display = AdminProperty.Inventoryitemproperty.list_display
    list_filter = AdminProperty.Inventoryitemproperty.list_filter
    list_editable = AdminProperty.Inventoryitemproperty.list_editable
    ordering = AdminProperty.Inventoryitemproperty.ordering
    filter_horizontal = AdminProperty.Inventoryitemproperty.filter_horizontal
    fieldsets = AdminProperty.Inventoryitemproperty.fieldsets
    add_fieldsets = AdminProperty.Inventoryitemproperty.add_fieldsets
    prepopulated_fields = AdminProperty.Inventoryitemproperty.prepopulated_fields
    readonly_fields = AdminProperty.Inventoryitemproperty.readonly_fields
    list_per_page = AdminProperty.Inventoryitemproperty.list_per_page
    list_max_show_all = AdminProperty.Inventoryitemproperty.list_max_show_all
    search_help_text = AdminProperty.Inventoryitemproperty.search_help_text

    # inlines = (Inlines.XInlineAdmin)
    # x_inline = inlines[0].tag_inline





@admin.register(Property)
class PropertyAdmin(AdminProperty.Property):
    model = Property
    search_fields = Property.SEARCH_FIELDS
    list_display = AdminProperty.Property.list_display
    list_filter = AdminProperty.Property.list_filter
    list_editable = AdminProperty.Property.list_editable
    ordering = AdminProperty.Property.ordering
    filter_horizontal = AdminProperty.Property.filter_horizontal
    fieldsets = AdminProperty.Property.fieldsets
    add_fieldsets = AdminProperty.Property.add_fieldsets
    prepopulated_fields = AdminProperty.Property.prepopulated_fields
    readonly_fields = AdminProperty.Property.readonly_fields
    list_per_page = AdminProperty.Property.list_per_page
    list_max_show_all = AdminProperty.Property.list_max_show_all
    search_help_text = AdminProperty.Property.search_help_text

    # inlines = (Inlines.XInlineAdmin)
    # x_inline = inlines[0].tag_inline





@admin.register(Ordermarket)
class OrdermarketAdmin(AdminProperty.Ordermarket):
    model = Ordermarket
    search_fields = Ordermarket.SEARCH_FIELDS
    list_display = AdminProperty.Ordermarket.list_display
    list_filter = AdminProperty.Ordermarket.list_filter
    list_editable = AdminProperty.Ordermarket.list_editable
    ordering = AdminProperty.Ordermarket.ordering
    filter_horizontal = AdminProperty.Ordermarket.filter_horizontal
    fieldsets = AdminProperty.Ordermarket.fieldsets
    add_fieldsets = AdminProperty.Ordermarket.add_fieldsets
    prepopulated_fields = AdminProperty.Ordermarket.prepopulated_fields
    readonly_fields = AdminProperty.Ordermarket.readonly_fields
    list_per_page = AdminProperty.Ordermarket.list_per_page
    list_max_show_all = AdminProperty.Ordermarket.list_max_show_all
    search_help_text = AdminProperty.Ordermarket.search_help_text

    # inlines = (Inlines.XInlineAdmin)
    # x_inline = inlines[0].tag_inline


