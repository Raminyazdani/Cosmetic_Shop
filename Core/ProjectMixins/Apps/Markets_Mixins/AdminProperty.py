from Core.admin import BaseAdminInlineRender, BaseAdminSlug, CustomInlineAdmin
from Core.ProjectMixins.Base.BaseInline import InlineMethods
from Markets.models import *
from Customers.models import *
from Shops.models import *
from Products.models import *
from Users.models import *

class Market(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True
    add_fieldsets = []
    fieldsets = (('Profiling', {'classes': ('extrapretty',), 'fields': (('id', 'uuid', 'slug'), ('img_preview',))}), ('Extras', {'classes': ('extrapretty', 'collapse'), 'fields': (('bio', 'email', 'firstname'), ('lastname', 'user_name'))}), ('Conditions', {'classes': 'extrapretty', 'fields': (('is_delete',),)}), ('Time', {'classes': ('extrapretty',), 'fields': (('created_at', 'modified_at', 'deleted_on'),)}), ('Relations', {'classes': ('extrapretty', 'collapse'), 'fields': ('inventory', 'orders', 'user')}), ('Properties', {'classes': ('extrapretty', 'collapse'), 'fields': ('order_objects', 'user_object', 'sell_count', 'order_finished_amount', 'inventory_items', 'sell_amount', 'order_finished_count', 'order_pending_amount', 'order_pending_count', 'sell_products', 'images', 'order_pending_objects', 'inventory_object', 'inventory_items_count', 'order_finished_objects', 'order_items', 'order_finished_order_items', 'primary_image', 'order_pending_order_items', 'order_counts')}))
    filter_horizontal = []
    list_display = ['__str__', 'id', 'user_name', 'slug', 'inventory', 'is_delete', 'created_at']
    list_display_links = ['__str__', 'inventory']
    list_editable = ['user_name', 'is_delete']
    list_filter = ['is_delete', 'inventory', 'orders', 'user']
    list_max_show_all = 100
    list_per_page = 25
    list_select_related = True
    ordering = ['created_at']
    prepopulated_fields = {'slug': ('id',)}
    readonly_fields = ['slug', 'img_preview', 'created_at', 'modified_at', 'deleted_on', 'orders', 'user', 'id', 'uuid', 'slug', 'img_preview', 'inventory', 'order_objects', 'user_object', 'sell_count', 'order_finished_amount', 'inventory_items', 'sell_amount', 'order_finished_count', 'order_pending_amount', 'order_pending_count', 'sell_products', 'images', 'order_pending_objects', 'inventory_object', 'inventory_items_count', 'order_finished_objects', 'order_items', 'order_finished_order_items', 'primary_image', 'order_pending_order_items', 'order_counts']
    search_help_text = ''

    def orders(self, obj):
        if  obj.orders.all().count() > 0:
            return obj.orders.all()
        return None
            
    def user(self, obj):
        if  obj.user.all().count() > 0:
            return obj.user.all()
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

    def sell_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.sell_count]
    else:
        temp = [obj.sell_count]
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

    def inventory_items(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.inventory_items]
    else:
        temp = [obj.inventory_items]
    if len(temp) > 0:
        return temp
    return None

    def sell_amount(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.sell_amount]
    else:
        temp = [obj.sell_amount]
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

    def sell_products(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.sell_products]
    else:
        temp = [obj.sell_products]
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

    def order_pending_objects(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.order_pending_objects]
    else:
        temp = [obj.order_pending_objects]
    if len(temp) > 0:
        return temp
    return None

    def inventory_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.inventory_object]
    else:
        temp = [obj.inventory_object]
    if len(temp) > 0:
        return temp
    return None

    def inventory_items_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.inventory_items_count]
    else:
        temp = [obj.inventory_items_count]
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

    def order_items(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.order_items]
    else:
        temp = [obj.order_items]
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

    def primary_image(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.primary_image]
    else:
        temp = [obj.primary_image]
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

    def order_counts(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.order_counts]
    else:
        temp = [obj.order_counts]
    if len(temp) > 0:
        return temp
    return None


