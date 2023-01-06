from django.db import models
from django.utils.translation import gettext_lazy as _

# Core imports
from Core.utils.ProjectUtils import CustomValidators


class BaseMethodCustomField :
    """
    Base Method Custom Field
    """

    class DelClassName :
        """
         This class is used to delete the class_name argument from the kwargs
        """

        def __init__(self , *args , **kwargs) :
            """
            This method is used to delete the class_name argument from the kwargs
            :param args:
            :param kwargs:
            """
            kwargs["verbose_name"] = kwargs.get("verbose_name" , _(kwargs['class_name'] + f"`s {kwargs['field_name']}"))
            kwargs["help_text"] = kwargs.get("help_text" , _(f"{kwargs['field_name']} of this {kwargs['class_name']} record"))

            del kwargs["class_name"] , kwargs['field_name'] ,
            super().__init__(*args , **kwargs)

    # class GetClassName:  #     def __init__(self, *args, **kwargs):  #         kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"].capitalize()  #         self.class_name = kwargs["class_name"].capitalize()  #

class CustomDefaultField :
    class Base(BaseMethodCustomField.DelClassName) :

        def __init__(self , *args , **kwargs) :
            super().__init__(*args , **kwargs)

    class CharField(Base , models.CharField) :
        class_field_name = "Char Field"
        class_costum_default_attrs = {
            "db_index" : False , "unique" : False , "max_length" : 30
            }

        def __init__(self , *args , **kwargs) :
            kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()
            kwargs["db_index"] = kwargs.get("db_index" , __class__.class_costum_default_attrs["db_index"])

            kwargs["unique"] = kwargs.get("unique" , __class__.class_costum_default_attrs["unique"])
            kwargs['max_length'] = kwargs.get('max_length' , __class__.class_costum_default_attrs["max_length"])

            super().__init__(*args , **kwargs)

    class PositiveIntegerField(Base , models.PositiveIntegerField) :
        class_field_name = "Positive Integer Field"
        class_costum_default_attrs = {
            "db_index" : True ,

            }

        def __init__(self , *args , **kwargs) :
            kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()
            kwargs["db_index"] = kwargs.get("db_index" , __class__.class_costum_default_attrs["db_index"])

            kwargs["null"] = kwargs.get("null" , False)

            super().__init__(*args , **kwargs)

    class DecimalField(Base , models.DecimalField) :
        class_field_name = "Decimal Field"
        class_costum_default_attrs = {
            'blank' : False , 'db_index' : True , 'decimal_places' : 2 , 'default' : 0.0 , 'max_digits' : 10 , 'null' : False ,
            }

        def __init__(self , *args , **kwargs) :
            kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()
            kwargs["blank"] = kwargs.get("blank" , __class__.class_costum_default_attrs["blank"])
            kwargs["db_index"] = kwargs.get("db_index" , __class__.class_costum_default_attrs["db_index"])
            kwargs["decimal_places"] = kwargs.get("decimal_places" , __class__.class_costum_default_attrs["decimal_places"])
            kwargs["default"] = kwargs.get("default" , __class__.class_costum_default_attrs["default"])
            kwargs["max_digits"] = kwargs.get("max_digits" , __class__.class_costum_default_attrs["max_digits"])
            kwargs["null"] = kwargs.get("null" , __class__.class_costum_default_attrs["null"])

            super().__init__(*args , **kwargs)

    class SlugField(Base , models.SlugField) :
        class_field_name = "Slug Field"
        class_costum_default_attrs = {
            'blank' : True , 'db_index' : True , 'max_length' : 100 , 'null' : True , 'unique' : True ,
            }

        def __init__(self , *args , **kwargs) :
            kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()
            kwargs["blank"] = kwargs.get("blank" , __class__.class_costum_default_attrs["blank"])
            kwargs["db_index"] = kwargs.get("db_index" , __class__.class_costum_default_attrs["db_index"])
            kwargs["max_length"] = kwargs.get("max_length" , __class__.class_costum_default_attrs["max_length"])
            kwargs["null"] = kwargs.get("null" , __class__.class_costum_default_attrs["null"])
            kwargs["unique"] = kwargs.get("unique" , __class__.class_costum_default_attrs["unique"])
            super().__init__(*args , **kwargs)

    class ForeignKey(Base , models.ForeignKey) :
        class_field_name = "Foreign Key"
        class_costum_default_attrs = {

            }

        # test CommentField
        # "kw_class_name" : "Product/User"
        # "kw_field_name" : "Comment"
        # "kw_app_name" : "Products"
        # "kw_class_model" : "Comment"
        # "kw_related_name" : "comment"
        def __init__(self , *args , **kwargs) :
            kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()
            kwargs["blank"] = kwargs.get("blank" , True)
            kwargs["db_index"] = kwargs.get("db_index" , True)
            kwargs["null"] = kwargs.get("null" , True)
            kwargs["on_delete"] = kwargs.get("on_delete" , models.SET_NULL)

            kwargs["to"] = kwargs.get("to" , f"{kwargs['app_name']}.{kwargs['class_model']}")
            kwargs["related_name"] = kwargs.get("related_name" , f"{kwargs['class_name'].lower()}_{kwargs['related_name_def']}")
            del kwargs["app_name"] , kwargs["class_model"] , kwargs["related_name_def"]
            super().__init__(*args , **kwargs)

    class ManyToManyField(Base , models.ManyToManyField) :
        class_field_name = "Many To Many Field"
        class_costum_default_attrs = {

            }

        # class_name = ProductCategory #dynamic
        # field_name = Category #dynamic/static
        # app_name = Products #static
        # class_model = Category #static
        # class_field_name = Category #static
        # class_related_name = category #static
        # class_through_fields = ('?', 'category') #static
        def __init__(self , *args , **kwargs) :
            kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()
            kwargs["blank"] = kwargs.get("blank" , True)
            kwargs["db_index"] = kwargs.get("db_index" , True)

            kwargs["to"] = kwargs.get("to" , f"{kwargs['app_name']}.{kwargs['class_model']}")
            kwargs["related_name"] = kwargs.get("related_name" , f"{kwargs['class_name'].lower()}_{kwargs['related_name_def']}")
            if kwargs["through_fields_def"][0] is None :
                through_field_1 = f"{kwargs['class_name'].lower()}_id"
                through_field_2 = f"{kwargs['through_fields_def'][1].lower()}_id"
                through_fields = (through_field_1 , through_field_2)

                kwargs["through"] = kwargs.get("through" , f"{kwargs['class_name']}{kwargs['class_model']}")
                kwargs["through_fields"] = kwargs.get("through_fields" , through_fields)
            if kwargs["through_fields_def"][1] is None :
                through_field_2 = f"{kwargs['through_fields_def'][0].lower()}_id"
                through_field_1 = f"{kwargs['class_name'].lower()}_id"
                through_fields = (through_field_1 , through_field_2)

                kwargs["through"] = kwargs.get("through" , f"{kwargs['class_model']}{kwargs['class_name'].capitalize()}")
                kwargs["through_fields"] = kwargs.get("through_fields" , through_fields)

            del kwargs["app_name"] , kwargs["class_model"] , kwargs["related_name_def"] , kwargs["through_fields_def"]

            super().__init__(*args , **kwargs)

    class TextField(Base , models.TextField) :
        class_field_name = "Text Field"
        class_costum_default_attrs = {
            'blank' : True , 'null' : True , 'max_length' : 1000 ,

            }

        def __init__(self , *args , **kwargs) :
            kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()
            kwargs["blank"] = kwargs.get("blank" , __class__.class_costum_default_attrs["blank"])
            kwargs['null'] = kwargs.get("null" , __class__.class_costum_default_attrs["null"])
            kwargs['max_length'] = kwargs.get("max_length" , __class__.class_costum_default_attrs["max_length"])
            super().__init__(*args , **kwargs)

    class BooleanField(Base , models.BooleanField) :
        class_field_name = "Boolean Field"
        class_costum_default_attrs = {
            "null" : False , "blank" : True , "default" : False , "db_index" : True ,
            }

        def __init__(self , *args , **kwargs) :
            kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()
            kwargs["blank"] = kwargs.get("blank" , __class__.class_costum_default_attrs["blank"])
            kwargs["null"] = kwargs.get("null" , __class__.class_costum_default_attrs["null"])
            kwargs["default"] = kwargs.get("default" , __class__.class_costum_default_attrs["default"])
            kwargs["db_index"] = kwargs.get("db_index" , __class__.class_costum_default_attrs["db_index"])

            super().__init__(*args , **kwargs)

    class DateTimeField(Base , models.DateTimeField) :
        class_field_name = "Date Time Field"
        class_costum_default_attrs = {
            'blank' : True , 'null' : True ,
            }

        def __init__(self , *args , **kwargs) :
            kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()
            kwargs["blank"] = kwargs.get("blank" , __class__.class_costum_default_attrs["blank"])
            kwargs['null'] = kwargs.get("null" , __class__.class_costum_default_attrs["null"])

            super().__init__(*args , **kwargs)

    class BigAutoField(Base , models.BigAutoField) :
        class_field_name = "Big Auto Field"
        class_costum_default_attrs = {

            }

        def __init__(self , *args , **kwargs) :
            kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()

            super().__init__(*args , **kwargs)

