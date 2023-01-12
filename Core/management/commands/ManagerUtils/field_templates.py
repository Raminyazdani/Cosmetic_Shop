class REQUIRED:
    initpy_Base = """
from .AbsoluteUrl import UrlName,UrlId,UrlPhone
from .Save import SaveId,SaveName,SaveNormal,SaveProduct,SaveParent,slugify
from .Str import Name,Title,PhoneNumber,ID
"""
    AbsoluteUrl = """
from Core.utils.ProjectUtils import GetNameSpaceProperty

class UrlPhone:
    class Meta:
        abstract = True

    \"\"\"
    Slug Mixin
    \"\"\"

    def get_absolute_url(self:object):
        \"\"\"
        Return absolute url
        :return:
        \"\"\"
        return GetNameSpaceProperty.abs_url_phone(self, self.__name__.lower())

class UrlName:
    class Meta:
        abstract = True

    \"\"\"
    Slug Mixin
    \"\"\"

    def get_absolute_url(self:object):
        \"\"\"
        Return absolute url
        :return:
        \"\"\"
        return GetNameSpaceProperty.abs_url_slug(self, self.__name__.lower())

class UrlId:
    class Meta:
        abstract = True

    \"\"\"
    Slug Mixin
    \"\"\"

    def get_absolute_url(self:object):
        \"\"\"
        Return absolute url
        :return:
        \"\"\"
        return GetNameSpaceProperty.abs_url_id(self, self.__name__.lower())

"""
    ModelForeigns = """
from django.utils.functional import cached_property

from Core.utils.ProjectUtils import GetNameSpaceProperty

class Parent:
    class Meta:
        abstract = True

    \"\"\"
    Brand Mixin
    \"\"\"

    @cached_property
    def parent_count(self,teststring=\"parent\",scopeparent=\"self\"):
        \"\"\"
        Return brand count
        :return:
        \"\"\"
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey
        return GetNameSpaceProperty.count(self, teststring,scopeparent)


    @cached_property
    def parent_name(self,teststring=\"parent\"):
        \"\"\"
        Return brand count
        :return:
        \"\"\"
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey

        return GetNameSpaceProperty.parent(self, teststring,scope = \"name\")
    @cached_property
    def parent_object(self,teststring=\"parent\"):
        \"\"\"
        Return brand count
        :return:
        \"\"\"
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey

        return GetNameSpaceProperty.parent(self, teststring,scope = \"nothing\")
    @cached_property
    def parent_slug(self,teststring=\"parent\"):
        \"\"\"
        Return brand count
        :return:
        \"\"\"
        # product   tag     brand       category        comment     onetoone    manytomany      foreignkey

        return GetNameSpaceProperty.parent(self, teststring,scope = \"slug\")

"""
    Save = """
from django.utils.text import slugify

class SaveNormal:
    class Meta:
        abstract = True

    \"\"\"
    Product Mixin
    \"\"\"

    def save(self, *args, **kwargs):
        \"\"\"
        Save product model Base
        :param args:
        :param kwargs:
        :return:
        \"\"\"
        super().save(*args, **kwargs)

class SaveId:
    class Meta:
        abstract = True

    \"\"\"
    Slug Mixin for id field
    \"\"\"

    def save(self, *args, **kwargs):
        \"\"\"
        Save slug field with id field
        :param args:
        :param kwargs:
        :return:
        \"\"\"
        slug = slugify(self.id)
        self.slug = slug
        super().save(*args, **kwargs)

class SaveName:
    class Meta:
        abstract = True

    \"\"\"
    Slug Mixin for name field
    \"\"\"

    def save(self: object, *args, **kwargs):
        \"\"\"
        Save slug field with name field
        :param args:
        :param kwargs:
        :return:
        \"\"\"
        slug = slugify(self.name)
        self.slug = slug
        super().save(*args, **kwargs)

class SaveParent:
    class Meta:
        abstract = True

    \"\"\"
    Slug Mixin for category field
    \"\"\"

    def save(self: object, *args, **kwargs):
        \"\"\"
        Save slug field with category field and parents
        :param args:
        :param kwargs:
        :return:
        \"\"\"
        parents = [slugify(parent) for parent in self.parent_name[::-1]]
        slug = parents + [self.slug]
        self.slug = \"/\".join(slug).lower()
        super().save(*args, **kwargs)
        if self.child is not None:
            childs = UpdateChilds.update_childs(self)
            for child in childs:
                child.save()


class UpdateChilds:
    class Meta:
        abstract=True
    @staticmethod
    def update_childs(object):
        \"\"\"
        Update childs
        :return:
        \"\"\"
        result = []
        if object.child is not None:
            for child in object.child.all():
                result.append(child)
                temp = UpdateChilds.update_childs(child)
                for item in temp:
                    result.append(item)
        return result
class SaveProduct:
    class Meta:
        abstract = True

    \"\"\"
    Product Mixin with category parents saving
    \"\"\"

    def save(self, *args, **kwargs):
        \"\"\"
        Save product model with categories parents
        :param args:
        :param kwargs:
        :return:
        \"\"\"
        if self.pk is None:
            super().save(*args, **kwargs)
        categories = self.category.all()
        categories_id = [x for x in categories.values_list('id', flat = True)]
        for category in categories:
            category_temp = category
            while category_temp.parent:
                category_temp = category_temp.parent
                categories_id.append(category_temp)
        categories_id = list(set(categories_id))
        print(categories_id)
        self.category.set(categories_id)
        super().save(*args, **kwargs)

class SaveCategory:
    class Meta:
        abstract = True

    \"\"\"
    Product Mixin with category parents saving
    \"\"\"

    def save(self:object, *args, **kwargs):
        \"\"\"
        Save product model with categories parents
        :param args:
        :param kwargs:
        :return:
        \"\"\"
        if self.id and self.parent :
            if self.id == self.parent.id:
                self.parent = None
        if self.pk is None:
            super().save(*args, **kwargs)
        super().save(*args, **kwargs)

"""
    Str = """
class ID:
    class Meta:
        abstract = True

    \"\"\"
    Str Mixin for id field
    \"\"\"

    def __str__(self:object):
        \"\"\"
        Return id field
        :return:  id field
        \"\"\"
        return self.id

class Name:
    class Meta:
        abstract = True

    \"\"\"
    Str Mixin for name field
    \"\"\"

    def __str__(self:object):
        \"\"\"
        Return name field
        :return:  name field
        \"\"\"
        return self.name

class PhoneNumber:
    class Meta:
        abstract = True

    \"\"\"
    Str Mixin for title field
    \"\"\"

    def __str__(self):
        \"\"\"
        Return title field
        :return:  title field
        \"\"\"
        return self.phone_number

class Title:
    class Meta:
        abstract = True

    \"\"\"
    Str Mixin for title field
    \"\"\"

    def __str__(self:object):
        \"\"\"
        Return title field
        :return:  title field
        \"\"\"
        return self.title

"""
    ProjectFields = """
from .DefaultFields import *
from .BigAutoFields import *
from .BigIntegerFields import *
from .BooleanFields import *
from .CharFields import *
from .DateTimeFields import *
from .DecimalFields import *
from .EmailFields import *
from .FilePathFields import *
from .ForeignKeyFields import *
from .GenericForeignKey import *
from .GenericRelation import *
from .FileFields import *
from .ManyToManyFields import *
from .OneToOneFields import *
from .PositiveIntegerFields import *
from .TimeFields import *
    
"""
    initpy_fields = """
    
"""

    REQUIRED_FILE_NAMES = {
        "initpy_Base": initpy_Base,
        "AbsoluteUrl": AbsoluteUrl,
        "ModelForeigns": ModelForeigns,
        "Save": Save,
        "Str": Str,
        "ProjectFields": ProjectFields,
        "initpy_fields": initpy_fields
        }

