from Core.admin import BaseAdminInlineRender, BaseAdminSlug, CustomInlineAdmin
from Core.ProjectMixins.Base.BaseInline import InlineMethods
from Markets.models import *
from Customers.models import *
from Shops.models import *
from Products.models import *
from Users.models import *

class Customer(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True
    add_fieldsets = []
    fieldsets = (('Profiling', {'classes': ('extrapretty',), 'fields': (('id', 'uuid', 'slug'), ('gender', 'img_preview'))}), ('Extras', {'classes': ('extrapretty', 'collapse'), 'fields': (('bio', 'email', 'firstname'), ('lastname', 'user_name'))}), ('Conditions', {'classes': 'extrapretty', 'fields': (('is_delete', 'is_email_verified'),)}), ('Time', {'classes': ('extrapretty',), 'fields': (('created_at', 'modified_at', 'deleted_on'),)}), ('Relations', {'classes': ('extrapretty', 'collapse'), 'fields': ('cart', 'favorite', 'wishlist', 'coupons', 'orders', 'comments', 'order_item', 'user')}), ('Properties', {'classes': ('extrapretty', 'collapse'), 'fields': ('coupon_unused_objects', 'order_objects', 'user_object', 'coupon_used_objects', 'order_order_items', 'coupon_used_order_objects', 'order_finished_amount', 'order_finished_count', 'coupon_count', 'order_pending_amount', 'order_pending_count', 'favorite_items_objects', 'coupon_objects', 'cart_item_inventory_items', 'comment_count', 'cart_items_objects', 'images', 'cart_object', 'comment_product_objects', 'order_pending_objects', 'comment_product_count', 'order_finished_objects', 'wish_list_items_products', 'favorite_items_products', 'cart_item_products', 'favorite_items_count', 'wishlist_object', 'order_finished_order_items', 'wish_list_items_count', 'coupon_unused_count', 'coupon_used_count', 'wish_list_items_objects', 'primary_image', 'favorite_object', 'order_pending_order_items', 'cart_item_count', 'comment_objects', 'order_counts')}))
    filter_horizontal = []
    list_display = ['__str__', 'id', 'user_name', 'slug', 'cart', 'favorite', 'wishlist', 'is_delete', 'is_email_verified', 'created_at']
    list_display_links = ['__str__', 'cart', 'favorite', 'wishlist']
    list_editable = ['user_name', 'is_delete', 'is_email_verified']
    list_filter = ['is_delete', 'is_email_verified', 'cart', 'favorite', 'wishlist', 'coupons', 'orders', 'comments', 'order_item', 'user']
    list_max_show_all = 100
    list_per_page = 25
    list_select_related = True
    ordering = ['created_at']
    prepopulated_fields = {'slug': ('id',)}
    readonly_fields = ['slug', 'img_preview', 'created_at', 'modified_at', 'deleted_on', 'coupons', 'orders', 'comments', 'order_item', 'user', 'id', 'uuid', 'slug', 'img_preview', 'cart', 'favorite', 'wishlist', 'coupon_unused_objects', 'order_objects', 'user_object', 'coupon_used_objects', 'order_order_items', 'coupon_used_order_objects', 'order_finished_amount', 'order_finished_count', 'coupon_count', 'order_pending_amount', 'order_pending_count', 'favorite_items_objects', 'coupon_objects', 'cart_item_inventory_items', 'comment_count', 'cart_items_objects', 'images', 'cart_object', 'comment_product_objects', 'order_pending_objects', 'comment_product_count', 'order_finished_objects', 'wish_list_items_products', 'favorite_items_products', 'cart_item_products', 'favorite_items_count', 'wishlist_object', 'order_finished_order_items', 'wish_list_items_count', 'coupon_unused_count', 'coupon_used_count', 'wish_list_items_objects', 'primary_image', 'favorite_object', 'order_pending_order_items', 'cart_item_count', 'comment_objects', 'order_counts']
    search_help_text = ''

    def coupons(self, obj):
        if  obj.coupons.all().count() > 0:
            return obj.coupons.all()
        return None
            
    def orders(self, obj):
        if  obj.orders.all().count() > 0:
            return obj.orders.all()
        return None
            
    def comments(self, obj):
        if  obj.comments.all().count() > 0:
            return obj.comments.all()
        return None
            
    def order_item(self, obj):
        if  obj.order_item.all().count() > 0:
            return obj.order_item.all()
        return None
            
    def user(self, obj):
        if  obj.user.all().count() > 0:
            return obj.user.all()
        return None
            
    def coupon_unused_objects(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.coupon_unused_objects]
    else:
        temp = [obj.coupon_unused_objects]
    if len(temp) > 0:
        return temp
    return None

    def order_objects(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.order_objects]
    else:
        temp = [obj.order_objects]
    if len(temp) > 0:
        return temp
    return None

    def user_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.user_object]
    else:
        temp = [obj.user_object]
    if len(temp) > 0:
        return temp
    return None

    def coupon_used_objects(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.coupon_used_objects]
    else:
        temp = [obj.coupon_used_objects]
    if len(temp) > 0:
        return temp
    return None

    def order_order_items(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.order_order_items]
    else:
        temp = [obj.order_order_items]
    if len(temp) > 0:
        return temp
    return None

    def coupon_used_order_objects(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.coupon_used_order_objects]
    else:
        temp = [obj.coupon_used_order_objects]
    if len(temp) > 0:
        return temp
    return None

    def order_finished_amount(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.order_finished_amount]
    else:
        temp = [obj.order_finished_amount]
    if len(temp) > 0:
        return temp
    return None

    def order_finished_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.order_finished_count]
    else:
        temp = [obj.order_finished_count]
    if len(temp) > 0:
        return temp
    return None

    def coupon_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.coupon_count]
    else:
        temp = [obj.coupon_count]
    if len(temp) > 0:
        return temp
    return None

    def order_pending_amount(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.order_pending_amount]
    else:
        temp = [obj.order_pending_amount]
    if len(temp) > 0:
        return temp
    return None

    def order_pending_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.order_pending_count]
    else:
        temp = [obj.order_pending_count]
    if len(temp) > 0:
        return temp
    return None

    def favorite_items_objects(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.favorite_items_objects]
    else:
        temp = [obj.favorite_items_objects]
    if len(temp) > 0:
        return temp
    return None

    def coupon_objects(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.coupon_objects]
    else:
        temp = [obj.coupon_objects]
    if len(temp) > 0:
        return temp
    return None

    def cart_item_inventory_items(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.cart_item_inventory_items]
    else:
        temp = [obj.cart_item_inventory_items]
    if len(temp) > 0:
        return temp
    return None

    def comment_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.comment_count]
    else:
        temp = [obj.comment_count]
    if len(temp) > 0:
        return temp
    return None

    def cart_items_objects(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.cart_items_objects]
    else:
        temp = [obj.cart_items_objects]
    if len(temp) > 0:
        return temp
    return None

    def images(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.images]
    else:
        temp = [obj.images]
    if len(temp) > 0:
        return temp
    return None

    def cart_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.cart_object]
    else:
        temp = [obj.cart_object]
    if len(temp) > 0:
        return temp
    return None

    def comment_product_objects(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.comment_product_objects]
    else:
        temp = [obj.comment_product_objects]
    if len(temp) > 0:
        return temp
    return None

    def order_pending_objects(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.order_pending_objects]
    else:
        temp = [obj.order_pending_objects]
    if len(temp) > 0:
        return temp
    return None

    def comment_product_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.comment_product_count]
    else:
        temp = [obj.comment_product_count]
    if len(temp) > 0:
        return temp
    return None

    def order_finished_objects(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.order_finished_objects]
    else:
        temp = [obj.order_finished_objects]
    if len(temp) > 0:
        return temp
    return None

    def wish_list_items_products(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.wish_list_items_products]
    else:
        temp = [obj.wish_list_items_products]
    if len(temp) > 0:
        return temp
    return None

    def favorite_items_products(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.favorite_items_products]
    else:
        temp = [obj.favorite_items_products]
    if len(temp) > 0:
        return temp
    return None

    def cart_item_products(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.cart_item_products]
    else:
        temp = [obj.cart_item_products]
    if len(temp) > 0:
        return temp
    return None

    def favorite_items_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.favorite_items_count]
    else:
        temp = [obj.favorite_items_count]
    if len(temp) > 0:
        return temp
    return None

    def wishlist_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.wishlist_object]
    else:
        temp = [obj.wishlist_object]
    if len(temp) > 0:
        return temp
    return None

    def order_finished_order_items(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.order_finished_order_items]
    else:
        temp = [obj.order_finished_order_items]
    if len(temp) > 0:
        return temp
    return None

    def wish_list_items_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.wish_list_items_count]
    else:
        temp = [obj.wish_list_items_count]
    if len(temp) > 0:
        return temp
    return None

    def coupon_unused_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.coupon_unused_count]
    else:
        temp = [obj.coupon_unused_count]
    if len(temp) > 0:
        return temp
    return None

    def coupon_used_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.coupon_used_count]
    else:
        temp = [obj.coupon_used_count]
    if len(temp) > 0:
        return temp
    return None

    def wish_list_items_objects(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.wish_list_items_objects]
    else:
        temp = [obj.wish_list_items_objects]
    if len(temp) > 0:
        return temp
    return None

    def primary_image(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.primary_image]
    else:
        temp = [obj.primary_image]
    if len(temp) > 0:
        return temp
    return None

    def favorite_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.favorite_object]
    else:
        temp = [obj.favorite_object]
    if len(temp) > 0:
        return temp
    return None

    def order_pending_order_items(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.order_pending_order_items]
    else:
        temp = [obj.order_pending_order_items]
    if len(temp) > 0:
        return temp
    return None

    def cart_item_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.cart_item_count]
    else:
        temp = [obj.cart_item_count]
    if len(temp) > 0:
        return temp
    return None

    def comment_objects(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.comment_objects]
    else:
        temp = [obj.comment_objects]
    if len(temp) > 0:
        return temp
    return None

    def order_counts(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.order_counts]
    else:
        temp = [obj.order_counts]
    if len(temp) > 0:
        return temp
    return None


