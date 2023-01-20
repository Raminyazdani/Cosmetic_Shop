
from django import forms
from django.contrib import admin
from django.template.loader import get_template

from Core.ProjectMixins.Apps.Customers_Mixins import AdminProperty
import Core.ProjectMixins.Base.AbsoluteUrl
from Core.admin import CustomInlineAdmin, CustomInlineAdminOneToMany
from .models import *

# Register your models here.



@admin.register(Customer)
class CustomerAdmin(AdminProperty.Customer):
    model = Customer
    search_fields = Customer.SEARCH_FIELDS
    list_display = AdminProperty.Customer.list_display
    list_filter = AdminProperty.Customer.list_filter
    list_editable = AdminProperty.Customer.list_editable
    ordering = AdminProperty.Customer.ordering
    filter_horizontal = AdminProperty.Customer.filter_horizontal
    fieldsets = AdminProperty.Customer.fieldsets
    add_fieldsets = AdminProperty.Customer.add_fieldsets
    prepopulated_fields = AdminProperty.Customer.prepopulated_fields
    readonly_fields = AdminProperty.Customer.readonly_fields
    list_per_page = AdminProperty.Customer.list_per_page
    list_max_show_all = AdminProperty.Customer.list_max_show_all
    search_help_text = AdminProperty.Customer.search_help_text

    # inlines = (Inlines.XInlineAdmin)
    # x_inline = inlines[0].tag_inline





@admin.register(Cart)
class CartAdmin(AdminProperty.Cart):
    model = Cart
    search_fields = Cart.SEARCH_FIELDS
    list_display = AdminProperty.Cart.list_display
    list_filter = AdminProperty.Cart.list_filter
    list_editable = AdminProperty.Cart.list_editable
    ordering = AdminProperty.Cart.ordering
    filter_horizontal = AdminProperty.Cart.filter_horizontal
    fieldsets = AdminProperty.Cart.fieldsets
    add_fieldsets = AdminProperty.Cart.add_fieldsets
    prepopulated_fields = AdminProperty.Cart.prepopulated_fields
    readonly_fields = AdminProperty.Cart.readonly_fields
    list_per_page = AdminProperty.Cart.list_per_page
    list_max_show_all = AdminProperty.Cart.list_max_show_all
    search_help_text = AdminProperty.Cart.search_help_text

    # inlines = (Inlines.XInlineAdmin)
    # x_inline = inlines[0].tag_inline





@admin.register(CartItem)
class CartitemAdmin(AdminProperty.Cartitem):
    model = CartItem
    search_fields = CartItem.SEARCH_FIELDS
    list_display = AdminProperty.Cartitem.list_display
    list_filter = AdminProperty.Cartitem.list_filter
    list_editable = AdminProperty.Cartitem.list_editable
    ordering = AdminProperty.Cartitem.ordering
    filter_horizontal = AdminProperty.Cartitem.filter_horizontal
    fieldsets = AdminProperty.Cartitem.fieldsets
    add_fieldsets = AdminProperty.Cartitem.add_fieldsets
    prepopulated_fields = AdminProperty.Cartitem.prepopulated_fields
    readonly_fields = AdminProperty.Cartitem.readonly_fields
    list_per_page = AdminProperty.Cartitem.list_per_page
    list_max_show_all = AdminProperty.Cartitem.list_max_show_all
    search_help_text = AdminProperty.Cartitem.search_help_text

    # inlines = (Inlines.XInlineAdmin)
    # x_inline = inlines[0].tag_inline





@admin.register(CustomerCoupon)
class CustomerCouponAdmin(AdminProperty.CustomerCoupon):
    model = CustomerCoupon
    search_fields = CustomerCoupon.SEARCH_FIELDS
    list_display = AdminProperty.CustomerCoupon.list_display
    list_filter = AdminProperty.CustomerCoupon.list_filter
    list_editable = AdminProperty.CustomerCoupon.list_editable
    ordering = AdminProperty.CustomerCoupon.ordering
    filter_horizontal = AdminProperty.CustomerCoupon.filter_horizontal
    fieldsets = AdminProperty.CustomerCoupon.fieldsets
    add_fieldsets = AdminProperty.CustomerCoupon.add_fieldsets
    prepopulated_fields = AdminProperty.CustomerCoupon.prepopulated_fields
    readonly_fields = AdminProperty.CustomerCoupon.readonly_fields
    list_per_page = AdminProperty.CustomerCoupon.list_per_page
    list_max_show_all = AdminProperty.CustomerCoupon.list_max_show_all
    search_help_text = AdminProperty.CustomerCoupon.search_help_text

    # inlines = (Inlines.XInlineAdmin)
    # x_inline = inlines[0].tag_inline





