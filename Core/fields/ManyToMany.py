from Core.fields.DefaultFields import CustomDefaultField

class AbstractObjectFieldManyToMany(CustomDefaultField.ManyToManyField):
    class Meta:
        abstract=True
    class_costum_default_attrs = {
        "class_name": "Model",  # in this # required
        "field_name": "ABCManyToMany",  # in this # required
        "app_name_destination": "...",  # in this # required
        "app_name_model_destination": "...",  # in this # required
        "through_fields": [None, None],  # in this # required
        "through": "..." or None, # in this  required ( it depends on where the through table is,if class_name is Child put None )
        "blank": True,  # in super
        "db_index": True,  # in super
        # "to": CustomStringMaker.ManyToMany.to_gen,  # generative # No matter
        # "related_name": CustomStringMaker.ManyToMany.related_name_gen,  # generative # No matter
        # "through": CustomStringMaker.ManyToMany.through_gen,  # generative # if through not declare
        # "through_fields": CustomStringMaker.ManyToMany.through_fields_gen,  # generative #
        # validators : None
        }

    def __init__(self, *args, **kwargs):
        for key, value in AbstractObjectFieldManyToMany.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        super().__init__(*args, **kwargs)

class CustomCategoryFieldManyToMany(CustomDefaultField.ManyToManyField):
    class Meta:
        abstract=True
    """
    Custom Category Field as ManyToMany

    """

    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "Category",
        "app_name_destination": "Products",
        "app_name_model_destination": "Category",
        "through_fields": [None, "category_id"],  # in this # required
        "through": "Products.ProductCategory"
        }

    def __init__(self, *args, **kwargs):
        for key, value in CustomCategoryFieldManyToMany.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)
        super().__init__(*args, **kwargs)

class CustomTagFieldManyToMany(CustomDefaultField.ManyToManyField):
    class Meta:
        abstract=True
    """
    Custom Tag Field as ManyToMany

    """

    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "Tag",
        "app_name_destination": "Products",
        "app_name_model_destination": "Tag",
        "through_fields": [None, "tag_id"],  # in this # required
        "through": "Products.ProductTag"
        }

    def __init__(self, *args, **kwargs):
        for key, value in CustomTagFieldManyToMany.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        super().__init__(*args, **kwargs)

class CustomBrandFieldManyToMany(CustomDefaultField.ManyToManyField):
    class Meta:
        abstract=True
    """
    Custom Brand Field as ManyToMany

    """

    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "Brand",
        "app_name_destination": "Products",
        "app_name_model_destination": "Brand",
        "through_fields": [None, "brand_id"],  # in this # required
        "through": "Products.ProductBrand"
        }

    def __init__(self, *args, **kwargs):
        for key, value in CustomBrandFieldManyToMany.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        super().__init__(*args, **kwargs)

class CustomProductFieldManyToMany(CustomDefaultField.ManyToManyField):
    class Meta:
        abstract=True
    """
    Custom Product Field as ManyToManyField

    """

    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "Product",
        "app_name_destination": "Products",
        "app_name_model_destination": "Product",
        "through_fields": ["product_id", None],  # in this # required
        "through": None
        }

    def __init__(self, *args, **kwargs):
        for key, value in CustomProductFieldManyToMany.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        super().__init__(*args, **kwargs)
