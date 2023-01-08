from django.urls import reverse
from django.utils.text import slugify
from django.utils.functional import cached_property
from Users.managers import CostumBaseUserManager

class ModelMethod :
    """
    Methods Mixin
    """

    class Str :
        """
        Str Mixin
        """

        class phone_number :
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
        """
        Save Mixin
        """

        class Slug :
            """
            Slug Mixin
            """

            class Name :
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
            """
            Base Mixin
            """

            class User :
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
        """
        AbsoluteUrl Mixin
        """

        class Slug :
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
    """
    Property Mixin
    """

    class Foreign :
        """
        Foreign Mixin
        """

        class Count :
            """
            Count Mixin
            """

            class ForUser :
                """
                ForProduct Mixin
                """
                pass

            class ForOther :
                """
                ForProduct Mixin
                """
                pass

        class Names :
            """
            Names Mixin
            """

            class ForOther :
                """
                ForOther Mixin
                """

                pass

            class ForUser :
                """
                ForProduct Mixin
                """

                pass

    class RequiredField() :
        """
        RequiredField Mixin
        """


        USER = ["password"]

    class SearchFields :
        """
        SearchFields Mixin
        """

        USER = ["phone_number" ,"id"]

    class UserNameField :
        """
        UserNameField Mixin
        """

        USER = 'phone_number'

    class Manager :
        """
        MANAGERS Mixin
        """
        USER_OBJECT = CostumBaseUserManager()
        USER_SUBSET = CostumBaseUserManager()

class ModelRequiredProperties :
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
    class User:
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