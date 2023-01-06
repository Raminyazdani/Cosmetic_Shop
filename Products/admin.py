from django.contrib import admin
from django.template.loader import get_template

from Core.admin import BaseAdminSlug, CustomInlineAdminOneToMany, CustomInlineAdmin
from .models import *


class Inlines:
    class TagInlineAdmin(CustomInlineAdmin):
        model = Product.tag.through

    class CategoryInlineAdmin(CustomInlineAdmin):
        model = Product.category.through

    class CommentInlineAdmin(CustomInlineAdminOneToMany):
        model = Comment
        readonly_fields = []
        prepopulated_fields = {'slug': ('id',)}

    class BrandInlineAdmin(CustomInlineAdmin):
        model = Product.brand.through

    class ProductInline:
        class Brand(CustomInlineAdmin):
            model = Product.brand.through
        class Category(CustomInlineAdmin):
            model = Product.category.through
        class Tag(CustomInlineAdmin):
            model = Product.tag.through


@admin.register(Product)
class ProductAdmin(BaseAdminSlug):
    model = Product

    list_display = ('id', 'name', 'gender',
                    'price', 'is_available', 'is_delete',
                    'comment_count', 'tag_count', 'category_count', 'brand_count', 'modified_at')
    list_filter = ['gender', 'is_available', 'is_delete', 'tag', 'category', 'brand']
    list_editable = ('price', 'is_available', 'is_delete', 'gender')
    search_fields = Product.SEARCH_FIELDS
    ordering = ['name']
    inlines = (
        Inlines.TagInlineAdmin, Inlines.CategoryInlineAdmin, Inlines.BrandInlineAdmin, Inlines.CommentInlineAdmin)
    filter_horizontal = ["tag", "category", "brand"]

    fieldsets = (

        ("Profiling", {
            'classes': ('extrapretty',),
            'fields': (('name', 'slug',), ('price', 'gender'), 'short_description', 'description',)

        }),
        ("Extras", {
            'fields': (
                'tag_inline', 'category_inline', 'brand_inline', 'comment_inline'),
            'classes': ('collapse', 'extrapretty',),
        }),

        ("conditions", {
            'fields': (('is_available', 'is_delete'),),
            'classes': ('wide',)
        }),
        ("time", {
            'fields': (('created_at', 'modified_at'),),
            'classes': ('wide',)
        }),
    )

    add_fieldsets = []
    prepopulated_fields = {'slug': ('name',), }

    readonly_fields = ['created_at', 'modified_at', 'brand_inline', 'tag_inline', 'category_inline', 'comment_inline']
    list_per_page = 25
    list_max_show_all = 100
    search_help_text = ""

    def tag_inline(self, *args, **kwargs):
        context = getattr(self.response, 'context_data', None) or {}
        inline = context['inline_admin_formset'] = context['inline_admin_formsets'].pop(0)
        return get_template(inline.opts.template).render(context, self.request)

    def category_inline(self, *args, **kwargs):
        context = getattr(self.response, 'context_data', None) or {}
        inline = context['inline_admin_formset'] = context['inline_admin_formsets'].pop(0)
        return get_template(inline.opts.template).render(context, self.request)

    def brand_inline(self, *args, **kwargs):
        context = getattr(self.response, 'context_data', None) or {}
        inline = context['inline_admin_formset'] = context['inline_admin_formsets'].pop(0)
        return get_template(inline.opts.template).render(context, self.request)

    def comment_inline(self, *args, **kwargs):
        context = getattr(self.response, 'context_data', None) or {}
        inline = context['inline_admin_formset'] = context['inline_admin_formsets'].pop(0)
        return get_template(inline.opts.template).render(context, self.request)

    def render_change_form(self, request, *args, **kwargs):
        self.request = request
        self.response = super().render_change_form(request, *args, **kwargs)
        return self.response

    #### custom query set
    # def get_queryset(self, request):
    #     # use our manager, rather than the default one
    #
    #     qs = super().get_queryset(request)
    #     qs = qs.annotate(comment_count=Count('comment'))
    #     qs = qs.annotate(tag_count=Count('tag'))
    #     qs = qs.annotate(brand_count=Count('brand'))
    #     qs = qs.annotate(category_count=Count('category'))
    #     return qs

    ### costum query set
    # def get_queryset(self, request):
    #     # use our manager, rather than the default one
    #
    #     qs = super().get_queryset(request)
    #     return qs

    # @staticmethod
    # def return_on_failure(value):
    #     def decorate(f):
    #         def applicator(*args, **kwargs):
    #             try:
    #                 return f(*args, **kwargs)
    #             except:
    #                 return value
    #
    #         return applicator
    #
    #     return decorate

    # def get_sortable_by(self, request):
    #     print(self.get_list_display(request))
    #     return {*self.get_list_display(request)}

    # def comments_count(self, inst):
    #     return inst.comment_count
    #
    # def tags_count(self, inst):
    #     return inst.tag_count
    #
    # def brands_count(self, inst):
    #     return inst.brand_count
    #
    # def categorys_count(self, inst):
    #     return inst.category_count
    #
    # comments_count.admin_order_field = 'comment_count'
    # tags_count.admin_order_field = 'tag_count'
    # categorys_count.admin_order_field = 'category_count'
    # brands_count.admin_order_field = 'brand_count'