class CustomNameField(CustomDefaultField.CharField) :
    """
    Custom Name Field as CharField
    """
    class_field_name = "name"
    class_costum_default_attrs = {
        "db_index" : True , 'unique' : True ,
        }
    class_validator = CustomValidators.NameValidator

    def __init__(self , *args , **kwargs) :
        """
        Custom Name Field
        :required kwargs key : class_name
        :param args:  args for models.CharField class constructor
        :param kwargs:  kwargs for models.CharField class constructor
        :custom default kwargs: 'class_name' : class name of model that use this field
        :custom default kwargs: 'validators' : CustomValidators.NameValidator
        :custom default kwargs: 'max_length' : 30
        :custom default kwargs: 'verbose_name' : '{kwargs['class_name']} + "`s Name"
        :custom default kwargs: 'unique' : True
        :custom default kwargs: 'db_index' : True
        :custom default kwargs: 'help_text' : 'Name of this {kwargs['class_name']} record'
        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"].capitalize()
        kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()

        kwargs['validators'] = kwargs.get('validators' , __class__.class_validator)
        kwargs["unique"] = kwargs.get("unique" , __class__.class_costum_default_attrs["unique"])
        kwargs["db_index"] = kwargs.get("db_index" , __class__.class_costum_default_attrs["db_index"])
        super().__init__(*args , **kwargs)

class CustomTitleField(CustomDefaultField.CharField) :
    """
    Custom Title Field as CharField
    """
    class_field_name = "title"
    class_costum_default_attrs = {
        "max_length" : 20
        }
    class_validator = CustomValidators.TitleValidator

    def __init__(self , *args , **kwargs) :
        """
        Custom Title Field
        :required kwargs key : class_name
        :param args:  args for models.CharField class constructor
        :param kwargs:  kwargs for models.CharField class constructor
        :custom default kwargs: 'class_name' : class name of model that use this field
        :custom default kwargs: 'db_index' : True
        :custom default kwargs: 'help_text' : 'Title of this {kwargs['class_name']} record'
        :custom default kwargs: 'max_length' : 20
        :custom default kwargs: 'unique' : True
        :custom default kwargs: 'validators' : CustomValidators.TitleValidator
        :custom default kwargs: 'verbose_name' : '{kwargs['class_name']} + "`s Title"
        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"].capitalize()
        kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()

        kwargs['max_length'] = kwargs.get('max_length' , __class__.class_costum_default_attrs["max_length"])

        kwargs['validators'] = kwargs.get('validators' , __class__.class_validator)

        super().__init__(*args , **kwargs)

class CustomShortDescriptionField(CustomDefaultField.CharField) :
    """
    Custom Short Description Field as CharField

    """
    class_field_name = "short description"
    class_costum_default_attrs = {
        "max_length" : 100 , "blank" : False , "null" : False
        }
    class_validator = CustomValidators.ShortDescriptionValidator

    def __init__(self , *args , **kwargs) :
        """
        Custom Short Description Field
        :param args:  args for models.CharField class constructor
        :param kwargs: kwargs for models.CharField class constructor
        :required kwargs key : class_name
        :custom default kwargs: "blank" : "blank", False
        :custom default kwargs: "help_text" : "help_text", _(f"Short description of this {kwargs['class_name']} record")
        :custom default kwargs: "max_length" : "max_length", 100
        :custom default kwargs: "null" : "null", False
        :custom default kwargs: "verbose_name" : "verbose_name", _(kwargs['class_name'] + "`s Short Description")
        :custom default kwargs: 'validators' : 'validators', CustomValidators.ShortDescriptionValidator

        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"].capitalize()
        kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()

        kwargs["blank"] = kwargs.get("blank" , __class__.class_costum_default_attrs["blank"])
        kwargs["max_length"] = kwargs.get("max_length" , __class__.class_costum_default_attrs["max_length"])
        kwargs["null"] = kwargs.get("null" , __class__.class_costum_default_attrs["null"])
        kwargs['validators'] = kwargs.get('validators' , __class__.class_validator)

        super().__init__(*args , **kwargs)

class CustomPhoneNumberField(CustomDefaultField.CharField) :
    """
    Custom Phone Number Field as CharField

    """

    class_field_name = "phone number"
    class_costum_default_attrs = {
        'max_length' : 15 , 'db_index' : True , 'unique' : True ,
        }
    class_validator = CustomValidators.PhoneValidator

    def __init__(self , *args , **kwargs) :
        """
        Custom Phone Number Field
        :param args:  args for models.CharField class constructor
        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"].capitalize()
        kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()
        kwargs['max_length'] = kwargs.get('max_length' , __class__.class_costum_default_attrs['max_length'])
        kwargs['db_index'] = kwargs.get('db_index' , __class__.class_costum_default_attrs['db_index'])
        kwargs['unique'] = kwargs.get('unique' , __class__.class_costum_default_attrs['unique'])
        kwargs['help_text'] = kwargs.get('help_text' , _(f"Phone number of this {kwargs['class_name']} record"))
        kwargs['validators'] = kwargs.get('validators' , __class__.class_validator)
        super().__init__(*args ,**kwargs)
