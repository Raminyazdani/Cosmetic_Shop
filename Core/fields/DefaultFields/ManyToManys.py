

import re
from django.contrib.contenttypes import fields
from django.db import models
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField
from Core.utils.ProjectUtils import CustomStringMaker, CustomValidators, kwargs_setter
from Core.fields import DefaultFields
from Core.fields.FieldClassBases import Base, DelClassName

class ManyToManys(Base,models.ManyToManyField):

    class Meta:
        abstract = True

    

    class_custom_default_attrs = {
    "class_name": "Model",
    "field_name": "ManyToManys",
    "blank": True,
    "db_index": True,
    "to": CustomStringMaker.ManyToMany.to_gen,
    "related_name": CustomStringMaker.ManyToMany.related_name_gen,
    "through": CustomStringMaker.ManyToMany.through_gen,
    "through_fields": CustomStringMaker.ManyToMany.through_fields_gen,
    }
    
    def __init__(self, *args, **kwargs):
        deleters = ['app_name_destination', 'app_name_model_destination', 'app_super_model']
        class_attrs = ManyToManys.class_custom_default_attrs
    


        kwargs = kwargs_setter(kwargs, class_attrs, deleters)
        super().__init__(*args, **kwargs)
    