class Inventory(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True
    add_fieldsets = []
    fieldsets = (('Profiling', {'classes': ('extrapretty',), 'fields': (('id', 'uuid', 'slug'),)}), ('Extras', {'classes': ('extrapretty', 'collapse'), 'fields': (('weekdays',),)}), ('Conditions', {'classes': 'extrapretty', 'fields': (('is_delete',),)}), ('Time', {'classes': ('extrapretty',), 'fields': (('created_at', 'modified_at', 'deleted_on', 'date_open', 'date_close', 'time_open', 'time_close'),)}), ('Relations', {'classes': ('extrapretty', 'collapse'), 'fields': ('market', 'inventory_items')}), ('Properties', {'classes': ('extrapretty', 'collapse'), 'fields': ('inventory_items_objects', 'is_available', 'inventory_items_products', 'inventory_items_count')}))
    filter_horizontal = []
    list_display = ['__str__', 'id', 'slug', 'is_delete', 'created_at']
    list_display_links = ['__str__']
    list_editable = ['is_delete']
    list_filter = ['is_delete', 'market', 'inventory_items']
    list_max_show_all = 100
    list_per_page = 25
    list_select_related = True
    ordering = ['created_at']
    prepopulated_fields = {'slug': ('id',)}
    readonly_fields = ['slug', 'created_at', 'modified_at', 'deleted_on', 'date_open', 'date_close', 'time_open', 'time_close', 'market', 'inventory_items', 'id', 'uuid', 'slug', 'inventory_items_objects', 'is_available', 'inventory_items_products', 'inventory_items_count']
    search_help_text = ''

    def market(self, obj):
        if  obj.market.all().count() > 0:
            return obj.market.all()
        return None
            
    def inventory_items(self, obj):
        if  obj.inventory_items.all().count() > 0:
            return obj.inventory_items.all()
        return None
            
    def inventory_items_objects(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.inventory_items_objects]
    else:
        temp = [obj.inventory_items_objects]
    if len(temp) > 0:
        return temp
    return None

    def is_available(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.is_available]
    else:
        temp = [obj.is_available]
    if len(temp) > 0:
        return temp
    return None

    def inventory_items_products(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.inventory_items_products]
    else:
        temp = [obj.inventory_items_products]
    if len(temp) > 0:
        return temp
    return None

    def inventory_items_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.inventory_items_count]
    else:
        temp = [obj.inventory_items_count]
    if len(temp) > 0:
        return temp
    return None


