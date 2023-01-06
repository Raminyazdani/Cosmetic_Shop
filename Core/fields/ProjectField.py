from django.db import models
from django.utils.translation import gettext_lazy as _

# Core imports
from Core.utils.ProjectUtils import CustomValidators


class BaseMethodCustomField:
    """
    Base Method Custom Field
    """
    class DelClassName:
        """ 
         This class is used to delete the class_name argument from the kwargs
        """
        def __init__(self, *args, **kwargs):
            """
            This method is used to delete the class_name argument from the kwargs
            :param args: 
            :param kwargs: 
            """
            del kwargs["class_name"]
            super().__init__(*args, **kwargs)

    # class GetClassName:
    #     def __init__(self, *args, **kwargs):
    #         kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"]
    #         self.class_name = kwargs["class_name"].capitalize()
    # 

class CustomNameField(BaseMethodCustomField.DelClassName,models.CharField):
    """
    Custom Name Field as CharField
    """

    def __init__(self, *args, **kwargs):
        """
        Custom Name Field
        :required kwargs key : class_name
        :param args:  args for models.CharField class constructor
        :param kwargs:  kwargs for models.CharField class constructor
        :custom default kwargs: 'class_name' : class name of model that use this field
        :custom default kwargs: 'validators' : CustomValidators.NameValidator
        :custom default kwargs: 'max_length' : 30
        :custom default kwargs: 'verbose_name' : '{modelclassdbname} + "`s Name"
        :custom default kwargs: 'unique' : True
        :custom default kwargs: 'db_index' : True
        :custom default kwargs: 'help_text' : 'Name of this {modelclassdbname} record'
        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"]
        modelclassdbname = kwargs["class_name"].capitalize()
        kwargs['validators'] = kwargs.get('validators', CustomValidators.NameValidator)
        kwargs['max_length'] = kwargs.get('max_length', 30)
        kwargs["verbose_name"] = kwargs.get("verbose_name", _(modelclassdbname + "`s Name"))
        kwargs["unique"] = kwargs.get("unique", True)
        kwargs["db_index"] = kwargs.get("db_index", True)
        kwargs["help_text"] = kwargs.get("help_text", _(f"Name of this {modelclassdbname} record"))
        super().__init__(*args, **kwargs)


class CustomTitleField(BaseMethodCustomField.DelClassName,models.CharField):
    """
    Custom Title Field as CharField
    """

    def __init__(self, *args, **kwargs):
        """
        Custom Title Field
        :required kwargs key : class_name
        :param args:  args for models.CharField class constructor
        :param kwargs:  kwargs for models.CharField class constructor
        :custom default kwargs: 'class_name' : class name of model that use this field
        :custom default kwargs: 'validators' : CustomValidators.TitleValidator
        :custom default kwargs: 'max_length' : 20
        :custom default kwargs: 'verbose_name' : '{modelclassdbname} + "`s Title"
        :custom default kwargs: 'unique' : True
        :custom default kwargs: 'db_index' : True
        :custom default kwargs: 'help_text' : 'Title of this {modelclassdbname} record'
        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"]
        modelclassdbname = kwargs["class_name"].capitalize()
        kwargs['validators'] = kwargs.get('validators', CustomValidators.TitleValidator)
        kwargs['max_length'] = kwargs.get('max_length', 20)
        kwargs["verbose_name"] = kwargs.get("verbose_name", _(modelclassdbname + "`s Title"))
        kwargs["unique"] = kwargs.get("unique", True)
        kwargs["db_index"] = kwargs.get("db_index", True)
        kwargs["help_text"] = kwargs.get("help_text", _(f"Title of this {modelclassdbname} record"))

        super().__init__(*args, **kwargs)