class Cart(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True
    add_fieldsets = []
    fieldsets = (('Profiling', {'classes': ('extrapretty',), 'fields': (('id', 'uuid', 'slug'),)}), ('Conditions', {'classes': 'extrapretty', 'fields': (('is_delete',),)}), ('Time', {'classes': ('extrapretty',), 'fields': (('created_at', 'modified_at', 'deleted_on'),)}), ('Relations', {'classes': ('extrapretty', 'collapse'), 'fields': ('customer', 'cart_items')}), ('Properties', {'classes': ('extrapretty', 'collapse'), 'fields': ('customer_object', 'cart_price_discount', 'cart_price_final', 'cart_item_count', 'cart_price_tax', 'cart_items_objects', 'cart_price_total')}))
    filter_horizontal = []
    list_display = ['__str__', 'id', 'slug', 'is_delete', 'created_at']
    list_display_links = ['__str__']
    list_editable = ['is_delete']
    list_filter = ['is_delete', 'customer', 'cart_items']
    list_max_show_all = 100
    list_per_page = 25
    list_select_related = True
    ordering = ['created_at']
    prepopulated_fields = {'slug': ('id',)}
    readonly_fields = ['slug', 'created_at', 'modified_at', 'deleted_on', 'customer', 'cart_items', 'id', 'uuid', 'slug', 'customer_object', 'cart_price_discount', 'cart_price_final', 'cart_item_count', 'cart_price_tax', 'cart_items_objects', 'cart_price_total']
    search_help_text = ''

    def customer(self, obj):
        if  obj.customer.all().count() > 0:
            return obj.customer.all()
        return None
            
    def cart_items(self, obj):
        if  obj.cart_items.all().count() > 0:
            return obj.cart_items.all()
        return None
            
    def customer_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.customer_object]
    else:
        temp = [obj.customer_object]
    if len(temp) > 0:
        return temp
    return None

    def cart_price_discount(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.cart_price_discount]
    else:
        temp = [obj.cart_price_discount]
    if len(temp) > 0:
        return temp
    return None

    def cart_price_final(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.cart_price_final]
    else:
        temp = [obj.cart_price_final]
    if len(temp) > 0:
        return temp
    return None

    def cart_item_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.cart_item_count]
    else:
        temp = [obj.cart_item_count]
    if len(temp) > 0:
        return temp
    return None

    def cart_price_tax(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.cart_price_tax]
    else:
        temp = [obj.cart_price_tax]
    if len(temp) > 0:
        return temp
    return None

    def cart_items_objects(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.cart_items_objects]
    else:
        temp = [obj.cart_items_objects]
    if len(temp) > 0:
        return temp
    return None

    def cart_price_total(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.cart_price_total]
    else:
        temp = [obj.cart_price_total]
    if len(temp) > 0:
        return temp
    return None


