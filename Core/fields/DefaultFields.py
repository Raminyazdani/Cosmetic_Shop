import re

from django.contrib.contenttypes import fields
from django.db import models
from django.utils.translation import gettext_lazy as _

from Core.utils.ProjectUtils import CustomStringMaker, CustomValidators

class BaseMethodCustomField:
    class Meta:
        abstract = True

    """
    Base Method Custom Field
    """

    class DelClassName:
        class Meta:
            abstract = True

        """
         This class is used to delete the class_name argument from the kwargs
        """

        def __init__(self, *args, **kwargs):
            """
            This method is used to delete the class_name argument from the kwargs
            :param args:
            :param kwargs:
            """
            res = re.findall('[A-Z][^A-Z]*', kwargs["class_name"])
            if len(res) > 1: kwargs["class_name"], kwargs["field_name"] = res[1], res[0]

            kwargs["verbose_name"] = kwargs.get("verbose_name", _(kwargs['class_name'] + f"`s {kwargs['field_name']}"))
            kwargs["help_text"] = kwargs.get("help_text", _(f"{kwargs['field_name']} of this {kwargs['class_name']} record"))

            del kwargs["class_name"], kwargs['field_name'],

            # print("\nstart")
            # print(self)
            # print(args)
            # print(kwargs)
            super().__init__(*args, **kwargs)  # class GetClassName:  #     def __init__(self, *args, **kwargs):  #         kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"].capitalize()  #         self.class_name = kwargs["class_name"].capitalize()  #

