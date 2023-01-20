

import re
from django.contrib.contenttypes import fields
from django.db import models
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField
from Core.utils.ProjectUtils import CustomStringMaker, CustomValidators, kwargs_setter
from Core.fields import DefaultFields
from Core.fields.FieldClassBases import Base, DelClassName

class WeekDays(DefaultFields.MultiSelects):

    class Meta:
        abstract = True

    
    Saturday = 0
    Sunday = 1
    Monday = 2
    Tuesday = 3
    Wednesday = 4
    Thursday = 5
    Friday = 6
    WEEKDAYS_CHOICES = (
        (Saturday, 'Saturday'),
        (Sunday, 'Sunday'),
        (Monday, 'Monday'),
        (Tuesday, 'Tuesday'),
        (Wednesday, 'Wednesday'),
        (Thursday, 'Thursday'),
        (Friday, 'Friday'),
    )
    

    class_custom_default_attrs = {
    "class_name": "Model",
    "field_name": "WeekDays",
    "choices": "WEEKDAYS_CHOICES",
    "default": "[]",
    "null": "True",
    "blank": "True"
    }
    
    def __init__(self, *args, **kwargs):
        deleters = []
        class_attrs = WeekDays.class_custom_default_attrs
    


        kwargs = kwargs_setter(kwargs, class_attrs, deleters)
        super().__init__(*args, **kwargs)
    