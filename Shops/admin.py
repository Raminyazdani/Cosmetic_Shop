from django import forms
from django.contrib import admin
from django.template.loader import get_template

from Core.ProjectMixins.Apps.Shops_Mixins import AdminProperty
import Core.ProjectMixins.Base.AbsoluteUrl
from Core.admin import CustomInlineAdmin, CustomInlineAdminOneToMany
from .models import *

# Shops

# Address

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

#### custom query set  # def get_queryset(self, request):  #     # use our manager, rather than the default one  #  #     qs = super().get_queryset(request)  #     qs = qs.annotate(comment_count=Count('comment'))  #     qs = qs.annotate(tag_count=Count('tag'))  #     qs = qs.annotate(brand_count=Count('brand'))  #     qs = qs.annotate(category_count=Count('category'))  #     return qs


# Coupon

# Register your models here.
@admin.register(Coupon)
class CouponAdmin(AdminProperty.Coupon):
    model = Coupon
    search_fields = Coupon.SEARCH_FIELDS
    list_display = AdminProperty.Coupon.list_display
    list_filter = AdminProperty.Coupon.list_filter
    list_editable = AdminProperty.Coupon.list_editable
    ordering = AdminProperty.Coupon.ordering
    filter_horizontal = AdminProperty.Coupon.filter_horizontal
    fieldsets = AdminProperty.Coupon.fieldsets
    add_fieldsets = AdminProperty.Coupon.add_fieldsets
    prepopulated_fields = AdminProperty.Coupon.prepopulated_fields
    readonly_fields = AdminProperty.Coupon.readonly_fields
    list_per_page = AdminProperty.Coupon.list_per_page
    list_max_show_all = AdminProperty.Coupon.list_max_show_all
    search_help_text = AdminProperty.Coupon.search_help_text

    # inlines = (Inlines.XInlineAdmin)
    # x_inline = inlines[0].tag_inline

#### custom query set  # def get_queryset(self, request):  #     # use our manager, rather than the default one  #  #     qs = super().get_queryset(request)  #     qs = qs.annotate(comment_count=Count('comment'))  #     qs = qs.annotate(tag_count=Count('tag'))  #     qs = qs.annotate(brand_count=Count('brand'))  #     qs = qs.annotate(category_count=Count('category'))  #     return qs



# Discount

# Register your models here.
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

#### custom query set  # def get_queryset(self, request):  #     # use our manager, rather than the default one  #  #     qs = super().get_queryset(request)  #     qs = qs.annotate(comment_count=Count('comment'))  #     qs = qs.annotate(tag_count=Count('tag'))  #     qs = qs.annotate(brand_count=Count('brand'))  #     qs = qs.annotate(category_count=Count('category'))  #     return qs



# Gallery

# Register your models here.
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

#### custom query set  # def get_queryset(self, request):  #     # use our manager, rather than the default one  #  #     qs = super().get_queryset(request)  #     qs = qs.annotate(comment_count=Count('comment'))  #     qs = qs.annotate(tag_count=Count('tag'))  #     qs = qs.annotate(brand_count=Count('brand'))  #     qs = qs.annotate(category_count=Count('category'))  #     return qs



# Image

# Register your models here.
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

#### custom query set  # def get_queryset(self, request):  #     # use our manager, rather than the default one  #  #     qs = super().get_queryset(request)  #     qs = qs.annotate(comment_count=Count('comment'))  #     qs = qs.annotate(tag_count=Count('tag'))  #     qs = qs.annotate(brand_count=Count('brand'))  #     qs = qs.annotate(category_count=Count('category'))  #     return qs



# Order

# Register your models here.
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

#### custom query set  # def get_queryset(self, request):  #     # use our manager, rather than the default one  #  #     qs = super().get_queryset(request)  #     qs = qs.annotate(comment_count=Count('comment'))  #     qs = qs.annotate(tag_count=Count('tag'))  #     qs = qs.annotate(brand_count=Count('brand'))  #     qs = qs.annotate(category_count=Count('category'))  #     return qs



# OrderItem

# Register your models here.
@admin.register(OrderItem)
class OrderItemAdmin(AdminProperty.OrderItem):
    model = OrderItem
    search_fields = OrderItem.SEARCH_FIELDS
    list_display = AdminProperty.OrderItem.list_display
    list_filter = AdminProperty.OrderItem.list_filter
    list_editable = AdminProperty.OrderItem.list_editable
    ordering = AdminProperty.OrderItem.ordering
    filter_horizontal = AdminProperty.OrderItem.filter_horizontal
    fieldsets = AdminProperty.OrderItem.fieldsets
    add_fieldsets = AdminProperty.OrderItem.add_fieldsets
    prepopulated_fields = AdminProperty.OrderItem.prepopulated_fields
    readonly_fields = AdminProperty.OrderItem.readonly_fields
    list_per_page = AdminProperty.OrderItem.list_per_page
    list_max_show_all = AdminProperty.OrderItem.list_max_show_all
    search_help_text = AdminProperty.OrderItem.search_help_text

    # inlines = (Inlines.XInlineAdmin)
    # x_inline = inlines[0].tag_inline