class CartItem(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True
    add_fieldsets = []
    fieldsets = (('Profiling', {'classes': ('extrapretty',), 'fields': (('id', 'uuid', 'slug'), ('quantity',))}), ('Conditions', {'classes': 'extrapretty', 'fields': (('is_delete',),)}), ('Time', {'classes': ('extrapretty',), 'fields': (('created_at', 'modified_at', 'deleted_on'),)}), ('Relations', {'classes': ('extrapretty', 'collapse'), 'fields': ('inventory_item', 'cart')}), ('Properties', {'classes': ('extrapretty', 'collapse'), 'fields': ('customer_object', 'price_total', 'inventory_item_object', 'primary_image', 'price_tax', 'price_discount', 'product_object', 'price_final', 'cart_object')}))
    filter_horizontal = []
    list_display = ['__str__', 'id', 'slug', 'is_delete', 'created_at']
    list_display_links = ['__str__']
    list_editable = ['is_delete']
    list_filter = ['is_delete', 'inventory_item', 'cart']
    list_max_show_all = 100
    list_per_page = 25
    list_select_related = True
    ordering = ['created_at']
    prepopulated_fields = {'slug': ('id',)}
    readonly_fields = ['slug', 'created_at', 'modified_at', 'deleted_on', 'id', 'uuid', 'slug', 'customer_object', 'price_total', 'inventory_item_object', 'primary_image', 'price_tax', 'price_discount', 'product_object', 'price_final', 'cart_object']
    search_help_text = ''

    def customer_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.customer_object]
    else:
        temp = [obj.customer_object]
    if len(temp) > 0:
        return temp
    return None

    def price_total(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.price_total]
    else:
        temp = [obj.price_total]
    if len(temp) > 0:
        return temp
    return None

    def inventory_item_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.inventory_item_object]
    else:
        temp = [obj.inventory_item_object]
    if len(temp) > 0:
        return temp
    return None

    def primary_image(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.primary_image]
    else:
        temp = [obj.primary_image]
    if len(temp) > 0:
        return temp
    return None

    def price_tax(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.price_tax]
    else:
        temp = [obj.price_tax]
    if len(temp) > 0:
        return temp
    return None

    def price_discount(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.price_discount]
    else:
        temp = [obj.price_discount]
    if len(temp) > 0:
        return temp
    return None

    def product_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.product_object]
    else:
        temp = [obj.product_object]
    if len(temp) > 0:
        return temp
    return None

    def price_final(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.price_final]
    else:
        temp = [obj.price_final]
    if len(temp) > 0:
        return temp
    return None

    def cart_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.cart_object]
    else:
        temp = [obj.cart_object]
    if len(temp) > 0:
        return temp
    return None