class CustomGenderField(BaseMethodCustomField.DelClassName,models.PositiveIntegerField):
    """
    Custom Gender Field as PositiveIntegerField
    Choices are defined as class variables so that they can be easily accessed from instances.
    includes: UNISEX, MALE , FEMALE
    """
    UNISEX = 0
    MALE = 1
    FEMALE = 2
    GENDER_CHOICES = (
        (UNISEX, _('Gender free')),
        (MALE, _('For men')),
        (FEMALE, _('For women')),
    )
    GENDER = GENDER_CHOICES

    def __init__(self, *args, **kwargs):
        """
        Custom Gender Field
        :required kwargs key : class_name
        :param args:  args for models.PositiveIntegerField class constructor
        :param kwargs:  kwargs for models.PositiveIntegerField class constructor
        :custom default kwargs: 'class_name' : class name of model that use this field
        :custom default kwargs: 'choices' : CustomGenderField
        :custom default kwargs: 'default' : CustomGenderField.UNISEX
        :custom default kwargs: 'verbose_name' : '{modelclassdbname}' + "`s Gender"
        :custom default kwargs: 'help_text' : "Men/Women/Gender-free"
        :custom default kwargs: 'db_index' : True
        :custom default kwargs: 'null' : False
        :custom default kwargs: 'validators' : CustomValidators.GenderValidator
        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"]
        modelclassdbname = kwargs["class_name"].capitalize()
        kwargs["choices"] = kwargs.get("choices", self.__class__.GENDER_CHOICES)
        kwargs["verbose_name"] = kwargs.get("verbose_name", _(modelclassdbname + "`s Gender"))
        kwargs["default"] = kwargs.get("default", self.__class__.UNISEX)
        kwargs["help_text"] = kwargs.get("help_text", _("Men/Women/Gender-free"))
        kwargs["db_index"] = kwargs.get("db_index", True)
        kwargs["null"] = kwargs.get("null", False)
        kwargs['validators'] = kwargs.get('validators', CustomValidators.GenderValidator)

        super().__init__(*args, **kwargs)


class CustomSlugField(BaseMethodCustomField.DelClassName,models.SlugField):
    """
    Custom Slug Field as SlugField
    """

    def __init__(self, *args, **kwargs):
        """
        Custom Slug Field
        :required kwargs key : class_name
        :param args:  args for models.SlugField class constructor
        :param kwargs:  kwargs for models.SlugField class constructor
        :custom default kwargs: 'class_name' : class name of model that use this field
        :custom default kwargs: 'max_length' : 100
        :custom default kwargs: 'verbose_name' : '{modelclassdbname}' + "`s Slug"
        :custom default kwargs: 'unique' : True
        :custom default kwargs: 'db_index' : True
        :custom default kwargs: 'help_text' : 'Slug of this {modelclassdbname} record'
        :custom default kwargs: 'null' : True
        :custom default kwargs: 'blank' : True
        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"]
        modelclassdbname = kwargs["class_name"].capitalize()
        kwargs["max_length"] = kwargs.get("max_length", 100)
        kwargs["verbose_name"] = kwargs.get("verbose_name", _(modelclassdbname + "`s Slug"))
        kwargs["unique"] = kwargs.get("unique", True)
        kwargs["db_index"] = kwargs.get("db_index", True)
        kwargs["help_text"] = kwargs.get("help_text", _(f"Slug of this {modelclassdbname} record"))
        kwargs["null"] = kwargs.get("null", True)
        kwargs["blank"] = kwargs.get("blank", True)
        super().__init__(*args, **kwargs)


class CustomCommentFieldForeignKey(BaseMethodCustomField.DelClassName,models.ForeignKey):
    """
    Custom Comment Field as ForeignKey
    """

    def __init__(self, *args, **kwargs):
        """
        Custom Comment Field
        :required kwargs key : class_name
        :param args:  args for models.ForeignKey class constructor
        :param kwargs:  kwargs for models.ForeignKey class constructor
        :custom default kwargs: 'class_name' : class name of model that use this field
        :custom default kwargs: 'to' : 'Product.Comment'
        :custom default kwargs: '?' : ?
        :custom default kwargs: 'blank' : True
        :custom default kwargs: 'on_delete' : models.CASCADE
        :custom default kwargs: 'verbose_name' : '{modelclassdbname}' + "`s Comment"
        :custom default kwargs: 'null' : True
        :custom default kwargs: 'related_name' : '{modelclassdbname}' + "_comment"
        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"]
        modelclassdbname = kwargs["class_name"].capitalize()
        kwargs["to"] = kwargs.get("to", "Products.Comment")
        kwargs["verbose_name"] = kwargs.get("verbose_name", _(modelclassdbname + "`s Comments"))
        kwargs["help_text"] = kwargs.get("help_text", _(f"Comment of this {modelclassdbname} record"))
        kwargs["on_delete"] = kwargs.get("on_delete", models.SET_NULL)
        kwargs["null"] = kwargs.get("null", True)
        kwargs["blank"] = kwargs.get("blank", True)
        kwargs["db_index"] = kwargs.get("db_index", True)
        kwargs["related_name"] = kwargs.get("related_name", f"{modelclassdbname.lower()}_comments")

        super().__init__(*args, **kwargs)


class CustomCategoryParentFieldForeignKey(BaseMethodCustomField.DelClassName,models.ForeignKey):
    """
    Custom Category Parent Field as ForeignKey

    """

    def __init__(self, *args, **kwargs):
        """
        Custom Category Parent Field
        :required kwargs key : class_name
        :param args:  args for models.ForeignKey class constructor
        :param kwargs:  kwargs for models.ForeignKey class constructor
        :custom default kwargs: "to" : "to", "Products.Category"
        :custom default kwargs: "verbose_name" : "verbose_name", _(modelclassdbname + "`s Parent")
        :custom default kwargs: "help_text" : "help_text", _(f"Parent of this {modelclassdbname} record")
        :custom default kwargs: "on_delete" : "on_delete", models.SET_NULL
        :custom default kwargs: "null" : "null", True
        :custom default kwargs: "blank" : "blank", True
        :custom default kwargs: "db_index" : "db_index", True
        :custom default kwargs: "related_name" : "related_name", f"{modelclassdbname.lower()}_parent"

        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"]
        modelclassdbname = kwargs["class_name"].capitalize()
        kwargs["to"] = kwargs.get("to", "Products.Category")
        kwargs["verbose_name"] = kwargs.get("verbose_name", _(modelclassdbname + "`s Parent"))
        kwargs["help_text"] = kwargs.get("help_text", _(f"Parent of this {modelclassdbname} record"))
        kwargs["on_delete"] = kwargs.get("on_delete", models.SET_NULL)
        kwargs["null"] = kwargs.get("null", True)
        kwargs["blank"] = kwargs.get("blank", True)
        kwargs["db_index"] = kwargs.get("db_index", True)
        kwargs["related_name"] = kwargs.get("related_name", f"{modelclassdbname.lower()}_parent")

        super().__init__(*args, **kwargs)