class InventoryItem(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True
    add_fieldsets = []
    fieldsets = (('Profiling', {'classes': ('extrapretty',), 'fields': (('id', 'uuid', 'price'), ('tax_price', 'slug'))}), ('Extras', {'classes': ('extrapretty', 'collapse'), 'fields': (('weekdays',),)}), ('Conditions', {'classes': 'extrapretty', 'fields': (('is_delete',),)}), ('Time', {'classes': ('extrapretty',), 'fields': (('created_at', 'modified_at', 'deleted_on', 'date_from', 'date_to', 'time_from', 'time_to'),)}), ('Relations', {'classes': ('extrapretty', 'collapse'), 'fields': ('inventory', 'product', 'discount', 'cart_items', 'inventory_item_property_items', 'property_items', 'order_items')}), ('Properties', {'classes': ('extrapretty', 'collapse'), 'fields': ('discount_object', 'inventory_object', 'market_object', 'has_discount', 'is_on_sale', 'property_item_objects', 'final_price', 'is_available_quantity', 'is_available', 'product_object')}))
    filter_horizontal = []
    list_display = ['__str__', 'id', 'slug', 'discount', 'is_delete', 'created_at']
    list_display_links = ['__str__', 'discount']
    list_editable = ['is_delete']
    list_filter = ['is_delete', 'inventory', 'product', 'discount', 'property_item', 'cart_items', 'inventory_item_property_items', 'property_items', 'order_items']
    list_max_show_all = 100
    list_per_page = 25
    list_select_related = True
    ordering = ['created_at']
    prepopulated_fields = {'slug': ('id',)}
    readonly_fields = ['slug', 'created_at', 'modified_at', 'deleted_on', 'date_from', 'date_to', 'time_from', 'time_to', 'cart_items', 'inventory_item_property_items', 'property_items', 'order_items', 'id', 'uuid', 'slug', 'discount', 'discount_object', 'inventory_object', 'market_object', 'has_discount', 'is_on_sale', 'property_item_objects', 'final_price', 'is_available_quantity', 'is_available', 'product_object']
    search_help_text = ''

    class PropertyItemInlineAdmin(CustomInlineAdmin):
        model = InventoryItem.property_item.through
        property_item_inline = InlineMethods.open    

    inlines = (PropertyItemInlineAdmin,)
    property_item_inline= inlines[0].property_item_inline,

    def cart_items(self, obj):
        if  obj.cart_items.all().count() > 0:
            return obj.cart_items.all()
        return None
            
    def inventory_item_property_items(self, obj):
        if  obj.inventory_item_property_items.all().count() > 0:
            return obj.inventory_item_property_items.all()
        return None
            
    def property_items(self, obj):
        if  obj.property_items.all().count() > 0:
            return obj.property_items.all()
        return None
            
    def order_items(self, obj):
        if  obj.order_items.all().count() > 0:
            return obj.order_items.all()
        return None
            
    def discount_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.discount_object]
    else:
        temp = [obj.discount_object]
    if len(temp) > 0:
        return temp
    return None

    def inventory_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.inventory_object]
    else:
        temp = [obj.inventory_object]
    if len(temp) > 0:
        return temp
    return None

    def market_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.market_object]
    else:
        temp = [obj.market_object]
    if len(temp) > 0:
        return temp
    return None

    def has_discount(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.has_discount]
    else:
        temp = [obj.has_discount]
    if len(temp) > 0:
        return temp
    return None

    def is_on_sale(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.is_on_sale]
    else:
        temp = [obj.is_on_sale]
    if len(temp) > 0:
        return temp
    return None

    def property_item_objects(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.property_item_objects]
    else:
        temp = [obj.property_item_objects]
    if len(temp) > 0:
        return temp
    return None

    def final_price(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.final_price]
    else:
        temp = [obj.final_price]
    if len(temp) > 0:
        return temp
    return None

    def is_available_quantity(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.is_available_quantity]
    else:
        temp = [obj.is_available_quantity]
    if len(temp) > 0:
        return temp
    return None

    def is_available(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.is_available]
    else:
        temp = [obj.is_available]
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


