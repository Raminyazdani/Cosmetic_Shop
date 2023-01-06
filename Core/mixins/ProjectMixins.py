from django.urls import reverse
from django.utils.text import slugify
from django.utils.functional import cached_property


class Methods:
    """
    Methods Mixin
    """

    class Str:
        """
        Str Mixin
        """

        class name:
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
        """
        Save Mixin
        """

        class Slug:
            """
            Slug Mixin
            """

            class Name:
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
                    self.slug = "/".join(slug)
                    super().save(*args, **kwargs)

        class Base:
            """
            Base Mixin
            """

            class Product:
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
                        categories_id = [x for x in categories.values_list('id', flat=True)]
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
        """
        AbsoluteUrl Mixin
        """

        class Slug:
            """
            Slug Mixin
            """

            def get_absolute_url(self):
                """
                Return absolute url
                :return:
                """
                return reverse('product_detail', kwargs={'slug': self.slug})


class Property:
    """
    Property Mixin
    """

    class Foreign:
        """
        Foreign Mixin
        """

        class Count:
            """
            Count Mixin
            """

            class ForComment:
                """
                Count Mixin for comments
                """

                class Tag:
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
                """
                ForOther Mixin
                """

                class Product:
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
                """
                ForProduct Mixin
                """

                class Comment:
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
            """
            Names Mixin
            """

            class ForOther:
                """
                ForOther Mixin
                """

                class Product:
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
                """
                ForProduct Mixin
                """

                class Brand:
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
                """
                ForComment Mixin
                """

                class Tag:
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
                """
                ForCategory Mixin
                """

                class Parent:
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
        """
        RequiredField Mixin
        """

        class PRODUCTS:
            """
            Product App Mixin
            """
            PRODUCT = ['name', 'gender']

            BRAND = ['name']

            CATEGORY = ['name']

            TAG = ['name']

            COMMENT = ['product', 'author', 'title', 'body', 'rating']

    class SearchFields:
        """
        SearchFields Mixin
        """

        class PRODUCTS:
            """
            Product App Mixin
            """
            PRODUCT = ['name', 'short_description', 'category__name', 'tag__name', 'brand__name']

            BRAND = ['name', 'product__name', 'product__category__name', 'product__tag__name',
                     'product__brand__name']
            CATEGORY = ['name', 'product__name', 'product__category__name', 'product__tag__name',
                        'product__brand__name', 'parent__name', 'parent__product__name']

            TAG = ['name', 'product__name', 'product__category__name', 'product__tag__name', 'product__brand__name']

            COMMENT = ['title', 'body', 'author__username', 'product__name', 'product__category__name',
                       'product__tag__name', 'product__brand__name']


