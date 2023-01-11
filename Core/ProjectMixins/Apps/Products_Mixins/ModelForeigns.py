from django.utils.functional import cached_property

from Core.utils.ProjectUtils import GetNameSpaceProperty

class Brand:
    class Meta:
        abstract = True

    """
    Brand Mixin
    """

    @cached_property
<<<<<<< Updated upstream
    def brand_count(self,teststring="brand",scopeparent="product"):
=======
    def brand_count(self):
>>>>>>> Stashed changes
        """
        Return brand count
        :return:
        """
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey
<<<<<<< Updated upstream
        return GetNameSpaceProperty.count(self, teststring,scopeparent)

    @cached_property
    def brand_name(self,teststring="brand",scopeparent="product"):
=======
        return GetNameSpaceProperty.count(self, "brand")

    @cached_property
    def brand_name(self):
>>>>>>> Stashed changes
        """
        Return brand count
        :return:
        """
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey
<<<<<<< Updated upstream
        return GetNameSpaceProperty.name(self, teststring,scopeparent)
=======
        return GetNameSpaceProperty.name(self, "brand")
>>>>>>> Stashed changes

class Category:
    class Meta:
        abstract = True

    """
    Brand Mixin
    """

    @cached_property
<<<<<<< Updated upstream
    def category_count(self,teststring="category",scopeparent="product"):
=======
    def category_count(self):
>>>>>>> Stashed changes
        """
        Return brand count
        :return:
        """
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey
<<<<<<< Updated upstream
        return GetNameSpaceProperty.count(self, teststring,scopeparent)


    @cached_property
    def category_name(self,teststring="category",scopeparent="product"):
=======
        return GetNameSpaceProperty.count(self, "category")


    @cached_property
    def category_name(self):
>>>>>>> Stashed changes
        """
        Return brand count
        :return:
        """
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey
<<<<<<< Updated upstream
        return GetNameSpaceProperty.name(self, teststring,scopeparent)
=======
        return GetNameSpaceProperty.name(self, "category")
class Parent:
    class Meta:
        abstract = True

    """
    Brand Mixin
    """

    @cached_property
    def parent_count(self):
        """
        Return brand count
        :return:
        """
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey
        return GetNameSpaceProperty.count(self, "category")


    @cached_property
    def parent_name(self):
        """
        Return brand count
        :return:
        """
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey
        return GetNameSpaceProperty.name(self, "parent")

>>>>>>> Stashed changes

class Comment:
    class Meta:
        abstract = True

    """
    Brand Mixin
    """

    @cached_property
<<<<<<< Updated upstream
    def comment_count(self,teststring="comment",scopeparent="product"):
=======
    def comment_count(self):
>>>>>>> Stashed changes
        """
        Return brand count
        :return:
        """
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey
<<<<<<< Updated upstream
        return GetNameSpaceProperty.count(self, teststring,scopeparent)

    @cached_property
    def comment_name(self,teststring="comment",scopeparent="product"):
=======
        return GetNameSpaceProperty.count(self, "comment")

    @cached_property
    def comment_name(self):
>>>>>>> Stashed changes
        """
        Return brand count
        :return:
        """
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey
<<<<<<< Updated upstream
        return GetNameSpaceProperty.name(self, teststring,scopeparent)
=======
        return GetNameSpaceProperty.name(self, "comment")
>>>>>>> Stashed changes

class Product:
    class Meta:
        abstract = True

    """
    Brand Mixin
    """

    @cached_property
<<<<<<< Updated upstream
    def product_count(self,teststring="product",scopeparent="product"):
=======
    def product_count(self):
>>>>>>> Stashed changes
        """
        Return brand count
        :return:
        """
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey
<<<<<<< Updated upstream
        return GetNameSpaceProperty.count(self, teststring,scopeparent)


    @cached_property
    def product_name(self,teststring="product",scopeparent="product"):
=======
        return GetNameSpaceProperty.count(self, "product")


    @cached_property
    def product_name(self):
>>>>>>> Stashed changes
        """
        Return brand count
        :return:
        """
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey
<<<<<<< Updated upstream
        return GetNameSpaceProperty.name(self, teststring,scopeparent)
=======
        return GetNameSpaceProperty.name(self, "product")
>>>>>>> Stashed changes

class Tag:
    class Meta:
        abstract = True

    """
    Brand Mixin
    """

    @cached_property
<<<<<<< Updated upstream
    def tag_count(self,teststring="tag",scopeparent="product"):
=======
    def tag_count(self):
>>>>>>> Stashed changes
        """
        Return brand count
        :return:
        """
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey
<<<<<<< Updated upstream
        return GetNameSpaceProperty.count(self, teststring,scopeparent)

    @cached_property
    def tag_name(self,teststring="tag",scopeparent="product"):
=======
        return GetNameSpaceProperty.count(self, "tag")

    @cached_property
    def tag_name(self):
>>>>>>> Stashed changes
        """
        Return brand count
        :return:
        """
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey
<<<<<<< Updated upstream
        return GetNameSpaceProperty.name(self, teststring,scopeparent)
=======
        return GetNameSpaceProperty.name(self, "tag")
>>>>>>> Stashed changes
