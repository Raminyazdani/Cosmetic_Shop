

import re
from django.contrib.contenttypes import fields
from django.db import models
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField
from django.contrib.contenttypes.models import ContentType

from Core.utils.ProjectUtils import CustomStringMaker, CustomValidators, kwargs_setter
from Core.fields import DefaultFields
from Core.fields.FieldClassBases import Base, DelClassName

class ContentTypes(Base,models.ForeignKey):

    class Meta:
        abstract = True

    

    class_custom_default_attrs = {
    "class_name": "Model",
    "field_name": "ContentTypes",
    "blank": True,
    "db_index": True,
    "default":None,
    "null": True,
    "on_delete": models.SET_NULL,
    "related_name": CustomStringMaker.ContentType.related_name_gen,
    "to": ContentType,
    }
    
    def __init__(self, *args, **kwargs):
        deleters = []
        class_attrs = ContentTypes.class_custom_default_attrs
    


        kwargs = kwargs_setter(kwargs, class_attrs, deleters)
        super().__init__(*args, **kwargs)
    