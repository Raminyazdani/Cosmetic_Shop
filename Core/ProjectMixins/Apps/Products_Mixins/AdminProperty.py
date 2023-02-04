from Core.admin import BaseAdminInlineRender, BaseAdminSlug, CustomInlineAdmin
from Core.ProjectMixins.Base.BaseInline import InlineMethods
from Markets.models import *
from Customers.models import *
from Shops.models import *
from Products.models import *
from Users.models import *

class Product(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True
    add_fieldsets = []
    fieldsets = (('Profiling', {'classes': ('extrapretty',), 'fields': (('id', 'uuid', 'name'), ('slug', 'short_description', 'gender'), ('img_preview',))}), ('Extras', {'classes': ('extrapretty', 'collapse'), 'fields': (('description',),)}), ('Conditions', {'classes': 'extrapretty', 'fields': (('is_delete', 'is_available'),)}), ('Time', {'classes': ('extrapretty',), 'fields': (('created_at', 'modified_at', 'deleted_on'),)}), ('Relations', {'classes': ('extrapretty', 'collapse'), 'fields': ('favorite_items', 'wishlist_items', 'inventory_items', 'categorys', 'brands', 'tags', 'comments', 'product_tags', 'product_categorys', 'product_brands', 'order_items')}), ('Properties', {'classes': ('extrapretty', 'collapse'), 'fields': ('seller_count', 'wishlist_count', 'sell_count', 'best_offer', 'category_count', 'sell_amount', 'inventory_item_has_discount', 'website_best_offer', 'category_object', 'inventory_item_average_price', 'tag_count', 'brand_name', 'brand_object', 'rating', 'order_items_object', 'brand_count', 'comment_count', 'images', 'tag_name', 'inventory_item_max_object', 'inventory_item_price', 'inventory_item_min_object', 'website_product_list', 'inventory_item_object', 'no_quantity', 'inventory_item_count', 'all_offers', 'inventory_item_market', 'tag_object', 'primary_image', 'inventory_item_min_price', 'market_objects', 'inventory_item_max_price', 'available_website', 'favorite_count', 'comment_object', 'category_name')}))
    filter_horizontal = []
    list_display = ['__str__', 'id', 'name', 'slug', 'is_delete', 'is_available', 'created_at']
    list_display_links = ['__str__']
    list_editable = ['name', 'is_delete', 'is_available']
    list_filter = ['is_delete', 'is_available', 'category', 'tag', 'brand', 'favorite_items', 'wishlist_items', 'inventory_items', 'categorys', 'brands', 'tags', 'comments', 'product_tags', 'product_categorys', 'product_brands', 'order_items']
    list_max_show_all = 100
    list_per_page = 25
    list_select_related = True
    ordering = ['created_at']
    prepopulated_fields = {'slug': ('id',)}
    readonly_fields = ['slug', 'img_preview', 'created_at', 'modified_at', 'deleted_on', 'favorite_items', 'wishlist_items', 'inventory_items', 'categorys', 'brands', 'tags', 'comments', 'product_tags', 'product_categorys', 'product_brands', 'order_items', 'id', 'uuid', 'slug', 'img_preview', 'seller_count', 'wishlist_count', 'sell_count', 'best_offer', 'category_count', 'sell_amount', 'inventory_item_has_discount', 'website_best_offer', 'category_object', 'inventory_item_average_price', 'tag_count', 'brand_name', 'brand_object', 'rating', 'order_items_object', 'brand_count', 'comment_count', 'images', 'tag_name', 'inventory_item_max_object', 'inventory_item_price', 'inventory_item_min_object', 'website_product_list', 'inventory_item_object', 'no_quantity', 'inventory_item_count', 'all_offers', 'inventory_item_market', 'tag_object', 'primary_image', 'inventory_item_min_price', 'market_objects', 'inventory_item_max_price', 'available_website', 'favorite_count', 'comment_object', 'category_name']
    search_help_text = ''

    class CategoryInlineAdmin(CustomInlineAdmin):
        model = Product.category.through
        category_inline = InlineMethods.open    

    class TagInlineAdmin(CustomInlineAdmin):
        model = Product.tag.through
        tag_inline = InlineMethods.open    

    class BrandInlineAdmin(CustomInlineAdmin):
        model = Product.brand.through
        brand_inline = InlineMethods.open    

    inlines = (CategoryInlineAdmin,TagInlineAdmin,BrandInlineAdmin,)
    category_inline,tag_inline,brand_inline= inlines[0].category_inline,inlines[1].tag_inline,inlines[2].brand_inline,

    def favorite_items(self, obj):
        if  obj.favorite_items.all().count() > 0:
            return obj.favorite_items.all()
        return None
            
    def wishlist_items(self, obj):
        if  obj.wishlist_items.all().count() > 0:
            return obj.wishlist_items.all()
        return None
            
    def inventory_items(self, obj):
        if  obj.inventory_items.all().count() > 0:
            return obj.inventory_items.all()
        return None
            
    def categorys(self, obj):
        if  obj.categorys.all().count() > 0:
            return obj.categorys.all()
        return None
            
    def brands(self, obj):
        if  obj.brands.all().count() > 0:
            return obj.brands.all()
        return None
            
    def tags(self, obj):
        if  obj.tags.all().count() > 0:
            return obj.tags.all()
        return None
            
    def comments(self, obj):
        if  obj.comments.all().count() > 0:
            return obj.comments.all()
        return None
            
    def product_tags(self, obj):
        if  obj.product_tags.all().count() > 0:
            return obj.product_tags.all()
        return None
            
    def product_categorys(self, obj):
        if  obj.product_categorys.all().count() > 0:
            return obj.product_categorys.all()
        return None
            
    def product_brands(self, obj):
        if  obj.product_brands.all().count() > 0:
            return obj.product_brands.all()
        return None
            
    def order_items(self, obj):
        if  obj.order_items.all().count() > 0:
            return obj.order_items.all()
        return None
            
    def seller_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.seller_count]
    else:
        temp = [obj.seller_count]
    if len(temp) > 0:
        return temp
    return None

    def wishlist_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.wishlist_count]
    else:
        temp = [obj.wishlist_count]
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

    def best_offer(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.best_offer]
    else:
        temp = [obj.best_offer]
    if len(temp) > 0:
        return temp
    return None

    def category_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.category_count]
    else:
        temp = [obj.category_count]
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

    def inventory_item_has_discount(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.inventory_item_has_discount]
    else:
        temp = [obj.inventory_item_has_discount]
    if len(temp) > 0:
        return temp
    return None

    def website_best_offer(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.website_best_offer]
    else:
        temp = [obj.website_best_offer]
    if len(temp) > 0:
        return temp
    return None

    def category_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.category_object]
    else:
        temp = [obj.category_object]
    if len(temp) > 0:
        return temp
    return None

    def inventory_item_average_price(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.inventory_item_average_price]
    else:
        temp = [obj.inventory_item_average_price]
    if len(temp) > 0:
        return temp
    return None

    def tag_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.tag_count]
    else:
        temp = [obj.tag_count]
    if len(temp) > 0:
        return temp
    return None

    def brand_name(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.brand_name]
    else:
        temp = [obj.brand_name]
    if len(temp) > 0:
        return temp
    return None

    def brand_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.brand_object]
    else:
        temp = [obj.brand_object]
    if len(temp) > 0:
        return temp
    return None

    def rating(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.rating]
    else:
        temp = [obj.rating]
    if len(temp) > 0:
        return temp
    return None

    def order_items_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.order_items_object]
    else:
        temp = [obj.order_items_object]
    if len(temp) > 0:
        return temp
    return None

    def brand_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.brand_count]
    else:
        temp = [obj.brand_count]
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

    def images(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.images]
    else:
        temp = [obj.images]
    if len(temp) > 0:
        return temp
    return None

    def tag_name(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.tag_name]
    else:
        temp = [obj.tag_name]
    if len(temp) > 0:
        return temp
    return None

    def inventory_item_max_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.inventory_item_max_object]
    else:
        temp = [obj.inventory_item_max_object]
    if len(temp) > 0:
        return temp
    return None

    def inventory_item_price(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.inventory_item_price]
    else:
        temp = [obj.inventory_item_price]
    if len(temp) > 0:
        return temp
    return None

    def inventory_item_min_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.inventory_item_min_object]
    else:
        temp = [obj.inventory_item_min_object]
    if len(temp) > 0:
        return temp
    return None

    def website_product_list(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.website_product_list]
    else:
        temp = [obj.website_product_list]
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

    def no_quantity(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.no_quantity]
    else:
        temp = [obj.no_quantity]
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

    def all_offers(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.all_offers]
    else:
        temp = [obj.all_offers]
    if len(temp) > 0:
        return temp
    return None

    def inventory_item_market(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.inventory_item_market]
    else:
        temp = [obj.inventory_item_market]
    if len(temp) > 0:
        return temp
    return None

    def tag_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.tag_object]
    else:
        temp = [obj.tag_object]
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

    def inventory_item_min_price(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.inventory_item_min_price]
    else:
        temp = [obj.inventory_item_min_price]
    if len(temp) > 0:
        return temp
    return None

    def market_objects(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.market_objects]
    else:
        temp = [obj.market_objects]
    if len(temp) > 0:
        return temp
    return None

    def inventory_item_max_price(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.inventory_item_max_price]
    else:
        temp = [obj.inventory_item_max_price]
    if len(temp) > 0:
        return temp
    return None

    def available_website(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.available_website]
    else:
        temp = [obj.available_website]
    if len(temp) > 0:
        return temp
    return None

    def favorite_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.favorite_count]
    else:
        temp = [obj.favorite_count]
    if len(temp) > 0:
        return temp
    return None

    def comment_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.comment_object]
    else:
        temp = [obj.comment_object]
    if len(temp) > 0:
        return temp
    return None

    def category_name(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.category_name]
    else:
        temp = [obj.category_name]
    if len(temp) > 0:
        return temp
    return None