class CustomerCoupon(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True
    add_fieldsets = []
    fieldsets = (('Profiling', {'classes': ('extrapretty',), 'fields': (('id', 'uuid', 'slug'),)}), ('Conditions', {'classes': 'extrapretty', 'fields': (('is_used',),)}), ('Time', {'classes': ('extrapretty',), 'fields': (('created_at', 'modified_at'),)}), ('Relations', {'classes': ('extrapretty', 'collapse'), 'fields': ('customer_id', 'coupon_id', 'ordercustomer')}), ('Properties', {'classes': ('extrapretty', 'collapse'), 'fields': ('customer_object', 'order_object_discount', 'coupon_type', 'coupon_object', 'order_object')}))
    filter_horizontal = []
    list_display = ['__str__', 'id', 'slug', 'is_used', 'created_at']
    list_display_links = ['__str__']
    list_editable = ['is_used']
    list_filter = ['is_used', 'customer_id', 'coupon_id', 'ordercustomer']
    list_max_show_all = 100
    list_per_page = 25
    list_select_related = True
    ordering = ['created_at']
    prepopulated_fields = {'slug': ('id',)}
    readonly_fields = ['slug', 'created_at', 'modified_at', 'ordercustomer', 'id', 'uuid', 'slug', 'customer_object', 'order_object_discount', 'coupon_type', 'coupon_object', 'order_object']
    search_help_text = ''

    def ordercustomer(self, obj):
        if  obj.ordercustomer.all().count() > 0:
            return obj.ordercustomer.all()
        return None
            
    def customer_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.customer_object]
    else:
        temp = [obj.customer_object]
    if len(temp) > 0:
        return temp
    return None

    def order_object_discount(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.order_object_discount]
    else:
        temp = [obj.order_object_discount]
    if len(temp) > 0:
        return temp
    return None

    def coupon_type(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.coupon_type]
    else:
        temp = [obj.coupon_type]
    if len(temp) > 0:
        return temp
    return None

    def coupon_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.coupon_object]
    else:
        temp = [obj.coupon_object]
    if len(temp) > 0:
        return temp
    return None

    def order_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.order_object]
    else:
        temp = [obj.order_object]
    if len(temp) > 0:
        return temp
    return None


