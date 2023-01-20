
from django import forms
from django.contrib import admin
from django.template.loader import get_template

from Core.ProjectMixins.Apps.Shops_Mixins import AdminProperty
import Core.ProjectMixins.Base.AbsoluteUrl
from Core.admin import CustomInlineAdmin, CustomInlineAdminOneToMany
from .models import *

# Register your models here.



@admin.register(Address)
class AddressAdmin(AdminProperty.Address):
    model = Address
    search_fields = Address.SEARCH_FIELDS
    list_display = AdminProperty.Address.list_display
    list_filter = AdminProperty.Address.list_filter
    list_editable = AdminProperty.Address.list_editable
    ordering = AdminProperty.Address.ordering
    filter_horizontal = AdminProperty.Address.filter_horizontal
    fieldsets = AdminProperty.Address.fieldsets
    add_fieldsets = AdminProperty.Address.add_fieldsets
    prepopulated_fields = AdminProperty.Address.prepopulated_fields
    readonly_fields = AdminProperty.Address.readonly_fields
    list_per_page = AdminProperty.Address.list_per_page
    list_max_show_all = AdminProperty.Address.list_max_show_all
    search_help_text = AdminProperty.Address.search_help_text

    # inlines = (Inlines.XInlineAdmin)
    # x_inline = inlines[0].tag_inline









@admin.register(Discount)
class DiscountAdmin(AdminProperty.Discount):
    model = Discount
    search_fields = Discount.SEARCH_FIELDS
    list_display = AdminProperty.Discount.list_display
    list_filter = AdminProperty.Discount.list_filter
    list_editable = AdminProperty.Discount.list_editable
    ordering = AdminProperty.Discount.ordering
    filter_horizontal = AdminProperty.Discount.filter_horizontal
    fieldsets = AdminProperty.Discount.fieldsets
    add_fieldsets = AdminProperty.Discount.add_fieldsets
    prepopulated_fields = AdminProperty.Discount.prepopulated_fields
    readonly_fields = AdminProperty.Discount.readonly_fields
    list_per_page = AdminProperty.Discount.list_per_page
    list_max_show_all = AdminProperty.Discount.list_max_show_all
    search_help_text = AdminProperty.Discount.search_help_text

    # inlines = (Inlines.XInlineAdmin)
    # x_inline = inlines[0].tag_inline





@admin.register(Gallery)
class GalleryAdmin(AdminProperty.Gallery):
    model = Gallery
    search_fields = Gallery.SEARCH_FIELDS
    list_display = AdminProperty.Gallery.list_display
    list_filter = AdminProperty.Gallery.list_filter
    list_editable = AdminProperty.Gallery.list_editable
    ordering = AdminProperty.Gallery.ordering
    filter_horizontal = AdminProperty.Gallery.filter_horizontal
    fieldsets = AdminProperty.Gallery.fieldsets
    add_fieldsets = AdminProperty.Gallery.add_fieldsets
    prepopulated_fields = AdminProperty.Gallery.prepopulated_fields
    readonly_fields = AdminProperty.Gallery.readonly_fields
    list_per_page = AdminProperty.Gallery.list_per_page
    list_max_show_all = AdminProperty.Gallery.list_max_show_all
    search_help_text = AdminProperty.Gallery.search_help_text

    # inlines = (Inlines.XInlineAdmin)
    # x_inline = inlines[0].tag_inline





@admin.register(Image)
class ImageAdmin(AdminProperty.Image):
    model = Image
    search_fields = Image.SEARCH_FIELDS
    list_display = AdminProperty.Image.list_display
    list_filter = AdminProperty.Image.list_filter
    list_editable = AdminProperty.Image.list_editable
    ordering = AdminProperty.Image.ordering
    filter_horizontal = AdminProperty.Image.filter_horizontal
    fieldsets = AdminProperty.Image.fieldsets
    add_fieldsets = AdminProperty.Image.add_fieldsets
    prepopulated_fields = AdminProperty.Image.prepopulated_fields
    readonly_fields = AdminProperty.Image.readonly_fields
    list_per_page = AdminProperty.Image.list_per_page
    list_max_show_all = AdminProperty.Image.list_max_show_all
    search_help_text = AdminProperty.Image.search_help_text

    # inlines = (Inlines.XInlineAdmin)
    # x_inline = inlines[0].tag_inline





