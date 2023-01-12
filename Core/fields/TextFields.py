from Core.fields.DefaultFields import CustomDefaultField
from Core.utils.ProjectUtils import CustomValidators

class TextABC(CustomDefaultField.TextField):
    class Meta:
        abstract=True
    class_custom_default_attrs = {
        "class_name": "Model", # in this # required
        "field_name": "ABCTextField", # in this # required
        "blank": True, # in super
        "null": True, # in super
        "max_length": 1000, # in super
        "validators": None # in this # optional
        # has help text in __init__ # in this # optional
        }

    def __init__(self, *args, **kwargs):
        for key, value in TextABC.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        super().__init__(*args, **kwargs)

class Description(CustomDefaultField.TextField):
    class Meta:
        abstract=True
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
        for key, value in Description.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        super().__init__(*args, **kwargs)

class Body(CustomDefaultField.TextField):
    class Meta:
        abstract=True
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
        for key, value in Body.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        super().__init__(*args, **kwargs)
