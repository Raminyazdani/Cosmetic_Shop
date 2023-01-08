from django.contrib import admin
from django.template.loader import get_template

from Core.ProjectMixins.Products import AdminProperty
from Core.admin import BaseAdminSlug, CategoryAdminSlug, CustomInlineAdmin, CustomInlineAdminOneToMany
from .models import *

class InlineMethods:

    def open(self, *args, **kwargs):
        context = getattr(self.response, 'context_data', None) or {}
        inline = context['inline_admin_formset'] = context['inline_admin_formsets'].pop()
        return get_template(inline.opts.template).render(context, self.request)

class Inlines:
    class TagInlineAdmin(CustomInlineAdmin):
        model = Product.tag.through
        tag_inline = InlineMethods.open

    class CategoryInlineAdmin(CustomInlineAdmin):
        model = Product.category.through
        category_inline = InlineMethods.open

    class CommentInlineAdmin(CustomInlineAdminOneToMany):
        model = Comment
        readonly_fields = []
        prepopulated_fields = {
            'slug': ('id',)
            }
        comment_inline = InlineMethods.open

    class BrandInlineAdmin(CustomInlineAdmin):
        model = Product.brand.through
        brand_inline = InlineMethods.open

    class ProductInline:
        class Brand(CustomInlineAdmin):
            model = Product.brand.through
            product_inline = InlineMethods.open

        class Category(CustomInlineAdmin):
            model = Product.category.through
            product_inline = InlineMethods.open

        class Tag(CustomInlineAdmin):
            model = Product.tag.through
            product_inline = InlineMethods.open

        class Comment(CustomInlineAdmin):
            model = Product
            product_inline = InlineMethods.open

@admin.register(Product)
class ProductAdmin(AdminProperty.Product):
    model = Product
    search_fields = Product.SEARCH_FIELDS
    list_display = AdminProperty.Product.list_display
    list_filter = AdminProperty.Product.list_filter
    list_editable = AdminProperty.Product.list_editable
    ordering = AdminProperty.Product.ordering
    filter_horizontal = AdminProperty.Product.filter_horizontal
    fieldsets = AdminProperty.Product.fieldsets
    add_fieldsets = AdminProperty.Product.add_fieldsets
    prepopulated_fields = AdminProperty.Product.prepopulated_fields
    readonly_fields = AdminProperty.Product.readonly_fields
    list_per_page = AdminProperty.Product.list_per_page
    list_max_show_all = AdminProperty.Product.list_max_show_all
    search_help_text = AdminProperty.Product.search_help_text

    inlines = (Inlines.TagInlineAdmin, Inlines.CategoryInlineAdmin, Inlines.BrandInlineAdmin, Inlines.CommentInlineAdmin)
    tag_inline, category_inline, brand_inline, comment_inline = inlines[0].tag_inline, inlines[1].category_inline, inlines[2].brand_inline, inlines[3].comment_inline,

#### custom query set  # def get_queryset(self, request):  #     # use our manager, rather than the default one  #  #     qs = super().get_queryset(request)  #     qs = qs.annotate(comment_count=Count('comment'))  #     qs = qs.annotate(tag_count=Count('tag'))  #     qs = qs.annotate(brand_count=Count('brand'))  #     qs = qs.annotate(category_count=Count('category'))  #     return qs

@admin.register(Brand)
class BrandAdmin(BaseAdminSlug):
    model = Brand
    search_fields = model.SEARCH_FIELDS
    list_display = AdminProperty.Brand.list_display
    list_filter = AdminProperty.Brand.list_filter
    list_editable = AdminProperty.Brand.list_editable
    ordering = AdminProperty.Brand.ordering
    filter_horizontal = AdminProperty.Brand.filter_horizontal
    fieldsets = AdminProperty.Brand.fieldsets
    add_fieldsets = AdminProperty.Brand.add_fieldsets
    prepopulated_fields = AdminProperty.Brand.prepopulated_fields
    readonly_fields = AdminProperty.Brand.readonly_fields
    list_per_page = AdminProperty.Brand.list_per_page
    list_max_show_all = AdminProperty.Brand.list_max_show_all
    search_help_text = AdminProperty.Brand.search_help_text

    inlines = [Inlines.ProductInline.Brand, ]
    product_inline = inlines[0].product_inline

@admin.register(Category)
class CategoryAdmin(CategoryAdminSlug):
    model = Category
    search_fields = model.SEARCH_FIELDS
    list_display = AdminProperty.Category.list_display
    list_filter = AdminProperty.Category.list_filter
    list_editable = AdminProperty.Category.list_editable
    ordering = AdminProperty.Category.ordering
    filter_horizontal = AdminProperty.Category.filter_horizontal
    fieldsets = AdminProperty.Category.fieldsets
    add_fieldsets = AdminProperty.Category.add_fieldsets
    prepopulated_fields = AdminProperty.Category.prepopulated_fields
    readonly_fields = AdminProperty.Category.readonly_fields
    list_per_page = AdminProperty.Category.list_per_page
    list_max_show_all = AdminProperty.Category.list_max_show_all
    search_help_text = AdminProperty.Category.search_help_text
    inlines = (Inlines.ProductInline.Category,)
    product_inline = inlines[0].product_inline

@admin.register(Tag)
class TagAdmin(BaseAdminSlug):
    model = Tag
    search_fields = model.SEARCH_FIELDS
    list_display =AdminProperty.Tag.list_display
    list_filter =AdminProperty.Tag.list_filter
    list_editable =AdminProperty.Tag.list_editable
    ordering =AdminProperty.Tag.ordering
    filter_horizontal =AdminProperty.Tag.filter_horizontal
    fieldsets =AdminProperty.Tag.fieldsets
    add_fieldsets =AdminProperty.Tag.search_fields
    prepopulated_fields =AdminProperty.Tag.prepopulated_fields
    readonly_fields =AdminProperty.Tag.readonly_fields
    list_per_page =AdminProperty.Tag.list_per_page
    list_max_show_all =AdminProperty.Tag.list_max_show_all
    search_help_text =AdminProperty.Tag.search_help_text
    
    inlines = (Inlines.ProductInline.Tag,)
    product_inline = inlines[0].product_inline

@admin.register(Comment)
class CommentAdmin(CategoryAdmin):
    model = Comment
    search_fields = model.SEARCH_FIELDS
    list_display =AdminProperty.Comment.list_display
    list_filter =AdminProperty.Comment.list_filter
    list_editable =AdminProperty.Comment.list_editable
    ordering =AdminProperty.Comment.ordering
    filter_horizontal =AdminProperty.Comment.filter_horizontal
    fieldsets =AdminProperty.Comment.fieldsets
    add_fieldsets =AdminProperty.Comment.add_fieldsets
    prepopulated_fields =AdminProperty.Comment.prepopulated_fields
    readonly_fields =AdminProperty.Comment.readonly_fields
    list_per_page =AdminProperty.Comment.list_per_page
    list_max_show_all =AdminProperty.Comment.list_max_show_all
    search_help_text =AdminProperty.Comment.search_help_text
    
    inlines = (Inlines.ProductInline.Comment,)
    product_inline = inlines[0].product_inline