class Category(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True
    add_fieldsets = []
    fieldsets = (('Profiling', {'classes': ('extrapretty',), 'fields': (('id', 'uuid', 'name'), ('slug', 'img_preview', 'parent_slug'))}), ('Extras', {'classes': ('extrapretty', 'collapse'), 'fields': (('description',),)}), ('Conditions', {'classes': 'extrapretty', 'fields': (('is_delete',),)}), ('Time', {'classes': ('extrapretty',), 'fields': (('created_at', 'modified_at', 'deleted_on'),)}), ('Relations', {'classes': ('extrapretty', 'collapse'), 'fields': ('parent', 'products', 'childs', 'product_categorys')}), ('Properties', {'classes': ('extrapretty', 'collapse'), 'fields': ('wishlist_count', 'product_name', 'sell_count', 'order_item_object', 'sell_amount', 'tag_count', 'brand_name', 'brand_object', 'rating', 'brand_count', 'comment_count', 'images', 'tag_name', 'parent_count', 'inventory_item_object', 'inventory_item_count', 'product_object', 'product_count', 'child_count', 'inventory_item_market', 'tag_object', 'parent_object', 'child_object', 'primary_image', 'parent_name', 'favorite_count', 'comment_object', 'child_name')}))
    filter_horizontal = []
    list_display = ['__str__', 'id', 'name', 'slug', 'is_delete', 'created_at']
    list_display_links = ['__str__']
    list_editable = ['name', 'is_delete']
    list_filter = ['is_delete', 'parent', 'product', 'products', 'childs', 'product_categorys']
    list_max_show_all = 100
    list_per_page = 25
    list_select_related = True
    ordering = ['created_at']
    prepopulated_fields = {'slug': ('id',)}
    readonly_fields = ['slug', 'img_preview', 'parent_slug', 'created_at', 'modified_at', 'deleted_on', 'products', 'childs', 'product_categorys', 'id', 'uuid', 'slug', 'img_preview', 'wishlist_count', 'product_name', 'sell_count', 'order_item_object', 'sell_amount', 'tag_count', 'brand_name', 'brand_object', 'rating', 'brand_count', 'comment_count', 'images', 'tag_name', 'parent_count', 'inventory_item_object', 'inventory_item_count', 'product_object', 'product_count', 'child_count', 'inventory_item_market', 'tag_object', 'parent_object', 'child_object', 'primary_image', 'parent_name', 'favorite_count', 'comment_object', 'child_name']
    search_help_text = ''

    class ProductInlineAdmin(CustomInlineAdmin):
        model = Category.product.through
        product_inline = InlineMethods.open    

    inlines = (ProductInlineAdmin,)
    product_inline= inlines[0].product_inline,

    def products(self, obj):
        if  obj.products.all().count() > 0:
            return obj.products.all()
        return None
            
    def childs(self, obj):
        if  obj.childs.all().count() > 0:
            return obj.childs.all()
        return None
            
    def product_categorys(self, obj):
        if  obj.product_categorys.all().count() > 0:
            return obj.product_categorys.all()
        return None
            
    def wishlist_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.wishlist_count]
    else:
        temp = [obj.wishlist_count]
    if len(temp) > 0:
        return temp
    return None

    def product_name(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.product_name]
    else:
        temp = [obj.product_name]
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

    def order_item_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.order_item_object]
    else:
        temp = [obj.order_item_object]
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

    def tag_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.tag_count]
    else:
        temp = [obj.tag_count]
    if len(temp) > 0:
        return temp
    return None

    def brand_name(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.brand_name]
    else:
        temp = [obj.brand_name]
    if len(temp) > 0:
        return temp
    return None

    def brand_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.brand_object]
    else:
        temp = [obj.brand_object]
    if len(temp) > 0:
        return temp
    return None

    def rating(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.rating]
    else:
        temp = [obj.rating]
    if len(temp) > 0:
        return temp
    return None

    def brand_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.brand_count]
    else:
        temp = [obj.brand_count]
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

    def images(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.images]
    else:
        temp = [obj.images]
    if len(temp) > 0:
        return temp
    return None

    def tag_name(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.tag_name]
    else:
        temp = [obj.tag_name]
    if len(temp) > 0:
        return temp
    return None

    def parent_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.parent_count]
    else:
        temp = [obj.parent_count]
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

    def inventory_item_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.inventory_item_count]
    else:
        temp = [obj.inventory_item_count]
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

    def product_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.product_count]
    else:
        temp = [obj.product_count]
    if len(temp) > 0:
        return temp
    return None

    def child_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.child_count]
    else:
        temp = [obj.child_count]
    if len(temp) > 0:
        return temp
    return None

    def inventory_item_market(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.inventory_item_market]
    else:
        temp = [obj.inventory_item_market]
    if len(temp) > 0:
        return temp
    return None

    def tag_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.tag_object]
    else:
        temp = [obj.tag_object]
    if len(temp) > 0:
        return temp
    return None

    def parent_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.parent_object]
    else:
        temp = [obj.parent_object]
    if len(temp) > 0:
        return temp
    return None

    def child_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.child_object]
    else:
        temp = [obj.child_object]
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

    def parent_name(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.parent_name]
    else:
        temp = [obj.parent_name]
    if len(temp) > 0:
        return temp
    return None

    def favorite_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.favorite_count]
    else:
        temp = [obj.favorite_count]
    if len(temp) > 0:
        return temp
    return None

    def comment_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.comment_object]
    else:
        temp = [obj.comment_object]
    if len(temp) > 0:
        return temp
    return None

    def child_name(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.child_name]
    else:
        temp = [obj.child_name]
    if len(temp) > 0:
        return temp
    return None


