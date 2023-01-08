from Core.fields.DefaultFields import CustomDefaultField

class CustomSlugField(CustomDefaultField.SlugField):
    """
    Custom Slug Field as SlugField
            "class_name": "Model",
            "field_name": "Slug Field",
            "blank": True,
            "db_index": True,
            "max_length": 100,
            "null": True,
            "unique": True,
    """

    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "Slug",
        # "validators": None
        }

    def __init__(self, *args, **kwargs):
        for key, value in CustomSlugField.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        super().__init__(*args, **kwargs)
