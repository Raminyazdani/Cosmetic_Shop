from django.urls import reverse
from django.utils.functional import cached_property
from django.utils.text import slugify

from Core.admin import BaseAdminInlineRender, BaseAdminSlug

class ModelMethod:
    class Meta:
        abstract=True
    """
    Methods Mixin
    """

    class Str:
        class Meta:
            abstract=True
        """
        Str Mixin
        """

        class name:
            class Meta:
                abstract=True
            """
            Str Mixin for name field
            """

            def __str__(self):
                """
                Return name field
                :return:  name field
                """
                return self.name

        class id:
            class Meta:
                abstract=True
            """
            Str Mixin for id field
            """

            def __str__(self):
                """
                Return id field
                :return:  id field
                """
                return self.id

        class title:
            class Meta:
                abstract=True
            """
            Str Mixin for title field
            """

            def __str__(self):
                """
                Return title field
                :return:  title field
                """
                return self.title

    class Save:
        class Meta:
            abstract=True
        """
        Save Mixin
        """

        class Slug:
            class Meta:
                abstract=True
            """
            Slug Mixin
            """

            class Name:
                class Meta:
                    abstract=True
                """
                Slug Mixin for name field
                """

                def save(self, *args, **kwargs):
                    """
                    Save slug field with name field
                    :param args:
                    :param kwargs:
                    :return:
                    """
                    slug = slugify(self.name)
                    self.slug = slug
                    super().save(*args, **kwargs)

            class Id:
                class Meta:
                    abstract=True
                """
                Slug Mixin for id field
                """

                def save(self, *args, **kwargs):
                    """
                    Save slug field with id field
                    :param args:
                    :param kwargs:
                    :return:
                    """
                    slug = slugify(self.id)
                    self.slug = slug
                    super().save(*args, **kwargs)

            class Category:
                class Meta:
                    abstract=True
                """
                Slug Mixin for category field
                """

                def save(self, *args, **kwargs):
                    """
                    Save slug field with category field and parents
                    :param args:
                    :param kwargs:
                    :return:
                    """
                    if self.id and self.parent and self.id == self.parent.id:
                        self.parent = None
                    if self.pk is None:
                        super().save(*args, **kwargs)
                    slug = self.parents_names + [slugify(self.name)]
                    self.slug = "/".join(slug).lower()
                    super().save(*args, **kwargs)

        class Base:
            class Meta:
                abstract=True
            """
            Base Mixin
            """

            class Product:
                class Meta:
                    abstract=True
                """
                Product Mixin
                """

                def save(self, *args, **kwargs):
                    """
                    Save product model Base
                    :param args:
                    :param kwargs:
                    :return:
                    """
                    super().save(*args, **kwargs)

                class WithCategoryParents:
                    class Meta:
                        abstract=True
                    """
                    Product Mixin with category parents saving
                    """

                    def save(self, *args, **kwargs):
                        """
                        Save product model with categories parents
                        :param args:
                        :param kwargs:
                        :return:
                        """
                        if self.pk is None:
                            super().save(*args, **kwargs)
                        categories = self.category.all()
                        categories_id = [x for x in categories.values_list('id', flat = True)]
                        for category in categories:
                            category_temp = category
                            while category_temp.parent:
                                category_temp = category_temp.parent
                                categories_id.append(category_temp.id)
                        categories_id = list(set(categories_id))
                        print(categories_id)
                        self.category.set(categories_id)
                        super().save(*args, **kwargs)

    class AbsoluteUrl:
        class Meta:
            abstract=True
        """
        AbsoluteUrl Mixin
        """

        class Slug:
            class Meta:
                abstract=True
            """
            Slug Mixin
            """

            def get_absolute_url(self):
                """
                Return absolute url
                :return:
                """
                return reverse('product_detail', kwargs = {
                    'slug': self.slug
                    })

