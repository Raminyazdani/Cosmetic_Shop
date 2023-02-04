
from Core.ProjectMixins import Base
from Core.models import CoreModel
from . import ModelForeigns, ModelProperty


class MarketMixin(  # METHODS
        Base.Save.SaveNormal,  # save methods
        # def str and get_absolute_url
        # Base.Str.Name, Base.AbsoluteUrl.UrlName,  # str and absolute url methods
        # property Counts
        # PROPERTIES
        # COUNTS
        Base.ImageMixin
        # ModelForeigns.MODELNAMEEXTRA,  # foreign count properties MODELNAMEEXTRA
        # NAMES
        ):
    #todo do this

    class Meta:
        abstract = True

    """
    Markets.Market Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.MARKET
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.MARKET


class InventoryMixin(  # METHODS
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
    Markets.Inventory Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.INVENTORY
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.INVENTORY


class InventoryitemMixin(  # METHODS
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
    Markets.InventoryItem Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.INVENTORYITEM
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.INVENTORYITEM


class InventoryitempropertyMixin(  # METHODS
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
    Markets.Inventoryitemproperty Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.INVENTORYITEMPROPERTY
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.INVENTORYITEMPROPERTY


class PropertyItemMixin(  # METHODS
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
    Markets.PropertyItem Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.PROPERTY
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.PROPERTY


class OrdermarketMixin(  # METHODS
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
    Markets.OrderMarket Mixin
    """
    REQUIRED_FIELDS = ModelProperty.REQUIREDFIELDS.ORDERMARKET
    SEARCH_FIELDS = ModelProperty.SEARCHFIELDS.ORDERMARKET