class Coupon(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True
    add_fieldsets = []
    fieldsets = (('Profiling', {'classes': ('extrapretty',), 'fields': (('id', 'uuid', 'coupon_type'), ('minimum_amount', 'maximum_amount', 'percentage'), ('slug',))}), ('Extras', {'classes': ('extrapretty', 'collapse'), 'fields': (('code', 'name'),)}), ('Conditions', {'classes': 'extrapretty', 'fields': (('is_delete', 'is_tax_free', 'is_shipping_free'),)}), ('Time', {'classes': ('extrapretty',), 'fields': (('created_at', 'modified_at', 'deleted_on', 'date_from', 'date_to'),)}), ('Relations', {'classes': ('extrapretty', 'collapse'), 'fields': ('customers',)}), ('Properties', {'classes': ('extrapretty', 'collapse'), 'fields': ('order_objects', 'order_count', 'is_active_str', 'customer_count', 'order_discount', 'is_active', 'customer_objects')}))
    filter_horizontal = []
    list_display = ['__str__', 'id', 'name', 'slug', 'is_delete', 'is_tax_free', 'is_shipping_free', 'created_at']
    list_display_links = ['__str__']
    list_editable = ['name', 'is_delete', 'is_tax_free', 'is_shipping_free']
    list_filter = ['is_delete', 'is_tax_free', 'is_shipping_free', 'customers']
    list_max_show_all = 100
    list_per_page = 25
    list_select_related = True
    ordering = ['created_at']
    prepopulated_fields = {'slug': ('id',)}
    readonly_fields = ['slug', 'created_at', 'modified_at', 'deleted_on', 'date_from', 'date_to', 'customers', 'id', 'uuid', 'slug', 'order_objects', 'order_count', 'is_active_str', 'customer_count', 'order_discount', 'is_active', 'customer_objects']
    search_help_text = ''

    def customers(self, obj):
        if  obj.customers.all().count() > 0:
            return obj.customers.all()
        return None
            
    def order_objects(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.order_objects]
    else:
        temp = [obj.order_objects]
    if len(temp) > 0:
        return temp
    return None

    def order_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.order_count]
    else:
        temp = [obj.order_count]
    if len(temp) > 0:
        return temp
    return None

    def is_active_str(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.is_active_str]
    else:
        temp = [obj.is_active_str]
    if len(temp) > 0:
        return temp
    return None

    def customer_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.customer_count]
    else:
        temp = [obj.customer_count]
    if len(temp) > 0:
        return temp
    return None

    def order_discount(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.order_discount]
    else:
        temp = [obj.order_discount]
    if len(temp) > 0:
        return temp
    return None

    def is_active(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.is_active]
    else:
        temp = [obj.is_active]
    if len(temp) > 0:
        return temp
    return None

    def customer_objects(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.customer_objects]
    else:
        temp = [obj.customer_objects]
    if len(temp) > 0:
        return temp
    return None