class CustomDefaultField:
    class Meta:
        abstract = True

    class Base(BaseMethodCustomField.DelClassName):
        class Meta:
            abstract = True

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

    class CharField(Base, models.CharField):
        class Meta:
            abstract = True

        class_custom_default_attrs = {
            "class_name": "Model",
            "field_name": "Char Field",
            "blank": True,
            "db_index": False,
            "max_length": 30,
            "null": True,
            "unique": False,
            # "validators":None,
            }

        def __init__(self, *args, **kwargs):
            for key, value in CustomDefaultField.CharField.class_custom_default_attrs.items():
                kwargs[key] = kwargs.get(key, value)

            super().__init__(*args, **kwargs)

    class PositiveIntegerField(Base, models.PositiveIntegerField):
        class Meta:
            abstract = True

        class_custom_default_attrs = {
            "class_name": "Model",
            "field_name": "Positive Integer Field",  # "choices":None,
            "db_index": False,
            "null": False,
            "blank": False,
            "default": 0,
            # "validators":None,
            }

        def __init__(self, *args, **kwargs):
            for key, value in CustomDefaultField.PositiveIntegerField.class_custom_default_attrs.items():
                kwargs[key] = kwargs.get(key, value)

            super().__init__(*args, **kwargs)

    class DecimalField(Base, models.DecimalField):
        class Meta:
            abstract = True

        class_custom_default_attrs = {
            "class_name": "Model",
            "field_name": "Decimal Field",
            "blank": False,
            "db_index": True,
            "decimal_places": 2,
            "default": 0.0,
            "max_digits": 10,
            "null": False,
            "validators": None
            }

        def __init__(self, *args, **kwargs):
            for key, value in CustomDefaultField.DecimalField.class_custom_default_attrs.items():
                kwargs[key] = kwargs.get(key, value)

            super().__init__(*args, **kwargs)

    class SlugField(Base, models.SlugField):
        class Meta:
            abstract = True

        class_custom_default_attrs = {
            "class_name": "Model",
            "field_name": "Slug Field",
            "blank": True,
            "db_index": True,
            "max_length": 100,
            "null": True,
            "unique": True,
            }

        def __init__(self, *args, **kwargs):
            for key, value in CustomDefaultField.SlugField.class_custom_default_attrs.items():
                kwargs[key] = kwargs.get(key, value)
            super().__init__(*args, **kwargs)

    class ForeignKey(Base, models.ForeignKey):
        class Meta:
            abstract = True

        class_costum_default_attrs = {
            "class_name": "Model",
            "field_name": "Foreign Key",  # "app_name_destination": "?", get
            # "app_name_model_destination": "?",get
            "blank": True,
            "db_index": True,
            "null": True,
            "on_delete": models.SET_NULL,
            "related_name": CustomStringMaker.ForeignKey.related_name_gen,
            "to": CustomStringMaker.ForeignKey.to_gen,
            # "validators":None,
            }

        # test CommentField
        # "kw_class_name" : "Product/User"
        # "kw_field_name" : "Comment"
        # "kw_app_name" : "Products"
        # "kw_class_model" : "Comment"
        # "kw_related_name" : "comment"
        def __init__(self, *args, **kwargs):
            for key, value in CustomDefaultField.ForeignKey.class_costum_default_attrs.items():
                if kwargs["class_name"] == "ContentType":
                    kwargs["related_name"] = kwargs.get("related_name", CustomStringMaker.ContentType.related_name_gen(kwargs["class_name"]))
                    break
                if key == "to":
                    kwargs[key] = kwargs.get(key, value(kwargs["app_name_destination"], kwargs["app_name_model_destination"]))
                elif key == "related_name":
                    kwargs[key] = kwargs.get(key, value(kwargs["class_name"], kwargs["app_name_model_destination"]))
                else:
                    kwargs[key] = kwargs.get(key, value)

            del kwargs["app_name_destination"], kwargs["app_name_model_destination"]
            super().__init__(*args, **kwargs)

    class ManyToManyField(Base, models.ManyToManyField):
        class Meta:
            abstract = True

        class_costum_default_attrs = {
            "class_name": "Model",
            "field_name": "Many To Many Field",
            "blank": True,
            "db_index": True,
            "to": CustomStringMaker.ManyToMany.to_gen,
            "related_name": CustomStringMaker.ManyToMany.related_name_gen,
            "through": CustomStringMaker.ManyToMany.through_gen,
            "through_fields": CustomStringMaker.ManyToMany.through_fields_gen,
            # validators : None
            }

        # class_name = ProductCategory #dynamic
        # field_name = Category #dynamic/static
        # app_name = Products #static
        # class_model = Category #static
        # class_field_name = Category #static
        # class_related_name = category #static
        # class_through_fields = ('?', 'category') #static
        def __init__(self, *args, **kwargs):
            for key, value in CustomDefaultField.ManyToManyField.class_costum_default_attrs.items():
                if key == "to":
                    kwargs[key] = kwargs.get(key, value(kwargs["app_name_destination"], kwargs["app_name_model_destination"]))
                elif key == "related_name":
                    kwargs[key] = kwargs.get(key, value(kwargs["class_name"], kwargs["app_name_model_destination"]))

                elif key == "through_fields":
                    kwargs[key] = kwargs.get(key, None)
                    if None in kwargs[key] or kwargs[key] is None:
                        kwargs[key] = value(kwargs["class_name"], kwargs["app_name_model_destination"], kwargs["through_fields"])
                elif key == "through":
                    kwargs[key] = kwargs.get(key, None)
                    if kwargs[key] is None:
                        kwargs[key] = value(kwargs["class_name"], kwargs["app_name_destination"], kwargs["through_fields"])
                else:
                    kwargs[key] = kwargs.get(key, value)
            del kwargs["app_name_destination"], kwargs["app_name_model_destination"]

            super().__init__(*args, **kwargs)

    class TextField(Base, models.TextField):
        class Meta:
            abstract = True

        class_custom_default_attrs = {
            "class_name": "Model",
            "field_name": "Text Field",
            "blank": True,
            "null": True,
            "max_length": 1000,
            # "validators": None
            }

        def __init__(self, *args, **kwargs):
            for key, value in CustomDefaultField.TextField.class_custom_default_attrs.items():
                kwargs[key] = kwargs.get(key, value)
            super().__init__(*args, **kwargs)

    class BooleanField(Base, models.BooleanField):
        class Meta:
            abstract = True

        class_custom_default_attrs = {
            "class_name": "Model",
            "field_name": "Boolean Field",
            "null": False,
            "blank": False,
            "default": False,
            "db_index": False,
            }

        def __init__(self, *args, **kwargs):
            for key, value in CustomDefaultField.BooleanField.class_custom_default_attrs.items():
                kwargs[key] = kwargs.get(key, value)

            super().__init__(*args, **kwargs)

    class DateTimeField(Base, models.DateTimeField):
        class Meta:
            abstract = True

        class_custom_default_attrs = {
            "class_name": "Model",
            "field_name": "Date Time Field",
            "blank": False,
            "null": False,
            }

        def __init__(self, *args, **kwargs):
            for key, value in CustomDefaultField.DateTimeField.class_custom_default_attrs.items():
                kwargs[key] = kwargs.get(key, value)

            super().__init__(*args, **kwargs)

    class BigAutoField(Base, models.BigAutoField):
        class Meta:
            abstract = True

        class_custom_default_attrs = {
            "class_name": "Model",
            "field_name": "Big Auto Field",  #
            "primary_key": True,  # "auto_created": True,
            # "blank": True,
            # "null": False,
            "db_index": True,
            # "editable": False,
            }

        def __init__(self, *args, **kwargs):
            for key, value in CustomDefaultField.BigAutoField.class_custom_default_attrs.items():
                kwargs[key] = kwargs.get(key, value)

            super().__init__(*args, **kwargs)

    class Time(Base, models.TimeField):
        class Meta:
            abstract = True

        class_custom_default_attrs = {
            "class_name": "Model",
            "field_name": "Big Auto Field",  #
            "auto_now": False,
            "auto_now_add": False,
            'null': True,
            "blank": True
            }

        def __init__(self, *args, **kwargs):
            for key, value in CustomDefaultField.Time.class_custom_default_attrs.items():
                kwargs[key] = kwargs.get(key, value)

            super().__init__(*args, **kwargs)

    class FilePath(Base, models.FilePathField):
        class Meta:
            abstract = True

        class_custom_default_attrs = {
            "class_name": "Model",
            "field_name": "File Path Field",  #
            "path": CustomStringMaker.FilePath.path_gen,
            "recursive": True,
            "match": None,
            "allow_files": True,
            }

        def __init__(self, *args, **kwargs):
            for key, value in CustomDefaultField.FilePath.class_custom_default_attrs.items():
                kwargs[key] = kwargs.get(key, value)

            super().__init__(*args, **kwargs)

    class File(Base, models.FileField):
        class Meta:
            abstract = True

        class_custom_default_attrs = {
            "class_name": "Model",
            "field_name": "File Path Field",  #
            "path": CustomStringMaker.File.path_gen,
            "recursive": True,
            "match": None,
            "allow_files": True,
            }

        def __init__(self, *args, **kwargs):
            for key, value in CustomDefaultField.File.class_custom_default_attrs.items():
                kwargs[key] = kwargs.get(key, value)

            super().__init__(*args, **kwargs)

    class Email(Base, models.EmailField):
        class Meta:
            abstract = True

        class_custom_default_attrs = {
            "class_name": "Model",
            "field_name": "Email Field",
            'null': True,
            'blank': True,  #
            "validator": CustomValidators.EmailValidator,
            }

        def __init__(self, *args, **kwargs):
            for key, value in CustomDefaultField.Email.class_custom_default_attrs.items():
                kwargs[key] = kwargs.get(key, value)

            super().__init__(*args, **kwargs)

    class OneToOne(Base, models.OneToOneField):
        class Meta:
            abstract = True

        class_costum_default_attrs = {
            "class_name": "Model",
            "field_name": "One To One Key",  # "app_name_destination": "?", get
            # "app_name_model_destination": "?",get
            "blank": True,
            "db_index": True,
            "null": True,
            "on_delete": models.SET_NULL,
            "related_name": CustomStringMaker.ForeignKey.related_name_gen,
            "to": CustomStringMaker.ForeignKey.to_gen,
            # "validators":None,
            }

        # test CommentField
        # "kw_class_name" : "Product/User"
        # "kw_field_name" : "Comment"
        # "kw_app_name" : "Products"
        # "kw_class_model" : "Comment"
        # "kw_related_name" : "comment"
        def __init__(self, *args, **kwargs):
            for key, value in CustomDefaultField.OneToOne.class_costum_default_attrs.items():
                if key == "to":
                    kwargs[key] = kwargs.get(key, value(kwargs["app_name_destination"], kwargs["app_name_model_destination"]))
                elif key == "related_name":
                    kwargs[key] = kwargs.get(key, value(kwargs["class_name"], kwargs["app_name_model_destination"]))
                else:
                    kwargs[key] = kwargs.get(key, value)

            del kwargs["app_name_destination"], kwargs["app_name_model_destination"]
            super().__init__(*args, **kwargs)

    class BigInteger(Base, models.BigIntegerField):
        class Meta:
            abstract = True

        class_custom_default_attrs = {
            "class_name": "Model",
            "field_name": "Big Integer Field",  #
            'default': None,
            'null': True,
            'blank': True,
            }

        def __init__(self, *args, **kwargs):
            for key, value in CustomDefaultField.BigInteger.class_custom_default_attrs.items():
                kwargs[key] = kwargs.get(key, value)

            super().__init__(*args, **kwargs)

    class GenericForeignKey(Base, fields.GenericForeignKey):
        class Meta:
            abstract = True

        class_custom_default_attrs = {
            "class_name": "Model",
            "field_name": "Big Integer Field",  #
            "ct_field": "content_type",
            "fk_field": "object_id",
            }

        def __init__(self, *args, **kwargs):
            for key, value in CustomDefaultField.GenericForeignKey.class_custom_default_attrs.items():
                kwargs[key] = kwargs.get(key, value)

            super().__init__(*args, **kwargs)

    class GenericRelation(Base, fields.GenericRelation):
        class Meta:
            abstract = True

        class_custom_default_attrs = {
            "class_name": "Model",
            "field_name": "Generic Relation Field",  #
            "to": CustomStringMaker.ForeignKey.to_gen,
            "content_type_field": "content_type",
            "object_id_field": "object_id",
            "related_query_name": CustomStringMaker.ForeignKey.related_name_gen,
            }

        def __init__(self, *args, **kwargs):
            for key, value in CustomDefaultField.GenericRelation.class_custom_default_attrs.items():
                if key == "to":
                    kwargs[key] = kwargs.get(key, value(kwargs["app_name_destination"], kwargs["app_name_model_destination"]))
                elif key == "related_query_name":
                    kwargs[key] = kwargs.get(key, value(kwargs["class_name"], kwargs["app_name_model_destination"]))
                else:
                    kwargs[key] = kwargs.get(key, value)

            super().__init__(*args, **kwargs)
