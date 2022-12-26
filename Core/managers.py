from django.db import models


class BaseManager(models.Manager):
    """
    base manager for all models in project
    """

    def get_queryset(self):
        """
        return all objects that is not deleted
        :return:
        """
        return super().get_queryset().filter(is_delete=False)

    def get_all(self):
        """
        return all objects including deleted objects
        :return:
        """
        return super().get_queryset()

    def get_deleted(self):
        """
        return all deleted objects
        :return:
        """
        return super().get_queryset().filter(is_delete=True)

    def delete(self):
        """
        soft delete objects
        :return:
        """
        return self.update(is_delete=True)

    def restore(self):
        """
        restore soft deleted objects
        :return:
        """
        return self.update(is_delete=False)

    def hard_delete(self):
        """
        hard delete objects
        :return:
        """
        return super().get_queryset().delete()

    
