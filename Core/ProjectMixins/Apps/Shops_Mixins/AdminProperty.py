from Core.admin import BaseAdminInlineRender, BaseAdminSlug, CustomInlineAdmin
from Core.ProjectMixins.Base.BaseInline import InlineMethods
from Markets.models import *
from Customers.models import *
from Shops.models import *
from Products.models import *
from Users.models import *

class Address(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True
    add_fieldsets = []
    fieldsets = (('Profiling', {'classes': ('extrapretty',), 'fields': (('id', 'uuid', 'slug'),)}), ('Extras', {'classes': ('extrapretty', 'collapse'), 'fields': (('address_line', 'city', 'content_type'), ('coordinate', 'country', 'firstname'), ('lastname', 'object_id', 'postal_code'), ('province',))}), ('Conditions', {'classes': 'extrapretty', 'fields': (('is_delete',),)}), ('Time', {'classes': ('extrapretty',), 'fields': (('created_at', 'modified_at', 'deleted_on'),)}), ('Properties', {'classes': ('extrapretty', 'collapse'), 'fields': ('full_name', 'owner_type', 'owner')}))
    filter_horizontal = []
    list_display = ['__str__', 'id', 'slug', 'is_delete', 'created_at']
    list_display_links = ['__str__']
    list_editable = ['is_delete']
    list_filter = ['is_delete']
    list_max_show_all = 100
    list_per_page = 25
    list_select_related = True
    ordering = ['created_at']
    prepopulated_fields = {'slug': ('id',)}
    readonly_fields = ['slug', 'created_at', 'modified_at', 'deleted_on', 'id', 'uuid', 'slug', 'full_name', 'owner_type', 'owner']
    search_help_text = ''

    def full_name(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.full_name]
    else:
        temp = [obj.full_name]
    if len(temp) > 0:
        return temp
    return None

    def owner_type(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.owner_type]
    else:
        temp = [obj.owner_type]
    if len(temp) > 0:
        return temp
    return None

    def owner(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.owner]
    else:
        temp = [obj.owner]
    if len(temp) > 0:
        return temp
    return None


class Discount(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True
    add_fieldsets = []
    fieldsets = (('Profiling', {'classes': ('extrapretty',), 'fields': (('id', 'uuid', 'discount_type'), ('minimum_amount', 'maximum_amount', 'percentage'), ('slug',))}), ('Conditions', {'classes': 'extrapretty', 'fields': (('is_delete',),)}), ('Time', {'classes': ('extrapretty',), 'fields': (('created_at', 'modified_at', 'deleted_on', 'date_from', 'date_to'),)}), ('Relations', {'classes': ('extrapretty', 'collapse'), 'fields': ('inventory_item',)}), ('Properties', {'classes': ('extrapretty', 'collapse'), 'fields': ('expired', 'discounted_price', 'market_object')}))
    filter_horizontal = []
    list_display = ['__str__', 'id', 'slug', 'is_delete', 'created_at']
    list_display_links = ['__str__']
    list_editable = ['is_delete']
    list_filter = ['is_delete', 'inventory_item']
    list_max_show_all = 100
    list_per_page = 25
    list_select_related = True
    ordering = ['created_at']
    prepopulated_fields = {'slug': ('id',)}
    readonly_fields = ['slug', 'created_at', 'modified_at', 'deleted_on', 'date_from', 'date_to', 'inventory_item', 'id', 'uuid', 'slug', 'expired', 'discounted_price', 'market_object']
    search_help_text = ''

    def inventory_item(self, obj):
        if  obj.inventory_item.all().count() > 0:
            return obj.inventory_item.all()
        return None
            
    def expired(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.expired]
    else:
        temp = [obj.expired]
    if len(temp) > 0:
        return temp
    return None

    def discounted_price(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.discounted_price]
    else:
        temp = [obj.discounted_price]
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


class Gallery(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True
    add_fieldsets = []
    fieldsets = (('Profiling', {'classes': ('extrapretty',), 'fields': (('id', 'uuid', 'slug'),)}), ('Extras', {'classes': ('extrapretty', 'collapse'), 'fields': (('content_type', 'object_id'),)}), ('Conditions', {'classes': 'extrapretty', 'fields': (('is_delete',),)}), ('Time', {'classes': ('extrapretty',), 'fields': (('created_at', 'modified_at', 'deleted_on'),)}), ('Relations', {'classes': ('extrapretty', 'collapse'), 'fields': ('images', 'gallery_images')}), ('Properties', {'classes': ('extrapretty', 'collapse'), 'fields': ('primary_image', 'owner_type', 'default_image', 'owner')}))
    filter_horizontal = []
    list_display = ['__str__', 'id', 'slug', 'is_delete', 'created_at']
    list_display_links = ['__str__']
    list_editable = ['is_delete']
    list_filter = ['is_delete', 'image', 'images', 'gallery_images']
    list_max_show_all = 100
    list_per_page = 25
    list_select_related = True
    ordering = ['created_at']
    prepopulated_fields = {'slug': ('id',)}
    readonly_fields = ['slug', 'created_at', 'modified_at', 'deleted_on', 'images', 'gallery_images', 'id', 'uuid', 'slug', 'primary_image', 'owner_type', 'default_image', 'owner']
    search_help_text = ''

    class ImageInlineAdmin(CustomInlineAdmin):
        model = Gallery.image.through
        image_inline = InlineMethods.open    

    inlines = (ImageInlineAdmin,)
    image_inline= inlines[0].image_inline,

    def images(self, obj):
        if  obj.images.all().count() > 0:
            return obj.images.all()
        return None
            
    def gallery_images(self, obj):
        if  obj.gallery_images.all().count() > 0:
            return obj.gallery_images.all()
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

    def owner_type(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.owner_type]
    else:
        temp = [obj.owner_type]
    if len(temp) > 0:
        return temp
    return None

    def default_image(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.default_image]
    else:
        temp = [obj.default_image]
    if len(temp) > 0:
        return temp
    return None

    def owner(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.owner]
    else:
        temp = [obj.owner]
    if len(temp) > 0:
        return temp
    return None


class Image(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True
    add_fieldsets = []
    fieldsets = (('Profiling', {'classes': ('extrapretty',), 'fields': (('id', 'uuid', 'image'), ('alt_text', 'slug'))}), ('Extras', {'classes': ('extrapretty', 'collapse'), 'fields': (('image_thumbnail', 'name', 'path_original'), ('path_thumbnail',))}), ('Conditions', {'classes': 'extrapretty', 'fields': (('is_delete',),)}), ('Time', {'classes': ('extrapretty',), 'fields': (('created_at', 'modified_at', 'deleted_on'),)}), ('Relations', {'classes': ('extrapretty', 'collapse'), 'fields': ('gallerys', 'gallery_images')}))
    filter_horizontal = []
    list_display = ['__str__', 'id', 'slug', 'is_delete', 'created_at']
    list_display_links = ['__str__']
    list_editable = ['is_delete']
    list_filter = ['is_delete', 'gallery', 'gallerys', 'gallery_images']
    list_max_show_all = 100
    list_per_page = 25
    list_select_related = True
    ordering = ['created_at']
    prepopulated_fields = {'slug': ('id',)}
    readonly_fields = ['slug', 'created_at', 'modified_at', 'deleted_on', 'gallerys', 'gallery_images', 'id', 'uuid', 'slug']
    search_help_text = ''

    class GalleryInlineAdmin(CustomInlineAdmin):
        model = Image.gallery.through
        gallery_inline = InlineMethods.open    

    inlines = (GalleryInlineAdmin,)
    gallery_inline= inlines[0].gallery_inline,

    def gallerys(self, obj):
        if  obj.gallerys.all().count() > 0:
            return obj.gallerys.all()
        return None
            
    def gallery_images(self, obj):
        if  obj.gallery_images.all().count() > 0:
            return obj.gallery_images.all()
        return None
            

class GalleryImage(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True
    add_fieldsets = []
    fieldsets = (('Profiling', {'classes': ('extrapretty',), 'fields': (('id', 'uuid', 'img_preview'),)}), ('Time', {'classes': ('extrapretty',), 'fields': (('created_at', 'modified_at'),)}), ('Relations', {'classes': ('extrapretty', 'collapse'), 'fields': ('gallery_id', 'image_id')}))
    filter_horizontal = []
    list_display = ['__str__', 'id', 'created_at']
    list_display_links = ['__str__']
    list_editable = []
    list_filter = ['gallery_id', 'image_id']
    list_max_show_all = 100
    list_per_page = 25
    list_select_related = True
    ordering = ['created_at']
    prepopulated_fields = {}
    readonly_fields = ['img_preview', 'created_at', 'modified_at', 'id', 'uuid', 'img_preview']
    search_help_text = ''


class Order(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True
    add_fieldsets = []
    fieldsets = (('Profiling', {'classes': ('extrapretty',), 'fields': (('id', 'uuid', 'status_order'), ('slug',))}), ('Conditions', {'classes': 'extrapretty', 'fields': (('is_delete',),)}), ('Time', {'classes': ('extrapretty',), 'fields': (('created_at', 'modified_at', 'deleted_on'),)}), ('Relations', {'classes': ('extrapretty', 'collapse'), 'fields': ('shipment', 'order_items')}), ('Properties', {'classes': ('extrapretty', 'collapse'), 'fields': ('order_market', 'order_customer')}))
    filter_horizontal = []
    list_display = ['__str__', 'id', 'slug', 'is_delete', 'created_at']
    list_display_links = ['__str__']
    list_editable = ['is_delete']
    list_filter = ['is_delete', 'shipment', 'order_items']
    list_max_show_all = 100
    list_per_page = 25
    list_select_related = True
    ordering = ['created_at']
    prepopulated_fields = {'slug': ('id',)}
    readonly_fields = ['slug', 'created_at', 'modified_at', 'deleted_on', 'order_items', 'id', 'uuid', 'slug', 'order_market', 'order_customer']
    search_help_text = ''

    def order_items(self, obj):
        if  obj.order_items.all().count() > 0:
            return obj.order_items.all()
        return None
            
    def order_market(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.order_market]
    else:
        temp = [obj.order_market]
    if len(temp) > 0:
        return temp
    return None

    def order_customer(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.order_customer]
    else:
        temp = [obj.order_customer]
    if len(temp) > 0:
        return temp
    return None


class OrderItem(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True
    add_fieldsets = []
    fieldsets = (('Profiling', {'classes': ('extrapretty',), 'fields': (('id', 'uuid', 'quantity'), ('final_price', 'discount_price', 'tax_price'), ('total_price', 'slug'))}), ('Time', {'classes': ('extrapretty',), 'fields': (('created_at', 'modified_at'),)}), ('Relations', {'classes': ('extrapretty', 'collapse'), 'fields': ('customer', 'order', 'order_customer', 'inventory_item', 'order_market', 'product')}), ('Properties', {'classes': ('extrapretty', 'collapse'), 'fields': ('customer_object', 'market_object', 'inventory_item_object', 'order_object', 'product_object')}))
    filter_horizontal = []
    list_display = ['__str__', 'id', 'slug', 'created_at']
    list_display_links = ['__str__']
    list_editable = []
    list_filter = ['customer', 'order', 'order_customer', 'inventory_item', 'order_market', 'product']
    list_max_show_all = 100
    list_per_page = 25
    list_select_related = True
    ordering = ['created_at']
    prepopulated_fields = {'slug': ('id',)}
    readonly_fields = ['slug', 'created_at', 'modified_at', 'id', 'uuid', 'slug', 'customer_object', 'market_object', 'inventory_item_object', 'order_object', 'product_object']
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

    def market_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.market_object]
    else:
        temp = [obj.market_object]
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

    def order_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.order_object]
    else:
        temp = [obj.order_object]
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


class Payment(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True
    add_fieldsets = []
    fieldsets = (('Profiling', {'classes': ('extrapretty',), 'fields': (('id', 'uuid', 'payment_type'), ('amount', 'status_payment', 'slug'))}), ('Extras', {'classes': ('extrapretty', 'collapse'), 'fields': (('content_type', 'description', 'object_id'),)}), ('Conditions', {'classes': 'extrapretty', 'fields': (('is_delete',),)}), ('Time', {'classes': ('extrapretty',), 'fields': (('created_at', 'modified_at', 'deleted_on'),)}), ('Properties', {'classes': ('extrapretty', 'collapse'), 'fields': ('order_type', 'order', 'is_paid')}))
    filter_horizontal = []
    list_display = ['__str__', 'id', 'slug', 'is_delete', 'created_at']
    list_display_links = ['__str__']
    list_editable = ['is_delete']
    list_filter = ['is_delete']
    list_max_show_all = 100
    list_per_page = 25
    list_select_related = True
    ordering = ['created_at']
    prepopulated_fields = {'slug': ('id',)}
    readonly_fields = ['slug', 'created_at', 'modified_at', 'deleted_on', 'id', 'uuid', 'slug', 'order_type', 'order', 'is_paid']
    search_help_text = ''

    def order_type(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.order_type]
    else:
        temp = [obj.order_type]
    if len(temp) > 0:
        return temp
    return None

    def order(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.order]
    else:
        temp = [obj.order]
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


class Wallet(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True
    add_fieldsets = []
    fieldsets = (('Profiling', {'classes': ('extrapretty',), 'fields': (('id', 'uuid', 'amount'), ('slug',))}), ('Extras', {'classes': ('extrapretty', 'collapse'), 'fields': (('card_number', 'content_type', 'firstname'), ('lastname', 'object_id', 'sheba'))}), ('Conditions', {'classes': 'extrapretty', 'fields': (('is_delete',),)}), ('Time', {'classes': ('extrapretty',), 'fields': (('created_at', 'modified_at', 'deleted_on'),)}), ('Properties', {'classes': ('extrapretty', 'collapse'), 'fields': ('owner_type', 'owner')}))
    filter_horizontal = []
    list_display = ['__str__', 'id', 'slug', 'is_delete', 'created_at']
    list_display_links = ['__str__']
    list_editable = ['is_delete']
    list_filter = ['is_delete']
    list_max_show_all = 100
    list_per_page = 25
    list_select_related = True
    ordering = ['created_at']
    prepopulated_fields = {'slug': ('id',)}
    readonly_fields = ['slug', 'created_at', 'modified_at', 'deleted_on', 'id', 'uuid', 'slug', 'owner_type', 'owner']
    search_help_text = ''

    def owner_type(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.owner_type]
    else:
        temp = [obj.owner_type]
    if len(temp) > 0:
        return temp
    return None

    def owner(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.owner]
    else:
        temp = [obj.owner]
    if len(temp) > 0:
        return temp
    return None


class Shipment(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True
    add_fieldsets = []
    fieldsets = (('Profiling', {'classes': ('extrapretty',), 'fields': (('id', 'uuid', 'address'), ('shipment_type', 'status_shipment', 'slug'), ('price',))}), ('Conditions', {'classes': 'extrapretty', 'fields': (('is_delete',),)}), ('Time', {'classes': ('extrapretty',), 'fields': (('created_at', 'modified_at', 'deleted_on'),)}), ('Relations', {'classes': ('extrapretty', 'collapse'), 'fields': ('order_customer', 'order_market', 'order')}), ('Properties', {'classes': ('extrapretty', 'collapse'), 'fields': ('order_customer_object', 'order_object', 'order_market_object')}))
    filter_horizontal = []
    list_display = ['__str__', 'id', 'slug', 'is_delete', 'created_at']
    list_display_links = ['__str__']
    list_editable = ['is_delete']
    list_filter = ['is_delete', 'order_customer', 'order_market', 'order']
    list_max_show_all = 100
    list_per_page = 25
    list_select_related = True
    ordering = ['created_at']
    prepopulated_fields = {'slug': ('id',)}
    readonly_fields = ['slug', 'created_at', 'modified_at', 'deleted_on', 'order_customer', 'order_market', 'order', 'id', 'uuid', 'slug', 'order_customer_object', 'order_object', 'order_market_object']
    search_help_text = ''

    def order_customer(self, obj):
        if  obj.order_customer.all().count() > 0:
            return obj.order_customer.all()
        return None
            
    def order_market(self, obj):
        if  obj.order_market.all().count() > 0:
            return obj.order_market.all()
        return None
            
    def order(self, obj):
        if  obj.order.all().count() > 0:
            return obj.order.all()
        return None
            
    def order_customer_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.order_customer_object]
    else:
        temp = [obj.order_customer_object]
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

    def order_market_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.order_market_object]
    else:
        temp = [obj.order_market_object]
    if len(temp) > 0:
        return temp
    return None


class ContactUs(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True
    add_fieldsets = []
    fieldsets = (('Profiling', {'classes': ('extrapretty',), 'fields': (('id', 'uuid', 'title'), ('body', 'slug'))}), ('Extras', {'classes': ('extrapretty', 'collapse'), 'fields': (('email', 'firstname', 'lastname'),)}), ('Conditions', {'classes': 'extrapretty', 'fields': (('is_delete',),)}), ('Time', {'classes': ('extrapretty',), 'fields': (('created_at', 'modified_at', 'deleted_on'),)}))
    filter_horizontal = []
    list_display = ['__str__', 'id', 'slug', 'is_delete', 'created_at']
    list_display_links = ['__str__']
    list_editable = ['is_delete']
    list_filter = ['is_delete']
    list_max_show_all = 100
    list_per_page = 25
    list_select_related = True
    ordering = ['created_at']
    prepopulated_fields = {'slug': ('id',)}
    readonly_fields = ['slug', 'created_at', 'modified_at', 'deleted_on', 'id', 'uuid', 'slug']
    search_help_text = ''

