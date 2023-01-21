
from django.utils.translation import gettext_lazy as _

from Core.ProjectMixins.Apps.Markets_Mixins import ModelRequiredProperties
from Core.fields import ProjectFields

from Core.fields import ProjectFields
from Core.models import CoreModelUniversal


# Create your models here.

class Market(ModelRequiredProperties.MarketMixin,CoreModelUniversal ):
    """
    Product Model.capitalize()
    """
    # """ Fields   """
    firstname = ProjectFields.FirstName(class_name = "Market")
    lastname = ProjectFields.LastName(class_name = "Market")
    user_name = ProjectFields.UserName(class_name = "Market")
    slug = ProjectFields.Slug(class_name = "Market")
    email = ProjectFields.Email(class_name = "Market")
    bio = ProjectFields.Bio(class_name = "Market")
    user = ProjectFields.UserForeignKey(class_name = "Market")
    gallery = ProjectFields.GalleryGenericRelation(class_name = "Market")
    wallet = ProjectFields.WalletGenericRelation(class_name = "Market")
    inventory= ProjectFields.InventoryForeignKey(class_name = "Market")
    address =ProjectFields.AddressGenericRelation(class_name = "Market")
    order_market = ProjectFields.OrderMarketForeignKey(class_name = "Market")
    # required options

    class Meta:
        verbose_name = _('Market')
        verbose_name_plural = _('Markets')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count


class Inventory(ModelRequiredProperties.InventoryMixin,CoreModelUniversal ):
    """
    Product Model.capitalize()
    """
    # """ Fields   """
    date_open = ProjectFields.DateOpen(class_name = "Inventory")
    date_close = ProjectFields.DateClose(class_name = "Inventory")
    time_open = ProjectFields.TimeOpen(class_name = "Inventory")
    time_close = ProjectFields.TimeClose(class_name = "Inventory")
    weekdays = ProjectFields.WeekDays(class_name = "Inventory")
    market = ProjectFields.MarketForeignKey(class_name = "Inventory")
    inventory_item = ProjectFields.InventoryItemForeignKey(class_name = "Inventory")
    # required options

    class Meta:
        verbose_name = _('Inventory')
        verbose_name_plural = _('Inventorys')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count


class InventoryItem(ModelRequiredProperties.InventoryitemMixin, CoreModelUniversal):
    """
    Product Model.capitalize()
    """
    # """ Fields   """
    price = ProjectFields.PriceDollar(class_name = "InventoryItem")
    date_from = ProjectFields.DateFrom(class_name = "InventoryItem")
    date_to = ProjectFields.DateTo(class_name = "InventoryItem")
    time_from = ProjectFields.TimeFrom(class_name = "InventoryItem")
    time_to = ProjectFields.TimeTo(class_name = "InventoryItem")
    weekdays = ProjectFields.WeekDays(class_name = "InventoryItem")
    inventory = ProjectFields.InventoryForeignKey(class_name = "InventoryItem")
    discount = ProjectFields.DiscountForeignKey(class_name = "InventoryItem")
    product = ProjectFields.ProductForeignKey(class_name = "InventoryItem")
    cart_item = ProjectFields.CartItemForeignKey(class_name = "InventoryItem")
    order_item = ProjectFields.OrderItemForeignKey(class_name = "InventoryItem")
    property = ProjectFields.PropertyManyToMany(class_name = "InventoryItem")

    # required options

    class Meta:
        verbose_name = _('Inventoryitem')
        verbose_name_plural = _('Inventoryitems')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count


class Inventoryitemproperty(ModelRequiredProperties.InventoryitempropertyMixin,CoreModelUniversal ):
    """
    Product Model.capitalize()
    """
    # """ Fields   """

    inventoryitem_id = ProjectFields.InventoryItemForeignKey(class_name = "Inventoryitemproperty")
    property_id = ProjectFields.PropertyForeignKey(class_name = "Inventoryitemproperty")

    # required options

    class Meta:
        verbose_name = _('Inventoryitemproperty')
        verbose_name_plural = _('Inventoryitempropertys')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count


class Property(ModelRequiredProperties.PropertyMixin,CoreModelUniversal ):
    """
    Product Model.capitalize()
    """
    # """ Fields   """
    key = ProjectFields.Key(class_name = "Property")
    value = ProjectFields.Value(class_name = "Property")
    inventory_item = ProjectFields.InventoryItemManyToMany(class_name = "Property")

    # required options

    class Meta:
        verbose_name = _('Property')
        verbose_name_plural = _('Propertys')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count


class Ordermarket(ModelRequiredProperties.OrdermarketMixin,CoreModelUniversal ):
    """
    Product Model.capitalize()
    """
    # """ Fields   """
    status_order = ProjectFields.StatusOrder(class_name = "Ordermarket")
    total_price = ProjectFields.TotalPrice(class_name = "Ordermarket")
    status_payment = ProjectFields.StatusPayment(class_name = "Ordermarket")
    order_item = ProjectFields.OrderItemForeignKey(class_name = "Ordermarket")
    order = ProjectFields.OrderForeignKey(class_name = "Ordermarket")
    shipment = ProjectFields.ShipmentForeignKey(class_name = "Ordermarket")
    payment = ProjectFields.PaymentGenericRelation(class_name = "Ordermarket")
    market = ProjectFields.MarketForeignKey(class_name = "Ordermarket")
    # required options

    class Meta:
        verbose_name = _('Ordermarket')
        verbose_name_plural = _('Ordermarkets')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count

