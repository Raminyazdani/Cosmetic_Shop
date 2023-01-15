import re

from django.contrib.contenttypes import fields
from django.db import models
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField

from Core.utils.ProjectUtils import CustomStringMaker, CustomValidators

class BaseMethodCustomField:
    class Meta:
        abstract = True

    class DelClassName:
        class Meta:
            abstract = True

        def __init__(self, *args, **kwargs):
            res = re.findall('[A-Z][^A-Z]*', kwargs["class_name"])
            if len(res) > 1: kwargs["class_name"], kwargs["field_name"] = res[1], res[0]

            kwargs["verbose_name"] = kwargs.get("verbose_name", _(kwargs['class_name'] + f"`s {kwargs['field_name']}"))
            kwargs["help_text"] = kwargs.get("help_text", _(f"{kwargs['field_name']} of this {kwargs['class_name']} record"))

            del kwargs["class_name"], kwargs['field_name'],

            super().__init__(*args, **kwargs)

class CustomDefaultField:
    class Meta:
        abstract = True

    class Base(BaseMethodCustomField.DelClassName):
        class Meta:
            abstract = True

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        @staticmethod
        def kwargs_setter(kwargs, class_defaults, deleters = None):
            for key, value in class_defaults.items():
                if callable(value) and key not in ["on_delete"]:
                    kwargs[key] = kwargs.get(key, value(kwargs))
                else:
                    kwargs[key] = kwargs.get(key, value)
            if deleters:
                for key in deleters:
                    del kwargs[key]
            return kwargs

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
            deleters = None
            class_attrs = CustomDefaultField.CharField.class_custom_default_attrs
            kwargs = CustomDefaultField.Base.kwargs_setter(kwargs, class_attrs, deleters)
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
            kwargs = CustomDefaultField.Base.kwargs_setter(kwargs, CustomDefaultField.PositiveIntegerField.class_custom_default_attrs)
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
            deleters = None
            class_attrs = CustomDefaultField.DecimalField.class_custom_default_attrs
            kwargs = CustomDefaultField.Base.kwargs_setter(kwargs, class_attrs, deleters)
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
            deleters = None
            class_attrs = CustomDefaultField.SlugField.class_custom_default_attrs
            kwargs = CustomDefaultField.Base.kwargs_setter(kwargs, class_attrs, deleters)
            super().__init__(*args, **kwargs)

    class ForeignKey(Base, models.ForeignKey):
        class Meta:
            abstract = True

        class_custom_default_attrs = {
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

        def __init__(self, *args, **kwargs):
            deleters = ["app_name_destination", "app_name_model_destination"]
            class_attrs = CustomDefaultField.ForeignKey.class_custom_default_attrs
            kwargs = CustomDefaultField.Base.kwargs_setter(kwargs, class_attrs, deleters)

            super().__init__(*args, **kwargs)  # if kwargs["class_name"] == "ContentType":  #     kwargs["related_name"] = kwargs.get("related_name", CustomStringMaker.ContentType.related_name_gen(kwargs["class_name"]))  #     break

    class ContentTypes(Base, models.ForeignKey):
        class_custom_default_attrs = {
            "class_name": "Model",
            "field_name": "Content Type",  # "app_name_destination": "?", get
            # "app_name_model_destination": "?",get
            "blank": True,
            "db_index": True,
            "null": True,
            "on_delete": models.SET_NULL,
            "related_name": CustomStringMaker.ContentType.related_name_gen,
            "to": "ContentType",
            # "validators":None,
            }

        def __init__(self, *args, **kwargs):
            deleters = None
            class_attrs = CustomDefaultField.ContentTypes.class_custom_default_attrs
            kwargs = CustomDefaultField.Base.kwargs_setter(kwargs, class_attrs, deleters)
            super().__init__(*args, **kwargs)

    class ManyToManyField(Base, models.ManyToManyField):
        class Meta:
            abstract = True

        class_custom_default_attrs = {
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

        def __init__(self, *args, **kwargs):
            deleters = ["app_name_destination", "app_name_model_destination", "app_super_model"]
            class_attrs = CustomDefaultField.ManyToManyField.class_custom_default_attrs
            kwargs = CustomDefaultField.Base.kwargs_setter(kwargs, class_attrs, deleters)

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
            deleters = None
            class_attrs = CustomDefaultField.TextField.class_custom_default_attrs
            kwargs = CustomDefaultField.Base.kwargs_setter(kwargs, class_attrs, deleters)
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
            deleters = None
            class_attrs = CustomDefaultField.BooleanField.class_custom_default_attrs
            kwargs = CustomDefaultField.Base.kwargs_setter(kwargs, class_attrs, deleters)

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
            deleter = None
            class_attrs = CustomDefaultField.DateTimeField.class_custom_default_attrs
            kwargs = CustomDefaultField.Base.kwargs_setter(kwargs, class_attrs, deleter)
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
            deleter = None
            class_attrs = CustomDefaultField.BigAutoField.class_custom_default_attrs
            kwargs = CustomDefaultField.Base.kwargs_setter(kwargs, class_attrs, deleter)
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
            deleters = None
            class_attrs = CustomDefaultField.Time.class_custom_default_attrs
            kwargs = CustomDefaultField.Base.kwargs_setter(kwargs, class_attrs, deleters)
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
            deleters = None
            class_attrs = CustomDefaultField.FilePath.class_custom_default_attrs
            kwargs = CustomDefaultField.Base.kwargs_setter(kwargs, class_attrs, deleters)
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
            deleters = None
            class_attrs = CustomDefaultField.File.class_custom_default_attrs
            kwargs = CustomDefaultField.Base.kwargs_setter(kwargs, class_attrs, deleters)
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
            deleters = None
            class_attrs = CustomDefaultField.Email.class_custom_default_attrs
            kwargs = CustomDefaultField.Base.kwargs_setter(kwargs, class_attrs, deleters)
            super().__init__(*args, **kwargs)

    class OneToOne(Base, models.OneToOneField):
        class Meta:
            abstract = True

        class_custom_default_attrs = {
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

        def __init__(self, *args, **kwargs):
            deleters = ["app_name_destination", "app_name_model_destination"]
            class_attrs = CustomDefaultField.OneToOne.class_custom_default_attrs
            kwargs = CustomDefaultField.Base.kwargs_setter(kwargs, class_attrs, deleters)
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
            deleters = None
            class_attrs = CustomDefaultField.BigInteger.class_custom_default_attrs
            kwargs = CustomDefaultField.Base.kwargs_setter(kwargs, class_attrs, deleters)
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
            deleters = None
            class_attrs = CustomDefaultField.GenericForeignKey.class_custom_default_attrs
            kwargs = CustomDefaultField.Base.kwargs_setter(kwargs, class_attrs, deleters)
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
            deleters = None
            class_attrs = CustomDefaultField.GenericRelation.class_custom_default_attrs
            kwargs = CustomDefaultField.Base.kwargs_setter(kwargs, class_attrs, deleters)
            super().__init__(*args, **kwargs)

    class MultiSelect(MultiSelectField):
        class Meta:
            abstract = True

        class_custom_default_attrs = {
            "class_name": "Model",
            "field_name": "Multi Select Field",  #
            "choices": None,
            "max_choices": None,
            "max_length": None,
            "min_choices": None,
            "null": True,
            "blank": True,
            "db_index": True,
            "default": None,
            }

        def __init__(self, *args, **kwargs):
            deleters = None
            class_attrs = CustomDefaultField.MultiSelect.class_custom_default_attrs
            kwargs = CustomDefaultField.Base.kwargs_setter(kwargs, class_attrs, deleters)
            super().__init__(*args, **kwargs)
