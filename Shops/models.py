
from django.utils.translation import gettext_lazy as _

from Core.ProjectMixins.Apps.Shops_Mixins import ModelRequiredProperties
from Core.fields import ProjectFields

from Core.fields import ProjectFields
from Core.models import CoreModelUniversal


# Create your models here.

class Address(ModelRequiredProperties.AddressMixin,CoreModelUniversal ):
    """
    Product Model.capitalize()
    """
    # """ Fields   """


    # required options

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresss')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count


class Coupon(ModelRequiredProperties.CouponMixin,CoreModelUniversal ):
    """
    Product Model.capitalize()
    """
    # """ Fields   """


    # required options

    class Meta:
        verbose_name = _('Coupon')
        verbose_name_plural = _('Coupons')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count


class Discount(ModelRequiredProperties.DiscountMixin,CoreModelUniversal ):
    """
    Product Model.capitalize()
    """
    # """ Fields   """


    # required options

    class Meta:
        verbose_name = _('Discount')
        verbose_name_plural = _('Discounts')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count


class Gallery(ModelRequiredProperties.GalleryMixin,CoreModelUniversal ):
    """
    Product Model.capitalize()
    """
    # """ Fields   """


    # required options

    class Meta:
        verbose_name = _('Gallery')
        verbose_name_plural = _('Gallerys')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count


class Image(ModelRequiredProperties.ImageMixin,CoreModelUniversal ):
    """
    Product Model.capitalize()
    """
    # """ Fields   """


    # required options

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count


class Galleryimage(ModelRequiredProperties.GalleryimageMixin,CoreModelUniversal ):
    """
    Product Model.capitalize()
    """
    # """ Fields   """


    # required options

    class Meta:
        verbose_name = _('Galleryimage')
        verbose_name_plural = _('Galleryimages')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count


class Order(ModelRequiredProperties.OrderMixin,CoreModelUniversal ):
    """
    Product Model.capitalize()
    """
    # """ Fields   """


    # required options

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count


class Orderitem(ModelRequiredProperties.OrderitemMixin,CoreModelUniversal ):
    """
    Product Model.capitalize()
    """
    # """ Fields   """


    # required options

    class Meta:
        verbose_name = _('Orderitem')
        verbose_name_plural = _('Orderitems')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count


class Payment(ModelRequiredProperties.PaymentMixin,CoreModelUniversal ):
    """
    Product Model.capitalize()
    """
    # """ Fields   """


    # required options

    class Meta:
        verbose_name = _('Payment')
        verbose_name_plural = _('Payments')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count


class Wallet(ModelRequiredProperties.WalletMixin,CoreModelUniversal ):
    """
    Product Model.capitalize()
    """
    # """ Fields   """


    # required options

    class Meta:
        verbose_name = _('Wallet')
        verbose_name_plural = _('Wallets')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count


class Shipment(ModelRequiredProperties.ShipmentMixin,CoreModelUniversal ):
    """
    Product Model.capitalize()
    """
    # """ Fields   """


    # required options

    class Meta:
        verbose_name = _('Shipment')
        verbose_name_plural = _('Shipments')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count


class Contactus(ModelRequiredProperties.ContactusMixin,CoreModelUniversal ):
    """
    Product Model.capitalize()
    """
    # """ Fields   """


    # required options

    class Meta:
        verbose_name = _('Contactus')
        verbose_name_plural = _('Contactuss')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count

