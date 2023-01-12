from django.utils.translation import gettext_lazy as _

from Core.fields.DefaultFields import CustomDefaultField
from Core.utils.ProjectUtils import CustomValidators

class CharABC(CustomDefaultField.CharField):
    class Meta:
        abstract=True
    class_custom_default_attrs = {
        "class_name": "Model", # in this
        "field_name": "ABCCharField", # in this
        "blank": True, # in super
        "db_index": False, # in super
        "max_length": 30, # in super
        "null": True, # in super
        "unique": False, # in super
        "validators": None, # in this # optional
        # has help text in __init__ # in this # optional
        }

    def __init__(self, *args, **kwargs):
        for key, value in CharABC.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)
        kwargs["help_text"] = kwargs.get("help_text", _(f" ... of this {kwargs['class_name']} record"))

        super().__init__(*args, **kwargs)

class Name(CustomDefaultField.CharField):
    class Meta:
        abstract=True
    """
    Custom Name Field as CharField default
            # "class_name": "Model",
            # "field_name": "Char Field",
            # "blank": True,
            # "db_index":False,
            # "max_length":30,
            # "null":True,
            # "unique":False,
            # "validator" : None,
    """

    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "Name",
        "db_index": True,
        "blank": False,
        "null": False,
        "unique": True,
        "validators": CustomValidators.NameValidator
        }

    def __init__(self, *args, **kwargs):
        for key, value in Name.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)
        super().__init__(*args, **kwargs)

class Title(CustomDefaultField.CharField):
    class Meta:
        abstract=True
    """
    Custom Title Field as CharField default
            # "class_name": "Model",
            # "field_name": "Char Field",
            # "blank": True,
            # "db_index":False,
            # "max_length":30,
            # "null":True,
            # "unique":False,
            " validators" : None,
    """
    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "Title",
        "blank": False,
        "null": False,
        "max_length": 20,
        "validators": CustomValidators.TitleValidator
        }

    def __init__(self, *args, **kwargs):
        for key, value in Title.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        super().__init__(*args, **kwargs)

class ShortDescription(CustomDefaultField.CharField):
    class Meta:
        abstract=True
    """
    Custom Short Description Field as CharField default
            # "class_name": "Model",
            # "field_name": "Char Field",
            # "blank": True,
            # "db_index":False,
            # "max_length":30,
            # "null":True,
            # "unique":False,
    """
    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "Short Description",
        "blank": False,
        "max_length": 100,
        "null": False,
        "validators": CustomValidators.ShortDescriptionValidator
        }

    def __init__(self, *args, **kwargs):
        for key, value in ShortDescription.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        super().__init__(*args, **kwargs)

class PhoneNumber(CustomDefaultField.CharField):
    class Meta:
        abstract=True
    """
    Custom Phone Number Field as CharField
            # "class_name": "Model",
            # "field_name": "Char Field",
            # "blank": True,
            # "db_index":False,
            # "max_length":30,
            # "null":True,
            # "unique":False,
    """

    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "phone number",
        "blank": False,
        "db_index": True,
        "max_length": 15,
        "null": False,
        "unique": True,
        "validators": CustomValidators.PhoneValidator
        # has help text in __init__
        }

    def __init__(self, *args, **kwargs):
        for key, value in PhoneNumber.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)
        kwargs["help_text"] = kwargs.get("help_text", _(f"Phone number of this {kwargs['class_name']} record"))

        super().__init__(*args, **kwargs)
