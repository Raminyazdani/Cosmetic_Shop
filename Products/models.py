from django.core.validators import MinValueValidator , MaxValueValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Core import
from Core.ProjectMixins.Products import Property , ModelRequiredProperties
from Core.fields import ProjectField
from Core.models import CoreModelUniversal , CoreModel
from Core.managers import BaseManager


# Create your models here.


class Product(ModelRequiredProperties.Product , CoreModelUniversal) :
    """
    Product Model
    """
    # """ Fields   """
    name = ProjectField.CustomNameField(class_name = "Product")
    comment = ProjectField.CustomCommentFieldForeignKey(class_name = "Product")
    category = ProjectField.CustomCategoryFieldManyToMany(class_name = "Product")
    tag = ProjectField.CustomTagFieldManyToMany(class_name = "Product")
    brand = ProjectField.CustomBrandFieldManyToMany(class_name = "Product")

    # GalleryField
    #   gallery = ProjectField.CustomGalleryField(class_name"Product")

    # slug field populated by name field
    slug = ProjectField.CustomSlugField(class_name = "Product")
    short_description = ProjectField.CustomShortDescriptionField(class_name = "Product")
    description = ProjectField.CustomDescriptionField(class_name = "Product")
    price = ProjectField.CustomPriceFieldDollar(class_name = "Product")
    is_available = ProjectField.CustomIsAvailableField(class_name = "Product")
    gender = ProjectField.CustomGenderField(class_name = "Product")

    # required options
    REQUIRED_FIELDS = Property.RequiredField.PRODUCT
    SEARCH_FIELDS = Property.SearchFields.PRODUCT


    class Meta :
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    # save methods are implemented in ProjectMixins
    # save slug field populated by name field and implemented in ProjectMixins
    # save Base Product implemented in ProjectMixins
    # Properties are implemented in ProjectMixins including :
    #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count

class Brand(ModelRequiredProperties.Brand , CoreModelUniversal) :
    """
    Brand Model
    """
    # """ Fields   """

    name = ProjectField.CustomNameField(class_name = "Brand")
    product = ProjectField.CustomProductFieldManyToMany(class_name = "Brand")

    # slug field populated by name field
    slug = ProjectField.CustomSlugField(class_name = "Brand")
    is_available = ProjectField.CustomIsAvailableField(class_name = "Brand")
    description = ProjectField.CustomDescriptionField(class_name = "Brand")

    # GalleryField
    #   gallery = ProjectField.CustomGalleryField("Product")

    # required options
    REQUIRED_FIELDS = Property.RequiredField.BRAND
    SEARCH_FIELDS = Property.SearchFields.BRAND

    class Meta :
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')

    # save methods are implemented in ProjectMixins
    # save slug field populated by name field and implemented in ProjectMixins
    # save Base Brand implemented in ProjectMixins
    # Properties are implemented in ProjectMixins including :
    #   tag_count , category_count , product_count , tag_names , category_names , product_names

class Category(ModelRequiredProperties.Category , CoreModelUniversal) :
    """
    Category Model
    """
    # """ Fields   """
    name = ProjectField.CustomNameField(class_name = "Category")
    parent = ProjectField.CustomCategoryParentFieldForeignKey(class_name = "Category")
    product = ProjectField.CustomProductFieldManyToMany(class_name = "Category")

    # slug field populated by name field of parent and self
    slug = ProjectField.CustomSlugField(class_name = "Category")
    description = ProjectField.CustomDescriptionField(class_name = "Category")

    # GalleryField
    #   gallery = ProjectField.CustomGalleryField("Product")

    # required options
    REQUIRED_FIELDS = Property.RequiredField.CATEGORY
    SEARCH_FIELDS = Property.SearchFields.CATEGORY

    class Meta :
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    # save methods are implemented in ProjectMixins
    # save slug field populated by name field and implemented in ProjectMixins
    # Properties are implemented in ProjectMixins including :
    #   tag_count  , product_count , brand_count , comment_count ,  tag_names , parent_names , product_names , brand_names

class Tag(ModelRequiredProperties.Tag , CoreModelUniversal) :
    """
    Tag Model
    """
    # """ Fields   """
    name = ProjectField.CustomNameField(class_name = "Tag")
    slug = ProjectField.CustomSlugField(class_name = "Tag")
    product = ProjectField.CustomProductFieldManyToMany(class_name = "Tag")

    # GalleryField
    #   gallery = ProjectField.CustomGalleryField("Product")

    # required options
    REQUIRED_FIELDS = Property.RequiredField.TAG
    SEARCH_FIELDS = Property.SearchFields.TAG

    class Meta :
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

    # save methods are implemented in ProjectMixins
    # save slug field populated by name field and implemented in ProjectMixins
    # Properties are implemented in ProjectMixins including :
    #   product_count , product_names , category_count , category_names , brand_count , brand_names , comment_count

class Comment(ModelRequiredProperties.Comment , CoreModelUniversal) :
    """
    Comment Model
    """
    # """ Fields   """
    author = ProjectField.CustomUserFieldForeignKey(
        class_name = "Comment" , verbose_name = _('Author') ,
        help_text = _('Author id') , related_name = 'comments_author'
        )
    product = ProjectField.CustomProductFieldForeignKey(class_name = "Comment")
    title = ProjectField.CustomTitleField(class_name = "Comment")
    body = ProjectField.CustomBodyField(class_name = "Comment")
    rating = ProjectField.CustomRatingField(class_name = "Comment")
    is_active = ProjectField.CustomIsActiveField(class_name = "Comment")

    # GalleryField
    #   gallery = ProjectField.CustomGalleryField("Product")

    # slug field populated by id field
    slug = ProjectField.CustomSlugField(class_name = "Comment")

    # required options
    SEARCH_FIELDS = Property.SearchFields.COMMENT
    REQUIRED_FIELDS = Property.RequiredField.COMMENT

    class Meta :
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    # save methods are implemented in ProjectMixins
    # save slug field populated by id field and implemented in ProjectMixins
    # Properties are implemented in ProjectMixins including :

class ProductTag(CoreModel) :
    """
    ProductTag Model as a many to many relationship between Product and Tag
    """
    # """ Fields   """
    product_id = ProjectField.CustomProductFieldForeignKey(class_name = "ProductTag")
    tag_id = ProjectField.CustomTagFieldForeignKey(class_name = "ProductTag")

    class Meta :
        verbose_name = _('Product Tag')
        verbose_name_plural = _('Products Tags')

class ProductCategory(CoreModel) :
    """
    ProductCategory Model as a many to many relationship between Product and Category
    """
    # """ Fields   """
    product_id = ProjectField.CustomProductFieldForeignKey(class_name = "ProductCategory")
    category_id = ProjectField.CustomCategoryFieldForeignKey(class_name = "ProductCategory")

    class Meta :
        verbose_name = _('Product Category')
        verbose_name_plural = _('Products Categories')

class ProductBrand(CoreModel) :
    """
    ProductBrand Model as a many to many relationship between Product and Brand
    """
    # """ Fields   """
    product_id = ProjectField.CustomProductFieldForeignKey(class_name = "ProductBrand")
    brand_id = ProjectField.CustomBrandFieldForeignKey(class_name = "ProductBrand")

    class Meta :
        verbose_name = _('Product Brand')
        verbose_name_plural = _('Products Brands')