@admin.register(Brand)
class BrandAdmin(BaseAdminSlug):
    model = Brand
    list_display = ['name', 'is_delete', 'is_available', 'product_count', 'comment_count', "tag_count",
                    'category_count', 'modified_at']
    list_filter = ['is_delete', 'is_available', 'product__tag', 'product__category']
    list_editable = ['is_delete', 'is_available']
    search_fields = Brand.SEARCH_FIELDS
    ordering = ['name']
    filter_horizontal = ["product"]

    inlines = (Inlines.ProductInline.Brand,)
    fieldsets = (

        ("Profiling", {
            'classes': ('extrapretty',),
            'fields': (('name', 'slug',),)

        }),
        ("Extras", {
            'fields': (
                ('product_inline',),
            ),

            'classes': ('collapse', 'extrapretty',),
        }),
        ("conditions", {
            'fields': (('is_available', 'is_delete'),),
            'classes': ('wide',)
        }),
        ("time", {
            'fields': (('created_at', 'modified_at'),),
            'classes': ('wide',)
        }),
    )

    add_fieldsets = []
    prepopulated_fields = {'slug': ('name',), }

    readonly_fields = ['created_at', 'modified_at', 'product_inline']
    list_per_page = 25
    list_max_show_all = 100
    search_help_text = ""

    def product_inline(self, *args, **kwargs):
        context = getattr(self.response, 'context_data', None) or {}
        inline = context['inline_admin_formset'] = context['inline_admin_formsets'].pop()
        return get_template(inline.opts.template).render(context, self.request)

    def render_change_form(self, request, *args, **kwargs):
        self.request = request
        self.response = super().render_change_form(request, *args, **kwargs)
        return self.response

    # product_count.admin_order_field = 'product_count'


@admin.register(Category)
class CategoryAdmin(BaseAdminSlug):
    model = Category
    list_display = ['name', 'parent', 'is_delete', 'brand_count', 'product_count', 'comment_count', "tag_count",
                    'modified_at','slug']
    list_filter = ['is_delete', 'product__tag','parent','product__brand']
    list_editable = ['is_delete']
    search_fields = Category.SEARCH_FIELDS
    ordering = ['name']
    filter_horizontal = ["product"]

    inlines = (Inlines.ProductInline.Category,)
    fieldsets = (

        ("Profiling", {
            'classes': ('extrapretty',),
            'fields': (('name', 'parent',),"slug",)

        }),
        ("Extras", {
            'fields': (
                ('product_inline',),
            ),

            'classes': ('collapse', 'extrapretty',),
        }),
        ("conditions", {
            'fields': (('is_delete'),),
            'classes': ('wide',)
        }),
        ("time", {
            'fields': (('created_at', 'modified_at'),),
            'classes': ('wide',)
        }),
    )

    add_fieldsets = []
    prepopulated_fields = {'slug': ('name',), }

    readonly_fields = ['created_at', 'modified_at', 'product_inline']
    list_per_page = 25
    list_max_show_all = 100
    search_help_text = ""

    def product_inline(self, *args, **kwargs):
        context = getattr(self.response, 'context_data', None) or {}
        inline = context['inline_admin_formset'] = context['inline_admin_formsets'].pop()
        return get_template(inline.opts.template).render(context, self.request)

    def render_change_form(self, request, *args, **kwargs):
        self.request = request
        self.response = super().render_change_form(request, *args, **kwargs)
        return self.response

    # product_count.admin_order_field = 'product_count'
