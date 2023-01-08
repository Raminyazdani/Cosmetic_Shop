from django.urls import reverse
from django.utils.text import slugify

from Users.managers import CostumBaseUserManager

class ModelMethod:
    class Meta:
        abstract=True
    """
    Methods Mixin
    """

    class Str:
        class Meta:
            abstract=True
        """
        Str Mixin
        """

        class Id:
            class Meta:
                abstract=True

            def __str__(self):
                """
                Return title field
                :return:  title field
                """
                return self.id

    class Save:
        class Meta:
            abstract=True
        """
        Save Mixin
        """

        class Slug:
            class Meta:
                abstract=True
            """
            Slug Mixin
            """

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


        class Base:
            class Meta:
                abstract=True
            """
            Base Mixin
            """

            class Super:
                class Meta:
                    abstract=True
                """
                Product Mixin
                """

                def save(self, *args, **kwargs):
                    """
                    Save product model Base
                    :param args:
                    :param kwargs:
                    :return:
                    """
                    super().save(*args, **kwargs)

    class AbsoluteUrl:
        class Meta:
            abstract=True
        """
        AbsoluteUrl Mixin
        """

        class Slug:
            class Meta:
                abstract=True
            """
            Slug Mixin
            """

            def get_absolute_url(self):
                """
                Return absolute url
                :return:
                """
                return reverse('product_detail', kwargs = {
                    'slug': self.slug
                    })

class ModelProperty:
    class Meta:
        abstract=True
    """
    Property Mixin
    """

    class Foreign:
        class Meta:
            abstract=True
        """
        Foreign Mixin
        """

        class Count:
            class Meta:
                abstract=True
            """
            Count Mixin
            """

            class ForABC:
                class Meta:
                    abstract=True
                """
                ForProduct Mixin
                """
                pass

            class ForOther:
                class Meta:
                    abstract=True
                """
                ForProduct Mixin
                """
                pass

        class Names:
            class Meta:
                abstract=True
            """
            Names Mixin
            """

            class ForABC:
                class Meta:
                    abstract=True
                """
                ForOther Mixin
                """

                pass

            class ForOther:
                class Meta:
                    abstract=True
                """
                ForProduct Mixin
                """

                pass

    class RequiredField():
        class Meta:
            abstract=True
        """
        RequiredField Mixin
        """

        ABC = []

    class SearchFields:
        class Meta:
            abstract=True
        """
        SearchFields Mixin
        """

        ABC = []

    class UserNameField:
        class Meta:
            abstract=True
        """
        UserNameField Mixin
        """

        ABC = ''

    class Manager:
        class Meta:
            abstract=True
        """
        MANAGERS Mixin
        """
        ABC_OBJECT = CostumBaseUserManager()
        ABC_SUBSET = CostumBaseUserManager()

class ModelRequiredProperties:
    class Meta:
        abstract=True
    """
    ModelRequiredProperties Mixin
    """

    class ABC(  # METHODS
            ...,  # save methods
            # def str and get_absolute_url
            ...,  # str and absolute url methods
            # PROPERTIES
            # MANAGERS
            ):
        """
        Users.User Model Mixin
        """
        pass

class AdminProperty():
    class Meta:
        abstract=True
    class ABC:
        class Meta:
            abstract=True
        list_display = []
        list_filter = []
        list_editable = []
        search_fields = []
        ordering = []
        filter_horizontal = []
        fieldsets = (("Profiling", {
            'fields': (),
            'classes': ('extrapretty')
            }), ("Conditions", {
            'fields': (),
            'classes': ('extrapretty')
            }), ("Extras", {
            'fields': (('product_inline',),),
            'classes': ('collapse', 'extrapretty',),
            }), ("Time", {
            'fields': (('created_at', 'modified_at'),),
            'classes': ('extrapretty')
            }))
        add_fieldsets = []
        readonly_fields = []
        list_per_page = 25
        list_max_show_all = 100
        prepopulated_fields = {
            "slug": ("phone_number",)
            }
        # prepopulated_fields = {
        #     "slug": (customize slug field)
        #     }
