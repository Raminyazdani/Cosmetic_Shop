
from Core.ProjectMixins import Base
from Core.models import CoreModel
from . import ModelForeigns, ModelProperty


class AddressMixin(  # METHODS
        Base.Save.SaveNormal,  # save methods
        # def str and get_absolute_url
        # Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        # ModelForeigns.MODELNAMEEXTRA,  # foreign count properties MODELNAMEEXTRA
        # NAMES
        ):
    #todo do this

    class Meta:
        abstract = True

    """
    Shops.Address Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.ADDRESS
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.ADDRESS




class DiscountMixin(  # METHODS
        Base.Save.SaveNormal,  # save methods
        # def str and get_absolute_url
        # Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        # ModelForeigns.MODELNAMEEXTRA,  # foreign count properties MODELNAMEEXTRA
        # NAMES
        ):
    #todo do this

    class Meta:
        abstract = True

    """
    Shops.Discount Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.DISCOUNT
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.DISCOUNT


class GalleryMixin(  # METHODS
        Base.Save.SaveNormal,  # save methods
        # def str and get_absolute_url
        # Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        # ModelForeigns.MODELNAMEEXTRA,  # foreign count properties MODELNAMEEXTRA
        # NAMES
        ):
    #todo do this

    class Meta:
        abstract = True

    """
    Shops.Gallery Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.GALLERY
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.GALLERY


class ImageMixin(  # METHODS
        Base.Save.SaveNormal,  # save methods
        # def str and get_absolute_url
        # Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        # ModelForeigns.MODELNAMEEXTRA,  # foreign count properties MODELNAMEEXTRA
        # NAMES
        ):
    #todo do this

    class Meta:
        abstract = True

    """
    Shops.Image Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.IMAGE
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.IMAGE


class GalleryimageMixin(  # METHODS
        Base.Save.SaveNormal,  # save methods
        # def str and get_absolute_url
        # Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        # ModelForeigns.MODELNAMEEXTRA,  # foreign count properties MODELNAMEEXTRA
        # NAMES
        ):
    #todo do this

    class Meta:
        abstract = True

    """
    Shops.Galleryimage Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.GALLERYIMAGE
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.GALLERYIMAGE


class OrderMixin(  # METHODS
        Base.Save.SaveNormal,  # save methods
        # def str and get_absolute_url
        # Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        # ModelForeigns.MODELNAMEEXTRA,  # foreign count properties MODELNAMEEXTRA
        # NAMES
        ):
    #todo do this

    class Meta:
        abstract = True

    """
    Shops.Order Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.ORDER
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.ORDER


class OrderitemMixin(  # METHODS
        Base.Save.SaveNormal,  # save methods
        # def str and get_absolute_url
        # Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        # ModelForeigns.MODELNAMEEXTRA,  # foreign count properties MODELNAMEEXTRA
        # NAMES
        ):
    #todo do this

    class Meta:
        abstract = True

    """
    Shops.Orderitem Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.ORDERITEM
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.ORDERITEM


class PaymentMixin(  # METHODS
        Base.Save.SaveNormal,  # save methods
        # def str and get_absolute_url
        # Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        # ModelForeigns.MODELNAMEEXTRA,  # foreign count properties MODELNAMEEXTRA
        # NAMES
        ):
    #todo do this

    class Meta:
        abstract = True

    """
    Shops.Payment Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.PAYMENT
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.PAYMENT


class WalletMixin(  # METHODS
        Base.Save.SaveNormal,  # save methods
        # def str and get_absolute_url
        # Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        # ModelForeigns.MODELNAMEEXTRA,  # foreign count properties MODELNAMEEXTRA
        # NAMES
        ):
    #todo do this

    class Meta:
        abstract = True

    """
    Shops.Wallet Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.WALLET
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.WALLET


class ShipmentMixin(  # METHODS
        Base.Save.SaveNormal,  # save methods
        # def str and get_absolute_url
        # Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        # ModelForeigns.MODELNAMEEXTRA,  # foreign count properties MODELNAMEEXTRA
        # NAMES
        ):
    #todo do this

    class Meta:
        abstract = True

    """
    Shops.Shipment Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.SHIPMENT
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.SHIPMENT


class ContactusMixin(  # METHODS
        Base.Save.SaveNormal,  # save methods
        # def str and get_absolute_url
        # Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        # ModelForeigns.MODELNAMEEXTRA,  # foreign count properties MODELNAMEEXTRA
        # NAMES
        ):
    #todo do this

    class Meta:
        abstract = True

    """
    Shops.ContactUs Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.CONTACTUS
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.CONTACTUS
