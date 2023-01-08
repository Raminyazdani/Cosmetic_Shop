from django.urls import reverse
from django.utils.text import slugify
from django.utils.functional import cached_property
from Users.managers import CostumBaseUserManager

class ModelMethod :
    class Meta:
        abstract=True
    """
    Methods Mixin
    """

    class Str :
        class Meta:
            abstract=True
        """
        Str Mixin
        """

        class phone_number :
            class Meta:
                abstract=True
            """
            Str Mixin for title field
            """

            def __str__(self) :
                """
                Return title field
                :return:  title field
                """
                return self.phone_number

    class Save :
        class Meta:
            abstract=True
        """
        Save Mixin
        """

        class Slug :
            class Meta:
                abstract=True
            """
            Slug Mixin
            """

            class Name :
                class Meta:
                    abstract=True
                """
                Slug Mixin for name field
                """

                def save(self , *args , **kwargs) :
                    """
                    Save slug field with name field
                    :param args:
                    :param kwargs:
                    :return:
                    """
                    slug = slugify(self.name)
                    self.slug = slug
                    super().save(*args , **kwargs)

            class Id :
                class Meta:
                    abstract=True
                """
                Slug Mixin for id field
                """

                def save(self , *args , **kwargs) :
                    """
                    Save slug field with id field
                    :param args:
                    :param kwargs:
                    :return:
                    """
                    slug = slugify(self.id)
                    self.slug = slug
                    super().save(*args , **kwargs)

        class Base :
            class Meta:
                abstract=True
            """
            Base Mixin
            """

            class User :
                class Meta:
                    abstract=True
                """
                Product Mixin
                """

                def save(self , *args , **kwargs) :
                    """
                    Save product model Base
                    :param args:
                    :param kwargs:
                    :return:
                    """
                    super().save(*args , **kwargs)

    class AbsoluteUrl :
        class Meta:
            abstract=True
        """
        AbsoluteUrl Mixin
        """

        class Slug :
            class Meta:
                abstract=True
            """
            Slug Mixin
            """

            def get_absolute_url(self) :
                """
                Return absolute url
                :return:
                """
                return reverse('product_detail' , kwargs = {'slug' : self.slug})

class ModelProperty :
    class Meta:
        abstract=True
    """
    Property Mixin
    """

    class Foreign :
        class Meta:
            abstract=True
        """
        Foreign Mixin
        """

        class Count :
            class Meta:
                abstract=True
            """
            Count Mixin
            """

            class ForUser :
                class Meta:
                    abstract=True
                """
                ForProduct Mixin
                """
                pass

            class ForOther :
                class Meta:
                    abstract=True
                """
                ForProduct Mixin
                """
                pass

        class Names :
            class Meta:
                abstract=True
            """
            Names Mixin
            """

            class ForOther :
                class Meta:
                    abstract=True
                """
                ForOther Mixin
                """

                pass

            class ForUser :
                class Meta:
                    abstract=True
                """
                ForProduct Mixin
                """

                pass

    class RequiredField() :
        class Meta:
            abstract=True
        """
        RequiredField Mixin
        """


        USER = ["password"]

    class SearchFields :
        class Meta:
            abstract=True
        """
        SearchFields Mixin
        """

        USER = ["phone_number" ,"id"]

    class UserNameField :
        class Meta:
            abstract=True
        """
        UserNameField Mixin
        """

        USER = 'phone_number'

    class Manager :
        class Meta:
            abstract=True
        """
        MANAGERS Mixin
        """
        USER_OBJECT = CostumBaseUserManager()
        USER_SUBSET = CostumBaseUserManager()

class ModelRequiredProperties :
    class Meta:
        abstract=True
    """
    ModelRequiredProperties Mixin
    """



    class User(
            # METHODS
            ModelMethod.Save.Slug.Name , ModelMethod.Save.Base.User ,  # save methods

            # def str and get_absolute_url
            ModelMethod.Str.phone_number , ModelMethod.AbsoluteUrl.Slug ,  # str and absolute url methods

            # PROPERTIES

            # MANAGERS

            ) :
        """
        Users.User Model Mixin
        """
        pass

class AdminProperty():
    class Meta:
        abstract=True
    class User:
        class Meta:
            abstract=True
        list_display = ['id', 'phone_number', 'is_costumer', 'is_market', 'is_staff', 'is_active', 'is_admin', 'is_superuser', 'is_verified', 'slug', 'is_delete', 'created_at', 'modified_at']
        list_filter = ['is_costumer', 'is_market', 'is_staff', 'is_active', 'is_admin', 'is_superuser', 'is_verified', 'is_delete', 'created_at']
        list_editable = ['is_costumer', 'is_market', 'is_staff', 'is_active', 'is_admin', 'is_superuser', 'is_verified', 'is_delete']

        search_fields = ['phone_number']
        ordering = ['phone_number']
        filter_horizontal = []
        fieldsets = (("Profiling", {
            'fields': (('phone_number', 'slug'), ('is_costumer', 'is_market')),
            'classes': ('extrapretty')
            }), ("Conditions", {
            'fields': (('is_staff', 'is_active', 'is_admin', 'is_superuser', 'is_verified', 'is_delete'),),
            'classes': ('extrapretty')
            }), ("Time", {
            'fields': (('created_at', 'modified_at'),),
            'classes': ('extrapretty')
            }))
        add_fieldsets = []
        readonly_fields = ['created_at', 'modified_at']
        list_per_page = 25
        list_max_show_all = 100
        prepopulated_fields = {
            "slug": ("phone_number",)
            }