class CustomUserFieldForeignKey(BaseMethodCustomField.DelClassName,models.ForeignKey):
    """
    Custom User Field as ForeginKey

    """

    def __init__(self, *args, **kwargs):
        """
        Custom User Field
        :param args:  args for models.ForeignKey class constructor
        :param kwargs:  kwargs for models.ForeignKey class constructor
        :required kwargs key : class_name
        :custom default kwargs: "to" : "to", "Users.User"
        :custom default kwargs: "verbose_name" : "verbose_name", _(modelclassdbname + "`s User")
        :custom default kwargs: "help_text" : "help_text", _(f"User of this {modelclassdbname} record")
        :custom default kwargs: "on_delete" : "on_delete", models.SET_NULL
        :custom default kwargs: "null" : "null", True
        :custom default kwargs: "blank" : "blank", True
        :custom default kwargs: "db_index" : "db_index", True
        :custom default kwargs: "related_name" : "related_name", f"{modelclassdbname.lower()}_user"
        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"]
        modelclassdbname = kwargs["class_name"].capitalize()
        kwargs["to"] = kwargs.get("to", "Users.User")
        kwargs["verbose_name"] = kwargs.get("verbose_name", _(modelclassdbname + "`s User"))
        kwargs["help_text"] = kwargs.get("help_text", _(f"User of this {modelclassdbname} record"))
        kwargs["on_delete"] = kwargs.get("on_delete", models.SET_NULL)
        kwargs["null"] = kwargs.get("null", True)
        kwargs["blank"] = kwargs.get("blank", True)
        kwargs["db_index"] = kwargs.get("db_index", True)
        kwargs["related_name"] = kwargs.get("related_name", f"{modelclassdbname.lower()}_user")

        super().__init__(*args, **kwargs)


class CustomProductFieldForeignKey(BaseMethodCustomField.DelClassName,models.ForeignKey):
    """
    Custom Product Field as ForeignKey

    """

    def __init__(self, *args, **kwargs):
        """
        Custom Product Field
        :param args:  args for models.ForeignKey class constructor
        :param kwargs:  kwargs for models.ForeignKey class constructor
        :required kwargs key : class_name
        :custom default kwargs: "to" : "to", "Products.Product"
        :custom default kwargs: "verbose_name" : "verbose_name", _(modelclassdbname + "`s Product")
        :custom default kwargs: "help_text" : "help_text", _(f"Product of this {modelclassdbname} record")
        :custom default kwargs: "on_delete" : "on_delete", models.SET_NULL
        :custom default kwargs: "null" : "null", True
        :custom default kwargs: "blank" : "blank", True
        :custom default kwargs: "db_index" : "db_index", True
        :custom default kwargs: "related_name" : "related_name", f"{modelclassdbname.lower()}_product"
        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"]
        modelclassdbname = kwargs["class_name"].capitalize()
        kwargs["to"] = kwargs.get("to", "Products.Product")
        kwargs["verbose_name"] = kwargs.get("verbose_name", _(modelclassdbname + "`s Product"))
        kwargs["help_text"] = kwargs.get("help_text", _(f"Product of this {modelclassdbname} record"))
        kwargs["on_delete"] = kwargs.get("on_delete", models.SET_NULL)
        kwargs["null"] = kwargs.get("null", True)
        kwargs["blank"] = kwargs.get("blank", True)
        kwargs["db_index"] = kwargs.get("db_index", True)
        kwargs["related_name"] = kwargs.get("related_name", f"{modelclassdbname.lower()}_product")

        super().__init__(*args, **kwargs)

class CustomCategoryFieldForeignKey(BaseMethodCustomField.DelClassName,models.ForeignKey):
    """
    Custom Category Field as ForeignKey

    """

    def __init__(self, *args, **kwargs):
        """
        Custom Category Field
        :param args:  args for models.ForeignKey class constructor
        :param kwargs:  kwargs for models.ForeignKey class constructor
        :required kwargs key : class_name
        :custom default kwargs: "to" : "to", "Products.Category"
        :custom default kwargs: "verbose_name" : "verbose_name", _(modelclassdbname + "`s Category")
        :custom default kwargs: "help_text" : "help_text", _(f"Category of this {modelclassdbname} record")
        :custom default kwargs: "on_delete" : "on_delete", models.SET_NULL
        :custom default kwargs: "null" : "null", True
        :custom default kwargs: "blank" : "blank", True
        :custom default kwargs: "db_index" : "db_index", True
        :custom default kwargs: "related_name" : "related_name", f"{modelclassdbname.lower()}_category"
        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"]
        modelclassdbname = kwargs["class_name"].capitalize()
        kwargs["to"] = kwargs.get("to", "Products.Category")
        kwargs["verbose_name"] = kwargs.get("verbose_name", _(modelclassdbname + "`s Category"))
        kwargs["help_text"] = kwargs.get("help_text", _(f"Category of this {modelclassdbname} record"))
        kwargs["on_delete"] = kwargs.get("on_delete", models.SET_NULL)
        kwargs["null"] = kwargs.get("null", True)
        kwargs["blank"] = kwargs.get("blank", True)
        kwargs["db_index"] = kwargs.get("db_index", True)
        kwargs["related_name"] = kwargs.get("related_name", f"{modelclassdbname.lower()}_category")

        super().__init__(*args, **kwargs)

class CustomTagFieldForeignKey(BaseMethodCustomField.DelClassName,models.ForeignKey):
    """
    Custom Tag Field as ForeignKey

    """

    def __init__(self, *args, **kwargs):
        """
        Custom Tag Field
        :param args:  args for models.ForeignKey class constructor
        :param kwargs:  kwargs for models.ForeignKey class constructor
        :required kwargs key : class_name
        :custom default kwargs: "to" : "to", "Products.Tag"
        :custom default kwargs: "verbose_name" : "verbose_name", _(modelclassdbname + "`s Tag")
        :custom default kwargs: "help_text" : "help_text", _(f"Tag of this {modelclassdbname} record")
        :custom default kwargs: "on_delete" : "on_delete", models.SET_NULL
        :custom default kwargs: "null" : "null", True
        :custom default kwargs: "blank" : "blank", True
        :custom default kwargs: "db_index" : "db_index", True
        :custom default kwargs: "related_name" : "related_name", f"{modelclassdbname.lower()}_tag"
        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"]
        modelclassdbname = kwargs["class_name"].capitalize()
        kwargs["to"] = kwargs.get("to", "Products.Tag")
        kwargs["verbose_name"] = kwargs.get("verbose_name", _(modelclassdbname + "`s Tag"))
        kwargs["help_text"] = kwargs.get("help_text", _(f"Tag of this {modelclassdbname} record"))
        kwargs["on_delete"] = kwargs.get("on_delete", models.SET_NULL)
        kwargs["null"] = kwargs.get("null", True)
        kwargs["blank"] = kwargs.get("blank", True)
        kwargs["db_index"] = kwargs.get("db_index", True)
        kwargs["related_name"] = kwargs.get("related_name", f"{modelclassdbname.lower()}_tag")

        super().__init__(*args, **kwargs)

