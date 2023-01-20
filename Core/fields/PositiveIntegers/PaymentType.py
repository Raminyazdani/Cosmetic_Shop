

import re
from django.contrib.contenttypes import fields
from django.db import models
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField
from Core.utils.ProjectUtils import CustomStringMaker, CustomValidators, kwargs_setter
from Core.fields import DefaultFields
from Core.fields.FieldClassBases import Base, DelClassName

class PaymentType(DefaultFields.PositiveIntegers):

    class Meta:
        abstract = True

    
    ONLINE = 0
    ATPLACCE = 1
    PAYMENT_TYPE_CHOICES = (
        (ONLINE, 'Online'),
        (ATPLACCE, 'At Place'),
    )
    

    class_custom_default_attrs = {
    "class_name": "Model",
    "field_name": "PaymentType",
    "choices": PAYMENT_TYPE_CHOICES,
    "db_index": True,
    "default": ONLINE,
    "validators": CustomValidators.PaymentTypeValidator
    }
    
    def __init__(self, *args, **kwargs):
        deleters = []
        class_attrs = PaymentType.class_custom_default_attrs
    


        kwargs = kwargs_setter(kwargs, class_attrs, deleters)
        super().__init__(*args, **kwargs)
    