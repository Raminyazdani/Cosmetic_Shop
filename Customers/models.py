
from django.utils.translation import gettext_lazy as _
from Core.ProjectMixins.Apps.Customers_Mixins import ModelRequiredProperties
from Core.fields import ProjectFields

from Core.fields import ProjectFields
from Core.models import CoreModelUniversal


# Create your models here.

class Customer(ModelRequiredProperties.CustomerMixin,CoreModelUniversal ):
    """
    Product Model.capitalize()
    """
    # """ Fields   """

    firstname = ProjectFields.FirstName(class_name = "Customer")
    lastname = ProjectFields.LastName(class_name = "Customer")
    user_name = ProjectFields.UserName(class_name = "Customer")
    slug = ProjectFields.Slug(class_name = "Customer")
    gender = ProjectFields.Gender(class_name = "Customer")
    email = ProjectFields.Email(class_name = "Customer")
    bio = ProjectFields.Bio(class_name = "Customer")

    gallery = ProjectFields.GalleryGenericRelation(class_name = "Customer")
    comments = ProjectFields.CommentForeignKey(class_name = "Customer")
    user = ProjectFields.UserForeignKey(class_name = "Customer")
    wish_list = ProjectFields.WishListForeignKey(class_name = "Customer")
    wallet = ProjectFields.WalletGenericRelation(class_name = "Customer")
    address = ProjectFields.AddressGenericRelation(class_name = "Customer")
    favorite = ProjectFields.FavoriteForeignKey(class_name = "Customer")
    cart = ProjectFields.CartForeignKey(class_name = "Customer")
    coupon = ProjectFields.CouponManyToMany(class_name = "Customer")
    order_customer = ProjectFields.OrderCustomerForeignKey(class_name = "Customer")

    # required options

    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count


class Cart(ModelRequiredProperties.CartMixin,CoreModelUniversal ):
    """
    Product Model.capitalize()
    """
    # """ Fields   """
    cart_item = ProjectFields.CartItemForeignKey(class_name = "Cart")
    customer = ProjectFields.CustomerForeignKey(class_name = "Cart")
    # required options

    class Meta:
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count


class CartItem(ModelRequiredProperties.CartItemMixin, CoreModelUniversal):
    """
    Product Model.capitalize()
    """
    # """ Fields   """
    cart = ProjectFields.CartForeignKey(class_name = "CartItem")
    inventory_item = ProjectFields.InventoryItemForeignKey(class_name = "CartItem")
    # required options

    class Meta:
        verbose_name = _('Cartitem')
        verbose_name_plural = _('Cartitems')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count


class CustomerCoupon(ModelRequiredProperties.CustomerCouponMixin, CoreModelUniversal):
    """
    Product Model.capitalize()
    """
    # """ Fields   """
    is_used = ProjectFields.IsUsed(class_name = "CustomerCoupon")

    customer_id = ProjectFields.CustomerForeignKey(class_name = "CustomerCoupon")
    coupon_id = ProjectFields.CouponForeignKey(class_name = "CustomerCoupon")
    # required options

    class Meta:
        verbose_name = _('Customercoupon')
        verbose_name_plural = _('Customercoupons')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count

class Coupon(ModelRequiredProperties.CouponMixin, CoreModelUniversal):
    """
    Product Model.capitalize()
    """
    # """ Fields   """
    date_from = ProjectFields.DateFrom(class_name = "Coupon")
    date_to = ProjectFields.DateTo(class_name = "Coupon")
    code = ProjectFields.Code(class_name = "Coupon")
    coupon_type = ProjectFields.CouponType(class_name = "Coupon")
    minimum_amount = ProjectFields.MinimumAmount(class_name = "Coupon")
    maximum_amount = ProjectFields.MaximumAmount(class_name = "Coupon")
    percentage = ProjectFields.Percentage(class_name = "Coupon")
    is_tax_free = ProjectFields.IsTaxFree(class_name = "Coupon")
    is_shipping_free = ProjectFields.IsShippingFree(class_name = "Coupon")
    customer= ProjectFields.CustomerManyToMany(class_name = "Coupon")

    # required options
    class Meta:
        verbose_name = _('Coupon')
        verbose_name_plural = _('Coupons')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count

class Favorite(ModelRequiredProperties.FavoriteMixin,CoreModelUniversal ):
    """
    Product Model.capitalize()
    """
    # """ Fields   """
    customer = ProjectFields.CustomerForeignKey(class_name = "Favorite")
    favorite_item = ProjectFields.FavoriteItemForeignKey(class_name = "Favorite")
    # required options

    class Meta:
        verbose_name = _('Favorite')
        verbose_name_plural = _('Favorites')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count


class FavoriteItem(ModelRequiredProperties.FavoriteitemMixin, CoreModelUniversal):
    """
    Product Model.capitalize()
    """
    # """ Fields   """
    favorite = ProjectFields.FavoriteForeignKey(class_name = "FavoriteItem")
    product = ProjectFields.ProductForeignKey(class_name = "FavoriteItem")
    # required options

    class Meta:
        verbose_name = _('FavoriteItem')
        verbose_name_plural = _('FavoriteItems')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count


class OrderCustomer(ModelRequiredProperties.OrdercustomerMixin,CoreModelUniversal ):
    """
    Product Model.capitalize()
    """
    # """ Fields   """
    Status_order = ProjectFields.StatusOrder(class_name = "OrderCustomer")
    total_price = ProjectFields.TotalPrice(class_name = "OrderCustomer")
    tax = ProjectFields.Tax(class_name = "OrderCustomer")
    discounted_price = ProjectFields.DiscountedPrice(class_name = "OrderCustomer")
    final_price = ProjectFields.FinalPrice(class_name = "OrderCustomer")

    order = ProjectFields.OrderForeignKey(class_name = "OrderCustomer")
    order_item = ProjectFields.OrderItemForeignKey(class_name = "OrderCustomer")
    shipment = ProjectFields.ShipmentForeignKey(class_name = "OrderCustomer")
    payment = ProjectFields.PaymentGenericRelation(class_name = "OrderCustomer")
    coupon = ProjectFields.CouponForeignKey(class_name = "OrderCustomer")
    customer = ProjectFields.CustomerForeignKey(class_name = "OrderCustomer")

    # required options

    class Meta:
        verbose_name = _('OrderCustomer')
        verbose_name_plural = _('OrderCustomers')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count


class Wishlist(ModelRequiredProperties.WishlistMixin,CoreModelUniversal ):
    """
    Product Model.capitalize()
    """
    # """ Fields   """

    wish_list_item = ProjectFields.WishListItemForeignKey(class_name = "Wishlist")
    customer = ProjectFields.CustomerForeignKey(class_name = "Wishlist")
    # required options

    class Meta:
        verbose_name = _('Wishlist')
        verbose_name_plural = _('Wishlists')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count


class Wishlistitem(ModelRequiredProperties.WishlistitemMixin,CoreModelUniversal ):
    """
    Product Model.capitalize()
    """
    # """ Fields   """

    wish_list = ProjectFields.WishListForeignKey(class_name = "WishListItem")
    product = ProjectFields.ProductForeignKey(class_name = "WishListItem")

    # required options

    class Meta:
        verbose_name = _('Wishlistitem')
        verbose_name_plural = _('Wishlistitems')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count

