from django.utils.text import slugify

class SaveNormal:
    class Meta:
        abstract = True

    """
    Product Mixin
    """

    def save(self, *args, **kwargs):
        """
        Save product model Base
        :param args:
        :param kwargs:
        :return:
        """
        super().save(*args, **kwargs)

class SaveId:
    class Meta:
        abstract = True

    """
    Slug Mixin for id field
    """

    def save(self, *args, **kwargs):
        """
        Save slug field with id field
        :param args:
        :param kwargs:
        :return:
        """
        slug = slugify(self.id)
        self.slug = slug
        super().save(*args, **kwargs)

class SaveName:
    class Meta:
        abstract = True

    """
    Slug Mixin for name field
    """

    def save(self: object, *args, **kwargs):
        """
        Save slug field with name field
        :param args:
        :param kwargs:
        :return:
        """
        slug = slugify(self.name)
        self.slug = slug
        super().save(*args, **kwargs)

class SaveParent:
    class Meta:
        abstract = True

    """
    Slug Mixin for category field
    """

    def save(self: object, *args, **kwargs):
        """
        Save slug field with category field and parents
        :param args:
        :param kwargs:
        :return:
        """
        if self.id and self.parent and (self.id == self.parent):
            self.parent = None
        if self.pk is None:
            super().save(*args, **kwargs)
        slug = self.parent_name + [self.slug]
        print(self.parent_name)
        self.slug = "/".join(slug).lower()
        print(self.slug)
        self.save()

class SaveProduct:
    class Meta:
        abstract = True

    """
    Product Mixin with category parents saving
    """

    def save(self, *args, **kwargs):
        """
        Save product model with categories parents
        :param args:
        :param kwargs:
        :return:
        """
        if self.pk is None:
            super().save(*args, **kwargs)
        categories = self.category.all()
        categories_id = [x for x in categories.values_list('id', flat = True)]
        for category in categories:
            category_temp = category
            while category_temp.parent:
                category_temp = category_temp.parent
                categories_id.append(category_temp)
        categories_id = list(set(categories_id))
        print(categories_id)
        self.category.set(categories_id)
        super().save(*args, **kwargs)
<<<<<<< Updated upstream
