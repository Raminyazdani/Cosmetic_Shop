from django.utils.translation import gettext_lazy as _

from Core.ProjectMixins.Apps.Products_Mixins import ModelRequiredProperties
# Create your models here.
from Core.fields import ProjectFields

# Core import
# Create your models here.
from Core.fields import ProjectFields
from Core.models import CoreModelUniversal

class Product(ModelRequiredProperties.ProductMixin,CoreModelUniversal ):
    """
    Product Model
    """
    # """ Fields   """
    name = ProjectFields.CustomNameField(class_name = "Product")
    comment = ProjectFields.CustomCommentFieldForeignKey(class_name = "Product")
    category = ProjectFields.CustomCategoryFieldManyToMany(class_name = "Product")
    tag = ProjectFields.CustomTagFieldManyToMany(class_name = "Product")
    brand = ProjectFields.CustomBrandFieldManyToMany(class_name = "Product")

    # GalleryField
    #   gallery = ProjectField.CustomGalleryField(class_name"Product")
    # slug field populated by name field
    slug = ProjectFields.CustomSlugField(class_name = "Product")
    short_description = ProjectFields.CustomShortDescriptionField(class_name = "Product")
    description = ProjectFields.CustomDescriptionField(class_name = "Product")
    price = ProjectFields.CustomPriceDollarField(class_name = "Product")
    is_available = ProjectFields.CustomIsAvailableField(class_name = "Product")
    gender = ProjectFields.CustomGenderField(class_name = "Product")

    # required options

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count

class Category(ModelRequiredProperties.CategoryMixin,CoreModelUniversal):
    """
    Category Model
    """
    # """ Fields   """
    name = ProjectFields.CustomNameField(class_name = "Category")
    parent = ProjectFields.CustomCategoryParentFieldForeignKey(class_name = "Category",default=None, null=True, blank=True)
    product = ProjectFields.CustomProductFieldManyToMany(class_name = "Category")

    # slug field populated by name field of parent and self
    slug = ProjectFields.CustomSlugField(class_name = "Category")
    description = ProjectFields.CustomDescriptionField(class_name = "Category")

    REQUIRED_FIELDS = ['name']
    # GalleryField
    #   gallery = ProjectField.CustomGalleryField("Product")
    # required options
<<<<<<< Updated upstream
    REQUIRED_FIELDS = ModelProperty.RequiredField.CATEGORY
    SEARCH_FIELDS = ModelProperty.SearchFields.CATEGORY

    class Meta :
=======
    class Meta:
>>>>>>> Stashed changes
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count  , product_count , brand_count , comment_count ,  tag_names , parent_names , product_names , brand_names
    def save(self: object, *args, **kwargs):

        super().save(*args, **kwargs)
class Brand(ModelRequiredProperties.BrandMixin,CoreModelUniversal):
    """
    Brand Model
    """
    # """ Fields   """
    name = ProjectFields.CustomNameField(class_name = "Brand")
    product = ProjectFields.CustomProductFieldManyToMany(class_name = "Brand")

    # slug field populated by name field
    slug = ProjectFields.CustomSlugField(class_name = "Brand")
    is_available = ProjectFields.CustomIsAvailableField(class_name = "Brand")
    description = ProjectFields.CustomDescriptionField(class_name = "Brand")

    # GalleryField
    #   gallery = ProjectField.CustomGalleryField("Product")
    # required options

    class Meta:
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Brand implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count , category_count , product_count , tag_names , category_names , product_names

class Tag(ModelRequiredProperties.TagMixin,CoreModelUniversal):
    """
    Tag Model
    """
    # """ Fields   """
    name = ProjectFields.CustomNameField(class_name = "Tag")
    slug = ProjectFields.CustomSlugField(class_name = "Tag")
    product = ProjectFields.CustomProductFieldManyToMany(class_name = "Tag")

    # GalleryField
    #   gallery = ProjectField.CustomGalleryField("Product")
    # required options

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   product_count , product_names , category_count , category_names , brand_count , brand_names , comment_count

class Comment(ModelRequiredProperties.CommentMixin,CoreModelUniversal):
    """
    Comment Model
    """
    # """ Fields   """
    author = ProjectFields.CustomUserFieldForeignKey(class_name = "Comment", verbose_name = _('Author'), help_text = _('Author id'), related_name = 'comments_author')
    product = ProjectFields.CustomProductFieldForeignKey(class_name = "Comment")
    title = ProjectFields.CustomTitleField(class_name = "Comment")
    body = ProjectFields.CustomBodyField(class_name = "Comment")
    rating = ProjectFields.CustomRatingField(class_name = "Comment")
    is_active = ProjectFields.CustomIsActiveField(class_name = "Comment")

    # GalleryField
    #   gallery = ProjectField.CustomGalleryField("Product")
    # slug field populated by id field
    slug = ProjectFields.CustomSlugField(class_name = "Comment")

    # required options

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')  # save methods are implemented in ProjectMixins  # save slug field populated by id field and implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :

class ProductTag(ModelRequiredProperties.ProductTagMixin,CoreModelUniversal):
    """
    ProductTag Model as a many to many relationship between Product and Tag
    """
    # """ Fields   """
    product_id = ProjectFields.CustomProductFieldForeignKey(class_name = "ProductTag")
    tag_id = ProjectFields.CustomTagFieldForeignKey(class_name = "ProductTag")

    class Meta:
        verbose_name = _('Product Tag')
        verbose_name_plural = _('Products and Tags')

class ProductCategory(ModelRequiredProperties.ProductCategoryMixin,CoreModelUniversal):
    """
    ProductCategory Model as a many to many relationship between Product and Category
    """
    # """ Fields   """
    product_id = ProjectFields.CustomProductFieldForeignKey(class_name = "ProductCategory")
    category_id = ProjectFields.CustomCategoryFieldForeignKey(class_name = "ProductCategory")

    class Meta:
        verbose_name = _('Product Category')
        verbose_name_plural = _('Products and Categories')

class ProductBrand(ModelRequiredProperties.ProductBrandMixin,CoreModelUniversal):
    """
    ProductBrand Model as a many to many relationship between Product and Brand
    """
    # """ Fields   """
    product_id = ProjectFields.CustomProductFieldForeignKey(class_name = "ProductBrand")
    brand_id = ProjectFields.CustomBrandFieldForeignKey(class_name = "ProductBrand")

    class Meta:
        verbose_name = _('Product Brand')
        verbose_name_plural = _('Products and Brands')
