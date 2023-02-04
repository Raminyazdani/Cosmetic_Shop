import Core.ProjectMixins.Base.ModelForeigns
from Core.ProjectMixins import Base
from Core.models import CoreModel
from . import ModelForeigns, ModelProperty

class TagMixin(  # METHODS
        Base.Save.SaveNormal,  # save methods
        # def str and get_absolute_url
        # Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        # NAMES
        Base.ImageMixin
        ):
    #todo do this

    class Meta:
        abstract = True

    """
    Products.Tag Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.TAG
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.TAG

class ProductMixin(  # METHODS
        Base.Save.SaveNormal,  # save methods
        # def str and get_absolute_url
        # Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        Base.ImageMixin# PropertyItem names
        # NAMES
        ):
    #todo do this

    class Meta:
        abstract = True

    """
    Products.Product Mixin
    """

    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.PRODUCT
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.PRODUCT

class CommentMixin(  # METHODS
        Base.Save.SaveNormal,  # save methods
        Base.ImageMixin# def str and get_absolute_url
        # Base.Str.Title, Base.AbsoluteUrl.UrlId,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        # ModelForeigns.Tag,  # foreign count properties Tag
        # ModelForeigns.Category,  # foreign count properties Category
        # ModelForeigns.Brand,  # foreign count properties Brand
        # ModelForeigns.Product,  # NAMES
        ):
    #todo do this

    class Meta:
        abstract = True

    """
    Product.Comment Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.COMMENT
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.COMMENT

class CategoryMixin(
        # METHODS
        Base.Save.SaveNormal,  # save methods
        Base.ImageMixin# def str and get_absolute_url
        # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS

        # NAMES
        ):
    #todo do this

    class Meta:
        abstract = True

    """
    Products.Category Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.CATEGORY
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.CATEGORY

class BrandMixin(  # METHODS
        Base.Save.SaveNormal,  # save methods
        Base.ImageMixin# def str and get_absolute_url
        # Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        ):
    #todo do this

    class Meta:
        abstract: True

    """
    Products.Brand Mixin
    """

    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.BRAND
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.BRAND

class ProductBrandMixin(CoreModel):
    #todo do this

    class Meta:
        abstract = True

    """
    Products.ProductBrand Mixin
    """

class ProductCategoryMixin(CoreModel):
    #todo do this

    class Meta:
        abstract = True

    """
    Products.ProductCategory Mixin
    """

class ProductTagMixin(CoreModel):
    #todo do this

    class Meta:
        abstract = True

    """
    Product.ProductTag Mixin
    """
