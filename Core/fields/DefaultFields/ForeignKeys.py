

import re
from django.contrib.contenttypes import fields
from django.db import models
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField
from Core.utils.ProjectUtils import CustomStringMaker, CustomValidators, kwargs_setter
from Core.fields import DefaultFields
from Core.fields.FieldClassBases import Base, DelClassName

class ForeignKeys(Base,models.ForeignKey):

    class Meta:
        abstract = True

    

    class_custom_default_attrs = {
    "class_name": "Model",
    "field_name": "ForeignKeys",
    "blank": True,
    "db_index": True,
    "null": True,
    "on_delete": models.SET_NULL,
    "related_name": CustomStringMaker.ForeignKey.related_name_gen,
    "to": CustomStringMaker.ForeignKey.to_gen,
    }
    
    def __init__(self, *args, **kwargs):
        deleters = ['app_name_destination', 'app_name_model_destination']
        class_attrs = ForeignKeys.class_custom_default_attrs
    


        kwargs = kwargs_setter(kwargs, class_attrs, deleters)
        super().__init__(*args, **kwargs)
    