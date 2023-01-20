from django.utils.translation import gettext_lazy as _

from Core.ProjectMixins.Apps.Products_Mixins import ModelRequiredProperties
# Create your models here.

# Core import
# Create your models here.
from Core.fields import ProjectFields
from Core.models import CoreModelUniversal

class Product(ModelRequiredProperties.ProductMixin,CoreModelUniversal ):
    """
    Product Model
    """
    # """ Fields   """
    name = ProjectFields.Name(class_name = "Product")
    comment = ProjectFields.CommentForeignKey(class_name = "Product")
    category = ProjectFields.CategoryManyToMany(class_name = "Product")
    tag = ProjectFields.TagManyToMany(class_name = "Product")
    brand = ProjectFields.BrandManyToMany(class_name = "Product")

    gallery = ProjectFields.GalleryGenericRelation(class_name = "Customer")

    # slug field populated by name field
    slug = ProjectFields.Slug(class_name = "Product")
    short_description = ProjectFields.ShortDescription(class_name = "Product")
    description = ProjectFields.Description(class_name = "Product")
    price = ProjectFields.PriceDollar(class_name = "Product")
    is_available = ProjectFields.IsAvailable(class_name = "Product")
    gender = ProjectFields.Gender(class_name = "Product")

    # required options

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count

class Category(ModelRequiredProperties.CategoryMixin,CoreModelUniversal):
    """
    Category Model
    """
    # """ Fields   """
    name = ProjectFields.Name(class_name = "Category")
    parent = ProjectFields.ParentForeignKey(class_name = "Category")
    product = ProjectFields.ProductManyToMany(class_name = "Category")

    # slug field populated by name field of parent and self
    slug = ProjectFields.Slug(class_name = "Category")
    description = ProjectFields.Description(class_name = "Category")
    gallery = ProjectFields.GalleryGenericRelation(class_name = "Customer")

    REQUIRED_FIELDS = ['name']

    # required options


    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count  , product_count , brand_count , comment_count ,  tag_names , parent_names , product_names , brand_names
    def save(self: object, *args, **kwargs):

        super().save(*args, **kwargs)
class Brand(ModelRequiredProperties.BrandMixin,CoreModelUniversal):
    """
    Brand Model
    """
    # """ Fields   """
    name = ProjectFields.Name(class_name = "Brand")
    product = ProjectFields.ProductManyToMany(class_name = "Brand")

    # slug field populated by name field
    slug = ProjectFields.Slug(class_name = "Brand")
    is_available = ProjectFields.IsAvailable(class_name = "Brand")
    description = ProjectFields.Description(class_name = "Brand")
    gallery = ProjectFields.GalleryGenericRelation(class_name = "Customer")

    # required options

    class Meta:
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Brand implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count , category_count , product_count , tag_names , category_names , product_names

class Tag(ModelRequiredProperties.TagMixin,CoreModelUniversal):
    """
    Tag Model
    """
    # """ Fields   """
    name = ProjectFields.Name(class_name = "Tag")
    slug = ProjectFields.Slug(class_name = "Tag")
    product = ProjectFields.ProductManyToMany(class_name = "Tag")
    gallery = ProjectFields.GalleryGenericRelation(class_name = "Customer")

    # required options

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   product_count , product_names , category_count , category_names , brand_count , brand_names , comment_count

class Comment(ModelRequiredProperties.CommentMixin,CoreModelUniversal):
    """
    Comment Model
    """
    # """ Fields   """
    author = ProjectFields.UserForeignKey(class_name = "Comment", verbose_name = _('Author'), help_text = _('Author id'), related_name = 'comments_author')
    product = ProjectFields.ProductForeignKey(class_name = "Comment")
    title = ProjectFields.Title(class_name = "Comment")
    body = ProjectFields.Body(class_name = "Comment")
    rating = ProjectFields.Rating(class_name = "Comment")
    is_active = ProjectFields.IsActive(class_name = "Comment")
    gallery = ProjectFields.GalleryGenericRelation(class_name = "Customer")

    # slug field populated by id field
    slug = ProjectFields.Slug(class_name = "Comment")

    # required options

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')  # save methods are implemented in ProjectMixins  # save slug field populated by id field and implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :

class ProductTag(ModelRequiredProperties.ProductTagMixin,CoreModelUniversal):
    """
    ProductTag Model as a many to many relationship between Product and Tag
    """
    # """ Fields   """
    product_id = ProjectFields.ProductForeignKey(class_name = "ProductTag")
    tag_id = ProjectFields.TagForeignKey(class_name = "ProductTag")

    class Meta:
        verbose_name = _('Product Tag')
        verbose_name_plural = _('Products and Tags')

class ProductCategory(ModelRequiredProperties.ProductCategoryMixin,CoreModelUniversal):
    """
    ProductCategory Model as a many to many relationship between Product and Category
    """
    # """ Fields   """
    product_id = ProjectFields.ProductForeignKey(class_name = "ProductCategory")
    category_id = ProjectFields.CategoryForeignKey(class_name = "ProductCategory")

    class Meta:
        verbose_name = _('Product Category')
        verbose_name_plural = _('Products and Categories')

class ProductBrand(ModelRequiredProperties.ProductBrandMixin,CoreModelUniversal):
    """
    ProductBrand Model as a many to many relationship between Product and Brand
    """
    # """ Fields   """
    product_id = ProjectFields.ProductForeignKey(class_name = "ProductBrand")
    brand_id = ProjectFields.BrandForeignKey(class_name = "ProductBrand")

    class Meta:
        verbose_name = _('Product Brand')
        verbose_name_plural = _('Products and Brands')
