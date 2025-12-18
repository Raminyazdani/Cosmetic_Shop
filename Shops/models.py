from django.db import models
from django.utils.translation import gettext_lazy as _

from Core.ProjectMixins.Apps.Shops_Mixins import ModelRequiredProperties
from Core.fields import ProjectFields
from Core.models import CoreModelUniversal  # Create your models here.

# Core import
# Create your models here.
# MODEL_NAME
# Shops


class Address(ModelRequiredProperties.AddressMixin, CoreModelUniversal):
    """
    Product Model
    """
    # """ Fields   """
    name = ProjectFields.CustomNameField(class_name = "Address")
    slug = ProjectFields.CustomSlugField(class_name = "Address")

    # required options
    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count

class Coupon(ModelRequiredProperties.CouponMixin, CoreModelUniversal):
    """
    Product Model
    """
    # """ Fields   """
    name = ProjectFields.CustomNameField(class_name = "Coupon")
    slug = ProjectFields.CustomSlugField(class_name = "Coupon")

    # required options
    class Meta:
        verbose_name = _('Coupon')
        verbose_name_plural = _('Coupons')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count

class Discount(ModelRequiredProperties.DiscountMixin, CoreModelUniversal):
    """
    Product Model
    """
    # """ Fields   """
    name = ProjectFields.CustomNameField(class_name = "Discount")
    slug = ProjectFields.CustomSlugField(class_name = "Discount")

    # required options
    class Meta:
        verbose_name = _('Discount')
        verbose_name_plural = _('Discounts')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count

class Gallery(ModelRequiredProperties.GalleryMixin, CoreModelUniversal):
    """
    Product Model
    """
    # """ Fields   """
    name = ProjectFields.CustomNameField(class_name = "Gallery")
    slug = ProjectFields.CustomSlugField(class_name = "Gallery")

    # required options
    class Meta:
        verbose_name = _('Gallery')
        verbose_name_plural = _('Galleries')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count

class Image(ModelRequiredProperties.ImageMixin, CoreModelUniversal):
    """
    Product Model
    """
    # """ Fields   """
    name = ProjectFields.CustomNameField(class_name = "Image")
    slug = ProjectFields.CustomSlugField(class_name = "Image")

    # required options
    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count
# Order


class Order(ModelRequiredProperties.OrderMixin, CoreModelUniversal):
    """
    Order Model
    """
    # """ Fields   """
    user = ProjectFields.CustomUserFieldForeignKey(class_name = "Order")
    name = ProjectFields.CustomNameField(class_name = "Order", unique = False)
    slug = ProjectFields.CustomSlugField(class_name = "Order")
    total_price = ProjectFields.CustomPriceDollarField(class_name = "Order")
    address = ProjectFields.CustomAddressFieldForeignKey(class_name = "Order")

    # required options
    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

class OrderItem(ModelRequiredProperties.OrderItemMixin, CoreModelUniversal):
    """
    OrderItem Model
    """
    # """ Fields   """
    order = ProjectFields.CustomOrderFieldForeignKey(class_name = "OrderItem")
    product = ProjectFields.CustomProductFieldForeignKey(class_name = "OrderItem")
    name = ProjectFields.CustomNameField(class_name = "OrderItem", unique = False)
    slug = ProjectFields.CustomSlugField(class_name = "OrderItem")
    quantity = models.PositiveIntegerField(default = 1)
    price = ProjectFields.CustomPriceDollarField(class_name = "OrderItem")

    class Meta:
        verbose_name = _('OrderItem')
        verbose_name_plural = _('OrderItems')

class Payment(ModelRequiredProperties.PaymentMixin, CoreModelUniversal):
    """
    Product Model
    """
    # """ Fields   """
    name = ProjectFields.CustomNameField(class_name = "Payment")
    slug = ProjectFields.CustomSlugField(class_name = "Payment")

    # required options
    class Meta:
        verbose_name = _('Payment')
        verbose_name_plural = _('Payments')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count

class Wallet(ModelRequiredProperties.WalletMixin, CoreModelUniversal):
    """
    Product Model
    """
    # """ Fields   """
    name = ProjectFields.CustomNameField(class_name = "Wallet")
    slug = ProjectFields.CustomSlugField(class_name = "Wallet")

    # required options
    class Meta:
        verbose_name = _('Wallet')
        verbose_name_plural = _('Wallets')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count

class Shipment(ModelRequiredProperties.ShipmentMixin, CoreModelUniversal):
    """
    Product Model
    """
    # """ Fields   """
    name = ProjectFields.CustomNameField(class_name = "Shipment")
    slug = ProjectFields.CustomSlugField(class_name = "Shipment")

    # required options
    class Meta:
        verbose_name = _('Shipment')
        verbose_name_plural = _('Shipments')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count


class ShipmentItem(ModelRequiredProperties.ShipmentItemMixin, CoreModelUniversal):
    """
    Product Model
    """
    # """ Fields   """
    name = ProjectFields.CustomNameField(class_name = "ShipmentItem")
    slug = ProjectFields.CustomSlugField(class_name = "ShipmentItem")

    # required options
    class Meta:
        verbose_name = _('ShipmentItem')
        verbose_name_plural = _('ShipmentItems')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count



class ContactUs(ModelRequiredProperties.ContactUsMixin,CoreModelUniversal ):
    """
    Product Model
    """
    # """ Fields   """
    name = ProjectFields.CustomNameField(class_name = "ContactUs")
    slug = ProjectFields.CustomSlugField(class_name = "ContactUs")

    # required options

    class Meta:
        verbose_name = _('ContactUs')
        verbose_name_plural = _('Contact Inquiries')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count