class CustomBrandFieldForeignKey(BaseMethodCustomField.DelClassName,models.ForeignKey):
    """
    Custom Brand Field as ForeignKey

    """

    def __init__(self, *args, **kwargs):
        """
        Custom Brand Field
        :param args:  args for models.ForeignKey class constructor
        :param kwargs:  kwargs for models.ForeignKey class constructor
        :required kwargs key : class_name
        :custom default kwargs: "to" : "to", "Products.Brand"
        :custom default kwargs: "verbose_name" : "verbose_name", _(modelclassdbname + "`s Brand")
        :custom default kwargs: "help_text" : "help_text", _(f"Product of this {modelclassdbname} record")
        :custom default kwargs: "on_delete" : "on_delete", models.SET_NULL
        :custom default kwargs: "null" : "null", True
        :custom default kwargs: "blank" : "blank", True
        :custom default kwargs: "db_index" : "db_index", True
        :custom default kwargs: "related_name" : "related_name", f"{modelclassdbname.lower()}_brand"
        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"]
        modelclassdbname = kwargs["class_name"].capitalize()
        kwargs["to"] = kwargs.get("to", "Products.Brand")
        kwargs["verbose_name"] = kwargs.get("verbose_name", _(modelclassdbname + "`s Brand"))
        kwargs["help_text"] = kwargs.get("help_text", _(f"Product of this {modelclassdbname} record"))
        kwargs["on_delete"] = kwargs.get("on_delete", models.SET_NULL)
        kwargs["null"] = kwargs.get("null", True)
        kwargs["blank"] = kwargs.get("blank", True)
        kwargs["db_index"] = kwargs.get("db_index", True)
        kwargs["related_name"] = kwargs.get("related_name", f"{modelclassdbname.lower()}_brand")

        super().__init__(*args, **kwargs)


class CustomCategoryFieldManyToMany(BaseMethodCustomField.DelClassName,models.ManyToManyField):
    """
    Custom Category Field as ManyToMany

    """

    def __init__(self, *args, **kwargs):
        """
        Custom Category Field
        :param args:  args for models.ManyToManyField class constructor
        :param kwargs:  kwargs for models.ManyToManyField class constructor
        :required kwargs key : class_name
        :custom default kwargs: "to" : "to", "Products.Category"
        :custom default kwargs: "verbose_name" : "verbose_name", _(modelclassdbname + "`s Category")
        :custom default kwargs: "help_text" : "help_text", _(f"Categories of this {modelclassdbname} record")
        :custom default kwargs: "blank" : "blank", True
        :custom default kwargs: "db_index" : "db_index", True
        :custom default kwargs: "related_name" : "related_name", f"{modelclassdbname.lower()}_categories"
        :custom default kwargs: "through" : "through", f"{modelclassdbname}Category"
        :custom default kwargs: "through_fields" : "through_fields", (f"{modelclassdbname.lower()}_id", "category_id")
        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"]
        modelclassdbname = kwargs["class_name"].capitalize()
        kwargs["to"] = kwargs.get("to", "Products.Category")
        kwargs["verbose_name"] = kwargs.get("verbose_name", _(modelclassdbname + "`s Category"))
        kwargs["help_text"] = kwargs.get("help_text", _(f"Categories of this {modelclassdbname} record"))
        kwargs["blank"] = kwargs.get("blank", True)
        kwargs["db_index"] = kwargs.get("db_index", True)
        kwargs["related_name"] = kwargs.get("related_name", f"{modelclassdbname.lower()}_categories")
        kwargs["through"] = kwargs.get("through", f"{modelclassdbname}Category")
        kwargs["through_fields"] = kwargs.get("through_fields", (f"{modelclassdbname.lower()}_id", "category_id"))

        super().__init__(*args, **kwargs)