class Favorite(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True
    add_fieldsets = []
    fieldsets = (('Profiling', {'classes': ('extrapretty',), 'fields': (('id', 'uuid', 'slug'),)}), ('Conditions', {'classes': 'extrapretty', 'fields': (('is_delete',),)}), ('Time', {'classes': ('extrapretty',), 'fields': (('created_at', 'modified_at', 'deleted_on'),)}), ('Relations', {'classes': ('extrapretty', 'collapse'), 'fields': ('customer', 'favorite_items')}), ('Properties', {'classes': ('extrapretty', 'collapse'), 'fields': ('customer_object', 'favorite_items_count', 'favorite_items_objects', 'favorite_items_products')}))
    filter_horizontal = []
    list_display = ['__str__', 'id', 'slug', 'is_delete', 'created_at']
    list_display_links = ['__str__']
    list_editable = ['is_delete']
    list_filter = ['is_delete', 'customer', 'favorite_items']
    list_max_show_all = 100
    list_per_page = 25
    list_select_related = True
    ordering = ['created_at']
    prepopulated_fields = {'slug': ('id',)}
    readonly_fields = ['slug', 'created_at', 'modified_at', 'deleted_on', 'customer', 'favorite_items', 'id', 'uuid', 'slug', 'customer_object', 'favorite_items_count', 'favorite_items_objects', 'favorite_items_products']
    search_help_text = ''

    def customer(self, obj):
        if  obj.customer.all().count() > 0:
            return obj.customer.all()
        return None
            
    def favorite_items(self, obj):
        if  obj.favorite_items.all().count() > 0:
            return obj.favorite_items.all()
        return None
            
    def customer_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.customer_object]
    else:
        temp = [obj.customer_object]
    if len(temp) > 0:
        return temp
    return None

    def favorite_items_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.favorite_items_count]
    else:
        temp = [obj.favorite_items_count]
    if len(temp) > 0:
        return temp
    return None

    def favorite_items_objects(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.favorite_items_objects]
    else:
        temp = [obj.favorite_items_objects]
    if len(temp) > 0:
        return temp
    return None

    def favorite_items_products(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.favorite_items_products]
    else:
        temp = [obj.favorite_items_products]
    if len(temp) > 0:
        return temp
    return None


class FavoriteItem(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True
    add_fieldsets = []
    fieldsets = (('Profiling', {'classes': ('extrapretty',), 'fields': (('id', 'uuid', 'slug'),)}), ('Conditions', {'classes': 'extrapretty', 'fields': (('is_delete',),)}), ('Time', {'classes': ('extrapretty',), 'fields': (('created_at', 'modified_at', 'deleted_on'),)}), ('Relations', {'classes': ('extrapretty', 'collapse'), 'fields': ('product', 'favorite')}), ('Properties', {'classes': ('extrapretty', 'collapse'), 'fields': ('customer_object', 'inventory_item_object', 'primary_image', 'favorite_object', 'product_object')}))
    filter_horizontal = []
    list_display = ['__str__', 'id', 'slug', 'is_delete', 'created_at']
    list_display_links = ['__str__']
    list_editable = ['is_delete']
    list_filter = ['is_delete', 'product', 'favorite']
    list_max_show_all = 100
    list_per_page = 25
    list_select_related = True
    ordering = ['created_at']
    prepopulated_fields = {'slug': ('id',)}
    readonly_fields = ['slug', 'created_at', 'modified_at', 'deleted_on', 'id', 'uuid', 'slug', 'customer_object', 'inventory_item_object', 'primary_image', 'favorite_object', 'product_object']
    search_help_text = ''

    def customer_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.customer_object]
    else:
        temp = [obj.customer_object]
    if len(temp) > 0:
        return temp
    return None

    def inventory_item_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.inventory_item_object]
    else:
        temp = [obj.inventory_item_object]
    if len(temp) > 0:
        return temp
    return None

    def primary_image(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.primary_image]
    else:
        temp = [obj.primary_image]
    if len(temp) > 0:
        return temp
    return None

    def favorite_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.favorite_object]
    else:
        temp = [obj.favorite_object]
    if len(temp) > 0:
        return temp
    return None

    def product_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.product_object]
    else:
        temp = [obj.product_object]
    if len(temp) > 0:
        return temp
    return None