class Brand(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True
    add_fieldsets = []
    fieldsets = (('Profiling', {'classes': ('extrapretty',), 'fields': (('id', 'uuid', 'name'), ('slug', 'img_preview'))}), ('Extras', {'classes': ('extrapretty', 'collapse'), 'fields': (('description',),)}), ('Conditions', {'classes': 'extrapretty', 'fields': (('is_delete', 'is_available'),)}), ('Time', {'classes': ('extrapretty',), 'fields': (('created_at', 'modified_at', 'deleted_on'),)}), ('Relations', {'classes': ('extrapretty', 'collapse'), 'fields': ('products', 'product_brands')}), ('Properties', {'classes': ('extrapretty', 'collapse'), 'fields': ('wishlist_count', 'product_name', 'sell_count', 'category_count', 'order_item_object', 'sell_amount', 'category_object', 'tag_count', 'rating', 'comment_count', 'images', 'tag_name', 'inventory_item_object', 'inventory_item_count', 'product_object', 'product_count', 'inventory_item_market', 'tag_object', 'primary_image', 'favorite_count', 'comment_object', 'category_name')}))
    filter_horizontal = []
    list_display = ['__str__', 'id', 'name', 'slug', 'is_delete', 'is_available', 'created_at']
    list_display_links = ['__str__']
    list_editable = ['name', 'is_delete', 'is_available']
    list_filter = ['is_delete', 'is_available', 'product', 'products', 'product_brands']
    list_max_show_all = 100
    list_per_page = 25
    list_select_related = True
    ordering = ['created_at']
    prepopulated_fields = {'slug': ('id',)}
    readonly_fields = ['slug', 'img_preview', 'created_at', 'modified_at', 'deleted_on', 'products', 'product_brands', 'id', 'uuid', 'slug', 'img_preview', 'wishlist_count', 'product_name', 'sell_count', 'category_count', 'order_item_object', 'sell_amount', 'category_object', 'tag_count', 'rating', 'comment_count', 'images', 'tag_name', 'inventory_item_object', 'inventory_item_count', 'product_object', 'product_count', 'inventory_item_market', 'tag_object', 'primary_image', 'favorite_count', 'comment_object', 'category_name']
    search_help_text = ''

    class ProductInlineAdmin(CustomInlineAdmin):
        model = Brand.product.through
        product_inline = InlineMethods.open    

    inlines = (ProductInlineAdmin,)
    product_inline= inlines[0].product_inline,

    def products(self, obj):
        if  obj.products.all().count() > 0:
            return obj.products.all()
        return None
            
    def product_brands(self, obj):
        if  obj.product_brands.all().count() > 0:
            return obj.product_brands.all()
        return None
            
    def wishlist_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.wishlist_count]
    else:
        temp = [obj.wishlist_count]
    if len(temp) > 0:
        return temp
    return None

    def product_name(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.product_name]
    else:
        temp = [obj.product_name]
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

    def category_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.category_count]
    else:
        temp = [obj.category_count]
    if len(temp) > 0:
        return temp
    return None

    def order_item_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.order_item_object]
    else:
        temp = [obj.order_item_object]
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

    def category_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.category_object]
    else:
        temp = [obj.category_object]
    if len(temp) > 0:
        return temp
    return None

    def tag_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.tag_count]
    else:
        temp = [obj.tag_count]
    if len(temp) > 0:
        return temp
    return None

    def rating(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.rating]
    else:
        temp = [obj.rating]
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

    def images(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.images]
    else:
        temp = [obj.images]
    if len(temp) > 0:
        return temp
    return None

    def tag_name(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.tag_name]
    else:
        temp = [obj.tag_name]
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

    def inventory_item_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.inventory_item_count]
    else:
        temp = [obj.inventory_item_count]
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

    def product_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.product_count]
    else:
        temp = [obj.product_count]
    if len(temp) > 0:
        return temp
    return None

    def inventory_item_market(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.inventory_item_market]
    else:
        temp = [obj.inventory_item_market]
    if len(temp) > 0:
        return temp
    return None

    def tag_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.tag_object]
    else:
        temp = [obj.tag_object]
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

    def favorite_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.favorite_count]
    else:
        temp = [obj.favorite_count]
    if len(temp) > 0:
        return temp
    return None

    def comment_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.comment_object]
    else:
        temp = [obj.comment_object]
    if len(temp) > 0:
        return temp
    return None

    def category_name(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.category_name]
    else:
        temp = [obj.category_name]
    if len(temp) > 0:
        return temp
    return None


