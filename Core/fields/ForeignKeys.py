from django.db import models

from Core.fields.DefaultFields import CustomDefaultField

class AbstractForeignKey(CustomDefaultField.ForeignKey):
    class Meta:
        abstract = True

    class_custom_default_attrs = {
        "class_name": "Model",  # in this # required
        "field_name": "ABCForeignKey",  # in this # required
        "app_name_destination": "...",  # in this # required
        "app_name_model_destination": "...",  # in this # required
        "blank": True,  # in super
        "db_index": True,  # in super
        "null": True,  # in super
        "on_delete": models.SET_NULL,  # in super
        # "related_name": CustomStringMaker.ForeignKey.related_name_gen, #generative
        # "to": CustomStringMaker.ForeignKey.to_gen,                 #generative
        # "validators":None,,
        }

    def __init__(self, *args, **kwargs):
        for key, value in AbstractForeignKey.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)
        super().__init__(*args, **kwargs)

class AbstractSelfForeignKey(CustomDefaultField.ForeignKey):
    class Meta:
        abstract = True

    class_custom_default_attrs = {
        "class_name": "Model",  # in this # required
        "field_name": "ABCForeignKeySelf",  # in this # required
        "app_name_destination": "...",  # in this # required
        "app_name_model_destination": "...",  # in this # required
        "blank": True,  # in super
        "db_index": True,  # in super
        "null": True,  # in super
        "on_delete": models.SET_NULL,  # in super
        "related_name": "...",  # in this # required
        "to": "self",  # in this # required
        }

    def __init__(self, *args, **kwargs):
        for key, value in AbstractSelfForeignKey.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        super().__init__(*args, **kwargs)

class CustomCommentFieldForeignKey(CustomDefaultField.ForeignKey):
    class Meta:
        abstract = True

    """
    Custom Comment Field as ForeignKey
            "class_name": "Model",
            "field_name": "Foreign Key",
            "blank": True,
            "db_index": True,
            "null": True,
            "on_delete": models.SET_NULL,
            "related_name": CustomStringMaker.ForeignKey.related_name, autogenerate
            "to": CustomStringMaker.ForeignKey.to,autogenerate
            # "validators":None,
    """
    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "Comment",
        "app_name_destination": "Products",
        "app_name_model_destination": "Comment",
        }

    def __init__(self, *args, **kwargs):
        # "kw_class_name" : "Product/User"
        # "kw_field_name" : "Comment"
        # "kw_app_name" : "Products"
        # "kw_class_model" : "Comment"
        # "kw_related_name" : "comment"
        for key, value in CustomCommentFieldForeignKey.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)
        super().__init__(*args, **kwargs)

class CustomCategoryParentFieldForeignKey(CustomDefaultField.ForeignKey):
    class Meta:
        abstract = True

    """
    Custom Category Parent Field as ForeignKey
            "class_name": "Model",
            "field_name": "Foreign Key",
            "blank": True,
            "db_index": True,
            "null": True,
            "on_delete": models.SET_NULL,
            "related_name": CustomStringMaker.ForeignKey.related_name, autogenerate
            "to": CustomStringMaker.ForeignKey.to  autogenerate
            # "validators":None,
    """

    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "Parent",
        "app_name_destination": "Products",
        "app_name_model_destination": "Category",
        "to": "self",
        'default':None,
        'db_index':True,
        "related_name": "child",
        }

    def __init__(self, *args, **kwargs):
        # "kw_class_name" : "Category"
        # "kw_field_name" : "Category parent"
        # "kw_app_name" : "Products"
        # "kw_class_model" : "Category"
        # "kw_related_name" : "parent"
        for key, value in CustomCategoryParentFieldForeignKey.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        super().__init__(*args, **kwargs)

class CustomUserFieldForeignKey(CustomDefaultField.ForeignKey):
    class Meta:
        abstract = True

    """
    Custom User Field as ForeignKey
            "class_name": "Model",
            "field_name": "Foreign Key",
            "blank": True,
            "db_index": True,
            "null": True,
            "on_delete": models.SET_NULL,
            "related_name": CustomStringMaker.ForeignKey.related_name, autogenerate
            "to": CustomStringMaker.ForeignKey.to,autogenerate
            # "validators":None,
    """
    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "User",
        "blank": False,
        "app_name_destination": "Users",
        "app_name_model_destination": "User",
        }

    def __init__(self, *args, **kwargs):
        # "kw_class_name" : "Comment/Product/Profile"
        # "kw_field_name" : "User"
        # "kw_app_name" : "Users"
        # "kw_class_model" : "User"
        # "kw_related_name" : "user"
        for key, value in CustomUserFieldForeignKey.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)

        super().__init__(*args, **kwargs)

