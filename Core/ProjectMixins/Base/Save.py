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
        parents = [slugify(parent) for parent in self.parent_name[::-1]]
        slug = parents + [self.slug]
        self.slug = "/".join(slug).lower()
        super().save(*args, **kwargs)
        if self.child is not None:
            childs = UpdateChilds.update_childs(self)
            for child in childs:
                child.save()


class UpdateChilds:
    class Meta:
        abstract=True
    @staticmethod
    def update_childs(object):
        """
        Update childs
        :return:
        """
        result = []
        if object.child is not None:
            for child in object.child.all():
                result.append(child)
                temp = UpdateChilds.update_childs(child)
                for item in temp:
                    result.append(item)
        return result
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
        self.category.set(categories_id)
        super().save(*args, **kwargs)

class SaveCategory:
    class Meta:
        abstract = True

    """
    Product Mixin with category parents saving
    """

    def save(self:object, *args, **kwargs):
        """
        Save product model with categories parents
        :param args:
        :param kwargs:
        :return:
        """
        if self.id and self.parent :
            if self.id == self.parent.id:
                self.parent = None
        if self.pk is None:
            super().save(*args, **kwargs)
        super().save(*args, **kwargs)
