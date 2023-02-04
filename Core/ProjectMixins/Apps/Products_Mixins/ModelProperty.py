from Core.managers import BaseManager

# todo do this

class REQUIREDFIELDS:

    BRAND = ['name']
    CATEGORY = ['name']
    COMMENT = ['product', 'author', 'title', 'body', 'rating']
    PRODUCT = ['name', 'gender']
    TAG = ['name']

class SEARCHFIELDS:
    BRAND = ['name', 'product__name', 'product__category__name', 'product__tag__name', 'product__brand__name']
    CATEGORY = ['name', 'product__name', 'product__category__name', 'product__tag__name', 'product__brand__name', 'parent__name', 'parent__product__name']
    COMMENT = ['title', 'body', 'author__username', 'product__name', 'product__category__name', 'product__tag__name', 'product__brand__name']
    PRODUCT = ['name', 'short_description', 'category__name', 'tag__name', 'brand__name']
    TAG = ['name', 'product__name', 'product__category__name', 'product__tag__name', 'product__brand__name']

class Manager:
    class OBJECTS:
        BRAND = BaseManager()
        CATEGORY = BaseManager()
        COMMENT = BaseManager()
        PRODUCT = BaseManager()
        TAG = BaseManager()

    class SUBSETS:
        BRAND = BaseManager()
        CATEGORY = BaseManager()
        COMMENT = BaseManager()
        PRODUCT = BaseManager()
        TAG = BaseManager()
