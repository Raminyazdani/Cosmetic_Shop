from Core.fields.DefaultFields import CustomDefaultField

class CustomCategoryFieldManyToMany(CustomDefaultField.ManyToManyField):
    """
    Custom Category Field as ManyToMany

    """

    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "Category",
        "app_name_destination": "Products",
        "app_name_model_destination": "Category",
        "through_fields": [None, "category_id"],
        "through": "ProductCategory",
        }

    def __init__(self, *args, **kwargs):
        # "kw_class_name" : ["Product","User"],
        # "kw_field_name" : "Category",
        # "kw_app_name" : "Products",
        # "kw_class_model" : "Category",
        # "kw_related_name" : "category",
        # "kw_through_fields" : ("?", "category")
        for key, value in CustomCategoryFieldManyToMany.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)
        super().__init__(*args, **kwargs)

class CustomTagFieldManyToMany(CustomDefaultField.ManyToManyField):
    """
    Custom Tag Field as ManyToMany

    """

    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "Tag",
        "app_name_destination": "Products",
        "app_name_model_destination": "Tag",
        "through_fields": [None, "tag_id"],
        "through": "ProductTag",
        }

    def __init__(self, *args, **kwargs):
        # "kw_class_name" : ["Product","User"],
        # "kw_field_name" : "Tag",
        # "kw_app_name" : "Products",
        # "kw_class_model" : "Tag",
        # "kw_related_name" : "tag",
        # "kw_through_fields" : ("?", "tag")
        for key, value in CustomTagFieldManyToMany.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        super().__init__(*args, **kwargs)

class CustomBrandFieldManyToMany(CustomDefaultField.ManyToManyField):
    """
    Custom Brand Field as ManyToMany

    """

    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "Brand",
        "app_name_destination": "Products",
        "app_name_model_destination": "Brand",
        "through_fields": [None, "brand_id"],
        "through": "ProductBrand",
        }

    def __init__(self, *args, **kwargs):
        # "kw_class_name" : ["Product","User"],
        # "kw_field_name" : "Brand",
        # "kw_app_name" : "Products",
        # "kw_class_model" : "Brand",
        # "kw_related_name" : "brand",
        # "kw_through_fields" : ("?", "brand")
        for key, value in CustomBrandFieldManyToMany.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        super().__init__(*args, **kwargs)

class CustomProductFieldManyToMany(CustomDefaultField.ManyToManyField):
    """
    Custom Product Field as ManyToManyField

    """

    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "Product",
        "app_name_destination": "Products",
        "app_name_model_destination": "Product",
        "through_fields": ["product_id", None],
        "through": None,
        }

    def __init__(self, *args, **kwargs):
        # "kw_class_name" : ["Brand","Category","Tag","User"],
        # "kw_field_name" : "Product",
        # "kw_app_name" : "Products",
        # "kw_class_model" : "Product",
        # "kw_related_name" : "product",
        # "kw_through_fields" : ("?", "category")
        for key, value in CustomProductFieldManyToMany.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)


        super().__init__(*args, **kwargs)