class CustomProductFieldForeignKey(CustomDefaultField.ForeignKey):
    class Meta:
        abstract = True

    """
    Custom Product Field as ForeignKey
            "class_name": "Model",
            "field_name": "Foreign Key",
            "blank": True,
            "db_index": True,
            "null": True,
            "on_delete": models.SET_NULL,
            "related_name": CustomStringMaker.ForeignKey.related_name, autogenerate
            "to": CustomStringMaker.ForeignKey.to,autogenerate
            # "validators":None,
    """

    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "Product",
        "app_name_destination": "Products",
        "app_name_model_destination": "Product",
        }

    def __init__(self, *args, **kwargs):
        # "kw_class_name" : "Comment/ProductCategory/ProductBrand/ProductTag"
        # "kw_field_name" : "Product"
        # "kw_app_name" : "Products"
        # "kw_class_model" : "Product"
        # "kw_related_name" : "product"
        for key, value in CustomProductFieldForeignKey.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)
        super().__init__(*args, **kwargs)

class CustomCategoryFieldForeignKey(CustomDefaultField.ForeignKey):
    class Meta:
        abstract = True

    """
    Custom Category Field as ForeignKey
            "class_name": "Model",
            "field_name": "Foreign Key",
            "blank": True,
            "db_index": True,
            "null": True,
            "on_delete": models.SET_NULL,
            "related_name": CustomStringMaker.ForeignKey.related_name, autogenerate
            "to": CustomStringMaker.ForeignKey.to,autogenerate
            # "validators":None,
    """

    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "Category",
        "app_name_destination": "Products",
        "app_name_model_destination": "Category",
        }

    def __init__(self, *args, **kwargs):
        # "kw_class_name" : "ProductCategory/Gallery"
        # "kw_field_name" : "Category"
        # "kw_app_name" : "Products"
        # "kw_class_model" : "Category"
        # "kw_related_name" : "category"
        for key, value in CustomCategoryFieldForeignKey.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)
        super().__init__(*args, **kwargs)

class CustomTagFieldForeignKey(CustomDefaultField.ForeignKey):
    class Meta:
        abstract = True

    """
    Custom Tag Field as ForeignKey
            "class_name": "Model",
            "field_name": "Foreign Key",
            "blank": True,
            "db_index": True,
            "null": True,
            "on_delete": models.SET_NULL,
            "related_name": CustomStringMaker.ForeignKey.related_name, autogenerate
            "to": CustomStringMaker.ForeignKey.to,autogenerate
            # "validators":None,
    """

    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "Tag",
        "app_name_destination": "Products",
        "app_name_model_destination": "Tag",
        }

    def __init__(self, *args, **kwargs):
        # "kw_class_name" : "ProductTag/Gallery"
        # "kw_field_name" : "Tag"
        # "kw_app_name" : "Products"
        # "kw_class_model" : "Tag"
        # "kw_related_name" : "tag"
        for key, value in CustomTagFieldForeignKey.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)
        super().__init__(*args, **kwargs)

class CustomBrandFieldForeignKey(CustomDefaultField.ForeignKey):
    class Meta:
        abstract = True

    """
    Custom Brand Field as ForeignKey
            "class_name": "Model",
            "field_name": "Foreign Key",
            "blank": True,
            "db_index": True,
            "null": True,
            "on_delete": models.SET_NULL,
            "related_name": CustomStringMaker.ForeignKey.related_name, autogenerate
            "to": CustomStringMaker.ForeignKey.to,autogenerate
            # "validators":None,
    """

    class_custom_default_attrs = {
        "class_name": "Model",
        "field_name": "Brand",
        "app_name_destination": "Products",
        "app_name_model_destination": "Brand",
        }

    def __init__(self, *args, **kwargs):
        # "kw_class_name" : "ProductBrand/Gallery"
        # "kw_field_name" : "Brand"
        # "kw_app_name" : "Products"
        # "kw_class_model" : "Brand"
        # "kw_related_name" : "brand"
        for key, value in CustomBrandFieldForeignKey.class_custom_default_attrs.items():
            kwargs[key] = kwargs.get(key, value)
        super().__init__(*args, **kwargs)
