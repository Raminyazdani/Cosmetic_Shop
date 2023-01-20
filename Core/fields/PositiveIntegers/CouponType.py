

import re
from django.contrib.contenttypes import fields
from django.db import models
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField
from Core.utils.ProjectUtils import CustomStringMaker, CustomValidators, kwargs_setter
from Core.fields import DefaultFields
from Core.fields.FieldClassBases import Base, DelClassName

class CouponType(DefaultFields.PositiveIntegers):

    class Meta:
        abstract = True

    
    PERCENT = 0
    AMOUNT = 1
    COUPON_TYPE_CHOICES = (
        (PERCENT, 'Percent'),
        (AMOUNT, 'Amount'),
    )
    

    class_custom_default_attrs = {
    "class_name": "Model",
    "field_name": "CouponType",
    "choices": COUPON_TYPE_CHOICES,
    "db_index": True,
    "default": PERCENT,
    "validators": CustomValidators.CouponTypeValidator
    }
    
    def __init__(self, *args, **kwargs):
        deleters = []
        class_attrs = CouponType.class_custom_default_attrs
    


        kwargs = kwargs_setter(kwargs, class_attrs, deleters)
        super().__init__(*args, **kwargs)
    