@admin.register(Favorite)
class FavoriteAdmin(AdminProperty.Favorite):
    model = Favorite
    search_fields = Favorite.SEARCH_FIELDS
    list_display = AdminProperty.Favorite.list_display
    list_filter = AdminProperty.Favorite.list_filter
    list_editable = AdminProperty.Favorite.list_editable
    ordering = AdminProperty.Favorite.ordering
    filter_horizontal = AdminProperty.Favorite.filter_horizontal
    fieldsets = AdminProperty.Favorite.fieldsets
    add_fieldsets = AdminProperty.Favorite.add_fieldsets
    prepopulated_fields = AdminProperty.Favorite.prepopulated_fields
    readonly_fields = AdminProperty.Favorite.readonly_fields
    list_per_page = AdminProperty.Favorite.list_per_page
    list_max_show_all = AdminProperty.Favorite.list_max_show_all
    search_help_text = AdminProperty.Favorite.search_help_text

    # inlines = (Inlines.XInlineAdmin)
    # x_inline = inlines[0].tag_inline





@admin.register(FavoriteItem)
class FavoriteitemAdmin(AdminProperty.Favoriteitem):
    model = FavoriteItem
    search_fields = FavoriteItem.SEARCH_FIELDS
    list_display = AdminProperty.Favoriteitem.list_display
    list_filter = AdminProperty.Favoriteitem.list_filter
    list_editable = AdminProperty.Favoriteitem.list_editable
    ordering = AdminProperty.Favoriteitem.ordering
    filter_horizontal = AdminProperty.Favoriteitem.filter_horizontal
    fieldsets = AdminProperty.Favoriteitem.fieldsets
    add_fieldsets = AdminProperty.Favoriteitem.add_fieldsets
    prepopulated_fields = AdminProperty.Favoriteitem.prepopulated_fields
    readonly_fields = AdminProperty.Favoriteitem.readonly_fields
    list_per_page = AdminProperty.Favoriteitem.list_per_page
    list_max_show_all = AdminProperty.Favoriteitem.list_max_show_all
    search_help_text = AdminProperty.Favoriteitem.search_help_text

    # inlines = (Inlines.XInlineAdmin)
    # x_inline = inlines[0].tag_inline

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





@admin.register(OrderCustomer)
class OrderCustomerAdmin(AdminProperty.Ordercustomer):
    model = OrderCustomer
    search_fields = OrderCustomer.SEARCH_FIELDS
    list_display = AdminProperty.Ordercustomer.list_display
    list_filter = AdminProperty.Ordercustomer.list_filter
    list_editable = AdminProperty.Ordercustomer.list_editable
    ordering = AdminProperty.Ordercustomer.ordering
    filter_horizontal = AdminProperty.Ordercustomer.filter_horizontal
    fieldsets = AdminProperty.Ordercustomer.fieldsets
    add_fieldsets = AdminProperty.Ordercustomer.add_fieldsets
    prepopulated_fields = AdminProperty.Ordercustomer.prepopulated_fields
    readonly_fields = AdminProperty.Ordercustomer.readonly_fields
    list_per_page = AdminProperty.Ordercustomer.list_per_page
    list_max_show_all = AdminProperty.Ordercustomer.list_max_show_all
    search_help_text = AdminProperty.Ordercustomer.search_help_text

    # inlines = (Inlines.XInlineAdmin)
    # x_inline = inlines[0].tag_inline





@admin.register(Wishlist)
class WishlistAdmin(AdminProperty.Wishlist):
    model = Wishlist
    search_fields = Wishlist.SEARCH_FIELDS
    list_display = AdminProperty.Wishlist.list_display
    list_filter = AdminProperty.Wishlist.list_filter
    list_editable = AdminProperty.Wishlist.list_editable
    ordering = AdminProperty.Wishlist.ordering
    filter_horizontal = AdminProperty.Wishlist.filter_horizontal
    fieldsets = AdminProperty.Wishlist.fieldsets
    add_fieldsets = AdminProperty.Wishlist.add_fieldsets
    prepopulated_fields = AdminProperty.Wishlist.prepopulated_fields
    readonly_fields = AdminProperty.Wishlist.readonly_fields
    list_per_page = AdminProperty.Wishlist.list_per_page
    list_max_show_all = AdminProperty.Wishlist.list_max_show_all
    search_help_text = AdminProperty.Wishlist.search_help_text

    # inlines = (Inlines.XInlineAdmin)
    # x_inline = inlines[0].tag_inline





@admin.register(Wishlistitem)
class WishlistitemAdmin(AdminProperty.Wishlistitem):
    model = Wishlistitem
    search_fields = Wishlistitem.SEARCH_FIELDS
    list_display = AdminProperty.Wishlistitem.list_display
    list_filter = AdminProperty.Wishlistitem.list_filter
    list_editable = AdminProperty.Wishlistitem.list_editable
    ordering = AdminProperty.Wishlistitem.ordering
    filter_horizontal = AdminProperty.Wishlistitem.filter_horizontal
    fieldsets = AdminProperty.Wishlistitem.fieldsets
    add_fieldsets = AdminProperty.Wishlistitem.add_fieldsets
    prepopulated_fields = AdminProperty.Wishlistitem.prepopulated_fields
    readonly_fields = AdminProperty.Wishlistitem.readonly_fields
    list_per_page = AdminProperty.Wishlistitem.list_per_page
    list_max_show_all = AdminProperty.Wishlistitem.list_max_show_all
    search_help_text = AdminProperty.Wishlistitem.search_help_text

    # inlines = (Inlines.XInlineAdmin)
    # x_inline = inlines[0].tag_inline


