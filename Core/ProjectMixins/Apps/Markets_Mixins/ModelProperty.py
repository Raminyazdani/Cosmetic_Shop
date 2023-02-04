from Core.managers import BaseManager

# todo do this

class REQUIREDFIELDS:
    MARKET = []
    INVENTORY = []
    INVENTORYITEM = []
    INVENTORYITEMPROPERTY = []
    PROPERTY = []
    ORDERMARKET = []
class SEARCHFIELDS:
    MARKET = []
    INVENTORY = []
    INVENTORYITEM = []
    INVENTORYITEMPROPERTY = []
    PROPERTY = []
    ORDERMARKET = []
class Manager:
    class OBJECTS:
        MARKET = BaseManager()
        INVENTORY = BaseManager()
        INVENTORYITEM = BaseManager()
        INVENTORYITEMPROPERTY = BaseManager()
        PROPERTY = BaseManager()
        ORDERMARKET = BaseManager()

    class SUBSETS:
        MARKET = BaseManager()
        INVENTORY = BaseManager()
        INVENTORYITEM = BaseManager()
        INVENTORYITEMPROPERTY = BaseManager()
        PROPERTY = BaseManager()
        ORDERMARKET = BaseManager()
