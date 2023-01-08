from django.utils.translation import gettext_lazy as _

from Core.fields.DefaultFields import CustomDefaultField
from Core.utils.ProjectUtils import CustomValidators

class CustomNameField(CustomDefaultField.CharField):
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
        for key, value in CustomNameField.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)
        super().__init__(*args, **kwargs)

class CustomTitleField(CustomDefaultField.CharField):
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
        for key, value in CustomTitleField.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        super().__init__(*args, **kwargs)

class CustomShortDescriptionField(CustomDefaultField.CharField):
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
        for key, value in CustomShortDescriptionField.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        super().__init__(*args, **kwargs)

class CustomPhoneNumberField(CustomDefaultField.CharField):
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
        for key, value in CustomPhoneNumberField.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)
        kwargs["help_text"] = kwargs.get("help_text", _(f"Phone number of this {kwargs['class_name']} record"))

        super().__init__(*args, **kwargs)
