from Core.managers import BaseManager

# todo do this

class REQUIREDFIELDS:
    ADDRESS = []
    COUPON = []
    DISCOUNT = []
    GALLERY = []
    IMAGE = []
    GALLERYIMAGE = []
    ORDER = []
    ORDERITEM = []
    PAYMENT = []
    WALLET = []
    SHIPMENT = []
    CONTACTUS = []
class SEARCHFIELDS:
    ADDRESS = []
    COUPON = []
    DISCOUNT = []
    GALLERY = []
    IMAGE = []
    GALLERYIMAGE = []
    ORDER = []
    ORDERITEM = []
    PAYMENT = []
    WALLET = []
    SHIPMENT = []
    CONTACTUS = []
class Manager:
    class OBJECTS:
        ADDRESS = BaseManager()
        COUPON = BaseManager()
        DISCOUNT = BaseManager()
        GALLERY = BaseManager()
        IMAGE = BaseManager()
        GALLERYIMAGE = BaseManager()
        ORDER = BaseManager()
        ORDERITEM = BaseManager()
        PAYMENT = BaseManager()
        WALLET = BaseManager()
        SHIPMENT = BaseManager()
        CONTACTUS = BaseManager()

    class SUBSETS:
        ADDRESS = BaseManager()
        COUPON = BaseManager()
        DISCOUNT = BaseManager()
        GALLERY = BaseManager()
        IMAGE = BaseManager()
        GALLERYIMAGE = BaseManager()
        ORDER = BaseManager()
        ORDERITEM = BaseManager()
        PAYMENT = BaseManager()
        WALLET = BaseManager()
        SHIPMENT = BaseManager()
        CONTACTUS = BaseManager()