@admin.register(Tag)
class TagAdmin(BaseAdminSlug):
    model = Tag
    list_display = ['name', 'is_delete', 'brand_count', 'product_count', 'comment_count', "category_count",
                    'modified_at']
    list_filter = ['is_delete', 'product__brand','product__category']
    list_editable = ['is_delete']
    search_fields = Tag.SEARCH_FIELDS
    ordering = ['name']
    filter_horizontal = ["product"]

    inlines = (Inlines.ProductInline.Tag,)
    fieldsets = (

        ("Profiling", {
            'classes': ('extrapretty',),
            'fields': (('name', 'slug',),)

        }),
        ("Extras", {
            'fields': (
                ('product_inline',),
            ),

            'classes': ('collapse', 'extrapretty',),
        }),
        ("conditions", {
            'fields': (('is_delete'),),
            'classes': ('wide',)
        }),
        ("time", {
            'fields': (('created_at', 'modified_at'),),
            'classes': ('wide',)
        }),
    )

    add_fieldsets = []
    prepopulated_fields = {'slug': ('name',), }

    readonly_fields = ['created_at', 'modified_at', 'product_inline']
    list_per_page = 25
    list_max_show_all = 100
    search_help_text = ""

    def product_inline(self, *args, **kwargs):
        context = getattr(self.response, 'context_data', None) or {}
        inline = context['inline_admin_formset'] = context['inline_admin_formsets'].pop()
        return get_template(inline.opts.template).render(context, self.request)

    def render_change_form(self, request, *args, **kwargs):
        self.request = request
        self.response = super().render_change_form(request, *args, **kwargs)
        return self.response

    # product_count.admin_order_field = 'product_count'

@admin.register(Comment)
class CommentAdmin(BaseAdminSlug):
    model = Comment
    list_display = ['author', 'rating','product', 'title','is_delete','is_active', 'modified_at','tag_names','category_names','brand_names']
    list_filter = ['is_delete', 'product__brand','product__category','product__tag']
    list_editable = ['is_delete','rating','is_active']
    search_fields = Comment.SEARCH_FIELDS
    ordering = ['product']
    filter_horizontal = []

    fieldsets = (

        ("Profiling", {
            'classes': ('extrapretty',),
            'fields': (('name', 'slug',),)

        }),
        ("Extras", {
            'fields': (
                ('product_inline',),
            ),

            'classes': ('collapse', 'extrapretty',),
        }),
        ("conditions", {
            'fields': (('is_delete'),),
            'classes': ('wide',)
        }),
        ("time", {
            'fields': (('created_at', 'modified_at'),),
            'classes': ('wide',)
        }),
    )

    add_fieldsets = []
    prepopulated_fields = {'slug': ('id',), }

    readonly_fields = ['created_at', 'modified_at', 'product_inline']
    list_per_page = 25
    list_max_show_all = 100
    search_help_text = ""

    def product_inline(self, *args, **kwargs):
        context = getattr(self.response, 'context_data', None) or {}
        inline = context['inline_admin_formset'] = context['inline_admin_formsets'].pop()
        return get_template(inline.opts.template).render(context, self.request)

    def render_change_form(self, request, *args, **kwargs):
        self.request = request
        self.response = super().render_change_form(request, *args, **kwargs)
        return self.response

    # product_count.admin_order_field = 'product_count'