class Tag(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True
    add_fieldsets = []
    fieldsets = (('Profiling', {'classes': ('extrapretty',), 'fields': (('id', 'uuid', 'name'), ('slug', 'img_preview'))}), ('Conditions', {'classes': 'extrapretty', 'fields': (('is_delete',),)}), ('Time', {'classes': ('extrapretty',), 'fields': (('created_at', 'modified_at', 'deleted_on'),)}), ('Relations', {'classes': ('extrapretty', 'collapse'), 'fields': ('products', 'product_tags')}), ('Properties', {'classes': ('extrapretty', 'collapse'), 'fields': ('wishlist_count', 'product_name', 'sell_count', 'category_count', 'order_item_object', 'sell_amount', 'category_object', 'brand_name', 'brand_object', 'rating', 'brand_count', 'comment_count', 'images', 'inventory_item_object', 'inventory_item_count', 'product_object', 'product_count', 'inventory_item_market', 'primary_image', 'favorite_count', 'comment_object', 'category_name')}))
    filter_horizontal = []
    list_display = ['__str__', 'id', 'name', 'slug', 'is_delete', 'created_at']
    list_display_links = ['__str__']
    list_editable = ['name', 'is_delete']
    list_filter = ['is_delete', 'product', 'products', 'product_tags']
    list_max_show_all = 100
    list_per_page = 25
    list_select_related = True
    ordering = ['created_at']
    prepopulated_fields = {'slug': ('id',)}
    readonly_fields = ['slug', 'img_preview', 'created_at', 'modified_at', 'deleted_on', 'products', 'product_tags', 'id', 'uuid', 'slug', 'img_preview', 'wishlist_count', 'product_name', 'sell_count', 'category_count', 'order_item_object', 'sell_amount', 'category_object', 'brand_name', 'brand_object', 'rating', 'brand_count', 'comment_count', 'images', 'inventory_item_object', 'inventory_item_count', 'product_object', 'product_count', 'inventory_item_market', 'primary_image', 'favorite_count', 'comment_object', 'category_name']
    search_help_text = ''

    class ProductInlineAdmin(CustomInlineAdmin):
        model = Tag.product.through
        product_inline = InlineMethods.open    

    inlines = (ProductInlineAdmin,)
    product_inline= inlines[0].product_inline,

    def products(self, obj):
        if  obj.products.all().count() > 0:
            return obj.products.all()
        return None
            
    def product_tags(self, obj):
        if  obj.product_tags.all().count() > 0:
            return obj.product_tags.all()
        return None
            
    def wishlist_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.wishlist_count]
    else:
        temp = [obj.wishlist_count]
    if len(temp) > 0:
        return temp
    return None

    def product_name(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.product_name]
    else:
        temp = [obj.product_name]
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

    def category_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.category_count]
    else:
        temp = [obj.category_count]
    if len(temp) > 0:
        return temp
    return None

    def order_item_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.order_item_object]
    else:
        temp = [obj.order_item_object]
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

    def category_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.category_object]
    else:
        temp = [obj.category_object]
    if len(temp) > 0:
        return temp
    return None

    def brand_name(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.brand_name]
    else:
        temp = [obj.brand_name]
    if len(temp) > 0:
        return temp
    return None

    def brand_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.brand_object]
    else:
        temp = [obj.brand_object]
    if len(temp) > 0:
        return temp
    return None

    def rating(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.rating]
    else:
        temp = [obj.rating]
    if len(temp) > 0:
        return temp
    return None

    def brand_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.brand_count]
    else:
        temp = [obj.brand_count]
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

    def images(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.images]
    else:
        temp = [obj.images]
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

    def inventory_item_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.inventory_item_count]
    else:
        temp = [obj.inventory_item_count]
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

    def product_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.product_count]
    else:
        temp = [obj.product_count]
    if len(temp) > 0:
        return temp
    return None

    def inventory_item_market(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.inventory_item_market]
    else:
        temp = [obj.inventory_item_market]
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

    def favorite_count(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.favorite_count]
    else:
        temp = [obj.favorite_count]
    if len(temp) > 0:
        return temp
    return None

    def comment_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.comment_object]
    else:
        temp = [obj.comment_object]
    if len(temp) > 0:
        return temp
    return None

    def category_name(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.category_name]
    else:
        temp = [obj.category_name]
    if len(temp) > 0:
        return temp
    return None