class CustomTagFieldManyToMany(BaseMethodCustomField.DelClassName,models.ManyToManyField):
    """
    Custom Tag Field as ManyToMany

    """

    def __init__(self, *args, **kwargs):
        """
        Custom Tag Field
        :param args:  args for models.ManyToManyField class constructor
        :param kwargs:  kwargs for models.ManyToManyField class constructor
        :required kwargs key : class_name
        :custom default kwargs: "to" : "to", "Products.Tag"
        :custom default kwargs: "verbose_name" : "verbose_name", _(modelclassdbname + "`s Tag")
        :custom default kwargs: "help_text" : "help_text", _(f"Tags of this {modelclassdbname} record")
        :custom default kwargs: "blank" : "blank", True
        :custom default kwargs: "db_index" : "db_index", True
        :custom default kwargs: "related_name" : "related_name", f"{modelclassdbname.lower()}_tags"
        :custom default kwargs: "through" : "through", f"{modelclassdbname}Tag"
        :custom default kwargs: "through_fields" : "through_fields", (f"{modelclassdbname.lower()}_id", "tag_id")
        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"]
        modelclassdbname = kwargs["class_name"].capitalize()
        kwargs["to"] = kwargs.get("to", "Products.Tag")
        kwargs["verbose_name"] = kwargs.get("verbose_name", _(modelclassdbname + "`s Tag"))
        kwargs["help_text"] = kwargs.get("help_text", _(f"Tags of this {modelclassdbname} record"))
        kwargs["blank"] = kwargs.get("blank", True)
        kwargs["db_index"] = kwargs.get("db_index", True)
        kwargs["related_name"] = kwargs.get("related_name", f"{modelclassdbname.lower()}_tags")
        kwargs["through"] = kwargs.get("through", f"{modelclassdbname}Tag")
        kwargs["through_fields"] = kwargs.get("through_fields", (f"{modelclassdbname.lower()}_id", "tag_id"))

        super().__init__(*args, **kwargs)


class CustomBrandFieldManyToMany(BaseMethodCustomField.DelClassName,models.ManyToManyField):
    """
    Custom Brand Field as ManyToMany

    """

    def __init__(self, *args, **kwargs):
        """
        Custom Brand Field
        :param args:  args for models.ManyToManyField class constructor
        :param kwargs:  kwargs for models.ManyToManyField class constructor
        :required kwargs key : class_name
        :custom default kwargs: "to" : "to", "Products.Brand"
        :custom default kwargs: "verbose_name" : "verbose_name", _(modelclassdbname + "`s Brand")
        :custom default kwargs: "help_text" : "help_text", _(f"Brands of this {modelclassdbname} record")
        :custom default kwargs: "blank" : "blank", True
        :custom default kwargs: "db_index" : "db_index", True
        :custom default kwargs: "related_name" : "related_name", f"{modelclassdbname.lower()}_brands"
        :custom default kwargs: "through" : "through", f"{modelclassdbname}Brand"
        :custom default kwargs: "through_fields" : "through_fields", (f"{modelclassdbname.lower()}_id", "brand_id")
        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"]
        modelclassdbname = kwargs["class_name"].capitalize()
        kwargs["to"] = kwargs.get("to", "Products.Brand")
        kwargs["verbose_name"] = kwargs.get("verbose_name", _(modelclassdbname + "`s Brand"))
        kwargs["help_text"] = kwargs.get("help_text", _(f"Brands of this {modelclassdbname} record"))
        kwargs["blank"] = kwargs.get("blank", True)
        kwargs["db_index"] = kwargs.get("db_index", True)
        kwargs["related_name"] = kwargs.get("related_name", f"{modelclassdbname.lower()}_brands")
        kwargs["through"] = kwargs.get("through", f"{modelclassdbname}Brand")
        kwargs["through_fields"] = kwargs.get("through_fields", (f"{modelclassdbname.lower()}_id", "brand_id"))

        super().__init__(*args, **kwargs)


class CustomShortDescriptionField(BaseMethodCustomField.DelClassName,models.CharField):
    """
    Custom Short Description Field as CharField

    """

    def __init__(self, *args, **kwargs):
        """
        Custom Short Description Field
        :param args:  args for models.CharField class constructor
        :param kwargs: kwargs for models.CharField class constructor
        :required kwargs key : class_name
        :custom default kwargs: "max_length" : "max_length", 100
        :custom default kwargs: "verbose_name" : "verbose_name", _(modelclassdbname + "`s Short Description")
        :custom default kwargs: "help_text" : "help_text", _(f"Short description of this {modelclassdbname} record")
        :custom default kwargs: "blank" : "blank", False
        :custom default kwargs: "null" : "null", False
        :custom default kwargs: 'validators' : 'validators', CustomValidators.ShortDescriptionValidator

        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"]
        modelclassdbname = kwargs["class_name"].capitalize()
        kwargs["max_length"] = kwargs.get("max_length", 100)
        kwargs["verbose_name"] = kwargs.get("verbose_name", _(modelclassdbname + "`s Short Description"))
        kwargs["help_text"] = kwargs.get("help_text", _(f"Short description of this {modelclassdbname} record"))
        kwargs["blank"] = kwargs.get("blank", False)
        kwargs["null"] = kwargs.get("null", False)
        kwargs['validators'] = kwargs.get('validators', CustomValidators.ShortDescriptionValidator)

        super().__init__(*args, **kwargs)


class CustomDescriptionField(BaseMethodCustomField.DelClassName,models.TextField):
    """
    Custom Description Field as TextField

    """

    def __init__(self, *args, **kwargs):
        """
        Custom Description Field
        :param args:  args for models.TextField class constructor
        :param kwargs:  kwargs for models.TextField class constructor
        :required kwargs key : class_name
        :custom default kwargs: 'max_length' : 'max_length', 1000
        :custom default kwargs: "verbose_name" : "verbose_name", _(modelclassdbname + "`s Description")
        :custom default kwargs: "help_text" : "help_text", _(f"Description of this {modelclassdbname} record")
        :custom default kwargs: "blank" : "blank", False
        :custom default kwargs: "null" : "null", False
        :custom default kwargs: 'validators' : 'validators', CustomValidators.DescriptionValidator

        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"]
        modelclassdbname = kwargs["class_name"].capitalize()
        kwargs['max_length'] = kwargs.get('max_length', 1000)
        kwargs["verbose_name"] = kwargs.get("verbose_name", _(modelclassdbname + "`s Description"))
        kwargs["help_text"] = kwargs.get("help_text", _(f"Description of this {modelclassdbname} record"))
        kwargs["blank"] = kwargs.get("blank", False)
        kwargs["null"] = kwargs.get("null", False)
        kwargs['validators'] = kwargs.get('validators', CustomValidators.DescriptionValidator)

        super().__init__(*args, **kwargs)


