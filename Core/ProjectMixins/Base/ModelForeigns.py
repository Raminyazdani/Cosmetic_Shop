from django.utils.functional import cached_property

from Core.utils.ProjectUtils import GetNameSpaceProperty

class Parent:
    class Meta:
        abstract = True

    """
    Brand Mixin
    """

    @cached_property
    def parent_count(self,teststring="parent",scopeparent="self"):
        """
        Return brand count
        :return:
        """
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey
        return GetNameSpaceProperty.count(self, teststring,scopeparent)


    @cached_property
    def parent_name(self,teststring="parent"):
        """
        Return brand count
        :return:
        """
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey

        return GetNameSpaceProperty.parent(self, teststring)