#### custom query set  # def get_queryset(self, request):  #     # use our manager, rather than the default one  #  #     qs = super().get_queryset(request)  #     qs = qs.annotate(comment_count=Count('comment'))  #     qs = qs.annotate(tag_count=Count('tag'))  #     qs = qs.annotate(brand_count=Count('brand'))  #     qs = qs.annotate(category_count=Count('category'))  #     return qs



# Payment

# Register your models here.
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

#### custom query set  # def get_queryset(self, request):  #     # use our manager, rather than the default one  #  #     qs = super().get_queryset(request)  #     qs = qs.annotate(comment_count=Count('comment'))  #     qs = qs.annotate(tag_count=Count('tag'))  #     qs = qs.annotate(brand_count=Count('brand'))  #     qs = qs.annotate(category_count=Count('category'))  #     return qs



# Wallet

# Register your models here.
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

#### custom query set  # def get_queryset(self, request):  #     # use our manager, rather than the default one  #  #     qs = super().get_queryset(request)  #     qs = qs.annotate(comment_count=Count('comment'))  #     qs = qs.annotate(tag_count=Count('tag'))  #     qs = qs.annotate(brand_count=Count('brand'))  #     qs = qs.annotate(category_count=Count('category'))  #     return qs



# Shipment

# Register your models here.
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

#### custom query set  # def get_queryset(self, request):  #     # use our manager, rather than the default one  #  #     qs = super().get_queryset(request)  #     qs = qs.annotate(comment_count=Count('comment'))  #     qs = qs.annotate(tag_count=Count('tag'))  #     qs = qs.annotate(brand_count=Count('brand'))  #     qs = qs.annotate(category_count=Count('category'))  #     return qs



# ShipmentItem

# Register your models here.
@admin.register(ShipmentItem)
class ShipmentItemAdmin(AdminProperty.ShipmentItem):
    model = ShipmentItem
    search_fields = ShipmentItem.SEARCH_FIELDS
    list_display = AdminProperty.ShipmentItem.list_display
    list_filter = AdminProperty.ShipmentItem.list_filter
    list_editable = AdminProperty.ShipmentItem.list_editable
    ordering = AdminProperty.ShipmentItem.ordering
    filter_horizontal = AdminProperty.ShipmentItem.filter_horizontal
    fieldsets = AdminProperty.ShipmentItem.fieldsets
    add_fieldsets = AdminProperty.ShipmentItem.add_fieldsets
    prepopulated_fields = AdminProperty.ShipmentItem.prepopulated_fields
    readonly_fields = AdminProperty.ShipmentItem.readonly_fields
    list_per_page = AdminProperty.ShipmentItem.list_per_page
    list_max_show_all = AdminProperty.ShipmentItem.list_max_show_all
    search_help_text = AdminProperty.ShipmentItem.search_help_text

    # inlines = (Inlines.XInlineAdmin)
    # x_inline = inlines[0].tag_inline

#### custom query set  # def get_queryset(self, request):  #     # use our manager, rather than the default one  #  #     qs = super().get_queryset(request)  #     qs = qs.annotate(comment_count=Count('comment'))  #     qs = qs.annotate(tag_count=Count('tag'))  #     qs = qs.annotate(brand_count=Count('brand'))  #     qs = qs.annotate(category_count=Count('category'))  #     return qs



# ContactUs

# Register your models here.
@admin.register(ContactUs)
class ContactUsAdmin(AdminProperty.ContactUs):
    model = ContactUs
    search_fields = ContactUs.SEARCH_FIELDS
    list_display = AdminProperty.ContactUs.list_display
    list_filter = AdminProperty.ContactUs.list_filter
    list_editable = AdminProperty.ContactUs.list_editable
    ordering = AdminProperty.ContactUs.ordering
    filter_horizontal = AdminProperty.ContactUs.filter_horizontal
    fieldsets = AdminProperty.ContactUs.fieldsets
    add_fieldsets = AdminProperty.ContactUs.add_fieldsets
    prepopulated_fields = AdminProperty.ContactUs.prepopulated_fields
    readonly_fields = AdminProperty.ContactUs.readonly_fields
    list_per_page = AdminProperty.ContactUs.list_per_page
    list_max_show_all = AdminProperty.ContactUs.list_max_show_all
    search_help_text = AdminProperty.ContactUs.search_help_text

    # inlines = (Inlines.XInlineAdmin)
    # x_inline = inlines[0].tag_inline

#### custom query set  # def get_queryset(self, request):  #     # use our manager, rather than the default one  #  #     qs = super().get_queryset(request)  #     qs = qs.annotate(comment_count=Count('comment'))  #     qs = qs.annotate(tag_count=Count('tag'))  #     qs = qs.annotate(brand_count=Count('brand'))  #     qs = qs.annotate(category_count=Count('category'))  #     return qs


