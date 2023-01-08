from Core.fields.DefaultFields import CustomDefaultField
from Core.utils.ProjectUtils import CustomValidators

class CustomPriceFieldDollar(CustomDefaultField.DecimalField):
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
        for key, value in CustomPriceFieldDollar.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        super().__init__(*args, **kwargs)
