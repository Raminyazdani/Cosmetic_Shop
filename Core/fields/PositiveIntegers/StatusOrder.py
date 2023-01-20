

import re
from django.contrib.contenttypes import fields
from django.db import models
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField
from Core.utils.ProjectUtils import CustomStringMaker, CustomValidators, kwargs_setter
from Core.fields import DefaultFields
from Core.fields.FieldClassBases import Base, DelClassName

class StatusOrder(DefaultFields.PositiveIntegers):

    class Meta:
        abstract = True

    
    PENDING = 0
    CANCEL = 1
    DONE = 2
    STATUS_ORDER_CHOICES = (
        (PENDING, 'Pending'),
        (CANCEL, 'Cancel'),
        (DONE, 'Done'),
    )
    

    class_custom_default_attrs = {
    "class_name": "Model",
    "field_name": "StatusOrder",
    "choices": STATUS_ORDER_CHOICES,
    "db_index": True,
    "default": PENDING,
    "validators": CustomValidators.StatusOrderValidator
    }
    
    def __init__(self, *args, **kwargs):
        deleters = []
        class_attrs = StatusOrder.class_custom_default_attrs
    


        kwargs = kwargs_setter(kwargs, class_attrs, deleters)
        super().__init__(*args, **kwargs)
    