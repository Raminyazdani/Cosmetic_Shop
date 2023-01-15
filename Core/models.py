from django.db import models

import Core.fields.BoleanFields
import Core.fields.DateFields
import Core.fields.IdFields
from Core.managers import BaseManager
from Core.fields import ProjectFields
from django.db import models


class CoreModel(models.Model):
    """
    Core Model

    """
    id = ProjectFields.CustomIdField()

    class Meta:
        abstract = True


class CoreModelUniversal(CoreModel):
    """
    Core Model Universal with universal fields and managers
    """
    is_delete = ProjectFields.CustomIsDeletedField()
    created_at = ProjectFields.CustomCreatedAtField()
    modified_at = ProjectFields.CustomModifiedAtField()

    objects = BaseManager()
    subset = BaseManager()

    class Meta:
        abstract = True