class OrderCustomer(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True
    add_fieldsets = []
    fieldsets = (('Profiling', {'classes': ('extrapretty',), 'fields': (('id', 'uuid', 'status_order'), ('total_price', 'tax', 'discounted_price'), ('final_price', 'slug'))}), ('Extras', {'classes': ('extrapretty', 'collapse'), 'fields': (('coupon',),)}), ('Conditions', {'classes': 'extrapretty', 'fields': (('is_delete',),)}), ('Time', {'classes': ('extrapretty',), 'fields': (('created_at', 'modified_at', 'deleted_on'),)}), ('Relations', {'classes': ('extrapretty', 'collapse'), 'fields': ('customer', 'shipment', 'order_items')}), ('Properties', {'classes': ('extrapretty', 'collapse'), 'fields': ('coupon_discount', 'customer_object', 'shipment_price', 'is_paid', 'shipment_object', 'order_items_inventory_items', 'order_items_products', 'order_items_objects', 'coupon_object', 'order_object', 'order_items_count')}))
    filter_horizontal = []
    list_display = ['__str__', 'id', 'slug', 'coupon', 'is_delete', 'created_at']
    list_display_links = ['__str__']
    list_editable = ['coupon', 'is_delete']
    list_filter = ['is_delete', 'customer', 'shipment', 'order_items']
    list_max_show_all = 100
    list_per_page = 25
    list_select_related = True
    ordering = ['created_at']
    prepopulated_fields = {'slug': ('id',)}
    readonly_fields = ['slug', 'created_at', 'modified_at', 'deleted_on', 'order_items', 'id', 'uuid', 'slug', 'coupon_discount', 'customer_object', 'shipment_price', 'is_paid', 'shipment_object', 'order_items_inventory_items', 'order_items_products', 'order_items_objects', 'coupon_object', 'order_object', 'order_items_count']
    search_help_text = ''

    def order_items(self, obj):
        if  obj.order_items.all().count() > 0:
            return obj.order_items.all()
        return None
            
    def coupon_discount(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.coupon_discount]
    else:
        temp = [obj.coupon_discount]
    if len(temp) > 0:
        return temp
    return None

    def customer_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.customer_object]
    else:
        temp = [obj.customer_object]
    if len(temp) > 0:
        return temp
    return None

    def shipment_price(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.shipment_price]
    else:
        temp = [obj.shipment_price]
    if len(temp) > 0:
        return temp
    return None

    def is_paid(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.is_paid]
    else:
        temp = [obj.is_paid]
    if len(temp) > 0:
        return temp
    return None

    def shipment_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.shipment_object]
    else:
        temp = [obj.shipment_object]
    if len(temp) > 0:
        return temp
    return None

    def order_items_inventory_items(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.order_items_inventory_items]
    else:
        temp = [obj.order_items_inventory_items]
    if len(temp) > 0:
        return temp
    return None

    def order_items_products(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.order_items_products]
    else:
        temp = [obj.order_items_products]
    if len(temp) > 0:
        return temp
    return None

    def order_items_objects(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.order_items_objects]
    else:
        temp = [obj.order_items_objects]
    if len(temp) > 0:
        return temp
    return None

    def coupon_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.coupon_object]
    else:
        temp = [obj.coupon_object]
    if len(temp) > 0:
        return temp
    return None

    def order_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.order_object]
    else:
        temp = [obj.order_object]
    if len(temp) > 0:
        return temp
    return None

    def order_items_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.order_items_count]
    else:
        temp = [obj.order_items_count]
    if len(temp) > 0:
        return temp
    return None


