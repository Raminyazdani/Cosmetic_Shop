

import re
from django.contrib.contenttypes import fields
from django.db import models
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField
from Core.utils.ProjectUtils import CustomStringMaker, CustomValidators, kwargs_setter
from Core.fields import DefaultFields
from Core.fields.FieldClassBases import Base, DelClassName

class GenericRelations(Base,fields.GenericRelation):

    class Meta:
        abstract = True

    

    class_custom_default_attrs = {
    "class_name": "Model",
    "field_name": "GenericRelations",
    "to": CustomStringMaker.ForeignKey.to_gen,
    "content_type_field": "content_type",
    "object_id_field": "object_id",
    "related_query_name": CustomStringMaker.ForeignKey.related_name_gen,
    }
    
    def __init__(self, *args, **kwargs):
        deleters = []
        class_attrs = GenericRelations.class_custom_default_attrs
    


        kwargs = kwargs_setter(kwargs, class_attrs, deleters)
        super().__init__(*args, **kwargs)
    