class ModelProperty:
    class Meta:
        abstract=True
    """
    Property Mixin
    """

    class Foreign:
        class Meta:
            abstract=True
        """
        Foreign Mixin
        """

        class Count:
            class Meta:
                abstract=True
            """
            Count Mixin
            """

            class ForComment:
                class Meta:
                    abstract=True
                """
                Count Mixin for comments
                """

                class Tag:
                    class Meta:
                        abstract=True
                    """
                    Count Mixin for tag
                    """

                    @cached_property
                    def tag_count(self):
                        """
                        Return tag count
                        :return:
                        """
                        return self.product.tag.count()

                class Category:
                    class Meta:
                        abstract=True
                    """
                    Count Mixin for category
                    """

                    @cached_property
                    def category_count(self):
                        """
                        Return category count
                        :return:
                        """
                        return self.product.category.count()

                class Brand:
                    class Meta:
                        abstract=True
                    """
                    Count Mixin for brand
                    """

                    @cached_property
                    def brand_count(self):
                        """
                        Return brand count
                        :return:
                        """
                        return self.product.brand.count()

            class ForOther:
                class Meta:
                    abstract=True
                """
                ForOther Mixin
                """

                class Product:
                    class Meta:
                        abstract=True
                    """
                    Product Mixin
                    """

                    @cached_property
                    def product_count(self):
                        """
                        Return product count
                        :return:
                        """
                        return self.product.count()

                class Comment:
                    class Meta:
                        abstract=True
                    """
                    Comment Mixin
                    """

                    @cached_property
                    def comment_count(self):
                        """
                        Return comment count
                        :return:
                        """
                        return sum([product.comment_count for product in self.product.all()])

                class Tag:
                    class Meta:
                        abstract=True
                    """
                    Tag Mixin
                    """

                    @cached_property
                    def tag_count(self):
                        """
                        Return tag count
                        :return:
                        """
                        return len(list(set([product.tag for product in self.product.all()])))

                class Category:
                    class Meta:
                        abstract=True
                    """
                    Category Mixin
                    """

                    @cached_property
                    def category_count(self):
                        """
                        Return category count
                        :return:
                        """
                        list_cat = []
                        products = self.product.all()
                        for product in products:
                            for category in product.category.all():
                                list_cat.append(category.id)
                        return len(set(list_cat))

                class Brand:
                    class Meta:
                        abstract=True
                    """
                    Brand Mixin
                    """

                    @cached_property
                    def brand_count(self):
                        """
                        Return brand count
                        :return:
                        """
                        return len(list(set([product.brand for product in self.product.all()])))

            class ForProduct:
                class Meta:
                    abstract=True
                """
                ForProduct Mixin
                """

                class Comment:
                    class Meta:
                        abstract=True
                    """
                    Comment Mixin
                    """

                    @cached_property
                    def comment_count(self):
                        """
                        Return comment count
                        :return:
                        """
                        return self.comment_product.count()

                class Tag:
                    class Meta:
                        abstract=True
                    """
                    Tag Mixin
                    """

                    @cached_property
                    def tag_count(self):
                        """
                        Return tag count
                        :return:
                        """
                        return self.tag.count()

                class Category:
                    class Meta:
                        abstract=True
                    """
                    Category Mixin
                    """

                    @cached_property
                    def category_count(self):
                        """
                        Return category count
                        :return:
                        """
                        return self.category.count()

                class Brand:
                    class Meta:
                        abstract=True
                    """
                    Brand Mixin
                    """

                    @cached_property
                    def brand_count(self):
                        """
                        Return brand count
                        :return:
                        """
                        return self.brand.count()

        class Names:
            class Meta:
                abstract=True
            """
            Names Mixin
            """

            class ForOther:
                class Meta:
                    abstract=True
                """
                ForOther Mixin
                """

                class Product:
                    class Meta:
                        abstract=True
                    """
                    Product Mixin
                    """

                    @cached_property
                    def product_names(self):
                        """
                        Return product names
                        :return:
                        """
                        return [product.name for product in self.product.all()]

                class Tag:
                    class Meta:
                        abstract=True
                    """
                    Tag Mixin
                    """

                    @cached_property
                    def tag_names(self):
                        """
                        Return tag names
                        :return:
                        """
                        products = self.product.all()
                        list_tag = []
                        for product in products:
                            tags = product.tag.all()
                            [list_tag.append(tag.name) for tag in tags]
                        if len(list_tag) > 0:
                            return list(set(list_tag))
                        return []

                class Category:
                    class Meta:
                        abstract=True
                    """
                    Category Mixin
                    """

                    @cached_property
                    def category_names(self):
                        """
                        Return category names
                        :return:
                        """
                        products = self.product.all()
                        list_cat = []
                        for product in products:
                            categories = product.category.all()
                            [list_cat.append(cat.name) for cat in categories]
                        if len(list_cat) > 0:
                            return list(set(list_cat))
                        return []

                class Brand:
                    class Meta:
                        abstract=True
                    """
                    Brand Mixin
                    """

                    @cached_property
                    def brand_names(self):
                        """
                        Return brand names
                        :return:
                        """
                        products = self.product.all()
                        list_brand = []
                        for product in products:
                            brands = product.brand.all()
                            [list_brand.append(brand.name) for brand in brands]
                        if len(list_brand) > 0:
                            return list(set(list_brand))
                        return []

            class ForProduct:
                class Meta:
                    abstract=True
                """
                ForProduct Mixin
                """

                class Brand:
                    class Meta:
                        abstract=True
                    """
                    Brand Mixin
                    """

                    @cached_property
                    def brand_name(self):
                        """
                        Return brand name
                        :return:
                        """
                        return [brand.name for brand in self.brand.all()]

                class Category:
                    class Meta:
                        abstract=True
                    """
                    Category Mixin
                    """

                    @cached_property
                    def category_name(self):
                        """
                        Return category name
                        :return:
                        """
                        return [category.name for category in self.category.all()]

                class Tag:
                    class Meta:
                        abstract=True
                    """
                    Tag Mixin
                    """

                    @cached_property
                    def tag_name(self):
                        """
                        Return tag name
                        :return:
                        """
                        return [tag.name for tag in self.tag.all()]

            class ForComment:
                class Meta:
                    abstract=True
                """
                ForComment Mixin
                """

                class Tag:
                    class Meta:
                        abstract=True
                    """
                    Tag Mixin
                    """

                    @cached_property
                    def tag_names(self):
                        """
                        Return tag name
                        :return:
                        """
                        return self.product.tag_name

                class Category:
                    class Meta:
                        abstract=True
                    """
                    Category Mixin
                    """

                    @cached_property
                    def category_names(self):
                        """
                        Return category name
                        :return:
                        """
                        return self.product.category_name

                class Brand:
                    class Meta:
                        abstract=True
                    """
                    Brand Mixin
                    """

                    @cached_property
                    def brand_names(self):
                        """
                        Return brand name
                        :return:
                        """
                        return self.product.brand_name

                class Product:
                    class Meta:
                        abstract=True
                    """
                    Product Mixin
                    """

                    @cached_property
                    def product_name(self):
                        """
                        Return product name
                        :return:
                        """
                        return self.product

                class User:
                    class Meta:
                        abstract=True
                    """
                    User Mixin
                    """

                    @cached_property
                    def user_name(self):
                        """
                        Return user name
                        :return:
                        """
                        return self.user.username

            class ForCategory:
                class Meta:
                    abstract=True
                """
                ForCategory Mixin
                """

                class Parent:
                    class Meta:
                        abstract=True
                    """
                    Parent Mixin
                    """

                    @cached_property
                    def parents_names(self):
                        """
                        Return parents names
                        :return:
                        """
                        parent_list = []
                        cat = self
                        while cat.parent:
                            parent_list.append(cat.parent.name)
                            cat = cat.parent
                        if len(parent_list) > 0:
                            return parent_list
                        return []

    class RequiredField():
        class Meta:
            abstract=True
        """
        RequiredField Mixin
        Product App Mixin
        """
        PRODUCT = ['name', 'gender']
        BRAND = ['name']
        CATEGORY = ['name']
        TAG = ['name']
        COMMENT = ['product', 'author', 'title', 'body', 'rating']

    class SearchFields:
        class Meta:
            abstract=True
        """
        SearchFields Mixin
        Product App Mixin
        """
        PRODUCT = ['name', 'short_description', 'category__name', 'tag__name', 'brand__name']
        BRAND = ['name', 'product__name', 'product__category__name', 'product__tag__name', 'product__brand__name']
        CATEGORY = ['name', 'product__name', 'product__category__name', 'product__tag__name', 'product__brand__name', 'parent__name', 'parent__product__name']
        TAG = ['name', 'product__name', 'product__category__name', 'product__tag__name', 'product__brand__name']
        COMMENT = ['title', 'body', 'author__username', 'product__name', 'product__category__name', 'product__tag__name', 'product__brand__name']

