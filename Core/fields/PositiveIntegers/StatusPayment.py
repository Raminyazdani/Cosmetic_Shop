

import re
from django.contrib.contenttypes import fields
from django.db import models
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField
from Core.utils.ProjectUtils import CustomStringMaker, CustomValidators, kwargs_setter
from Core.fields import DefaultFields
from Core.fields.FieldClassBases import Base, DelClassName

class StatusPayment(DefaultFields.PositiveIntegers):

    class Meta:
        abstract = True

    
    PENDING = 0
    CANCEL = 1
    PAID = 2
    STATUS_PAYMENT_CHOICES = (
        (PENDING, 'Pending'),
        (CANCEL, 'Cancel'),
        (PAID, 'Paid'),
    )
    

    class_custom_default_attrs = {
    "class_name": "Model",
    "field_name": "StatusPayment",
    "choices": STATUS_PAYMENT_CHOICES,
    "db_index": True,
    "default": PENDING,
    "validators": CustomValidators.StatusPaymentValidator
    }
    
    def __init__(self, *args, **kwargs):
        deleters = []
        class_attrs = StatusPayment.class_custom_default_attrs
    


        kwargs = kwargs_setter(kwargs, class_attrs, deleters)
        super().__init__(*args, **kwargs)
    