class InventoryItemPropertyItem(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True
    add_fieldsets = []
    fieldsets = (('Profiling', {'classes': ('extrapretty',), 'fields': (('id', 'uuid'),)}), ('Time', {'classes': ('extrapretty',), 'fields': (('created_at', 'modified_at'),)}), ('Relations', {'classes': ('extrapretty', 'collapse'), 'fields': ('inventoryitem_id', 'propertyitem_id')}))
    filter_horizontal = []
    list_display = ['__str__', 'id', 'created_at']
    list_display_links = ['__str__']
    list_editable = []
    list_filter = ['inventoryitem_id', 'propertyitem_id']
    list_max_show_all = 100
    list_per_page = 25
    list_select_related = True
    ordering = ['created_at']
    prepopulated_fields = {}
    readonly_fields = ['created_at', 'modified_at', 'id', 'uuid']
    search_help_text = ''


class PropertyItem(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True
    add_fieldsets = []
    fieldsets = (('Profiling', {'classes': ('extrapretty',), 'fields': (('id', 'uuid', 'slug'),)}), ('Extras', {'classes': ('extrapretty', 'collapse'), 'fields': (('key', 'value'),)}), ('Conditions', {'classes': 'extrapretty', 'fields': (('is_delete',),)}), ('Time', {'classes': ('extrapretty',), 'fields': (('created_at', 'modified_at', 'deleted_on'),)}), ('Relations', {'classes': ('extrapretty', 'collapse'), 'fields': ('inventory_items', 'inventory_item_property_items')}), ('Properties', {'classes': ('extrapretty', 'collapse'), 'fields': ('inventory_item_objects', 'inventory_item_count')}))
    filter_horizontal = []
    list_display = ['__str__', 'id', 'slug', 'is_delete', 'created_at']
    list_display_links = ['__str__']
    list_editable = ['is_delete']
    list_filter = ['is_delete', 'inventory_item', 'inventory_items', 'inventory_item_property_items']
    list_max_show_all = 100
    list_per_page = 25
    list_select_related = True
    ordering = ['created_at']
    prepopulated_fields = {'slug': ('id',)}
    readonly_fields = ['slug', 'created_at', 'modified_at', 'deleted_on', 'inventory_items', 'inventory_item_property_items', 'id', 'uuid', 'slug', 'inventory_item_objects', 'inventory_item_count']
    search_help_text = ''

    class InventoryItemInlineAdmin(CustomInlineAdmin):
        model = PropertyItem.inventory_item.through
        inventory_item_inline = InlineMethods.open    

    inlines = (InventoryItemInlineAdmin,)
    inventory_item_inline= inlines[0].inventory_item_inline,

    def inventory_items(self, obj):
        if  obj.inventory_items.all().count() > 0:
            return obj.inventory_items.all()
        return None
            
    def inventory_item_property_items(self, obj):
        if  obj.inventory_item_property_items.all().count() > 0:
            return obj.inventory_item_property_items.all()
        return None
            
    def inventory_item_objects(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.inventory_item_objects]
    else:
        temp = [obj.inventory_item_objects]
    if len(temp) > 0:
        return temp
    return None

    def inventory_item_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.inventory_item_count]
    else:
        temp = [obj.inventory_item_count]
    if len(temp) > 0:
        return temp
    return None


class OrderMarket(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True
    add_fieldsets = []
    fieldsets = (('Profiling', {'classes': ('extrapretty',), 'fields': (('id', 'uuid', 'status_order'), ('total_price', 'status_payment', 'slug'))}), ('Conditions', {'classes': 'extrapretty', 'fields': (('is_delete',),)}), ('Time', {'classes': ('extrapretty',), 'fields': (('created_at', 'modified_at', 'deleted_on'),)}), ('Relations', {'classes': ('extrapretty', 'collapse'), 'fields': ('shipment', 'market', 'order_items')}), ('Properties', {'classes': ('extrapretty', 'collapse'), 'fields': ('order_objects', 'shipment_price', 'market_object', 'order_item_objects', 'shipment_object', 'order_items_products', 'is_cancel', 'is_finished', 'is_pending', 'order_item_count', 'order_items_inventory_items')}))
    filter_horizontal = []
    list_display = ['__str__', 'id', 'slug', 'is_delete', 'created_at']
    list_display_links = ['__str__']
    list_editable = ['is_delete']
    list_filter = ['is_delete', 'shipment', 'market', 'order_items']
    list_max_show_all = 100
    list_per_page = 25
    list_select_related = True
    ordering = ['created_at']
    prepopulated_fields = {'slug': ('id',)}
    readonly_fields = ['slug', 'created_at', 'modified_at', 'deleted_on', 'order_items', 'id', 'uuid', 'slug', 'order_objects', 'shipment_price', 'market_object', 'order_item_objects', 'shipment_object', 'order_items_products', 'is_cancel', 'is_finished', 'is_pending', 'order_item_count', 'order_items_inventory_items']
    search_help_text = ''

    def order_items(self, obj):
        if  obj.order_items.all().count() > 0:
            return obj.order_items.all()
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

    def shipment_price(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.shipment_price]
    else:
        temp = [obj.shipment_price]
    if len(temp) > 0:
        return temp
    return None

    def market_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.market_object]
    else:
        temp = [obj.market_object]
    if len(temp) > 0:
        return temp
    return None

    def order_item_objects(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.order_item_objects]
    else:
        temp = [obj.order_item_objects]
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

    def order_items_products(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.order_items_products]
    else:
        temp = [obj.order_items_products]
    if len(temp) > 0:
        return temp
    return None

    def is_cancel(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.is_cancel]
    else:
        temp = [obj.is_cancel]
    if len(temp) > 0:
        return temp
    return None

    def is_finished(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.is_finished]
    else:
        temp = [obj.is_finished]
    if len(temp) > 0:
        return temp
    return None

    def is_pending(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.is_pending]
    else:
        temp = [obj.is_pending]
    if len(temp) > 0:
        return temp
    return None

    def order_item_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.order_item_count]
    else:
        temp = [obj.order_item_count]
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

