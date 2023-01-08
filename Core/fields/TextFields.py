from Core.fields.DefaultFields import CustomDefaultField
from Core.utils.ProjectUtils import CustomValidators

class CustomDescriptionField(CustomDefaultField.TextField):
    """
    Custom Description Field as TextField
            "class_name": "Model",
            "field_name": "Text Field",
            "blank": True,
            "null": True,
            "max_length": 1000,
            # "validator": None
    """

    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "description",
        "validators": CustomValidators.DescriptionValidator
        }

    def __init__(self, *args, **kwargs):
        for key, value in CustomDescriptionField.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        super().__init__(*args, **kwargs)

class CustomBodyField(CustomDefaultField.TextField):
    """
    Custom Body Field as TextField
            "class_name": "Model",
            "field_name": "Text Field",
            "blank": True,
            "null": True,
            "max_length": 1000,
            # "validator": None
    """

    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "Body",
        "blank": False,
        "max_length": 250,
        "null": False,
        "validators": CustomValidators.BodyValidator
        }

    def __init__(self, *args, **kwargs):
        for key, value in CustomBodyField.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        super().__init__(*args, **kwargs)