class Comment(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True
    add_fieldsets = []
    fieldsets = (('Profiling', {'classes': ('extrapretty',), 'fields': (('id', 'uuid', 'title'), ('body', 'rating', 'slug'), ('img_preview',))}), ('Conditions', {'classes': 'extrapretty', 'fields': (('is_delete',),)}), ('Time', {'classes': ('extrapretty',), 'fields': (('created_at', 'modified_at', 'deleted_on'),)}), ('Relations', {'classes': ('extrapretty', 'collapse'), 'fields': ('author', 'product')}), ('Properties', {'classes': ('extrapretty', 'collapse'), 'fields': ('brand_name', 'author_name', 'product_name', 'primary_image', 'author_object', 'images', 'tag_name', 'product_object', 'category_name')}))
    filter_horizontal = []
    list_display = ['__str__', 'id', 'slug', 'is_delete', 'created_at']
    list_display_links = ['__str__']
    list_editable = ['is_delete']
    list_filter = ['is_delete', 'author', 'product']
    list_max_show_all = 100
    list_per_page = 25
    list_select_related = True
    ordering = ['created_at']
    prepopulated_fields = {'slug': ('id',)}
    readonly_fields = ['slug', 'img_preview', 'created_at', 'modified_at', 'deleted_on', 'id', 'uuid', 'slug', 'img_preview', 'brand_name', 'author_name', 'product_name', 'primary_image', 'author_object', 'images', 'tag_name', 'product_object', 'category_name']
    search_help_text = ''

    def brand_name(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.brand_name]
    else:
        temp = [obj.brand_name]
    if len(temp) > 0:
        return temp
    return None

    def author_name(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.author_name]
    else:
        temp = [obj.author_name]
    if len(temp) > 0:
        return temp
    return None

    def product_name(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.product_name]
    else:
        temp = [obj.product_name]
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

    def author_object(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.author_object]
    else:
        temp = [obj.author_object]
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

    def tag_name(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.tag_name]
    else:
        temp = [obj.tag_name]
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

    def category_name(self ,obj):
        temp = []
    if hasattr(name, '__iter__'):
        temp = [i for i in obj.category_name]
    else:
        temp = [obj.category_name]
    if len(temp) > 0:
        return temp
    return None


class ProductTag(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True
    add_fieldsets = []
    fieldsets = (('Profiling', {'classes': ('extrapretty',), 'fields': (('id', 'uuid'),)}), ('Time', {'classes': ('extrapretty',), 'fields': (('created_at', 'modified_at'),)}), ('Relations', {'classes': ('extrapretty', 'collapse'), 'fields': ('product_id', 'tag_id')}))
    filter_horizontal = []
    list_display = ['__str__', 'id', 'created_at']
    list_display_links = ['__str__']
    list_editable = []
    list_filter = ['product_id', 'tag_id']
    list_max_show_all = 100
    list_per_page = 25
    list_select_related = True
    ordering = ['created_at']
    prepopulated_fields = {}
    readonly_fields = ['created_at', 'modified_at', 'id', 'uuid']
    search_help_text = ''


class ProductCategory(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True
    add_fieldsets = []
    fieldsets = (('Profiling', {'classes': ('extrapretty',), 'fields': (('id', 'uuid'),)}), ('Time', {'classes': ('extrapretty',), 'fields': (('created_at', 'modified_at'),)}), ('Relations', {'classes': ('extrapretty', 'collapse'), 'fields': ('product_id', 'category_id')}))
    filter_horizontal = []
    list_display = ['__str__', 'id', 'created_at']
    list_display_links = ['__str__']
    list_editable = []
    list_filter = ['product_id', 'category_id']
    list_max_show_all = 100
    list_per_page = 25
    list_select_related = True
    ordering = ['created_at']
    prepopulated_fields = {}
    readonly_fields = ['created_at', 'modified_at', 'id', 'uuid']
    search_help_text = ''


class ProductBrand(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True
    add_fieldsets = []
    fieldsets = (('Profiling', {'classes': ('extrapretty',), 'fields': (('id', 'uuid'),)}), ('Time', {'classes': ('extrapretty',), 'fields': (('created_at', 'modified_at'),)}), ('Relations', {'classes': ('extrapretty', 'collapse'), 'fields': ('product_id', 'brand_id')}))
    filter_horizontal = []
    list_display = ['__str__', 'id', 'created_at']
    list_display_links = ['__str__']
    list_editable = []
    list_filter = ['product_id', 'brand_id']
    list_max_show_all = 100
    list_per_page = 25
    list_select_related = True
    ordering = ['created_at']
    prepopulated_fields = {}
    readonly_fields = ['created_at', 'modified_at', 'id', 'uuid']
    search_help_text = ''

