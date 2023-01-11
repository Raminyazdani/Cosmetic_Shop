class ID:
    class Meta:
        abstract = True

    """
    Str Mixin for id field
    """

    def __str__(self:object):
        """
        Return id field
        :return:  id field
        """
        return self.id

class Name:
    class Meta:
        abstract = True

    """
    Str Mixin for name field
    """

    def __str__(self:object):
        """
        Return name field
        :return:  name field
        """
        return self.name

class PhoneNumber:
    class Meta:
        abstract = True

    """
    Str Mixin for title field
    """

    def __str__(self):
        """
        Return title field
        :return:  title field
        """
        return self.phone_number

class Title:
    class Meta:
        abstract = True

    """
    Str Mixin for title field
    """

    def __str__(self:object):
        """
        Return title field
        :return:  title field
        """
        return self.title
