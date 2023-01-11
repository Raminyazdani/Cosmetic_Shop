from django.utils.functional import cached_property

from Core.utils.ProjectUtils import GetNameSpaceProperty

# User
# user
# user
class User:
    class Meta:
        abstract = True

    """
    User Mixin
    """

    @cached_property
    def user_count(self,teststring="user",scopeparent="user"):
        """
        Return brand count
        :return:
        """
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey
        return GetNameSpaceProperty.count(self, "user","SCOPEPARENT")

    @cached_property
    def user_name(self,teststring="user",scopeparent="user"):
        """
        Return brand count
        :return:
        """
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey
        return GetNameSpaceProperty.name(self, "user","SCOPEPARENT")