class CustomBodyField(BaseMethodCustomField.DelClassName,models.TextField):
    """
    Custom Body Field as TextField

    """

    def __init__(self, *args, **kwargs):
        """
        Custom Body Field
        :param args:  args for models.TextField class constructor
        :param kwargs:  kwargs for models.TextField class constructor
        :required kwargs key : class_name
        :custom default kwargs: 'max_length' : 'max_length', 250
        :custom default kwargs: "verbose_name" : "verbose_name", _(modelclassdbname + "`s Body")
        :custom default kwargs: "help_text" : "help_text", _(f"Body of this {modelclassdbname} record")
        :custom default kwargs: "blank" : "blank", False
        :custom default kwargs: "null" : "null", False
        :custom default kwargs: 'validators' : 'validators', CustomValidators.BodyValidator

        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"]
        modelclassdbname = kwargs["class_name"].capitalize()
        kwargs['max_length'] = kwargs.get('max_length', 250)
        kwargs["verbose_name"] = kwargs.get("verbose_name", _(modelclassdbname + "`s Body"))
        kwargs["help_text"] = kwargs.get("help_text", _(f"Body of this {modelclassdbname} record"))
        kwargs["blank"] = kwargs.get("blank", False)
        kwargs["null"] = kwargs.get("null", False)
        kwargs['validators'] = kwargs.get('validators', CustomValidators.BodyValidator)

        super().__init__(*args, **kwargs)


class CustomRatingField(BaseMethodCustomField.DelClassName,models.PositiveIntegerField):
    """
    Custom Rating Field as PositiveIntegerField

    """

    def __init__(self, *args, **kwargs):
        """
        Custom Rating Field
        :param args:  args for models.PositiveIntegerField class constructor
        :param kwargs:  kwargs for models.PositiveIntegerField class constructor
        :required kwargs key : class_name
        :custom default kwargs: "verbose_name" : "verbose_name", _(modelclassdbname + "`s Rating")
        :custom default kwargs: "help_text" : "help_text", _(f"Rating of this {modelclassdbname} record")
        :custom default kwargs: 'validators' : 'validators', CustomValidators.RatingValidator

        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"]
        modelclassdbname = kwargs["class_name"].capitalize()
        kwargs["verbose_name"] = kwargs.get("verbose_name", _(modelclassdbname + "`s Rating"))
        kwargs["help_text"] = kwargs.get("help_text", _(f"Rating of this {modelclassdbname} record"))
        kwargs['validators'] = kwargs.get('validators', CustomValidators.RatingValidator)

        super().__init__(*args, **kwargs)