@admin.register(GalleryImage)
class GalleryimageAdmin(AdminProperty.Galleryimage):
    model = GalleryImage
    search_fields = GalleryImage.SEARCH_FIELDS
    list_display = AdminProperty.Galleryimage.list_display
    list_filter = AdminProperty.Galleryimage.list_filter
    list_editable = AdminProperty.Galleryimage.list_editable
    ordering = AdminProperty.Galleryimage.ordering
    filter_horizontal = AdminProperty.Galleryimage.filter_horizontal
    fieldsets = AdminProperty.Galleryimage.fieldsets
    add_fieldsets = AdminProperty.Galleryimage.add_fieldsets
    prepopulated_fields = AdminProperty.Galleryimage.prepopulated_fields
    readonly_fields = AdminProperty.Galleryimage.readonly_fields
    list_per_page = AdminProperty.Galleryimage.list_per_page
    list_max_show_all = AdminProperty.Galleryimage.list_max_show_all
    search_help_text = AdminProperty.Galleryimage.search_help_text

    # inlines = (Inlines.XInlineAdmin)
    # x_inline = inlines[0].tag_inline





@admin.register(Order)
class OrderAdmin(AdminProperty.Order):
    model = Order
    search_fields = Order.SEARCH_FIELDS
    list_display = AdminProperty.Order.list_display
    list_filter = AdminProperty.Order.list_filter
    list_editable = AdminProperty.Order.list_editable
    ordering = AdminProperty.Order.ordering
    filter_horizontal = AdminProperty.Order.filter_horizontal
    fieldsets = AdminProperty.Order.fieldsets
    add_fieldsets = AdminProperty.Order.add_fieldsets
    prepopulated_fields = AdminProperty.Order.prepopulated_fields
    readonly_fields = AdminProperty.Order.readonly_fields
    list_per_page = AdminProperty.Order.list_per_page
    list_max_show_all = AdminProperty.Order.list_max_show_all
    search_help_text = AdminProperty.Order.search_help_text

    # inlines = (Inlines.XInlineAdmin)
    # x_inline = inlines[0].tag_inline





@admin.register(OrderItem)
class OrderItemAdmin(AdminProperty.Orderitem):
    model = OrderItem
    search_fields = OrderItem.SEARCH_FIELDS
    list_display = AdminProperty.Orderitem.list_display
    list_filter = AdminProperty.Orderitem.list_filter
    list_editable = AdminProperty.Orderitem.list_editable
    ordering = AdminProperty.Orderitem.ordering
    filter_horizontal = AdminProperty.Orderitem.filter_horizontal
    fieldsets = AdminProperty.Orderitem.fieldsets
    add_fieldsets = AdminProperty.Orderitem.add_fieldsets
    prepopulated_fields = AdminProperty.Orderitem.prepopulated_fields
    readonly_fields = AdminProperty.Orderitem.readonly_fields
    list_per_page = AdminProperty.Orderitem.list_per_page
    list_max_show_all = AdminProperty.Orderitem.list_max_show_all
    search_help_text = AdminProperty.Orderitem.search_help_text

    # inlines = (Inlines.XInlineAdmin)
    # x_inline = inlines[0].tag_inline