class WishList(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True
    add_fieldsets = []
    fieldsets = (('Profiling', {'classes': ('extrapretty',), 'fields': (('id', 'uuid', 'slug'),)}), ('Conditions', {'classes': 'extrapretty', 'fields': (('is_delete',),)}), ('Time', {'classes': ('extrapretty',), 'fields': (('created_at', 'modified_at', 'deleted_on'),)}), ('Relations', {'classes': ('extrapretty', 'collapse'), 'fields': ('customer', 'wishlist_items')}), ('Properties', {'classes': ('extrapretty', 'collapse'), 'fields': ('customer_object', 'wishlist_items_count', 'wishlist_items_products', 'wishlist_items_objects')}))
    filter_horizontal = []
    list_display = ['__str__', 'id', 'slug', 'is_delete', 'created_at']
    list_display_links = ['__str__']
    list_editable = ['is_delete']
    list_filter = ['is_delete', 'customer', 'wishlist_items']
    list_max_show_all = 100
    list_per_page = 25
    list_select_related = True
    ordering = ['created_at']
    prepopulated_fields = {'slug': ('id',)}
    readonly_fields = ['slug', 'created_at', 'modified_at', 'deleted_on', 'customer', 'wishlist_items', 'id', 'uuid', 'slug', 'customer_object', 'wishlist_items_count', 'wishlist_items_products', 'wishlist_items_objects']
    search_help_text = ''

    def customer(self, obj):
        if  obj.customer.all().count() > 0:
            return obj.customer.all()
        return None
            
    def wishlist_items(self, obj):
        if  obj.wishlist_items.all().count() > 0:
            return obj.wishlist_items.all()
        return None
            
    def customer_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.customer_object]
    else:
        temp = [obj.customer_object]
    if len(temp) > 0:
        return temp
    return None

    def wishlist_items_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.wishlist_items_count]
    else:
        temp = [obj.wishlist_items_count]
    if len(temp) > 0:
        return temp
    return None

    def wishlist_items_products(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.wishlist_items_products]
    else:
        temp = [obj.wishlist_items_products]
    if len(temp) > 0:
        return temp
    return None

    def wishlist_items_objects(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.wishlist_items_objects]
    else:
        temp = [obj.wishlist_items_objects]
    if len(temp) > 0:
        return temp
    return None


class WishListItem(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True
    add_fieldsets = []
    fieldsets = (('Profiling', {'classes': ('extrapretty',), 'fields': (('id', 'uuid', 'slug'),)}), ('Conditions', {'classes': 'extrapretty', 'fields': (('is_delete',),)}), ('Time', {'classes': ('extrapretty',), 'fields': (('created_at', 'modified_at', 'deleted_on'),)}), ('Relations', {'classes': ('extrapretty', 'collapse'), 'fields': ('wish_list', 'product')}), ('Properties', {'classes': ('extrapretty', 'collapse'), 'fields': ('customer_object', 'inventory_item_object', 'primary_image', 'wishlist_object', 'product_object')}))
    filter_horizontal = []
    list_display = ['__str__', 'id', 'slug', 'is_delete', 'created_at']
    list_display_links = ['__str__']
    list_editable = ['is_delete']
    list_filter = ['is_delete', 'wish_list', 'product']
    list_max_show_all = 100
    list_per_page = 25
    list_select_related = True
    ordering = ['created_at']
    prepopulated_fields = {'slug': ('id',)}
    readonly_fields = ['slug', 'created_at', 'modified_at', 'deleted_on', 'id', 'uuid', 'slug', 'customer_object', 'inventory_item_object', 'primary_image', 'wishlist_object', 'product_object']
    search_help_text = ''

    def customer_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.customer_object]
    else:
        temp = [obj.customer_object]
    if len(temp) > 0:
        return temp
    return None

    def inventory_item_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.inventory_item_object]
    else:
        temp = [obj.inventory_item_object]
    if len(temp) > 0:
        return temp
    return None

    def primary_image(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.primary_image]
    else:
        temp = [obj.primary_image]
    if len(temp) > 0:
        return temp
    return None

    def wishlist_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.wishlist_object]
    else:
        temp = [obj.wishlist_object]
    if len(temp) > 0:
        return temp
    return None

    def product_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.product_object]
    else:
        temp = [obj.product_object]
    if len(temp) > 0:
        return temp
    return None

