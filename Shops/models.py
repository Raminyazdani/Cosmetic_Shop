from django.utils.translation import gettext_lazy as _

from Core.ProjectMixins.Apps.Shops_Mixins import ModelRequiredProperties
from Core.fields import ProjectFields
from Core.models import CoreModelUniversal
from django.contrib.contenttypes.models import ContentType

# Create your models here.

class Address(ModelRequiredProperties.AddressMixin, CoreModelUniversal):
    """
    Product Model.capitalize()
    """
    # """ Fields   """
    country = ProjectFields.Country(class_name = "Address")
    city = ProjectFields.City(class_name = "Address")
    province = ProjectFields.Province(class_name = "Address")
    address_line = ProjectFields.AddressLine(class_name = "Address")
    postal_code = ProjectFields.PostalCode(class_name = "Address")
    firstname = ProjectFields.FirstName(class_name = "Address")
    lastname = ProjectFields.LastName(class_name = "Address")
    Coordinate = ProjectFields.Coordinate(class_name = "Address")

    content_type = ProjectFields.ContentType(class_name = "Address")
    object_id = ProjectFields.ObjectId(class_name = "Address")
    object = ProjectFields.Object(class_name = "Address")

    # required options
    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count


class Discount(ModelRequiredProperties.DiscountMixin, CoreModelUniversal):
    """
    Product Model.capitalize()
    """
    # """ Fields   """
    discount_type = ProjectFields.DiscountType(class_name = "Discount")
    minimum_amount= ProjectFields.MinimumAmount(class_name = "Discount")
    maximum_amount= ProjectFields.MaximumAmount(class_name = "Discount")
    percentage= ProjectFields.Percentage(class_name = "Discount")
    date_from= ProjectFields.DateFrom(class_name = "Discount")
    date_to= ProjectFields.DateTo(class_name = "Discount")
    inventory_item= ProjectFields.InventoryItemForeignKey(class_name = "Discount")

    # required options
    class Meta:
        verbose_name = _('Discount')
        verbose_name_plural = _('Discounts')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count

class Gallery(ModelRequiredProperties.GalleryMixin, CoreModelUniversal):
    """
    Product Model.capitalize()
    """
    # """ Fields   """

    image = ProjectFields.ImageManyToMany(class_name = "Gallery")

    # required options
    class Meta:
        verbose_name = _('Gallery')
        verbose_name_plural = _('Galleries')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count

class Image(ModelRequiredProperties.ImageMixin, CoreModelUniversal):
    """
    Product Model.capitalize()
    """
    # """ Fields   """
    path_original = ProjectFields.PathOriginal(class_name = "Image")
    path_thumbnail = ProjectFields.PathThumbnail(class_name = "Image")
    image= ProjectFields.Image(class_name = "Image")
    alt_text= ProjectFields.AltText(class_name = "Image")
    gallery= ProjectFields.GalleryManyToMany(class_name = "Image")

    # required options
    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count

class GalleryImage(ModelRequiredProperties.GalleryimageMixin, CoreModelUniversal):
    """
    Product Model.capitalize()
    """
    # """ Fields   """
    gallery_id= ProjectFields.GalleryForeignKey(class_name = "GalleryImage")
    image_id = ProjectFields.ImageForeignKey(class_name = "GalleryImage")

    # required options
    class Meta:
        verbose_name = _('GalleryImage')
        verbose_name_plural = _('GalleryImages')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count

class Order(ModelRequiredProperties.OrderMixin, CoreModelUniversal):
    """
    Product Model.capitalize()
    """
    # """ Fields   """
    status_order = ProjectFields.StatusOrder(class_name = "Order")
    order_item = ProjectFields.OrderItemForeignKey(class_name = "Order")
    order_customer= ProjectFields.OrderCustomerForeignKey(class_name = "Order")
    order_market= ProjectFields.OrderMarketForeignKey(class_name = "Order")

    # required options
    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count

class OrderItem(ModelRequiredProperties.OrderitemMixin, CoreModelUniversal):
    """
    Product Model.capitalize()
    """
    # """ Fields   """
    quantity= ProjectFields.Quantity(class_name = "OrderItem")
    final_price= ProjectFields.FinalPrice(class_name = "OrderItem")
    order= ProjectFields.OrderForeignKey(class_name = "OrderItem")
    order_customer= ProjectFields.OrderCustomerForeignKey(class_name = "OrderItem")
    inventory_item= ProjectFields.InventoryItemForeignKey(class_name = "OrderItem")
    order_market= ProjectFields.OrderMarketForeignKey(class_name = "OrderItem")

    # required options
    class Meta:
        verbose_name = _('Orderitem')
        verbose_name_plural = _('Orderitems')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count

class Payment(ModelRequiredProperties.PaymentMixin, CoreModelUniversal):
    """
    Product Model.capitalize()
    """
    # """ Fields   """
    payment_type = ProjectFields.PaymentType(class_name = "Payment")
    amount = ProjectFields.Amount(class_name = "Payment")
    description = ProjectFields.Description(class_name = "Payment")
    status_payment = ProjectFields.StatusPayment(class_name = "Payment")
    content_type = ProjectFields.ContentType(class_name = "Payment")
    object_id =  ProjectFields.ObjectId(class_name = "Payment")
    object =  ProjectFields.Object(class_name = "Payment")


    # required options
    class Meta:
        verbose_name = _('Payment')
        verbose_name_plural = _('Payments')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count

class Wallet(ModelRequiredProperties.WalletMixin, CoreModelUniversal):
    """
    Product Model.capitalize()
    """
    # """ Fields   """
    amount = ProjectFields.Amount(class_name = "Wallet")
    sheba = ProjectFields.Sheba(class_name = "Wallet")
    card_number = ProjectFields.CardNumber(class_name = "Wallet")
    firstname = ProjectFields.FirstName(class_name = "Wallet")
    lastname = ProjectFields.LastName(class_name = "Wallet")
    content_type = ProjectFields.ContentType(class_name = "Wallet")
    object_id =  ProjectFields.ObjectId(class_name = "Wallet")
    object =  ProjectFields.Object(class_name = "Wallet")

    # required options
    class Meta:
        verbose_name = _('Wallet')
        verbose_name_plural = _('Wallets')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count

class Shipment(ModelRequiredProperties.ShipmentMixin, CoreModelUniversal):
    """
    Product Model.capitalize()
    """
    # """ Fields   """
    shipment_type = ProjectFields.ShipmentType(class_name = "Shipment")
    status_shipment = ProjectFields.StatusShipment(class_name = "Shipment")
    order_customer= ProjectFields.OrderCustomerForeignKey(class_name = "Shipment")
    order_market= ProjectFields.OrderMarketForeignKey(class_name = "Shipment")

    # required options
    class Meta:
        verbose_name = _('Shipment')
        verbose_name_plural = _('Shipments')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count

class Contactus(ModelRequiredProperties.ContactusMixin, CoreModelUniversal):
    """
    Product Model.capitalize()
    """
    # """ Fields   """
    firstname = ProjectFields.FirstName(class_name = "Contactus")
    lastname = ProjectFields.LastName(class_name = "Contactus")
    title  = ProjectFields.Title(class_name = "Contactus")
    body = ProjectFields.Body(class_name = "Contactus")
    email = ProjectFields.Email(class_name = "Contactus")

    # required options
    class Meta:
        verbose_name = _('Contactus')
        verbose_name_plural = _('Contactuss')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count