@admin.register(Payment)
class PaymentAdmin(AdminProperty.Payment):
    model = Payment
    search_fields = Payment.SEARCH_FIELDS
    list_display = AdminProperty.Payment.list_display
    list_filter = AdminProperty.Payment.list_filter
    list_editable = AdminProperty.Payment.list_editable
    ordering = AdminProperty.Payment.ordering
    filter_horizontal = AdminProperty.Payment.filter_horizontal
    fieldsets = AdminProperty.Payment.fieldsets
    add_fieldsets = AdminProperty.Payment.add_fieldsets
    prepopulated_fields = AdminProperty.Payment.prepopulated_fields
    readonly_fields = AdminProperty.Payment.readonly_fields
    list_per_page = AdminProperty.Payment.list_per_page
    list_max_show_all = AdminProperty.Payment.list_max_show_all
    search_help_text = AdminProperty.Payment.search_help_text

    # inlines = (Inlines.XInlineAdmin)
    # x_inline = inlines[0].tag_inline





@admin.register(Wallet)
class WalletAdmin(AdminProperty.Wallet):
    model = Wallet
    search_fields = Wallet.SEARCH_FIELDS
    list_display = AdminProperty.Wallet.list_display
    list_filter = AdminProperty.Wallet.list_filter
    list_editable = AdminProperty.Wallet.list_editable
    ordering = AdminProperty.Wallet.ordering
    filter_horizontal = AdminProperty.Wallet.filter_horizontal
    fieldsets = AdminProperty.Wallet.fieldsets
    add_fieldsets = AdminProperty.Wallet.add_fieldsets
    prepopulated_fields = AdminProperty.Wallet.prepopulated_fields
    readonly_fields = AdminProperty.Wallet.readonly_fields
    list_per_page = AdminProperty.Wallet.list_per_page
    list_max_show_all = AdminProperty.Wallet.list_max_show_all
    search_help_text = AdminProperty.Wallet.search_help_text

    # inlines = (Inlines.XInlineAdmin)
    # x_inline = inlines[0].tag_inline





@admin.register(Shipment)
class ShipmentAdmin(AdminProperty.Shipment):
    model = Shipment
    search_fields = Shipment.SEARCH_FIELDS
    list_display = AdminProperty.Shipment.list_display
    list_filter = AdminProperty.Shipment.list_filter
    list_editable = AdminProperty.Shipment.list_editable
    ordering = AdminProperty.Shipment.ordering
    filter_horizontal = AdminProperty.Shipment.filter_horizontal
    fieldsets = AdminProperty.Shipment.fieldsets
    add_fieldsets = AdminProperty.Shipment.add_fieldsets
    prepopulated_fields = AdminProperty.Shipment.prepopulated_fields
    readonly_fields = AdminProperty.Shipment.readonly_fields
    list_per_page = AdminProperty.Shipment.list_per_page
    list_max_show_all = AdminProperty.Shipment.list_max_show_all
    search_help_text = AdminProperty.Shipment.search_help_text

    # inlines = (Inlines.XInlineAdmin)
    # x_inline = inlines[0].tag_inline





@admin.register(Contactus)
class ContactusAdmin(AdminProperty.Contactus):
    model = Contactus
    search_fields = Contactus.SEARCH_FIELDS
    list_display = AdminProperty.Contactus.list_display
    list_filter = AdminProperty.Contactus.list_filter
    list_editable = AdminProperty.Contactus.list_editable
    ordering = AdminProperty.Contactus.ordering
    filter_horizontal = AdminProperty.Contactus.filter_horizontal
    fieldsets = AdminProperty.Contactus.fieldsets
    add_fieldsets = AdminProperty.Contactus.add_fieldsets
    prepopulated_fields = AdminProperty.Contactus.prepopulated_fields
    readonly_fields = AdminProperty.Contactus.readonly_fields
    list_per_page = AdminProperty.Contactus.list_per_page
    list_max_show_all = AdminProperty.Contactus.list_max_show_all
    search_help_text = AdminProperty.Contactus.search_help_text

    # inlines = (Inlines.XInlineAdmin)
    # x_inline = inlines[0].tag_inline


