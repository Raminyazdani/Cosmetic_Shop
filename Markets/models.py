
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


    # required options

    class Meta:
        verbose_name = _('Market')
        verbose_name_plural = _('Markets')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count


class Inventory(ModelRequiredProperties.InventoryMixin,CoreModelUniversal ):
    """
    Product Model.capitalize()
    """
    # """ Fields   """


    # required options

    class Meta:
        verbose_name = _('Inventory')
        verbose_name_plural = _('Inventorys')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count


class Inventoryitem(ModelRequiredProperties.InventoryitemMixin,CoreModelUniversal ):
    """
    Product Model.capitalize()
    """
    # """ Fields   """


    # required options

    class Meta:
        verbose_name = _('Inventoryitem')
        verbose_name_plural = _('Inventoryitems')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count


class Inventoryitemproperty(ModelRequiredProperties.InventoryitempropertyMixin,CoreModelUniversal ):
    """
    Product Model.capitalize()
    """
    # """ Fields   """


    # required options

    class Meta:
        verbose_name = _('Inventoryitemproperty')
        verbose_name_plural = _('Inventoryitempropertys')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count


class Property(ModelRequiredProperties.PropertyMixin,CoreModelUniversal ):
    """
    Product Model.capitalize()
    """
    # """ Fields   """


    # required options

    class Meta:
        verbose_name = _('Property')
        verbose_name_plural = _('Propertys')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count


class Ordermarket(ModelRequiredProperties.OrdermarketMixin,CoreModelUniversal ):
    """
    Product Model.capitalize()
    """
    # """ Fields   """


    # required options

    class Meta:
        verbose_name = _('Ordermarket')
        verbose_name_plural = _('Ordermarkets')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count