class CustomPriceFieldDollar(BaseMethodCustomField.DelClassName,models.DecimalField):
    """
    Custom Price Field as DecimalField

    """

    def __init__(self, *args, **kwargs):
        """
        Custom Price Field
        :param args:  args for models.DecimalField class constructor
        :param kwargs:  kwargs for models.DecimalField class constructor
        :required kwargs key : class_name
        :custom default kwargs: "verbose_name" : "verbose_name", _(modelclassdbname + "`s Price")
        :custom default kwargs: "help_text" : "help_text", _(f"Dollar Price of this {modelclassdbname} record")
        :custom default kwargs: "blank" : "blank", False
        :custom default kwargs: "null" : "null", False
        :custom default kwargs: "max_digits" : "max_digits", 10
        :custom default kwargs: "decimal_places" : "decimal_places", 2
        :custom default kwargs: "default" : "default", 0.0
        :custom default kwargs: "db_index" : "db_index", True
        :custom default kwargs: 'validators' : 'validators', CustomValidators.PriceValidator
        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"]
        modelclassdbname = kwargs["class_name"].capitalize()
        kwargs["verbose_name"] = kwargs.get("verbose_name", _(modelclassdbname + "`s Price"))
        kwargs["help_text"] = kwargs.get("help_text", _(f"Dollar Price of this {modelclassdbname} record"))
        kwargs["blank"] = kwargs.get("blank", False)
        kwargs["null"] = kwargs.get("null", False)
        kwargs["max_digits"] = kwargs.get("max_digits", 10)
        kwargs["decimal_places"] = kwargs.get("decimal_places", 2)
        kwargs["default"] = kwargs.get("default", 0.0)
        kwargs["db_index"] = kwargs.get("db_index", True)
        kwargs['validators'] = kwargs.get('validators', CustomValidators.PriceValidator)
        super().__init__(*args, **kwargs)


class CustomIsAvailableField(BaseMethodCustomField.DelClassName,models.BooleanField):
    """
    Custom Is Available Field as BooleanField

    """

    def __init__(self, *args, **kwargs):
        """
        Custom Is Available Field
        :param args:  args for models.BooleanField class constructor
        :param kwargs:  kwargs for models.BooleanField class constructor
        :required kwargs key : class_name
        :custom default kwargs: "verbose_name" : "verbose_name", _(modelclassdbname + "`s availability")
        :custom default kwargs: "help_text" : "help_text", _(f"Is this {modelclassdbname} record available ?")
        :custom default kwargs: "blank" : "blank", False
        :custom default kwargs: "null" : "null", False
        :custom default kwargs: "default" : "default", True
        :custom default kwargs: "db_index" : "db_index", True
        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"]
        modelclassdbname = kwargs["class_name"].capitalize()
        kwargs["verbose_name"] = kwargs.get("verbose_name", _(modelclassdbname + "`s availability"))
        kwargs["help_text"] = kwargs.get("help_text", _(f"Is this {modelclassdbname} record available ?"))
        kwargs["blank"] = kwargs.get("blank", False)
        kwargs["null"] = kwargs.get("null", False)
        kwargs["default"] = kwargs.get("default", True)
        kwargs["db_index"] = kwargs.get("db_index", True)
        super().__init__(*args, **kwargs)


class CustomIsActiveField(BaseMethodCustomField.DelClassName,models.BooleanField):
    """
    Custom Is Active Field as BooleanField

    """

    def __init__(self, *args, **kwargs):
        """
        Custom Is Active Field
        :param args:  args for models.BooleanField class constructor
        :param kwargs:  kwargs for models.BooleanField class constructor
        :required kwargs key : class_name
        :custom default kwargs: "verbose_name" : "verbose_name", _(modelclassdbname + "`s active status")
        :custom default kwargs: "help_text" : "help_text", _(f"Is this {modelclassdbname} record active ?")
        :custom default kwargs: "blank" : "blank", False
        :custom default kwargs: "null" : "null", False
        :custom default kwargs: "default" : "default", True
        :custom default kwargs: "db_index" : "db_index", True

        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"]
        modelclassdbname = kwargs["class_name"].capitalize()
        kwargs["verbose_name"] = kwargs.get("verbose_name", _(modelclassdbname + "`s active status"))
        kwargs["help_text"] = kwargs.get("help_text", _(f"Is this {modelclassdbname} record active ?"))
        kwargs["blank"] = kwargs.get("blank", False)
        kwargs["null"] = kwargs.get("null", False)
        kwargs["default"] = kwargs.get("default", True)
        kwargs["db_index"] = kwargs.get("db_index", True)
        super().__init__(*args, **kwargs)


class CustomIsDeletedField(BaseMethodCustomField.DelClassName,models.BooleanField):
    """
    Custom Is Deleted Field as BooleanField

    """

    def __init__(self, *args, **kwargs):
        """
        Custom Is Deleted Field
        :param args:  args for models.BooleanField class constructor
        :param kwargs:  kwargs for models.BooleanField class constructor
        :required kwargs key : class_name
        :custom default kwargs: "verbose_name" : "verbose_name", _("Is Deleted")
        :custom default kwargs: "help_text" : "help_text", _(f"Is this {modelclassdbname} record deleted ?")
        :custom default kwargs: "blank" : "blank", False
        :custom default kwargs: "null" : "null", False
        :custom default kwargs: "default" : "default", False
        :custom default kwargs: "db_index" : "db_index", True

        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"]
        modelclassdbname = kwargs["class_name"].capitalize()
        kwargs["verbose_name"] = kwargs.get("verbose_name", _("Is Deleted"))
        kwargs["help_text"] = kwargs.get("help_text", _(f"Is this {modelclassdbname} record deleted ?"))
        kwargs["blank"] = kwargs.get("blank", False)
        kwargs["null"] = kwargs.get("null", False)
        kwargs["default"] = kwargs.get("default", False)
        kwargs["db_index"] = kwargs.get("db_index", True)
        super().__init__(*args, **kwargs)


