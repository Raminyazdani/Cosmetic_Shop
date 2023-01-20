

import re
from django.contrib.contenttypes import fields
from django.db import models
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField
from Core.utils.ProjectUtils import CustomStringMaker, CustomValidators, kwargs_setter
from Core.fields import DefaultFields
from Core.fields.FieldClassBases import Base, DelClassName

class FilePaths(Base,models.FilePathField):

    class Meta:
        abstract = True

    

    class_custom_default_attrs = {
    "class_name": "Model",
    "field_name": "FilePaths",
    "path": CustomStringMaker.FilePath.path_gen,
    "recursive": True,
    "match": None,
    "allow_files": True,
    }
    
    def __init__(self, *args, **kwargs):
        deleters = []
        class_attrs = FilePaths.class_custom_default_attrs
    


        kwargs = kwargs_setter(kwargs, class_attrs, deleters)
        super().__init__(*args, **kwargs)
    