import Core.ProjectMixins.Base.ModelForeigns
from Core.ProjectMixins import Base
from Core.models import CoreModel
from . import ModelForeigns, ModelProperty

class TagMixin(  # METHODS
        Base.Save.SaveName,  # save methods
        # def str and get_absolute_url
        Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        ModelForeigns.Brand,  # foreign count properties Brand
        ModelForeigns.Category,  # foreign count properties Category
        ModelForeigns.Comment,  # foreign count properties Comment
        ModelForeigns.Product,  # foreign count properties Product
        # NAMES
        ):
    class Meta:
        abstract = True

    """
    Products.Tag Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.TAG
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.TAG

class ProductMixin(  # METHODS
        Base.Save.SaveName, Base.Save.SaveProduct,  # save methods
        # def str and get_absolute_url
        Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        ModelForeigns.Tag,  # foreign count properties Tag
        ModelForeigns.Category,  # foreign count properties Category
        ModelForeigns.Comment,  # foreign count properties Comment
        ModelForeigns.Brand,  # foreign count properties Brand
        # Property names
        # NAMES
        ):
    class Meta:
        abstract = True

    """
    Products.Product Mixin
    """

    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.PRODUCT
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.PRODUCT

class CommentMixin(  # METHODS
        Base.Save.SaveId,  # save methods
        # def str and get_absolute_url
        Base.Str.Title, Base.AbsoluteUrl.UrlId,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        ModelForeigns.Tag,  # foreign count properties Tag
        ModelForeigns.Category,  # foreign count properties Category
        ModelForeigns.Brand,  # foreign count properties Brand
        ModelForeigns.Product,  # NAMES
        ):
    class Meta:
        abstract = True

    """
    Product.Comment Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.COMMENT
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.COMMENT

class CategoryMixin(
        # METHODS
        Base.Save.SaveName,Base.Save.SaveCategory,Base.Save.SaveParent,  # save methods
        # def str and get_absolute_url
        Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        ModelForeigns.Tag,  # foreign count properties Tag
        Core.ProjectMixins.Base.ModelForeigns.Parent,  # foreign count properties Parent
        ModelForeigns.Brand,  # foreign count properties Brand
        ModelForeigns.Comment,  # foreign count properties Comment
        ModelForeigns.Product,  # foreign count properties Products
        # NAMES
        ):
    class Meta:
        abstract = True

    """
    Products.Category Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.CATEGORY
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.CATEGORY

class BrandMixin(  # METHODS
        Base.Save.SaveName,  # save methods
        # def str and get_absolute_url
        Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        ModelForeigns.Tag,  # foreign count properties Tag
        ModelForeigns.Category,  # foreign count properties Category
        ModelForeigns.Comment,  # foreign count properties Comment
        ModelForeigns.Product,  # foreign count properties Product
        ):
    class Meta:
        abstract: True

    """
    Products.Brand Mixin
    """

    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.BRAND
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.BRAND

class ProductBrandMixin(CoreModel):
    class Meta:
        abstract = True

    """
    Products.ProductBrand Mixin
    """

class ProductCategoryMixin(CoreModel):
    class Meta:
        abstract = True

    """
    Products.ProductCategory Mixin
    """

class ProductTagMixin(CoreModel):
    class Meta:
        abstract = True

    """
    Product.ProductTag Mixin
    """
