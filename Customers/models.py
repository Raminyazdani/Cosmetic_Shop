
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


    # required options

    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count


class Cart(ModelRequiredProperties.CartMixin,CoreModelUniversal ):
    """
    Product Model.capitalize()
    """
    # """ Fields   """


    # required options

    class Meta:
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count


class Cartitem(ModelRequiredProperties.CartitemMixin,CoreModelUniversal ):
    """
    Product Model.capitalize()
    """
    # """ Fields   """


    # required options

    class Meta:
        verbose_name = _('Cartitem')
        verbose_name_plural = _('Cartitems')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count


class Customercoupon(ModelRequiredProperties.CustomercouponMixin,CoreModelUniversal ):
    """
    Product Model.capitalize()
    """
    # """ Fields   """


    # required options

    class Meta:
        verbose_name = _('Customercoupon')
        verbose_name_plural = _('Customercoupons')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count


class Favorite(ModelRequiredProperties.FavoriteMixin,CoreModelUniversal ):
    """
    Product Model.capitalize()
    """
    # """ Fields   """


    # required options

    class Meta:
        verbose_name = _('Favorite')
        verbose_name_plural = _('Favorites')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count


class Favoriteitem(ModelRequiredProperties.FavoriteitemMixin,CoreModelUniversal ):
    """
    Product Model.capitalize()
    """
    # """ Fields   """


    # required options

    class Meta:
        verbose_name = _('Favoriteitem')
        verbose_name_plural = _('Favoriteitems')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count


class Ordercustomer(ModelRequiredProperties.OrdercustomerMixin,CoreModelUniversal ):
    """
    Product Model.capitalize()
    """
    # """ Fields   """


    # required options

    class Meta:
        verbose_name = _('Ordercustomer')
        verbose_name_plural = _('Ordercustomers')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count


class Wishlist(ModelRequiredProperties.WishlistMixin,CoreModelUniversal ):
    """
    Product Model.capitalize()
    """
    # """ Fields   """


    # required options

    class Meta:
        verbose_name = _('Wishlist')
        verbose_name_plural = _('Wishlists')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count


class Wishlistitem(ModelRequiredProperties.WishlistitemMixin,CoreModelUniversal ):
    """
    Product Model.capitalize()
    """
    # """ Fields   """


    # required options

    class Meta:
        verbose_name = _('Wishlistitem')
        verbose_name_plural = _('Wishlistitems')  # save methods are implemented in ProjectMixins  # save slug field populated by name field and implemented in ProjectMixins  # save Base Product implemented in ProjectMixins  # Properties are implemented in ProjectMixins including :  #   tag_count ,tag_names , category_count , brand_count , tag_names , category_names , brand_names , comment_count