class CustomGenderField(CustomDefaultField.PositiveIntegerField) :
    """
    Custom Gender Field as PositiveIntegerField
    Choices are defined as class variables so that they can be easily accessed from instances.
    includes: UNISEX, MALE , FEMALE
    """
    UNISEX = 0
    MALE = 1
    FEMALE = 2
    GENDER_CHOICES = ((UNISEX , _('Gender free')) , (MALE , _('For men')) , (FEMALE , _('For women')) ,)
    GENDER = GENDER_CHOICES

    class_field_name = "Gender"
    class_costum_default_attrs = {
        "choices" : GENDER_CHOICES , "default" : UNISEX ,
        }

    class_validator = CustomValidators.GenderValidator

    def __init__(self , *args , **kwargs) :
        """
        Custom Gender Field
        :required kwargs key : class_name
        :param args:  args for models.PositiveIntegerField class constructor
        :param kwargs:  kwargs for models.PositiveIntegerField class constructor
        :custom default kwargs: 'choices' : CustomGenderField
        :custom default kwargs: 'class_name' : class name of model that use this field
        :custom default kwargs: 'db_index' : True
        :custom default kwargs: 'default' : CustomGenderField.UNISEX
        :custom default kwargs: 'help_text' : "Men/Women/Gender-free"
        :custom default kwargs: 'null' : False
        :custom default kwargs: 'validators' : CustomValidators.GenderValidator
        :custom default kwargs: 'verbose_name' : '{kwargs['class_name']}' + "`s Gender"
        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"].capitalize()
        kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()

        kwargs["choices"] = kwargs.get("choices" , __class__.class_costum_default_attrs["choices"])
        kwargs["default"] = kwargs.get("default" , __class__.class_costum_default_attrs["default"])
        kwargs["help_text"] = kwargs.get("help_text" , _("UNISEX/MALE/FEMALE as integers"))

        kwargs["verbose_name"] = kwargs.get("verbose_name" , _(kwargs['class_name'] + f"`s {kwargs['field_name']}"))
        kwargs['validators'] = kwargs.get('validators' , __class__.class_validator)
        super().__init__(*args , **kwargs)

class CustomRatingField(CustomDefaultField.PositiveIntegerField) :
    """
    Custom Rating Field as PositiveIntegerField

    """

    class_field_name = "Rating"
    class_costum_default_attrs = {

        }
    class_validator = CustomValidators.RatingValidator

    def __init__(self , *args , **kwargs) :
        """
        Custom Rating Field
        :param args:  args for models.PositiveIntegerField class constructor
        :param kwargs:  kwargs for models.PositiveIntegerField class constructor
        :required kwargs key : class_name
        :custom default kwargs: "verbose_name" : "verbose_name", _(kwargs['class_name'] + "`s Rating")
        :custom default kwargs: 'db_index' : True
        :custom default kwargs: "help_text" : "help_text", _(f"Rating of this {kwargs['class_name']} record")
        :custom default kwargs: 'validators' : 'validators', CustomValidators.RatingValidator

        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"].capitalize()
        kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()

        kwargs['validators'] = kwargs.get('validators' , __class__.class_validator)

        super().__init__(*args , **kwargs)

class CustomPriceFieldDollar(CustomDefaultField.DecimalField) :
    """
    Custom Price Field as DecimalField

    """
    class_field_name = "Dollar Price"
    class_costum_default_attrs = {
        "decimal_places" : 2 , "max_digits" : 10 ,
        }
    class_validator = CustomValidators.PriceValidator

    def __init__(self , *args , **kwargs) :
        """
        Custom Price Field
        :param args:  args for models.DecimalField class constructor
        :param kwargs:  kwargs for models.DecimalField class constructor
        :required kwargs key : class_name
        :custom default kwargs: "verbose_name" : "verbose_name", _(kwargs['class_name'] + "`s Price")
        :custom default kwargs: "help_text" : "help_text", _(f"Dollar Price of this {kwargs['class_name']} record")
        :custom default kwargs: "blank" : "blank", False
        :custom default kwargs: "null" : "null", False
        :custom default kwargs: "max_digits" : "max_digits", 10
        :custom default kwargs: "decimal_places" : "decimal_places", 2
        :custom default kwargs: "default" : "default", 0.0
        :custom default kwargs: "db_index" : "db_index", True
        :custom default kwargs: 'validators' : 'validators', CustomValidators.PriceValidator
        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"].capitalize()
        kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()
        kwargs["max_digits"] = kwargs.get("max_digits" , __class__.class_costum_default_attrs["max_digits"])
        kwargs["decimal_places"] = kwargs.get("decimal_places" , __class__.class_costum_default_attrs["decimal_places"])
        kwargs['validators'] = kwargs.get('validators' , __class__.class_validator)
        super().__init__(*args , **kwargs)

class CustomSlugField(CustomDefaultField.SlugField) :
    """
    Custom Slug Field as SlugField
    """

    class_field_name = "Slug"
    class_costum_default_attrs = {

        }
    class_validator = None

    def __init__(self , *args , **kwargs) :
        """
        Custom Slug Field
        :required kwargs key : class_name
        :param args:  args for models.SlugField class constructor
        :param kwargs:  kwargs for models.SlugField class constructor
        :custom default kwargs: 'blank' : True
        :custom default kwargs: 'class_name' : class name of model that use this field
        :custom default kwargs: 'db_index' : True
        :custom default kwargs: 'help_text' : 'Slug of this {kwargs['class_name']} record'
        :custom default kwargs: 'max_length' : 100
        :custom default kwargs: 'null' : True
        :custom default kwargs: 'unique' : True
        :custom default kwargs: 'verbose_name' : '{kwargs['class_name']}' + "`s Slug"
        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"].capitalize()
        kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()

        super().__init__(*args , **kwargs)

class CustomCommentFieldForeignKey(CustomDefaultField.ForeignKey) :
    """
    Custom Comment Field as ForeignKey
    """
    class_app_name = "Products"
    class_model = "Comment"
    class_field_name = "Comment"
    class_related_name = "comment"
    class_costum_default_attrs = {

        }
    class_validator = None

    def __init__(self , *args , **kwargs) :
        """
        Custom Comment Field
        :required kwargs key : class_name
        :param args:  args for models.ForeignKey class constructor
        :param kwargs:  kwargs for models.ForeignKey class constructor
        :custom default kwargs: 'class_name' : class name of model that use this field
        :custom default kwargs: 'null' : True
        :custom default kwargs: 'on_delete' : models.CASCADE
        :custom default kwargs: 'related_name' : '{kwargs['class_name']}' + "_comment"
        :custom default kwargs: 'to' : 'Product.Comment'
        :custom default kwargs: 'verbose_name' : '{kwargs['class_name']}' + "`s Comment":custom default kwargs: 'blank' : True
        """
        # "kw_class_name" : "Product/User"
        # "kw_field_name" : "Comment"
        # "kw_app_name" : "Products"
        # "kw_class_model" : "Comment"
        # "kw_related_name" : "comment"
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"].capitalize()
        kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()
        kwargs["app_name"] , kwargs["class_model"] , kwargs["related_name_def"] = __class__.class_app_name , __class__.class_model , __class__.class_related_name
        super().__init__(*args , **kwargs)