class ModelRequiredProperties:
    class Meta:
        abstract=True
    """
    ModelRequiredProperties Mixin
    """

    class Product(  # METHODS
            ModelMethod.Save.Slug.Name, ModelMethod.Save.Base.Product,  # save methods
            # def str and get_absolute_url
            ModelMethod.Str.name, ModelMethod.AbsoluteUrl.Slug,  # str and absolute url methods
            # property Counts
            # PROPERTIES
            # COUNTS
            ModelProperty.Foreign.Count.ForProduct.Tag,  # foreign count properties Tag
            ModelProperty.Foreign.Count.ForProduct.Category,  # foreign count properties Category
            ModelProperty.Foreign.Count.ForProduct.Comment,  # foreign count properties Comment
            ModelProperty.Foreign.Count.ForProduct.Brand,  # foreign count properties Brand
            # Property names
            # NAMES
            ModelProperty.Foreign.Names.ForProduct.Tag,  # foreign name properties Tag
            ModelProperty.Foreign.Names.ForProduct.Category,  # foreign name properties Category
            ModelProperty.Foreign.Names.ForProduct.Brand,  # foreign name properties Brand
            ):
        """
        Products.Product Mixin
        """
        pass

    class Brand(  # METHODS
            ModelMethod.Save.Slug.Name,  # save methods
            # def str and get_absolute_url
            ModelMethod.Str.name, ModelMethod.AbsoluteUrl.Slug,  # str and absolute url methods
            # property Counts
            # PROPERTIES
            # COUNTS
            ModelProperty.Foreign.Count.ForOther.Tag,  # foreign count properties Tag
            ModelProperty.Foreign.Count.ForOther.Category,  # foreign count properties Category
            ModelProperty.Foreign.Count.ForOther.Comment,  # foreign count properties Comment
            ModelProperty.Foreign.Count.ForOther.Product,  # foreign count properties Products
            # NAMES
            ModelProperty.Foreign.Names.ForOther.Tag,  # foreign name properties Tag
            ModelProperty.Foreign.Names.ForOther.Category,  # foreign name properties Category
            ModelProperty.Foreign.Names.ForOther.Product,  # foreign name properties Products
            ):
        """
        Products.Brand Mixin
        """
        pass

    class Category(  # METHODS
            ModelMethod.Save.Slug.Category,  # save methods
            # def str and get_absolute_url
            ModelMethod.Str.name, ModelMethod.AbsoluteUrl.Slug,  # str and absolute url methods
            # property Counts
            # PROPERTIES
            # COUNTS
            ModelProperty.Foreign.Count.ForOther.Tag,  # foreign count properties Tag
            ModelProperty.Foreign.Count.ForOther.Brand,  # foreign count properties Brand
            ModelProperty.Foreign.Count.ForOther.Comment,  # foreign count properties Comment
            ModelProperty.Foreign.Count.ForOther.Product,  # foreign count properties Products
            # NAMES
            ModelProperty.Foreign.Names.ForOther.Tag,  # foreign name properties Tag
            ModelProperty.Foreign.Names.ForOther.Brand,  # foreign name properties Brand
            ModelProperty.Foreign.Names.ForOther.Product,  # foreign name properties Products
            ModelProperty.Foreign.Names.ForCategory.Parent,  # foreign name properties Parent
            ):
        """
        Products.Category Mixin
        """
        pass

    class Tag(  # METHODS
            ModelMethod.Save.Slug.Name,  # save methods
            # def str and get_absolute_url
            ModelMethod.Str.name, ModelMethod.AbsoluteUrl.Slug,  # str and absolute url methods
            # property Counts
            # PROPERTIES
            # COUNTS
            ModelProperty.Foreign.Count.ForOther.Brand,  # foreign count properties Brand
            ModelProperty.Foreign.Count.ForOther.Category,  # foreign count properties Category
            ModelProperty.Foreign.Count.ForOther.Comment,  # foreign count properties Comment
            ModelProperty.Foreign.Count.ForOther.Product,  # foreign count properties Products
            # NAMES
            ModelProperty.Foreign.Names.ForOther.Brand,  # foreign name properties Brand
            ModelProperty.Foreign.Names.ForOther.Category,  # foreign name properties Category
            ModelProperty.Foreign.Names.ForOther.Product,  # foreign name properties Products
            ):
        """
        Products.Tag Mixin
        """
        pass

    class Comment(  # METHODS
            ModelMethod.Save.Slug.Id,  # save methods
            # def str and get_absolute_url
            ModelMethod.Str.title, ModelMethod.AbsoluteUrl.Slug,  # str and absolute url methods
            # property Counts
            # PROPERTIES
            # COUNTS
            ModelProperty.Foreign.Count.ForComment.Tag,  # foreign count properties Tag
            ModelProperty.Foreign.Count.ForComment.Category,  # foreign count properties Category
            ModelProperty.Foreign.Count.ForComment.Brand,  # foreign count properties Brand
            # NAMES
            ModelProperty.Foreign.Names.ForComment.Tag,  # foreign name properties Tag
            ModelProperty.Foreign.Names.ForComment.Category,  # foreign name properties Category
            ModelProperty.Foreign.Names.ForComment.Product,  # foreign name properties Products
            ModelProperty.Foreign.Names.ForComment.Brand,  # foreign name properties Brand
            ):
        """
        Products.Comment Mixin
        """
        pass

    class ProductTag():
        class Meta:
            abstract=True
        """
        Products.ProductTag Mixin
        """
        pass

    class ProductCategory():
        class Meta:
            abstract=True
        """
        Products.ProductCategory Mixin
        """
        pass

    class ProductBrand():
        class Meta:
            abstract=True
        """
        Products.ProductBrand Mixin
        """
        pass

class AdminProperty():
    class Meta:
        abstract=True
    class Product(BaseAdminInlineRender, BaseAdminSlug):
        class Meta:
            abstract=True
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

    class Brand(BaseAdminInlineRender, BaseAdminSlug):
        class Meta:
            abstract=True
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

    class Category(BaseAdminInlineRender, BaseAdminSlug):
        class Meta:
            abstract=True
        list_display = ['name', 'parent', 'is_delete', 'brand_count', 'product_count', 'comment_count', "tag_count", 'modified_at', 'slug']
        list_filter = ['is_delete', 'product__tag', 'parent', 'product__brand']
        list_editable = ['is_delete']
        ordering = ['name']
        filter_horizontal = ["product"]
        fieldsets = (("Profiling", {
            'classes': ('extrapretty',),
            'fields': (('name', 'parent',), "slug",)
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

    class Tag(BaseAdminInlineRender, BaseAdminSlug):
        class Meta:
            abstract=True
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

    class Comment(BaseAdminInlineRender, BaseAdminSlug):
        class Meta:
            abstract=True
        list_display = ['author', 'rating', 'product', 'title', 'is_delete', 'is_active', 'modified_at', 'tag_names', 'category_names', 'brand_names']
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
