

import re
from django.contrib.contenttypes import fields
from django.db import models
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField
from Core.utils.ProjectUtils import CustomStringMaker, CustomValidators, kwargs_setter
from Core.fields import DefaultFields
from Core.fields.FieldClassBases import Base, DelClassName

class ShipmentType(DefaultFields.PositiveIntegers):

    class Meta:
        abstract = True

    
    FAST = 0
    NORMAL = 1
    SHIPMENT_TYPE_CHOICES = (
        (FAST, 'Fast'),
        (NORMAL, 'Normal'),
    )
    

    class_custom_default_attrs = {
    "class_name": "Model",
    "field_name": "ShipmentType",
    "choices": SHIPMENT_TYPE_CHOICES,
    "db_index": True,
    "default": FAST,
    "validators": CustomValidators.ShipmentTypeValidator
    }
    
    def __init__(self, *args, **kwargs):
        deleters = []
        class_attrs = ShipmentType.class_custom_default_attrs
    


        kwargs = kwargs_setter(kwargs, class_attrs, deleters)
        super().__init__(*args, **kwargs)
    