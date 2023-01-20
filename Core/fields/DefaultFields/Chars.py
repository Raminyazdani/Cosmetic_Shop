

import re
from django.contrib.contenttypes import fields
from django.db import models
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField
from Core.utils.ProjectUtils import CustomStringMaker, CustomValidators, kwargs_setter
from Core.fields import DefaultFields
from Core.fields.FieldClassBases import Base, DelClassName

class Chars(Base,models.CharField):

    class Meta:
        abstract = True

    

    class_custom_default_attrs = {
    "class_name": "Model",
    "field_name": "Chars",
    "blank": True,
    "db_index": False,
    "max_length": 30,
    "null": True,
    "unique": False,
    }
    
    def __init__(self, *args, **kwargs):
        deleters = []
        class_attrs = Chars.class_custom_default_attrs
    


        kwargs = kwargs_setter(kwargs, class_attrs, deleters)
        super().__init__(*args, **kwargs)
    