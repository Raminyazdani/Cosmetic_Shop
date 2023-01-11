from Core.admin import BaseAdminInlineRender, BaseAdminSlug, CategoryAdminSlug

class Brand(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True

    list_display = ['name', 'is_delete', 'is_available', 'product_count', 'comment_count', "tag_count", 'category_count', 'modified_at']
    list_filter = ['is_delete', 'is_available', 'product__tag', 'product__category']
    list_editable = ['is_delete', 'is_available']
    ordering = ['name']
    filter_horizontal = ["product"]
    fieldsets = (("Profiling", {
        'classes': ('extrapretty',),
        'fields': (('name', 'slug',),)
        }), ("Extras", {
        'fields': (('product_inline',),),
        'classes': ('collapse', 'extrapretty',),
        }), ("conditions", {
        'fields': (('is_available', 'is_delete'),),
        'classes': ('wide',)
        }), ("time", {
        'fields': (('created_at', 'modified_at'),),
        'classes': ('wide',)
        }),)
    add_fieldsets = []
    prepopulated_fields = {
        'slug': ('name',),
        }
    readonly_fields = ['created_at', 'modified_at', 'product_inline']
    list_per_page = 25
    list_max_show_all = 100
    search_help_text = ""

class Category(BaseAdminInlineRender, CategoryAdminSlug):

    list_display = ['id','name', 'parent', 'is_delete', 'brand_count', 'product_count', 'comment_count', "tag_count", 'modified_at', 'slug']
<<<<<<< Updated upstream
    # list_display = ['id','name', 'is_delete', 'brand_count', 'product_count', 'comment_count', "tag_count", 'modified_at', 'slug']
    list_filter = ['is_delete', 'product__tag', 'parent', 'product__brand']
    # list_filter = ['is_delete', 'product__tag', 'product__brand']

=======
    list_filter = ['is_delete', 'product__tag', 'parent', 'product__brand']
>>>>>>> Stashed changes
    list_editable = ['is_delete']
    ordering = ['name']
    filter_horizontal = ["product"]
    fieldsets = (("Profiling", {
        'classes': ('extrapretty',),
        'fields': (("id",'name', 'parent',), "slug",)
        }), ("Extras", {
        'fields': (('product_inline',),),
        'classes': ('collapse', 'extrapretty',),
        }), ("conditions", {
        'fields': (('is_delete'),),
        'classes': ('wide',)
        }), ("time", {
        'fields': (('created_at', 'modified_at'),),
        'classes': ('wide',)
        }),)
    add_fieldsets = []
    prepopulated_fields = {
        'slug': ('name',),
        }
    readonly_fields = ["id",'created_at', 'modified_at', 'product_inline']
    list_per_page = 25
    list_max_show_all = 100
    search_help_text = ""

class Comment(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True

    list_display = ['author', 'rating', 'product', 'title', 'is_delete', 'is_active', 'modified_at', 'tag_name', 'category_name', 'brand_name']
    list_filter = ['is_delete', 'product__brand', 'product__category', 'product__tag']
    list_editable = ['is_delete', 'rating', 'is_active']
    ordering = ['product']
    filter_horizontal = []
    fieldsets = (("Profiling", {
        'classes': ('extrapretty',),
        'fields': (('author', "rating", "slug"), "title", "body")
        }), ("Extras", {
        'fields': (('product_inline',),),
        'classes': ('collapse', 'extrapretty',),
        }), ("conditions", {
        'fields': (('is_delete'),),
        'classes': ('wide',)
        }), ("time", {
        'fields': (('created_at', 'modified_at'),),
        'classes': ('wide',)
        }),)
    add_fieldsets = []
    prepopulated_fields = {
        'slug': ('id',),
        }
    readonly_fields = ['created_at', 'modified_at', 'product_inline']
    list_per_page = 25
    list_max_show_all = 100
    search_help_text = ""

class Product(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True

    list_display = ('id', 'name', 'gender', 'price', 'is_available', 'is_delete', 'comment_count', 'tag_count', 'category_count', 'brand_count', 'modified_at')
    list_filter = ['gender', 'is_available', 'is_delete', 'tag', 'category', 'brand']
    list_editable = ('price', 'is_available', 'is_delete', 'gender')
    ordering = ['name']
    filter_horizontal = ["tag", "category", "brand"]
    fieldsets = (("Profiling", {
        'classes': ('extrapretty',),
        'fields': (('name', 'slug',), ('price', 'gender'), 'short_description', 'description',)
        }), ("Extras", {
        'fields': ('tag_inline', 'category_inline', 'brand_inline', 'comment_inline'),
        'classes': ('collapse', 'extrapretty',),
        }), ("conditions", {
        'fields': (('is_available', 'is_delete'),),
        'classes': ('wide',)
        }), ("time", {
        'fields': (('created_at', 'modified_at'),),
        'classes': ('wide',)
        }),)
    add_fieldsets = []
    prepopulated_fields = {
        'slug': ('name',),
        }
    readonly_fields = ['created_at', 'modified_at', 'brand_inline', 'tag_inline', 'category_inline', 'comment_inline']
    list_per_page = 25
    list_max_show_all = 100
    search_help_text = ""

class Tag(BaseAdminInlineRender, BaseAdminSlug):
    class Meta:
        abstract = True

    list_display = ['name', 'is_delete', 'brand_count', 'product_count', 'comment_count', "category_count", 'modified_at']
    list_filter = ['is_delete', 'product__brand', 'product__category']
    list_editable = ['is_delete']
    ordering = ['name']
    filter_horizontal = ["product"]
    fieldsets = (("Profiling", {
        'classes': ('extrapretty',),
        'fields': (('name', 'slug',),)
        }), ("Extras", {
        'fields': (('product_inline',),),
        'classes': ('collapse', 'extrapretty',),
        }), ("conditions", {
        'fields': (('is_delete'),),
        'classes': ('wide',)
        }), ("time", {
        'fields': (('created_at', 'modified_at'),),
        'classes': ('wide',)
        }),)
    add_fieldsets = []
    prepopulated_fields = {
        'slug': ('name',),
        }
    readonly_fields = ['created_at', 'modified_at', 'product_inline']
    list_per_page = 25
    list_max_show_all = 100
    search_help_text = ""
