from Core.fields.DefaultFields import CustomDefaultField

class SlugABC(CustomDefaultField.SlugField):
    class Meta:
        abstract=True
    """
    Abstract Slug Field
    """
    class_custom_default_attrs = {
        "class_name": "Model",  # in this # required
        "field_name": "ABCSlug",  # in this # required
        "blank": True,  # in super
        "db_index": True,  # in super
        "max_length": 100,  # in super
        "null": True,  # in super
        "unique": True,  # in super
        }


    def __init__(self, *args, **kwargs):
        for key, value in SlugABC.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        super().__init__(*args, **kwargs)

class Slug(CustomDefaultField.SlugField):
    class Meta:
        abstract=True
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
        for key, value in Slug.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        super().__init__(*args, **kwargs)
