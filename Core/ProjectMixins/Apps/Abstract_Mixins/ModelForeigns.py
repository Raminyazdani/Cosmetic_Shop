from django.utils.functional import cached_property

from Core.utils.ProjectUtils import GetNameSpaceProperty

# MODEL_NAME
# LOWER

class MODEL_NAME:
    class Meta:
        abstract = True

    """
    MODEL_NAME Mixin
    """

    @cached_property
    def LOWER_count(self,teststring="LOWER",scopeparent="SCOUPEPARENT"):
        """
        Return brand count
        :return:
        """
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey
        return GetNameSpaceProperty.count(self, "LOWER","SCOPEPARENT")

    @cached_property
    def LOWER_name(self,teststring="LOWER",scopeparent="SCOUPEPARENT"):
        """
        Return brand count
        :return:
        """
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey
        return GetNameSpaceProperty.name(self, "LOWER","SCOPEPARENT")
