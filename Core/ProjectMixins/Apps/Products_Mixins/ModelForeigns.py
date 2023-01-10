from django.utils.functional import cached_property

from Core.utils.ProjectUtils import GetNameSpaceProperty

class Brand:
    class Meta:
        abstract = True

    """
    Brand Mixin
    """

    @cached_property
    def brand_count(self):
        """
        Return brand count
        :return:
        """
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey
        return GetNameSpaceProperty.count(self, "brand")

    @cached_property
    def brand_name(self):
        """
        Return brand count
        :return:
        """
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey
        return GetNameSpaceProperty.name(self, "brand")

class Category:
    class Meta:
        abstract = True

    """
    Brand Mixin
    """

    @cached_property
    def category_count(self):
        """
        Return brand count
        :return:
        """
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey
        return GetNameSpaceProperty.count(self, "category")


    @cached_property
    def category_name(self):
        """
        Return brand count
        :return:
        """
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey
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
        parent_list = []
        cat = self
        while cat.parent:
            parent_list.append(cat.parent.name)
            cat = cat.parent
        if len(parent_list) > 0:
            return parent_list
        return []

class Comment:
    class Meta:
        abstract = True

    """
    Brand Mixin
    """

    @cached_property
    def comment_count(self):
        """
        Return brand count
        :return:
        """
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey
        return GetNameSpaceProperty.count(self, "comment")

    @cached_property
    def comment_name(self):
        """
        Return brand count
        :return:
        """
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey
        return GetNameSpaceProperty.name(self, "comment")

class Product:
    class Meta:
        abstract = True

    """
    Brand Mixin
    """

    @cached_property
    def product_count(self):
        """
        Return brand count
        :return:
        """
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey
        return GetNameSpaceProperty.count(self, "product")


    @cached_property
    def product_name(self):
        """
        Return brand count
        :return:
        """
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey
        return GetNameSpaceProperty.name(self, "product")

class Tag:
    class Meta:
        abstract = True

    """
    Brand Mixin
    """

    @cached_property
    def tag_count(self):
        """
        Return brand count
        :return:
        """
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey
        return GetNameSpaceProperty.count(self, "tag")

    @cached_property
    def tag_name(self):
        """
        Return brand count
        :return:
        """
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey
        return GetNameSpaceProperty.name(self, "tag")
