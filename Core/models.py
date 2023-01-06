from django.db import models
from Core.managers import BaseManager
from Core.fields import ProjectField
from django.db import models


class CoreModel(models.Model):
    """
    Core Model

    """
    id = ProjectField.CustomIdField()

    class Meta:
        abstract = True


class CoreModelUniversal(CoreModel):
    """
    Core Model Universal with universal fields and managers
    """
    is_delete = ProjectField.CustomIsDeletedField()
    created_at = ProjectField.CustomCreatedAtField()
    modified_at = ProjectField.CustomModifiedAtField()

    objects = BaseManager()
    subset = BaseManager()

    class Meta:
        abstract = True



