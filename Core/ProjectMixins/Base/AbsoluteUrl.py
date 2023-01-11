from Core.utils.ProjectUtils import GetNameSpaceProperty

class UrlPhone:
    class Meta:
        abstract = True

    """
    Slug Mixin
    """

    def get_absolute_url(self:object):
        """
        Return absolute url
        :return:
        """
        return GetNameSpaceProperty.abs_url_phone(self, self.__name__.lower())

class UrlName:
    class Meta:
        abstract = True

    """
    Slug Mixin
    """

    def get_absolute_url(self:object):
        """
        Return absolute url
        :return:
        """
        return GetNameSpaceProperty.abs_url_slug(self, self.__name__.lower())

class UrlId:
    class Meta:
        abstract = True

    """
    Slug Mixin
    """

    def get_absolute_url(self:object):
        """
        Return absolute url
        :return:
        """
        return GetNameSpaceProperty.abs_url_id(self, self.__name__.lower())
