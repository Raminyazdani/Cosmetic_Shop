from Core.fields.DefaultFields import CustomDefaultField
from Core.utils.ProjectUtils import CustomValidators

class DecimalABC:
    class Meta:
        abstract=True
    class_custom_default_attrs = {
        "class_name": "Model", # in this # required
        "field_name": "ABCDecimalField", # in this # required
        "blank": False, # in super
        "db_index": True, # in super
        "decimal_places": 2,# in super
        "default": 0.0,# in super
        "max_digits": 10,# in super
        "null": False,# in super
        "validators": None # in this # optional
        }

    def __init__(self, *args, **kwargs):
        for key, value in DecimalABC.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        super().__init__(*args, **kwargs)

class PriceDollar(CustomDefaultField.DecimalField):
    class Meta:
        abstract=True
    """
    Custom Price Field as DecimalField
            "class_name": "Model",
            "field_name": "Decimal Field",
            "blank": False,
            "db_index": True,
            "decimal_places": 2,
            "default": 0.0,
            "max_digits": 10,
            "null": False,
            "validator" : None
    """
    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "Dollar Price",
        "validators": CustomValidators.DollarPriceValidator
        }

    def __init__(self, *args, **kwargs):
        for key, value in PriceDollar.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        super().__init__(*args, **kwargs)
