# from django.utils.translation import gettext_lazy as _
#
# # Core import
# from Core.ProjectMixins.Shop import ModelProperty, ModelRequiredProperties
# from Core.fields import ProjectFields
# from Core.models import CoreModel, CoreModelUniversal
#
# # Create your models here.
#
#
# class Address(ModelRequiredProperties.Address, CoreModelUniversal):
#     """
#     Address Model
#     """
#     # """ Fields   """
#     ...
#     # GalleryField
#     #   gallery = ProjectField.CustomGalleryField(class_name"Product")
#     # slug field populated by name field
#     ...
#     # required options
#     REQUIRED_FIELDS = ModelProperty.RequiredFields.Address
#     SEARCH_FIELDS = ModelProperty.AdminProperty.Address
#
#     class Meta:
#         verbose_name = _('Address')
#         verbose_name_plural = _('Address')
#         # save methods are implemented in ProjectMixins
#         # save slug field populated by name field and implemented in ProjectMixins
#         # save Base Address implemented in ProjectMixins
#         # Properties are implemented in ProjectMixins including :
#         #
#
# class Coupon(ModelRequiredProperties.Coupon, CoreModelUniversal):
#     """
#     Coupon Model
#     """
#     # """ Fields   """
#     ...
#     # GalleryField
#     #   gallery = ProjectField.CustomGalleryField(class_name"Product")
#     # slug field populated by name field
#     ...
#     # required options
#     REQUIRED_FIELDS = ModelProperty.RequiredFields.Coupon
#     SEARCH_FIELDS = ModelProperty.AdminProperty.Coupon
#
#     class Meta:
#         verbose_name = _('Coupon')
#         verbose_name_plural = _('Coupon')
#         # save methods are implemented in ProjectMixins
#         # save slug field populated by name field and implemented in ProjectMixins
#         # save Base Coupon implemented in ProjectMixins
#         # Properties are implemented in ProjectMixins including :
#         #
#
# class Discount(ModelRequiredProperties.Discount, CoreModelUniversal):
#     """
#     Discount Model
#     """
#     # """ Fields   """
#     ...
#     # GalleryField
#     #   gallery = ProjectField.CustomGalleryField(class_name"Product")
#     # slug field populated by name field
#     ...
#     # required options
#     REQUIRED_FIELDS = ModelProperty.RequiredFields.Discount
#     SEARCH_FIELDS = ModelProperty.AdminProperty.Discount
#
#     class Meta:
#         verbose_name = _('Discount')
#         verbose_name_plural = _('Discount')
#         # save methods are implemented in ProjectMixins
#         # save slug field populated by name field and implemented in ProjectMixins
#         # save Base Discount implemented in ProjectMixins
#         # Properties are implemented in ProjectMixins including :
#         #
#
# class Gallery(ModelRequiredProperties.Gallery, CoreModelUniversal):
#     """
#     Gallery Model
#     """
#     # """ Fields   """
#     ...
#     # GalleryField
#     #   gallery = ProjectField.CustomGalleryField(class_name"Product")
#     # slug field populated by name field
#     ...
#     # required options
#     REQUIRED_FIELDS = ModelProperty.RequiredFields.Gallery
#     SEARCH_FIELDS = ModelProperty.AdminProperty.Gallery
#
#     class Meta:
#         verbose_name = _('Gallery')
#         verbose_name_plural = _('Gallery')
#         # save methods are implemented in ProjectMixins
#         # save slug field populated by name field and implemented in ProjectMixins
#         # save Base Gallery implemented in ProjectMixins
#         # Properties are implemented in ProjectMixins including :
#         #
#
# class Image(ModelRequiredProperties.Image, CoreModelUniversal):
#     """
#     Image Model
#     """
#     # """ Fields   """
#     ...
#     # GalleryField
#     #   gallery = ProjectField.CustomGalleryField(class_name"Product")
#     # slug field populated by name field
#     ...
#     # required options
#     REQUIRED_FIELDS = ModelProperty.RequiredFields.Image
#     SEARCH_FIELDS = ModelProperty.AdminProperty.Image
#
#     class Meta:
#         verbose_name = _('Image')
#         verbose_name_plural = _('Image')
#         # save methods are implemented in ProjectMixins
#         # save slug field populated by name field and implemented in ProjectMixins
#         # save Base Image implemented in ProjectMixins
#         # Properties are implemented in ProjectMixins including :
#         #
#
#
# class Order(ModelRequiredProperties.Order, CoreModelUniversal):
#     """
#     Order Model
#     """
#     # """ Fields   """
#     ...
#     # GalleryField
#     #   gallery = ProjectField.CustomGalleryField(class_name"Product")
#     # slug field populated by name field
#     ...
#     # required options
#     REQUIRED_FIELDS = ModelProperty.RequiredFields.Order
#     SEARCH_FIELDS = ModelProperty.AdminProperty.Order
#
#     class Meta:
#         verbose_name = _('Order')
#         verbose_name_plural = _('Order')
#         # save methods are implemented in ProjectMixins
#         # save slug field populated by name field and implemented in ProjectMixins
#         # save Base Order implemented in ProjectMixins
#         # Properties are implemented in ProjectMixins including :
#         #
#
# class OrderItem(ModelRequiredProperties.OrderItem, CoreModelUniversal):
#     """
#     OrderItem Model
#     """
#     # """ Fields   """
#     ...
#     # GalleryField
#     #   gallery = ProjectField.CustomGalleryField(class_name"Product")
#     # slug field populated by name field
#     ...
#     # required options
#     REQUIRED_FIELDS = ModelProperty.RequiredFields.OrderItem
#     SEARCH_FIELDS = ModelProperty.AdminProperty.OrderItem
#
#     class Meta:
#         verbose_name = _('OrderItem')
#         verbose_name_plural = _('OrderItem')
#         # save methods are implemented in ProjectMixins
#         # save slug field populated by name field and implemented in ProjectMixins
#         # save Base OrderItem implemented in ProjectMixins
#         # Properties are implemented in ProjectMixins including :
#         #
#
# class Payment(ModelRequiredProperties.Payment, CoreModelUniversal):
#     """
#     Payment Model
#     """
#     # """ Fields   """
#     ...
#     # GalleryField
#     #   gallery = ProjectField.CustomGalleryField(class_name"Product")
#     # slug field populated by name field
#     ...
#     # required options
#     REQUIRED_FIELDS = ModelProperty.RequiredFields.Payment
#     SEARCH_FIELDS = ModelProperty.AdminProperty.Payment
#
#     class Meta:
#         verbose_name = _('Payment')
#         verbose_name_plural = _('Payment')
#         # save methods are implemented in ProjectMixins
#         # save slug field populated by name field and implemented in ProjectMixins
#         # save Base Payment implemented in ProjectMixins
#         # Properties are implemented in ProjectMixins including :
#         #
#
# class Wallet(ModelRequiredProperties.Wallet, CoreModelUniversal):
#     """
#     Wallet Model
#     """
#     # """ Fields   """
#     ...
#     # GalleryField
#     #   gallery = ProjectField.CustomGalleryField(class_name"Product")
#     # slug field populated by name field
#     ...
#     # required options
#     REQUIRED_FIELDS = ModelProperty.RequiredFields.Wallet
#     SEARCH_FIELDS = ModelProperty.AdminProperty.Wallet
#
#     class Meta:
#         verbose_name = _('Wallet')
#         verbose_name_plural = _('Wallet')
#         # save methods are implemented in ProjectMixins
#         # save slug field populated by name field and implemented in ProjectMixins
#         # save Base Wallet implemented in ProjectMixins
#         # Properties are implemented in ProjectMixins including :
#         #
#
# class Shipment(ModelRequiredProperties.Shipment, CoreModelUniversal):
#     """
#     Shipment Model
#     """
#     # """ Fields   """
#     ...
#     # GalleryField
#     #   gallery = ProjectField.CustomGalleryField(class_name"Product")
#     # slug field populated by name field
#     ...
#     # required options
#     REQUIRED_FIELDS = ModelProperty.RequiredFields.Shipment
#     SEARCH_FIELDS = ModelProperty.AdminProperty.Shipment
#
#     class Meta:
#         verbose_name = _('Shipment')
#         verbose_name_plural = _('Shipment')
#         # save methods are implemented in ProjectMixins
#         # save slug field populated by name field and implemented in ProjectMixins
#         # save Base Shipment implemented in ProjectMixins
#         # Properties are implemented in ProjectMixins including :
#         #
#
# class ContactUs(ModelRequiredProperties.ContactUs, CoreModelUniversal):
#     """
#     ContactUs Model
#     """
#     # """ Fields   """
#     ...
#     # GalleryField
#     #   gallery = ProjectField.CustomGalleryField(class_name"Product")
#     # slug field populated by name field
#     ...
#     # required options
#     REQUIRED_FIELDS = ModelProperty.RequiredFields.ContactUs
#     SEARCH_FIELDS = ModelProperty.AdminProperty.ContactUs
#
#     class Meta:
#         verbose_name = _('ContactUs')
#         verbose_name_plural = _('ContactUs')
#         # save methods are implemented in ProjectMixins
#         # save slug field populated by name field and implemented in ProjectMixins
#         # save Base ContactUs implemented in ProjectMixins
#         # Properties are implemented in ProjectMixins including :
#         #
#
