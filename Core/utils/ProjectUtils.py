import re

from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator, MaxValueValidator, MinLengthValidator, MinValueValidator, RegexValidator
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class CustomRegex:
    phone_regex = r'^(\+98|\+980|0098|00980|0|)\d{10}$'
    name_regex = r'^.{3,30}$'
    title_regex = r'^.{3,20}$'
    email_regex = r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"

class CustomValidators:
    RatingValidator = [MinValueValidator(0, message = _('Rating must be at least 0')), MaxValueValidator(10, message = _('Rating must be at most 10'))]
    PhoneValidator = [RegexValidator(regex = CustomRegex.phone_regex, message = _('must be a phone number with 10 digits'))]
    NameValidator = [RegexValidator(regex = CustomRegex.name_regex, message = _('must be a valid name with 3 to 30 characters'))]
    GenderValidator = [MinValueValidator(0, message = _('Gender is integer ,must be at least 0')), MaxValueValidator(2, message = _('Gender is integer ,must be at most 2'))]
    ShortDescriptionValidator = [MinLengthValidator(3, message = _('Short description must be at least 3 characters')), MaxLengthValidator(100, message = _('Short description must be at most 100 characters'))]
    DescriptionValidator = [MinLengthValidator(10, message = _('Description must be at least 10 characters')), MaxLengthValidator(1000, message = _('Description must be at most 1000 characters'))]
    DollarPriceValidator = [MinValueValidator(0, message = _('Price must be at least 0')), MaxValueValidator(1000000000, message = _('Price must be at most 1000000000'))]
    TitleValidator = [RegexValidator(regex = CustomRegex.title_regex, message = _('Title must be a valid string with 3 to 20 characters'))]
    BodyValidator = [MinLengthValidator(10, message = _('Body must be at least 10 characters')), MaxLengthValidator(250, message = _('Body must be at most 250 characters'))]
    EmailValidator = [RegexValidator(regex = CustomRegex.email_regex, message = _("Must be an email)"))]

class CustomStringMaker:
    class ContentType:

        @staticmethod
        def related_name_gen(kwargs):
            name = kwargs["class_name"]
            name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
            return name

    class FilePath:

        @staticmethod
        def path_gen(kwargs):
            return f"settings.FILE_PATH_FIELD_DIRECTORY + '{kwargs['field_name']}'"

    class File:

        @staticmethod
        def path_gen(kwargs):
            return f"settings.{kwargs['field_name'].upper()}_DIRECTORY"

    class ForeignKey:

        @staticmethod
        def to_gen(kwargs):
            app_name = kwargs["app_name_destination"]
            class_model = kwargs["app_name_model_destination"]
            return app_name + '.' + class_model

        @staticmethod
        def related_name_gen(kwargs):
            # return class_name.lower()+'_'+related_name_default.lower()

            return kwargs['class_name'].lower() + "s"

    class ManyToMany:

        @staticmethod
        def to_gen(kwargs):
            return kwargs['app_name_destination'] + '.' + kwargs['app_name_model_destination']

        @staticmethod
        def related_name_gen(kwargs):
            return kwargs['class_name'].lower()+"s"

        @staticmethod
        def through_gen(kwargs):
            app_name_model_destination = kwargs['app_name_model_destination']
            app_super_model = kwargs["app_super_model"]
            class_name = kwargs["class_name"]
            result = app_super_model.capitalize() + class_name.capitalize()
            if result != app_super_model.capitalize()+app_super_model.capitalize():
                return result
            else:
                return app_super_model.capitalize()+app_name_model_destination.capitalize()
        @staticmethod
        def through_fields_gen(kwargs):
            class_name = kwargs["class_name"]
            app_model_name = kwargs["app_name_model_destination"]
            return (class_name.lower() + "_id", app_model_name.lower() + "_id")

class GetNameSpaceProperty:

    @staticmethod
    def name(self: object, teststring, scopeparent):
        if teststring == "parent":
            parent_list = []
            parent = self.parent
            while parent:
                parent_list.append(parent.name)
                parent = parent.__getattribute__("parent")
                if parent is not None:
                    if parent.name in parent_list:
                        return ValidationError("parent is recursive")
            return parent_list[::-1]
        else:
            try:
                return [objects.name for objects in self.__getattribute__(teststring).all()]
            except:
                try:
                    return [objects.name for objects in self.__getattribute__(teststring + "s").all()]
                except:
                    try:
                        temp = []
                        try:
                            items = self.__getattribute__(scopeparent).all()
                        except:
                            items = self.__getattribute__(scopeparent + "s").all()

                        for item in items:
                            temp += item.__getattribute__(teststring + "_name")
                        temp = list(set(temp))
                        return temp
                    except:
                        return []

    @staticmethod
    def count(self: object, teststring, scopeparent):
        try:
            return self.__getattribute__(teststring).count()
        except:
            try:
                return self.__getattribute__(teststring + "s").count()
            except:
                try:
                    temp = []
                    try:
                        items = self.__getattribute__(scopeparent).all()
                    except:
                        items = self.__getattribute__(scopeparent + "s").all()

                    for item in items:
                        temp += item.__getattribute__(teststring + "_name")
                    temp = len(set(temp))
                    return temp
                except:
                    return 0

    @staticmethod
    def parent(self: object, teststring, scope):
        parent_list = []
        item = self

        while item.parent:
            if scope != "nothing":
                parent_list.append(item.__getattribute__(teststring).__getattribute__(scope))
            else:
                parent_list.append(item.__getattribute__(teststring))
            item = item.parent
        if len(parent_list) > 0:
            return parent_list

        return []

    @staticmethod
    def abs_url_slug(self: object, teststring):
        return reverse(teststring + "_detail", kwargs = {
            'slug': self.slug
            })

    @staticmethod
    def abs_url_id(self: object, teststring):
        return reverse(teststring + "_detail", kwargs = {
            'pk': self.id
            })

    @staticmethod
    def abs_url_phone(self: object, teststring):
        return reverse(teststring + "_detail", kwargs = {
            'phone_number': self.phone_number
            })
