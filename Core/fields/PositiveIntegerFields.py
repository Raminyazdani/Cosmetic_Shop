from django.utils.translation import gettext_lazy as _

from Core.fields.DefaultFields import CustomDefaultField
from Core.utils.ProjectUtils import CustomValidators

class PostivieIntegerABC(CustomDefaultField.PositiveIntegerField):
    class Meta:
        abstract=True
    """
    Abstract Positive Integer Field
    """
    class_custom_default_attrs = {
        "class_name": "Model",  # in this # required
        "field_name": "ABCPositiveIntegerField",  # in this # required
        "blank": False,  # in super
        "choices": None,  # in this # optional
        "db_index": False,  # in super
        "default": 0,  # in super
        "null": False,  # in super
        "validators": None,  # in this # optional
        # has help text in __init__ # in this # optional
        }

    
    def __init__(self, *args, **kwargs):
        for key, value in PostivieIntegerABC.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        kwargs["help_text"] = kwargs.get("help_text", _("UNISEX/MALE/FEMALE as integers"))

        super().__init__(*args, **kwargs)

class Gender(CustomDefaultField.PositiveIntegerField):
    class Meta:
        abstract=True
    """
    Custom Gender Field as PositiveIntegerField default
    Choices are defined as class variables so that they can be easily accessed from instances.
    includes: UNISEX, MALE , FEMALE
            "class_name":"Model",
            "field_name":"Positive Integer Field",
            "choices":None,
            "db_index":False,
            "null":False,
            "blank":False,
            "default":0,
            "validators":None,
    """
    UNISEX = 0
    MALE = 1
    FEMALE = 2
    GENDER_CHOICES = ((UNISEX, _("Gender free")), (MALE, _("For men")), (FEMALE, _("For women")),)
    GENDER = GENDER_CHOICES

    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "Gender",
        "choices": GENDER_CHOICES,
        "db_index": True,
        "default": UNISEX,
        "validators": CustomValidators.GenderValidator
        # has help text in __init__
        }

    def __init__(self, *args, **kwargs):
        for key, value in Gender.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        kwargs["help_text"] = kwargs.get("help_text", _("UNISEX/MALE/FEMALE as integers"))

        super().__init__(*args, **kwargs)

class Rating(CustomDefaultField.PositiveIntegerField):
    class Meta:
        abstract=True
    """
    Custom Rating Field as PositiveIntegerField
            "class_name":"Model",
            "field_name":"Positive Integer Field",
            "choices":None,
            "db_index":False,
            "null":False,
            "blank":False,
            "default":0,
            "validators":None,
    """

    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "Rating",
        "db_index": True,
        "validators": CustomValidators.RatingValidator
        }

    def __init__(self, *args, **kwargs):
        for key, value in Rating.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        super().__init__(*args, **kwargs)
