
from Core.ProjectMixins import Base
from Core.models import CoreModel
from . import ModelForeigns, ModelProperty


class CustomerMixin(  # METHODS
        Base.Save.SaveName,  # save methods
        # def str and get_absolute_url
        Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        # ModelForeigns.MODELNAMEEXTRA,  # foreign count properties MODELNAMEEXTRA
        # NAMES
        ):
    class Meta:
        abstract = True

    """
    Customers.Customer Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.CUSTOMER
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.CUSTOMER


class CartMixin(  # METHODS
        Base.Save.SaveName,  # save methods
        # def str and get_absolute_url
        Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        # ModelForeigns.MODELNAMEEXTRA,  # foreign count properties MODELNAMEEXTRA
        # NAMES
        ):
    class Meta:
        abstract = True

    """
    Customers.Cart Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.CART
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.CART


class CartitemMixin(  # METHODS
        Base.Save.SaveName,  # save methods
        # def str and get_absolute_url
        Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        # ModelForeigns.MODELNAMEEXTRA,  # foreign count properties MODELNAMEEXTRA
        # NAMES
        ):
    class Meta:
        abstract = True

    """
    Customers.Cartitem Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.CARTITEM
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.CARTITEM


class CustomercouponMixin(  # METHODS
        Base.Save.SaveName,  # save methods
        # def str and get_absolute_url
        Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        # ModelForeigns.MODELNAMEEXTRA,  # foreign count properties MODELNAMEEXTRA
        # NAMES
        ):
    class Meta:
        abstract = True

    """
    Customers.Customercoupon Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.CUSTOMERCOUPON
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.CUSTOMERCOUPON


class FavoriteMixin(  # METHODS
        Base.Save.SaveName,  # save methods
        # def str and get_absolute_url
        Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        # ModelForeigns.MODELNAMEEXTRA,  # foreign count properties MODELNAMEEXTRA
        # NAMES
        ):
    class Meta:
        abstract = True

    """
    Customers.Favorite Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.FAVORITE
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.FAVORITE


class FavoriteitemMixin(  # METHODS
        Base.Save.SaveName,  # save methods
        # def str and get_absolute_url
        Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        # ModelForeigns.MODELNAMEEXTRA,  # foreign count properties MODELNAMEEXTRA
        # NAMES
        ):
    class Meta:
        abstract = True

    """
    Customers.Favoriteitem Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.FAVORITEITEM
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.FAVORITEITEM


class OrdercustomerMixin(  # METHODS
        Base.Save.SaveName,  # save methods
        # def str and get_absolute_url
        Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        # ModelForeigns.MODELNAMEEXTRA,  # foreign count properties MODELNAMEEXTRA
        # NAMES
        ):
    class Meta:
        abstract = True

    """
    Customers.Ordercustomer Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.ORDERCUSTOMER
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.ORDERCUSTOMER


class WishlistMixin(  # METHODS
        Base.Save.SaveName,  # save methods
        # def str and get_absolute_url
        Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        # ModelForeigns.MODELNAMEEXTRA,  # foreign count properties MODELNAMEEXTRA
        # NAMES
        ):
    class Meta:
        abstract = True

    """
    Customers.Wishlist Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.WISHLIST
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.WISHLIST


class WishlistitemMixin(  # METHODS
        Base.Save.SaveName,  # save methods
        # def str and get_absolute_url
        Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        # ModelForeigns.MODELNAMEEXTRA,  # foreign count properties MODELNAMEEXTRA
        # NAMES
        ):
    class Meta:
        abstract = True

    """
    Customers.Wishlistitem Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.WISHLISTITEM
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.WISHLISTITEM