class CustomCategoryParentFieldForeignKey(CustomDefaultField.ForeignKey) :
    """
    Custom Category Parent Field as ForeignKey

    """

    class_app_name = "Products"
    class_model = "Category"
    class_field_name = "Category parent"
    class_related_name = "parent"
    class_costum_default_attrs = {

        }
    class_validator = None

    def __init__(self , *args , **kwargs) :
        """
        Custom Category Parent Field
        :required kwargs key : class_name
        :param args:  args for models.ForeignKey class constructor
        :param kwargs:  kwargs for models.ForeignKey class constructor
        :custom default kwargs: "blank" : "blank", True
        :custom default kwargs: "db_index" : "db_index", True
        :custom default kwargs: "help_text" : "help_text", _(f"Parent of this {kwargs['class_name']} record")
        :custom default kwargs: "null" : "null", True
        :custom default kwargs: "on_delete" : "on_delete", models.SET_NULL
        :custom default kwargs: "related_name" : "related_name", f"{kwargs['class_name'].lower()}_parent"
        :custom default kwargs: "to" : "to", "Products.Category"
        :custom default kwargs: "verbose_name" : "verbose_name", _(kwargs['class_name'] + "`s Parent")

        """
        # "kw_class_name" : "Category"
        # "kw_field_name" : "Category parent"
        # "kw_app_name" : "Products"
        # "kw_class_model" : "Category"
        # "kw_related_name" : "parent"
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"].capitalize()
        kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()
        kwargs["app_name"] , kwargs["class_model"] , kwargs["related_name_def"] = __class__.class_app_name , __class__.class_model , __class__.class_related_name
        super().__init__(*args , **kwargs)

class CustomUserFieldForeignKey(CustomDefaultField.ForeignKey) :
    """
    Custom User Field as ForeginKey

    """
    class_app_name = "Users"
    class_model = "User"
    class_field_name = "User"
    class_related_name = "user"
    class_costum_default_attrs = {

        'blank' : False , 'null' : True ,
        }
    class_validator = None

    def __init__(self , *args , **kwargs) :
        """
        Custom User Field
        :param args:  args for models.ForeignKey class constructor
        :param kwargs:  kwargs for models.ForeignKey class constructor
        :required kwargs key : class_name
        :custom default kwargs: "blank" : "blank", True
        :custom default kwargs: "db_index" : "db_index", True
        :custom default kwargs: "help_text" : "help_text", _(f"User of this {kwargs['class_name']} record")
        :custom default kwargs: "null" : "null", True
        :custom default kwargs: "on_delete" : "on_delete", models.SET_NULL
        :custom default kwargs: "related_name" : "related_name", f"{kwargs['class_name'].lower()}_user"
        :custom default kwargs: "to" : "to", "Users.User"
        :custom default kwargs: "verbose_name" : "verbose_name", _(kwargs['class_name'] + "`s User")
        """

        # "kw_class_name" : "Comment/Product/Profile"
        # "kw_field_name" : "User"
        # "kw_app_name" : "Users"
        # "kw_class_model" : "User"
        # "kw_related_name" : "user"

        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"].capitalize()
        kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()
        kwargs["app_name"] , kwargs["class_model"] , kwargs["related_name_def"] = __class__.class_app_name , __class__.class_model , __class__.class_related_name

        kwargs["blank"] = kwargs.get("blank" , __class__.class_costum_default_attrs["blank"])
        kwargs["null"] = kwargs.get("null" , __class__.class_costum_default_attrs["null"])

        super().__init__(*args , **kwargs)

class CustomProductFieldForeignKey(CustomDefaultField.ForeignKey) :
    """
    Custom Product Field as ForeignKey

    """

    class_app_name = "Products"
    class_model = "Product"
    class_field_name = "Product"
    class_related_name = "product"
    class_costum_default_attrs = {

        }
    class_validator = None

    def __init__(self , *args , **kwargs) :
        """
        Custom Product Field
        :param args:  args for models.ForeignKey class constructor
        :param kwargs:  kwargs for models.ForeignKey class constructor
        :required kwargs key : class_name
        :custom default kwargs: "blank" : "blank", True
        :custom default kwargs: "db_index" : "db_index", True
        :custom default kwargs: "help_text" : "help_text", _(f"Product of this {kwargs['class_name']} record")
        :custom default kwargs: "null" : "null", True
        :custom default kwargs: "on_delete" : "on_delete", models.SET_NULL
        :custom default kwargs: "related_name" : "related_name", f"{kwargs['class_name'].lower()}_product"
        :custom default kwargs: "to" : "to", "Products.Product"
        :custom default kwargs: "verbose_name" : "verbose_name", _(kwargs['class_name'] + "`s Product")
        """

        # "kw_class_name" : "Comment/ProductCategory/ProductBrand/ProductTag"
        # "kw_field_name" : "Product"
        # "kw_app_name" : "Products"
        # "kw_class_model" : "Product"
        # "kw_related_name" : "product"
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"].capitalize()
        kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()
        kwargs["app_name"] , kwargs["class_model"] , kwargs["related_name_def"] = __class__.class_app_name , __class__.class_model , __class__.class_related_name
        super().__init__(*args , **kwargs)

class CustomCategoryFieldForeignKey(CustomDefaultField.ForeignKey) :
    """
    Custom Category Field as ForeignKey

    """
    class_app_name = "Products"
    class_model = "Category"
    class_field_name = "Category"
    class_related_name = "category"
    class_costum_default_attrs = {

        }
    class_validator = None

    def __init__(self , *args , **kwargs) :
        """
        Custom Category Field
        :param args:  args for models.ForeignKey class constructor
        :param kwargs:  kwargs for models.ForeignKey class constructor
        :required kwargs key : class_name
        :custom default kwargs: "blank" : "blank", True
        :custom default kwargs: "db_index" : "db_index", True
        :custom default kwargs: "help_text" : "help_text", _(f"Category of this {kwargs['class_name']} record")
        :custom default kwargs: "null" : "null", True
        :custom default kwargs: "on_delete" : "on_delete", models.SET_NULL
        :custom default kwargs: "related_name" : "related_name", f"{kwargs['class_name'].lower()}_category"
        :custom default kwargs: "to" : "to", "Products.Category"
        :custom default kwargs: "verbose_name" : "verbose_name", _(kwargs['class_name'] + "`s Category")
        """
        # "kw_class_name" : "ProductCategory/Gallery"
        # "kw_field_name" : "Category"
        # "kw_app_name" : "Products"
        # "kw_class_model" : "Category"
        # "kw_related_name" : "category"
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"].capitalize()
        kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()
        kwargs["app_name"] , kwargs["class_model"] , kwargs["related_name_def"] = __class__.class_app_name , __class__.class_model , __class__.class_related_name
        super().__init__(*args , **kwargs)

