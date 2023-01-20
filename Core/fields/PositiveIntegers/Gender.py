

import re
from django.contrib.contenttypes import fields
from django.db import models
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField
from Core.utils.ProjectUtils import CustomStringMaker, CustomValidators, kwargs_setter
from Core.fields import DefaultFields
from Core.fields.FieldClassBases import Base, DelClassName

class Gender(DefaultFields.PositiveIntegers):

    class Meta:
        abstract = True

    
    UNISEX = 0
    MALE = 1
    FEMALE = 2
    GENDER_CHOICES = ((UNISEX, _("Gender free")), (MALE, _("For men")), (FEMALE, _("For women")),)
    

    class_custom_default_attrs = {
    "class_name": "Model",
    "field_name": "Gender",
    "choices": GENDER_CHOICES,
    "db_index": True,
    "default": UNISEX,
    "validators": CustomValidators.GenderValidator
    }
    
    def __init__(self, *args, **kwargs):
        deleters = []
        class_attrs = Gender.class_custom_default_attrs
    


        kwargs = kwargs_setter(kwargs, class_attrs, deleters)
        super().__init__(*args, **kwargs)
    