class CustomCreatedAtField(BaseMethodCustomField.DelClassName,models.DateTimeField):
    """
    Custom Created At Field as DateTimeField

    """

    def __init__(self, *args, **kwargs):
        """
        Custom Created At Field
        :param args:   args for models.DateTimeField class constructor
        :param kwargs:  kwargs for models.DateTimeField class constructor
        :required kwargs key : class_name
        :custom default kwargs: "verbose_name" : "verbose_name", _("Created At")
        :custom default kwargs: "help_text" : "help_text", _(f"When this {modelclassdbname} record was created")
        :custom default kwargs: "blank" : "blank", False
        :custom default kwargs: "null" : "null", False
        :custom default kwargs: "auto_now_add" : "auto_now_add", True
        :custom default kwargs: "db_index" : "db_index", True

        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"]
        modelclassdbname = kwargs["class_name"].capitalize()
        kwargs["verbose_name"] = kwargs.get("verbose_name", _("Created At"))
        kwargs["help_text"] = kwargs.get("help_text", _(f"When this {modelclassdbname} record was created"))
        kwargs["blank"] = kwargs.get("blank", False)
        kwargs["null"] = kwargs.get("null", False)
        kwargs["auto_now_add"] = kwargs.get("auto_now_add", True)
        kwargs["db_index"] = kwargs.get("db_index", True)
        super().__init__(*args, **kwargs)


class CustomModifiedAtField(BaseMethodCustomField.DelClassName,models.DateTimeField):
    """
    Custom Modified At Field as DateTimeField

    """

    def __init__(self, *args, **kwargs):
        """
        Custom Modified At Field
        :param args:  args for models.DateTimeField class constructor
        :param kwargs:  kwargs for models.DateTimeField class constructor
        :required kwargs key : class_name
        :custom default kwargs: "verbose_name" : "verbose_name", _("Modified At")
        :custom default kwargs: "help_text" : "help_text", _(f"When this {modelclassdbname} record was modified")
        :custom default kwargs: "blank" : "blank", False
        :custom default kwargs: "null" : "null", False
        :custom default kwargs: "auto_now" : "auto_now", True
        :custom default kwargs: "db_index" : "db_index", True

        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"]
        modelclassdbname = kwargs["class_name"].capitalize()
        kwargs["verbose_name"] = kwargs.get("verbose_name", _("Modified At"))
        kwargs["help_text"] = kwargs.get("help_text", _(f"When this {modelclassdbname} record was modified"))
        kwargs["blank"] = kwargs.get("blank", False)
        kwargs["null"] = kwargs.get("null", False)
        kwargs["auto_now"] = kwargs.get("auto_now", True)
        kwargs["db_index"] = kwargs.get("db_index", True)
        super().__init__(*args, **kwargs)


class CustomProductFieldManyToMany(BaseMethodCustomField.DelClassName,models.ManyToManyField):
    """
    Custom Product Field as ManyToManyField

    """

    def __init__(self, *args, **kwargs):
        """
        Custom Product Field
        :param args:  args for models.ManyToManyField class constructor
        :param kwargs:  kwargs for models.ManyToManyField class constructor
        :custom default kwargs: "to" : "to", "Products.Product"
        :custom default kwargs: "verbose_name" : "verbose_name", _(modelclassdbname + "`s Products")
        :custom default kwargs: "help_text" : "help_text", _(f"Products of this {modelclassdbname} record")
        :custom default kwargs: "blank" : "blank", True
        :custom default kwargs: "db_index" : "db_index", True
        :custom default kwargs: "related_name" : "related_name", f"product_{modelclassdbname.lower()}s"
        :custom default kwargs: "through" : "through", f"Product{modelclassdbname}"
        :custom default kwargs: "through_fields" : "through_fields", (f"{modelclassdbname.lower()}_id", "product_id")
        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"]
        modelclassdbname = kwargs["class_name"].capitalize()
        kwargs["to"] = kwargs.get("to", "Products.Product")
        kwargs["verbose_name"] = kwargs.get("verbose_name", _(modelclassdbname + "`s Products"))
        kwargs["help_text"] = kwargs.get("help_text", _(f"Products of this {modelclassdbname} record"))
        kwargs["blank"] = kwargs.get("blank", True)
        kwargs["db_index"] = kwargs.get("db_index", True)
        kwargs["related_name"] = kwargs.get("related_name", f"product_{modelclassdbname.lower()}s")
        kwargs["through"] = kwargs.get("through", f"Product{modelclassdbname}")
        kwargs["through_fields"] = kwargs.get("through_fields", (f"{modelclassdbname.lower()}_id", "product_id"))
        super().__init__(*args, **kwargs)


class CustomIdField(BaseMethodCustomField.DelClassName,models.BigAutoField):
    """
    Custom Id Field as BigAutoField

    """

    def __init__(self, *args, **kwargs):
        """
        Custom Id Field
        :param args:  args for models.BigAutoField class constructor
        :param kwargs:  kwargs for models.BigAutoField class constructor
        :custom default kwargs: "verbose_name" : "verbose_name", _(modelclassdbname + "`s Id")
        :custom default kwargs: "help_text" : "help_text", _(f"Id of this {modelclassdbname} record")
        :custom default kwargs: "primary_key" : "primary_key", True
        :custom default kwargs: "blank" : "blank", False
        :custom default kwargs: "null" : "null", False
        :custom default kwargs: "auto_created" : "auto_created", True
        :custom default kwargs: "db_index" : "db_index", True
        :custom default kwargs: "editable" : "editable", False

        """
        kwargs["class_name"] = "Model" if "class_name" not in kwargs else kwargs["class_name"]
        modelclassdbname = kwargs["class_name"].capitalize()
        kwargs["verbose_name"] = kwargs.get("verbose_name", _(modelclassdbname + "`s Id"))
        kwargs["help_text"] = kwargs.get("help_text", _(f"Id of this {modelclassdbname} record"))
        kwargs["primary_key"] = kwargs.get("primary_key", True)
        kwargs["blank"] = kwargs.get("blank", False)
        kwargs["null"] = kwargs.get("null", False)
        kwargs["auto_created"] = kwargs.get("auto_created", True)
        kwargs["db_index"] = kwargs.get("db_index", True)
        kwargs["editable"] = kwargs.get("editable", False)
        super().__init__(*args, **kwargs)


# Add your custom gallery field
# gallery = models.OneToOneField('Gallery', on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('Gallery'),help_text=_('Gallery of the product'))