class CustomTagFieldForeignKey(CustomDefaultField.ForeignKey) :
    """
    Custom Tag Field as ForeignKey

    """
    class_app_name = "Products"
    class_model = "Tag"
    class_field_name = "Tag"
    class_related_name = "tag"
    class_costum_default_attrs = {

        }
    class_validator = None

    def __init__(self , *args , **kwargs) :
        """
        Custom Tag Field
        :param args:  args for models.ForeignKey class constructor
        :param kwargs:  kwargs for models.ForeignKey class constructor
        :required kwargs key : class_name
        :custom default kwargs: "blank" : "blank", True
        :custom default kwargs: "db_index" : "db_index", True
        :custom default kwargs: "help_text" : "help_text", _(f"Tag of this {kwargs['class_name']} record")
        :custom default kwargs: "null" : "null", True
        :custom default kwargs: "on_delete" : "on_delete", models.SET_NULL
        :custom default kwargs: "related_name" : "related_name", f"{kwargs['class_name'].lower()}_tag"
        :custom default kwargs: "to" : "to", "Products.Tag"
        :custom default kwargs: "verbose_name" : "verbose_name", _(kwargs['class_name'] + "`s Tag")
        """
        # "kw_class_name" : "ProductTag/Gallery"
        # "kw_field_name" : "Tag"
        # "kw_app_name" : "Products"
        # "kw_class_model" : "Tag"
        # "kw_related_name" : "tag"
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"].capitalize()
        kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()
        kwargs["app_name"] , kwargs["class_model"] , kwargs["related_name_def"] = __class__.class_app_name , __class__.class_model , __class__.class_related_name
        super().__init__(*args , **kwargs)

class CustomBrandFieldForeignKey(CustomDefaultField.ForeignKey) :
    """
    Custom Brand Field as ForeignKey

    """
    class_app_name = "Products"
    class_model = "Brand"
    class_field_name = "Brand"
    class_related_name = "brand"
    class_costum_default_attrs = {

        }
    class_validator = None

    def __init__(self , *args , **kwargs) :
        """
        Custom Brand Field
        :param args:  args for models.ForeignKey class constructor
        :param kwargs:  kwargs for models.ForeignKey class constructor
        :required kwargs key : class_name
        :custom default kwargs: "blank" : "blank", True
        :custom default kwargs: "db_index" : "db_index", True
        :custom default kwargs: "help_text" : "help_text", _(f"Product of this {kwargs['class_name']} record")
        :custom default kwargs: "null" : "null", True
        :custom default kwargs: "on_delete" : "on_delete", models.SET_NULL
        :custom default kwargs: "related_name" : "related_name", f"{kwargs['class_name'].lower()}_brand"
        :custom default kwargs: "to" : "to", "Products.Brand"
        :custom default kwargs: "verbose_name" : "verbose_name", _(kwargs['class_name'] + "`s Brand")
        """
        # "kw_class_name" : "ProductBrand/Gallery"
        # "kw_field_name" : "Brand"
        # "kw_app_name" : "Products"
        # "kw_class_model" : "Brand"
        # "kw_related_name" : "brand"
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"].capitalize()
        kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()
        kwargs["app_name"] , kwargs["class_model"] , kwargs["related_name_def"] = __class__.class_app_name , __class__.class_model , __class__.class_related_name
        super().__init__(*args , **kwargs)

class CustomCategoryFieldManyToMany(CustomDefaultField.ManyToManyField) :
    """
    Custom Category Field as ManyToMany

    """
    class_app_name = "Products"
    class_model = "Category"
    class_field_name = "Category"
    class_related_name = "category"
    class_through_fields = (None , "category")
    class_costum_default_attrs = {

        }
    class_validator = None

    def __init__(self , *args , **kwargs) :
        """
        Custom Category Field
        :param args:  args for models.ManyToManyField class constructor
        :param kwargs:  kwargs for models.ManyToManyField class constructor
        :required kwargs key : class_name
        :custom default kwargs: "blank" : "blank", True
        :custom default kwargs: "db_index" : "db_index", True
        :custom default kwargs: "help_text" : "help_text", _(f"Categories of this {kwargs['class_name']} record")
        :custom default kwargs: "related_name" : "related_name", f"{kwargs['class_name'].lower()}_categories"
        :custom default kwargs: "through" : "through", f"{kwargs['class_name']}Category"
        :custom default kwargs: "through_fields" : "through_fields", (f"{kwargs['class_name'].lower()}_id", "category_id")
        :custom default kwargs: "to" : "to", "Products.Category"
        :custom default kwargs: "verbose_name" : "verbose_name", _(kwargs['class_name'] + "`s Category")
        """
        # "kw_class_name" : ["Product","User"],
        # "kw_field_name" : "Category",
        # "kw_app_name" : "Products",
        # "kw_class_model" : "Category",
        # "kw_related_name" : "category",
        # "kw_through_fields" : ("?", "category")

        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"].capitalize()
        kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()
        kwargs["app_name"] , kwargs["class_model"] , kwargs["related_name_def"] , kwargs["through_fields_def"] = __class__.class_app_name , __class__.class_model , __class__.class_related_name , __class__.class_through_fields

        super().__init__(*args , **kwargs)

class CustomTagFieldManyToMany(CustomDefaultField.ManyToManyField) :
    """
    Custom Tag Field as ManyToMany

    """

    class_app_name = "Products"
    class_model = "Tag"
    class_field_name = "Tag"
    class_related_name = "tag"
    class_through_fields = (None , "tag")
    class_costum_default_attrs = {

        }
    class_validator = None

    def __init__(self , *args , **kwargs) :
        """
        Custom Tag Field
        :param args:  args for models.ManyToManyField class constructor
        :param kwargs:  kwargs for models.ManyToManyField class constructor
        :required kwargs key : class_name
        :custom default kwargs: "blank" : "blank", True
        :custom default kwargs: "db_index" : "db_index", True
        :custom default kwargs: "help_text" : "help_text", _(f"Tags of this {kwargs['class_name']} record")
        :custom default kwargs: "related_name" : "related_name", f"{kwargs['class_name'].lower()}_tags"
        :custom default kwargs: "through" : "through", f"{kwargs['class_name']}Tag"
        :custom default kwargs: "through_fields" : "through_fields", (f"{kwargs['class_name'].lower()}_id", "tag_id")
        :custom default kwargs: "to" : "to", "Products.Tag"
        :custom default kwargs: "verbose_name" : "verbose_name", _(kwargs['class_name'] + "`s Tag")
        """
        # "kw_class_name" : ["Product","User"],
        # "kw_field_name" : "Tag",
        # "kw_app_name" : "Products",
        # "kw_class_model" : "Tag",
        # "kw_related_name" : "tag",
        # "kw_through_fields" : ("?", "tag")

        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"].capitalize()
        kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()
        kwargs["app_name"] , kwargs["class_model"] , kwargs["related_name_def"] , kwargs["through_fields_def"] = __class__.class_app_name , __class__.class_model , __class__.class_related_name , __class__.class_through_fields

        super().__init__(*args , **kwargs)

