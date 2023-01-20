

import re
from django.contrib.contenttypes import fields
from django.db import models
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField
from Core.utils.ProjectUtils import CustomStringMaker, CustomValidators, kwargs_setter
from Core.fields import DefaultFields
from Core.fields.FieldClassBases import Base, DelClassName

class Decimals(Base,models.DecimalField):

    class Meta:
        abstract = True

    

    class_custom_default_attrs = {
    "class_name": "Model",
    "field_name": "Decimals",
    "blank": False,
    "db_index": True,
    "decimal_places": 2,
    "default": 0.0,
    "max_digits": 10,
    "null": False,
    }
    
    def __init__(self, *args, **kwargs):
        deleters = []
        class_attrs = Decimals.class_custom_default_attrs
    


        kwargs = kwargs_setter(kwargs, class_attrs, deleters)
        super().__init__(*args, **kwargs)
    