from Core.managers import BaseManager

# todo do this

class REQUIREDFIELDS:
    CUSTOMER = []
    CART = []
    CARTITEM = []
    COUPON= []
    CUSTOMERCOUPON = []
    FAVORITE = []
    FAVORITEITEM = []
    ORDERCUSTOMER = []
    WISHLIST = []
    WISHLISTITEM = []
class SEARCHFIELDS:
    CUSTOMER = []
    CART = []
    CARTITEM = []
    COUPON= []
    CUSTOMERCOUPON = []
    FAVORITE = []
    FAVORITEITEM = []
    ORDERCUSTOMER = []
    WISHLIST = []
    WISHLISTITEM = []
class Manager:
    class OBJECTS:
        CUSTOMER = BaseManager()
        CART = BaseManager()
        CARTITEM = BaseManager()
        COUPON = BaseManager()
        CUSTOMERCOUPON = BaseManager()
        FAVORITE = BaseManager()
        FAVORITEITEM = BaseManager()
        ORDERCUSTOMER = BaseManager()
        WISHLIST = BaseManager()
        WISHLISTITEM = BaseManager()

    class SUBSETS:
        CUSTOMER = BaseManager()
        CART = BaseManager()
        CARTITEM = BaseManager()
        COUPON = BaseManager()
        CUSTOMERCOUPON = BaseManager()
        FAVORITE = BaseManager()
        FAVORITEITEM = BaseManager()
        ORDERCUSTOMER = BaseManager()
        WISHLIST = BaseManager()
        WISHLISTITEM = BaseManager()