class CustomBrandFieldManyToMany(CustomDefaultField.ManyToManyField) :
    """
    Custom Brand Field as ManyToMany

    """

    class_app_name = "Products"
    class_model = "Brand"
    class_field_name = "Brand"
    class_related_name = "brand"
    class_through_fields = (None , "brand")
    class_costum_default_attrs = {

        }
    class_validator = None

    def __init__(self , *args , **kwargs) :
        """
        Custom Brand Field
        :param args:  args for models.ManyToManyField class constructor
        :param kwargs:  kwargs for models.ManyToManyField class constructor
        :required kwargs key : class_name
        :custom default kwargs: "blank" : "blank", True
        :custom default kwargs: "db_index" : "db_index", True
        :custom default kwargs: "help_text" : "help_text", _(f"Brands of this {kwargs['class_name']} record")
        :custom default kwargs: "related_name" : "related_name", f"{kwargs['class_name'].lower()}_brands"
        :custom default kwargs: "through" : "through", f"{kwargs['class_name']}Brand"
        :custom default kwargs: "through_fields" : "through_fields", (f"{kwargs['class_name'].lower()}_id", "brand_id")
        :custom default kwargs: "to" : "to", "Products.Brand"
        :custom default kwargs: "verbose_name" : "verbose_name", _(kwargs['class_name'] + "`s Brand")
        """
        # "kw_class_name" : ["Product","User"],
        # "kw_field_name" : "Brand",
        # "kw_app_name" : "Products",
        # "kw_class_model" : "Brand",
        # "kw_related_name" : "brand",
        # "kw_through_fields" : ("?", "brand")

        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"].capitalize()
        kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()
        kwargs["app_name"] , kwargs["class_model"] , kwargs["related_name_def"] , kwargs["through_fields_def"] = __class__.class_app_name , __class__.class_model , __class__.class_related_name , __class__.class_through_fields

        super().__init__(*args , **kwargs)

class CustomProductFieldManyToMany(CustomDefaultField.ManyToManyField) :
    """
    Custom Product Field as ManyToManyField

    """
    class_app_name = "Products"
    class_model = "Product"

    class_field_name = "Product"
    class_related_name = "product"
    class_through_fields = ("product" , None)
    class_costum_default_attrs = {

        }
    class_validator = None

    def __init__(self , *args , **kwargs) :
        """
        Custom Product Field
        :param args:  args for models.ManyToManyField class constructor
        :param kwargs:  kwargs for models.ManyToManyField class constructor
        :custom default kwargs: "blank" : "blank", True
        :custom default kwargs: "db_index" : "db_index", True
        :custom default kwargs: "help_text" : "help_text", _(f"Products of this {kwargs['class_name']} record")
        :custom default kwargs: "related_name" : "related_name", f"product_{kwargs['class_name'].lower()}s"
        :custom default kwargs: "through" : "through", f"Product{kwargs['class_name']}"
        :custom default kwargs: "through_fields" : "through_fields", (f"{kwargs['class_name'].lower()}_id", "product_id")
        :custom default kwargs: "to" : "to", "Products.Product"
        :custom default kwargs: "verbose_name" : "verbose_name", _(kwargs['class_name'] + "`s Products")
        """
        # "kw_class_name" : ["Brand","Category","Tag","User"],
        # "kw_field_name" : "Product",
        # "kw_app_name" : "Products",
        # "kw_class_model" : "Product",
        # "kw_related_name" : "product",
        # "kw_through_fields" : ("?", "category")

        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"].capitalize()
        kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()
        kwargs["app_name"] , kwargs["class_model"] , kwargs["related_name_def"] , kwargs["through_fields_def"] = __class__.class_app_name , __class__.class_model , __class__.class_related_name , __class__.class_through_fields

        super().__init__(*args , **kwargs)

class CustomDescriptionField(CustomDefaultField.TextField) :
    """
    Custom Description Field as TextField

    """

    class_field_name = "description"
    class_costum_default_attrs = {
        'blank' : False , 'null' : False ,
        }
    class_validator = CustomValidators.DescriptionValidator

    def __init__(self , *args , **kwargs) :
        """
        Custom Description Field
        :param args:  args for models.TextField class constructor
        :param kwargs:  kwargs for models.TextField class constructor
        :required kwargs key : class_name
        :custom default kwargs: "blank" : "blank", False
        :custom default kwargs: "help_text" : "help_text", _(f"Description of this {kwargs['class_name']} record")
        :custom default kwargs: "null" : "null", False
        :custom default kwargs: "verbose_name" : "verbose_name", _(kwargs['class_name'] + "`s Description")
        :custom default kwargs: 'max_length' : 'max_length', 1000
        :custom default kwargs: 'validators' : 'validators', CustomValidators.DescriptionValidator

        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"].capitalize()
        kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()

        kwargs['validators'] = kwargs.get('validators' , __class__.class_validator)

        super().__init__(*args , **kwargs)

class CustomBodyField(CustomDefaultField.TextField) :
    """
    Custom Body Field as TextField

    """

    class_field_name = ""
    class_costum_default_attrs = {
        'max_length' : 250 , 'blank' : False , 'null' : False ,
        }
    class_validator = CustomValidators.BodyValidator

    def __init__(self , *args , **kwargs) :
        """
        Custom Body Field
        :param args:  args for models.TextField class constructor
        :param kwargs:  kwargs for models.TextField class constructor
        :required kwargs key : class_name
        :custom default kwargs: "blank" : "blank", False
        :custom default kwargs: "help_text" : "help_text", _(f"Body of this {kwargs['class_name']} record")
        :custom default kwargs: "null" : "null", False
        :custom default kwargs: "verbose_name" : "verbose_name", _(kwargs['class_name'] + "`s Body")
        :custom default kwargs: 'max_length' : 'max_length', 250
        :custom default kwargs: 'validators' : 'validators', CustomValidators.BodyValidator

        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"].capitalize()
        kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()
        kwargs["null"] = kwargs.get("null" , __class__.class_costum_default_attrs["null"])
        kwargs["blank"] = kwargs.get("blank" , __class__.class_costum_default_attrs["blank"])
        kwargs['max_length'] = kwargs.get('max_length' , __class__.class_costum_default_attrs['max_length'])
        kwargs['validators'] = kwargs.get('validators' , __class__.class_validator)

        super().__init__(*args , **kwargs)

