from django.utils.functional import cached_property

from Core.utils.ProjectUtils import GetNameSpaceProperty

class Brand:
    class Meta:
        abstract = True

    """
    Brand Mixin
    """

    @cached_property
    def brand_count(self,teststring="brand",scopeparent="product"):
        """
        Return brand count
        :return:
        """
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey
        return GetNameSpaceProperty.count(self, teststring,scopeparent)

    @cached_property
    def brand_name(self,teststring="brand",scopeparent="product"):
        """
        Return brand count
        :return:
        """
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey
        return GetNameSpaceProperty.name(self, teststring,scopeparent)

class Category:
    class Meta:
        abstract = True

    """
    Brand Mixin
    """

    @cached_property
    def category_count(self,teststring="category",scopeparent="product"):
        """
        Return brand count
        :return:
        """
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey
        return GetNameSpaceProperty.count(self, teststring,scopeparent)


    @cached_property
    def category_name(self,teststring="category",scopeparent="product"):
        """
        Return brand count
        :return:
        """
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey
        return GetNameSpaceProperty.name(self, teststring,scopeparent)

class Comment:
    class Meta:
        abstract = True

    """
    Brand Mixin
    """

    @cached_property
    def comment_count(self,teststring="comment",scopeparent="product"):
        """
        Return brand count
        :return:
        """
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey
        return GetNameSpaceProperty.count(self, teststring,scopeparent)

    @cached_property
    def comment_name(self,teststring="comment",scopeparent="product"):
        """
        Return brand count
        :return:
        """
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey
        return GetNameSpaceProperty.name(self, teststring,scopeparent)

class Product:
    class Meta:
        abstract = True

    """
    Brand Mixin
    """

    @cached_property
    def product_count(self,teststring="product",scopeparent="product"):
        """
        Return brand count
        :return:
        """
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey
        return GetNameSpaceProperty.count(self, teststring,scopeparent)


    @cached_property
    def product_name(self,teststring="product",scopeparent="product"):
        """
        Return brand count
        :return:
        """
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey
        return GetNameSpaceProperty.name(self, teststring,scopeparent)

class Tag:
    class Meta:
        abstract = True

    """
    Brand Mixin
    """

    @cached_property
    def tag_count(self,teststring="tag",scopeparent="product"):
        """
        Return brand count
        :return:
        """
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey
        return GetNameSpaceProperty.count(self, teststring,scopeparent)

    @cached_property
    def tag_name(self,teststring="tag",scopeparent="product"):
        """
        Return brand count
        :return:
        """
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey
        return GetNameSpaceProperty.name(self, teststring,scopeparent)