class Header:
    DefaultFields = r"""
import re
from django.contrib.contenttypes import fields


from django.db import models
from django.utils.translation import gettext_lazy as _

from Core.utils.ProjectUtils import CustomStringMaker,CustomValidators

class BaseMethodCustomField:
    class Meta:
        abstract=True
    

    class DelClassName:
        class Meta:
            abstract=True
        
        
        def __init__(self, *args, **kwargs):
           
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
        abstract=True
        
    class Base(BaseMethodCustomField.DelClassName):
        class Meta:
            abstract=True
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
"""
    BigAutoFields = r"""
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
"""
    BigIntegerFields = r"""
    class BigInteger(Base,models.BigIntegerField):
        class Meta:
            abstract = True

        class_custom_default_attrs = {
            "class_name": "Model",
            "field_name": "Big Integer Field",  #
            'default': None,
            'null':True,
            'blank':True,
            }

        def __init__(self, *args, **kwargs):
            for key, value in CustomDefaultField.BigInteger.class_custom_default_attrs.items():
                kwargs[key] = kwargs.get(key, value)

            super().__init__(*args, **kwargs)

"""
    BooleanFields = r"""
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

"""
    CharFields = r"""
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
"""
    DateTimeFields = r"""
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
"""
    DecimalFields = r"""
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

"""
    EmailFields = r"""
    class Email(Base,models.EmailField):
        class Meta:
            abstract = True

        class_custom_default_attrs = {
            "class_name": "Model",
            "field_name": "Email Field",  
            'null':True,
            'blank':True,#
            "validator": CustomValidators.EmailValidator,
            }

        def __init__(self, *args, **kwargs):
            for key, value in CustomDefaultField.Email.class_custom_default_attrs.items():
                kwargs[key] = kwargs.get(key, value)

            super().__init__(*args, **kwargs)
            
"""
    FilePathFields = r"""
    class FilePath(Base,models.FilePathField):
        class Meta:
            abstract = True

        class_custom_default_attrs = {
            "class_name": "Model",
            "field_name": "File Path Field",  #
            "path":CustomStringMaker.FilePath.path_gen,
            "recursive":True,
            "match":None,
            "allow_files":True,
            }

        def __init__(self, *args, **kwargs):
            for key, value in CustomDefaultField.FilePath.class_custom_default_attrs.items():
                kwargs[key] = kwargs.get(key, value)

            super().__init__(*args, **kwargs)

"""
    ForeignKey = r"""
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
                    kwargs["related_name"]=kwargs.get("related_name", CustomStringMaker.ContentType.related_name_gen(kwargs["class_name"]))
                    break
                if key == "to":
                    kwargs[key] = kwargs.get(key, value(kwargs["app_name_destination"], kwargs["app_name_model_destination"]))
                elif key == "related_name":
                    kwargs[key] = kwargs.get(key, value(kwargs["class_name"], kwargs["app_name_model_destination"]))
                else:
                    kwargs[key] = kwargs.get(key, value)

            del kwargs["app_name_destination"], kwargs["app_name_model_destination"]
            super().__init__(*args, **kwargs)

"""
    GenericForeignKey = r"""
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

"""
    GenericRelation = r"""
    class GenericRelation(Base, fields.GenericRelation):
        class Meta:
            abstract = True

        class_custom_default_attrs = {
            "class_name": "Model",
            "field_name": "Generic Relation Field",  #
            "to":CustomStringMaker.ForeignKey.to_gen,
            "content_type_field": "content_type",
            "object_id_field": "object_id",
            "related_query_name":CustomStringMaker.ForeignKey.related_name_gen,
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


"""
    FileFields = r"""
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
            for key, value in CustomDefaultField.FilePath.class_custom_default_attrs.items():
                kwargs[key] = kwargs.get(key, value)

            super().__init__(*args, **kwargs)

"""
    ManyToManyFields = r"""
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

"""
    OneToOneFields = r"""
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

"""
    PositiveIntegerFields = r"""
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

"""
    SlugFields=r"""
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

"""
    TimeFields = r"""
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

"""
    TextFields = r"""
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

    """
    ABSTRACT_CLASS_NAME = {
        "DefaultFields": DefaultFields,
        "BigAutoFields": BigAutoFields,
        "BigIntegerFields": BigIntegerFields,
        "BooleanFields": BooleanFields,
        "CharFields": CharFields,
        "DateTimeFields": DateTimeFields,
        "DecimalFields": DecimalFields,
        "EmailFields": EmailFields,
        "FilePathFields":FilePathFields,
        "ForeignKey": ForeignKey,
        "GenericForeignKey":GenericForeignKey,
        "GenericRelation": GenericRelation,
        "FileFields":FileFields,
        "ManyToManyFields": ManyToManyFields,
        "OneToOneFields": OneToOneFields,
        "PositiveIntegerFields": PositiveIntegerFields,
        "SlugFields": SlugFields,
        "TextFields":TextFields,
        "TimeFields": TimeFields,


        }

class Body:
    DefaultFields = r"""
"""
    BigAutoFields = r"""
"""
    BigIntegerFields = r"""
"""
    BooleanFields = r"""
"""
    CharFields = r"""
"""
    DateTimeFields = r"""
"""
    DecimalFields = r"""
"""
    EmailFields = r"""
"""
    FilePathFields = r"""
"""
    ForeignKeyFields = r"""
"""
    GenericForeignKey = r"""
"""
    GenericRelation = r"""
"""
    FileFields = r"""
"""
    ManyToManyFields = r"""
"""
    OneToOneFields = r"""
"""
    PositiveIntegerFields = r"""
"""
    SlugFields=r"""
"""
    TextFields=r"""
"""
    TimeFields = f"""
"""

