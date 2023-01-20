from django.db import models

from Core.managers import BaseManager
from Core.fields import ProjectFields
from django.db import models


class CoreModel(models.Model):
    """
    Core Model

    """
    id = ProjectFields.Id()

    class Meta:
        abstract = True


class CoreModelUniversal(CoreModel):
    """
    Core Model Universal with universal fields and managers
    """
    is_delete = ProjectFields.IsDelete()
    created_at = ProjectFields.CreatedAt()
    modified_at = ProjectFields.ModifiedAt()

    objects = BaseManager()
    subset = BaseManager()

    class Meta:
        abstract = True