class ModelRequiredProperties:
    """
    ModelRequiredProperties Mixin
    """

    class PRODUCTS:
        """
        Product App Mixin
        """

        class Product(
            # METHODS
            Methods.Save.Slug.Name, Methods.Save.Base.Product,  # save methods

            # def str and get_absolute_url
            Methods.Str.name, Methods.AbsoluteUrl.Slug,  # str and absolute url methods

            # property Counts

            # PROPERTIES
            # COUNTS
            Property.Foreign.Count.ForProduct.Tag,  # foreign count properties Tag
            Property.Foreign.Count.ForProduct.Category,  # foreign count properties Category
            Property.Foreign.Count.ForProduct.Comment,  # foreign count properties Comment
            Property.Foreign.Count.ForProduct.Brand,  # foreign count properties Brand

            # Property names
            # NAMES
            Property.Foreign.Names.ForProduct.Tag,  # foreign name properties Tag
            Property.Foreign.Names.ForProduct.Category,  # foreign name properties Category
            Property.Foreign.Names.ForProduct.Brand,  # foreign name properties Brand

        ):
            """
            Products.Product Mixin
            """
            pass

        class Brand(
            # METHODS
            Methods.Save.Slug.Name,  # save methods

            # def str and get_absolute_url
            Methods.Str.name, Methods.AbsoluteUrl.Slug,  # str and absolute url methods

            # property Counts

            # PROPERTIES
            # COUNTS
            Property.Foreign.Count.ForOther.Tag,  # foreign count properties Tag
            Property.Foreign.Count.ForOther.Category,  # foreign count properties Category
            Property.Foreign.Count.ForOther.Comment,  # foreign count properties Comment
            Property.Foreign.Count.ForOther.Product,  # foreign count properties Products
            # NAMES
            Property.Foreign.Names.ForOther.Tag,  # foreign name properties Tag
            Property.Foreign.Names.ForOther.Category,  # foreign name properties Category
            Property.Foreign.Names.ForOther.Product,  # foreign name properties Products
        ):
            """
            Products.Brand Mixin
            """
            pass

        class Category(
            # METHODS
            Methods.Save.Slug.Category,  # save methods

            # def str and get_absolute_url
            Methods.Str.name, Methods.AbsoluteUrl.Slug,  # str and absolute url methods

            # property Counts

            # PROPERTIES
            # COUNTS
            Property.Foreign.Count.ForOther.Tag,  # foreign count properties Tag
            Property.Foreign.Count.ForOther.Brand,  # foreign count properties Brand
            Property.Foreign.Count.ForOther.Comment,  # foreign count properties Comment
            Property.Foreign.Count.ForOther.Product,  # foreign count properties Products
            # NAMES
            Property.Foreign.Names.ForOther.Tag,  # foreign name properties Tag
            Property.Foreign.Names.ForOther.Brand,  # foreign name properties Brand
            Property.Foreign.Names.ForOther.Product,  # foreign name properties Products
            Property.Foreign.Names.ForCategory.Parent,  # foreign name properties Parent
        ):
            """
            Products.Category Mixin
            """
            pass

        class Tag(
            # METHODS
            Methods.Save.Slug.Name,  # save methods

            # def str and get_absolute_url
            Methods.Str.name, Methods.AbsoluteUrl.Slug,  # str and absolute url methods

            # property Counts

            # PROPERTIES
            # COUNTS
            Property.Foreign.Count.ForOther.Brand,  # foreign count properties Brand
            Property.Foreign.Count.ForOther.Category,  # foreign count properties Category
            Property.Foreign.Count.ForOther.Comment,  # foreign count properties Comment
            Property.Foreign.Count.ForOther.Product,  # foreign count properties Products
            # NAMES
            Property.Foreign.Names.ForOther.Brand,  # foreign name properties Brand
            Property.Foreign.Names.ForOther.Category,  # foreign name properties Category
            Property.Foreign.Names.ForOther.Product,  # foreign name properties Products
        ):
            """
            Products.Tag Mixin
            """
            pass

        class Comment(
            # METHODS
            Methods.Save.Slug.Id,  # save methods

            # def str and get_absolute_url
            Methods.Str.title, Methods.AbsoluteUrl.Slug,  # str and absolute url methods

            # property Counts

            # PROPERTIES
            # COUNTS
            Property.Foreign.Count.ForComment.Tag,  # foreign count properties Tag
            Property.Foreign.Count.ForComment.Category,  # foreign count properties Category
            Property.Foreign.Count.ForComment.Brand,  # foreign count properties Brand
            # NAMES
            Property.Foreign.Names.ForComment.Tag,  # foreign name properties Tag
            Property.Foreign.Names.ForComment.Category,  # foreign name properties Category
            Property.Foreign.Names.ForComment.Product,  # foreign name properties Products
            Property.Foreign.Names.ForComment.Brand,  # foreign name properties Brand
        ):
            """
            Products.Comment Mixin
            """
            pass

        class ProductTag():
            """
            Products.ProductTag Mixin
            """
            pass

        class ProductCategory():
            """
            Products.ProductCategory Mixin
            """
            pass

        class ProductBrand():
            """
            Products.ProductBrand Mixin
            """
            pass
