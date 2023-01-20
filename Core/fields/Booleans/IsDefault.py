

import re
from django.contrib.contenttypes import fields
from django.db import models
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField
from Core.utils.ProjectUtils import CustomStringMaker, CustomValidators, kwargs_setter
from Core.fields import DefaultFields
from Core.fields.FieldClassBases import Base, DelClassName

class IsDefault(DefaultFields.Booleans):

    class Meta:
        abstract = True

    

    class_custom_default_attrs = {
    "class_name": "Model",
    "field_name": "IsDefault",
    'default': False,
    'db_index': True,
    }
    
    def __init__(self, *args, **kwargs):
        deleters = []
        class_attrs = IsDefault.class_custom_default_attrs
    
        kwargs["help_text"] = kwargs.get("help_text", _(f"Is this {kwargs['class_name']} record default? ?"))
        kwargs["verbose_name"] = kwargs.get("verbose_name", _("Is Default"))


        kwargs = kwargs_setter(kwargs, class_attrs, deleters)
        super().__init__(*args, **kwargs)
    