from Core.fields.DefaultFields import CustomDefaultField

class ManyToManyABC(CustomDefaultField.ManyToManyField):
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
        "app_super_model":None
        # "to": CustomStringMaker.ManyToMany.to_gen,  # generative # No matter
        # "related_name": CustomStringMaker.ManyToMany.related_name_gen,  # generative # No matter
        # "through": CustomStringMaker.ManyToMany.through_gen,  # generative # if through not declare
        # "through_fields": CustomStringMaker.ManyToMany.through_fields_gen,  # generative #
        # validators : None
        }

    def __init__(self, *args, **kwargs):
        for key, value in ManyToManyABC.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        super().__init__(*args, **kwargs)

class ManyToManyCategory(CustomDefaultField.ManyToManyField):
    class Meta:
        abstract=True
    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "Category",
        "app_name_destination": "Products",
        "app_name_model_destination": "Category",
        "app_super_model": "Product"
        }

    def __init__(self, *args, **kwargs):
        for key, value in ManyToManyCategory.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)
        super().__init__(*args, **kwargs)

class ManyToManyTag(CustomDefaultField.ManyToManyField):
    class Meta:
        abstract=True

    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "Tag",
        "app_name_destination": "Products",
        "app_name_model_destination": "Tag",
        "app_super_model": "Product"
        }

    def __init__(self, *args, **kwargs):
        for key, value in ManyToManyTag.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        super().__init__(*args, **kwargs)

class ManyToManyBrand(CustomDefaultField.ManyToManyField):
    class Meta:
        abstract=True

    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "Brand",
        "app_name_destination": "Products",
        "app_name_model_destination": "Brand",
        "app_super_model": "Product"
        }

    def __init__(self, *args, **kwargs):
        for key, value in ManyToManyBrand.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        super().__init__(*args, **kwargs)

class ManyToManyProduct(CustomDefaultField.ManyToManyField):
    class Meta:
        abstract=True

    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "Product",
        "app_name_destination": "Products",
        "app_name_model_destination": "Product",
        "app_super_model": "Product"
        }

    def __init__(self, *args, **kwargs):
        for key, value in ManyToManyProduct.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        super().__init__(*args, **kwargs)