class CustomIsAvailableField(CustomDefaultField.BooleanField) :
    """
    Custom Is Available Field as BooleanField

    """

    class_field_name = "is available"
    class_costum_default_attrs = {
        'default' : True ,
        }
    class_validator = None

    def __init__(self , *args , **kwargs) :
        """
        Custom Is Available Field
        :param args:  args for models.BooleanField class constructor
        :param kwargs:  kwargs for models.BooleanField class constructor
        :required kwargs key : class_name
        :custom default kwargs: "blank" : "blank", False
        :custom default kwargs: "db_index" : "db_index", True
        :custom default kwargs: "default" : "default", True
        :custom default kwargs: "help_text" : "help_text", _(f"Is this {kwargs['class_name']} record available ?")
        :custom default kwargs: "null" : "null", False
        :custom default kwargs: "verbose_name" : "verbose_name", _(kwargs['class_name'] + "`s availability")
        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"].capitalize()
        kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()

        kwargs["default"] = kwargs.get("default" , __class__.class_costum_default_attrs["default"])

        kwargs["help_text"] = kwargs.get("help_text" , _(f"Is this {kwargs['class_name']} record available ?"))
        kwargs["verbose_name"] = kwargs.get("verbose_name" , _(kwargs['class_name'] + "`s availability"))

        super().__init__(*args , **kwargs)

class CustomIsActiveField(CustomDefaultField.BooleanField) :
    """
    Custom Is Active Field as BooleanField

    """

    class_field_name = "is active"
    class_costum_default_attrs = {
        'default' : True ,

        }
    class_validator = None

    def __init__(self , *args , **kwargs) :
        """
        Custom Is Active Field
        :param args:  args for models.BooleanField class constructor
        :param kwargs:  kwargs for models.BooleanField class constructor
        :required kwargs key : class_name
        :custom default kwargs: "blank" : "blank", False
        :custom default kwargs: "db_index" : "db_index", True
        :custom default kwargs: "default" : "default", True
        :custom default kwargs: "help_text" : "help_text", _(f"Is this {kwargs['class_name']} record active ?")
        :custom default kwargs: "null" : "null", False
        :custom default kwargs: "verbose_name" : "verbose_name", _(kwargs['class_name'] + "`s active status")

        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"].capitalize()
        kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()

        kwargs["default"] = kwargs.get("default" , __class__.class_costum_default_attrs["default"])

        kwargs["help_text"] = kwargs.get("help_text" , _(f"Is this {kwargs['class_name']} record available ?"))
        kwargs["verbose_name"] = kwargs.get("verbose_name" , _(kwargs['class_name'] + "`s availability"))

        super().__init__(*args , **kwargs)

class CustomIsDeletedField(CustomDefaultField.BooleanField) :
    """
    Custom Is Deleted Field as BooleanField

    """

    class_field_name = ""
    class_costum_default_attrs = {

        }
    class_validator = None

    def __init__(self , *args , **kwargs) :
        """
        Custom Is Deleted Field
        :param args:  args for models.BooleanField class constructor
        :param kwargs:  kwargs for models.BooleanField class constructor
        :required kwargs key : class_name
        :custom default kwargs: "blank" : "blank", False
        :custom default kwargs: "db_index" : "db_index", True
        :custom default kwargs: "default" : "default", False
        :custom default kwargs: "help_text" : "help_text", _(f"Is this {kwargs['class_name']} record deleted ?")
        :custom default kwargs: "null" : "null", False
        :custom default kwargs: "verbose_name" : "verbose_name", _("Is Deleted")

        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"].capitalize()
        kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()
        kwargs["help_text"] = kwargs.get("help_text" , _(f"Is this {kwargs['class_name']} record deleted ?"))
        kwargs["verbose_name"] = kwargs.get("verbose_name" , _("Is Deleted"))

        super().__init__(*args , **kwargs)

class CustomIsCostumerField(CustomDefaultField.BooleanField) :
    """
    Custom Is Deleted Field as BooleanField
    """

    class_field_name = ""
    class_costum_default_attrs = {

        }
    class_validator = None

    def __init__(self , *args , **kwargs) :
        """
        Custom Is Deleted Field
        :param args:  args for models.BooleanField class constructor
        :param kwargs:  kwargs for models.BooleanField class constructor
        :required kwargs key : class_name
        :custom default kwargs: "blank" : "blank", False
        :custom default kwargs: "db_index" : "db_index", True
        :custom default kwargs: "default" : "default", False
        :custom default kwargs: "help_text" : "help_text", _(f"Is this {kwargs['class_name']} record deleted ?")
        :custom default kwargs: "null" : "null", False
        :custom default kwargs: "verbose_name" : "verbose_name", _("Is Deleted")

        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"].capitalize()
        kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()
        kwargs["help_text"] = kwargs.get("help_text" , _(f"Is this {kwargs['class_name']} record has costumer profile ?"))
        kwargs["verbose_name"] = kwargs.get("verbose_name" , _("Is Costumer"))
        super().__init__(*args , **kwargs)

class CustomIsMarketField(CustomDefaultField.BooleanField) :
    """
    Custom Is Market Field as BooleanField
    """

    class_field_name = "is market"
    class_costum_default_attrs = {

        }
    class_validator = None

    def __init__(self , *args , **kwargs) :
        """
        Custom Is Market Field
        :param args:  args for models.BooleanField class constructor
        :param kwargs:  kwargs for models.BooleanField class constructor
        :required kwargs key : class_name
        :custom default kwargs: "blank" : "blank", False
        :custom default kwargs: "db_index" : "db_index", True
        :custom default kwargs: "default" : "default", False
        :custom default kwargs: "help_text" : "help_text", _(f"Is this {kwargs['class_name']} record deleted ?")
        :custom default kwargs: "null" : "null", False
        :custom default kwargs: "verbose_name" : "verbose_name", _("Is Deleted")

        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"].capitalize()
        kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()
        kwargs["help_text"] = kwargs.get("help_text" , _(f"Is this {kwargs['class_name']} record has market profile ?"))
        kwargs["verbose_name"] = kwargs.get("verbose_name" , _("Is Market"))
        super().__init__(*args , **kwargs)

class CustomIsStaffField(CustomDefaultField.BooleanField) :
    """
    Custom Is Staff Field as BooleanField
    """

    class_field_name = "is staff"
    class_costum_default_attrs = {

        }
    class_validator = None

    def __init__(self , *args , **kwargs) :
        """
        Custom Is Staff Field
        :param args:  args for models.BooleanField class constructor
        :param kwargs:  kwargs for models.BooleanField class constructor
        :required kwargs key : class_name
        :custom default kwargs: "blank" : "blank", False
        :custom default kwargs: "db_index" : "db_index", True
        :custom default kwargs: "default" : "default", False
        :custom default kwargs: "help_text" : "help_text", _(f"Is this {kwargs['class_name']} record deleted ?")
        :custom default kwargs: "null" : "null", False
        :custom default kwargs: "verbose_name" : "verbose_name", _("Is Deleted")

        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"].capitalize()
        kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()
        kwargs["help_text"] = kwargs.get("help_text" , _(f"Is this {kwargs['class_name']} record has staff permissions ?"))
        kwargs["verbose_name"] = kwargs.get("verbose_name" , _("Is Staff"))
        super().__init__(*args , **kwargs)

