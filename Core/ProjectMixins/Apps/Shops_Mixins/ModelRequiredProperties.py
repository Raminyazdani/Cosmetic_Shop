from Core.ProjectMixins import Base
from Core.models import CoreModel
from . import ModelForeigns, ModelProperty

# MODELNAME
# MODELNAMEEXTRA

class AddressMixin(  # METHODS
        Base.Save.SaveName,  # save methods
        # def str and get_absolute_url
        Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        ModelForeigns.MODELNAMEEXTRA,  # foreign count properties AddressEXTRA
        # NAMES
        ):
    class Meta:
        abstract = True

    """
    Products.Tag Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.Address
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.Address


class CouponMixin(  # METHODS
        Base.Save.SaveName,  # save methods
        # def str and get_absolute_url
        Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        ModelForeigns.MODELNAMEEXTRA,  # foreign count properties CouponEXTRA
        # NAMES
        ):
    class Meta:
        abstract = True

    """
    Products.Tag Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.Coupon
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.Coupon

# Discount

class DiscountMixin(  # METHODS
        Base.Save.SaveName,  # save methods
        # def str and get_absolute_url
        Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        ModelForeigns.MODELNAMEEXTRA,  # foreign count properties DiscountEXTRA
        # NAMES
        ):
    class Meta:
        abstract = True

    """
    Products.Tag Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.Discount
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.Discount

# Gallery

class GalleryMixin(  # METHODS
        Base.Save.SaveName,  # save methods
        # def str and get_absolute_url
        Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        ModelForeigns.MODELNAMEEXTRA,  # foreign count properties GalleryEXTRA
        # NAMES
        ):
    class Meta:
        abstract = True

    """
    Products.Tag Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.Gallery
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.Gallery

# Image

class ImageMixin(  # METHODS
        Base.Save.SaveName,  # save methods
        # def str and get_absolute_url
        Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        ModelForeigns.MODELNAMEEXTRA,  # foreign count properties ImageEXTRA
        # NAMES
        ):
    class Meta:
        abstract = True

    """
    Products.Tag Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.Image
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.Image

# Order

class OrderMixin(  # METHODS
        Base.Save.SaveName,  # save methods
        # def str and get_absolute_url
        Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        ModelForeigns.MODELNAMEEXTRA,  # foreign count properties OrderEXTRA
        # NAMES
        ):
    class Meta:
        abstract = True

    """
    Products.Tag Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.Order
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.Order

# OrderItem

class OrderItemMixin(  # METHODS
        Base.Save.SaveName,  # save methods
        # def str and get_absolute_url
        Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        ModelForeigns.MODELNAMEEXTRA,  # foreign count properties OrderItemEXTRA
        # NAMES
        ):
    class Meta:
        abstract = True

    """
    Products.Tag Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.OrderItem
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.OrderItem

# Payment

class PaymentMixin(  # METHODS
        Base.Save.SaveName,  # save methods
        # def str and get_absolute_url
        Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        ModelForeigns.MODELNAMEEXTRA,  # foreign count properties PaymentEXTRA
        # NAMES
        ):
    class Meta:
        abstract = True

    """
    Products.Tag Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.Payment
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.Payment

# Wallet

class WalletMixin(  # METHODS
        Base.Save.SaveName,  # save methods
        # def str and get_absolute_url
        Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        ModelForeigns.MODELNAMEEXTRA,  # foreign count properties WalletEXTRA
        # NAMES
        ):
    class Meta:
        abstract = True

    """
    Products.Tag Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.Wallet
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.Wallet

# Shipment

class ShipmentMixin(  # METHODS
        Base.Save.SaveName,  # save methods
        # def str and get_absolute_url
        Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        ModelForeigns.MODELNAMEEXTRA,  # foreign count properties ShipmentEXTRA
        # NAMES
        ):
    class Meta:
        abstract = True

    """
    Products.Tag Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.Shipment
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.Shipment

# ShipmentItem

class ShipmentItemMixin(  # METHODS
        Base.Save.SaveName,  # save methods
        # def str and get_absolute_url
        Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        ModelForeigns.MODELNAMEEXTRA,  # foreign count properties ShipmentItemEXTRA
        # NAMES
        ):
    class Meta:
        abstract = True

    """
    Products.Tag Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.ShipmentItem
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.ShipmentItem

# ContactUs

class ContactUsMixin(  # METHODS
        Base.Save.SaveName,  # save methods
        # def str and get_absolute_url
        Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        ModelForeigns.MODELNAMEEXTRA,  # foreign count properties ContactUsEXTRA
        # NAMES
        ):
    class Meta:
        abstract = True

    """
    Products.Tag Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.ContactUs
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.ContactUs