class CustomIsAdminField(CustomDefaultField.BooleanField) :
    """
    Custom Is Admin Field as BooleanField
    """

    class_field_name = "is admin"
    class_costum_default_attrs = {

        }
    class_validator = None

    def __init__(self , *args , **kwargs) :
        """
        Custom Is Admin Field
        :param args:  args for models.BooleanField class constructor
        :param kwargs:  kwargs for models.BooleanField class constructor
        :required kwargs key : class_name
        :custom default kwargs: "blank" : "blank", False
        :custom default kwargs: "db_index" : "db_index", True
        :custom default kwargs: "default" : "default", False
        :custom default kwargs: "help_text" : "help_text", _(f"Is this {kwargs['class_name']} record deleted ?")
        :custom default kwargs: "null" : "null", False
        :custom default kwargs: "verbose_name" : "verbose_name", _("Is Deleted")

        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"].capitalize()
        kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()
        kwargs["help_text"] = kwargs.get("help_text" , _(f"Is this {kwargs['class_name']} record has admin permissions ?"))
        kwargs["verbose_name"] = kwargs.get("verbose_name" , _("Is Admin"))
        super().__init__(*args , **kwargs)

class CustomIsSuperUserField(CustomDefaultField.BooleanField) :
    """
    Custom Is Super User Field as BooleanField
    """

    class_field_name = "is super user"
    class_costum_default_attrs = {

        }
    class_validator = None

    def __init__(self , *args , **kwargs) :
        """
        Custom Is Super User Field
        :param args:  args for models.BooleanField class constructor
        :param
        kwargs:  kwargs for models.BooleanField class constructor
        :required
        kwargs key : class_name
        :custom
        default kwargs: "blank" : "blank", False
        :custom
        default kwargs: "db_index" : "db_index", True
        :custom
        default kwargs: "default" : "default", False
        :custom
        default kwargs: "help_text" : "help_text", _(f"Is this {kwargs['class_name']} record deleted ?")
        :custom
        default kwargs: "null" : "null", False
        :custom
        default kwargs: "verbose_name" : "verbose_name", _("Is Deleted")

        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"].capitalize()
        kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()
        kwargs["help_text"] = kwargs.get("help_text" , _(f"Is this {kwargs['class_name']} record has super user permissions ?"))
        kwargs["verbose_name"] = kwargs.get("verbose_name" , _("Is Super User"))
        super().__init__(*args , **kwargs)

class CustomIsVerifiedField(CustomDefaultField.BooleanField) :
    """
    Custom Is Verified Field as BooleanField
    """

    class_field_name = "is verified"
    class_costum_default_attrs = {

        }
    class_validator = None

    def __init__(self , *args , **kwargs) :
        """
        Custom Is Verified Field
        :param args:  args for models.BooleanField class constructor
        :param kwargs:  kwargs for models.BooleanField class constructor
        :required kwargs key : class_name
        :custom default kwargs: "blank" : "blank", False
        :custom default kwargs: "db_index" : "db_index", True
        :custom default kwargs: "default" : "default", False
        :custom default kwargs: "help_text" : "help_text", _(f"Is this {kwargs['class_name']} record deleted ?")
        :custom default kwargs: "null" : "null", False
        :custom default kwargs: "verbose_name" : "verbose_name", _("Is Deleted")

        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"].capitalize()
        kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()
        kwargs["help_text"] = kwargs.get("help_text" , _(f"Is this {kwargs['class_name']} record verified ?"))
        kwargs["verbose_name"] = kwargs.get("verbose_name" , _("Is Verified"))
        super().__init__(*args , **kwargs)

class CustomCreatedAtField(CustomDefaultField.DateTimeField) :
    """
    Custom Created At Field as DateTimeField
    """

    class_field_name = "created at"
    class_costum_default_attrs = {
        "auto_now_add" : True ,

        }
    class_validator = None

    def __init__(self , *args , **kwargs) :
        """
        Custom Created At Field
        :param args:   args for models.DateTimeField class constructor
        :param kwargs:  kwargs for models.DateTimeField class constructor
        :required kwargs key : class_name
        :custom default kwargs: "auto_now_add" : "auto_now_add", True
        :custom default kwargs: "blank" : "blank", False
        :custom default kwargs: "db_index" : "db_index", True
        :custom default kwargs: "help_text" : "help_text", _(f"When this {kwargs['class_name']} record was created")
        :custom default kwargs: "null" : "null", False
        :custom default kwargs: "verbose_name" : "verbose_name", _("Created At")

        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"].capitalize()
        kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()

        kwargs["auto_now_add"] = kwargs.get("auto_now_add" , __class__.class_costum_default_attrs["auto_now_add"])
        kwargs["help_text"] = kwargs.get("help_text" , _(f"When this {kwargs['class_name']} record was created"))
        kwargs["verbose_name"] = kwargs.get("verbose_name" , _("Created At"))
        super().__init__(*args , **kwargs)

class CustomModifiedAtField(CustomDefaultField.DateTimeField) :
    """
    Custom Modified At Field as DateTimeField

    """

    class_field_name = "modified at"
    class_costum_default_attrs = {
        'auto_now' : True ,
        }
    class_validator = None

    def __init__(self , *args , **kwargs) :
        """
        Custom Modified At Field
        :param args:  args for models.DateTimeField class constructor
        :param kwargs:  kwargs for models.DateTimeField class constructor
        :required kwargs key : class_name
        :custom default kwargs: "auto_now" : "auto_now", True
        :custom default kwargs: "blank" : "blank", False
        :custom default kwargs: "db_index" : "db_index", True
        :custom default kwargs: "help_text" : "help_text", _(f"When this {kwargs['class_name']} record was modified")
        :custom default kwargs: "null" : "null", False
        :custom default kwargs: "verbose_name" : "verbose_name", _("Modified At")

        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"].capitalize()
        kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()
        kwargs["auto_now"] = kwargs.get("auto_now" , __class__.class_costum_default_attrs["auto_now"])
        kwargs["help_text"] = kwargs.get("help_text" , _(f"When this {kwargs['class_name']} record was modified"))
        kwargs["verbose_name"] = kwargs.get("verbose_name" , _("Modified At"))
        super().__init__(*args , **kwargs)

class CustomIdField(CustomDefaultField.BigAutoField) :
    """
    Custom Id Field as BigAutoField

    """

    class_field_name = ""
    class_costum_default_attrs = {

        }
    class_validator = None

    def __init__(self , *args , **kwargs) :
        """
        Custom Id Field
        :param args:  args for models.BigAutoField class constructor
        :param kwargs:  kwargs for models.BigAutoField class constructor
        :custom default kwargs: "auto_created" : "auto_created", True
        :custom default kwargs: "blank" : "blank", False
        :custom default kwargs: "db_index" : "db_index", True
        :custom default kwargs: "editable" : "editable", False
        :custom default kwargs: "help_text" : "help_text", _(f"Id of this {kwargs['class_name']} record")
        :custom default kwargs: "null" : "null", False
        :custom default kwargs: "primary_key" : "primary_key", True
        :custom default kwargs: "verbose_name" : "verbose_name", _(kwargs['class_name'] + "`s Id")

        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"].capitalize()
        kwargs["field_name"] = __class__.class_field_name.capitalize() if "field_name" not in kwargs else kwargs["field_name"].capitalize()
        kwargs["auto_created"] = kwargs.get("auto_created" , True)
        kwargs["blank"] = kwargs.get("blank" , False)
        kwargs["db_index"] = kwargs.get("db_index" , True)
        kwargs["editable"] = kwargs.get("editable" , False)
        kwargs["help_text"] = kwargs.get("help_text" , _(f"Id of this {kwargs['class_name']} record"))
        kwargs["null"] = kwargs.get("null" , False)
        kwargs["primary_key"] = kwargs.get("primary_key" , True)
        kwargs["verbose_name"] = kwargs.get("verbose_name" , _(kwargs['class_name'] + "`s Id"))
        super().__init__(*args , **kwargs)

# Add your custom gallery field
# gallery = models.OneToOneField('Gallery', on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('Gallery'),help_text=_('Gallery of the product'))
